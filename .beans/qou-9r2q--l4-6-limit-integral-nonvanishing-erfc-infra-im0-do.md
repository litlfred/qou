---
# qou-9r2q
title: 'L4-6: limit integral nonvanishing — erfc infra + Im>0 domination; then instance VdVWhiteheadLemma4'
status: todo
type: task
created_at: 2026-08-11T00:36:12Z
updated_at: 2026-08-11T00:36:12Z
---

RE-SCOPED 2026-08-19 -- QOU/MathlibExt/GaussianShearIntegral.lean already
mentions erfc.  Read it before building erfc infra.  Audit:
docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md

RE-SCOPED AGAIN 2026-08-19, and this time the news is good: BOTH halves of this
brick are already answered on main, by the one-loop arc (qou-vdvS / qou-vdvE /
qou-mlgp (D)) that this epic never referenced.

1. "erfc infra" -- OBVIATED, not merely available.  The erfc factors are an
   ARTEFACT OF THE PUBLISHED PROOF, not of the mathematics.  vdV's Lemma 2a is
   stated in DISTANCES n' = |n - floor(N/2)|, k' = |k - floor(N/4)|, which turns
   Step 4 into an integral over an ORTHANT and produces erfc factors that only
   close in low rank.  The underlying Taylor expansion is SIGNED --
     f(pi/2+x, pi/4+y) = f(pi/2,pi/4) - (x^2 + 2xy + 2y^2) + O(|x|^3+|y|^3),
   and 2xy < 0 when x,y have opposite signs -- so restoring the signs puts the
   integral back over all of R^{n+1}, where it factorises completely.
   NO ERFC IS NEEDED.  (QOU/MathlibExt/GaussianShearIntegral.lean header;
   docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md Sec 1.)

2. "limit integral nonvanishing" -- SUPPLIED, sorry-free:
     QOU.MathlibExt.integral_vdv_step4 (n) (hA : 0 < A.re) :
       int_u int_v exp(-pi (A u^2/2 + 2 sum_j (v_j + u/2)^2))
         = (sqrt 2)^{-n} * (2/A)^{1/2}
   manifestly NONZERO for Re A > 0.  A = n - m i with n = c+d, m = 4a-c+d, so
   Re A = c+d >= 1 > 0 for the whole b=1 family -- which CONTAINS the Whitehead
   link W_{0,1,1,0}.  The outreach note states independently that vdV's main
   theorem needs Vol, D and E != 0 and that all three survive the corrections.

WHAT IS STILL NOT SUPPLIED (do not overclaim): the UNIFORM ERROR CONTROL that
licenses replacing the sum by that integral -- vdV Lemma 2a/2b, i.e. bean
qou-vy77 (L4-2) -- and the assembly of the two into WhiteheadLinkLowerRate.
The value of the limit integral is in hand; the sum-to-integral step is not.

So this brick becomes: CITE integral_vdv_step4, do not build erfc infra.
Ledger: docs/coordination/whitehead-link-volume-conjecture-join.md

