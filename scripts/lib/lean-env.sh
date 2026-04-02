#!/usr/bin/env bash
# Shared Lean environment helpers for session hooks.
#
# Source this file to get:
#   - PATH set up for elan/lean/lake/uv/bun
#   - LEAN_DIR pointing to the Lean project
#   - REPO_ROOT pointing to the repo root
#   - has()          — check if a command exists
#   - lean_mode()    — detect lean availability mode (local/remote/local-degraded/none)
#   - lean_fix_hint()— suggest what to run to fix missing lean
#
# Usage:
#   source "$(dirname "$0")/lib/lean-env.sh"

# ── Paths ──────────────────────────────────────────────────────────
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LEAN_DIR="$REPO_ROOT/content/quantum-observable-universe/lean"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$HOME/.bun/bin:$PATH"

# ── Helpers ────────────────────────────────────────────────────────
has() { command -v "$1" &>/dev/null; }

# ── Remote MCP URL (from lean-mcp.config.json) ────────────────────
_lean_remote_url() {
  local config="$REPO_ROOT/lean-mcp.config.json"
  if [ -f "$config" ] && has python3; then
    local domain
    domain=$(python3 -c "import json; print(json.load(open('$config')).get('domain',''))" 2>/dev/null || true)
    [ -n "$domain" ] && echo "https://$domain/mcp"
  fi
}

# ── Lean mode detection ───────────────────────────────────────────
# Sets these variables:
#   LEAN_OK        — lean binary found
#   LEAN_VER       — lean --version output
#   UV_OK          — uv binary found
#   DEPS_OK        — lake-manifest.json present and deps match
#   CACHE_OK       — Mathlib oleans present
#   LEAN_LOCAL_READY — fully ready for local use
#   LEAN_REMOTE_OK — remote MCP reachable
#   LEAN_MODE      — local / remote / local-degraded / none
lean_detect() {
  LEAN_OK=false; LEAN_VER=""; UV_OK=false
  DEPS_OK=true; CACHE_OK=true
  LEAN_LOCAL_READY=false; LEAN_REMOTE_OK=false
  LEAN_MODE="none"

  has uv && UV_OK=true
  if has lean; then
    LEAN_OK=true
    LEAN_VER=$(lean --version 2>&1 | head -1)

    # Check deps
    if [ -f "$LEAN_DIR/lakefile.toml" ] && [ ! -f "$LEAN_DIR/lake-manifest.json" ]; then
      DEPS_OK=false
    fi
    # Check Mathlib cache
    if [ ! -d "$LEAN_DIR/.lake/packages/mathlib/.lake/build/lib" ] 2>/dev/null; then
      CACHE_OK=false
    fi

    if [ "$UV_OK" = true ] && [ "$DEPS_OK" = true ] && [ "$CACHE_OK" = true ]; then
      LEAN_LOCAL_READY=true
      LEAN_MODE="local"
    else
      LEAN_MODE="local-degraded"
    fi
  fi

  # Check remote
  local remote_url
  remote_url=$(_lean_remote_url)
  if [ -n "$remote_url" ]; then
    if curl -sf --max-time 3 -o /dev/null "$remote_url" 2>/dev/null; then
      LEAN_REMOTE_OK=true
      [ "$LEAN_MODE" = "none" ] && LEAN_MODE="remote"
    fi
  fi
}

# ── Fix hint ──────────────────────────────────────────────────────
lean_fix_hint() {
  case "$LEAN_MODE" in
    local) echo "" ;;
    local-degraded)
      if [ "$UV_OK" = false ]; then
        echo "Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
      elif [ "$DEPS_OK" = false ]; then
        echo "Run: cd content/quantum-observable-universe/lean && lake update"
      elif [ "$CACHE_OK" = false ]; then
        echo "Run: cd content/quantum-observable-universe/lean && lake exe cache get"
      fi
      ;;
    remote) echo "" ;;
    none) echo "Use paper-assistant MCP tool: lean_setup" ;;
  esac
}
