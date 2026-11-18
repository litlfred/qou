import Mathlib.LinearAlgebra.CrossProduct
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# The Frenet framing of `T(2, q)` on the torus jumps at `r = 4 / (q² + 4)`

`computations/probes/the_torsion_half_is_not_an_invariant_probe.py` (bean `qou-m3sh`)
measures total curvature, total torsion, writhe and the Frenet self-linking
`Lk_F = Wr + (1/2π)∮τ ds` along the family of torus embeddings

    γ(t) = ((1 + r cos qt) cos 2t, (1 + r cos qt) sin 2t, r sin qt),   0 < r < 1,

of the `(2, q)`-torus knot, `q` odd. It found `Lk_F` integral at every `r` but NOT
constant: `-2q` on the fat side and `-q` on the thin side, the jump sitting where the
sampled curvature minimum touched zero. So even the integer half of Călugăreanu is not an
invariant of the knot type — the Frenet framing is a framing of the *curve*, and it is
discontinuous across an inflection.

This file proves the algebra of where that happens. At `t = π/q` one has `cos qt = -1`,
`sin qt = 0`, and with `ρ = 1 - r`, `c = cos(2π/q)`, `s = sin(2π/q)` the derivatives are

    γ'(π/q)  = (-2ρ s, 2ρ c, -q r),
    γ''(π/q) = ((q² r - 4ρ) c, (q² r - 4ρ) s, 0)

(the differentiation is done symbolically by the probe and NOT formalised here; the two
vectors are taken as the definitions `vel` and `acc`). Their cross product is

    γ' × γ'' = (q² r - 4ρ) · (q r s, -q r c, -2ρ (c² + s²))          (`cross_vel_acc`)

and the second factor is non-zero for `r < 1`, so the curvature vanishes at `t = π/q`
exactly when `q² r = 4(1 - r)`, i.e. `r = 4 / (q² + 4)` (`inflection_iff`). For the
three component types of the canonical closure that is `r* = 4/13, 4/29, 4/53`
(`inflection_radius_three_five_seven`) — the trefoil value matches the probe's
golden-section estimate `0.307692` — and `cos(q t) = -1` at the `q` distinct parameters
`t_k = (2k + 1)π/q`, `k < q` (`cos_q_mul_inflection`, `inflection_params_injective`),
which is why the jump in `Lk_F` is by `q`.

Not formalised: that `γ'` and `γ''` are the derivatives of `γ`, that these are the only
inflections of the family, and the jump itself (a statement about framings). Bean `qou-m3sh`.
-/

namespace QOU.Mass.TorusInflection

/-- `γ'(π/q)` written with `c = cos(2π/q)`, `s = sin(2π/q)`: `(-2(1-r) s, 2(1-r) c, -q r)`. -/
def vel (q r c s : ℝ) : Fin 3 → ℝ := ![-2 * (1 - r) * s, 2 * (1 - r) * c, -(q * r)]

/-- `γ''(π/q)`: `((q² r - 4(1-r)) c, (q² r - 4(1-r)) s, 0)`. -/
def acc (q r c s : ℝ) : Fin 3 → ℝ :=
  ![(q ^ 2 * r - 4 * (1 - r)) * c, (q ^ 2 * r - 4 * (1 - r)) * s, 0]

/-- The cross product at `t = π/q` factors through `q² r - 4(1 - r)`. -/
theorem cross_vel_acc (q r c s : ℝ) :
    crossProduct (vel q r c s) (acc q r c s)
      = (q ^ 2 * r - 4 * (1 - r)) • ![q * r * s, -(q * r * c), -2 * (1 - r) * (c ^ 2 + s ^ 2)] := by
  rw [cross_apply]
  ext i
  fin_cases i <;> simp [vel, acc] <;> ring

/-- **The inflection radius.** For `0 < q`, `r < 1` and `c² + s² = 1`, the curvature of the
torus embedding vanishes at `t = π/q` iff `r = 4 / (q² + 4)`. -/
theorem inflection_iff (q r c s : ℝ) (hq : 0 < q) (hr : r < 1) (hcs : c ^ 2 + s ^ 2 = 1) :
    crossProduct (vel q r c s) (acc q r c s) = 0 ↔ r = 4 / (q ^ 2 + 4) := by
  rw [cross_vel_acc]
  have hq4 : q ^ 2 + 4 ≠ 0 := by positivity
  constructor
  · intro h
    have h2 : (q ^ 2 * r - 4 * (1 - r)) * (-2 * (1 - r) * (c ^ 2 + s ^ 2)) = 0 := by
      simpa using congrFun h 2
    rw [hcs] at h2
    rcases mul_eq_zero.1 h2 with h0 | h0
    · field_simp
      linear_combination h0
    · exfalso
      linarith
  · intro h
    have h0 : q ^ 2 * r - 4 * (1 - r) = 0 := by
      rw [h]
      field_simp
      ring
    rw [h0, zero_smul]

/-- The three component types of the canonical closure. -/
theorem inflection_radius_three_five_seven :
    (4 : ℝ) / (3 ^ 2 + 4) = 4 / 13 ∧ (4 : ℝ) / (5 ^ 2 + 4) = 4 / 29 ∧
      (4 : ℝ) / (7 ^ 2 + 4) = 4 / 53 := by
  norm_num

/-- At `t_k = (2k + 1)π/q` one has `cos(q t_k) = -1`. -/
theorem cos_q_mul_inflection (q : ℕ) (hq : 0 < q) (k : ℕ) :
    Real.cos ((q : ℝ) * ((2 * k + 1) * Real.pi / q)) = -1 := by
  have hq' : (q : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
  have : (q : ℝ) * ((2 * k + 1) * Real.pi / q) = Real.pi + k * (2 * Real.pi) := by
    field_simp
    ring
  rw [this, Real.cos_add_nat_mul_two_pi, Real.cos_pi]

/-- The `q` parameters `t_k`, `k < q`, are distinct: the inflections come `q` at a time. -/
theorem inflection_params_injective (q : ℕ) :
    Function.Injective (fun k : Fin q => (2 * (k : ℝ) + 1) * Real.pi / q) := by
  intro a b hab
  have hpi := Real.pi_pos
  simp only at hab
  have h : (2 * (a : ℝ) + 1) * Real.pi = (2 * (b : ℝ) + 1) * Real.pi := by
    rcases Nat.eq_zero_or_pos q with hq | hq
    · exact absurd a.isLt (by simp [hq])
    · have hq' : (q : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
      exact (div_left_inj' hq').1 hab
  have h2 : (a : ℝ) = b := by
    have := mul_right_cancel₀ hpi.ne' h
    linarith
  exact Fin.ext (by exact_mod_cast h2)

/-- Additive residual form of `cos_q_mul_inflection`: `Real.cos ((q : ℝ) * ((2 * k + 1) * Real.pi / q)) + 1 = 0`. -/
theorem cos_q_mul_inflection_add_one_eq_zero (q : ℕ) (hq : 0 < q) (k : ℕ) :
    Real.cos ((q : ℝ) * ((2 * k + 1) * Real.pi / q)) + 1 = 0 := by
  rw [cos_q_mul_inflection q hq k, neg_add_cancel]

end QOU.Mass.TorusInflection
