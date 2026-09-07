#!/usr/bin/env bash
# Run the whole exact-verification chain for one obstruction class.
#
# Each stage GATES the next, and that ordering is the point: a character read off a
# point that has not round-tripped is meaningless, and PR #6815's retraction was
# exactly a downstream result reported from an unverified reduction.  Any stage
# exiting non-zero stops the chain.
#
#   1  rur_exact_number_field      pin the RUR convention; verify the saturated
#                                  system EXACTLY in K = Q[t]/(f)
#   2  ptolemy_exact_character     lift all Ptolemy coordinates and ROUND-TRIP them
#                                  against snappy's ORIGINAL equations
#   3  exact_character_selfduality complex type, by a word sweep -- never generators
#   4  exact_irreducibility        Burnside rank + the Zariski-density hypotheses
#   5  exact_trace_field           real roots, trace field, generator shapes
#
# Usage: verify_class.sh <manifold> <class> [word-sweep-length]
set -euo pipefail
NAME="${1:-L6a4}"; K="${2:-1}"; LEN="${3:-4}"
D="$(cd "$(dirname "$0")" && pwd)"
run() { echo; echo "=== $1 ==="; shift; python3 -u "$@"; }
run "1/5 pin + verify over Q"   "$D/rur_exact_number_field.py"      "$NAME" "$K"
run "2/5 lift + ROUND TRIP"     "$D/ptolemy_exact_character.py"     "$NAME" "$K"
run "3/5 self-duality"          "$D/exact_character_selfduality.py" "$NAME" "$K" "$LEN"
run "4/5 irreducibility"        "$D/exact_irreducibility.py"        "$NAME" "$K"
run "5/5 trace field"           "$D/exact_trace_field.py"           "$NAME" "$K" 3
echo; echo "=== chain complete for $NAME c$K ==="
