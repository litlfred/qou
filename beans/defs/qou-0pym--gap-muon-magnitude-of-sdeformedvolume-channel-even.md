---
# qou-0pym
title: 'GAP: muon magnitude of SDeformedVolume channel — boost-rapidity factor c=√A≈1.43'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:34:46Z
updated_at: 2026-10-04T15:20:14Z
parent: qou-avtq
---

Deriving `S = Q_β/E₀` (Subgoal-2) via the SDeformedVolume channel
`S = Im 𝔙₄₁(u(q₀))` decouples into two orthogonal open pieces (audit
`docs/audits/2026-08-01-derive-S-Qbeta-E0-leading-bound-decoupling.md`):

- **proton sign flip** ← the spin/imaginary part of `u(q₀)` (bean `qou-fook`);
- **muon magnitude** ← THIS gap.

**Proved bound (this pass, sorry-free):**
`FigureEightComplexVolume.imV₄₁_le_cuspModulus_reSq` — `Im 𝔙₄₁(u) ≤ κ·(Re u)²`
(since `Im²u ≥ 0`, `κ = √3/4 > 0`). So the spin part can only *decrease*
`Im 𝔙₄₁`; the muon deficit (`S_μ = 2.054 × κ(ln q₀)²`) is UNREACHABLE by any
real spin (`imV₄₁_leading_unreachable_of_lt`) ⇒ it must be a `Re u` enhancement.

**Convergence with sibling #4515 (survivor `qou-iyj5`).** PR #4515 reached the
same `A ≈ 2.05` gap from the exact figure-eight CS integral and sharpened it:
the deficit is the boost-rapidity factor `c = √A ≈ 1.4305`, i.e. the effective
rapidity is `√2.05·ln q₀` not the meridian rapidity `ln q₀`. The `O(u⁴)` NZ tail
is EXCLUDED as the source by #4508 (radius of convergence `0.96 ≫ u = 0.104`).
This bean's `imV₄₁_le_cuspModulus_reSq` is the Lean backing for #4515's
"spin only decreases `Im 𝔙₄₁`" claim.

**Next honest step (open, do NOT fit):** derive `c = √A ≈ 1.43` — the `O(1)`
boost-rapidity enhancement — from the substrate geometry (why `√2.05·ln q₀`?).
A `c` obtained by inverting `S_μ` is a fit and may not be wired as canonical
(anti-laundering). Coordinate on `qou-iyj5` (sibling #4515).
