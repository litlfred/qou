#!/usr/bin/env bash
# Command-line face of scripts/lib/branch-cache.sh, the common infrastructure
# of qou's branch caches (wheel-cache, trace-cache, mn-chi-cache, and the
# lake-cache model they follow). `computations/_branch_cache.py` calls this, so
# the Python and shell sides share one implementation of keying, verification
# and seeding. See the library header for the rules.
#
# USAGE
#   scripts/branch-cache.sh prefix        <kind>
#   scripts/branch-cache.sh source-key    <label> <dir>...
#   scripts/branch-cache.sh source-trees  <dir>...
#   scripts/branch-cache.sh list          <kind>
#   scripts/branch-cache.sh shard-restore <kind> <member> <outdir>
#   scripts/branch-cache.sh shard-seed    <kind> <member> <shard.jsonl> <meta.json> <readme.md>
#
# EXIT CODES: 0 hit/seeded/present, 1 miss, 2 usage/environment,
# 3 undetermined/corrupt/unreachable (never a hit).
set -uo pipefail
ROOT="$(git -C "$(dirname "${BASH_SOURCE[0]}")/.." rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
# shellcheck source=lib/branch-cache.sh
. "$ROOT/scripts/lib/branch-cache.sh"

cmd="${1:-}"; shift || true
case "$cmd" in
  prefix)       [ $# -eq 1 ] || bc_die "usage: prefix <kind>"; bc_prefix "$1" || exit 1 ;;
  source-key)   [ $# -ge 2 ] || bc_die "usage: source-key <label> <dir>..."; bc_source_key "$@"; exit $? ;;
  source-trees) [ $# -ge 1 ] || bc_die "usage: source-trees <dir>..."; bc_source_trees_json "$@" ;;
  list)         [ $# -eq 1 ] || bc_die "usage: list <kind>"; bc_init "$1"; bc_list ;;
  shard-restore)
    [ $# -eq 3 ] || bc_die "usage: shard-restore <kind> <member> <outdir>"
    bc_init "$1"; bc_shard_restore "$2" "$3"; exit $? ;;
  shard-seed)
    [ $# -eq 5 ] || bc_die "usage: shard-seed <kind> <member> <shard.jsonl> <meta.json> <readme.md>"
    bc_init "$1"
    [ -f "$3" ] || bc_die "no such shard: $3"
    bc_shard_seed "$2" "$(realpath -- "$3")" "$(cat "$4")" "$(cat "$5")"; exit $? ;;
  *) bc_die "usage: $0 prefix|source-key|source-trees|list|shard-restore|shard-seed ..." ;;
esac
