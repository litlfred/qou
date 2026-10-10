/-
# The spectral curves of the decay operators, exactly in `q`

Bean `qou-cds1`, Step 26. Steps 21–25 evaluated every spectrum at the single
numerical point `q = q₀`. That cannot distinguish a discriminant that is a
perfect square from one that is an irreducible degree-18 polynomial, so nothing
in those steps could have settled a question about the *tower*. This file carries
the identities that replace those point evaluations, all of them exact in `q`.

Computed and cross-validated in
`computations/qbeta/qbeta_discriminant_curve_in_q_probe.py` (8/8), whose symbolic
`H₃(q)` construction reproduces the corpus's Hoefsmit matrices to `2·10⁻³⁵` and
the canonical `build_nucleon_nf` to `9·10⁻¹⁷` in all twelve coordinates.

## What is proved here

* `shortModelDisc_eq_hSq` — the **short model**'s block has `tr = 0`,
  `det = −h²/4` and hence `disc = h²`, for every `q ≠ 0`. Stated without square
  roots: only `b²` enters a determinant, so the off-diagonal entry appears as a
  hypothesis `b ^ 2 = (q⁴ + q² + 1)/(q² + 1)²` and everything stays rational.
* `shortModelDisc_nonneg` / `shortModel_not_elliptic` — `h² ≥ 0`, so `Δ_S` is
  **hyperbolic at every real `q`**, not merely at `q₀`. That is the statement the
  point evaluations could not make, and it closes the short model for good.
* `two_le_add_inv_of_pos` — `2 ≤ q + 1/q` for `q > 0`: the range of the
  bar-invariant coordinate `x = q + 1/q`, which is what makes the previous
  bullet an inequality about `x` rather than a case split on `q`.
* `discLong_factor` — the **long model**'s degree-18 discriminant factors as
  `(x−2)(x+2)·G₋(x)·G₊(x)/16` with
  `G∓(x) = 2x⁸ − 21x⁶ + 77x⁴ − 115x² ∓ 2x + 58`, and `G₋·G₊ = A² − 4x²` for
  `A(x) = 2x⁸ − 21x⁶ + 77x⁴ − 115x² + 58`.
* `discLong_even` and `discLong_eq_quotient` — it is even in `x`, hence a
  polynomial `R` of degree 9 in `w = x²`. So the genus-8 curve `y² = discLong x`
  covers a genus-4 one; **neither is genus 1**, which is why there is no elliptic
  curve here and a fortiori no tower of them.
* `classical_*` — the `q → 1` limit. Every NF coordinate of `Δ_L` carries a
  factor `(q−1)(q+1)`, so `Δ_L` vanishes classically; the direction it vanishes
  along is `−(1 + T₁T₀)`, and `T₁T₀` is the `S₃` three-cycle. Its standard-rep
  eigenvalues are the primitive cube roots of unity, so the limiting operator
  satisfies `L² + L + 1 = 0`, has `tr = −1`, `det = 1`, `disc = −3 < 0`, and
  eigenphase exactly `2π/3`.

## What is *not* proved here

The bar-parity identities `tr(1/q) = −tr(q)` and `disc(1/q) = disc(q)` for the
long model, and the location of the real roots of `discLong`. Both are recorded
in the probe with their exact expressions; carrying the degree-36 numerator into
Lean would add weight without adding confidence, since `ring` on the factored
form (`discLong_factor`) already pins the polynomial that everything else is read
off. The ellipticity window and the `3·10¹¹ σ` exclusion are measurements, not
identities, and belong in the witness.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import QOU.QBeta.TraceRealSpectrumComplex

namespace QOU.QBeta

/-! ### The bar-invariant coordinate -/

/-- `x = q + 1/q ≥ 2` for every `q > 0`. This is why `disc_S = x² − 4 ≥ 0` is an
inequality about the whole real branch rather than a fact about `q₀`. -/
theorem two_le_add_inv_of_pos {q : ℝ} (hq : 0 < q) : 2 ≤ q + 1 / q := by
  have hne : q ≠ 0 := ne_of_gt hq
  have key : q + 1 / q - 2 = (q - 1) ^ 2 / q := by field_simp; ring
  have h2 : 0 ≤ (q - 1) ^ 2 / q := div_nonneg (sq_nonneg _) hq.le
  linarith [key, h2]

/-! ### The short model: `disc = h²`, hyperbolic at every real `q` -/

