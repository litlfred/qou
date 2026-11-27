import QOU.Core.AlgebraErrorFiltration
import QOU.Core.MarkovUnusedGenerator

/-!
# QOU.Core.JetTowerTrace — Markov traces on the graded pieces of the jet tower

This file attacks `conj:jet-prefix-gb-filtration` using the `(q − 1)`-adic jet tower
`F k = tᵏ · A` of `QOU.Core.AlgebraErrorFiltration`. `A` is an `R`-algebra, for
example `H_n(q)` over `R = ℤ[q, q⁻¹]`, and `t = q − 1`.
The conjecture's filtration `J^k` is not pinned down in the corpus. Filtering a semisimple
algebra by Wedderburn-block ideals collapses (`AlgFiltration.stable_of_idem`), so
this file reads `J^k` as the jet tower.

## What is proved

* **Traces descend to graded pieces** (`map_mem`, `map_sub_mem`). Any `R`-linear map
  `φ : A → B` sends level `k` to level `k`. That covers the Markov trace `A → R`, and
  equally the partial (conditional-expectation) trace `A_{n+1} → A_n`. So each induces
  a map on `F k / F (k+1)`. On level `k` the trace is `tᵏ` times the trace of the
  quotient (`map_shift`).
* **The graded Markov property** (`markov_graded`). Let `T` be a Markov tower (Core,
  `R`-linear trace). Suppose `a ∈ H n` and `a ≡ a'` modulo `F (k+1)`. Then
  `tr(a σ_n) ≡ z · tr a'` modulo `t^{k+1}`. Each graded piece therefore carries a
  Markov trace with parameter `z mod t`.
* **Every graded piece is the classical limit** (`smul_mem_succ_iff`). If `t` is
  regular on `A`, then `tᵏ y ∈ F (k+1) ↔ y ∈ F 1`. So `y ↦ tᵏ y` gives
  `A / tA ≅ F k / F (k+1)`. For `H_n(q)` this is the `q = 1` algebra, where each
  generator's symbol is an involution (`hecke_sq_sub_one_mem`). A free module over a
  domain has `t ≠ 0` regular (`isSMulRegular_of_ne_zero`).
* **Braid words have depth zero** (`unit_not_mem_one`). Suppose some linear functional
  has `f 1 = 1` (a normalised trace does) and `t` is not a unit. Then no unit of `A`
  lies in `F 1`.

## Consequence for the conjecture

The conjecture defines `β_k^{GS}` as the projection of a braid word `T_w` onto
`J^{k−3}/J^{k−2}`. Under the jet-tower reading, `T_w` is a unit, so it lies in no
`F j` with `j ≥ 1`. The projection is therefore defined only for `k = 3`. To be
well-posed, `β_k` must be the `t^{k−3}`-coefficient of an expansion
`T_w = Σ tʲ s_j`, taken with respect to a chosen section (e.g. the `T_w` basis). By the
two results above, its level trace is `t^{k−3}` times a `q = 1` trace of `s_{k−3}`.
That reduces the numerator of the formula to classical group-algebra traces. The
denominator (restriction multiplicities) and the formula itself remain unproved.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

open AlgFiltration

variable {R A B : Type*} [CommRing R] [Ring A] [Algebra R A] [Ring B] [Algebra R B]

/-- Shorthand: level `k` of the jet tower of `A`. -/
abbrev jet (A : Type*) [Ring A] [Algebra R A] (t : R) (k : ℕ) : Submodule R A :=
  (scalarAdic t : AlgFiltration R A).F k

/-- **Linear maps preserve jet level.** This covers the Markov trace (`B = R`) and the
partial trace (`B = A_n`). -/
theorem map_mem (φ : A →ₗ[R] B) {t : R} {k : ℕ} {x : A} (hx : x ∈ jet A t k) :
    φ x ∈ jet B t k := by
  obtain ⟨y, rfl⟩ := mem_scalarAdic.mp hx
  exact mem_scalarAdic.mpr ⟨φ y, by simp⟩

/-- Linear maps descend to the graded pieces `F k / F (k+1)`. -/
theorem map_sub_mem (φ : A →ₗ[R] B) {t : R} {k : ℕ} {x x' : A}
    (h : x - x' ∈ jet A t (k + 1)) : φ x - φ x' ∈ jet B t (k + 1) := by
  rw [← map_sub]
  exact map_mem φ h

/-- On level `k` a linear map is `tᵏ` times its value on the quotient. -/
theorem map_shift (φ : A →ₗ[R] B) (t : R) (k : ℕ) (y : A) :
    φ (t ^ k • y) = t ^ k • φ y :=
  φ.map_smul _ _

/-- **The graded Markov property.** -/
theorem markov_graded (T : QOU.MathlibExt.MarkovUnusedGenerator.MarkovTower R A) {t : R} {n k : ℕ} {a a' : A} (ha : a ∈ T.H n)
    (h : a - a' ∈ jet A t (k + 1)) :
    T.tr (a * T.σ n) - T.z * T.tr a' ∈ jet R t (k + 1) := by
  rw [T.markov n a ha, ← mul_sub]
  exact (scalarAdic t : AlgFiltration R R).mul_mem_left T.z (map_sub_mem T.tr h)

/-- **Each graded piece is a copy of `A / tA`** when `t` is regular on `A`. -/
theorem smul_mem_succ_iff {t : R} (ht : IsSMulRegular A t) (k : ℕ) (y : A) :
    t ^ k • y ∈ jet A t (k + 1) ↔ y ∈ jet A t 1 := by
  simp only [mem_scalarAdic, pow_one]
  constructor
  · rintro ⟨z, hz⟩
    refine ⟨z, (ht.pow k) ?_⟩
    simp only
    rw [← hz, pow_succ, mul_smul, smul_comm]
  · rintro ⟨z, rfl⟩
    exact ⟨z, by rw [pow_succ, mul_smul]⟩

/-- Without zero divisors (e.g. a free module over a domain, such as `H_n(q)` over
`ℤ[q, q⁻¹]`), every non-zero scalar is regular. -/
theorem isSMulRegular_of_ne_zero [NoZeroSMulDivisors R A] {t : R} (ht : t ≠ 0) :
    IsSMulRegular A t :=
  smul_right_injective A ht

/-- **Units have depth zero.** If some linear functional takes `1` to `1` and `t` is
not a unit, then no unit of `A` lies in the first jet level. -/
theorem unit_not_mem_one (f : A →ₗ[R] R) (hf : f 1 = 1) {t : R} (ht : ¬ IsUnit t)
    {u : A} (hu : IsUnit u) : u ∉ jet A t 1 := by
  intro h
  obtain ⟨v, hv⟩ := hu.exists_left_inv
  have h1 : (1 : A) ∈ jet A t 1 := by
    rw [← hv]
    exact (scalarAdic t : AlgFiltration R A).mul_mem_left v h
  obtain ⟨y, hy⟩ := mem_scalarAdic.mp h1
  apply ht
  refine isUnit_of_mul_eq_one t (f y) ?_
  rw [← hf, ← hy, pow_one, f.map_smul, smul_eq_mul]

/-- So a unit is in no jet level `k ≥ 1`: its stratum projection is undefined. -/
theorem unit_not_mem (f : A →ₗ[R] R) (hf : f 1 = 1) {t : R} (ht : ¬ IsUnit t)
    {u : A} (hu : IsUnit u) {k : ℕ} (hk : 1 ≤ k) : u ∉ jet A t k := fun h =>
  unit_not_mem_one f hf ht hu ((scalarAdic t : AlgFiltration R A).anti hk h)

end QOU.Core.Error
