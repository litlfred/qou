# Copilot Cloud Agent — Lean MCP Quickstart

This document explains how to wire the Lean MCP server (`lean-lsp-mcp`)
into the GitHub Copilot coding agent for the **Quantum Observable Universe**
repository, so that Copilot sessions have live Lean diagnostics, goal states,
and Mathlib search available.

---

## 1. How it works

The repository ships a
[Copilot setup steps workflow](../.github/workflows/copilot-setup-steps.yml)
that runs on every Copilot session before the agent starts work. It:

1. Installs **uv** (the `uvx` runner).
2. Installs **elan** and the pinned Lean toolchain from
   [`lean-toolchain`](../lean-toolchain).
3. Warms the **Mathlib cache** (`lake exe cache get`) so the agent does not
   have to recompile Mathlib from scratch.
4. Verifies that `uvx lean-lsp-mcp --help` succeeds.

After setup, Copilot invokes `uvx lean-lsp-mcp` as a local MCP server on each
session; this gives it access to Lean diagnostics, goal inspection, LeanSearch,
and more.

---

## 2. Repository settings — MCP server config

Paste the following JSON into
**Repository Settings → Copilot → Coding agent → Model context protocol (MCP) servers**:

```json
{
  "mcpServers": {
    "lean-lsp": {
      "type": "local",
      "command": "uvx",
      "args": ["lean-lsp-mcp"],
      "tools": ["*"]
    }
  }
}
```

This config tells Copilot to start `uvx lean-lsp-mcp` and expose all of its
tools to the agent.

---

## 3. Lean tools available to the agent

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

## 4. Verifying the setup

After the setup workflow runs you can confirm the environment is healthy:

```bash
# From the repository root (inside a Copilot session):
lean --version          # should print leanprover/lean4:v4.x.x
lake --version          # should print Lake v...
uvx lean-lsp-mcp --help # should print the lean-lsp-mcp help text
```

To verify the Lake workspace builds:

```bash
lake build QOU        # quantum-observable-universe package
lake build UGB        # unital-groebner-bases package
lake build Fred2005   # fred2005-formal-groups package
```

---

## 5. Related files

| File | Purpose |
|------|---------|
| `.github/workflows/copilot-setup-steps.yml` | Setup workflow (this feature) |
| `lean-toolchain` | Pinned Lean version |
| `lakefile.toml` | Root Lake workspace |
| `.mcp.json` | Local paper-assistant MCP config (Claude Code sessions) |
| `.claude/skills/local/lean-environment-setup.md` | Claude Code Lean setup skill |
| `scripts/mcp-server/install.sh` | Full local MCP server install script |
| `deploy/setup-remote.sh` | Remote Lean MCP server setup |
