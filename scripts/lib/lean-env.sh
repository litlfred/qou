#!/usr/bin/env bash
# Shared Lean environment helpers — SOURCE this, do not execute.
#
#   Sets (exported):  REPO_ROOT  LEAN_DIR  PATH (+ elan, /usr/local/bin)
#   Defines:          has()  lean_toolchain_slug()  lean_leanpath()
#                     lean_mathlib_url_fix()  mathlib_local_path()
#                     mathlib_local_available()  mathlib_enable_local_redirect()
#
# Safe under `set -u`; idempotent (re-sourcing does not double-prepend
# PATH). Referenced by scripts/lean-build-bg.sh, scripts/lean-verify.sh,
# scripts/lean-cache-restore.sh. The canonical sandbox recipe these
# encode lives in
# `.claude/skills/local/lean-environment-setup.md` and
# `docs/coordination/2026-06-08-lean-cache-architecture.md`.
#
# PRIMARY Lean path: the `paper-assistant` (folio-assistant) MCP server
# in `.mcp.json` exposes `lean_setup` / `lean_build` (Lean + Mathlib
# baked into ghcr.io/litlfred/qou/paper-assistant). Prefer those when the
# MCP server is connected. THESE scripts are the non-MCP fallback for
# sandboxes where the paper-assistant / lean-lsp MCP is unavailable
# (e.g. a fresh web-session container): restore the olean cache from a
# GitHub Release asset (tar.zst) — or legacy `lake-cache/*` orphan
# branch — and verify with `lean`-direct.

# ── REPO_ROOT (prefer git; fall back to this file's location) ─────────
if command -v git >/dev/null 2>&1 \
  && git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel >/dev/null 2>&1; then
  REPO_ROOT="$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)"
else
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fi
export REPO_ROOT

# ── LEAN_DIR: the QOU Lake package root ───────────────────────────────
LEAN_DIR="$REPO_ROOT/content/quantum-observable-universe/lean"
export LEAN_DIR

# ── PATH: elan binaries + the /usr/local/bin symlink dir ──────────────
# Non-interactive subprocesses don't get ~/.elan/bin; prepend it (once).
case ":$PATH:" in *":$HOME/.elan/bin:"*) ;; *) PATH="$HOME/.elan/bin:$PATH" ;; esac
case ":$PATH:" in *":/usr/local/bin:"*) ;; *) PATH="/usr/local/bin:$PATH" ;; esac
export PATH

# ── has CMD — true iff CMD resolves on PATH ───────────────────────────
has() { command -v "$1" >/dev/null 2>&1; }

# ── lean_toolchain_slug — cache-branch slug from the pinned toolchain ─
#    e.g. `leanprover/lean4:v4.24.0` -> `v4-24-0` (CRLF-safe).
lean_toolchain_slug() {
  cut -d: -f2 "$REPO_ROOT/lean-toolchain" | tr -d '\r' | tr . -
}

# ── lean_leanpath — LEAN_PATH for `lean`-direct verification ──────────
#    All dependency olean dirs under .lake/packages, plus the workspace
#    and QOU-package build dirs (so files importing `QOU.*` resolve).
lean_leanpath() {
  local lp papers full
  lp=$(find "$REPO_ROOT/.lake/packages" "$LEAN_DIR/.lake/packages" -maxdepth 5 -type d \
         -path '*/.lake/build/lib/lean' 2>/dev/null | tr '\n' ':')
  # Sibling paper-package build dirs (QOU / UGB / Fred2005). Without these
  # a cross-paper content-sibling import (e.g. a climax-volume-mass file
  # doing `import UGB.GrobnerShirshov.HeckeGS`) raises `unknown module
  # prefix 'UGB'` even though the olean is built in-tree. Additive: a
  # missing dir contributes nothing, distinct module roots so no clash.
  papers=$(find "$REPO_ROOT/content" -maxdepth 6 -type d \
         -path '*/lean/.lake/build/lib/lean' 2>/dev/null | tr '\n' ':')
  full="${lp}${papers}${REPO_ROOT}/.lake/build/lib/lean:${LEAN_DIR}/.lake/build/lib/lean"
  # Strip leading/trailing/duplicate colons: an empty LEAN_PATH segment
  # makes Lean also search the cwd (module-resolution conflicts).
  printf '%s' "$full" | sed -e 's/^:*//' -e 's/:*$//' -e 's/::*/:/g'
}

# ── lean_mathlib_url_fix — restore the canonical mathlib origin URL ───
#    The cache seeder leaves a local-proxy `origin` on .lake/packages/
#    mathlib; any later `lake` run then detects "URL changed", deletes
#    the package, and WIPES the ~2900 restored oleans. Resetting the URL
#    up-front avoids that documented hazard. No-op if mathlib absent.
lean_mathlib_url_fix() {
  local mdir="$REPO_ROOT/.lake/packages/mathlib"
  [ -d "$mdir/.git" ] || return 0
  git -C "$mdir" remote set-url origin \
    https://github.com/leanprover-community/mathlib4 2>/dev/null || true
}

# ── mathlib_local_path — configured local mathlib clone, absolute ─────
#    Reads `lean.local_mathlib_path` from lean-mcp.config.json (default
#    `../mathlib4`, relative to REPO_ROOT). Prints nothing and returns 1
#    if the config is unreadable.
mathlib_local_path() {
  local raw
  if has python3 && [ -f "$REPO_ROOT/lean-mcp.config.json" ]; then
    raw=$(python3 -c 'import json,sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    sys.exit(1)
print(d.get("lean", {}).get("local_mathlib_path", "../mathlib4"))'       "$REPO_ROOT/lean-mcp.config.json" 2>/dev/null) || raw="../mathlib4"
  else
    raw="../mathlib4"
  fi
  [ -n "$raw" ] || return 1
  case "$raw" in
    /*) printf '%s' "$raw" ;;
    *)  printf '%s' "$(cd "$REPO_ROOT" && cd "$(dirname "$raw")" 2>/dev/null \
          && pwd)/$(basename "$raw")" ;;
  esac
}

# ── mathlib_upstream_url — the URL the redirect replaces ──────────────
mathlib_upstream_url() {
  local raw
  if has python3 && [ -f "$REPO_ROOT/lean-mcp.config.json" ]; then
    raw=$(python3 -c 'import json,sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    sys.exit(1)
print(d.get("lean", {}).get("mathlib_git_url",
      "https://github.com/leanprover-community/mathlib4"))'       "$REPO_ROOT/lean-mcp.config.json" 2>/dev/null)       || raw="https://github.com/leanprover-community/mathlib4"
  else
    raw="https://github.com/leanprover-community/mathlib4"
  fi
  printf '%s' "$raw"
}

# ── mathlib_local_available — true iff the local clone is usable ──────
#    False (silently) when no clone is present, which is the common case
#    in a fresh container. Callers must treat that as "feature off", not
#    as an error.
mathlib_local_available() {
  local p
  p="$(mathlib_local_path)" || return 1
  [ -n "$p" ] && [ -d "$p/.git" ]
}

# ── mathlib_enable_local_redirect — point lake's fetch at the clone ───
#    `insteadOf` makes every `lake` fetch of mathlib resolve to the local
#    clone instead of GitHub, which is the difference between reusing a
#    checkout and recompiling Mathlib from source. Idempotent: git
#    replaces an existing value for the same key. No-op without a clone.
mathlib_enable_local_redirect() {
  local p url
  mathlib_local_available || return 0
  p="$(mathlib_local_path)" || return 0
  url="$(mathlib_upstream_url)"
  git config --global "url.file://${p}.insteadOf" "$url" 2>/dev/null || return 1
}
