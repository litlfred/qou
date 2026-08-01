---
# qou-qnnq
title: 'GAP: ϑ_K(q₀) — angular/spin deformation on the character variety of knot K. The surviving open DOF in the Δ_λ magnitude chain (𝔲_K = ln q₀ + i·ϑ_K). Knot-dependent: different particles = different ϑ. Determined by A(e^𝔲,ℓ)=0 boundary condition = G3 monodromy datum. Closes if Faddeev rigidity (hibinv+hratio) forces A_ω=3 AND pins the sheet. Probed values: ϑ_{4₁}(proton)=0.203, ϑ_{4₁}(muon)=0.059, ϑ_{4₁}(q*)=ln q*=0.104.'
status: todo
type: task
created_at: 2026-07-27T15:06:31Z
updated_at: 2026-08-01T00:00:00Z
---

## Re-scope (2026-08-01, qou-fs0m) — corrected framing after Fantini–Wheeler

Reading Fantini–Wheeler 2024 (arXiv:2410.20973) onto this gap corrects two
framings that made the problem look harder than it is. See
`docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`.

1. **The "off-lattice ϑ" is NOT the obstruction it seemed — category error.**
   FW's ϑ is a *Borel ray angle* (peacock rays, accumulate at arg τ = ±π/2);
   this bean's ϑ_K is the *cusp shape* Im(𝔲_K) that feeds the volume V. Two
   different ϑ's. The cusp shape is **transcendental by construction** (it's
   the geometric datum), so ϑ_K being off the integer lattice is **expected**,
   not a defect. The "T4-inverted ϑ off the lattice = sharpest obstruction"
   framing is retired.

2. **"A_ω = 3 for all winding classes" is too coarse.** The literature Stokes
   object for these knots is an **integer matrix** S(q) ∈ GL_{max{A,B}}(Z[q^±])
   with a KS cocycle (FW eqs. 26–27), not a scalar. For 5₂: (A,B)=(2,3),
   max=3 (the σ₁σ₂σ₃ geometric connections); the "4-character variety" here =
   the *extended* matrix (+ trivial σ₀). The AK state integral is the
   (m,ℓ)=(0,0) member of a rank-max{A,B} `Z[q^±]`-module `I_{m,ℓ}`.

**Restated open problem:** not "which single integer (m,ℓ)/A_ω does a braid
word pick" but **which entry/row of the GL_{max{A,B}}(Z[q^±]) Stokes matrix a
given braid closure selects, and how c₃ reads off it.** This is route 2 of the
original analysis, now literature-supported. Follow-ups: qou-3xug (5₂ AK
integral), qou-6yf7 (4₁ Stokes series), qou-cm6a (Lean conditional bridge).
Still OPEN — no fit, nothing wired.
