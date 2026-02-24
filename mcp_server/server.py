import asyncio
import json
import os
from pathlib import Path

import anthropic
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("Claros Document Server")

# ---------------------------------------------------------------------------
# Data paths
# ---------------------------------------------------------------------------

_MOCK_DATA_DIR = Path(__file__).parent.parent / "mock_data"
_SEARCH_RESPONSE_FILE = _MOCK_DATA_DIR / "search_response.json"
_DOCUMENTS_DIR = _MOCK_DATA_DIR / "documents"
_CASE_CONFIG_FILE = Path(__file__).parent / "case_config.json"

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

def _load_case_config(case_type: str) -> dict | None:
    if not _CASE_CONFIG_FILE.exists():
        return None
    with _CASE_CONFIG_FILE.open() as f:
        config = json.load(f)
    entry = config.get(case_type)
    if not entry or not entry.get("extraction_focus"):
        return None
    return {
        "extraction_focus": entry["extraction_focus"],
        "primary_document_hint": entry.get("primary_document_hint", ""),
        "priority_documents": entry.get("priority_documents", []),
    }


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search",
            description=(
                "Search for documents associated with an applicant participant ID. "
                "Returns a list of document metadata records and, if case_type is provided "
                "and matches a known config, a case_config object with extraction guidance. "
                "Use summarize_document with a document_id to get a focused summary of any document."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "participant_id": {
                        "type": "string",
                        "description": "The applicant's participant/case identifier.",
                    },
                    "case_type": {
                        "type": "string",
                        "description": (
                            "Optional case type key (e.g. 'bar_admissions', "
                            "'nursing_license_reinstatement'). When provided and recognized, "
                            "the response includes a case_config object with extraction guidance."
                        ),
                    },
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
        types.Tool(
            name="summarize_document",
            description=(
                "Retrieve a document by its document_id and return a concise summary "
                "focused on content relevant to the provided extraction_focus."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "document_id": {
                        "type": "string",
                        "description": "The document_id returned by search.",
                    },
                    "extraction_focus": {
                        "type": "string",
                        "description": "The summarization lens — what to extract and why.",
                    },
                },
                "required": ["document_id", "extraction_focus"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "search":
        participant_id = arguments["participant_id"]
        index = _load_search_index()
        documents = index.get(participant_id, [])
        response: dict = {"documents": documents}
        case_type = arguments.get("case_type")
        if case_type:
            case_config = _load_case_config(case_type)
            if case_config:
                response["case_config"] = case_config
        return [types.TextContent(type="text", text=json.dumps(response, indent=2))]

    if name == "retrieve_text_content":
        document_id = arguments["document_id"]
        text = _load_document_text(document_id)
        if text is None:
            return [types.TextContent(type="text", text=f"Error: document '{document_id}' not found.")]
        return [types.TextContent(type="text", text=text)]

    if name == "summarize_document":
        document_id = arguments["document_id"]
        extraction_focus = arguments["extraction_focus"]
        text = _load_document_text(document_id)
        if text is None:
            return [types.TextContent(type="text", text=f"Error: document '{document_id}' not found.")]
        client = anthropic.AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        message = await client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            system=(
                f"You are a document summarizer. Extract only information relevant to: {extraction_focus}. "
                "Return a concise summary of one to three sentences. Do not include information outside the extraction focus."
            ),
            messages=[{"role": "user", "content": text}],
        )
        summary = message.content[0].text
        return [types.TextContent(type="text", text=summary)]

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
