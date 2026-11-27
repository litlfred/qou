#!/usr/bin/env bash
# Restore the lean-direct refresh addon over the base olean seed.
#
#   scripts/lean-restore-refresh-oleans.sh [--force]
#
# The base seed (lake-cache/qou-<slug>, restored by lean-cache-restore.sh) was
# taken at a792c46 and is ~900 modules behind current source.  The addon
# lake-cache/qou-<slug>-lean-direct-refresh holds every QOU/UGB olean rebuilt
# lean-direct from current source (seeded 2026-11-19 from qou c4a0c309a: 3251
# oleans + 3324 `.srcsha` stamps, ~974 MB in 11 parts).  Without it a fresh
# session rebuilds those ~900 modules, about 2 h.
#
# Paths in the tarball are repo-relative and already `folio/...`.
#
# Idempotent: the addon commit it last applied is recorded in
# .lake/lean-refresh-addon.sha; a second run with the same head does nothing.
# The fetch goes into a THROWAWAY repo so `rm -rf` reclaims the ~1 GB of
# objects (fetching into .git does not; AGENTS.md records a session bricked
# that way).
#
# NOT a Lake restore.  Plain oleans, no fresh `.trace`: verify with lean-direct
# (scripts/lean-direct-cone.sh decides freshness from the `.srcsha` stamps);
# never `lake build` afterwards.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FORCE=false
[ "${1:-}" = --force ] && FORCE=true
REPO_ROOT="$ROOT" source "$ROOT/scripts/lib/lake-cache-family.sh"
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)
BRANCH="$(lake_cache_read_branch "qou-${SLUG}-lean-direct-refresh")"
URL="$(git -C "$ROOT" remote get-url origin)"
MARK="$ROOT/.lake/lean-refresh-addon.sha"

HEAD=$(git ls-remote "$URL" "refs/heads/$BRANCH" 2>/dev/null | cut -f1)
if [ -z "$HEAD" ]; then
  echo "lean-restore-refresh: no $BRANCH on origin; skipping (the base seed still works, just older)." >&2
  exit 0
fi
if ! $FORCE && [ -f "$MARK" ] && [ "$(cat "$MARK")" = "$HEAD" ]; then
  echo "lean-restore-refresh: $BRANCH ($HEAD) already applied."
  exit 0
fi

T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT INT TERM
git init -q "$T"
git -C "$T" remote add origin "$URL"
git -C "$T" fetch --depth=1 -q origin "$BRANCH"
C=$(git -C "$T" rev-parse FETCH_HEAD)
parts=$(git -C "$T" ls-tree --name-only "$C" | grep '^lake-oleans\.tgz\.part' | sort)
[ -n "$parts" ] || { echo "lean-restore-refresh: no lake-oleans.tgz.part* on $BRANCH" >&2; exit 1; }
for p in $parts; do git -C "$T" show "$C:$p"; done | tar xzf - -C "$ROOT" --unlink-first
mkdir -p "$ROOT/.lake"
echo "$C" > "$MARK"
n=$(find "$ROOT"/folio/*/lean/.lake/build -name '*.srcsha' 2>/dev/null | wc -l | tr -d ' ')
echo "lean-restore-refresh: applied $BRANCH ($C); $n .srcsha stamps present."
