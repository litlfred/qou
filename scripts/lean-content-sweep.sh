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
  mapfile -t TARGETS < <(
    find content -name '*.lean' -not -path '*/lean/QOU/*' -print0 |
      xargs -0 grep -l '^import QOU' | sort)
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

one() {
  f="$1"
  log="$OUT/$(echo "$f" | tr '/' '_').log"
  timeout 900 lean "$f" > "$log" 2>&1
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
