import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.LinearCombination

/-!
# The affine causality cone and its boosts (bean `qou-2k68`, routes 2a and 2b)

`def:contact-affine-chart` gives the affine coordinate `Z = α_H / (ι_ξ α)` on the contact affine
chart of the projective line object, and the speed-of-light remark evaluates it on the
`q`-connection to `c_q = q⁻¹ / ℏ_q`. In homogeneous coordinates `[ω : u]` (Reeb component,
horizontal component) the chart is `Z = u / ω`, and the causality cone of the chart is
`|Z| < c` with null points `Z = ±c`.

This file derives the Lorentzian structure from those two null points alone, with no trace:

* `quadratic_with_cone_roots`: a binary quadratic form `A ω² + B ω u + C u²` vanishing at
  `[1 : c]` and `[1 : -c]` is `-C · (c² ω² - u²)`. So the cone fixes the form `coneForm`
  up to scale (route 2b's missing signature).
* `boostLin` and `coneForm_boostLin`: the linear maps `(ω, u) ↦ (ω + v u / c², u + v ω)`
  multiply `coneForm` by `1 - v²/c²`, so they preserve it projectively.
* `boost`, `boost_fix_pos`, `boost_fix_neg` and `boost_comp`: in the affine coordinate these maps
  are `Z ↦ (Z + v) / (1 + v Z / c²)`. They fix both null points and compose by relativistic
  velocity addition (route 2a: boosts as the projective stabiliser of the cone).
* `boost_preserves_cone`: over an ordered field, `|Z| < c` and `|v| < c` imply `|boost Z| < c`.

What this does NOT give: the mass. The einbein elimination of `coneForm`
(`ReebWorldlineSignature.einbein_stationary_value`) produces `-m √(c² ω² - u²)` with `m` a free
parameter, so `BraidBoostInertialEquivalence` stays open. It now has a well-posed form: a braid's
inertial mass is the coefficient `m` once its traced Lagrangian along a worldline is shown to be
boost-covariant in this sense.
-/

namespace QOU.Core.AffineCausalityCone

section Generic

variable {K : Type*} [Field K]

/-- The cone form `c² ω² - u²` on homogeneous coordinates `[ω : u]` of the affine chart. -/
def coneForm (c ω u : K) : K := c ^ 2 * ω ^ 2 - u ^ 2

/-- On the affine chart (`ω = 1`), the null points of the cone form are exactly `Z = ±c`. -/
theorem coneForm_null_iff (c Z : K) : coneForm c 1 Z = 0 ↔ Z = c ∨ Z = -c := by
  unfold coneForm
  constructor
  · intro h
    have h' : (Z - c) * (Z + c) = 0 := by linear_combination -h
    rcases mul_eq_zero.mp h' with h1 | h1
    · left; linear_combination h1
    · right; linear_combination h1
  · rintro (rfl | rfl) <;> ring

/-- **The cone fixes the form.** If `A ω² + B ω u + C u²` vanishes at `[1 : c]` and `[1 : -c]`
(with `2 ≠ 0`, `c ≠ 0`), it equals `-C · coneForm c ω u`. -/
theorem quadratic_with_cone_roots {A B C c : K} (h2 : (2 : K) ≠ 0) (hc : c ≠ 0)
    (hp : A + B * c + C * c ^ 2 = 0) (hm : A - B * c + C * c ^ 2 = 0) (ω u : K) :
    A * ω ^ 2 + B * ω * u + C * u ^ 2 = -C * coneForm c ω u := by
  have hB : B = 0 := by
    have h2Bc : (2 : K) * (B * c) = 0 := by linear_combination hp - hm
    rcases mul_eq_zero.mp h2Bc with h | h
    · exact absurd h h2
    · rcases mul_eq_zero.mp h with h | h
      · exact h
      · exact absurd h hc
  have hA : A = -C * c ^ 2 := by linear_combination hp - c * hB
  unfold coneForm
  rw [hA, hB]
  ring

/-- The linear boost on homogeneous coordinates: `(ω, u) ↦ (ω + v u / c², u + v ω)`. -/
def boostLin (c v ω u : K) : K × K := (ω + v * u / c ^ 2, u + v * ω)

/-- The linear boost multiplies the cone form by `1 - v²/c²`. -/
theorem coneForm_boostLin {c : K} (hc : c ≠ 0) (v ω u : K) :
    coneForm c (boostLin c v ω u).1 (boostLin c v ω u).2 =
      (1 - v ^ 2 / c ^ 2) * coneForm c ω u := by
  unfold coneForm boostLin
  field_simp
  ring

/-- The boost in the affine coordinate: `Z ↦ (Z + v) / (1 + v Z / c²)`. -/
def boost (c v Z : K) : K := (Z + v) / (1 + v * Z / c ^ 2)

/-- The affine boost is the projective image of the linear boost at `ω = 1`. -/
theorem boost_eq_ratio (c v Z : K) :
    boost c v Z = (boostLin c v 1 Z).2 / (boostLin c v 1 Z).1 := by
  simp [boost, boostLin]

/-- Cleared-denominator form: `boost c v Z = c² (Z + v) / (c² + v Z)` (for `c ≠ 0`; both sides
are `0` when the denominator vanishes). -/
theorem boost_eq {c : K} (hc : c ≠ 0) (v Z : K) :
    boost c v Z = c ^ 2 * (Z + v) / (c ^ 2 + v * Z) := by
  unfold boost
  have hc2 : c ^ 2 ≠ 0 := pow_ne_zero 2 hc
  have h : 1 + v * Z / c ^ 2 = (c ^ 2 + v * Z) / c ^ 2 := by field_simp
  rw [h, div_div_eq_mul_div, mul_comm]

/-- The boost fixes the null point `+c` (when `c + v ≠ 0`). -/
theorem boost_fix_pos {c v : K} (hc : c ≠ 0) (hd : c + v ≠ 0) : boost c v c = c := by
  rw [boost_eq hc]
  have h : c ^ 2 + v * c = c * (c + v) := by ring
  rw [h, div_eq_iff (mul_ne_zero hc hd)]
  ring

/-- The boost fixes the null point `-c` (when `c - v ≠ 0`). -/
theorem boost_fix_neg {c v : K} (hc : c ≠ 0) (hd : c - v ≠ 0) : boost c v (-c) = -c := by
  rw [boost_eq hc]
  have h : c ^ 2 + v * -c = c * (c - v) := by ring
  rw [h, div_eq_iff (mul_ne_zero hc hd)]
  ring

/-- Relativistic velocity addition. -/
def vadd (c v w : K) : K := (v + w) / (1 + v * w / c ^ 2)

/-- **Boosts compose by velocity addition**, where the cleared denominators
`c² + w Z` and `c² + v w` are non-zero. -/
theorem boost_comp {c v w Z : K} (hc : c ≠ 0) (h1 : c ^ 2 + w * Z ≠ 0)
    (h2 : c ^ 2 + v * w ≠ 0) :
    boost c v (boost c w Z) = boost c (vadd c v w) Z := by
  have hc2 : c ^ 2 ≠ 0 := pow_ne_zero 2 hc
  have hv : vadd c v w = c ^ 2 * (v + w) / (c ^ 2 + v * w) := by
    unfold vadd
    have h : 1 + v * w / c ^ 2 = (c ^ 2 + v * w) / c ^ 2 := by field_simp
    rw [h, div_div_eq_mul_div, mul_comm]
  rw [boost_eq hc, boost_eq hc, boost_eq hc, hv]
  have d1 : c ^ 2 + v * (c ^ 2 * (Z + w) / (c ^ 2 + w * Z)) =
      c ^ 2 * (c ^ 2 + v * w + (v + w) * Z) / (c ^ 2 + w * Z) := by
    rw [eq_div_iff h1, add_mul, mul_assoc, div_mul_cancel₀ _ h1]; ring
  have d2 : c ^ 2 + c ^ 2 * (v + w) / (c ^ 2 + v * w) * Z =
      c ^ 2 * (c ^ 2 + v * w + (v + w) * Z) / (c ^ 2 + v * w) := by
    rw [eq_div_iff h2, add_mul, mul_right_comm, div_mul_cancel₀ _ h2]; ring
  have hA : (c ^ 2 * (Z + w) / (c ^ 2 + w * Z) + v) * (c ^ 2 + w * Z) =
      c ^ 2 * (Z + w) + v * (c ^ 2 + w * Z) := by
    rw [add_mul, div_mul_cancel₀ _ h1]
  have hB : (Z + c ^ 2 * (v + w) / (c ^ 2 + v * w)) * (c ^ 2 + v * w) =
      Z * (c ^ 2 + v * w) + c ^ 2 * (v + w) := by
    rw [add_mul, div_mul_cancel₀ _ h2]
  rw [d1, d2, div_div_eq_mul_div, div_div_eq_mul_div, mul_assoc, hA, mul_assoc, hB]
  congr 1
  ring

end Generic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Boosts preserve the causality cone.** If `0 < c`, `|Z| < c` and `|v| < c`, then
`|boost c v Z| < c`. -/
theorem boost_preserves_cone {c v Z : K} (hc : 0 < c) (hZ : |Z| < c) (hv : |v| < c) :
    |boost c v Z| < c := by
  obtain ⟨hZl, hZr⟩ := abs_lt.mp hZ
  obtain ⟨hvl, hvr⟩ := abs_lt.mp hv
  have p1 : 0 < (c - Z) * (c - v) := mul_pos (by linarith) (by linarith)
  have p2 : 0 < (c + Z) * (c + v) := mul_pos (by linarith) (by linarith)
  have hden : 0 < c ^ 2 + v * Z := by nlinarith
  rw [boost_eq (ne_of_gt hc), abs_lt]
  constructor
  · rw [lt_div_iff₀ hden]
    nlinarith [mul_pos hc p2]
  · rw [div_lt_iff₀ hden]
    nlinarith [mul_pos hc p1]

end Ordered

end QOU.Core.AffineCausalityCone
