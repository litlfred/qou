import Mathlib.Analysis.Complex.Basic
import Mathlib.LinearAlgebra.Complex.FiniteDimensional
import QOU.Archimedean.BlochRigidity.Algebra


/-!
# Bloch–Suslin rigidity: algebra over `ℂ` (no analysis)

Two facts about `ℂ` as a real vector space, and the step that solves the cocycle equation.

* `rlinear_functional_eq_re`, `rlinear_eq_add_conj`: these package a real derivative of a real
  (or complex) function into a complex coefficient `ω` (or a pair `α, β`). They let the analytic
  propositions state their output as complex identities.
* `cocycle_eq_mul_im` (stage U1, algebraic half): a real `ρ` with
  `ρ(ab) = ρ(a)·b̄ + a·ρ(b)` is `k · Im` on `ℂ ∖ {0,1}`.
-/

open Complex

namespace QOU.Archimedean.BlochRigidity

/-- Every `ℝ`-linear functional on `ℂ` is `v ↦ Re (ω v)` for `ω = L 1 - i L i`. -/
theorem rlinear_functional_eq_re (L : ℂ →ₗ[ℝ] ℝ) (v : ℂ) :
    L v = (((L 1 : ℂ) - I * (L I : ℂ)) * v).re := by
  have hv : v = (v.re : ℝ) • (1 : ℂ) + (v.im : ℝ) • I := by
    apply Complex.ext <;> simp
  conv_lhs => rw [hv]
  rw [map_add, map_smul, map_smul]
  simp [Complex.mul_re, smul_eq_mul]
  ring

/-- Every `ℝ`-linear map `ℂ → ℂ` is `v ↦ α v + β v̄`. -/
theorem rlinear_eq_add_conj (L : ℂ →ₗ[ℝ] ℂ) (v : ℂ) :
    L v = (L 1 - I * L I) / 2 * v + (L 1 + I * L I) / 2 * (starRingEnd ℂ) v := by
  have hv : v = (v.re : ℝ) • (1 : ℂ) + (v.im : ℝ) • I := by
    apply Complex.ext <;> simp
  conv_lhs => rw [hv]
  rw [map_add, map_smul, map_smul]
  conv_rhs => rw [hv]
  simp only [Complex.real_smul, map_add, map_mul, Complex.conj_ofReal, map_one, Complex.conj_I]
  ring_nf
  rw [Complex.I_sq]
  ring

/-- **The ρ-cocycle is a multiple of `Im`.** If a real function `ρ` satisfies
`ρ(ab) = ρ(a)·b̄ + a·ρ(b)` for all `a, b ∉ {0,1}` with `ab ≠ 1`, then `ρ = k · Im` on `ℂ ∖ {0,1}`.
Pure algebra in `ℂ`: the imaginary part of the identity gives `ρ(a) Im b = ρ(b) Im a`. -/
theorem cocycle_eq_mul_im {ρ : ℂ → ℝ}
    (h : ∀ a b : ℂ, a ≠ 0 → a ≠ 1 → b ≠ 0 → b ≠ 1 → a * b ≠ 1 →
      ((ρ (a * b) : ℝ) : ℂ) = (ρ a : ℂ) * (starRingEnd ℂ) b + a * (ρ b : ℂ)) :
    ∃ k : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → ρ z = k * z.im := by
  -- imaginary part of the identity
  have him : ∀ a b : ℂ, a ≠ 0 → a ≠ 1 → b ≠ 0 → b ≠ 1 → a * b ≠ 1 →
      ρ a * b.im = ρ b * a.im := by
    intro a b ha0 ha1 hb0 hb1 hab
    have := congrArg Complex.im (h a b ha0 ha1 hb0 hb1 hab)
    simp [Complex.mul_im] at this
    linarith
  refine ⟨ρ I, fun z hz0 hz1 => ?_⟩
  have hI0 : (I : ℂ) ≠ 0 := I_ne_zero
  have hI1 : (I : ℂ) ≠ 1 := by intro h; simpa using congrArg Complex.im h
  -- second reference point `2i`
  set J : ℂ := 2 * I
  have hJ0 : J ≠ 0 := mul_ne_zero two_ne_zero hI0
  have hJ1 : J ≠ 1 := by intro h; simpa [J] using congrArg Complex.im h
  have hIJ : I * J ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    simp [J] at this
    norm_num at this
  -- ρ J = 2 ρ I
  have hJ : ρ J = ρ I * 2 := by
    have := him I J hI0 hI1 hJ0 hJ1 hIJ
    simp [J] at this; linarith
  by_cases hzI : z * I = 1
  · -- then `z * J ≠ 1`; use `J`
    have hzJ : z * J ≠ 1 := by
      intro h'
      have : z * J = 2 * (z * I) := by simp [J]; ring
      rw [this, hzI] at h'; norm_num at h'
    have := him z J hz0 hz1 hJ0 hJ1 hzJ
    simp [J] at this
    rw [hJ] at this
    linarith
  · have := him z I hz0 hz1 hI0 hI1 hzI
    simp at this
    linarith

