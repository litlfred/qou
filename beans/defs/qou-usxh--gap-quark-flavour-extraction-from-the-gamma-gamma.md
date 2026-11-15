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
