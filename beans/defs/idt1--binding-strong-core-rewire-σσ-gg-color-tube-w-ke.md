---
# idt1
title: 'Binding strong-core rewire: σ/σ⁻¹ → gg color-tube W (keystone-gated, 754x step 5b)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-06-30T23:51:28Z
updated_at: 2026-10-04T15:16:42Z
parent: qou-v2om
---


## Context (2026-06-30, bean 754x step 5b — deferred)

Bean 754x diagnosed that production `B_sym`'s like-nucleon bond assignment
`p-p↦σ, n-n↦σ⁻¹` is the **flavor-only projection** of the color-tube `W_{c₁c₂}`
weighting and over-breaks strong charge symmetry by ~78% (570× the derived 0.14%
p/n split). The gg-production test collapsed it to 0; the Coulomb kill-switch
confirmed the mirror split is Coulomb on a charge-symmetric core.

**Step 5A (DONE, merged):** the additive Coulomb EM term is wired
(`computations/coulomb_energy.py` + dashboard `E_C` column).

**Step 5B (THIS bean, GATED):** replace the σ/σ⁻¹ strong core with the gg
charge-symmetric core using the full **9-channel color-tube weight `W_{c₁c₂}`**.
- BLOCKED on the keystone: `W_{c₁c₂}` is gated on `conj:s5-so3-fiber-action`
  (= bean s013 / s5bb — the `bwS0=d_q/D` realization). Do NOT wire a bare-σ_avg
  stopgap: it zeroes the **derived 0.14% flavor split** the owner directed be kept;
  the full `W` preserves it.
- Scope when unblocked: production change touching ~72 producers / ~840 muon-q₀
  witnesses ⇒ explicit owner sign-off + a witness-migration plan (NOT an idle drain).
- Kill-switch on completion: the isovector residual `b → 0`
  (`BindingIsovectorChiralResidue.lean`); a chiral derivation leaving `b≈−1.7` is wrong.

### Cross-refs
- Bean 754x (parent finding), `inter-nucleon-channel-color-tube.md`
- Bean s013 / s5bb (the keystone `W` this depends on)
- `docs/coordination/s5-so3-keystone.md` §"Binding-side test routed in"

- **Round 90 (`https://github.com/litlfred/qou/pull/8410`, head `507a878f2b14ab11470e7af5019207b486d15e86`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
