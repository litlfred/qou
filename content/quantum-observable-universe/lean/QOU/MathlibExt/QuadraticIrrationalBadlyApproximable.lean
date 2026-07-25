import Mathlib.RingTheory.Real.Irrational
import Mathlib.Algebra.Order.Round

/-!
# Quadratic surds are badly approximable — a Mathlib-gap lemma

Mathlib knows `Irrational (Real.sqrt D)` (for non-square `D`) but does not carry the
classical **badly-approximable** lower bound: for `α = √D` there is `c > 0` with
`‖jα‖ ≥ c/j` for every `j ≥ 1`, where `‖·‖ = |· − round ·|` is the distance to the
nearest integer.  Equivalently, the continued-fraction partial quotients of a quadratic
surd are bounded — but the bound here is proved *elementarily*, with no continued-fraction
machinery, from the single arithmetic fact that `D j² − p²` is a **nonzero integer**
(hence `|D j² − p²| ≥ 1`).

This is the number-theoretic input the Dilog Part B W-P1 limit needs to make the
no-resonance / `wp1_tendsto_of_powerBound` hypothesis unconditional for `x = e^{−√D}`:
the maximal-cell branch-point gap is `≈ {j√D}·(q_j − 1) ≥ (c/j)·(q_j − 1) ≈ c·(q_j − 1)²`
(the quadratic bound `K = 2`).

`sqrt_badlyApproximable` : `∃ c > 0, ∀ j ≥ 1, c/j ≤ ‖j√D‖`.

-- Ref: [manuscript] bean qou-jplv; Liouville-type bound for quadratic irrationals
-/

namespace QOU.MathlibExt

open scoped Topology

/-- **Quadratic surds are badly approximable.**  For `α = √D` irrational there is
    `c > 0` with `c/j ≤ |jα − round(jα)|` for all `j ≥ 1`.  Elementary: with
    `p = round(jα)`, the integer `D j² − p²` is nonzero (else `α = p/j` is rational),
    so `|D j² − p²| ≥ 1`; factoring `(jα − p)(jα + p) = D j² − p²` and bounding
    `|jα + p| ≤ (2α + 1)·j` gives `|jα − p| ≥ 1/((2α+1) j)`. -/
