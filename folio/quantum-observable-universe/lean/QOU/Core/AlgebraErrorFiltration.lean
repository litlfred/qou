import Mathlib.Algebra.Algebra.Operations
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Core.AlgebraErrorFiltration — error filtrations on a noncommutative algebra

Companion to `QOU.Core.ErrorFiltration` for algebras that are not commutative, such
as the Hecke algebra `H_n(q)` that carries the jet-prefix filtration of
`conj:jet-prefix-gb-filtration`.

## What is proved

* `AlgFiltration`: submodules `F 0 = ⊤ ⊇ F 1 ⊇ …` of an `R`-algebra `A` with
  `F a · F b ⊆ F (a + b)`. Every level is a two-sided ideal (`mul_mem_left`,
  `mul_mem_right`).
* **Symbol map is multiplicative** (`symbol_mul`). If `x ≡ x'` modulo `F (a+1)` with
  `x ∈ F a`, and `y ≡ y'` modulo `F (b+1)` with `y' ∈ F b`, then `x y ≡ x' y'`
  modulo `F (a+b+1)`. So the leading symbols `F a / F (a+1)` multiply into the
  associated graded `⊕ F k / F (k+1)`. This is the symbol map that the jet-prefix
  formula takes as given.
* **Ideal filtrations collapse when ideals are idempotent** (`stable_of_idem`). If one
  level `F a` with `a ≥ 1` satisfies `F a · F a = F a` (true of every two-sided ideal
  of a semisimple algebra, such as `H_n(q)` at generic `q`), then `F m = F a` for all
  `m ≥ a`. So on a semisimple algebra, a filtration by Wedderburn-block ideals gives
  no quadratic error calculus: its error order cannot exceed one.
* **The jet tower** (`scalarAdic`). For a scalar `t ∈ R`, `F n = tⁿ · A` is a
  multiplicative filtration. With `t = q − 1` this is order of vanishing at `q = 1`,
  the jet grading.
* **Classical-limit symbol** (`hecke_sq_sub_one_mem`). If `σ² = (q − q⁻¹) σ + 1` (the
  Hecke relation) with `q` a unit, then `σ² − 1 ∈ (q − 1) · A`. The jet symbol of each
  generator is an involution, so the degree-0 piece sees the symmetric-group relation
  `s² = 1`.

## What is not proved

The identification of the graded pieces with `R/(q−1) ⊗ ℤ[S_n]`, the Gröbner–Shirshov
basis of each truncation, and the partial Markov trace on the symbols remain open.
The jet-prefix evaluation formula is not proved here.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

/-- A multiplicative error filtration on an `R`-algebra, which need not be
commutative. -/
structure AlgFiltration (R A : Type*) [CommRing R] [Ring A] [Algebra R A] where
  F : ℕ → Submodule R A
  anti : Antitone F
  zero_top : F 0 = ⊤
  mul_le : ∀ a b, F a * F b ≤ F (a + b)

namespace AlgFiltration

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A] (E : AlgFiltration R A)

/-- Orders of errors add under multiplication. -/
theorem mul_mem {a b : ℕ} {x y : A} (hx : x ∈ E.F a) (hy : y ∈ E.F b) :
    x * y ∈ E.F (a + b) :=
  E.mul_le a b (Submodule.mul_mem_mul hx hy)

/-- Every level is a left ideal. -/
theorem mul_mem_left {n : ℕ} (a : A) {x : A} (hx : x ∈ E.F n) : a * x ∈ E.F n := by
  have := E.mul_mem (show a ∈ E.F 0 by simp [E.zero_top]) hx
  rwa [zero_add] at this

/-- Every level is a right ideal. -/
theorem mul_mem_right {n : ℕ} {x : A} (a : A) (hx : x ∈ E.F n) : x * a ∈ E.F n := by
  have := E.mul_mem hx (show a ∈ E.F 0 by simp [E.zero_top])
  rwa [add_zero] at this

