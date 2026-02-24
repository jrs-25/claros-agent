# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A local agent implementation for bar admissions character and fitness case analysis, backed by a two-server Model Context Protocol (MCP) architecture. The agent retrieves applicant documents via one MCP server and summarizes them via a separate, general-purpose summarization server.

The same architecture and reasoning pattern applies to other eligibility domains such as VA character of discharge determinations, toxic exposure benefit reviews, and personal trauma evidence evaluations.

## Directory Structure

- `agent/` - Core agent logic and system instructions
- `mcp_server/` - MCP server implementations (see below)
- `mock_data/` - Mock applicant documents and search index used for development
- `tests/` - Test files
- `output/` - Generated output files (e.g. character and fitness analysis reports)

## MCP Server Architecture

The `mcp_server/` directory contains two servers with distinct responsibilities:

### `mcp_server/server.py` — Data Retrieval Server
Pure data layer. No LLM calls, no external API dependencies.

| Tool | Parameters | Description |
|---|---|---|
| `search` | `participant_id` (string) | Returns document metadata for an applicant by application/participant ID |
| `retrieve_text_content` | `document_id` (string) | Returns the full raw text of a document |

### `mcp_server/summarizer_server.py` — Summarization Server
General-purpose LLM summarization. Caller controls the prompt focus and model.

| Tool | Parameters | Description |
|---|---|---|
| `summarize` | `document_text` (string), `extraction_focus` (string), `model` (string) | Sends document text to an Anthropic model and returns a focused summary. `extraction_focus` is the task context passed to the model describing what to extract and why. |

The `summarize` tool requires `ANTHROPIC_API_KEY` to be set in the environment. The data retrieval server has no such dependency.

## Setup and Commands

No build system or package configuration has been established yet. Update this file once a language/framework is chosen and commands are available.
