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

die() { echo "trace-cache: $*" >&2; exit "${2:-2}"; }

set_func() {
  case "$1" in
    tr-m-atomic-mpfr|tr-m-atomic-mpfr-suffixes) FUNC="$1" ;;
    *) die "unknown function: $1 (tr-m-atomic-mpfr | tr-m-atomic-mpfr-suffixes)" ;;
  esac
}
SRCS="tools/pyhecke-native tools/hecke-engine"   # same order as wheel-cache.sh, so the keys agree

PREFIX="$(python3 - "$ROOT/qou.json" <<'PY' 2>/dev/null
import json, sys
for e in json.load(open(sys.argv[1])).get("directories", []):
    st = e.get("storage") or {}
    if "trace-cache" in (e.get("graphTypologies") or []) and st.get("keyedBy") == "family":
        print(st["branchPrefix"]); break
PY
)"
[ -n "$PREFIX" ] || die "qou.json declares no trace-cache family"

remote_url() { git remote get-url origin; }
bare() {
  local b; b="$(git rev-parse --path-format=absolute --git-common-dir)/trace-cache.git"
  [ -d "$b" ] || git init -q --bare "$b" || return 1
  echo "$b"
}

engine_key() {
  local dirty d trees=""
  # shellcheck disable=SC2086
  dirty="$(git status --porcelain -- $SRCS)"
  if [ -n "$dirty" ]; then echo "undetermined: engine sources differ from HEAD"; return 3; fi
  for d in $SRCS; do trees+="$d $(git rev-parse "HEAD:$d")"$'\n'; done
  printf '%s' "$trees" | sha256sum | cut -c1-12
}

# Prints the member name, or "undetermined: <why>" and returns 3.
member_key() {
  local q="$1" dps="$2" ek qk
  case "$dps" in ''|*[!0-9]*) die "dps must be a positive integer: $dps" ;; esac
  case "$q" in ''|*[!0-9.eE+-]*) die "q0 must be a decimal string: $q" ;; esac
  ek="$(engine_key)" || { echo "$ek"; return 3; }
  qk="$(printf '%s' "$q" | sha256sum | cut -c1-12)"
  echo "$FUNC-$ek-q$qk-dps$dps"
}

# fetch <branch> -> prints the commit, exit 1 if absent, 3 if unreachable.
fetch_member() {
  local br="$1" B ls
  ls="$(git ls-remote --heads "$(remote_url)" "$br" 2>/dev/null)" \
    || { echo "trace-cache: could not reach origin (unknown, not a miss)" >&2; return 3; }
  [ -n "$ls" ] || return 1
  B="$(bare)" || return 2
  git -C "$B" fetch -q --depth=1 "$(remote_url)" "refs/heads/$br" 2>/dev/null \
    || { echo "trace-cache: fetch of $br failed (unknown, not a miss)" >&2; return 3; }
  git -C "$B" rev-parse FETCH_HEAD
}

cmd="${1:-}"; shift || true
case "$cmd" in
  key)
    [ $# -eq 3 ] || die "usage: key <function> <q0> <dps>"
    set_func "$1"; shift
    member_key "$1" "$2"; exit $?
    ;;

  list)
    git ls-remote --heads "$(remote_url)" "${PREFIX}*" | sed "s#.*refs/heads/${PREFIX}##"
    ;;

  restore)
    [ $# -eq 4 ] || die "usage: restore <function> <q0> <dps> <outdir>"
    set_func "$1"; shift
    m="$(member_key "$1" "$2")"; rc=$?
    [ $rc -eq 0 ] || { echo "trace-cache: $m" >&2; exit 3; }
    out="$3"; br="$PREFIX$m"
    C="$(fetch_member "$br")"; rc=$?
    [ $rc -eq 1 ] && { echo "trace-cache: miss $br" >&2; exit 1; }
    [ $rc -eq 0 ] || exit "$rc"
    B="$(bare)" || exit 2
    git -C "$B" show "$C:manifest.json" > "$out.manifest.tmp" 2>/dev/null \
      || { echo "trace-cache: corrupt $br: no manifest.json" >&2; rm -f "$out.manifest.tmp"; exit 3; }
    mkdir -p "$out/shards" || exit 2
    python3 - "$m" "$out.manifest.tmp" "$B" "$C" "$out/shards" <<'PY' || { rm -f "$out.manifest.tmp"; exit 3; }
import hashlib, json, os, subprocess, sys
member, man, bare, commit, outdir = sys.argv[1:]
d = json.load(open(man))
if d.get("$schema") != "trace-cache-member/v1" or d.get("member") != member:
    sys.exit(f"trace-cache: corrupt: manifest names {d.get('member')!r}")
for s in d.get("shards", []):
    name = s["file"]
    if "/" in name or name.startswith(".") or not name.endswith(".jsonl"):
        sys.exit(f"trace-cache: corrupt: bad shard name {name!r}")
    blob = subprocess.run(["git", "-C", bare, "cat-file", "blob", f"{commit}:shards/{name}"],
                          capture_output=True, check=False).stdout
    if hashlib.sha256(blob).hexdigest() != s["sha256"]:
        sys.exit(f"trace-cache: corrupt: sha256 of {name} does not match")
    with open(os.path.join(outdir, name), "wb") as f:
        f.write(blob)
print(f"trace-cache: restored {len(d.get('shards', []))} shard(s)", file=sys.stderr)
PY
    mv "$out.manifest.tmp" "$out/manifest.json"
    echo "trace-cache: hit $br" >&2
    ;;

  seed)
    [ $# -eq 4 ] || die "usage: seed <function> <q0> <dps> <shard.jsonl>"
    set_func "$1"; shift
    q="$1"; dps="$2"; shard="$(realpath -- "$3" 2>/dev/null || echo "$3")"
    [ -f "$shard" ] || die "no such shard: $shard"
    m="$(member_key "$q" "$dps")"; rc=$?
    [ $rc -eq 0 ] || { echo "trace-cache: not seeding: $m" >&2; exit 3; }
    br="$PREFIX$m"; B="$(bare)" || exit 2
    sha="$(sha256sum "$shard" | cut -d' ' -f1)"; name="$sha.jsonl"
    hs="$(git -C "$B" hash-object -w "$shard")" || exit 2
    for attempt in 1 2 3 4 5; do
      C="$(fetch_member "$br")"; rc=$?
      case $rc in 0) parent="$C" ;; 1) parent="" ;; *) exit "$rc" ;; esac
      oldf="$(mktemp)"; echo '{}' > "$oldf"
      [ -n "$parent" ] && git -C "$B" show "$parent:manifest.json" > "$oldf"
      man="$(python3 - "$m" "$FUNC" "$q" "$dps" "$name" "$sha" "$shard" "$oldf" $SRCS <<'PY'
