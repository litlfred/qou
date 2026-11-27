#!/usr/bin/env bash
# gen-block-jsonld.sh -- qou's wrapper around the platform's block-node
# generator (cat-harness-tools/pipeline/gen-block-jsonld.ts).
#
# WHY A WRAPPER (owner, 2026-11-25: "day's photon PRs left 11 knowledge-graph
# nodes stale or missing ... improve process"). Every content block has a
# generated `<block>.jsonld` sibling, and the site build (`site:document`)
# refuses a missing or stale one. The generator picks each node's @context from
# the layer that holds the output file, and it finds the layers by looking
# beside its OWN install (`dirname(HARNESS_ROOT)`):
#
#   root mounts (index.lock.json replayed at the repo root)
#       -> it sees qou.json -> qou's context    -> 0 nodes change on main
#   light platform (scripts/mount-platform-lite.sh, under folio-assistant/)
#       -> it sees no qou.json -> the platform's shared default context
#       -> ALL ~3,900 qou nodes change
#
# So on the light platform the generator cannot be used at all, and agents
# rightly skipped it, leaving their nodes stale. This wrapper makes the wrong
# platform impossible to mistake: it refuses unless the generator runs from the
# root mounts, refuses a write that would rewrite more than a handful of nodes,
# and refuses any node carrying the shared default context.
#
# Usage:
#   scripts/gen-block-jsonld.sh --check [--paper P]...   # gate: exit 1 if stale
#   scripts/gen-block-jsonld.sh [--paper P]...           # regenerate
#   scripts/gen-block-jsonld.sh --force ...              # allow a large rewrite
# No --paper: every paper (folio/<p>/<p>.ts).
#
# Env: QOU_JSONLD_MAX_REWRITE (default 200) -- the largest write allowed
#      without --force. A normal PR touches tens; a wrong platform, thousands.
#
# Exit: 0 ok; 1 stale (--check); 3 wrong/absent platform; 4 refused write.
set -uo pipefail
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel) || exit 3
cd "$ROOT" || exit 3

check=0 force=0 papers=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --check) check=1 ;;
    --force) force=1 ;;
    --paper) papers+=("$2"); shift ;;
    --paper=*) papers+=("${1#--paper=}") ;;
    *) echo "gen-block-jsonld.sh: unknown argument $1" >&2; exit 2 ;;
  esac
  shift
done
MAX=${QOU_JSONLD_MAX_REWRITE:-200}
DEFAULT_CTX='https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld'

GEN="$ROOT/cat-harness-tools/pipeline/gen-block-jsonld.ts"
if [ ! -f "$ROOT/qou.json" ] || [ ! -f "$GEN" ] || [ ! -d "$ROOT/node_modules" ] \
   || [ ! -d "$ROOT/folio-assistant-sci" ]; then
  cat >&2 <<EOF
gen-block-jsonld.sh: REFUSED -- the generator is not running from the root
  layer mounts (index.lock.json), so it would emit the platform's shared
  default @context and rewrite every qou node. The light platform under
  folio-assistant/ (mount-platform-lite.sh) cannot generate qou's nodes.
  Fix (about 40 s, about 500 MB, measured 2026-11-25):
    bash .github/mount-from-lock.sh && bun install
  then re-run this script.
EOF
  exit 3
fi
# builders.ts imports through folio-assistant/; point it at the root mounts.
. "$ROOT/scripts/lib/platform-root.sh" && qou_platform_shim "$ROOT" >/dev/null

if [ "${#papers[@]}" -eq 0 ]; then
  for d in folio/*/; do p=$(basename "$d"); [ -f "folio/$p/$p.ts" ] && papers+=("$p"); done
fi

run() { bun run "$GEN" "$@"; }

# Count what --check says is stale, per paper.
stale_total=0 rc=0
for p in "${papers[@]}"; do
  out=$(run --check --paper "$p" 2>&1); s=$?
  n=$(printf '%s\n' "$out" | sed -nE 's/^([0-9]+) \.jsonld sibling\(s\) are stale or missing:.*/\1/p' | head -1)
  n=${n:-0}
  if [ "$s" -ne 0 ] && [ "$n" -eq 0 ]; then
    printf '%s\n' "$out" | tail -20 >&2
    echo "gen-block-jsonld.sh: generator failed on $p (exit $s)" >&2
    rc=1
  fi
  stale_total=$((stale_total + n))
  if [ "$check" -eq 1 ]; then
    if [ "$n" -gt 0 ]; then
      printf '%s\n' "$out" | sed -n '/are stale or missing/,$p' | head -45
      echo "  -> regenerate: scripts/gen-block-jsonld.sh --paper $p"
      rc=1
    else
      printf '%s\n' "$out" | grep -E 'up to date' | sed "s/^/[$p] /"
    fi
  fi
done
[ "$check" -eq 1 ] && exit "$rc"

if [ "$stale_total" -gt "$MAX" ] && [ "$force" -eq 0 ]; then
  echo "gen-block-jsonld.sh: REFUSED -- $stale_total node(s) would be rewritten (limit $MAX)." >&2
  echo "  A content change touches tens. Thousands means a wrong platform or a" >&2
  echo "  platform re-pin; check index.lock.json, then re-run with --force if intended." >&2
  exit 4
fi
for p in "${papers[@]}"; do run --paper "$p" >/dev/null 2>&1 || rc=1; done

# Last guard: no qou node may carry the shared default context.
bad=$(git diff --name-only -- 'folio/*.jsonld' | xargs -r grep -l -m1 -F "\"$DEFAULT_CTX\"" 2>/dev/null)
if [ -n "$bad" ]; then
  echo "gen-block-jsonld.sh: REFUSED -- these nodes now carry the shared default" >&2
  echo "  @context ($DEFAULT_CTX), i.e. the wrong platform wrote them:" >&2
  printf '    %s\n' $bad | head -20 >&2
  echo "  Undo: git checkout -- \$(git diff --name-only -- 'folio/*.jsonld')" >&2
  exit 4
fi
echo "gen-block-jsonld.sh: $stale_total node(s) regenerated."
exit "$rc"
