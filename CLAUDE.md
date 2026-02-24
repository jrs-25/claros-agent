# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A local agent implementation for bar admissions character and fitness case analysis, backed by a single Model Context Protocol (MCP) server. The agent retrieves applicant document metadata, summarizes documents, and synthesizes findings entirely through that one server.

The same architecture and reasoning pattern applies to other eligibility domains such as VA character of discharge determinations, toxic exposure benefit reviews, and personal trauma evidence evaluations.

## Directory Structure

- `agent/` - Core agent logic and system instructions
- `mcp_server/` - MCP server implementation (see below)
- `mock_data/` - Mock applicant documents and search index used for development
- `tests/` - Test files
- `output/` - Generated output files (e.g. character and fitness analysis reports)

## MCP Server Architecture

The `mcp_server/` directory contains one server, `server.py`, which exposes all agent-facing tools.

### `mcp_server/server.py` — claros-agent Server

| Tool | Parameters | Description |
|---|---|---|
| `search` | `participant_id` (string), `case_type` (string, optional) | Returns document metadata for an applicant and optional case configuration |
| `summarize_document` | `document_id` (string), `extraction_focus` (string) | Summarizes a document focused on a specific extraction lens; calls an LLM internally |
| `retrieve_text_content` | `document_id` (string) | Returns full raw text of a document — available in the server but not exposed to the agent |

`summarize_document` requires `ANTHROPIC_API_KEY` to be set in the environment.

## Setup and Commands

No build system or package configuration has been established yet. Update this file once a language/framework is chosen and commands are available.
