---
# qou-ntck
title: 'q-Plancherel measure (generic degrees) as the candidate principle fixing m: first check whether it differs from the corpus y_lambda Wenzl weights'
status: completed
type: task
priority: normal
created_at: 2026-08-30T11:49:56Z
updated_at: 2026-08-30T12:28:51Z
---

RESOLVED 2026-08-30. The gating question is answered and the lead is CLOSED, but the headline that motivated it was WRONG and is corrected in the audit doc.

1. MY 'GENUINE GAP' CLAIM WAS FALSE. The audit doc asserted q-Plancherel appears nowhere in computations/, content/ or docs/. Measured with grep -ril: 202 live files, plus 8 deprecated and 16 beans. The corpus carries content blocks prop:/conj:q-plancherel-asymptotic-skeleton and computations/deltalambda/ uses a weight it calls 'Ocneanu / q-Plancherel' throughout. The grep was too narrow; an absence is a measurement and it was not made.

2. THE TWO ARE DIFFERENT OBJECTS (symbolic, exact). corpus W_lambda = d_q^2/[n]_q! = [n]_q!/prod[h]_q^2 (balanced, hooks SQUARED) vs paper M_{n,q} = Q^{b(lambda)} dim lambda / prod{h}_Q (unbalanced, hooks first power, classical dim). Unequal at every partition for n=2,3,4; both collapse to classical (dim)^2/n! at q=1, which is why both carry the name.

3. THE CORPUS W IS NOT NORMALIZED. Sum_lambda W at q0: 0.99458 (n=2), 0.98744 (n=3), 0.98217 (n=4), 0.98222 (n=5), 1.11092 (n=9) -- not 1, not monotone. Sum M = 1 exactly at every n and Q. So the (C5) reference d_q^2/D^2 is MIS-NORMALIZED in the corpus: D^2 = Sum_mu d_q(mu)^2, and that equals [n]_q! only at q=1 (~11% off at n=9).

4. THE LEAD IS CLOSED. Implied z via z_from_weights at q0: y_lambda 0.612688 (ABOVE the 1/sqrt5 ceiling, excluded), W as used 0.103964, W properly normalized 0.104530, paper M 0 EXACTLY. Needed m* = 0.444379. The z=0 is definitional not numerical: M decomposes the REGULAR trace and tau_q(T_sigma)=0 for sigma != id. Same one-line argument excludes the whole regular-trace/Plancherel family including classical Plancherel -- so the search restricts to Markov traces and their deformations. That exclusion is worth more than the lead was.

Scope (a) for the interface; the gate's surjectivity wall is untouched. Probe computations/probes/q_plancherel_vs_y_lambda_probe.py, 23 checks all exact (sympy), witness q-plancherel-vs-y-lambda.witness.json (q0Anchor: proton, Q0_OK). Includes a literature cross-check against the paper's own Figure 3.


CORRECTION TO ITEM 3 ABOVE (same session, caught by corpus-grep path 6 -- the beans).
Item 3 said the corpus 'MIS-NORMALIZES' the (C5) reference and that the right
denominator is D^2 = Sum_mu d_q(mu)^2. BOTH HALVES ARE RETRACTED:

 - NOT a defect. Owner ruling 2026-08-16 (notation/notation-collisions.md):
   Sum_lambda w_lambda(q) != 1 at q != 1 BY DESIGN -- 'Never write a normalisation
   claim on bare w_lambda' -- quoting 0.987 at n=3 and 1.051 at n=8. My numbers
   reproduce the ruling's independently. The retracted claim would have broken
   that ruling in the opposite direction.
 - Sum_mu d_q(mu)^2 is NOT canonical either. Bean qou-sf1t says explicitly that
   QPlancherel.sum_measureOn_eq_one is 'NOT evidence that Sum d_q^2 is the
   canonical normaliser' (one line from Finset.sum_div, true by construction).
   The sibling's 2026-08-29 n=3 Molien result gives Z = (q^2-qz-1)^2.

WHAT REPLACES IT IS STRONGER. W_lambda is conjugation-symmetric (lambda and
lambda' share a hook multiset and [n]_q!, so W_lambda = W_lambda' exactly;
verified n=2..5). At n=2 that forces z = c*(q^2-1)/(q^2+1) = c*0.1039637101 for
EVERY normalisation c. Reaching m* = 0.4443787009 needs c = 4.2743636, i.e.
Sum_lambda W = 0.23395295 -- ~4.3x from any probability-like normalisation, and
the wrong way from both the raw 0.99458 and the self-normalised 1. So NO choice
of normaliser rescues the d_q^2 weight, and the live 'which normaliser is
canonical' question does not bear on it. Normalisation-independent exclusion of
the whole family, not a miss by two evaluated numbers.

GATE ATTRIBUTION. precision-gates.sh --changed exits 1 with five REDs (q0-anchor
flip, q0-anchor refill, float64-padding, q0-value drift, witness scriptFile
provenance). NONE is mine: the RED set is byte-identical before and after this
change, and my witness is mentioned ZERO times in the gate output. My probe's
own witness is q0Anchor: proton, q0Value stamped, classified Q0_OK by
q0_anchor_consistency_audit (the first run had it in Q0_ANCHOR_MISSING; fixed at
the producer, not baselined).
