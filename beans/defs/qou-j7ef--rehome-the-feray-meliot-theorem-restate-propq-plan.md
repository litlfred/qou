---
# qou-j7ef
title: 'Rehome the Feray-Meliot theorem: restate prop:q-plancherel-asymptotic-skeleton over M_{n,q} (= the corpus''s Molien family under Q=q^2), so clause 2 actually holds instead of being disclaimed'
status: completed
type: task
priority: normal
created_at: 2026-09-05T06:57:23Z
updated_at: 2026-09-05T07:58:08Z
---

## Closed 2026-09-05 (PR #6771)

**The rehoming is done, and the enabling fact is that the corpus already held
`M_{n,q}` under another name.** Measured exactly (Fraction arithmetic, all 96
partitions of n=1..9):

    f^lam * q^{-contentSum(lam)} * dim_q(lam) / [n]_q!  ==  M_{n,q^2}(lam)

i.e. `MolienFakeDegreeGeneralN.molienSum`'s weight IS Feray-Meliot Definition 1
at Q = q^2. The kappa exponent is FORCED by that substitution (via
`sum h = n(lam)+n(lam')+n` and `contentSum = n(lam')-n(lam)`, both verified
independently over n<=10), not chosen.

q>1 costs an orientation, not the theorem: their duality
`M_{n,1/Q}(lam') = M_{n,Q}(lam)` is exact (verified n<=9), so the substrate's
Q = q0^2 ~ 1.232 reads as the q<1 result on conjugate diagrams.

Producer: `computations/probes/molien_feray_meliot_bridge_probe.py` (5/5).

**Three defects found and fixed, one recorded:**
1. The block cited `feray2010` (Feray, *Stanley's formula*), not the
   q-Plancherel paper. Corrected to `feray-meliot2012`.
2. The `O(1/sqrt(n-3))` variance bound occurs NOWHERE in Feray-Meliot (27
   sections searched); their result is a CLT at scale sqrt(n). Lean field
   renamed `feray_meliot_bound` -> `variance_majorant` and documented as an
   assumption. Provenance is UNSOURCED, not refuted -- a Feray-Sniady character
   bound is the plausible family and the corpus holds one
   (`arxiv-math-0701051v4`), unchecked.
3. The block's own separation column 0.158..12.6 was M at Q = q0, not at the
   bridge argument Q = q0^2 (where it is 0.368..978). Both now measured.

**Not done, deliberately:** `plancherel-term-7-formulation` still uses a dim_q^2
family. That is `qou-oots` and is not cosmetic -- three families, three
different k=3 winners.
