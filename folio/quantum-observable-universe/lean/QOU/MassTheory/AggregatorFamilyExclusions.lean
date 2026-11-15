import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Which convex aggregators the three-point grid can already exclude

`QOU.MassTheory.AggregatorConvexityDichotomy` narrowed the many-body binding
magnitude to **convex-through-the-origin** aggregators: writing
`B(A) = Φ(m_A · g)` for the total bond weight, the measured `b₃ = +1.4262225`
excludes every concave-through-the-origin `Φ`, and AME's own `Φ` is convex and
strictly superadditive on the grid the light nuclei supply.

That is a *class*, not a candidate. This file supplies the two exclusion tests
that the same three data points can run against a proposed `Φ` **without fitting
anything**, so the next candidate is checked before it is believed.

Both are ordinary consistency conditions — the point is that the grid has three
points and the families have fewer than three parameters, so each leaves a
residual identity that the data either satisfies or does not.

## Test 1 — two-parameter linear families (`not_realizable_of_det3_ne_zero`)

`Φ(x) = c·x + a·ψ(x)` for a **fixed** shape `ψ` and free `(c, a)` — the
volume-plus-correction form, of which the semi-empirical
volume-minus-surface `c·x − a·x^{2/3}` is the canonical member, and which is
exactly the shape the convexity result points at (a linear term minus a concave
deficit is convex, and its secant ratio `Φ(x)/x → c` is bounded, so it is
compatible with saturation).

Three points, two parameters, one residual: realizability forces the `3 × 3`
determinant of `(x, ψ, Φ)` to vanish (`det3_eq_zero_of_realizable`). A nonzero
determinant therefore **excludes the whole family for that `ψ`** — every `(c, a)`
at once, with no fit performed and no optimisation involved.

## Test 2 — pure power laws (`powerLaw_log_ratio`)

`Φ(x) = c·x^p`. Its log-ratio across a scale factor `k` is `p·log k`,
*independent of where on the ray you measure it* — so the local exponent
extracted between any two grid points is the same number. Two grid intervals
give two extractions, and if they disagree the family is excluded
(`not_powerLaw_of_log_ratios_differ`).

## Scope

Both are scope-**(b)** exclusions for the families as stated, with the invariant
proved here rather than cited. Neither excludes anything outside its family. In
particular:

* Test 1 excludes a **two**-parameter family. The full semi-empirical formula
  carries Coulomb, asymmetry and pairing terms as well; on `Z = N` light nuclei
  the asymmetry term vanishes, but three points cannot test a three-or-more
  parameter form at all — it is underdetermined, hence **untestable here**, not
  excluded here. Do not report a `det3 ≠ 0` as excluding "the SEMF".
* Test 2 excludes exact power laws, not functions that merely look like one over
  a range.

Neither test identifies `Φ`. They are filters, and they exist because the
surviving class after the convexity dichotomy is still large.
-/

namespace QOU.MassTheory.AggregatorFamily

open Real

/-! ### Test 1 — two-parameter linear families -/

/-- The data `φ` is realizable on the grid `x` by the two-parameter family
`c·x + a·ψ` for **some** choice of the two parameters. -/
def Realizable (x ψ φ : Fin 3 → ℝ) : Prop :=
  ∃ c a : ℝ, ∀ i, φ i = c * x i + a * ψ i

/-- The `3 × 3` determinant of the columns `(x, ψ, φ)`. -/
def det3 (x ψ φ : Fin 3 → ℝ) : ℝ :=
  x 0 * (ψ 1 * φ 2 - ψ 2 * φ 1)
    - ψ 0 * (x 1 * φ 2 - x 2 * φ 1)
    + φ 0 * (x 1 * ψ 2 - x 2 * ψ 1)

/-- **Realizability forces the determinant to vanish.** If the data is a linear
combination of the two shape columns then the three columns are dependent. No
hypothesis on `x` or `ψ` is needed — in particular the grid need not be
increasing and the shapes need not be independent. -/
theorem det3_eq_zero_of_realizable {x ψ φ : Fin 3 → ℝ} (h : Realizable x ψ φ) :
    det3 x ψ φ = 0 := by
  obtain ⟨c, a, h⟩ := h
  simp only [det3, h 0, h 1, h 2]
  ring

/-- **The exclusion, as a candidate filter.** A nonzero determinant rules out the
entire two-parameter family for that shape `ψ` — every `(c, a)` simultaneously,
with nothing fitted. -/
theorem not_realizable_of_det3_ne_zero {x ψ φ : Fin 3 → ℝ} (h : det3 x ψ φ ≠ 0) :
    ¬ Realizable x ψ φ := fun hr => h (det3_eq_zero_of_realizable hr)

/-- **Non-vacuity.** The determinant does vanish on data that *is* realizable, so
the test is not excluding everything. -/
theorem det3_eq_zero_of_construction (x ψ : Fin 3 → ℝ) (c a : ℝ) :
    det3 x ψ (fun i => c * x i + a * ψ i) = 0 :=
  det3_eq_zero_of_realizable ⟨c, a, fun _ => rfl⟩

/-- **The test has teeth.** A grid on which the determinant is nonzero exists, so
`not_realizable_of_det3_ne_zero` has non-empty hypotheses. -/
theorem det3_ne_zero_example :
    det3 ![1, 2, 3] ![1, 4, 9] ![0, 0, 1] ≠ 0 := by
  norm_num [det3, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons]

/-! ### Test 2 — pure power laws -/

/-- **A pure power law has a scale-invariant log-ratio.** For `Φ x = c · x^p` the
quantity `log Φ(k·x) − log Φ(x)` is `p · log k` — it depends on the scale factor
`k` alone and not on where along the ray it is measured. That is the identity the
three-point grid tests twice. -/
theorem powerLaw_log_ratio {c p x k : ℝ} (hc : 0 < c) (hx : 0 < x) (hk : 0 < k) :
    log (c * (k * x) ^ p) - log (c * x ^ p) = p * log k := by
  have hkx : (0:ℝ) < k * x := mul_pos hk hx
  rw [log_mul (ne_of_gt hc) (ne_of_gt (rpow_pos_of_pos hkx p)),
      log_mul (ne_of_gt hc) (ne_of_gt (rpow_pos_of_pos hx p)),
      log_rpow hkx, log_rpow hx, log_mul (ne_of_gt hk) (ne_of_gt hx)]
  ring

/-- **The exclusion.** If the exponent extracted across one scale factor differs
from the exponent extracted across another, no single `p` — and hence no pure
power law `c · x^p` — reproduces both. Stated as the contrapositive of
`powerLaw_log_ratio` applied at two base points. -/
theorem not_powerLaw_of_log_ratios_differ
    {c p x₁ x₂ k₁ k₂ : ℝ} (hc : 0 < c) (hx₁ : 0 < x₁) (hx₂ : 0 < x₂)
    (hk₁ : 0 < k₁) (hk₂ : 0 < k₂) (hlk₁ : log k₁ ≠ 0) (hlk₂ : log k₂ ≠ 0)
    (hne : (log (c * (k₁ * x₁) ^ p) - log (c * x₁ ^ p)) / log k₁
         ≠ (log (c * (k₂ * x₂) ^ p) - log (c * x₂ ^ p)) / log k₂) : False := by
  rw [powerLaw_log_ratio hc hx₁ hk₁, powerLaw_log_ratio hc hx₂ hk₂,
      mul_div_assoc, mul_div_assoc, div_self hlk₁, div_self hlk₂] at hne
  exact hne rfl

end QOU.MassTheory.AggregatorFamily
