#!/usr/bin/env bash
# Shared Lean environment helpers — SOURCE this, do not execute.
#
#   Sets (exported):  REPO_ROOT  LEAN_DIR  PATH (+ elan, /usr/local/bin)
#   Defines:          has()  lean_toolchain_slug()  lean_leanpath()
#                     lean_mathlib_url_fix()
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
# (e.g. a fresh web-session container): restore the olean cache from the
# `lake-cache/*` orphan branch and verify with `lean`-direct.

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
  local lp full
  lp=$(find "$REPO_ROOT/.lake/packages" "$LEAN_DIR/.lake/packages" -maxdepth 5 -type d \
         -path '*/.lake/build/lib/lean' 2>/dev/null | tr '\n' ':')
  full="${lp}${REPO_ROOT}/.lake/build/lib/lean:${LEAN_DIR}/.lake/build/lib/lean"
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
