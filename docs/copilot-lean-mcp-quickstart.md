# Copilot + Claude Code MCP Quickstart

This document explains how to wire MCP servers for both:

1. **GitHub Copilot coding agent** (cloud sessions), and
2. **Claude Code** (local `.mcp.json` sessions),

in the **Quantum Observable Universe** repository.

It covers:

- Lean tooling (`lean-lsp-mcp`) for proof diagnostics/navigation.
- Literature discovery/retrieval MCPs:
  - `paper-search-mcp` (`openags/paper-search-mcp`)
  - `openalex-mcp-server` package from `LeoGitGuy/alex-paper-search-mcp`
  - `mcp-scholar` (`renyumeng1/mcp_scholar`)

---

## 1. Copilot cloud-agent setup (`copilot-setup-steps.yml`)

The repository ships a
[Copilot setup steps workflow](../.github/workflows/copilot-setup-steps.yml)
that runs on every Copilot session before the agent starts work. It:

1. Installs **uv** (the `uvx` runner).
2. Installs **elan** and the pinned Lean toolchain from
   [`lean-toolchain`](../lean-toolchain).
3. Warms the **Mathlib cache** (`lake exe cache get`) so the agent does not
   have to recompile Mathlib from scratch.
4. Verifies that `uvx lean-lsp-mcp --help` succeeds.

After setup, Copilot can invoke `uvx`-backed MCP servers (including `lean-lsp-mcp`
and literature MCPs) from repository MCP settings.

---

## 2. Copilot repository settings — MCP server config

Paste the following JSON into:
**Repository Settings → Copilot → Coding agent → Model context protocol (MCP) servers**:

```json
{
  "mcpServers": {
    "lean-lsp": {
      "type": "local",
      "command": "uvx",
      "args": ["lean-lsp-mcp"],
      "tools": ["*"]
    },
    "paper-search-mcp": {
      "type": "local",
      "command": "uvx",
      "args": ["paper-search-mcp"],
      "tools": ["*"]
    },
    "openalex-paper-search": {
      "type": "local",
      "command": "uvx",
      "args": ["openalex-mcp-server"],
      "tools": ["*"]
    },
    "mcp-scholar": {
      "type": "local",
      "command": "uvx",
      "args": ["mcp-scholar"],
      "tools": ["*"]
    }
  }
}
```

This config tells Copilot to start all four MCP servers via `uvx` and expose
their tools to the agent.

### Copilot environment variables (recommended)

For stable behavior and better rate limits, set these in
**Settings → Environments → `copilot` → Environment variables / secrets**:

- `PAPER_SEARCH_MCP_UNPAYWALL_EMAIL` (recommended)
- `PAPER_SEARCH_MCP_CORE_API_KEY` (optional)
- `PAPER_SEARCH_MCP_SEMANTIC_SCHOLAR_API_KEY` (optional)
- `PAPER_SEARCH_MCP_GOOGLE_SCHOLAR_PROXY_URL` (optional)
- `OPENALEX_EMAIL` (recommended)
- `OPENALEX_API_KEY` (optional)

---

## 3. Claude Code local setup (`.mcp.json`)

This repository now includes the same literature MCP setup for Claude Code in:

- [`.mcp.json`](../.mcp.json)

Configured servers:

1. `paper-assistant`
2. `lean-lsp`
3. `paper-search-mcp`
4. `openalex-paper-search`
5. `mcp-scholar`

### Prerequisites for Claude Code

- Install `uv` so `uvx` is available:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Export needed API/environment variables from your shell before launching Claude Code.
  `.mcp.json` intentionally does not hard-code secrets.

Example:

```bash
export PAPER_SEARCH_MCP_UNPAYWALL_EMAIL="you@example.com"
export OPENALEX_EMAIL="you@example.com"
```

This gives Claude Code parity with Copilot for literature retrieval and Lean tooling MCP access.

---

## 4. Lean tools available to the agent

Once the MCP server is running, the agent can use:

| Tool | Purpose |
|------|---------|
| `lean_diagnostic_messages` | Check errors / warnings in a `.lean` file |
| `lean_goal` | Inspect the proof goal at a cursor position |
| `lean_hover` | Hover docs for a symbol |
| `lean_leansearch` | Natural-language search over Mathlib |
| `lean_loogle` | Type-signature search over Mathlib |
| `lean_multi_attempt` | Try multiple tactics and return the first that works |
| `lean_verify` | Audit axiom dependencies of a declaration |

For the full list see the
[lean-lsp-mcp README](https://github.com/oOo0oOo/lean-lsp-mcp).

---

## 5. Verifying the setup

After the setup workflow runs you can confirm the environment is healthy:

```bash
# From the repository root (inside a Copilot session):
lean --version          # should print leanprover/lean4:v4.x.x
lake --version          # should print Lake v...
uvx lean-lsp-mcp --help # should print the lean-lsp-mcp help text
uvx paper-search-mcp --help
uvx openalex-mcp-server --help
uvx mcp-scholar --help
```

To verify the Lake workspace builds:

```bash
lake build QOU        # quantum-observable-universe package
lake build UGB        # unital-groebner-bases package
lake build Fred2005   # fred2005-formal-groups package
```

---

## 6. Related files

| File | Purpose |
|------|---------|
| `.github/workflows/copilot-setup-steps.yml` | Setup workflow (this feature) |
| `lean-toolchain` | Pinned Lean version |
| `lakefile.toml` | Root Lake workspace |
| `.mcp.json` | Local paper-assistant MCP config (Claude Code sessions) |
| `.claude/skills/local/lean-environment-setup.md` | Claude Code Lean setup skill |
| `scripts/mcp-server/install.sh` | Full local MCP server install script |
| `deploy/setup-remote.sh` | Remote Lean MCP server setup |
