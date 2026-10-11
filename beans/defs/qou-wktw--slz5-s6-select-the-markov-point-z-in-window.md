---
# qou-wktw
title: 'slz5 S6: select the Markov point z in [0, h]'
status: todo
type: task
priority: normal
created_at: 2026-10-10T15:10:00Z
updated_at: 2026-10-10T18:55:00Z
parent: qou-slz5
---

Stepping stone 6. OPEN. All weights positive iff 0 <= z <= h (QOU.SchurWeyl.PositiveWindow.forall_pos_iff, sorry-free). Convention D, z_D = q^3/(q^2+1), lies outside (kills 3-row blocks).

Candidates inside: z = 0 (Molien / tau endpoint), z = h/2 (self-dual: bar-invariant midpoint; S2 shows it is the unique z where pp and nn are symmetric under C3), z = h (edge; nn factor exactly 0).

Question: does the full-tower requirement, or bar-invariance, single out one point by derivation? Interaction with the 2026-08-15 convention-D ruling must go to the owner; nothing here overrides it.

## 2026-10-10 — the window reflection is the sign-twist, not bar (PR #7612, 90006099cfe)

`QOU/SchurWeyl/OcneanuWeightWindowInvolution.lean` (sorry-free, generic field; lean-direct exit 0; axioms propext/Classical.choice/Quot.sound). Probe ocneanu_window_involution_probe.py, exact sympy, 7/7, every mu |- n for n <= 7.

- **Sign-twist** sigma -> -sigma^{-1}: w_{mu'}(q, h - z) = w_mu(q, z) (`ocneanuWeight_transpose_reflect`). This IS the window reflection z -> h - z, and h/2 is its unique fixed point: `transpose_symmetric_iff_half`. The n = 2 pair alone forces it.
- **Bar** sigma -> sigma^{-1}, q -> q^{-1}: w_mu(q^{-1}, z - h) = w_mu(q, z) (`ocneanuWeight_bar`). A parameter is bar-invariant iff z = h/2 + u with u bar-EVEN (`barInvariant_iff_even`). That class includes h/2, every rank parameter z_k = h q^{2k}/(q^{2k}-1), their mirrors h - z_k, convention D (z_D = z_2), and z = h/2 + h^2/(1+h^2), which lies inside the window. **Bar-invariance does not force h/2** (scope (a), for this one condition only).
- Bar-invariant plus bar-odd is equivalent to sign-twist invariance, and that is what pins h/2.

Prior work cited in the Lean docstring: QOU.BraidsAndKnots.markov_param_eq_half_h, the character-level converse; docs/audits/2026-08-31-cds1-block-bar-defect-and-conjugation.md, Result 4; computations/hecke_conjugation_duality_sign_probe.py.

**Derived or chosen?** The six-path search found no artifact that requires sign-twist (conjugation, mu <-> mu') symmetry. So h/2 is forced only if that symmetry is chosen. Physically, sigma -> -sigma^{-1} swaps the symmetric and antisymmetric channels (boson <-> fermion statistics). This stays OPEN; the owner decides whether conjugation symmetry is a requirement. Convention D, the 2026-08-15 ruling, is untouched.
