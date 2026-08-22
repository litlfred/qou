---
# qou-d51g
title: 'INFRA: the CODATA gate is 87s and the cost is per-literal mpmath, not I/O'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T19:45:47Z
updated_at: 2026-08-22T19:46:20Z
---

Follow-up to qou-wn1w (#5461), which wired the CODATA stale-edition scan into
scripts/precision-gates.sh. That PR recorded the gate as the slowest in the
array (~100s against ~40s for every other gate combined) and accepted the cost
rather than leave the detector unwired.

MEASURED, this branch, on 25,233 files:

  read + regex only ................ 15.2 s
  full scan ........................ 87.5 s

So ~72 s is per-literal mpmath. cProfile (302 s under profiling) attributes it:

  mpf.__sub__   6,448,043 calls
  mpf.__abs__  13,265,093
  mpf.__eq__   13,637,114
  mp.log10        372,558   <- once per literal
  normalize    35,092,995

372,265 literals clear MIN_SIG_DIGITS. Each pays one mp.log10 for its exponent,
then compares against every table row sharing that exponent -- 6.45M/372k is
about 17 mpf subtractions per literal. The file's own comment ("the cost is in
the per-literal mpmath comparison across ~25k files, not in the I/O") is
correct, and the inner loop is the larger half of it.

Two semantics-preserving fixes, both verifiable by exact output equivalence
against the current scan on the real corpus:

1. Digit-prefix prefilter. A near-miss at rel < 1e-5 agrees with its table row
   to ~5 significant digits, so (exponent, first-4-digits) computed by pure
   string slicing is a sound necessary condition. Survivors go through mpmath
   unchanged; the rest never construct an mpf at all.

2. Lazy span computation. _nonexec_spans_py tokenizes EVERY .py file up front
   (~7 s real), including the overwhelming majority with no candidate literal.
   Compute spans on the first finding in a file instead.

Also fixes qou-s2gm defect 1 while in this block: --changed reads the working
tree only, so it silently no-ops after a commit -- a false all-clear.
