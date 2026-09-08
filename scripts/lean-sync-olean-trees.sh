#!/usr/bin/env bash
# Hardlink the UNION of every Lean olean tree into every Lean olean tree.
#
# WHY THIS EXISTS.  There are two locations a package's oleans can live:
#
#   ROOT   $ROOT/.lake/packages/<pkg>/.lake/build/lib/lean
#   PAPER  $ROOT/content/*/lean/.lake/packages/<pkg>/.lake/build/lib/lean
#
# and Lean resolves a package from the FIRST `LEAN_PATH` root that holds that
# package's directory -- not from the first root that holds the MODULE.  So a
# paper tree containing a partial `Mathlib/` wins for the whole of Mathlib, and
# a complete root tree sitting later on the path is never consulted.
#
# Both orderings have now been measured to fail, in opposite directions:
#
#   PAPER incomplete  scripts/lean-content-sweep.sh reported 855 RED in QOU, all
#                     one class (MISSING-OLEAN, zero source errors), against a
#                     paper mathlib of 1802 oleans and a root mathlib of 3480.
#                     Bean `qou-4h26`.
#   ROOT incomplete   root held a 0-byte `Mathlib/Tactic.olean`, no
#                     `Mathlib/Data/Real/Basic.olean` and 1212 oleans, so every
#                     Mathlib-importing module failed "invalid header" / "does
#                     not exist".  Bean `qou-tpdg`.
#
# `lean-shadow-verify.sh` pins PAPER first and explains why; that choice is
# correct and is NOT changed here.  The repair is to remove the asymmetry the
# ordering is trying to paper over: make every tree hold the union, so which one
# wins stops mattering.  Hardlinks, so the union costs no disk.
#
# NOT a Lake restore.  Linked oleans carry no `.trace`, so `lake build` treats
# them as stale and evicts them (AGENTS.md, bean 02kc).  Use `lean`-direct /
# the sweeps afterwards; never `lake build`.
#
# Usage:
#   scripts/lean-sync-olean-trees.sh              # link, print before/after
#   scripts/lean-sync-olean-trees.sh --dry-run    # report only, link nothing
#   LEAN_TREE_ROOT=<dir> scripts/lean-sync-olean-trees.sh   # test fixture root
set -euo pipefail

DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

ROOT="${LEAN_TREE_ROOT:-$(git rev-parse --show-toplevel)}"

# --selftest builds a synthetic two-package / two-location fixture and asserts
# the three properties that matter.  Added because the cross-package bug above
# was invisible to "does it run": it exited 0 and printed a plausible summary.
if [ "${1:-}" = "--selftest" ]; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  rt="$T/.lake/packages"; pp="$T/content/paper/lean/.lake/packages"
  mk() { mkdir -p "$(dirname "$1")"; printf '%s' "$2" > "$1"; }
  # mathlib: root has A, paper has B  -> both must end with A and B
  mk "$rt/mathlib/.lake/build/lib/lean/Mathlib/A.olean" xx
  mk "$pp/mathlib/.lake/build/lib/lean/Mathlib/B.olean" yy
  # batteries: paper only, plus a 0-byte corruption in root
  mk "$pp/batteries/.lake/build/lib/lean/Batteries/C.olean" zz
  mk "$rt/batteries/.lake/build/lib/lean/Batteries/C.olean" ""
  LEAN_TREE_ROOT="$T" "$0" > "$T/log" 2>&1 || true
  fail=0
  chk() { if [ "$2" = "$3" ]; then echo "  ok   $1"; else echo "  FAIL $1: got '$2' want '$3'"; fail=1; fi; }
  chk "mathlib root has union"  "$(cd "$rt/mathlib/.lake/build/lib/lean" && find . -name '*.olean' | sort | tr '\n' ' ')" "./Mathlib/A.olean ./Mathlib/B.olean "
  chk "mathlib paper has union" "$(cd "$pp/mathlib/.lake/build/lib/lean" && find . -name '*.olean' | sort | tr '\n' ' ')" "./Mathlib/A.olean ./Mathlib/B.olean "
  chk "no Batteries in mathlib" "$(find "$rt/mathlib" "$pp/mathlib" -name 'C.olean' | wc -l)" "0"
  chk "no Mathlib in batteries" "$(find "$rt/batteries" "$pp/batteries" -name 'A.olean' -o -name 'B.olean' | wc -l)" "0"
  chk "0-byte olean repaired"   "$(stat -c%s "$rt/batteries/.lake/build/lib/lean/Batteries/C.olean")" "2"
  [ "$fail" -eq 0 ] && echo "selftest: PASS" || { echo "selftest: FAIL"; cat "$T/log"; }
  exit "$fail"
