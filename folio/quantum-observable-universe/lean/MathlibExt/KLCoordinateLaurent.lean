import MathlibExt.LaurentUnits

/-!
# Integral, bar-invariant coordinates on `H₂(q)` over `ℤ[q, q⁻¹]`

A coordinate on the Markov-trace family is `c = tr(b)` for an element
`b = u·σ + v` of `H₂` over the integral form `ℤ[q, q⁻¹]`
(`def:bar-involution`; the chapter intro of `braids-and-knots` puts the
trace over `ℤ[q, q⁻¹]`). Here `q = T 1`, and the scalar bar map `q ↦ q⁻¹` is
Mathlib's `LaurentPolynomial.invert`.

Using `σ⁻¹ = σ − (q − q⁻¹)`, the element `bar b = bar(u)·σ⁻¹ + bar(v)` equals `b`
exactly when `bar u = u` and `bar v − v = u·(q − q⁻¹)`. That pair of equations
is `IsBarInvariantCoord u v` below.

Results:
* `kl_coord_classification`: if `u` is a unit (so that `b` and `1` span `H₂`
  over `ℤ[q, q⁻¹]`) and `b` is bar-invariant, then `u = ±1` and
  `v = −u·q + c` with `c` bar-invariant. These are the Kazhdan–Lusztig
  elements `±(σ − q) + c`. The converse also holds.
* Both hypotheses are needed:
  - `unit_not_bar_invariant`: every `q^m` is a unit, but it is bar-invariant
    only when `m = 0`. With integrality alone the derivative is
    `±q^(−m)·q⁻³` for any `m`.
  - `bar_invariant_coord_not_unit`: `b = [2]_q·σ − q²` is integral and
    bar-invariant, but `[2]_q = q + q⁻¹` is not a unit (it evaluates to `2` at
    `q = 1`). With bar-invariance alone the derivative is `q⁻³/[2]_q`.

What this does not show: no axiom in the corpus requires the coordinate to be
integral and bar-invariant. The criterion is stated, not derived.
-/

namespace QOU.MathlibExt.KLCoordinateLaurent

open LaurentPolynomial QOU.MathlibExt.LaurentUnits

/-- `b = u·σ + v` is fixed by the bar involution `σ ↦ σ⁻¹ = σ − (q − q⁻¹)`,
`q ↦ q⁻¹`. -/
def IsBarInvariantCoord (u v : ℤ[T;T⁻¹]) : Prop :=
  invert u = u ∧ invert v - v = u * (T 1 - T (-1))

theorem kl_coord_classification (u v : ℤ[T;T⁻¹]) :
    (IsUnit u ∧ IsBarInvariantCoord u v) ↔
      ((u = 1 ∨ u = -1) ∧ ∃ c : ℤ[T;T⁻¹], invert c = c ∧ v = -u * T 1 + c) := by
  constructor
  · rintro ⟨hu, hbu, hbv⟩
    obtain ⟨ε, m, hε, rfl⟩ := (int_isUnit_iff u).mp hu
    have hεu : IsUnit ε := by rcases hε with rfl | rfl <;> simp
    have hfix : LaurentPolynomial.C ε * T m = LaurentPolynomial.C ε * T (-m) := by
      have := hbu
      rw [map_mul, invert_C, invert_T] at this
      exact this.symm
    have hm := unit_bar_invariant_exponent_zero hεu m hfix
    subst hm
    refine ⟨by rcases hε with rfl | rfl <;> simp, ?_⟩
    refine ⟨v + LaurentPolynomial.C ε * T 0 * T 1, ?_, by ring⟩
    have hv : invert v = v + LaurentPolynomial.C ε * T 0 * (T 1 - T (-1)) := by
      rw [← hbv]; ring
    rw [map_add, hv, map_mul, map_mul, invert_C, invert_T, invert_T]
    have h1 : (T 1 : ℤ[T;T⁻¹]) * T (-1) = 1 := by rw [← T_add]; simp
    simp only [neg_zero]
    ring
  · rintro ⟨hu, c, hc, rfl⟩
    refine ⟨?_, ?_, ?_⟩
    · rcases hu with rfl | rfl <;> simp
    · rcases hu with rfl | rfl <;> simp
    · have hinv : invert u = u := by rcases hu with rfl | rfl <;> simp
      rw [map_add, map_mul, map_neg, hinv, invert_T, hc]
      ring

/-- Integrality alone does not fix the exponent: `q^m` is a unit for every `m`,
and it is bar-invariant only for `m = 0`. -/
theorem unit_not_bar_invariant (m : ℤ) :
    IsUnit (T m : ℤ[T;T⁻¹]) ∧ (invert (T m : ℤ[T;T⁻¹]) = T m ↔ m = 0) := by
  refine ⟨isUnit_T m, ?_, ?_⟩
  · intro h
    rw [invert_T] at h
    have := unit_bar_invariant_exponent_zero (R := ℤ) isUnit_one m
      (by simpa using h.symm)
    exact this
  · rintro rfl; simp

/-- Bar-invariance alone does not give a unit: `b = [2]_q·σ − q²` is
bar-invariant, but `[2]_q = q + q⁻¹` is not a unit of `ℤ[q, q⁻¹]`. -/
theorem bar_invariant_coord_not_unit :
    IsBarInvariantCoord (T 1 + T (-1)) (-T 2) ∧ ¬ IsUnit (T 1 + T (-1) : ℤ[T;T⁻¹]) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · rw [map_add, invert_T, invert_T, neg_neg, add_comm]
  · have e1 : (T 2 : ℤ[T;T⁻¹]) = T 1 * T 1 := by rw [← T_add]; norm_num
    have e2 : (T (-2) : ℤ[T;T⁻¹]) = T (-1) * T (-1) := by rw [← T_add]; norm_num
    have h1 : (T 1 : ℤ[T;T⁻¹]) * T (-1) = 1 := by rw [← T_add]; simp
    rw [map_neg, invert_T, e1, e2]
    ring
  · intro h
    have h2 := h.map (LaurentPolynomial.eval₂ (RingHom.id ℤ) (1 : ℤˣ))
    rw [map_add, eval₂_T, eval₂_T] at h2
    simp only [one_zpow, Units.val_one] at h2
    norm_num [Int.isUnit_iff] at h2

end QOU.MathlibExt.KLCoordinateLaurent
