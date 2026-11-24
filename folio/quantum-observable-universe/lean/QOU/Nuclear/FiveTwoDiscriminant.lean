import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Polyrith

/-!
# The GGM curve's discriminant vanishes on `|x| = 1`

Bean `qou-trns`; the Lean form of Route 16
(`computations/probes/qbeta_5two_route16_discriminant_vanishes_probe.py`).

## What this refutes

`qou-trns` recorded the transport's sub-gap 1 as **closed** — "`k = 0` is pinned
by the base point" — with a step that reads

> "The three branches `yⱼ(x)` are continuous and **never collide on the arc**
> (`min |disc| = 0.348`), so `g` is continuous."

and stated the envelope theorem's implicit-function hypothesis as satisfied, on
the same constant. **Both are false.** The discriminant has a zero on the unit
circle, so two branches collide there.

`0.348` was a *grid* minimum from an ~360-point scan of `[0, π]`; the dip is
narrow (`|disc'| ≈ 87`), so refining the scan gives 0.068, then 0.0068, then 0.

## Why this is Lean-sized

The refutation needs no analysis of the branches at all. Three ingredients:

1. `disc` is the standard cubic discriminant of the GGM curve — a `ring`
   identity (`disc_eq_cubic_formula`).
2. `disc` is **palindromic**, so `disc x = x⁴ · Q (x + 1/x)` with
   `Q u = u⁴ − 6u³ + 7u² + 6u − 31` — a `field_simp; ring` identity
   (`disc_eq_Q`).
3. `Q (−2) = 49 > 0 > −23 = Q (−1)`, so `Q` has a real root in `(−2,−1)` by the
   intermediate value theorem. Points of `|x| = 1` are exactly those with
   `x + 1/x` real in `[−2,2]`, and `(−2,−1)` is inside it.

So the whole thing is polynomial algebra plus IVT, and `Q_neg_two`/`Q_neg_one`
are `norm_num`.

## Scope

This refutes the *argument*. It does **not** endanger the transport's
conclusion: Route 17 shows `S(e^{iφ}) − S(1) = φ²` holds to `4e-40` **through**
the branch point, because `S` sums over all roots and is therefore symmetric —
a collision permutes roots, and a symmetric function cannot notice a
permutation. Only the per-root labelling dies, and only the argument used
labels.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDiscriminant

/-- The GGM deformed 5₂ curve as a cubic in `y`: at `x = 1` it is the 5₂
polynomial `y³ − 2y² + 3y − 1`. -/
noncomputable def ggm (x y : ℂ) : ℂ := x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x

/-- `disc_y` of `ggm`, expanded. Palindromic. -/
noncomputable def disc (x : ℂ) : ℂ :=
  x ^ 8 - 6 * x ^ 7 + 11 * x ^ 6 - 12 * x ^ 5 - 11 * x ^ 4 - 12 * x ^ 3 + 11 * x ^ 2 - 6 * x + 1

/-- `disc` really is the standard cubic discriminant
`18abcd − 4b³d + b²c² − 4ac³ − 27a²d²` of `ggm`, whose coefficients are
`a = x`, `b = −(x²+1)`, `c = x²+x+1`, `d = −x`. -/
theorem disc_eq_cubic_formula (x : ℂ) :
    18 * x * (-(x ^ 2 + 1)) * (x ^ 2 + x + 1) * (-x)
        - 4 * (-(x ^ 2 + 1)) ^ 3 * (-x)
        + (-(x ^ 2 + 1)) ^ 2 * (x ^ 2 + x + 1) ^ 2
        - 4 * x * (x ^ 2 + x + 1) ^ 3
        - 27 * x ^ 2 * (-x) ^ 2 = disc x := by
  unfold disc; ring

/-- At `x = 1` the curve is the 5₂ polynomial and the discriminant is `−23`. -/
theorem disc_one : disc 1 = -23 := by unfold disc; norm_num

theorem ggm_one (y : ℂ) : ggm 1 y = y ^ 3 - 2 * y ^ 2 + 3 * y - 1 := by unfold ggm; ring

/-- The palindromic reduction, over `ℂ`. -/
noncomputable def Qc (u : ℂ) : ℂ := u ^ 4 - 6 * u ^ 3 + 7 * u ^ 2 + 6 * u - 31

/-- …and over `ℝ`, where the sign change lives. -/
noncomputable def Q (u : ℝ) : ℝ := u ^ 4 - 6 * u ^ 3 + 7 * u ^ 2 + 6 * u - 31

/-- **The palindromic reduction.** `disc x = x⁴ · Q(x + 1/x)`. -/
theorem disc_eq_Q {x : ℂ} (hx : x ≠ 0) : disc x = x ^ 4 * Qc (x + 1 / x) := by
  unfold disc Qc
  field_simp
  ring

