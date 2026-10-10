---
# qou-iyj5
title: 'REDUCED: c3 single-structure u(q0) map — lattice-sum routes closed (scope-b Thurston); on-anchor-singularity REFUTED (R=2logφ≈0.96, #4508); survivor is the NZ-½ boost factor A≈2 (c=√2), precision-ceilinged → successor qou-yh67'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T21:10:52Z
updated_at: 2026-10-04T15:23:18Z
parent: qou-avtq
---

## RESOLUTION (2026-08-07 read of the merged decisive test + sibling)

**The original title's `R ≈ 0.1` / on-anchor-singularity hypothesis is REFUTED.** The
decisive test (PR #4508, merged) measured the radius directly from the figure-8
A-polynomial branch points: `R = 2·log φ ≈ 0.9624` (golden ratio; nearest branch at
meridian eigenvalue `M = φ`), validated against the proved `√3/4` leading coefficient.
The anchor `u = ln q₀ ≈ 0.104 = 0.108·R` is **deep inside** — so `u(q₀)` is smoothly
analytic and there is **no singularity near the anchor**. The `2.05×` boost gap is
therefore NOT an analytic near-singularity (and #4509, merged: the `dc₃/dq ≈ 10⁶`
"hypersensitivity" is a `1/u³` extraction artifact, not physical).

**Survivor reduced to a named, binary, precision-limited question (REDUCED, scope-a).**
- The gap is unambiguously a `Re u` boost-rapidity enhancement `c = √A ≈ 1.4305`
  (exact-CS integral, PR #4515; spin part only *decreases* `Im 𝔙₄₁`).
- The clean value `A = 2` (`c = √2`) is **Lean-exact** = the Neumann–Zagier ½ potential
  normalization: `κ_shape/κ_pot = (√3/2)/(√3/4) = 2` (`BoostFactorNZNormalization.lean`,
  merged; audit `2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md`).
  So "why `c=√A`?" reduces to: *does the bar-odd leak `S` carry the NZ-½ potential form
  (`A=1`) or the raw cusp-shape form (`A=2`)?*
- **Precision ceiling:** `σ_A ≈ 40 % ≫` the `≤ 2.63 %` clean-candidate spread
  (`{A=2, q₀+q₀⁻¹, Vol(4₁), q₀²+q₀⁻², 2.054}`). The measurement **cannot identify** which
  constant `c` equals — pushing it as a high-precision hunt is numerology (PR #1805
  pattern). Verdict: **REDUCED, not derived, not refuted.**

**Status:** at terminus for what measurement can do. The honest remaining open content is
the binary NZ-½ normalization question, tracked in the successor bean **`qou-yh67`**
(the derivation must come from structure, not a precision fit). This bean (`qou-iyj5`)
is superseded by that reduction; keep for history.

## History — the gap (2026-08-01, before the decisive test)


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
