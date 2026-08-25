#!/usr/bin/env bash
# Source me: sets PATH + LEAN_PATH for `lean`-direct verification against the
# RESTORED olean tree (never `lake build` — see AGENTS.md §"VERIFY a single file
# with lean-direct" and the .lake/RESTORED-NO-TRACES marker, which records that
# Lake would treat every restored olean as stale and evict the whole restore).
#
# Two different name manglings are in play and they are easy to swap:
#   * elan toolchain dir  = the descriptor with `/`->`--` and `:`->`---`,
#     DOTS KEPT           -> leanprover--lean4---v4.24.0
#   * lake-cache branch   = the version with dots->hyphens
#     slug                -> lake-cache/qou-v4-24-0
# Resolve the repo from THIS script's own location, not from $PWD: the whole
# point is to run `lean` on files outside the repo (scratch harnesses), and
# `git rev-parse` fails the moment you cd away.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
DESC="$(tr -d '\r' < "$ROOT/lean-toolchain" | tr -d '[:space:]')"        # leanprover/lean4:v4.24.0
TCDIR="$HOME/.elan/toolchains/$(printf '%s' "$DESC" | sed 's|/|--|g; s|:|---|g')"
if [ ! -x "$TCDIR/bin/lean" ]; then
  echo "lean-direct-env: no toolchain at $TCDIR" >&2
  echo "  install it per .claude/skills/local/lean-environment-setup.md" >&2
  return 1 2>/dev/null || exit 1
fi
export PATH="$TCDIR/bin:$PATH"
LP=""
for p in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do [ -d "$p" ] && LP="$LP${LP:+:}$p"; done
for p in "$ROOT"/content/*/lean/.lake/build/lib/lean; do [ -d "$p" ] && LP="$LP${LP:+:}$p"; done
export LEAN_PATH="$LP"
