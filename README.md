# Claros Agent

A local AI agent that uses [Claude Code](https://claude.ai/code) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to analyze eligibility cases requiring character and fitness evaluation. Given an applicant's participant ID, the agent retrieves application documents, applies the relevant regulatory framework, and produces a structured legal analysis for a human reviewer.

---

## What It Does

Eligibility determinations — whether for bar admission, VA benefits, professional licensing, or other regulated contexts — require synthesizing multiple document types against a domain-specific legal framework. Reviewing these cases manually is time-intensive and error-prone. This agent automates the discovery and organization phase so the human reviewer can focus on judgment.

This project demonstrates an agentic workflow in which Claude Code:

1. Calls a `search` MCP tool to retrieve document metadata for an applicant participant ID
2. Calls `retrieve_text_content` in parallel for each document
3. Analyzes the full document set — mandatory and discretionary disqualification thresholds, factors for and against, mitigating factors timeline — without any scripted prompting
4. Produces a structured character and fitness analysis report saved to `output/`

The MCP server ships with realistic mock data modeled after actual bar admissions document types. No real applicant data is used.

---

## Reference Implementation: Bar Admissions

The current mock data and system instructions use **bar admissions character and fitness review** as the reference domain. An applicant with a prior DUI conviction and mental health treatment history is evaluated against the Board of Bar Examiners' Rules of Admission, weighing mandatory and discretionary disqualification grounds against mitigating factors.

---

## Applying This Pattern to Other Domains

The same architecture supports any eligibility workflow that follows the structure:

> **trigger document** → **disqualification threshold analysis** → **mitigating factors** → **recommendation summary for human reviewer**

| Domain | Trigger Document | Disqualification Framework | Mitigating Factors |
|---|---|---|---|
| Bar admissions | Bar application form | Rules of Admission (mandatory / discretionary) | Rehabilitation, character references, mental health treatment |
| VA character of discharge | DD-214 | 38 C.F.R. § 3.12 (statutory / regulatory bar) | Service-connected mental health, combat record, compelling circumstances |
| VA toxic exposure | Service records | PACT Act eligibility criteria | Deployment records, nexus evidence, personal statements |
| Personal trauma evidence | Incident report / treatment records | Regulatory benefit threshold | Medical records, lay statements, timeline evidence |

To adapt to a new domain: update the system instructions in `agent/`, replace the mock data in `mock_data/`, and adjust the `extraction_focus` passed to the `summarize` tool.

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

The server exposes two tools:

### `search`
```
Input:  { "participant_id": "APP-2023-78901" }
Output: Array of document metadata records (id, type, title, date, source)
```

### `retrieve_text_content`
```
Input:  { "document_id": "DOC001" }
Output: Full text of the document
```

---

## Example Output

The file `output/fitness_analysis_taylor_jordan.md` shows a full run against the mock dataset. Highlights:

**Mandatory disqualification finding:**
> The DUI conviction (single offense, misdemeanor) does not trigger a mandatory disqualification under the Rules of Admission. The case turns on the discretionary disqualification analysis and the totality of the applicant's character record.

**Mitigating factors assessment:**
> The temporal sequence — law school stress (2020) → DUI incident (Aug 2020) → voluntary treatment (Oct 2020) → sustained rehabilitation (2020–present) — is consistent with a mitigating factors argument. Character references and clean record since the incident substantially support admission.

**Overall finding:**
> Strong factual basis for a favorable fitness determination, but the initial deferral stands because a formal rehabilitation attestation from the treating therapist has not yet been filed. Priority action: obtain character reference letter from Dr. Reyes before the one-year evidence submission window closes.

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
│   └── fitness_analysis_taylor_jordan.md   # Example agent output
├── .mcp.json                      # MCP server registration for Claude Code
├── requirements.txt               # Python dependencies
└── CLAUDE.md                      # Project instructions for Claude Code
```
