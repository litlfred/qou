import Mathlib.RingTheory.Real.Irrational
import Mathlib.Algebra.Order.Round
import Mathlib.Algebra.Order.Group.Abs

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

-- Ref: [leitner2026] bean qou-jplv; Liouville-type bound for quadratic irrationals
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

/-- **Fractional-part form.**  For `α = √D` irrational, `c/j ≤ {jα}` for all `j ≥ 1`
    (`{·} = Int.fract`).  This is the shape the Dilog Part B maximal-cell branch-point
    gap needs (the gap is `≈ {j√D}·(q_j − 1)`).  Proved directly with `p = ⌊jα⌋`: since
    `p ≤ jα`, `jα + p ≤ 2αj` (no `1/2` slack), and `D j² − p²` is a positive integer
    (`{jα} = 0` would make `jα = p ∈ ℤ`, contradicting irrationality), so
    `{jα} = jα − p = (D j² − p²)/(jα + p) ≥ 1/(2αj)`. -/
theorem sqrt_fract_badlyApproximable {D : ℕ} (hD : Irrational (Real.sqrt (D : ℝ))) :
    ∃ c : ℝ, 0 < c ∧ ∀ j : ℕ, 1 ≤ j → c / (j : ℝ) ≤ Int.fract ((j : ℝ) * Real.sqrt (D : ℝ)) := by
  set α : ℝ := Real.sqrt (D : ℝ) with hα
  have hα0 : 0 ≤ α := Real.sqrt_nonneg _
  have hD1 : (D : ℝ) ≠ 0 := by
    intro h; exact hD (by rw [hα, h, Real.sqrt_zero]; exact ⟨0, by norm_num⟩)
  have hDpos : (0 : ℝ) < (D : ℝ) := lt_of_le_of_ne (Nat.cast_nonneg D) (Ne.symm hD1)
  have hαpos : 0 < α := Real.sqrt_pos.mpr hDpos
  have hαsq : α ^ 2 = (D : ℝ) := Real.sq_sqrt hDpos.le
  refine ⟨1 / (2 * α), by positivity, ?_⟩
  intro j hj
  have hjR : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have hjpos : (0 : ℝ) < (j : ℝ) := by linarith
  have hjα0 : 0 ≤ (j : ℝ) * α := by positivity
  set p : ℤ := ⌊(j : ℝ) * α⌋ with hp
  have hp0 : 0 ≤ p := Int.floor_nonneg.mpr hjα0
  have hpnn : (0 : ℝ) ≤ (p : ℝ) := by exact_mod_cast hp0
  have hple : (p : ℝ) ≤ (j : ℝ) * α := by rw [hp]; exact Int.floor_le _
  have hfr : Int.fract ((j : ℝ) * α) = (j : ℝ) * α - (p : ℝ) := by rw [hp, Int.fract]
  rw [hfr]
  -- D j² − p² is a positive integer
  have hne : (D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 ≠ 0 := by
    intro heq
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
  have hge1 : (1 : ℝ) ≤ (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2 := by
    have hnn : (0 : ℝ) ≤ (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2 := by
      have : ((j : ℝ) * α) ^ 2 = (D : ℝ) * (j : ℝ) ^ 2 := by rw [mul_pow, hαsq]; ring
      nlinarith [this, hple, hpnn, hjα0]
    have hcast : (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2
        = (((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ) := by push_cast; ring
    have hz1 : (1 : ℤ) ≤ (D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 := by
      rcases lt_or_gt_of_ne hne with h | h
      · exfalso; rw [hcast] at hnn; have : ((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) < 0 := h
        have : (((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ) < 0 := by exact_mod_cast this
        linarith
      · omega
    calc (1 : ℝ) = ((1 : ℤ) : ℝ) := by norm_num
      _ ≤ (((D : ℤ) * (j : ℤ) ^ 2 - p ^ 2 : ℤ) : ℝ) := by exact_mod_cast hz1
      _ = (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2 := by rw [hcast]
  -- factorization and the sum bound jα + p ≤ 2αj
  have hfac : ((j : ℝ) * α - (p : ℝ)) * ((j : ℝ) * α + (p : ℝ))
      = (D : ℝ) * (j : ℝ) ^ 2 - (p : ℝ) ^ 2 := by
    have : ((j : ℝ) * α) ^ 2 = (D : ℝ) * (j : ℝ) ^ 2 := by rw [mul_pow, hαsq]; ring
    nlinarith [this]
  have hsum_le : (j : ℝ) * α + (p : ℝ) ≤ 2 * α * (j : ℝ) := by nlinarith [hple]
  -- (jα − p) ≥ (D j² − p²)/(jα + p) ≥ 1/(2αj)
  have hkey : 1 ≤ ((j : ℝ) * α - (p : ℝ)) * ((j : ℝ) * α + (p : ℝ)) := by rw [hfac]; exact hge1
  have hjmp : 0 ≤ (j : ℝ) * α - (p : ℝ) := by linarith [hple]
  rw [div_div, div_le_iff₀ (by positivity : (0 : ℝ) < 2 * α * (j : ℝ))]
  calc (1 : ℝ) ≤ ((j : ℝ) * α - (p : ℝ)) * ((j : ℝ) * α + (p : ℝ)) := hkey
    _ ≤ ((j : ℝ) * α - (p : ℝ)) * (2 * α * (j : ℝ)) :=
        mul_le_mul_of_nonneg_left hsum_le hjmp

/-- **Every real quadratic irrational is badly approximable (fract form).**  If `β > 0`
    is irrational and satisfies an integer quadratic `Aβ² + Bβ + C = 0` (`A ≠ 0`), then
    `∃ κ > 0, ∀ j ≥ 1, κ/j ≤ {jβ}` — the degree-2 Liouville bound.  With `p = ⌊jβ⌋`, the
    integer `N = A p² + B p j + C j²` is nonzero (else `p/j` is a rational root, forcing
    `β` or its conjugate rational), so `|N| ≥ 1`; the identity
    `N = −(jβ − p)·(A(p+jβ) + Bj)` (using the root relation) with the bound
    `|A(p+jβ)+Bj| ≤ j·(2|A|β + |B|)` gives `{jβ} = jβ − p ≥ 1/(j·(2|A|β+|B|))`.
    Generalizes `sqrt_fract_badlyApproximable` (`A=1, B=0, C=−D`) to all quadratic
    surds, hence the unconditional Dilog Part B limit to `x = e^{−β}` for every
    quadratic-irrational `β > 0`. -/
theorem quadratic_irrational_fract_badlyApproximable {A B C : ℤ} {β : ℝ}
    (hA : A ≠ 0) (hβ : Irrational β) (hβ0 : 0 < β)
    (hroot : (A : ℝ) * β ^ 2 + (B : ℝ) * β + (C : ℝ) = 0) :
    ∃ κ : ℝ, 0 < κ ∧ ∀ j : ℕ, 1 ≤ j → κ / (j : ℝ) ≤ Int.fract ((j : ℝ) * β) := by
  have hAR : (A : ℝ) ≠ 0 := Int.cast_ne_zero.mpr hA
  have hApos_abs : 0 < |(A : ℝ)| := abs_pos.mpr hAR
  set M : ℝ := 2 * |(A : ℝ)| * β + |(B : ℝ)| with hM
  have hMpos : 0 < M := by
    rw [hM]; have := mul_pos (mul_pos (by norm_num : (0:ℝ) < 2) hApos_abs) hβ0
    linarith [abs_nonneg (B : ℝ)]
  refine ⟨1 / M, one_div_pos.mpr hMpos, ?_⟩
  intro j hj
  have hjR : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have hjpos : (0 : ℝ) < (j : ℝ) := by linarith
  have hj0 : j ≠ 0 := by omega
  have hjβ_irr : Irrational ((j : ℝ) * β) := hβ.natCast_mul hj0
  have hjβ_pos : 0 < (j : ℝ) * β := mul_pos hjpos hβ0
  set p : ℤ := ⌊(j : ℝ) * β⌋ with hp
  have hpnn : (0 : ℝ) ≤ (p : ℝ) := by
    exact_mod_cast Int.floor_nonneg.mpr hjβ_pos.le
  have hple : (p : ℝ) ≤ (j : ℝ) * β := by rw [hp]; exact Int.floor_le _
  have hfr : Int.fract ((j : ℝ) * β) = (j : ℝ) * β - (p : ℝ) := by rw [hp, Int.fract]
  rw [hfr]
  have hfr_nn : 0 ≤ (j : ℝ) * β - (p : ℝ) := by linarith [hple]
  set N : ℤ := A * p ^ 2 + B * p * (j : ℤ) + C * (j : ℤ) ^ 2 with hN
  set F2 : ℝ := (A : ℝ) * ((p : ℝ) + (j : ℝ) * β) + (B : ℝ) * (j : ℝ) with hF2
  -- factorization N = −(jβ − p)·F2 (uses the root relation)
  have hfacR : (N : ℝ) = -(((j : ℝ) * β - (p : ℝ)) * F2) := by
    rw [hF2]; push_cast [hN]; linear_combination (j : ℝ) ^ 2 * hroot
  -- both factors nonzero ⇒ N ≠ 0
  have hf1 : (j : ℝ) * β - (p : ℝ) ≠ 0 := sub_ne_zero.mpr (hjβ_irr.ne_int p)
  have hf2 : F2 ≠ 0 := by
    rw [hF2]; intro h
    apply hjβ_irr
    refine ⟨(-(A * p + B * (j : ℤ)) : ℤ) / (A : ℚ), ?_⟩
    push_cast
    rw [div_eq_iff hAR]
    linear_combination -h
  have hNne : N ≠ 0 := by
    have : (N : ℝ) ≠ 0 := by rw [hfacR]; simp [hf1, hf2]
    exact_mod_cast this
  have tri : ∀ a b : ℝ, |a + b| ≤ |a| + |b| := fun a b =>
    abs_le.mpr ⟨by linarith [neg_abs_le a, neg_abs_le b], by linarith [le_abs_self a, le_abs_self b]⟩
  -- |N| ≥ 1, and |N| = (jβ − p)·|F2|
  have hNabs : (1 : ℝ) ≤ |(N : ℝ)| := by
    have h1 : (1 : ℤ) ≤ |N| := Int.one_le_abs hNne
    calc (1 : ℝ) = ((1 : ℤ) : ℝ) := by norm_num
      _ ≤ ((|N| : ℤ) : ℝ) := by exact_mod_cast h1
      _ = |(N : ℝ)| := by rw [Int.cast_abs]
  have hNeq : |(N : ℝ)| = ((j : ℝ) * β - (p : ℝ)) * |F2| := by
    rw [hfacR, abs_neg, abs_mul, abs_of_nonneg hfr_nn]
  -- |F2| ≤ j·M
  have hF2_le : |F2| ≤ (j : ℝ) * M := by
    have hpjβ : (0 : ℝ) ≤ (p : ℝ) + (j : ℝ) * β := by positivity
    rw [hF2, hM]
    calc |(A : ℝ) * ((p : ℝ) + (j : ℝ) * β) + (B : ℝ) * (j : ℝ)|
        ≤ |(A : ℝ) * ((p : ℝ) + (j : ℝ) * β)| + |(B : ℝ) * (j : ℝ)| := tri _ _
      _ = |(A : ℝ)| * ((p : ℝ) + (j : ℝ) * β) + |(B : ℝ)| * (j : ℝ) := by
          rw [abs_mul, abs_mul, abs_of_nonneg hpjβ, abs_of_pos hjpos]
      _ ≤ |(A : ℝ)| * (2 * ((j : ℝ) * β)) + |(B : ℝ)| * (j : ℝ) := by
          gcongr; linarith [hple]
      _ = (j : ℝ) * (2 * |(A : ℝ)| * β + |(B : ℝ)|) := by ring
  -- assemble
  have hfinal : 1 ≤ ((j : ℝ) * β - (p : ℝ)) * ((j : ℝ) * M) :=
    calc (1 : ℝ) ≤ |(N : ℝ)| := hNabs
      _ = ((j : ℝ) * β - (p : ℝ)) * |F2| := hNeq
      _ ≤ ((j : ℝ) * β - (p : ℝ)) * ((j : ℝ) * M) :=
          mul_le_mul_of_nonneg_left hF2_le hfr_nn
  rw [div_div, div_le_iff₀ (by positivity : (0 : ℝ) < M * (j : ℝ))]
  nlinarith [hfinal]

end QOU.MathlibExt