theorem Qc_ofReal (u : ℝ) : Qc (u : ℂ) = (Q u : ℂ) := by
  unfold Qc Q; push_cast; ring

/-! ### The sign change — integer arithmetic -/

theorem Q_neg_two : Q (-2) = 49 := by unfold Q; norm_num

theorem Q_neg_one : Q (-1) = -23 := by unfold Q; norm_num

theorem Q_continuous : Continuous Q := by
  unfold Q; fun_prop

/-- **`Q` has a real root in `(−2,−1)`.** This is the whole refutation: `(−2,−1)`
sits inside `[−2,2]`, which is exactly the range of `x + 1/x` on `|x| = 1`. -/
theorem exists_root_Q : ∃ u : ℝ, u ∈ Set.Ioo (-2 : ℝ) (-1) ∧ Q u = 0 := by
  have hmem : (0 : ℝ) ∈ Set.Ioo (Q (-1)) (Q (-2)) := by
    rw [Q_neg_one, Q_neg_two]; constructor <;> norm_num
  obtain ⟨u, hu, hqu⟩ :=
    intermediate_value_Ioo' (by norm_num : (-2 : ℝ) ≤ -1) Q_continuous.continuousOn hmem
  exact ⟨u, hu, hqu⟩

/-! ### From a root of `Q` to a point of the unit circle

For `u ∈ [−2,2]` the point `x = u/2 + i·√(1 − u²/4)` has `‖x‖ = 1` and
`x + 1/x = u`. That is the correspondence the reduction trades on. -/

/-- The unit-circle point with `x + 1/x = u`. -/
noncomputable def onCircle (u : ℝ) : ℂ := ⟨u / 2, Real.sqrt (1 - u ^ 2 / 4)⟩

theorem normSq_onCircle {u : ℝ} (h2 : -2 ≤ u) (h2' : u ≤ 2) :
    Complex.normSq (onCircle u) = 1 := by
  have hnn : (0 : ℝ) ≤ 1 - u ^ 2 / 4 := by nlinarith
  simp only [onCircle, Complex.normSq_mk]
  rw [Real.mul_self_sqrt hnn]
  ring

theorem norm_onCircle {u : ℝ} (h2 : -2 ≤ u) (h2' : u ≤ 2) : ‖onCircle u‖ = 1 := by
  have h := normSq_onCircle h2 h2'
  have : ‖onCircle u‖ ^ 2 = 1 := by
    rw [← Complex.normSq_eq_norm_sq]  -- ‖z‖^2 = normSq z
    exact h
  nlinarith [norm_nonneg (onCircle u), this]

theorem onCircle_ne_zero {u : ℝ} (h2 : -2 ≤ u) (h2' : u ≤ 2) : onCircle u ≠ 0 := by
  intro h
  have := norm_onCircle h2 h2'
  rw [h] at this
  simp at this

/-- `x + 1/x = u` at the circle point. -/
theorem onCircle_add_inv {u : ℝ} (h2 : -2 ≤ u) (h2' : u ≤ 2) :
    onCircle u + 1 / onCircle u = (u : ℂ) := by
  have hne := onCircle_ne_zero h2 h2'
  have hsq : onCircle u * (starRingEnd ℂ) (onCircle u) = 1 := by
    rw [Complex.mul_conj]
    exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) (normSq_onCircle h2 h2')
  have hinv : 1 / onCircle u = (starRingEnd ℂ) (onCircle u) := by
    field_simp
    linear_combination -hsq
  rw [hinv]
  simp only [onCircle, Complex.ext_iff, Complex.add_re, Complex.add_im, Complex.conj_re,
    Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im]
  constructor <;> ring

/-- **The refutation.** There is a point of the unit circle at which the GGM
curve's discriminant vanishes — so two of its three `y`-branches collide there,
and `min |disc| = 0` on `|x| = 1`, not `0.348`. -/
theorem exists_unit_circle_disc_zero : ∃ x : ℂ, ‖x‖ = 1 ∧ disc x = 0 := by
  obtain ⟨u, hu, hqu⟩ := exists_root_Q
  have h2 : (-2 : ℝ) ≤ u := le_of_lt hu.1
  have h2' : u ≤ 2 := by linarith [hu.2]
  refine ⟨onCircle u, norm_onCircle h2 h2', ?_⟩
  rw [disc_eq_Q (onCircle_ne_zero h2 h2'), onCircle_add_inv h2 h2', Qc_ofReal, hqu]
  simp

end QOU.QBeta.FiveTwoDiscriminant
