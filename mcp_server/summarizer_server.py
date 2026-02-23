import asyncio
import os

import anthropic
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("Summarizer Server")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="summarize",
            description=(
                "Send document text to an Anthropic model and return a focused summary. "
                "The caller specifies what information to extract and why via extraction_focus, "
                "and which model to use."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "document_text": {
                        "type": "string",
                        "description": "The raw text content of the document to summarize.",
                    },
                    "extraction_focus": {
                        "type": "string",
                        "description": (
                            "A description of what information to extract from the document "
                            "and why it is needed. This is passed directly to the model as "
                            "task context."
                        ),
                    },
                    "model": {
                        "type": "string",
                        "description": "The Anthropic model ID to use for summarization (e.g. claude-haiku-4-5-20251001).",
                    },
                },
                "required": ["document_text", "extraction_focus", "model"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name != "summarize":
        raise ValueError(f"Unknown tool: {name}")

    document_text = arguments["document_text"]
    extraction_focus = arguments["extraction_focus"]
    model = arguments["model"]

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return [types.TextContent(type="text", text="Error: ANTHROPIC_API_KEY environment variable not set.")]

    prompt = (
        f"{extraction_focus}\n\n"
        f"If the document contains no relevant content, state that explicitly.\n"
        f"Be concise and factual. Cite specific dates and details where present.\n\n"
        f"DOCUMENT:\n{document_text}"
    )

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return [types.TextContent(type="text", text=message.content[0].text)]


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
