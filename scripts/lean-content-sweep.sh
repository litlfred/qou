#!/usr/bin/env bash
# lean-content-sweep.sh — compile every content-block `.lean` sibling that
# imports QOU against the library SOURCE, and report which are red.
#
# WHY
#
# Content-block `.lean` files live outside the Lake package: they have no lake
# target, no `.qa.json` Lean criterion, and CI auto-triggers are disabled
# repo-wide.  The only thing that ever compiles them is an agent running
# `lean`-direct against the restored olean cache — which is a snapshot, so a
# library signature that moved after the snapshot leaves them green and broken
# at once.  One such file (`descartes-knot-eigenbasis.lean`) was found by
# accident on 2026-09-05 and had been red on main since it landed.  This sweeps
# the rest.  Bean `qou-56qy`.
#
# HOW
#
# `lean-shadow-verify.sh REBUILD_ONLY=1` builds ONE shadow tree for the union
# import cone of every target, rebuilding from source only the modules whose
# own olean predates their own last source commit.  Then each target is
# compiled against that shadow, in parallel.  `lake` is never invoked, so the
# restored cache cannot be evicted.
#
# USAGE
#   scripts/lean-content-sweep.sh [-j N] [-o OUTDIR] [file.lean ...]
#
# With no files, sweeps every `content/**/*.lean` outside `lean/QOU/` that has
# an `import QOU` line.  Per-file logs land in OUTDIR (default: a temp dir,
# reported at the end); the summary goes to stdout and to OUTDIR/summary.tsv.
#
# Set SHADOW=<dir> to reuse a shadow across runs (it is ~2.3 GB).

set -uo pipefail

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
JOBS=3
OUT=""
while getopts "j:o:" o; do
  case "$o" in
    j) JOBS=$OPTARG ;;
    o) OUT=$OPTARG ;;
    *) echo "usage: $0 [-j N] [-o OUTDIR] [file.lean ...]" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [ $# -gt 0 ]; then
  TARGETS=("$@")
else
  # EVERY content-block .lean — everything under `content/` that is NOT inside a
  # package's `lean/` tree.  That prune drops both the library modules
  # (`content/*/lean/<Lib>/**`) and the package ROOT module
  # (`content/*/lean/<Lib>.lean`, the Lake aggregator); excluding the tree but
  # not the root was an earlier bug, in which `QOU.lean` was the sweep's only
  # "red" and was neither a content block nor broken.
  #
  #
  # The filter was `grep -l '^import QOU'`, which reads as "the files that depend
  # on the library" and is the wrong population: measured 2026-09-05 there are
  # 938 content-block .lean files and that filter reached 263 of them.  The other
  # 675 import only Mathlib — they are still content blocks, still compiled by
  # nothing else in the repo, and still able to carry the auto-implicit vacuity
  # class this sweep exists to catch.  A 28%-coverage sweep reporting "0 red"
  # is the kind of green this whole bean is about.
  mapfile -t TARGETS < <(
    find content -path '*/lean/*' -prune -o -name '*.lean' -print | sort)
fi
[ "${#TARGETS[@]}" -gt 0 ] || { echo "no targets" >&2; exit 2; }
echo "targets: ${#TARGETS[@]}"

[ -n "$OUT" ] || OUT=$(mktemp -d)
mkdir -p "$OUT"

# One shadow for the union cone of every target.
export SHADOW="${SHADOW:-$OUT/shadow}"
LPLINE=$(REBUILD_ONLY=1 scripts/lean-shadow-verify.sh "${TARGETS[@]}" 2>&1 | tee "$OUT/rebuild.log" | grep '^LEAN_PATH=')
if [ -z "$LPLINE" ]; then
  echo "shadow rebuild FAILED — see $OUT/rebuild.log" >&2
  tail -30 "$OUT/rebuild.log" >&2
  exit 1
fi
export LEAN_PATH="${LPLINE#LEAN_PATH=}"
export PATH="$HOME/.elan/bin:$PATH"
export OUT
# See scripts/lean-shadow-verify.sh: a bare `lean` does NOT apply the
# lakefile's [leanOptions], and `autoImplicit` differs (lean: true,
# lakefile: false), which makes bare lean-direct a WEAKER check than Lake.
export LEAN_OPTS="${LEAN_OPTS:--DautoImplicit=false -s 65536}"

one() {
  f="$1"
  log="$OUT/$(echo "$f" | tr '/' '_').log"
  timeout 900 lean $LEAN_OPTS "$f" > "$log" 2>&1
  s=$?
  n=$(grep -c ': error:' "$log" 2>/dev/null || true)
  printf '%s\t%s\t%s\n' "$s" "$n" "$f"
  # Progress to stderr so stdout stays a clean TSV.
  [ "$s" -eq 0 ] && printf '.' >&2 || printf '\nRED (%s errors) %s\n' "$n" "$f" >&2
}
export -f one

printf 'exit\terrors\tfile\n' > "$OUT/summary.tsv"
printf '%s\n' "${TARGETS[@]}" |
  xargs -P "$JOBS" -I{} bash -c 'one "$@"' _ {} >> "$OUT/summary.tsv"
echo >&2

red=$(awk -F'\t' 'NR>1 && $1 != 0' "$OUT/summary.tsv" | wc -l)
tot=$((${#TARGETS[@]}))
echo
echo "=== swept $tot, RED $red ==="
awk -F'\t' 'NR>1 && $1 != 0 {printf "  exit %-3s %-4s errors  %s\n", $1, $2, $3}' \
  "$OUT/summary.tsv" | sort -k4
echo
echo "logs + summary.tsv: $OUT"
[ "$red" -eq 0 ]
