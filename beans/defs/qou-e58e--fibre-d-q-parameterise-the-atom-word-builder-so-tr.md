---
# qou-e58e
title: 'FIBRE-D: q-parameterise the atom word builder so tr_M(q0^-1) is computable -- unblocks every bar-parity claim'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-11-17T07:52:47Z
parent: qou-10v9
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

SECOND PASS 2026-08-19 ("try" = go for delta closed form). DID NOT GET IT. Got the structure exactly, plus a named blocker and a refuted guess.

EXACT SYMBOLIC (sympy): every atom-word letter is exactly bar-odd EXCEPT the color-weighted interface d = -h*(1/2 - f/4). Since f(1/q) = -q^2 f(q), the f-part does not flip with h, leaving the fully-factored defect
    d(q) + d(1/q) = (q-1)^4 (q+1)^2 (q^2+1)^2 / (12 q^5)
manifestly positive for q>0, vanishing to 4th order at q=1. The interface letters are ALSO exactly what separates the atom word from the free word -- so the atom/free asymmetry and the bar-parity defect have the SAME SUPPORT. That is why delta is an interface property and nothing else.

EXACT EXTENSIVE/INTENSIVE SPLIT (measured, not fitted). Summing ln|tr(Z,N;q)/tr(N,Z;1/q)|/ln q over a mirror pair, the FIRST DIFFERENCE is constant to 3.6e-24, so S_free(A) = A*c(q) with NO constant term (max |S_free - A*c| = 3.4e-24). No two-parameter form was ever solved for -- a constant first difference is a measurement. The ATOM channel obeys the same extensive law MINUS a purely intensive 2*delta, identical at every A (spread 6.0e-23). Same extensive/intensive language the Delta_lambda magnitude problem is stated in; here the separation is exact.

STILL OPEN, THE REAL STEP: the NUMBER of interface letters grows with A but delta does not. Nothing here explains how a growing set of interface defects nets to an A-independent amount. Any closed form for delta must come through that.

BLOCKER, NAMED AND FIXABLE: chi_monotone_transfer.word_to_mpfr calls float(h) as a TEMPLATE CLASSIFIER (not a computation -- it rebuilds d at full dps after, so precision is fine). That float is what refuses a sympy symbol, so chi_all_lambda_reduced_block and hence the whole trace cannot go symbolic. The WORD builder is symbolic; the TRANSFER is not. Making the classifier structural instead of numeric opens the symbolic derivation of delta. Concrete next step.

REFUTED GUESS (recorded): I expected q -> 1/q to act as lambda -> lambda-conjugate (standard H_n(q) iso H_n(1/q)). For the self-mirror deuteron the per-lambda ratios are all approx -1 (defect 1.6e-4..1.8e-3) so the shape is right, but at n=9 they scatter (-0.66, -0.70, +1.08, +3.47). The naive per-lambda conjugation law is REFUTED as stated -- and it could not have been the mechanism anyway, since y_lambda != y_lambda-conj so the sum would not transform cleanly.

Probe extended with part 5; ASSERTIONS PASS. Audit section 4b.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under related carrier M11 (qou-wzgm) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## Implementation & Witness Progress (PR #8264)
- Branch: `qou-10v9-e58e-gcmn-vbyi-vtlj-xy5f` (`248efc097170676991e07dd557f09bee0827f2bc`), PR: `litlfred/qou#8264`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityIsospinSplitBppConfoundSingletTensorInvarianceDeltaFourValuesAndOrderingDofShift.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/bar_parity_isospin_split_bpp_confound_singlet_tensor_invariance_delta_four_values_and_ordering_dof_shift_probe.py` -> `computations/probes/bar-parity-isospin-split-bpp-confound-singlet-tensor-invariance-delta-four-values-and-ordering-dof-shift.witness.json` (`allPassed: true`, `scriptHash: e7d87b167c3f`, `scriptCommitSha: 7d111fc9111a5ac911879c633afd63652e0f6384`)
