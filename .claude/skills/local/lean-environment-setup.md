---
name: lean-environment-setup
roles: [collaborator, owner]
description: >
  Sets up and troubleshoots the Lean 4 environment for Claude Code sessions.
  Ensures elan, lake, lean are installed so the paper-assistant MCP's Lean
  tools are operational. Handles sandboxed/cloud environments where downloads
  may be restricted.
allowed-tools: Read Edit Bash Grep Glob
---

# Lean Environment Setup

## Architecture

All MCP functionality — including Lean tools — is served through a single
`paper-assistant` MCP server (`./scripts/start-folio-assistant.sh`). There is
**no separate lean-lsp MCP entry**. The paper-assistant detects lean/lake
on the PATH and enables Lean tools automatically.

## When to Use This Skill

- At session start when `session-status.sh` reports Lean as unavailable
- When paper-assistant Lean tools fail with "No such file or directory: 'lake'"
- When a user says "set up Lean" or "install Lean"

## Prerequisites

The paper-assistant's Lean tools require these on the PATH:

1. **elan** — Lean toolchain manager (`~/.elan/bin/`)
2. **lean** — the Lean compiler (installed via elan)
3. **lake** — the Lean build tool (installed with lean)
4. **uv** — Python package manager (optional, for uvx-based tools)
5. **ripgrep** — for local symbol search (optional)

## Setup Procedure

### Step 1: Check current state

Use the `lean_status` MCP tool. It reports the current mode
(local/remote/local-degraded/none) and what's missing.

### Step 2: Install Lean toolchain

Use the `lean_setup` MCP tool. It handles the full installation:
elan, lean, lake, uv, ripgrep, lake update, Mathlib cache, and build.
Safe to re-run — skips already-installed components.

If `lean_setup` fails (e.g., 403 errors from network restrictions in
sandboxed environments), proceed to Step 3.

### Step 3: Diagnose network restrictions

In sandboxed/cloud environments (GitHub Codespaces, Claude Code cloud,
CI runners), outbound HTTPS to `github.com` or `raw.githubusercontent.com`
may be blocked. Test:

```bash
curl -sSf --max-time 5 https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /dev/null && echo "OK" || echo "BLOCKED"
curl -sSf --max-time 5 https://github.com/leanprover/lean4/releases -o /dev/null && echo "OK" || echo "BLOCKED"
```

If blocked, local Lean installation is impossible. Inform the user that
Lean tools require running Claude Code locally where lean/lake are installed.

### Step 4: Verify Lean tools via paper-assistant

After setup, verify with the `lean_status` MCP tool. If mode is
`local`, Lean is fully operational.

## Docker-based setup (offline)

If the paper-assistant Docker image is available, all tools (Lean, TeX,
Bun) are pre-installed and ready to use without any network access:

```bash
# Pull once (requires network)
docker pull ghcr.io/litlfred/qou/paper-assistant:latest

# Run with repo mounted — full toolchain available
docker run --rm --entrypoint "" \
  -v $(pwd):/work -w /work \
  ghcr.io/litlfred/qou/paper-assistant:latest \
  bash -c "lean --version && lake --version && pdflatex --version | head -1"
```

The render hooks (`render-on-change.sh`, `render-pre-commit.sh`) auto-detect
Docker and use the image as a fallback when local tools are missing. See
`scripts/lib/docker-tex.sh` for the helper library.

## Fallback: Structural Analysis Without Lean

When Lean is not installed, agents can still:

- Read `.lean` files with the Read tool
- Search for `sorry` with Grep
- Validate content object schemas via `paper-assistant` MCP
- Check cross-references between `.ts` manifests and `.lean` files
- Verify naming conventions (label → declaration mapping)
- Audit `status` fields against file contents

What agents **cannot** do without Lean:

- Type-check proofs
- Get goal states at positions
- Search Mathlib (leansearch, loogle)
- Verify axiom dependencies
- Get autocompletions or hover info

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| "No such file or directory: 'lake'" | lean not on PATH | `export PATH="$HOME/.elan/bin:$PATH"` or install elan |
| elan install 403 | Network restrictions | Run Claude Code locally where lean is installed |
| "lake update" hangs | Git fetch blocked | Check `git ls-remote` works for mathlib4 |
| Lean tools timeout | Workspace not built | Run `lake build` at the **repo root** (root workspace builds all paper packages) |
| "toolchain not installed" | Wrong lean version | `elan toolchain install $(cat lean-toolchain)` from the repo root |
| paper-assistant shows `✗ lean` | lean not on PATH | Add `$HOME/.elan/bin` to PATH in shell profile |

## PATH Configuration

All session scripts source `scripts/lib/lean-env.sh`, which sets:

```bash
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$HOME/.bun/bin:$PATH"
```

The paper-assistant inherits the shell's PATH when launched via `.mcp.json`.
Ensure elan's bin directory is on the PATH in the shell profile
(`~/.bashrc`, `~/.zshrc`, or `~/.profile`).
