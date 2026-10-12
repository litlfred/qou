---
# qou-6082
title: Explore a tower over Bring's surface (covers / levels)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:35Z
updated_at: 2026-10-12T18:51:39Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (QOU/Brings/BringCoverTower.lean, lean-direct exit 0)
Σ₄ = regular map of type (2,4,5); Riemann–Hurwitz 40(g−1) = |G| (bring_rh: |S₅|=120 → g=4). Canonical tower: iterated mod-m homology covers (characteristic ⇒ normal in Δ(2,4,5) ⇒ every level is again type (2,4,5), same cone angles, so the C₅ rotation/chirality data lifts). Proved: g_{k+1}−1 = m^{2g_k}(g_k−1) is RH-consistent at every level (tower_rh), strictly increasing, g_{k+1} ≥ m^{2g_k}; g_1 = 1+3m⁸ (769 at m=2, 1 171 876 at m=5). NOT derived: the modulus m (choosing it by what it reproduces would be a fit). No identification with confinement levels claimed.
