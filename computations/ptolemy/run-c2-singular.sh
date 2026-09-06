#!/usr/bin/env bash
# Class 2 via SNAPPY'S OWN ROUTE: full 27-variable system, saturate by every variable,
# over Q -- executed in Singular, which is Sage's Groebner engine, so this is what
# compute_solutions(engine='sage') would run without Sage installed.
#
# It is a DIFFERENT COMPUTATION from the one that timed out, not a longer run of it.
# The msolve attempts used the corpus's FKR-reduced system (11 vars): small, fast for
# class 1, and provisional because clearing denominators adds the locus {A=0}.  This is
# snappy's route: 27 vars, and saturation removes the degenerate components BY
# CONSTRUCTION, so a dimension it reports needs no round trip to be meaningful.
#
# Honest expectation: it may well be slower -- the corpus measured Singular's std at 39
# minutes on a system msolve settled in 4.  Bigger system AND the slower engine.  It is
# worth running because it is the documented route, it answers a sounder question, and
# EMPTY would be conclusive on its own.
ulimit -v 10485760
ulimit -f 2097152
cd "$(dirname "$0")"
echo "start $(date -u +%FT%TZ) | disk $(df -h / | awk 'NR==2{print $4}')"
timeout 5400 Singular -q L6a4-c2-saturate-full.sing
echo "exit=$? end=$(date -u +%FT%TZ) | disk $(df -h / | awk 'NR==2{print $4}')"
