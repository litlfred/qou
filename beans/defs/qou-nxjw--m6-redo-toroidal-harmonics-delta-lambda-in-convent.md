---
# qou-nxjw
title: 'M6: redo toroidal-harmonics-delta-lambda in convention D'
status: todo
type: task
priority: normal
created_at: 2026-10-10T08:58:08Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-d8c7
---

mass-theory/toroidal-harmonics-delta-lambda.md:12 sets z = sqrt(q)/(1+q), w = z^2 (1 user). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed). The C identity w=z^2=1/(2(cosh eta+1)) fails under D (sympy). z_D^2 gives x=0.332<1, no toroidal reading. Bar-invariant w = z_D z_- = 1/[2]_q^2 = 1/(2(cosh 2eta+1)) gives x = cosh 2eta. Golden-ratio 0.12% near-match does not survive (x=3/2 lands 14.7% below c_lambda^exp, which is itself circular). OPEN: whether z_D z_- is the right variable; link to the z-recursion never established. Also: ToroidalHarmonicsBasis.lean x_of_w docstring and computations/qbeta/toroidal_harmonics.py (C comments, scipy float64 lpmv) not edited. Stays open.

2026-10-10 (branch claude/toroidal-harmonics-d-cleanup-2026-10-10): leftovers done. (1) ToroidalHarmonicsBasis.lean: only the x_of_w / ToroidalMarkovWOperator DOCSTRINGS encoded C; every Lean statement is the convention-neutral change of variables x=1/(2w)-1, so no math changed. lean-direct -DautoImplicit=false exit 0. (2) toroidal_harmonics.py: scipy lpmv -> mpmath.legenp at dps 50, C comments -> D, adds a symbolic D check (w=z z_- gives x=cosh 2eta exactly; w=z^2 residual nonzero). No witness exists. mpmath reproduces the old scipy numbers (golden-C ratio 0.944649, x*=1.120643), and the D anchors match the .md (golden x=3/2 ratio 0.804485, -14.73%; substrate x=1.021853 ratio 0.989206, +4.84%; D inversion q*=1.27532 / 0.78411). FINDING on the open question (sympy-checked, not Lean): z_D z_- = z_C(q^2)^2 and z_D = q^2 z_C(q^2), i.e. sqrt(w)=1/[2]_q is the C Markov parameter at q^2. Hence sqrt(w) = sum_n a_n (q^2-1)^n with a_n = markovParamCoeff (the proved 3-term recursion is just the Taylor series of sqrt(t)/(1+t) at t=1, so this is a substitution identity, not a D derivation). But the corpus already classes that recursion as a C-frame fact (docs/audits/2026-09-06-convention-c-excision-and-c-conditional-gates.md L164/L179: z_D leaves a nonzero residual in its ODE); z_D's own ODE in t=q-1 is (1+t)(t^2+2t+2) z' = (t^2+2t+4) z, a different recursion, not in the corpus. Also sqrt(2w)=(1+x)^{-1/2} is NOT a solution of the n=0 toroidal Legendre equation (residual 1/(2(x+1)^{3/2})), so the w-ODE does not make the loop value a toroidal harmonic. Whether z z_- is THE right variable is a selection question that no corpus artifact decides; left open. Not closeable.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released. The D redo and cleanup landed (#7562, #7617 merged). Open: whether w = z_D·z_− is the right variable. That is a selection question no corpus artifact decides, so it is left for the owner.
