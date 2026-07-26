# Faddeev keystone — growth-estimate epic: scope & workplan

**Date:** 2026-07-26 · **Bean epic:** `qou-7xvy` follow-up · **Axis:** G3 / Faddeev
rigidity · **Tier:** scoping (no new Lean claim; a decomposition + tractability
assessment of the sole remaining keystone input). Grounds the next tranche.

## Context

The Faddeev–Volkov uniqueness leg for the physical `Φ_b` is sorry-free modulo **one**
analytic input — the `Φ_b` **divisor-rigidity / growth estimate**
([keystone-state map](../audits/2026-07-25-faddeev-uniqueness-keystone-state.md)). Both
uniqueness routes reduce to it:

- **divisor route** — `hr_entire`: the ratio `Ψ / phiBProd` of two solutions extends to
  entire;
- **growth route** — `hbdd`: that ratio is bounded on `ℂ`.

The prior framing called this "the Écalle–Borel / state-integral growth estimate — a
Mathlib contour-integration gap." This document **re-scopes** that framing after the
input-1 closure (PR #4296) and the `phiBProd`-side divisor computation (PR #4304).

## Headline scoping result: contour integration is NOT required

The state-integral definition
$$\Phi_b(z) = \exp\!\int_{\mathbb{R}+i0}\frac{e^{-2izw}}{4\sinh(wb)\sinh(w/b)}\frac{dw}{w}$$
is the object the "contour-integration gap" referred to. But the growth bound it would
supply is **already available from the product form** (input 1), by elementary
product-norm estimates — **no contour integral, no residue theorem**.

### Mathlib inventory (surveyed 2026-07-26 against pinned `v4.24.0` source)

| Needed for | Mathlib status |
|---|---|
| improper line integral over `ℝ` (`IntegralEqImproper`, `MeasureTheory.integral`) | **present** |
| `CauchyIntegral`, `CircleIntegral`, `intervalIntegral` | **present** |
| **residue theorem** / general contour-shifting along arbitrary paths | **absent** |
| `Multipliable.norm_tprod` (`‖∏' f‖ = ∏' ‖f‖`) | **present** |
| `Real.add_one_le_exp` (`1 + x ≤ eˣ`), `Real.rexp_tsum_eq_tprod` | **present** |
| `tprod_one_add_ne_zero_of_summable` (no spurious zeros) | **present** (used in PR #4304) |

The residue theorem is the genuinely-missing piece for **Route A** (deriving `Φ_b`'s
properties *from* the state integral). It is **not** on the critical path for the
keystone, because **Route B** (below) reaches the growth bound from the product.

## Two routes

### Route A — state integral (NOT recommended; large, blocked on Mathlib)

Formalize the contour definition, prove convergence, derive the functional equations and
growth from it via residue calculus / steepest descent. Blocked on the **absent residue
theorem** and needs steepest-descent asymptotics Mathlib lacks. This is a multi-tranche
undertaking whose only payoff over Route B is *deriving* (rather than *characterizing by*)
the growth condition. **Out of scope** for closing the keystone.

### Route B — product-norm growth (RECOMMENDED; tractable, Mathlib-supported)

On the substrate branch `Im b² > 0`, `phiBProd = (∏ numFactor)/(∏ denFactor)` with
`numFactor = 1 + numExpₖ`, `‖numExpₖ‖ = e^{M(z)}·rⁿ` geometric (`r = e^{Re c} < 1`).
Then, by `Multipliable.norm_tprod` + `1 + x ≤ eˣ` + `rexp_tsum_eq_tprod`:
$$\Big\|\textstyle\prod_k \mathrm{numFactor}_k\Big\| = \prod_k \|1+\mathrm{numExp}_k\|
  \le \prod_k e^{\|\mathrm{numExp}_k\|} = e^{\sum_k \|\mathrm{numExp}_k\|} < \infty,$$
locally uniformly — an **explicit strip bound**. The denominator lower bound (away from its
pole lattice) uses `‖1+a‖ ≥ 1-‖a‖` and `∏(1-‖aₖ‖) ≥ e^{-C\sum\|aₖ\|}`. Together they bound
`‖phiBProd(z)‖` above and below on strips **with no contour integral**.

## Recommended decomposition (Route B bricks)

| # | Brick | Lean target | Mathlib support | Est. |
|---|---|---|---|---|
| G1 | numerator strip **upper** bound | `‖∏ numFactor b · k‖ ≤ exp(S⁺(z))`, `S⁺` the summed factor-norm bound | `Multipliable.norm_tprod`, `Real.add_one_le_exp`, `rexp_tsum_eq_tprod` | S |
| G2 | denominator strip **lower** bound (off dual lattice) | `‖∏ denFactor b · k‖ ≥ exp(−S⁻(z))` | `norm_prod`, `1−‖a‖ ≤ ‖1+a‖`, summability | M |
| G3 | `phiBProd` strip bound | `‖phiBProd b z‖ ≤ exp(S⁺+S⁻)` from G1/G2 | `norm_div` | S |
| G4 | growth-condition **class** (§3b) | `class FaddeevPhiStripGrowth (b) (Φ)` carrying the polynomial-in-strip / bounded-ratio field; **prove `phiBProd` an instance** from G3 | §3b conjecture-class pattern | M |
| G5 | growth ⟹ `hbdd` wiring | two solutions both `[FaddeevPhiStripGrowth]` ⟹ ratio bounded ⟹ `faddeevPhi_proportional_of_bounded_ratio` | existing capstone + `DoublyPeriodicBoundedLocalization` | M |

**Honesty note (anti-laundering).** G4 axiomatizes the *physical characterization* of `Φ_b`
(Faddeev–Kashaev: the shift-solution with prescribed strip growth) as a class field — the
standard, legitimate move. It is **not** a proof of the growth *from first principles*
(that would be Route A). Per §3b-cond it must (i) carry the growth **hypothesis**, not the
conclusion, and (ii) be *satisfied by `phiBProd`* (G4's instance obligation, discharged by
G3) so the class is non-vacuous. The keystone then reads: any solution in the
`FaddeevPhiStripGrowth` class is proportional to `phiBProd` — a rigorous conditional result
modulo the *named, phiBProd-realized* growth characterization, not modulo an unproved axiom.

## Recommendation

Pursue **Route B** (G1→G5). G1/G3 are **S**-sized and land immediately on the product
infrastructure already merged. G2 is the one genuine estimate (denominator lower bound). G4
is the honest characterization; its instance obligation is discharged by G3, so the class is
non-vacuous by construction. Route A (state integral) stays a documented reference
(`FaddeevQuantumDilogarithm` module docstring) — the physical *why*, not a Lean dependency.

The "contour-integration epic" as originally feared **does not exist on the critical path**;
the real remaining work is five product-estimate bricks, all within current Mathlib.

## Progress log

- **G1 + G3** (PR #4328) — `PhiBProdStripBound.lean`: numerator/denominator upper bounds +
  conditional `phiBProd` strip bound.
- **G2 + G4** (PR #4332) — `PhiBProdStripLowerBound.lean` (denominator lower bound ⇒
  *unconditional* strip bound) + `FaddeevPhiStripGrowth.lean` (the growth class,
  `phiBProd` instance, `ratio_bounded_of_stripGrowth`).
- **G5 crux** (this PR) — `MeromorphicPuncturedBounded.lean`: the removable-singularity
  extension, the hard analytic heart of G5.

### G5 assessment (the remaining wiring — no Mathlib gap)

The boundedness capstone needs `hbdd : ∀ z, ‖toMeromorphicNFOn (Φ₁/Φ₂) univ z‖ ≤ C`
(bound at **every** point). G4 supplies the raw-ratio bound only on the **dense**
`{Φ₂ ≠ 0}` locus. The bridge is now proved:

| G5 piece | status |
|---|---|
| removable-singularity extension (punctured bound ⇒ global `hbdd`) | ✅ **proved** — `norm_le_of_bounded_on_punctured` (+ the local order lemma) |
| `Φ₂`'s zeros isolated: `∀ᶠ w in 𝓝[≠] z, Φ₂ w ≠ 0` | assembly — for `phiBProd` from `meromorphicOrderAt ≠ ⊤` (PR #4225) |
| `hr_ratio`: `toMeromorphicNFOn (Φ₁/Φ₂) = Φ₁/Φ₂` off poles | assembly — meromorphic normal-form API |
| `MeromorphicOn Φ₁` (arbitrary second solution) | honest physical hypothesis to add |

None of the remaining pieces is a Mathlib gap: they are API assembly plus one legitimate
meromorphicity hypothesis on the second solution. The analytically-hard step (that a
codiscrete bound extends across removable singularities) is done. Closing G5 is then a
matter of threading `Φ₂ = phiBProd`'s explicit zero-isolation and the normal-form identity
into `norm_le_of_bounded_on_punctured` → `faddeevPhi_proportional_of_bounded_ratio`.
