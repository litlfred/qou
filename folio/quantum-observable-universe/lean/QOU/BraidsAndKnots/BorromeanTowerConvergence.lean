/-
  Borromean brane-tower convergence: the TRUE Li₂^q radius bound.

  The per-braid brane tower `B_tower = B_can⁰ + E₀·z²·Σ_pairs g(τᵢτⱼ·f)`
  with `g(x) = −Li₂^q(−x)` converges iff every pair argument satisfies
  `|τᵢτⱼ·f| < q` (the Li₂^q radius). The 2026-06-28 formalize-first plan
  (docs/audits/2026-06-28-brane-tower-formalize-first-plan.md §4-§5)
  REFUTED the originally-planned atom-word bound `|tr_M(ξ)| < q₀` (the
  colour-weighted proton trace is 1.0653 > 1; the free pp pair exceeds
  the radius, exact counterexample at ⁴He H₁₂) and directed that the
  TRUE bound be Lean'd instead: the Borromean nucleon trace satisfies
  `|tr_M(β_Bor)| < 1`, hence every pair trace is `< q₀`.

  This file proves that bound from the closed form in
  `QOU.BraidsAndKnots.BorromeanMarkovTrace`:

    tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

  1. `trM_borromean_lt_one`      — t < 1 for every h ≠ 0 (the numerator
     deficit is `3h⁴ + h⁶ > 0`; exactly the strict inequality that fails
     at h = 0, where t = 1).
  2. `abs_trM_borromean_lt_one`  — |t| < 1 on the physical domain h² ≤ 1
     (substrate h₀ = q₀ − q₀⁻¹ ≈ 0.209, h₀² ≈ 0.0437 ≪ 1).
  3. `pair_trace_lt_radius`      — generic: |t| < 1 and 1 < q give
     |t·t| < q (the free-pair radius bound).
  4. `pair_trace_dressed_lt_radius` — the interface-dressed pair
     |t·t·f| < q for any bond factor |f| ≤ 1 (covers f_pp = f_pn = z
     and f_nn = z − h, both in (0,1) at q₀).
  5. `borromean_pair_within_radius` — the composite: the Borromean pair
     argument is inside the Li₂^q radius for every q > 1 on the
     physical domain.

  Archimedean layer: ordering is intrinsic here, so the section lives
  over `ℚ` like the parent file's quotient/positivity section (§7c —
  no gratuitous `ℝ`; the substrate evaluation at q₀ descends from ℚ
  statements by monotone limits downstream).

  What is NOT claimed: no statement about the colour-weighted atom-word
  traces (refuted bound), and no numeric evaluation at q₀ — the h² ≤ 1
  hypothesis is discharged downstream where h₀ is constructed.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kashaev1995] https://doi.org/10.1142/S0217732395001526
-/
import QOU.BraidsAndKnots.BorromeanMarkovTrace
import Mathlib.Algebra.Order.AbsoluteValue.Basic

namespace QOU.BraidsAndKnots

/-! ## Strict trace bound: `tr_M(β_Bor) < 1` away from `h = 0` -/

/-- **The Borromean trace is strictly below 1 for every `h ≠ 0`.**
    From the closed form, `1 − t = (3h⁴ + h⁶)/(h² + 4)` with a positive
    numerator when `h ≠ 0`. At `h = 0` the trace is exactly 1
    (`isBorromeanMarkovTrace_one_at_zero`), so the hypothesis is sharp. -/
theorem trM_borromean_lt_one (h : ℚ) (hh : h ≠ 0) :
    trM_borromean h < 1 := by
  have hden : trM_borromean_den h > 0 := trM_borromean_den_pos h
  have h4 : 0 < h ^ 4 := by positivity
  unfold trM_borromean
  rw [div_lt_one₀ hden]
  unfold trM_borromean_num trM_borromean_den
  nlinarith [sq_nonneg h, sq_nonneg (h ^ 2), h4]