theorem sqrt_badlyApproximable {D : ℕ} (hD : Irrational (Real.sqrt (D : ℝ))) :
    ∃ c : ℝ, 0 < c ∧ ∀ j : ℕ, 1 ≤ j →
      c / (j : ℝ) ≤ |(j : ℝ) * Real.sqrt (D : ℝ) - (round ((j : ℝ) * Real.sqrt (D : ℝ)) : ℝ)| := by
  set α : ℝ := Real.sqrt (D : ℝ) with hα
  have hα0 : 0 ≤ α := Real.sqrt_nonneg _
  -- α > 0 and α² = D
  have hD1 : (D : ℝ) ≠ 0 := by
    intro h; exact hD (by rw [hα, h, Real.sqrt_zero]; exact ⟨0, by norm_num⟩)
  have hDpos : (0 : ℝ) < (D : ℝ) := lt_of_le_of_ne (Nat.cast_nonneg D) (Ne.symm hD1)
  have hαpos : 0 < α := Real.sqrt_pos.mpr hDpos
  have hαsq : α ^ 2 = (D : ℝ) := Real.sq_sqrt hDpos.le
  refine ⟨1 / (2 * α + 1), by positivity, ?_⟩
  intro j hj
  have hjR : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have hjpos : (0 : ℝ) < (j : ℝ) := by linarith
  set p : ℤ := round ((j : ℝ) * α) with hp
  -- p ≥ 0 since jα ≥ 0
  have hjα0 : 0 ≤ (j : ℝ) * α := by positivity
  have hp0 : 0 ≤ p := by
    have hb := abs_sub_round ((j : ℝ) * α)
    rw [← hp] at hb
    have hb2 : (j : ℝ) * α - (p : ℝ) ≤ 1 / 2 := (abs_le.mp hb).2
    have hlt : (-1 : ℝ) < (p : ℝ) := by linarith [hjα0]
    have hz : (-1 : ℤ) < p := by exact_mod_cast hlt
    omega
  have hpnn : (0 : ℝ) ≤ (p : ℝ) := by exact_mod_cast hp0
  -- the integer D j² − p² is nonzero
  have hne : (D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 ≠ 0 := by
    intro heq
    -- from D j² = p² (ℤ) get (jα)² = p², hence jα = p (both ≥ 0), so α = p/j rational
    have hZR : (D : ℝ) * (j : ℝ) ^ 2 = (p : ℝ) ^ 2 := by
      have h2 : (((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ) = 0 := by exact_mod_cast heq
      push_cast at h2; linarith
    have hsq : ((j : ℝ) * α) ^ 2 = ((p : ℝ)) ^ 2 := by rw [mul_pow, hαsq]; linarith [hZR]
    have hjαp : (j : ℝ) * α = (p : ℝ) := by
      have h1 : |(j : ℝ) * α| = |(p : ℝ)| := by
        rw [← Real.sqrt_sq_eq_abs, ← Real.sqrt_sq_eq_abs, hsq]
      rwa [abs_of_nonneg hjα0, abs_of_nonneg hpnn] at h1
    have hdiv : α = (p : ℝ) / (j : ℝ) := by rw [eq_div_iff hjpos.ne', mul_comm]; exact hjαp
    exact hD ⟨(p : ℚ) / (j : ℚ), by push_cast; rw [hdiv]⟩
  -- |D j² − p²| ≥ 1
  have hge1 : (1 : ℝ) ≤ |(D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2| := by
    have hcast : (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2
        = (((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ) := by push_cast; ring
    rw [hcast]
    have : (1 : ℤ) ≤ |(D : ℤ) * (j : ℤ) ^ 2 - p ^ 2| := Int.one_le_abs hne
    calc (1 : ℝ) = ((1 : ℤ) : ℝ) := by norm_num
      _ ≤ ((|(D : ℤ) * (j : ℤ) ^ 2 - p ^ 2| : ℤ) : ℝ) := by exact_mod_cast this
      _ = |(((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ)| := by rw [Int.cast_abs]
  -- factorization (jα − p)(jα + p) = D j² − p²
  have hfac : ((j : ℝ) * α - (p : ℝ)) * ((j : ℝ) * α + (p : ℝ))
      = (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2 := by
    have : ((j : ℝ) * α) ^ 2 = (D : ℝ) * (j : ℝ) ^ 2 := by rw [mul_pow, hαsq]; ring
    nlinarith [this]
  -- |jα + p| ≤ (2α + 1) j
  have hround : |(j : ℝ) * α - (p : ℝ)| ≤ 1 / 2 := by
    rw [hp]; exact abs_sub_round ((j : ℝ) * α)
  have hp_le : (p : ℝ) ≤ (j : ℝ) * α + 1 / 2 := by
    have := (abs_le.mp hround).1; linarith
  have hsum_nn : 0 ≤ (j : ℝ) * α + (p : ℝ) := add_nonneg hjα0 hpnn
  have hsum_le : |(j : ℝ) * α + (p : ℝ)| ≤ (2 * α + 1) * (j : ℝ) := by
    rw [abs_of_nonneg hsum_nn]; nlinarith [hp_le, hjR, hαpos.le]
  -- |jα + p| > 0
  have hjα_pos : 0 < (j : ℝ) * α := mul_pos hjpos hαpos
  have hsum_pos : 0 < |(j : ℝ) * α + (p : ℝ)| := by
    rw [abs_of_nonneg hsum_nn]; linarith [hjα_pos, hpnn]
  -- assemble: |jα − p| = |D j² − p²| / |jα + p| ≥ 1/((2α+1) j)
  have habs_prod : |(j : ℝ) * α - (p : ℝ)| * |(j : ℝ) * α + (p : ℝ)|
      = |(D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2| := by rw [← abs_mul, hfac]
  have hlb : 1 ≤ |(j : ℝ) * α - (p : ℝ)| * |(j : ℝ) * α + (p : ℝ)| := by
    rw [habs_prod]; exact hge1
  -- so |jα − p| ≥ 1 / |jα + p| ≥ 1 / ((2α+1) j) = c / j
  have hstep : 1 / ((2 * α + 1) * (j : ℝ)) ≤ |(j : ℝ) * α - (p : ℝ)| := by
    rw [div_le_iff₀ (by positivity)]
    calc (1 : ℝ) ≤ |(j : ℝ) * α - (p : ℝ)| * |(j : ℝ) * α + (p : ℝ)| := hlb
      _ ≤ |(j : ℝ) * α - (p : ℝ)| * ((2 * α + 1) * (j : ℝ)) :=
          mul_le_mul_of_nonneg_left hsum_le (abs_nonneg _)
  calc (1 / (2 * α + 1)) / (j : ℝ) = 1 / ((2 * α + 1) * (j : ℝ)) := by
        rw [div_div]
    _ ≤ |(j : ℝ) * α - (p : ℝ)| := hstep

end QOU.MathlibExt
