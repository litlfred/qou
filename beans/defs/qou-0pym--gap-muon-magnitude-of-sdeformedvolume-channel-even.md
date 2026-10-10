---
# qou-0pym
title: 'GAP: muon magnitude of SDeformedVolume channel — boost-rapidity factor c=√A≈1.43'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:34:46Z
updated_at: 2026-10-10T08:30:00Z
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DUPLICATE.** Duplicate of qou-yh67. Note also that its A=2.054 rests on the superseded CODATA-2018 muon S_leak and on a central value whose CAL-3 uncertainty (±1.262, qbeta-c3-barodd-sleak.witness.json) is 126x the value.

Evidence: Same gap as yh67 (`c=√A≈1.43`), and yh67 is the declared successor of qou-iyj5, which 0pym says to coordinate on. A=2.054 uses the superseded CODATA-2018 `S_mu=0.00968298`. Witness `S_uncertainty.muon=1.262` gives sigma_A ≈ 268. The cited Lean (`imV₄₁_le_cuspModulus_reSq`, `imV₄₁_leading_unreachable_of_lt`, FigureEightComplexVolume.lean:252,265) is sorry-free but is algebra on the defined quadratic `V₄₁`.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
