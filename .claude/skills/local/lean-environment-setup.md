---
name: lean-environment-setup
roles: [collaborator, owner]
description: >
  Sets up and troubleshoots the Lean 4 environment for Claude Code sessions.
  Ensures elan, lake, lean, and the lean-lsp MCP server are operational.
  Handles both local and sandboxed/cloud environments where downloads may be
  restricted.
allowed-tools: Read Edit Bash Grep Glob
---

# Lean Environment Setup

## When to Use This Skill

- At session start when `session-status.sh` reports Lean as unavailable
- When `lean-lsp` MCP tools fail with "No such file or directory: 'lake'"
- When a user says "set up Lean" or "install Lean"
- When switching between local and remote MCP modes

## Prerequisites

The Lean MCP (`lean-lsp-mcp`) requires:

1. **elan** — Lean toolchain manager (`~/.elan/bin/`)
2. **lean** — the Lean compiler (installed via elan)
3. **lake** — the Lean build tool (installed with lean)
4. **uv** — Python package manager (for `uvx lean-lsp-mcp`)
5. **ripgrep** — for `lean_local_search` (optional)

## Setup Procedure

### Step 1: Check current state

```bash
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"
which elan lean lake uv 2>/dev/null
cat /tmp/qou-lean-build-status.json 2>/dev/null
```

### Step 2: Attempt local installation

Run the setup script if lean/elan are missing:

```bash
./scripts/setup-lean-mcp.sh
```

If the script fails (e.g., 403 errors from network restrictions in
sandboxed environments), proceed to Step 3.

### Step 3: Diagnose network restrictions

In sandboxed/cloud environments (GitHub Codespaces, Claude Code cloud,
CI runners), outbound HTTPS to `github.com` or `raw.githubusercontent.com`
may be blocked. Test:

```bash
curl -sSf --max-time 5 https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /dev/null && echo "OK" || echo "BLOCKED"
curl -sSf --max-time 5 https://github.com/leanprover/lean4/releases -o /dev/null && echo "OK" || echo "BLOCKED"
```

If blocked, local Lean installation is impossible. Proceed to Step 4.

### Step 4: Switch to remote MCP

If local installation fails, configure the remote MCP server:

1. Check if remote is reachable:
   ```bash
   DOMAIN=$(python3 -c "import json; print(json.load(open('lean-mcp.config.json')).get('domain',''))" 2>/dev/null)
   curl -sf --max-time 3 "https://$DOMAIN/mcp" && echo "REACHABLE" || echo "UNREACHABLE"
   ```

2. If reachable, update `.mcp.json` to use remote:
   ```json
   {
     "mcpServers": {
       "lean-lsp": {
         "url": "https://lean.litlfred.org/mcp"
       },
       "paper-assistant": {
         "command": "./scripts/start-assistant.sh",
         "args": ["--stdio"]
       }
     }
   }
   ```

3. If neither local nor remote works, inform the user that Lean MCP tools
   are unavailable. Structural analysis (reading `.lean` files, checking
   schemas, cross-refs) can still proceed without compilation.

### Step 5: Verify MCP connectivity

After setup, test that MCP tools work:

```
lean_diagnostic_messages on any .lean file in lean-archive/
```

If this returns results (even errors), the MCP is operational.

## MCP Configuration Reference

The `.mcp.json` file supports two modes for `lean-lsp`:

### Local mode (default — requires lean installed)

```json
{
  "lean-lsp": {
    "command": "uvx",
    "args": ["lean-lsp-mcp", "--project", "./lean-archive"],
    "cwd": "."
  }
}
```

Or via the wrapper script:

```json
{
  "lean-lsp": {
    "command": "./scripts/start-lean-mcp.sh",
    "args": [],
    "cwd": "."
  }
}
```

### Remote mode (no local lean needed)

```json
{
  "lean-lsp": {
    "url": "https://lean.litlfred.org/mcp"
  }
}
```

## Fallback: Structural Analysis Without Lean

When Lean MCP is unavailable, agents can still:

- Read `.lean` files with the Read tool
- Search for `sorry` with Grep
- Validate content object schemas via `paper-assistant` MCP
- Check cross-references between `.ts` manifests and `.lean` files
- Verify naming conventions (label → declaration mapping)
- Audit `status` fields against file contents

What agents **cannot** do without Lean MCP:

- Type-check proofs
- Get goal states at positions
- Search Mathlib (leansearch, loogle)
- Run `lean_verify` for axiom audits
- Get autocompletions or hover info

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| "No such file or directory: 'lake'" | lean not on PATH | `export PATH="$HOME/.elan/bin:$PATH"` or install elan |
| "No valid Lean project path found" | MCP can't find lakefile | Ensure `lean-archive/lakefile.toml` exists, set `--project` arg |
| elan install 403 | Network restrictions | Use remote MCP mode |
| "lake update" hangs | Git fetch blocked | Check `git ls-remote` works for mathlib4 |
| MCP tools return `isError: true` | LSP timeout | Run `lake build` first, or increase timeout |
| "toolchain not installed" | Wrong lean version | `cd lean-archive && elan toolchain install $(cat lean-toolchain)` |

## PATH Configuration

The lean-build-bg.sh and session-status.sh scripts both set:

```bash
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"
```

If the MCP server is launched via `.mcp.json` command, it inherits the
shell's PATH. Ensure elan's bin directory is on the PATH in the shell
profile (`~/.bashrc`, `~/.zshrc`, or `~/.profile`).
