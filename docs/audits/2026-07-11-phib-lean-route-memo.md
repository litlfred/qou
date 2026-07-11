# Φ_b Lean build route — decision memo (contour vs combinatorial)

**Date:** 2026-07-11 · **Axis:** Faddeev Φ_b (T3, decay/bar-odd face) · **Tier:** route decision, no formalization performed here.
**Beans:** `qou-qsme` (formalize contour integral), `qou-5843` (tetraplectic combinatorial reduction), session `qou-rwwa`.
**Numerical ground truth:** [`phi-b-substrate-regime.witness.json`](../../computations/qbeta/phi-b-substrate-regime.witness.json) (10/10 battery, this PR).

## The question

`QOU.MathlibExt.FaddeevQuantumDilogarithm` (landed on main, commit `cded140c`)
axiomatizes `FaddeevPhi b Φ` as a §3b conjecture-class carrying the two
modular-double shift equations. The open build question: how to go beyond the
class — construct an actual `Φ` and discharge the instance. Two candidate
routes were on the table:

1. **Contour-integral machinery** — formalize
   `log Φ_b(z) = ∫_{ℝ+i0} e^{-2izw} / (4w·sinh(wb)·sinh(w/b)) dw`
   directly. Mathlib has no support for this class of contour integral
   (oscillatory kernel, pole-avoiding contour, shift-equation proofs via
   residue bookkeeping). Research-grade, multi-session, high risk.

2. **Combinatorial evaluation** (à la the tetraplectic reduction, bean
   `qou-5843`) — replace the integral by exact discrete algebra.

## Decision: route 2, via the modular-double PRODUCT at the substrate branch

The substrate-regime battery (this PR) settles the choice mechanically. At the
physical anchors (real q₀ > 1) with the pinned b-map
`b = √(ln q₀/2π)·e^{+iπ/4}`:

- **The modular-double product EQUALS the contour integral to 1e-39 at both
  anchors** (S5). The product
  `Φ_b(z) = ∏_{k≥0} (1 + q^{2k+1}·e^{2πbz}) / (1 + q̃^{2k+1}·e^{2πz/b})`
  (with `q = e^{iπb²}`, `q̃ = e^{-iπ/b²}`, both `|·| < 1` on this branch) is an
  absolutely convergent product of algebraic factors — exactly the "discrete
  algebraic domain" object the tetraplectic bean asks for. **No contour
  integration is needed to have Φ_b at the physical anchors.**
- Both shift equations hold for the product by **index re-shifting** (S3
  validated it product-side) — the same cocycle argument as the merged finite
  `qPochProd_add` backbone (PR #3500), taken to the infinite product.
- The dual half is exactly `|q̃|^{1/2} ≈ 1e-82`-suppressed at real
  substrate-scale arguments (S6), so the compact-T1 backbone is recovered as
  the product's numerator half — the T1 ↔ T3 boundary is a factorization, not
  a discontinuity.

**Lean plan (follow-up branch, medium effort — not research-grade):**

1. Define `phiBProd (b : ℂ) (z : ℂ) : ℂ` as a `tprod` over `ℕ` of the two
   factor families (Mathlib has `Multipliable`/`tprod` in Banach algebras; the
   factors converge geometrically for `Im b² > 0`).
2. Prove `Multipliable` from the geometric bound (`|q|^k` majorant).
3. Prove the two shift equations by re-indexing (`Equiv.addRight 1` on the
   product index; telescoping leaves the `k = 0` factor — the finite-product
   cocycle `qPochProd_add` argument in the limit).
4. **Instantiate `FaddeevPhi b (phiBProd b)`** — discharging the §3b class
   with a genuine inhabitant on the `Im b² > 0` branch. The conjecture-class
   then carries real content exactly where it is open: the `|q| = 1` fibre
   regime (real b), where the product genuinely diverges and only the contour
   integral defines Φ_b. That remaining case stays the honest class-conjecture.

## What stays open (scope-honest)

- `|q| = 1` (real b, fibre/root-of-unity regime): contour-only; route 1 would
  be needed there. Not required for the substrate-anchor S-leak program.
- The S-leak argument identification itself: the 60-readout substrate-canonical
  scan (this PR) is a clean scope-(a) negative — the menu as-is does not
  reproduce `S(muon)/S(proton)`; the well-posed continuation is the un-levered
  target `r = S·u³` (slope ≈ −2.4, smooth) over the c_b-lattice / complex-
  argument space ([`qbeta-c3-phib-argument-scan.witness.json`](../../computations/qbeta/qbeta-c3-phib-argument-scan.witness.json)).

## Cross-references

- S-leak target: [`2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md)
- T3 class scaffold: `content/quantum-observable-universe/lean/QOU/MathlibExt/FaddeevQuantumDilogarithm.lean`
- T1 backbone + infinite-product workplan: [`2026-07-11-q-dilog-infinite-product.md`](../workplans/2026-07-11-q-dilog-infinite-product.md)
- Chirality/bar-odd source note: main commit `cfe961d6`
