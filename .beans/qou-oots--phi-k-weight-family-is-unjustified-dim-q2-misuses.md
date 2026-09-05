---
# qou-oots
title: 'Phi_k weight family is unjustified: dim_q^2 misuses a quantum dimension where f^lambda*dim_q (Molien, Lean-proved exactly normalized) or y_lambda (Markov, canonical Frobenius pairing) may belong'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T05:55:40Z
updated_at: 2026-09-05T06:35:54Z
---

## 2026-09-05 — requirement derivation + prune + discriminator (in-progress; the CHOICE is open, the PRUNE is not)

DELIVERABLE: docs/audits/2026-09-05-phi-k-weight-family.md
LEAN: QOU/BraidKnot/DepthStratifiedWeightRequirements.lean (lean-direct exit 0,
      0 sorry, #print axioms clean on all 6 decls)
PROBE: computations/probes/phi_k_weight_family_discriminator.py + witness

THREE REQUIREMENTS DERIVED (Lean, generic over abstract w/m/c, no anchor):
  R3 phiDiff_eq_sum_log_ratio -- the d_q INSIDE the log CANCELS in the
     observable difference (same index set, same weights on free and atom), so
     B = SUM_k a_k SUM_l w_l log|chi_free/chi_atom| is a weighted GEOMETRIC MEAN
     of character ratios. NOT linear in the braid element => Phi is NOT a trace
     => no Markov property is required of w. Consequences BOTH ways: y_lambda's
     only claim to privilege here evaporates, AND
     q_plancherel_vs_y_lambda_probe's "regular-trace family gives z=0, restrict
     to Markov traces" exclusion MUST NOT be imported -- it is scoped to the
     interface bond scalar z = tr(sigma_1), a linear trace evaluation Phi never
     performs. Importing it would be an arity/scope error.
  R1 phi_eq_zero_of_weights_vanish -- w vanishing on the stratum makes Phi_k
     identically 0. y_lambda's SU(N) row cap ([N+c]_q = [0]_q = 0 at the cell of
     content -N; RowCapObstruction.lean) makes y = 0 on EVERY stratum of depth
     >= N. Verified symbolically: N=2 (n=3,4,5,6) and N=3 (n=4,6). Depth 3 is
     killed at BOTH the mass (N=2) and colour (N=3) readings.
     => SCOPE-(b) exclusion of y_lambda. Measured: all three candidate knots
     reproduce the no-FR baseline to the last digit (5.3561249).
  R2 crossRatio_smul -- w -> k_n w multiplies the cross-nucleus metric by
     k_1/k_2; n = 3A differs, so the normaliser must be n-INDEPENDENT. NOTE this
     is WEAKER than "probability measure" -- any n-independent constant does.
     SUM d_q^2/[n]_q! = 0.9946/0.9874/0.9822/0.9822/0.9911 at n=2..6 and
     0.99108/1.11092/1.51713 at the nuclear n=6/9/12 => SCOPE-(b) exclusion of
     d_q^2/[n]_q! for cross-nucleus use (it stays valid same-n, by
     WLambdaNormalizationInvariance.ratio_invariant).
  NOT a requirement: conjugation symmetry. d_q^2 families are symmetric, Molien
  is asymmetric (q^{-kappa}, kappa = n(l')-n(l)) -- but the DEPTH stratification
  already separates l from l', so a symmetric w is not incompatible with a
  chirality channel. Recorded as a property, not derived as a requirement.

TWO SURVIVE: d_q^2/D^2 and the Molien family. THE CHOICE IS OPEN.

NEW IDENTIFICATION (exact in Q(q), every partition, n=2,3,4,5): the corpus's
Lean-proved MOLIEN family f^l q^{-kappa_l} d_q(l)/[n]_q! IS the literature's
q-Plancherel measure M_{n,Q}(l) = Q^{b(l)} dim l / prod{h}_Q
(Feray-Meliot, arxiv-1001.2180v2) under the corpus's own Q = q^2 bridge. One
line of hook arithmetic: prod[h]_q = q^{-(n(l)+n(l'))} prod{h}_Q and
kappa_l = SUM contents = n(l')-n(l). So the corpus HOLDS the literature's
q-Plancherel measure under a different name (molienSum) while calling
d_q^2/[n]_q! "q-Plancherel" -- and it is the FORMER that is exactly normalised.

THE DISCRIMINATOR FLIPPED, AND NOT THE WAY I EXPECTED. The k=3 ranking is NOT
weight-family-invariant. Three scoreable families, three different orderings,
three different winners:
  d_q^2/[n]_q!  no-FR 1.562126  4_1 1.5014667  5_2 1.5394226  6_1 1.6040329  best 4_1
  d_q^2/D^2     no-FR 1.0659881 4_1 1.2425297  5_2 1.2911323  6_1 1.0478474  best 6_1
  molien        no-FR 1.5488755 4_1 1.2308566  5_2 1.2168828  6_1 1.6067832  best 5_2
  y_lambda      5.3561249 for ALL FOUR rows (vacuous, R1)
Under MOLIEN -- the family with the best structural credentials -- the paper's
named 6_1 is the WORST of the three and the ONLY one that makes its own baseline
worse (-3.74%), while 4_1 and 5_2 are near-tied at +20.5%/+21.4%, a far LARGER
FR effect than any family has reported. Robust Molien statement: "{4_1,5_2}
close ~21%, 6_1 opens it" -- the 1.1% between 4_1 and 5_2 is not resolved by
this metric.
HARNESS VALIDATED: under d_q^2/D^2 the companion reproduces the committed
fr-pullback-k3-test witness on all 4 rows to <= 3.1e-16.

TWO DEFECTS FOUND, one mine:
  1. MINE. Hand-typed B_AME["T"] = 8.481798 vs the corpus constant 8.4817962 --
     a uniform 2.12219e-7 disagreement on 3 of 4 rows. Visible only because of
     the cross-validation, diagnosable only because the 4th row (6_1) agreed to
     3e-16 (T is the argmin for the other three, not for 6_1). Same class as the
     self-comparing AME literal fr_pullback_k3_test already caveats.
  2. UPSTREAM, flagged not fixed. fr_pullback_k3_test takes q0 from
     qou_substrate.constants.Q, which is a Python FLOAT; Q_50_DIGIT_STR exists.
     Measured 2.725e-17 relative. Immaterial here (15 orders under the effect)
     and NOT fixed -- changing a producer's anchor moves its published numbers
     and would break the controlled comparison. This probe uses the string.

STILL OPEN (why the bean stays in-progress): which of d_q^2/D^2 and Molien is
correct. My judgement, marked as judgement in the audit: MOLIEN, on exact
normalisation-by-theorem vs by-construction, the correct one-factor q-lift of
Burnside, an independently-named normaliser, and the q-Plancherel
identification. But NONE of that is derived FROM Phi_k, so adopting it would
substitute a good argument for a derivation. What would close it, in order:
  (a) name which object the nucleus is a state in -- V^{tensor n} gives the
      Molien shape f^l d_q(l)/[n]_q!, End(V^{tensor n}) gives d_q^2/D^2. This is
      structural, not numerical, and it is the whole content.
  (b) a same-n within-stratum observable (normalisation-invariant by
      ratio_invariant, but the PROFILE is not -- the two survivors put
      S_3 = 0.349/0.392/0.137 (Molien) vs 0.249/0.469/0.329 (d_q^2/D^2) on the
      depth-3 stratum at D/T/4He).
  (c) more than four nuclei; max/min over n in {6,9,9,12} cannot resolve 1.1%.
PRACTICAL OUTPUT: no k=3 knot conclusion should be quoted without naming the
weight family it was computed under.
