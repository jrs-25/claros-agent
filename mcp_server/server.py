import asyncio
import json
from pathlib import Path

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("COD Document Server")

# ---------------------------------------------------------------------------
# Data paths
# ---------------------------------------------------------------------------

_MOCK_DATA_DIR = Path(__file__).parent.parent / "mock_data"
_SEARCH_RESPONSE_FILE = _MOCK_DATA_DIR / "search_response.json"
_DOCUMENTS_DIR = _MOCK_DATA_DIR / "documents"

# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def _load_search_index() -> dict[str, list[dict]]:
    with _SEARCH_RESPONSE_FILE.open() as f:
        return json.load(f)

def _load_document_text(document_id: str) -> str | None:
    path = _DOCUMENTS_DIR / f"{document_id}.txt"
    if not path.exists():
        return None
    return path.read_text()


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search",
            description=(
                "Search for documents associated with a veteran participant ID. "
                "Returns a list of document metadata records. Use retrieve_text_content "
                "with a document_id to fetch the full text of any document."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "participant_id": {
                        "type": "string",
                        "description": "The veteran's participant/ICN identifier.",
                    }
                },
                "required": ["participant_id"],
            },
        ),
        types.Tool(
            name="retrieve_text_content",
            description="Retrieve the full text content of a document by its document_id.",
            inputSchema={
                "type": "object",
                "properties": {
                    "document_id": {
                        "type": "string",
                        "description": "The document_id returned by search.",
                    }
                },
                "required": ["document_id"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "search":
        participant_id = arguments["participant_id"]
        index = _load_search_index()
        results = index.get(participant_id, [])
        return [types.TextContent(type="text", text=json.dumps(results, indent=2))]

    if name == "retrieve_text_content":
        document_id = arguments["document_id"]
        text = _load_document_text(document_id)
        if text is None:
            return [types.TextContent(type="text", text=f"Error: document '{document_id}' not found.")]
        return [types.TextContent(type="text", text=text)]

    raise ValueError(f"Unknown tool: {name}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
