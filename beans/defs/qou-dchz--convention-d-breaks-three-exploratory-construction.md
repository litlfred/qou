---
# qou-dchz
title: Convention D breaks three exploratory constructions that were valid under C — Phi_q divergence, Im-cancellation failure, 4-body determinant ceiling
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T21:29:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

Found 2026-08-24 completing the qou-37xc conversion of _li_2_q_util (PR #5622,
bean qou-cds1). All three follow from one fact: z_D = 0.6126880 is 22.70 %
LARGER than z_C = 0.4993203, and several constructions sat close enough to a
pole or a positivity ceiling that the increase crosses it.

None of this is evidence against the owner's convention-D ruling. D is canonical
by ruling; these are EXPLORATORY probes that were formulated and tuned in the C
frame. Scope-(a) in every case: these constructions AS BUILT do not survive the
convention change. No ingredient is excluded.

1. PHI_Q TOWER DIVERGES. convergence_safe_vhat_tower emits '+inf' in 12 fields
   under D, e.g. raw_towers_dimensionless.cand1_phi_q.proton.T3 went
   2007063.2185098311654841850736 -> +inf. Phi_q diverges as |z| -> q (the k=1
   factor hits zero) and z_D sits closer to q than z_C did. The file's own name
   is 'convergence_safe'; under the canonical convention it is not. Related:
   the Phi_q-pole problem recorded on bean qou-2tuv and in
   mass_at_3A_proper.per_generator_V_hat_3A's docstring ('V_hat at 1.08837
   against a cap of 1.087779'). Serialized as the STRING "+inf", so the witness
   stays strict-JSON valid; the divergence is recorded, not crashed on.

2. IMAGINARY CANCELLATION FAILS. vhat_tower_im_cancellation's whole subject is
   that an imaginary part cancels. Under C it was EXACTLY 0.0; under D it is
   not: mechanism_d_branch_average.neutron.total_plus_i0.im 0.0 -> 0.6567822989,
   and total_minus_i0.im 0.0 -> -0.6567822989 (equal and opposite, so the
   cancellation is between the branches rather than within them). 230 fields
   moved, the largest count in the sweep.

3. FOUR-BODY DETERMINANTS CROSS THE PHYSICALITY CEILING. Two producers, one
   cause:
     * wlambda_cumulant_specification REFUSES BY DESIGN — 'Determinant for 3H is
       non-positive (det <= 0) ... exceeds the physicality ceiling'. exit=1 with
       a traceback, and that is correct behaviour, not a defect. Consequence: its
       witness CANNOT be regenerated under D, so it remains a C-frame record
       beside D-frame code. Stated, not papered over.
     * b4_1four_pairtype_magnitude_profile hit the same ceiling but had a LATENT
       BUG: it marks a row 'UNPHYSICAL (some det <= 0)', continues past the block
       that sets B4_ratio, then indexes it unconditionally -> KeyError. C never
       triggered it because option A was always physical. Fixed at the producer.
       All four options are unphysical under D:
         A_uniform_g   det4 = -0.26513168
         B_pn_g_like_z det4 = -0.29176533
         C_pn_z_like_g det4 = -0.56309856
         D_uniform_z   det4 = -0.54774417
       Its comparison target 0.9399185 is a CONVENTION-C-FROZEN transcribed
       constant and is flagged as such in-code rather than silently re-fitted.

NOT A FINDING, recorded so nobody chases it: deltalambda-perpair-bond-magnitude-
derive shows worst_rel = 192.8, which is an ARTIFACT of a small denominator.
The value crosses zero (0.0030557251 -> -0.58614969); the absolute move is 0.589
and the ratio is meaningless. Report sign changes as sign changes.

WHAT VERIFIED THE CONVERSION ITSELF, separately from these negatives: five
witnesses moved by exactly 5.056e-01, which is the predicted quadratic ratio
(z_D/z_C)^2 = 1.505637 computed in advance. A wrong substitution cannot
manufacture that.


CORRECTION 2026-08-29 (bean qou-zloi, PR #5978) -- item 1's "Related:" line is
wrong in kind, and the rest of item 1 stands.

That line reads: "Related: the Phi_q-pole problem recorded on bean qou-2tuv and
in mass_at_3A_proper.per_generator_V_hat_3A's docstring ('V_hat at 1.08837
against a cap of 1.087779')." MEASURED: that pole problem is NOT an instance of
the C -> D change and cannot be moved by re-pinning the convention.

`per_generator_V_hat_3A` is affine in an effective Markov parameter
Z = Sum_lambda omega_lambda tr(sigma^lambda)/dim lambda, and its production
weight scheme (normalized_plancherel) pins Z = h/2 = (q - 1/q)/2 = 0.10453014
BY SYMMETRY -- 79 % below z_C = 0.4993203 and 83 % below z_D = 0.6126880, and
identical at n = 3, 6, 9. Proved: QOU.BraidsAndKnots.markov_param_eq_half_h
(normalised + transpose-symmetric weights force h/2, any n). So the convention
never reaches that producer; the pole distance is set by the sigma-coefficient
alpha_i of the collapsed braid word (QOU.BraidsAndKnots.vHat_margin).

WHAT STILL STANDS. Item 1's own subject -- convergence_safe_vhat_tower emitting
+inf in 12 fields under D -- is a DIFFERENT producer and is untouched by this.
Items 2 and 3 are untouched. The C->D cascade is real; it just does not extend
to `per_generator_V_hat_3A`.

Note also that 1.08837 is the NEUTRON's gen-1 V_hat, not the proton's
(proton max is 1.0551103188). And the corpus carries two inequivalent proton
V_hat -- canonical_tower.per_gen_V_hat_canonical gives 1.0646262154 by a
Plancherel-averaged JM eigenvalue -- so quote the entry point with the number.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8328, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