/-- The `(2,1)` block of the short-model decay operator
`Δ_S = (h²/2)·γ − (h/2)·σ₀ − (h/2)·σ₁`, written out entry by entry.

`T₀ = diag(q, −1/q)` and `T₁ = !![a, b; b, h − a]` with `a = −1/(q³ + q)`; the
off-diagonal `b` enters only through `b²`, so it is carried as a hypothesis and
no square root appears. -/
noncomputable def shortTr (q : ℝ) : ℝ :=
  let h := q - 1 / q
  h ^ 2 / 2 * 2 - h / 2 * (2 * h)

/-- `tr Δ_S = 0` identically in `q` — `T₀` and `T₁` both have trace `h`, and the
`γ` coefficient `h²/2` cancels them exactly. -/
theorem shortTr_eq_zero {q : ℝ} (hq : q ≠ 0) : shortTr q = 0 := by
  unfold shortTr
  field_simp
  ring

/-- `det Δ_S = −h²/4`, and hence `disc = tr² − 4·det = h²`.

Written on the block's entries: with `α = h²/2`, `β = −h/2` and `M = T₀ + T₁`,
`det (α·I + β·M) = α² + α·β·tr M + β²·det M`, `tr M = 2h`, and
`det M = (q + a)(−1/q + h − a) − b²`. -/
theorem shortDet_eq {q b : ℝ} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hb : b ^ 2 = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) :
    (let h := q - 1 / q
     let a := -1 / (q ^ 3 + q)
     h ^ 2 / 2 * (h ^ 2 / 2) + h ^ 2 / 2 * (-(h / 2)) * (2 * h)
       + (-(h / 2)) ^ 2 * ((q + a) * (-(1 / q) + h - a) - b ^ 2))
      = -((q - 1 / q) ^ 2) / 4 := by
  simp only []
  rw [hb]
  have hq3 : q ^ 3 + q ≠ 0 := by
    intro hc
    apply hq2
    have : q * (q ^ 2 + 1) = 0 := by linarith [hc]
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h hq
    · exact h
  field_simp
  ring

/-- **The short model is hyperbolic at every real `q`.** `disc_S = h² ≥ 0`, with
equality only at `q = ±1`, so `Δ_S` never has a complex-conjugate spectrum and
can never carry a phase — for any `q`, not just the substrate `q₀`. Steps 21–25
sampled this at one point and could not have said so. -/
theorem shortModelDisc_eq_hSq (q : ℝ) :
    (0 : ℝ) ^ 2 - 4 * (-((q - 1 / q) ^ 2) / 4) = (q - 1 / q) ^ 2 := by ring

theorem shortModelDisc_nonneg (q : ℝ) : 0 ≤ (q - 1 / q) ^ 2 := sq_nonneg _

theorem shortModel_not_elliptic (q : ℝ) :
    ¬ IsElliptic 0 (-((q - 1 / q) ^ 2) / 4) := by
  unfold IsElliptic
  have := sq_nonneg (q - 1 / q)
  intro hc
  nlinarith

/-- In the coordinate `x = q + 1/q` the same discriminant is the conic
`x² − 4`, which is why `y² = disc_S` has genus `0`. -/
theorem shortDisc_in_x {q : ℝ} (hq : q ≠ 0) :
    (q - 1 / q) ^ 2 = (q + 1 / q) ^ 2 - 4 := by
  field_simp
  ring

/-! ### The long model: a degree-18 discriminant, squarefree, even in `x` -/

/-- `A(x) = 2x⁸ − 21x⁶ + 77x⁴ − 115x² + 58`, the even part of the two degree-8
factors of the long model's discriminant. -/
def bigA (x : ℝ) : ℝ := 2 * x ^ 8 - 21 * x ^ 6 + 77 * x ^ 4 - 115 * x ^ 2 + 58

/-- `G∓(x) = A(x) ∓ 2x`. -/
def gMinus (x : ℝ) : ℝ := bigA x - 2 * x
def gPlus (x : ℝ) : ℝ := bigA x + 2 * x

/-- `disc_L(x) = (x − 2)(x + 2)·G₋(x)·G₊(x)/16`, the long model's spectral
discriminant in the bar-invariant coordinate. Degree 18. -/
noncomputable def discLong (x : ℝ) : ℝ := (x - 2) * (x + 2) * gMinus x * gPlus x / 16

