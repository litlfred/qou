---
# qou-ls7l
title: habiro_coefficients_extended fails 4/4 and exits 0 — the L1 gate's Habiro input is unreproducible
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:17:49Z
updated_at: 2026-08-21T15:18:22Z
---

Found 2026-08-21 while trying to fix the pin straddle in qou-3zby. The fix I had proposed -- 'regenerate habiro-coefficients-extended under QOU_Q0_ANCHOR=ideal' -- would have DESTROYED the only working copy. That is why this is filed separately.

## Measured

computations/habiro/habiro_coefficients_extended.py, run today:

  4 of 4 atoms ERROR, and it exits 0.

  ValueError: LaurentQ.from_sympy: non-Laurent factor
    -(1 - 1/q**4)*(q - 1)**2/12 + 1/2
  in (-q + 1/q)*(-(1 - 1/q**4)*(q - 1)**2/12 + 1/2)

on D (deuteron A=2), T (triton A=3), 3He (helion A=3), 4He (alpha A=4).

The errors are recorded INSIDE the witness (results[label] = {'error': ...},
line 177) and main() ended in an unconditional 'return 0' (line 214). So a
total failure was indistinguishable from a clean run to anything reading the
exit code.

## Why this matters more than one broken script

The L1 tr_M cross-check (cross_check_trM_1ppb.py, the L1 compute-precision
gate) consumes this witness as one of its four methods. Two facts together:

  1. The producer writes to computations/habiro/ ... , and the copy the gate
     actually reads is computations/... -- a different file (qou-kcii).
  2. The producer FAILS.

So the gate's Habiro input is UNREPRODUCIBLE: the good top-level copy
(4/4 real results, 2026-07-18T23:59) is the surviving output of a script that
no longer works. The habiro/ copy is that same script's 17:45 run and is 4/4
errors.

An L1 gate depending on a witness nobody can regenerate is the actual
finding. The pin straddle is downstream of it -- you cannot re-pin a witness
you cannot rebuild.

## Fixed here (partial)

The exit code only. main() now returns 1 when any atom errored, and prints
which ones plus 'do not treat it as a regeneration, and do not copy it over
a good witness'. Verified: EXIT=1 with the four names.

That stops the silent-clobber accident. It does NOT fix the maths.

## NOT fixed, and this is the open item

The LaurentQ.from_sympy failure itself. The offending factor
-(1 - 1/q**4)*(q - 1)**2/12 + 1/2 is a sum, not a Laurent monomial, so
from_sympy rejects it -- plausibly it needs expanding/normalising before the
call, or from_sympy needs to accept sums. Untouched: this is the Habiro
arc's maths, and guessing at it is how a 'fix' becomes a fit.

Whoever takes it: the top-level witness is the reference for what a CORRECT
run looks like (4/4, deg_p_u ~90, engine 'python+sympy+markov_peel'). Do not
overwrite it until the producer reproduces it.
