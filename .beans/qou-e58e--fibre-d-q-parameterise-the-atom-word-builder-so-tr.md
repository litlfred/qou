---
# qou-e58e
title: 'FIBRE-D: q-parameterise the atom word builder so tr_M(q0^-1) is computable -- unblocks every bar-parity claim'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-08-19T17:47:17Z
---

THE BLOCKER IS TOOLING, NOT MATHEMATICS. complex_volume_witness.py already attempts the bar-norm ||tr_M||^2 = tr_M(q0)*tr_M(q0^-1) and guards it, with its own comment: "The canonical color-weighted atom word BAKES q0 into its crossing values, so it cannot re-lift at q^-1 (a q-parameterised word builder is required)". Same comment records the fact the whole route turns on: bar-norm and |tr_M|^2 "coincide on the unit circle (where conjugation = bar-involution) and DIFFER at the real anchor q0". So every bar-parity claim about a trace-derived quantity currently rests on a quantity the corpus CANNOT EVALUATE. Task: parameterise tr_m_atom_via_transfer over q, then un-guard the bar-norm. Prerequisite for options B/C/E being more than prose. Cost UNMEASURED -- q0 may be baked in at more than one site. Doc: docs/audits/2026-08-19-frakv-fibre-workplan-options.md option D.

RESULT 2026-08-19 -- MY OWN PREMISE WAS WRONG, and what replaced it is better.

tr_M(q0^-1) ALREADY COMPUTES (milliseconds). tr_m_atom_zn.__doc__ said two contradictory things thirty lines apart; the "q0-baked / raises ValueError" paragraph predated the q-parameterisation. Both that docstring and the complex_volume_witness bar-norm comment that cited it are corrected in this commit.

The bar-norm guard fires for a DIFFERENT reason than it states: not a raise, but bar_prod > 0 failing -- the product is NEGATIVE (deuteron -8.52e-4, free -3.30e-3). So the "principled bar-norm mass modulus" does not EXIST as a real number for this word. Stronger than "not computable"; the claim should be retired, not repaired.

FINDINGS (probe computations/substrate/bar_involution_is_isospin_probe.py, ASSERTIONS PASS):
1. y_lambda are EXACTLY bar-even -- bit-identical at 5 q, all 11 partitions of 6, and they do vary with q so it is not a cache hit. Reason: ratios of [k]_q, each bar-odd, so the ratio is bar-even at every n. => ALL bar parity lives in the WORD, never the weights. Generalises the D two-row observation from n=3.
2. THE BAR INVOLUTION IS ISOSPIN CONJUGATION. With L = ln(tr_free/tr_atom): L(Z,N;q) - L(N,Z;1/q) = delta(q), delta INDEPENDENT of (Z,N). Measured A=2..6, both mirror orientations (11 nuclei), 5 values of q; spread 7.9e-24 .. 2.4e-30. 3H at q0 = 3He at 1/q0 to 22 digits after subtracting delta.
3. delta(q) = O(h^5), delta(q0) = 3.2829e-5 = RELATIVE 4.85e-5 on the deuteron binding = 6219x the Q_beta L2 100x target. NOT negligible.
4. NOT IDENTIFIED: delta/h^5 drifts 0.0822 -> 0.0723, so h^5 is the leading ORDER only; naming a constant would be a fit.

BEARS ON conj:binding-qbeta-complex-volume as a CONSISTENCY, NOT a derivation: the bar-odd partner of bar-even binding is the mirror-pair difference, and 3H->3He IS a beta decay -- the channel the conjecture assigns to Im frakV. But nothing here derives Im frakV, the mirror difference is NOT identified with Q_beta (0.784 MeV vs 18.6 keV are different numbers), and Im(q0)=0 still kills Im frakV after tau.

Precision gates: RED is PRE-EXISTING and not from this diff -- the one NEW dirty witness is probes/gswz_epsm_m3_one_two_relation_closure.witness.json, untouched here (shape guard: 0 witnesses modified).

FOLLOW-ON: formalize the mirror law in Lean and derive delta symbolically from the deuteron word (the honest route to identifying it); re-scope qou-sglq with this in hand. Audit: docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md
