#!/usr/bin/env bash
# Built-wheel cache for qou's native Python extensions — the `wheel-cache`
# family declared in qou.json (bean qou-dgkf).
#
# WHY. `pyhecke-native` is not on PyPI. Every fresh container rebuilt it with
# maturin (about 2.5 min) at SessionStart, in the background, so a producer
# that ran early could still find it missing. Owner, 2026-11-21: "Cache wheel
# on a branch", then "Use cat-harness infra for repo branch cache".
#
# THE INFRA. This is the cat-harness `family` keying, the one `lake-cache`
# uses: qou.json declares `{ id: "wheel-cache", storage: { branchPrefix,
# keyedBy: "family", keyFrom } }`, and each member is one orphan branch
# `<branchPrefix><member>`. The kind `wheel-cache` is declared in qou's own
# `typologies/` graph. The prefix is READ from qou.json, never written here.
#
# A MEMBER is `<package>-<version>-<cpython-tag>-<platform>-<source-key>`. The
# source key is the first 12 hex of sha256 over the git TREE ids of the
# package's source directories at HEAD. A dirty source tree has no key
# (`undetermined`), so it never restores a wheel built from other sources and
# never seeds one. The member branch holds:
#
#   manifest.json   wheel-cache-member/v1: package, version, python, platform,
#                   sourceKey, sourceTrees, wheel, sha256, builtFrom, builtAt
#   <wheel>.whl     the wheel itself (well under GitHub's 100 MB blob limit)
#   README.md
#
# Git objects live in a PRIVATE bare repository,
# `<git-common-dir>/wheel-cache.git`, never in the checkout's object store, the
# same rule `branch-store.ts` follows. A seed pushes WITHOUT force: a member
# that already exists is never overwritten (rule 9 also forbids deleting it).
#
# USAGE
#   scripts/wheel-cache.sh key     <package>
#   scripts/wheel-cache.sh restore <package> <outdir>   # prints the wheel path
#   scripts/wheel-cache.sh seed    <package> <wheel>
#   scripts/wheel-cache.sh list
#
# EXIT CODES
#   0  hit / seeded / already present
#   1  miss (restore) — build it
#   2  usage or environment error
#   3  undetermined or corrupt: no usable key (dirty source tree), a member
#      whose manifest disagrees with its key or whose sha256 does not match,
#      or the remote could not be reached. Never treat 3 as a hit.
set -uo pipefail
ROOT="$(git -C "$(dirname "${BASH_SOURCE[0]}")/.." rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2

die() { echo "wheel-cache: $*" >&2; exit "${2:-2}"; }

# The declared prefix. No fallback: a family nobody declared is not a cache.
PREFIX="$(python3 - "$ROOT/qou.json" <<'PY' 2>/dev/null
import json, sys
for e in json.load(open(sys.argv[1])).get("directories", []):
    st = e.get("storage") or {}
    if "wheel-cache" in (e.get("graphTypologies") or []) and st.get("keyedBy") == "family":
        print(st["branchPrefix"]); break
PY
)"
[ -n "$PREFIX" ] || die "qou.json declares no wheel-cache family"

# Packages this cache knows: source directories (their trees make the key)
# and the Cargo.toml the version is read from.
pkg_sources() {
  case "$1" in
    pyhecke-native) echo "tools/pyhecke-native tools/hecke-engine" ;;
    *) return 1 ;;
  esac
}
pkg_version() {
  local toml
  case "$1" in pyhecke-native) toml="tools/pyhecke-native/Cargo.toml" ;; *) return 1 ;; esac
  sed -n 's/^version *= *"\([^"]*\)".*/\1/p' "$toml" | head -1
}

remote_url() { git remote get-url origin; }
bare() {
  local b; b="$(git rev-parse --path-format=absolute --git-common-dir)/wheel-cache.git"
  [ -d "$b" ] || git init -q --bare "$b" || return 1
  echo "$b"
}

# Prints the member name, or "undetermined: <why>" and returns 3.
member_key() {
  local pkg="$1" srcs ver py plat dirty d trees="" key
  srcs="$(pkg_sources "$pkg")" || die "unknown package: $pkg"
  ver="$(pkg_version "$pkg")"; [ -n "$ver" ] || die "no version in $pkg's Cargo.toml"
  # shellcheck disable=SC2086
  dirty="$(git status --porcelain -- $srcs)"
  if [ -n "$dirty" ]; then echo "undetermined: $pkg's sources differ from HEAD"; return 3; fi
  for d in $srcs; do trees+="$d $(git rev-parse "HEAD:$d")"$'\n'; done
  key="$(printf '%s' "$trees" | sha256sum | cut -c1-12)"
  py="$(python3 -c 'import sys; print(f"cp{sys.version_info[0]}{sys.version_info[1]}")')"
  plat="$(python3 -c 'import sysconfig; print(sysconfig.get_platform().replace("-", "_").replace(".", "_"))')"
  echo "$pkg-$ver-$py-$plat-$key"
}

