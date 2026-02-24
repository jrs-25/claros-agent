# Claros Agent

A local AI agent that uses [Claude Code](https://claude.ai/code) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to analyze eligibility cases requiring character and fitness evaluation. Given an applicant's participant ID, the agent retrieves application documents, applies the relevant regulatory framework, and produces a structured legal analysis for a human reviewer.

---

## What It Does

Eligibility determinations — whether for bar admission, insurance benefits, professional licensing, or other regulated contexts — require synthesizing multiple document types against a domain-specific legal framework. Reviewing these cases manually is time-intensive and error-prone. This agent automates the discovery and organization phase so the human reviewer can focus on judgment.

This project demonstrates an agentic workflow in which Claude Code:

1. Calls `search` to retrieve document metadata for an applicant participant ID
2. Identifies the anchor document (bar application form or equivalent) from the metadata
3. Calls `summarize_document` on the anchor to understand what issues are flagged and why
4. Selects which remaining documents are relevant to those issues
5. Calls `summarize_document` in parallel for the targeted documents
6. Compiles findings into a structured character and fitness analysis report saved to `output/`

The MCP server ships with realistic mock data modeled after actual bar admissions document types. No real applicant data is used.

---

## Reference Implementation: Bar Admissions

The current mock data and system instructions use **bar admissions character and fitness review** as the reference domain. An applicant with a prior DUI conviction and mental health treatment history is evaluated against the Board of Bar Examiners' Rules of Admission, weighing mandatory and discretionary disqualification grounds against mitigating factors.

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI agent host | Claude Code (claude-sonnet-4-6) |
| Agent–tool protocol | Model Context Protocol (MCP) over stdio |
| MCP server | Python 3, `mcp` SDK |
| Transport | `mcp.server.stdio` (subprocess, no network required) |
| Mock data | Inline Python (simulates bar admissions case management systems) |

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
    "claros-agent": {
      "command": "python3",
      "args": ["mcp_server/server.py"]
    }
  }
}
```

Update the `command` path if your Python binary is elsewhere (e.g. a virtualenv or conda env). Claude Code reads this file automatically when you open the project.

### Set the API key

`summarize_document` calls an Anthropic model internally. Set your key before starting Claude Code:

```bash
export ANTHROPIC_API_KEY=sk-...
```

### Verify the server is registered

```bash
claude mcp list
```

You should see `claros-agent` listed as an available server.

---

## Running the Agent

Open the project in Claude Code and prompt it to run a case analysis:

```
Use the claros-agent MCP tools to analyze Jordan Taylor's application.
Call search with participant_id "APP-2023-78901", then retrieve
and analyze the relevant documents, and produce a structured character
and fitness analysis summary.
```

Claude Code will:
- Call `search` → receive document metadata records
- Call `summarize_document` on the bar application to understand the case
- Call `summarize_document` in parallel for documents relevant to the flagged issues
- Compile findings into a character and fitness analysis
- Write the output to `output/`

---

## MCP Tools

One server (`claros-agent`) exposes two agent-facing tools.

#### `search`
```
Input:  { "participant_id": "APP-2023-78901", "case_type": "bar_admissions" }
Output: Document metadata records + optional case_config with extraction guidance
```

#### `summarize_document`
```
Input:  { "document_id": "taylor-001", "extraction_focus": "fitness determination, mitigating factors" }
Output: Focused summary containing only information relevant to the extraction focus
```

Requires `ANTHROPIC_API_KEY` to be set in the environment.

---

## Example Output

The file `output/jordan_taylor_CF_analysis_v4.json` shows a full run against the mock dataset. The JSON output covers:

- **Participant and applicant metadata**
- **Documents reviewed** — each with a one-sentence summary focused on the extraction lens
- **Overall summary** — ≤50 word synthesis of case status and key findings
- **Missing evidence** — documents or information referenced in the file but not present

---

## Project Structure

```
claros-agent/
├── agent/
│   └── system_instructions.md     # Active system instructions for the agent
├── mcp_server/
│   └── server.py                  # MCP server: search, summarize_document, retrieve_text_content
├── mock_data/
│   ├── search_response.json       # Mock search index
│   └── documents/                 # Mock applicant documents (taylor-001–taylor-011)
├── output/
│   └── jordan_taylor_CF_analysis_v4.json   # Example agent output (canonical schema)
├── .mcp.json                      # MCP server registration for Claude Code
├── requirements.txt               # Python dependencies
└── CLAUDE.md                      # Project instructions for Claude Code
```
