#!/usr/bin/env bash
# Exact-trace result cache for qou's probes — the `trace-cache` family
# declared in qou.json, modelled on `scripts/wheel-cache.sh` (bean qou-dgkf).
#
# WHY. A probe such as `computations/qbeta/qbeta_derived_w_overdetermined_test_probe.py`
# evaluates `pyhecke_native.tr_m_atomic_mpfr` on thousands of expanded signed
# words; at 4He (n = 12) one run is hours. Containers restart. Owner,
# 2026-11-21: an incremental calculation with stored cache data, so a re-run or
# an interrupted run resumes instead of recomputing.
#
# THE INFRA. The cat-harness `family` keying, the one `lake-cache` and
# `wheel-cache` use: qou.json declares `{ id: "trace-cache", storage: {
# branchPrefix, keyedBy: "family", keyFrom } }`, each member is one orphan
# branch `<branchPrefix><member>`, and the kind is declared in qou's own
# `typologies/`. The prefix is READ from qou.json, never written here.
#
# A MEMBER is `<function>-<engine-key>-q<q-key>-dps<dps>`:
#   function    the producer function whose values are stored:
#               `tr-m-atomic-mpfr`          pyhecke_native.tr_m_atomic_mpfr(w)
#               `tr-m-atomic-mpfr-suffixes` pyhecke_native.tr_m_atomic_mpfr_suffixes,
#                                           one value per (w, positive suffix s)
#               Two routes to the same exact number may round its last MPFR
#               digits differently, so each route is its own member.
#   engine-key  first 12 hex of sha256 over the git TREE ids of
#               tools/pyhecke-native and tools/hecke-engine at HEAD — the same
#               key wheel-cache uses, so a trace member and the wheel that
#               computed it share a key. A dirty source tree has no key
#               (`undetermined`): it never restores and never seeds.
#   q-key       first 12 hex of sha256 over the q0 decimal STRING as passed
#   dps         the decimal precision passed to the producer
# Within a member an entry is keyed by (n, signed word w, suffix s); see
# computations/trace_cache.py. Values are the producer's exact decimal strings.
#
# A member branch holds:
#   manifest.json       trace-cache-member/v1: member, function, engineKey,
#                       sourceTrees, q0, dps, shards[{file, sha256, entries}]
#   shards/<sha>.jsonl  content-addressed shards, one JSON object per line
#   README.md
# A seed ADDS one shard as a new commit on top of the member's tip and pushes
# WITHOUT force; if another writer moved the tip first, it refetches and
# re-applies. A shard is never rewritten or removed.
#
# The family rules (prefix from qou.json, source keying, private bare repo,
# no-force pushes, manifest checks) live in scripts/lib/branch-cache.sh,
# shared with every other branch cache; this script adds only its own member
# name and manifest fields.
#
# Git objects live in a PRIVATE bare repository,
# `<git-common-dir>/trace-cache.git`, never in the checkout's object store.
#
# USAGE
#   scripts/trace-cache.sh key     <function> <q0> <dps>
#   scripts/trace-cache.sh restore <function> <q0> <dps> <outdir>  # writes <outdir>/shards/*.jsonl
#   scripts/trace-cache.sh seed    <function> <q0> <dps> <shard.jsonl>
#   scripts/trace-cache.sh list
#
# EXIT CODES
#   0  hit / seeded / already present
#   1  miss (restore) — compute it
#   2  usage or environment error
#   3  undetermined or corrupt: dirty source tree, a manifest that disagrees
#      with its key, a shard whose sha256 does not match, or the remote could
#      not be reached. Never treat 3 as a hit.
set -uo pipefail
ROOT="$(git -C "$(dirname "${BASH_SOURCE[0]}")/.." rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2

# shellcheck source=lib/branch-cache.sh
. "$ROOT/scripts/lib/branch-cache.sh"
die() { BC_KIND=trace-cache bc_die "$@"; }

set_func() {
  case "$1" in
    tr-m-atomic-mpfr|tr-m-atomic-mpfr-suffixes) FUNC="$1" ;;
    *) die "unknown function: $1 (tr-m-atomic-mpfr | tr-m-atomic-mpfr-suffixes)" ;;
  esac
}
SRCS="tools/pyhecke-native tools/hecke-engine"   # same order as wheel-cache.sh, so the keys agree

bc_init trace-cache
PREFIX="$BC_PREFIX"

# Prints the member name, or "undetermined: <why>" and returns 3.
member_key() {
  local q="$1" dps="$2" ek qk
  case "$dps" in ''|*[!0-9]*) die "dps must be a positive integer: $dps" ;; esac
  case "$q" in ''|*[!0-9.eE+-]*) die "q0 must be a decimal string: $q" ;; esac
  # shellcheck disable=SC2086
  ek="$(bc_source_key "engine sources" $SRCS)" || { echo "$ek"; return 3; }
  qk="$(printf '%s' "$q" | sha256sum | cut -c1-12)"
  echo "$FUNC-$ek-q$qk-dps$dps"
}

cmd="${1:-}"; shift || true
case "$cmd" in
  key)
    [ $# -eq 3 ] || die "usage: key <function> <q0> <dps>"
    set_func "$1"; shift
    member_key "$1" "$2"; exit $?
    ;;

  list)
    bc_list
    ;;

  restore)
    [ $# -eq 4 ] || die "usage: restore <function> <q0> <dps> <outdir>"
    set_func "$1"; shift
    m="$(member_key "$1" "$2")"; rc=$?
    [ $rc -eq 0 ] || { echo "trace-cache: $m" >&2; exit 3; }
    bc_shard_restore "$m" "$3"; exit $?
    ;;

  seed)
    [ $# -eq 4 ] || die "usage: seed <function> <q0> <dps> <shard.jsonl>"
    set_func "$1"; shift
    q="$1"; dps="$2"; shard="$(realpath -- "$3" 2>/dev/null || echo "$3")"
    [ -f "$shard" ] || die "no such shard: $shard"
    m="$(member_key "$q" "$dps")"; rc=$?
    [ $rc -eq 0 ] || { echo "trace-cache: not seeding: $m" >&2; exit 3; }
    # shellcheck disable=SC2086
    meta="$(python3 - "$FUNC" "$m" "$q" "$dps" "$(bc_source_trees_json $SRCS)" <<'PY'
import json, sys
func, m, q, dps, trees = sys.argv[1:]
print(json.dumps({"function": func, "engineKey": m[len(func) + 1:].split("-")[0],
                  "sourceTrees": json.loads(trees), "q0": q, "dps": int(dps)}))
PY
)" || die "could not write the manifest"
    readme="# $m

One member of qou's \`trace-cache\` family (declared in qou.json; kind in
\`typologies/trace-cache.json\`). Exact \`$FUNC\` decimal strings at
q0 = $q, dps = $dps, keyed by (n, signed word, suffix). Read by
\`computations/trace_cache.py\`; written by \`scripts/trace-cache.sh seed\`.
Never edit by hand."
    bc_shard_seed "$m" "$shard" "$meta" "$readme"; exit $?
    ;;

  *) die "usage: $0 key|restore|seed|list ..." ;;
esac
