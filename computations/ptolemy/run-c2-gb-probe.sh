#!/usr/bin/env bash
# Class-2 DIAGNOSTIC: compute the degrevlex Groebner basis only (-g 2), not the RUR.
#
# WHY THIS RATHER THAN A LONGER RUN.  The 3000 s timeout tells us the full solve is
# expensive; it does NOT tell us WHICH half is expensive.  msolve does two things:
# (1) a degrevlex Groebner basis, then (2) a change of order / parametrisation (FGLM)
# to produce the RUR.  For an ideal of high degree, (2) is routinely the dominant
# cost.  -g 2 stops after (1).
#
# WHAT IT BUYS EVEN IF THE RUR STAYS OUT OF REACH.  A degrevlex GB determines the
# DIMENSION from its staircase (leading terms), and when the dimension is 0 the
# DEGREE is the count of standard monomials.  So this probe can answer the actual
# question -- is class 2 zero-dimensional, and of what degree -- without ever
# producing a parametrisation.  A blind longer run answers nothing it does not
# already answer.
#
# Caps as before: memory generous (OOM is survivable), file size tight (a GB can be
# large, and disk exhaustion is not survivable from inside the session).
ulimit -v 10485760
ulimit -f 2097152
cd "$(dirname "$0")"
echo "start $(date -u +%FT%TZ) | disk $(df -h / | awk 'NR==2{print $4}')"
timeout 2700 msolve -t 3 -g 2 -f L6a4-c2-sweep-modp.ms -o L6a4-c2-gb-modp.txt
echo "exit=$? end=$(date -u +%FT%TZ) | disk $(df -h / | awk 'NR==2{print $4}') | out=$(wc -c < L6a4-c2-gb-modp.txt 2>/dev/null || echo NONE) bytes"
