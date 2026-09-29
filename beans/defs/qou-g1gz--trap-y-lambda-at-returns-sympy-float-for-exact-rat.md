---
# qou-g1gz
title: 'TRAP: y_lambda_at returns sympy Float for exact Rational input -- zero-tests on it are normalisation-dependent'
status: todo
type: task
created_at: 2026-08-22T15:34:11Z
updated_at: 2026-08-22T15:34:11Z
---

FOUND 2026-08-22 while testing a (refuted) closed form for y_lambda.

THE TRAP. wedderburn_jones_markov.y_lambda_at(n, q) returns sympy Float even when
q is an exact sympy.Rational:

    y_lambda_at(4, Rational(3,2))[(2,1,1)]  ->  type=Float, repr=0.0

        sympy.simplify(that) == 0   ->   False
        sympy.nsimplify(that) == 0  ->   True

Two standard normalisations DISAGREE about whether the same value is zero, and
neither is wrong -- simplify leaves a Float(0.0) which does not compare equal to
the integer 0 on that path; nsimplify rationalises it to Zero.

WHY IT MATTERS. It flipped a structural test twice in one session, in opposite
directions, from the same producer output: pass 1 (nsimplify) said y_lam vanishes
for >2-row partitions; pass 2 (simplify) said it does not, and the first reading
was retracted; pass 3 showed the retraction was the artefact. Two wrong
intermediate conclusions, no bad input.

GUIDANCE. Do not zero-test y_lambda_at output with a bare == 0. Rationalise first
(nsimplify) or compare to a stated tolerance, and say which. And note the
consequence: while the producer returns floats on exact input, NO probe over
y_lambda can claim an exact identity -- only agreement to the arithmetic used.
That is the AGENTS.md "PROBES ARE NOT EXEMPT" hazard sitting inside a canonical
producer rather than in a one-off probe.

POSSIBLE FIX (not attempted here, needs the producer owner): give y_lambda_at an
exact path when q is Rational/symbolic -- the hook-content formula is a rational
function of q, so exactness is available in principle. Until then the float return
is the documented behaviour and callers must defend against it.

NOT CLAIMED: that y_lam does or does not vanish on >2-row partitions. The float
path cannot separate "exactly 0" from "1e-31", so this bean does not settle it.
