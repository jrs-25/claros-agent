# COD Agent

A local AI agent that uses [Claude Code](https://claude.ai/code) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to analyze VA Character of Discharge (COD) cases. Given a veteran's participant ID, the agent retrieves service and claims documents, applies the relevant regulatory framework, and produces a structured legal analysis.

---

## What It Does

Veterans separated with an Other Than Honorable (OTH) discharge are frequently denied VA benefits — even when the underlying misconduct was driven by undiagnosed combat-related PTSD. Reviewing these cases requires synthesizing multiple document types (DD214, service records, PTSD statements, buddy statements, prior VA decisions) against a specific statutory framework (38 C.F.R. § 3.12, the Kurta Memo).

This project demonstrates an agentic workflow in which Claude Code:

1. Calls a `search` MCP tool to retrieve document metadata for a veteran participant ID
2. Calls `retrieve_text_content` in parallel for each document
3. Analyzes the full document set — statutory bar thresholds, factors for and against, nexus timeline — without any scripted prompting
4. Produces a structured COD analysis report saved to `output/`

The MCP server ships with realistic mock data modeled after actual VA document types. No real veteran data is used.

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI agent host | Claude Code (claude-sonnet-4-6) |
| Agent–tool protocol | Model Context Protocol (MCP) over stdio |
| MCP server | Python 3, `mcp` SDK |
| Transport | `mcp.server.stdio` (subprocess, no network required) |
| Mock data | Inline Python (simulates VBMS, NPRC, DPRIS sources) |

---

## Setup

### Prerequisites

- Python 3.10+
- [Claude Code](https://claude.ai/code) installed and authenticated

### Install dependencies

```bash
pip install mcp
```

### Configure the MCP server

The `.mcp.json` file at the repo root registers the MCP server with Claude Code:

```json
{
  "mcpServers": {
    "cod-agent": {
      "command": "python3",
      "args": ["mcp_server/server.py"]
    }
  }
}
```

Update the `command` path if your Python binary is elsewhere (e.g. a virtualenv or conda env). Claude Code reads this file automatically when you open the project.

### Verify the server is registered

```bash
claude mcp list
```

You should see `cod-agent` listed as an available server.

---

## Running the Agent

Open the project in Claude Code and prompt it to run a case analysis:

```
Use the cod-agent MCP tools to analyze Samuel Murphy's case.
Call search with participant_id "1012345678V123456", then retrieve
and analyze the relevant documents, and produce a structured COD
analysis summary.
```

Claude Code will:
- Call `search` → receive 5 document metadata records
- Call `retrieve_text_content` for each document (in parallel)
- Synthesize the full record into a COD analysis
- Write the output to `output/`

---

## MCP Tools

The server exposes two tools:

### `search`
```
Input:  { "participant_id": "1012345678V123456" }
Output: Array of document metadata records (id, type, title, date, source)
```

### `retrieve_text_content`
```
Input:  { "document_id": "DOC001" }
Output: Full text of the document
```

---

## Example Output

The file `output/cod_analysis_murphy_samuel.md` shows a full run against the mock dataset. Highlights:

**Statutory bar finding:**
> The 107-day AWOL does not trigger the 38 C.F.R. § 3.12(c)(6) 180-day bar. The case turns entirely on the § 3.12(d) totality-of-service analysis.

**Kurta Memo assessment:**
> The temporal sequence — combat trauma (Nov 2001) → symptom onset (Apr 2002) → failed treatment (Nov 2002) → AWOL (Feb 2003) — is consistent with a Kurta Memo nexus argument. The criteria are substantially met.

**Overall finding:**
> Strong factual basis for a favorable COD determination, but the initial denial stands because a formal clinical nexus opinion has not yet been filed. Priority action: obtain nexus letter before the one-year evidence window closes (June 2024).

---

## Project Structure

```
cod-agent-local/
├── mcp_server/
│   └── server.py          # MCP server with mock veteran documents
├── output/
│   └── cod_analysis_murphy_samuel.md   # Example agent output
├── .mcp.json              # MCP server registration for Claude Code
├── requirements.txt       # Python dependencies
└── CLAUDE.md              # Project instructions for Claude Code
```