fi

# Every olean tree, grouped by package name.  A loop, not `ls -d <pat1> <pat2>`:
# `ls` sorts its arguments and would silently reorder the two locations.
declare -A TREES=()
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean \
         "$ROOT"/content/*/lean/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] || continue
  # <pkg>/.lake/build/lib/lean -> four levels up.  Three lands on ".lake",
  # which collapses EVERY package into one group and cross-links them.  That
  # bug was written, run, and caught here: it merged `batteries` (3 oleans,
  # Batteries/*) into `mathlib` (5 oleans, Cache/*) and back, both to 8.
  pkg=$(basename "$(dirname "$(dirname "$(dirname "$(dirname "$d")")")")")
  TREES["$pkg"]="${TREES[$pkg]:-}$d"$'\n'
done

if [ ${#TREES[@]} -eq 0 ]; then
  echo "lean-sync-olean-trees: no olean trees under $ROOT — nothing to do."
  echo "  (restore the cache first; AGENTS.md §\"Mathlib cache 403 fallback\")"
  exit 0
fi

total_linked=0 total_repaired=0 pkgs_touched=0

for pkg in $(printf '%s\n' "${!TREES[@]}" | sort); do
  mapfile -t dirs < <(printf '%s' "${TREES[$pkg]}" | sed '/^$/d')
  [ "${#dirs[@]}" -ge 2 ] || continue          # one location ⇒ no asymmetry

  before=""
  for d in "${dirs[@]}"; do
    before="$before $(find "$d" -name '*.olean' | wc -l)"
  done

  linked=0 repaired=0
  # Union: for every (source, target) ordered pair, supply what target lacks.
  for src in "${dirs[@]}"; do
    for dst in "${dirs[@]}"; do
      [ "$src" = "$dst" ] && continue
      while IFS= read -r rel; do
        s="$src/$rel"; t="$dst/$rel"
        if [ -e "$t" ]; then
          # A 0-byte olean is the qou-tpdg corruption: replace it, never keep it.
          if [ ! -s "$t" ] && [ -s "$s" ]; then
            [ "$DRY" -eq 0 ] && { rm -f "$t"; ln "$s" "$t" 2>/dev/null || cp "$s" "$t"; }
            repaired=$((repaired + 1))
          fi
          continue
        fi
        [ "$DRY" -eq 0 ] && { mkdir -p "$(dirname "$t")"; ln "$s" "$t" 2>/dev/null || cp "$s" "$t"; }
        linked=$((linked + 1))
      done < <(cd "$src" && find . -name '*.olean' -o -name '*.ilean' | sed 's|^\./||')
    done
  done

  if [ "$linked" -gt 0 ] || [ "$repaired" -gt 0 ]; then
    after=""
    for d in "${dirs[@]}"; do
      after="$after $(find "$d" -name '*.olean' | wc -l)"
    done
    printf '  %-22s olean%s ->%s   linked %d, repaired %d\n' \
      "$pkg" "$before" "$after" "$linked" "$repaired"
    pkgs_touched=$((pkgs_touched + 1))
  fi
  total_linked=$((total_linked + linked))
  total_repaired=$((total_repaired + repaired))
done

if [ "$total_linked" -eq 0 ] && [ "$total_repaired" -eq 0 ]; then
  echo "lean-sync-olean-trees: every tree already holds the union — nothing to do."
else
  echo "lean-sync-olean-trees: $pkgs_touched package(s), $total_linked file(s) linked, $total_repaired 0-byte olean(s) repaired.$([ "$DRY" -eq 1 ] && echo '  [DRY RUN — nothing written]')"
  echo "  Hardlinks: no disk cost.  No .trace sidecars: use lean-direct/the sweeps, never lake build."
fi
