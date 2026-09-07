#!/usr/bin/env bash
# Calibrate gb_staircase.py against a REAL system whose answer is already known.
#
# The self-test passes on five hand-checked toy ideals, which proves the parser and the
# combinatorics but NOT that the pipeline reads this corpus's actual files correctly.
# L6a4 class 1 saturated is established at dim 0, degree 4 (over Q, with a round-tripped
# witness, #6815 as corrected).  If the staircase route reproduces that from the Groebner
# basis ALONE -- no RUR, no parametrisation -- then its verdict on class 2 is trustworthy.
# If it does not, the tool is wrong and any class-2 number it produces would have been
# reported with false confidence.
ulimit -v 10485760
ulimit -f 2097152
cd "$(dirname "$0")"
echo "start $(date -u +%FT%TZ) | 1 thread (leaving the class-2 probe its 3)"
timeout 1500 msolve -t 1 -g 2 -f L6a4-c1-saturated-modp.ms -o L6a4-c1-gb-modp.txt
echo "msolve exit=$? | $(wc -c < L6a4-c1-gb-modp.txt 2>/dev/null || echo 0) bytes"
python3 gb_staircase.py L6a4-c1-gb-modp.txt
echo "EXPECTED: DIMENSION = 0, DEGREE = 4"
echo "end $(date -u +%FT%TZ)"