/-- **Two-sided bound on the physical domain.** For `h ≠ 0` with
    `h² ≤ 1` (the substrate has `h₀² ≈ 0.0437`), the trace also stays
    above `−1`: the numerator plus denominator is `8 + 2h² − 3h⁴ − h⁶ ≥
    8 − 2h² ≥ 6 > 0`. Combined with `trM_borromean_lt_one`, `|t| < 1`. -/
theorem abs_trM_borromean_lt_one (h : ℚ) (hh : h ≠ 0) (hsmall : h ^ 2 ≤ 1) :
    |trM_borromean h| < 1 := by
  have hden : trM_borromean_den h > 0 := trM_borromean_den_pos h
  have hlt : trM_borromean h < 1 := trM_borromean_lt_one h hh
  have hgt : -1 < trM_borromean h := by
    unfold trM_borromean
    rw [lt_div_iff₀ hden]
    unfold trM_borromean_num trM_borromean_den
    nlinarith [sq_nonneg h, sq_nonneg (h ^ 2), sq_nonneg (h ^ 3)]
  exact abs_lt.mpr ⟨hgt, hlt⟩

/-! ## Li₂^q radius bounds for the pair arguments -/

/-- **Free-pair radius bound (generic).** Any trace value with `|t| < 1`
    has its pair argument `t·t` inside the Li₂^q radius `q` for `q > 1`. -/
theorem pair_trace_lt_radius (t q : ℚ) (ht : |t| < 1) (hq : 1 < q) :
    |t * t| < q := by
  have h0 : (0 : ℚ) ≤ |t| := abs_nonneg t
  have : |t * t| < 1 := by
    rw [abs_mul]
    nlinarith
  linarith

/-- **Interface-dressed pair radius bound.** The bound survives dressing
    by any bond factor with `|f| ≤ 1` (at q₀ the Phase 5q factors are
    `f_pp = f_pn = z ≈ 0.499` and `f_nn = z − h ≈ 0.290`, both in
    `(0,1)`; their membership is a downstream numeric fact). -/
theorem pair_trace_dressed_lt_radius (t f q : ℚ)
    (ht : |t| < 1) (hf : |f| ≤ 1) (hq : 1 < q) :
    |t * t * f| < q := by
  have h0 : (0 : ℚ) ≤ |t| := abs_nonneg t
  have h1 : (0 : ℚ) ≤ |f| := abs_nonneg f
  have : |t * t * f| < 1 := by
    rw [abs_mul, abs_mul]
    nlinarith
  linarith

/-- **The composite convergence bound** (the TRUE bound of the
    formalize-first plan): on the physical domain (`h ≠ 0`, `h² ≤ 1`)
    the Borromean free-pair argument is inside the Li₂^q radius for
    every `q > 1`. Together with `pair_trace_dressed_lt_radius` this
    gives convergence of every pair term of the brane tower over the
    Borromean nucleon — for ALL Z, with no per-isotope hypothesis. -/
theorem borromean_pair_within_radius (h q : ℚ)
    (hh : h ≠ 0) (hsmall : h ^ 2 ≤ 1) (hq : 1 < q) :
    |trM_borromean h * trM_borromean h| < q :=
  pair_trace_lt_radius _ q (abs_trM_borromean_lt_one h hh hsmall) hq

/-- **Interface-dressed Borromean nucleon pair convergence bound (`bean moqg`).**
    On the physical domain (`h ≠ 0`, `h² ≤ 1`), for any bond factor `|f| ≤ 1`
    and any `q > 1`, the dressed pair argument `|tr_M(β_Bor)² · f|` lies strictly
    inside the `Li₂^q` convergence radius `q`. -/
theorem borromean_dressed_pair_within_radius (h f q : ℚ)
    (hh : h ≠ 0) (hsmall : h ^ 2 ≤ 1) (hf : |f| ≤ 1) (hq : 1 < q) :
    |trM_borromean h * trM_borromean h * f| < q :=
  pair_trace_dressed_lt_radius _ f q (abs_trM_borromean_lt_one h hh hsmall) hf hq

end QOU.BraidsAndKnots
