# Claros Agent

A local AI agent that uses [Claude Code](https://claude.ai/code) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to analyze eligibility cases requiring character and fitness evaluation. Given an applicant's participant ID, the agent retrieves application documents, applies the relevant regulatory framework, and produces a structured legal analysis for a human reviewer.

---

## What It Does

Eligibility determinations — whether for bar admission, VA benefits, professional licensing, or other regulated contexts — require synthesizing multiple document types against a domain-specific legal framework. Reviewing these cases manually is time-intensive and error-prone. This agent automates the discovery and organization phase so the human reviewer can focus on judgment.

This project demonstrates an agentic workflow in which Claude Code:

1. Calls a `search` MCP tool to retrieve document metadata for an applicant participant ID
2. Calls `retrieve_text_content` in parallel for each document
3. Calls `summarize` in parallel for each document, passing a uniform extraction focus
4. Compiles the summaries into a structured character and fitness analysis report saved to `output/`

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

The `.mcp.json` file at the repo root registers the MCP servers with Claude Code:

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
- Call `retrieve_text_content` for each document (in parallel)
- Synthesize the full record into a character and fitness analysis
- Write the output to `output/`

---

## MCP Tools

Two servers expose three tools in total.

### claros-agent (data retrieval)

#### `search`
```
Input:  { "participant_id": "APP-2023-78901" }
Output: Array of document metadata records (id, type, title, date, source)
```

#### `retrieve_text_content`
```
Input:  { "document_id": "DOC001" }
Output: Full text of the document
```

### claros-summarizer (LLM summarization)

#### `summarize`
```
Input:  { "document_text": "...", "extraction_focus": "...", "model": "claude-haiku-4-5-20251001" }
Output: Focused summary containing only information relevant to the extraction focus
```

Requires `ANTHROPIC_API_KEY` to be set in the environment.

---

## Example Output

The file `output/jordan_taylor_CF_analysis.md` shows a full run against the mock dataset. The report covers:

- **Fitness determination status** — current Board determination, issue code, and deferral reason
- **Disciplinary history** — criminal and academic incidents with dispositions, sourced to specific document IDs
- **Mental health record** — diagnosis, treatment duration, clinician assessment
- **Mitigating factors** — full enumeration with document citations
- **Character evidence** — referee observations keyed to each reference document
- **Outstanding requirements** — items still needed before a final determination can be issued
- **Structured JSON output** — machine-readable summary of all findings

---

## Project Structure

```
claros-agent/
├── agent/
│   └── system_instructions.md     # Active system instructions for the agent
├── mcp_server/
│   ├── server.py                  # MCP server with mock applicant documents
│   └── summarizer_server.py       # LLM summarization server
├── mock_data/
│   ├── search_response.json       # Mock search index
│   └── documents/                 # Mock applicant documents (DOC001–DOC008)
├── output/
│   └── jordan_taylor_CF_analysis.md        # Example agent output
├── .mcp.json                      # MCP server registration for Claude Code
├── requirements.txt               # Python dependencies
└── CLAUDE.md                      # Project instructions for Claude Code
```
