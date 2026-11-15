---
# qou-usxh
title: 'GAP: quark-flavour extraction from the gamma-gamma NF is unformalised; chain at phi=0 yields no quark'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:17:21Z
updated_at: 2026-11-15T08:17:21Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u, PR #7825, QOU/Interactions/GammaGammaPairChannels.lean. The gamma-gamma product is the vacuum at phi = psi = 0 (pair_vacuum_at_zero), so the derivation chain produces no quark at the reference point of prop:confinement-universality. The up-quark channel sigma_0 depends on phi (sigma0_channel_nonconstant). Universality can hold only on the set of photon states that yield the nucleon flavours. OPEN: define the extraction map (pair NF -> quark type) and characterise that set. Until it exists the conjecture is either definitional (flavours supplied from outside) or unstated.


2026-11-15: handed to sibling 6a, which owns the quark-state definition (coordinator). Reading (b) of prop:confinement-universality reduces to non-emptiness/geometry of the fibre F^-1(nucleon flavours); see docs/audits/2026-11-15-confinement-universality-readings-and-polarization-real-structure.md.


## 2026-11-15 — γγ-built nucleon (PR #7741, `h2_gg_atom/`, `h2_gg_electron/`; owner decision C)

On three strands every γγ word is a power of V = σ₀σ₁⁻¹, so a γγ-built nucleon is V^m. Pre-registered and measured: only V³ and V⁶ pass reading 3 at every level (m = 3…7); proton and neutron are then the same word, so there is no flavour on three strands. With a γγ electron (V³ or V⁶) H₂ passes every level and the only passing bond is V³. Every γγ word has χ_(1³) = 1 (#7896). Scope (a). Bearing on this bean: flavour extraction from a three-strand γγ nucleon is empty (p = n).