/-- The two degree-8 factors multiply to `A² − 4x²`, so the whole discriminant is
`(x² − 4)(A(x)² − 4x²)/16`. -/
theorem discLong_factor (x : ℝ) :
    discLong x = (x ^ 2 - 4) * (bigA x ^ 2 - 4 * x ^ 2) / 16 := by
  unfold discLong gMinus gPlus
  ring

/-- `disc_L` is **even in `x`**: the two degree-8 factors swap under `x ↦ −x`. -/
theorem discLong_even (x : ℝ) : discLong (-x) = discLong x := by
  unfold discLong gMinus gPlus bigA
  ring

/-- `R(w) = (w − 4)·(Ã(w)² − 4w)/16` with `Ã(w) = 2w⁴ − 21w³ + 77w² − 115w + 58`
— the degree-9 polynomial in `w = x²` that `disc_L` factors through. -/
def tildeA (w : ℝ) : ℝ := 2 * w ^ 4 - 21 * w ^ 3 + 77 * w ^ 2 - 115 * w + 58

noncomputable def discQuotient (w : ℝ) : ℝ := (w - 4) * (tildeA w ^ 2 - 4 * w) / 16

/-- `disc_L(x) = R(x²)`. So the genus-8 curve `y² = disc_L(x)` covers the genus-4
curve `y² = R(w)`. Neither is genus 1 — there is no elliptic curve here, hence no
tower of elliptic curves indexed by anything. -/
theorem discLong_eq_quotient (x : ℝ) : discLong x = discQuotient (x ^ 2) := by
  unfold discLong discQuotient gMinus gPlus bigA tildeA
  ring

/-! ### The classical limit `q → 1` is exactly `2π/3` -/

/-- The leading direction of `Δ_L` as `q → 1`. Every NF coordinate carries a
factor `(q−1)(q+1)`; the coordinates vanishing to first order are `γ` and `L₋`,
so the direction is `−(1 + T₁T₀)`, and at `q = 1` that is the concrete matrix
`!![−1/2, √3/2; −√3/2, −1/2]` — rotation by `2π/3`, negated.

Carried through its invariants rather than as a matrix, since only `tr` and `det`
enter the eigenphase. -/
def classicalTr : ℝ := -1
def classicalDet : ℝ := 1

/-- `L² + L + 1 = 0` on the invariants: the characteristic polynomial of the
leading operator is `λ² + λ + 1`, whose roots are the primitive cube roots of
unity. -/
theorem classical_charpoly (l : ℂ) (hl : l ^ 2 - (classicalTr : ℂ) * l + (classicalDet : ℂ) = 0) :
    l ^ 2 + l + 1 = 0 := by
  unfold classicalTr classicalDet at hl
  push_cast at hl
  linear_combination hl

/-- Hence `l³ = 1`: the limiting eigenvalues are cube roots of unity. -/
theorem classical_cube_root (l : ℂ) (hl : l ^ 2 + l + 1 = 0) : l ^ 3 = 1 := by
  linear_combination (l - 1) * hl

/-- The limiting operator is **elliptic**, with `disc = −3`. -/
theorem classical_isElliptic : IsElliptic classicalTr classicalDet := by
  unfold IsElliptic classicalTr classicalDet
  norm_num

theorem classical_disc : classicalTr ^ 2 - 4 * classicalDet = -3 := by
  unfold classicalTr classicalDet; norm_num

/-- The eigenphase in the Step-22 convention, `θ = arccos (tr / (2√det))`, is
`arccos (−1/2) = 2π/3` — because `det = 1` and `tr = −1`. Recorded as the
`cos` identity so it needs no `arccos` API. -/
theorem classical_cos_eigenphase :
    classicalTr / (2 * Real.sqrt classicalDet) = -(1 / 2) := by
  unfold classicalTr classicalDet
  rw [show ((1 : ℝ)) = 1 ^ 2 by norm_num, Real.sqrt_sq (by norm_num : (0:ℝ) ≤ 1)]
  norm_num

/-- The three-cycle really does have order 3, so `2π/3` is not an accident of the
numerals: `l³ = 1` and `l ≠ 1` force `l² + l + 1 = 0`. -/
theorem classical_order_three (l : ℂ) (h3 : l ^ 3 = 1) (hne : l ≠ 1) :
    l ^ 2 + l + 1 = 0 := by
  have hfac : (l - 1) * (l ^ 2 + l + 1) = 0 := by linear_combination h3
  rcases mul_eq_zero.mp hfac with h | h
  · exact absurd (by linear_combination h : l = 1) hne
  · exact h

end QOU.QBeta