/-- **Two-term symmetry over `ℂ`.** A real five-term solution that is inversion-odd and
conjugation-odd satisfies `φ (1 - z) = - φ z` on `ℂ ∖ {0,1}`. This is pure algebra: `two_term`
handles generic `z`. The exceptional point `z = 2` is real, where conjugation-oddness gives
`φ = 0`. The exceptional roots of `z² - z + 1` satisfy `1 - z = z⁻¹`, so inversion applies. -/
theorem one_sub_odd {φ : ℂ → ℝ}
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (hconj : ∀ z : ℂ, φ ((starRingEnd ℂ) z) = -φ z)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) : φ (1 - z) = -φ z := by
  have hreal : ∀ r : ℝ, φ (r : ℂ) = 0 := by
    intro r; have := hconj (r : ℂ); rw [Complex.conj_ofReal] at this; linarith
  by_cases h2 : z = 2
  · subst h2
    have e1 := hreal 2
    have e2 := hreal (-1)
    push_cast at e1 e2
    rw [show (1 : ℂ) - 2 = -1 by norm_num, e1, e2]; simp
  by_cases h6 : z ^ 2 - z + 1 = 0
  · have : 1 - z = z⁻¹ := by
      field_simp; linear_combination -h6
    rw [this, hinv z hz0 hz1]
  · have := two_term hinv h5 hz0 hz1 h2 h6
    rw [nsmul_eq_mul] at this
    norm_num at this
    linarith

/-- **The mixed-derivative identity forces `β·|z|²|1-z|² = k·Im z`.** Substitute
`x = (1-b)/(1-ab)`, `y = a x` (so `y/x = a`, `(1-x)/(1-y) = b`), apply `cocycle_of_mixed` with
`X = x̄`, `Y = ȳ`, and conclude with `cocycle_eq_mul_im`. The hypothesis `h` is exactly what the
chain rule produces from the five-term relation; the proof itself uses no analysis. -/
theorem mixed_eq_mul_im {β : ℂ → ℝ}
    (h : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      (β (y / x) : ℂ) * (starRingEnd ℂ) (-y / x ^ 2) * (1 / x)
        - (β (y / x * ((1 - x) / (1 - y))) : ℂ) * (starRingEnd ℂ) (-y / (x ^ 2 * (1 - y)))
            * ((1 - x) / (x * (1 - y) ^ 2))
        + (β ((1 - x) / (1 - y)) : ℂ) * (starRingEnd ℂ) (-1 / (1 - y))
            * ((1 - x) / (1 - y) ^ 2) = 0) :
    ∃ k : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → β z * normSq z * normSq (1 - z) = k * z.im := by
  apply cocycle_eq_mul_im (ρ := fun z => β z * normSq z * normSq (1 - z))
  intro a b ha0 ha1 hb0 hb1 hab
  have hab' : 1 - a * b ≠ 0 := sub_ne_zero.2 (Ne.symm hab)
  have h1a : 1 - a ≠ 0 := sub_ne_zero.2 (Ne.symm ha1)
  have h1b : 1 - b ≠ 0 := sub_ne_zero.2 (Ne.symm hb1)
  have hba : 1 - b * a ≠ 0 := by rwa [mul_comm]
  set x : ℂ := (1 - b) / (1 - a * b) with hxdef
  set y : ℂ := a * x with hydef
  have hx0 : x ≠ 0 := div_ne_zero h1b hab'
  have hy0 : y ≠ 0 := mul_ne_zero ha0 hx0
  have h1x : 1 - x = b * (1 - a) / (1 - a * b) := by
    rw [hxdef, eq_div_iff hab']; field_simp; ring
  have h1y : 1 - y = (1 - a) / (1 - a * b) := by
    rw [hydef, hxdef]; field_simp; ring
  have hx1 : x ≠ 1 := fun e => by
    have : 1 - x = 0 := by rw [e]; ring
    rw [h1x] at this; exact div_ne_zero (mul_ne_zero hb0 h1a) hab' this
  have hy1 : y ≠ 1 := fun e => by
    have : 1 - y = 0 := by rw [e]; ring
    rw [h1y] at this; exact div_ne_zero h1a hab' this
  have hxy : x ≠ y := fun e => by
    have : x * (1 - a) = 0 := by rw [hydef] at e; linear_combination e
    rcases mul_eq_zero.1 this with h | h
    · exact hx0 h
    · exact h1a h
  have hya : y / x = a := by rw [hydef]; field_simp
  have hyb : (1 - x) / (1 - y) = b := by rw [h1x, h1y]; field_simp
  have Hc := h x y hx0 hx1 hy0 hy1 hxy
  rw [hya, hyb] at Hc
  have cj : ∀ z : ℂ, z ≠ 0 → (starRingEnd ℂ) z ≠ 0 := fun z hz => by
    simpa using hz
  have cj1 : ∀ z : ℂ, z ≠ 1 → (starRingEnd ℂ) z ≠ 1 := fun z hz => by
    intro e; apply hz; simpa using congrArg (starRingEnd ℂ) e
  have hXY : (starRingEnd ℂ) x ≠ (starRingEnd ℂ) y := fun e =>
    hxy (by simpa using congrArg (starRingEnd ℂ) e)
  simp only [map_div₀, map_neg, map_pow, map_mul, map_sub, map_one] at Hc
  have K := cocycle_of_mixed hx0 hx1 hy1 hxy (cj x hx0) (cj1 x hx1) (cj1 y hy1) hXY Hc
  have hYX : (starRingEnd ℂ) y / (starRingEnd ℂ) x = (starRingEnd ℂ) a := by
    rw [← map_div₀, hya]
  have hYb : (1 - (starRingEnd ℂ) x) / (1 - (starRingEnd ℂ) y) = (starRingEnd ℂ) b := by
    rw [← map_one (starRingEnd ℂ), ← map_sub, ← map_sub, ← map_div₀, hyb]
  rw [hya, hyb, hYX, hYb] at K
  push_cast
  rw [← mul_conj, ← mul_conj, ← mul_conj, ← mul_conj, ← mul_conj, ← mul_conj]
  simp only [map_mul, map_sub, map_one]
  linear_combination K

end QOU.Archimedean.BlochRigidity