/-- **The symbol map is multiplicative.** Leading symbols in `F a / F (a+1)` and
`F b / F (b+1)` multiply to a well-defined symbol in `F (a+b) / F (a+b+1)`. -/
theorem symbol_mul {a b : ℕ} {x x' y y' : A} (hx : x ∈ E.F a) (hxx : x - x' ∈ E.F (a + 1))
    (hy' : y' ∈ E.F b) (hyy : y - y' ∈ E.F (b + 1)) :
    x * y - x' * y' ∈ E.F (a + b + 1) := by
  have e : x * y - x' * y' = x * (y - y') + (x - x') * y' := by noncomm_ring
  have h₁ := E.mul_mem hx hyy
  have h₂ := E.mul_mem hxx hy'
  rw [show a + (b + 1) = a + b + 1 by omega] at h₁
  rw [show a + 1 + b = a + b + 1 by omega] at h₂
  rw [e]
  exact add_mem h₁ h₂

/-- **Idempotent levels collapse the tail.** If `F a · F a = F a` for some `a ≥ 1`, the
filtration is constant from level `a` on. -/
theorem stable_of_idem {a : ℕ} (ha : 1 ≤ a) (h : E.F a * E.F a = E.F a) :
    ∀ m, a ≤ m → E.F m = E.F a := by
  have key : ∀ k : ℕ, E.F a ≤ E.F (a * (k + 1)) := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      calc E.F a = E.F a * E.F a := h.symm
        _ ≤ E.F (a * (k + 1)) * E.F a := mul_le_mul' ih le_rfl
        _ ≤ E.F (a * (k + 1) + a) := E.mul_le _ _
        _ = E.F (a * (k + 1 + 1)) := by congr 1
  intro m hm
  refine le_antisymm (E.anti hm) ((key m).trans (E.anti ?_))
  calc m ≤ 1 * (m + 1) := by omega
    _ ≤ a * (m + 1) := Nat.mul_le_mul_right _ ha

/-- **The jet tower** `F n = tⁿ · A` for a scalar `t`. With `t = q − 1` it measures
order of vanishing at `q = 1`. -/
def scalarAdic (t : R) : AlgFiltration R A where
  F n := LinearMap.range ((t ^ n) • (LinearMap.id : A →ₗ[R] A))
  anti := by
    intro n m h x hx
    obtain ⟨y, rfl⟩ := hx
    refine ⟨(t ^ (m - n)) • y, ?_⟩
    simp only [LinearMap.smul_apply, LinearMap.id_apply, smul_smul, ← pow_add]
    rw [Nat.add_sub_cancel' h]
  zero_top := by
    ext x
    simp only [pow_zero, one_smul, LinearMap.range_id, Submodule.mem_top]
  mul_le a b := by
    refine Submodule.mul_le.mpr ?_
    rintro _ ⟨u, rfl⟩ _ ⟨v, rfl⟩
    refine ⟨u * v, ?_⟩
    simp only [LinearMap.smul_apply, LinearMap.id_apply, smul_mul_smul_comm, pow_add]

theorem mem_scalarAdic {t : R} {n : ℕ} {x : A} :
    x ∈ (scalarAdic t : AlgFiltration R A).F n ↔ ∃ y : A, t ^ n • y = x := by
  simp [scalarAdic]

/-- `q − q⁻¹ = (q − 1)(1 + q⁻¹)` for a unit `q`. -/
theorem sub_inv_eq (q : Rˣ) : (q : R) - (↑q⁻¹ : R) = ((q : R) - 1) * (1 + (↑q⁻¹ : R)) := by
  have h := q.mul_inv
  linear_combination (-1 : R) * h

/-- **Classical-limit symbol of a Hecke generator.** If `σ² = (q − q⁻¹) σ + 1`, then
`σ² − 1` lies in the first level of the `(q − 1)`-adic jet tower: the symbol of `σ` is
an involution. -/
theorem hecke_sq_sub_one_mem (q : Rˣ) (σ : A)
    (hrel : σ * σ = ((q : R) - (↑q⁻¹ : R)) • σ + 1) :
    σ * σ - 1 ∈ (scalarAdic ((q : R) - 1) : AlgFiltration R A).F 1 := by
  rw [mem_scalarAdic]
  refine ⟨(1 + (↑q⁻¹ : R)) • σ, ?_⟩
  rw [hrel, sub_inv_eq, pow_one, smul_smul]
  abel

end AlgFiltration

end QOU.Core.Error
