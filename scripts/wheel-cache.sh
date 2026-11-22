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
# The family rules (prefix from qou.json, source keying, private bare repo,
# no-force pushes, manifest checks) live in scripts/lib/branch-cache.sh,
# shared with every other branch cache; this script adds only its own member
# name and manifest fields.
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

# shellcheck source=lib/branch-cache.sh
. "$ROOT/scripts/lib/branch-cache.sh"
die() { BC_KIND=wheel-cache bc_die "$@"; }

# The declared prefix, read from qou.json by the shared library.
bc_init wheel-cache
PREFIX="$BC_PREFIX"

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

remote_url() { bc_remote_url; }
bare() { bc_bare; }

# Prints the member name, or "undetermined: <why>" and returns 3.
member_key() {
  local pkg="$1" srcs ver py plat key
  srcs="$(pkg_sources "$pkg")" || die "unknown package: $pkg"
  ver="$(pkg_version "$pkg")"; [ -n "$ver" ] || die "no version in $pkg's Cargo.toml"
  # shellcheck disable=SC2086
  key="$(bc_source_key "$pkg's sources" $srcs)" || { echo "$key"; return 3; }
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
    bc_list
    ;;

  restore)
    [ $# -eq 2 ] || die "usage: restore <package> <outdir>"
    pkg="$1"; out="$2"
    m="$(member_key "$pkg")"; rc=$?
    [ $rc -eq 0 ] || { echo "wheel-cache: $m" >&2; exit 3; }
    br="$PREFIX$m"
    C="$(bc_fetch_member "$br")"; rc=$?
    [ $rc -eq 1 ] && { echo "wheel-cache: miss $br" >&2; exit 1; }
    [ $rc -eq 0 ] || exit "$rc"
    B="$(bare)" || exit 2
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
    if bc_present "$br"; then
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
    bc_seed_single "$m" "$whl" "$man" "$readme" "wheel-cache: seed $m" \
      "Built from qou $(git rev-parse HEAD)." || exit $?
    ;;

  *) die "usage: $0 key|restore|seed|list ..." ;;
esac
