/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.MassTheory.TiltDerivativeCovariance
import QOU.BraidKnot.IdentityIPlancherelConditional

/-!
# `M₁` is the tilt derivative — for the ACTUAL Plancherel measure, not a generic family

Bean `qou-k5r5`, epic `qou-x631`. Sequel to `QOU.MassTheory.TiltDerivativeCovariance`.

That file proved the tilt identity for an arbitrary finite family over an arbitrary field.
On its own that is a lemma about polynomials: it says nothing about Plancherel measure,
about `ω₃`, or about `M₁`. This file discharges its hypothesis **at the corpus's own
Plancherel datum**, which is what turns it into a statement about the gap.

## The hypothesis that had to be discharged

`tilt_deriv_eq_wCov` assumes `wMean w f = 0`. Here `w λ = dim(λ)²` and
`f = ω₃ := Σ_c c² − binom(n,2)`, and the hypothesis is exactly the Plancherel
content-square mean — the fact `qou-ujil` uses to eliminate limit-shape arguments.

It is **not assumed here**. `plancherel_weighted_omega3_sum_eq_zero` derives it from the
two `PlancherelSnData` fields already in the corpus:

* `sum_dim_sq : ∑ dim² = n!`
* `two_sum_dim_sq_content : 2·∑ dim²·Σc² = n(n−1)·n!`

so `∑ dim²·ω₃ = n(n−1)n!/2 − binom(n,2)·n! = 0` **exactly**, by `ring` after casting.

## Epistemic status — read this before citing

`[PlancherelSnData n]` is a **class hypothesis** (AGENTS.md §3b-cond), so every theorem
below is a *conditional* result. The class is not a hole: the corpus inhabits it at every
`n` (`PlancherelSnDataGeneral.plancherelSnDataGeneral`, from RSK + Okounkov–Vershik), and
its unlabelled Wedderburn form is proved unconditionally and sorry-free
(`IdentityBWedderburn.identityB_via_wedderburn_unconditional`). But **conditional-proved is
not premise-established**: state these as "modulo `PlancherelSnData`", never flatly.

## Scope — this is still not the gap

`M₁ > 0` remains **OPEN**. Nothing here bounds the derivative below or determines its sign;
the tilt statistic `hgt` is left arbitrary, so this fixes the *shape* of the reformulation
and not one numerical fact about it. Generality is deliberate: the identity does not need
`hgt = Σ□h`, and pinning it there would claim less while looking like more.
-/

namespace QOU.MassTheory

open Polynomial Finset QOU.BraidKnot.IdentityI

variable (n : ℕ) [h : PlancherelSnData n]

/-- The Plancherel weight `w λ = dim(λ)²`, as a rational. -/
noncomputable def plancherelWeight (l : List ℕ) : ℚ := ((h.dim l : ℚ)) ^ 2

/-- `ω₃(λ) = Σ_c c(c)² − binom(n,2)`, the centred content-square statistic, as a rational.

Kept over `ℚ` rather than `ℤ` because `binom(n,2) = n(n−1)/2` is not an integer-valued
expression in this spelling, and because the tilt identity divides. -/
noncomputable def omega3Q (l : List ℕ) : ℚ :=
  (sumSqContents l : ℚ) - (n : ℚ) * ((n : ℚ) - 1) / 2

/-- **The Plancherel `ω₃`-mean vanishes — derived, not assumed.**

`∑_λ dim(λ)² · ω₃(λ) = 0`, exactly, from the two `PlancherelSnData` fields. This is the
hypothesis of `tilt_deriv_eq_wCov`, and it is the same fact that makes a limit-shape
evaluation of `M₁` return `0 ≤ 0`. -/
theorem plancherel_weighted_omega3_sum_eq_zero :
    ∑ l ∈ h.parts, plancherelWeight n l * omega3Q n l = 0 := by
  have hcontent := h.two_sum_dim_sq_content
  have hdim := h.sum_dim_sq
  have hcontentQ : (2 : ℚ) * ∑ l ∈ h.parts, ((h.dim l : ℚ)) ^ 2 * (sumSqContents l : ℚ)
      = (n : ℚ) * ((n : ℚ) - 1) * (n.factorial : ℚ) := by
    exact_mod_cast congrArg (fun z : ℤ => (z : ℚ)) hcontent
  have hdimQ : ∑ l ∈ h.parts, ((h.dim l : ℚ)) ^ 2 = (n.factorial : ℚ) := by
    exact_mod_cast congrArg (fun z : ℤ => (z : ℚ)) hdim
  simp only [plancherelWeight, omega3Q, mul_sub, Finset.sum_sub_distrib]
  rw [← Finset.sum_mul, hdimQ]
  linarith [hcontentQ]

/-- The Plancherel weighted mean of `ω₃` is zero. -/
theorem plancherel_wMean_omega3_eq_zero :
    wMean h.parts (plancherelWeight n) (omega3Q n) = 0 := by
  rw [wMean, plancherel_weighted_omega3_sum_eq_zero, zero_div]

/-- **`M₁` IS the tilt derivative, at the actual Plancherel measure.**

For *any* integer statistic `hgt` used as the tilt exponent, the derivative at `x = 1` of
the `hgt`-tilted Plancherel mean of `ω₃` equals the Plancherel covariance of `hgt` with
`ω₃`. Taking `hgt = Σ□h` gives `M₁`.

Conditional on `[PlancherelSnData n]` — see the epistemic-status note in the module
docstring. Says nothing about the sign. -/
theorem plancherel_tilt_deriv_eq_wCov (hgt : List ℕ → ℕ) :
    (derivative (tiltNum h.parts (plancherelWeight n) (omega3Q n) hgt)).eval 1
        / (tiltDen h.parts (plancherelWeight n) hgt).eval 1
      = wCov h.parts (plancherelWeight n) (fun l => (hgt l : ℚ)) (omega3Q n) :=
  tilt_deriv_eq_wCov _ _ _ _ (plancherel_wMean_omega3_eq_zero n)

/-- The tilted mean **vanishes at `x = 1`** — the obstruction, stated for the real objects.

This is why evaluating on the limit shape proves nothing: the quantity being computed is
identically zero at the point where such an evaluation happens. The content of the
reformulation is that the *derivative* there is not. -/
theorem plancherel_tiltNum_eval_one_eq_zero (hgt : List ℕ → ℕ) :
    (tiltNum h.parts (plancherelWeight n) (omega3Q n) hgt).eval 1 = 0 := by
  rw [tiltNum_eval_one]
  exact plancherel_weighted_omega3_sum_eq_zero n

end QOU.MassTheory
