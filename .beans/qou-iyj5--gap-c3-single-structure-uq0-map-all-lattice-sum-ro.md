---
# qou-iyj5
title: 'GAP: c3 single-structure u(q0) map — all lattice-sum routes closed (scope-b Thurston); survivor is locating the transcendental singularity q* (= boost-enhancement A=2.05 = NZ radius R~0.1 at the anchor)'
status: todo
type: task
parent: qou-82w7
created_at: 2026-08-01T21:10:52Z
updated_at: 2026-08-01T21:10:52Z
---

## The gap (2026-08-01, after the sum-branch closure)

The c₃ magnitude `|S_p/S_m| ≈ 4.075` and the argument map `u(q₀)` are one open
object. This session closed **all lattice-sum routes** to it:

- single canonical winding pair — 3.9× short (PR #4497)
- multi-winding even-channel sum, quadratic truncation — diverges scope-(a) (PR #4501)
- resurgent one-instanton ratio — circular (PR #4501)
- multi-winding sum, **full 𝔙₄₁** — diverges **scope-(b) via Thurston** (PR #4503):
  the Dehn-surgery bound `Re𝔙 ≤ Vol(4₁)` floors every term at `e^{−Vol/ℏ_q}>0`, so the
  sum diverges for the exact potential too, not just the truncation.

**The sole survivor: the single geometric structure `u(q₀)`.** Fresh reduction:
with the pinned boost `Re u = ln q₀ ≈ 0.104`, the muon anchor is `2.05×` the leading
supremum `(√3/4)(ln q₀)²`; closing that gap under the exact potential needs its NZ
Taylor to have quartic/quadratic ratio `≈ 97`, i.e. **radius of convergence
`R ≈ 0.10 ≈ u` — a transcendental singularity sitting AT the anchor**. Equivalently:
the boost-enhancement `A ≈ 2.05` (= locating `q*`). This is the irreducible open core.

## Next step (the decisive test)

Build the exact figure-8 `𝔙₄₁(u)` by solving the gluing equations numerically
(cross-check against `Vol(4₁)=2.0299` at `u=0` and the `√3/4` leading term), then
**measure its radius of convergence / nearest singularity directly**:

- if `R ≈ 0.1` → the on-anchor-singularity / resurgence picture is vindicated;
- if `R = O(1)` → the boost-enhancement `A` must be geometric (a different mechanism).

This single measurement decides between the two live open readings. Slip-safe
(verified against known anchors). Anti-fit-gated; do NOT fit `A` or `q*`.

## Cross-refs

- Parent: `qou-82w7` (transcendental argument map). Sharpens `qou-3kos` (A≳2.05 bound
  now robust at exact-potential level). Even-channel bean `qou-dtd3` is negative 4 ways.
- Also reconcile with the [W] winding reframe (sibling `udeform-spin-part` sessions):
  on-anchor-singularity vs discrete-winding-channel — make consistent or refute one.
- Audits: docs/audits/2026-08-01-c3-magnitude-full-volume-thurston-sum-exclusion.md and
  the two siblings; docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md.