import json, subprocess, sys, datetime
m, func, q, dps, name, sha, shard, oldf, *srcs = sys.argv[1:]
old = json.load(open(oldf))
shards = old.get("shards", [])
if any(s["file"] == name for s in shards):
    print("PRESENT"); sys.exit(0)
entries = sum(1 for line in open(shard) if '"v":' in line)
shards.append({"file": name, "sha256": sha, "entries": entries,
               "addedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "addedFrom": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()})
trees = {s: subprocess.check_output(["git", "rev-parse", f"HEAD:{s}"], text=True).strip() for s in srcs}
print(json.dumps({"$schema": "trace-cache-member/v1", "member": m, "function": func,
                  "engineKey": m[len(func) + 1:].split("-")[0], "sourceTrees": trees,
                  "q0": q, "dps": int(dps), "shards": shards}, indent=2))
PY
)"; rc=$?; rm -f "$oldf"
      [ $rc -eq 0 ] || die "could not write the manifest"
      if [ "$man" = "PRESENT" ]; then echo "trace-cache: $name already in $br" >&2; exit 0; fi
      readme="# $m

One member of qou's \`trace-cache\` family (declared in qou.json; kind in
\`typologies/trace-cache.json\`). Exact \`$FUNC\` decimal strings at
q0 = $q, dps = $dps, keyed by (n, signed word, suffix). Read by
\`computations/trace_cache.py\`; written by \`scripts/trace-cache.sh seed\`.
Never edit by hand."
      hm="$(printf '%s\n' "$man" | git -C "$B" hash-object -w --stdin)" || exit 2
      hr="$(printf '%s\n' "$readme" | git -C "$B" hash-object -w --stdin)" || exit 2
      stree="$( { [ -n "$parent" ] && git -C "$B" ls-tree "$parent:shards"; \
                  printf '100644 blob %s\t%s\n' "$hs" "$name"; } | git -C "$B" mktree)" || exit 2
      tree="$(printf '100644 blob %s\tREADME.md\n100644 blob %s\tmanifest.json\n040000 tree %s\tshards\n' \
               "$hr" "$hm" "$stree" | git -C "$B" mktree)" || exit 2
      pflag=(); [ -n "$parent" ] && pflag=(-p "$parent")
      commit="$(git -C "$B" -c user.name="${GIT_AUTHOR_NAME:-qou trace-cache}" \
               -c user.email="${GIT_AUTHOR_EMAIL:-noreply@anthropic.com}" \
               commit-tree "$tree" "${pflag[@]}" -m "trace-cache: add shard $name to $m" \
               -m "From qou $(git rev-parse HEAD).")" || exit 2
      if git -C "$B" push -q "$(remote_url)" "$commit:refs/heads/$br" 2>/dev/null; then
        echo "trace-cache: seeded $name into $br" >&2; exit 0
      fi
      echo "trace-cache: push of $br refused (attempt $attempt); refetching" >&2
      sleep "$attempt"
    done
    echo "trace-cache: gave up seeding $br after 5 attempts" >&2; exit 3
    ;;

  *) die "usage: $0 key|restore|seed|list ..." ;;
esac
