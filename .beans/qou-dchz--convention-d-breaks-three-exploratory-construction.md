---
# qou-dchz
title: Convention D breaks three exploratory constructions that were valid under C — Phi_q divergence, Im-cancellation failure, 4-body determinant ceiling
status: todo
type: task
priority: normal
created_at: 2026-08-24T21:29:51Z
updated_at: 2026-08-24T21:30:29Z
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