cmd="${1:-}"; shift || true
case "$cmd" in
  key)
    [ $# -eq 1 ] || die "usage: key <package>"
    member_key "$1"; exit $?
    ;;

  list)
    git ls-remote --heads "$(remote_url)" "${PREFIX}*" | sed "s#.*refs/heads/${PREFIX}##"
    ;;

  restore)
    [ $# -eq 2 ] || die "usage: restore <package> <outdir>"
    pkg="$1"; out="$2"
    m="$(member_key "$pkg")"; rc=$?
    [ $rc -eq 0 ] || { echo "wheel-cache: $m" >&2; exit 3; }
    br="$PREFIX$m"
    ls="$(git ls-remote --heads "$(remote_url)" "$br" 2>/dev/null)"; rc=$?
    [ $rc -eq 0 ] || { echo "wheel-cache: could not reach origin (unknown, not a miss)" >&2; exit 3; }
    [ -n "$ls" ] || { echo "wheel-cache: miss $br" >&2; exit 1; }
    B="$(bare)" || exit 2
    git -C "$B" fetch -q --depth=1 "$(remote_url)" "refs/heads/$br" 2>/dev/null \
      || { echo "wheel-cache: fetch of $br failed (unknown, not a miss)" >&2; exit 3; }
    C="$(git -C "$B" rev-parse FETCH_HEAD)"
    man="$(git -C "$B" show "$C:manifest.json" 2>/dev/null)" \
      || { echo "wheel-cache: corrupt $br: no manifest.json" >&2; exit 3; }
    read -r mkey whl sha < <(python3 -c '
import json, sys
d = json.loads(sys.stdin.read())
assert d.get("$schema") == "wheel-cache-member/v1"
print(d["member"], d["wheel"], d["sha256"])' <<<"$man") \
      || { echo "wheel-cache: corrupt $br: unreadable manifest" >&2; exit 3; }
    [ "$mkey" = "$m" ] || { echo "wheel-cache: corrupt $br: manifest names $mkey" >&2; exit 3; }
    case "$whl" in */*|..*|"") echo "wheel-cache: corrupt $br: bad wheel name" >&2; exit 3 ;; esac
    mkdir -p "$out" || exit 2
    git -C "$B" cat-file blob "$C:$whl" > "$out/$whl" 2>/dev/null \
      || { echo "wheel-cache: corrupt $br: $whl missing" >&2; rm -f "$out/$whl"; exit 3; }
    got="$(sha256sum "$out/$whl" | cut -d' ' -f1)"
    [ "$got" = "$sha" ] || { echo "wheel-cache: corrupt $br: sha256 $got != $sha" >&2; rm -f "$out/$whl"; exit 3; }
    echo "wheel-cache: hit $br" >&2
    echo "$out/$whl"
    ;;

  seed)
    [ $# -eq 2 ] || die "usage: seed <package> <wheel>"
    pkg="$1"; whl="$(realpath -- "$2" 2>/dev/null || echo "$2")"
    [ -f "$whl" ] || die "no such wheel: $whl"
    m="$(member_key "$pkg")"; rc=$?
    [ $rc -eq 0 ] || { echo "wheel-cache: not seeding: $m" >&2; exit 3; }
    br="$PREFIX$m"
    if [ -n "$(git ls-remote --heads "$(remote_url)" "$br" 2>/dev/null)" ]; then
      echo "wheel-cache: $br already present; not overwritten" >&2; exit 0
    fi
    B="$(bare)" || exit 2
    name="$(basename "$whl")"
    py="$(echo "${m#"$pkg"-}" | cut -d- -f2)"
    case "$name" in
      *-"$py"-*) ;;
      *) echo "wheel-cache: not seeding: $name is not a $py wheel (member $m)" >&2; exit 3 ;;
    esac
    sha="$(sha256sum "$whl" | cut -d' ' -f1)"
    srcs="$(pkg_sources "$pkg")"
    man="$(python3 - "$m" "$pkg" "$(pkg_version "$pkg")" "$name" "$sha" "$(git rev-parse HEAD)" $srcs <<'PY'
import json, subprocess, sys, datetime
m, pkg, ver, whl, sha, head, *srcs = sys.argv[1:]
parts = m[len(pkg) + 1:].split("-")
trees = {s: subprocess.check_output(["git", "rev-parse", f"HEAD:{s}"], text=True).strip() for s in srcs}
print(json.dumps({
    "$schema": "wheel-cache-member/v1",
    "member": m, "package": pkg, "version": ver,
    "python": parts[1], "platform": parts[2], "sourceKey": parts[3],
    "sourceTrees": trees, "wheel": whl, "sha256": sha,
    "builtFrom": head,
    "builtAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
}, indent=2))
PY
)" || die "could not write the manifest"
    readme="# $m

One member of qou's \`wheel-cache\` family (declared in qou.json; kind in
\`typologies/wheel-cache.json\`). Built from qou \`$(git rev-parse --short HEAD)\`.
Restore with \`scripts/wheel-cache.sh restore $pkg <dir>\`; never edit by hand."
    hw="$(git -C "$B" hash-object -w "$whl")" || exit 2
    hm="$(printf '%s\n' "$man" | git -C "$B" hash-object -w --stdin)" || exit 2
    hr="$(printf '%s\n' "$readme" | git -C "$B" hash-object -w --stdin)" || exit 2
    tree="$(printf '100644 blob %s\tREADME.md\n100644 blob %s\tmanifest.json\n100644 blob %s\t%s\n' \
             "$hr" "$hm" "$hw" "$name" | git -C "$B" mktree)" || exit 2
    commit="$(git -C "$B" -c user.name="${GIT_AUTHOR_NAME:-qou wheel-cache}" \
             -c user.email="${GIT_AUTHOR_EMAIL:-noreply@anthropic.com}" \
             commit-tree "$tree" -m "wheel-cache: seed $m" -m "Built from qou $(git rev-parse HEAD).")" || exit 2
    git -C "$B" push -q "$(remote_url)" "$commit:refs/heads/$br" \
      || { echo "wheel-cache: push of $br refused (another seed may have won; that is fine)" >&2; exit 3; }
    echo "wheel-cache: seeded $br" >&2
    ;;

  *) die "usage: $0 key|restore|seed|list ..." ;;
esac
