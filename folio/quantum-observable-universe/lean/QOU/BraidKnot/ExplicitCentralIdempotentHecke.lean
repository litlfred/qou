import QOU.SchurWeyl.QJucysMurphy
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Explicit central idempotents on the real Hecke algebra (bean `qou-2150`, owner ruling D2)

The carrier `ExplicitCentralIdempotentConjecture` in
`QOU.BraidKnot.ExplicitCentralIdempotent` states the Murphy–Lagrange conjecture about an
`opaque` element `centralIdempotent : R` of a **commutative** ring, with projectors valued in
`R`. Idempotency and orthogonality there are statements about scalars, so no proof of the
conjecture can be written against it. The owner ruled on 2026-11-20 (D2) to re-state it over the
real Iwahori–Hecke algebra `QOU.SchurWeyl.Hecke`.

This module is the first step:

* `lagrangePoly`, `lagrangeProj` — the Murphy–Lagrange projector of the `.md` boxed formula, built
  in `Hecke K q qi n = H_{n+1}(q)` from the Murphy elements `qJM` (`L_0 = 1`,
  `L_{k+1} = σ_k L_k σ_k`) as a product over `k` of `aeval L_k` of a Lagrange polynomial.
* `MurphyLagrangeComplete` — what the conjecture asserts about a family of joint eigenvalue
  vectors: idempotent, pairwise orthogonal, summing to `1`.
* `murphyLagrangeComplete_two` — **proved** for `H_2(q)` with the two tableaux of shapes `(2)` and
  `(1,1)`, for `q·qi = 1` and `q² ≠ qi²`. Sorry-free.

**Not yet done:** the general statement for `n ≥ 3`, with the family taken to be the q-content
vectors `k ↦ q^{2·content(T(k))}` of all standard Young tableaux of size `n+1`. That needs a choice
among the corpus's several SYT types and a `Fintype` on it. Until then the conjecture block's
`lean.ref` still names the old carrier. Self-adjointness and bar-pairing (cross-checks 3–4) are also
not stated here.

Base ring: a `Field K` (§7c: the Lagrange denominators `t − c` are inverted), with `qi` the
intended inverse of `q` as in `QOU.SchurWeyl.HeckeAlgebra`.
-/

namespace QOU.BraidKnot.ExplicitCentralIdempotentHecke

open QOU.SchurWeyl Polynomial

variable {K : Type*} [Field K] [DecidableEq K] (q qi : K) (n : ℕ)

/-- Lagrange polynomial for target eigenvalue `t` over a spectrum `S`:
    `∏_{c ∈ S, c ≠ t} (X − c)/(t − c)`. -/
noncomputable def lagrangePoly (S : Finset K) (t : K) : K[X] :=
  ∏ c ∈ S.erase t, (C (t - c)⁻¹ * (X - C c))

/-- The Murphy–Lagrange projector in `H_{n+1}(q) = Hecke K q qi n` attached to a joint
    eigenvalue vector `t` (one value per Murphy element `L_0, …, L_n`), with spectra `S`. -/
noncomputable def lagrangeProj (S : ℕ → Finset K) (t : ℕ → K) : Hecke K q qi n :=
  ((List.range (n + 1)).map fun k => aeval (qJM K q qi n k) (lagrangePoly (S k) (t k))).prod

/-- The statement the conjecture makes about a family `𝒯` of joint eigenvalue vectors:
    the Lagrange projectors are idempotent, pairwise orthogonal, and sum to `1`. -/
def MurphyLagrangeComplete (S : ℕ → Finset K) (𝒯 : Finset (ℕ → K)) : Prop :=
  (∀ t ∈ 𝒯, lagrangeProj q qi n S t * lagrangeProj q qi n S t = lagrangeProj q qi n S t) ∧
  (∀ t ∈ 𝒯, ∀ t' ∈ 𝒯, t ≠ t' → lagrangeProj q qi n S t * lagrangeProj q qi n S t' = 0) ∧
  (∑ t ∈ 𝒯, lagrangeProj q qi n S t = 1)

section NTwo

variable {q qi}

/-- The single generator `σ₀` of `H_2(q) = Hecke K q qi 1`. -/
noncomputable abbrev s0 (q qi : K) : Hecke K q qi 1 := Hecke.σ K q qi 1 ⟨0, Nat.one_pos⟩

omit [DecidableEq K] in
/-- Products of elements of `span {1, σ₀}` in `H_2(q)`. -/
theorem pair_mul (hqi : q * qi = 1) (α β γ δ : K) :
    (α • s0 q qi + β • (1 : Hecke K q qi 1)) * (γ • s0 q qi + δ • 1)
      = (α * γ * (q - qi) + α * δ + β * γ) • s0 q qi + (α * γ + β * δ) • (1 : Hecke K q qi 1) := by
  have hq : s0 q qi * s0 q qi = (q - qi) • s0 q qi + (q * qi) • 1 :=
    Hecke.σ_quadratic K q qi 1 ⟨0, Nat.one_pos⟩
  rw [hqi, one_smul] at hq
  simp only [add_mul, mul_add, smul_mul_smul_comm, one_mul, mul_one, hq, smul_add, smul_smul]
  module

/-- Spectra of the Murphy elements of `H_2(q)`: `L_0 = 1`, and `L_1 = σ₀²` with eigenvalues
    `q²` (on the trivial block, `σ₀ = q`) and `qi²` (on the sign block, `σ₀ = −qi`). -/
noncomputable def specTwo (q qi : K) : ℕ → Finset K := fun k => if k = 0 then {1} else {q ^ 2, qi ^ 2}

/-- Joint eigenvalue vector of the tableau of shape `(2)`. -/
noncomputable def tTriv (q : K) : ℕ → K := fun k => if k = 0 then 1 else q ^ 2

/-- Joint eigenvalue vector of the tableau of shape `(1,1)`. -/
noncomputable def tSign (qi : K) : ℕ → K := fun k => if k = 0 then 1 else qi ^ 2

omit [DecidableEq K] in
theorem qJM_one_two (hqi : q * qi = 1) :
    qJM K q qi 1 1 = (q - qi) • s0 q qi + (1 : K) • (1 : Hecke K q qi 1) := by
  rw [qJM_one_expand K q qi 1 Nat.one_pos, hqi]

theorem lagrangeProj_two (hqi : q * qi = 1) (a b : K) (hab : a ≠ b)
    (t : ℕ → K) (ht0 : t 0 = 1) (ht1 : t 1 = a) (hS : ({q ^ 2, qi ^ 2} : Finset K) = {a, b}) :
    lagrangeProj q qi 1 (specTwo q qi) t
      = ((a - b)⁻¹ * (q - qi)) • s0 q qi + ((a - b)⁻¹ * (1 - b)) • (1 : Hecke K q qi 1) := by
  have hpoly1 : lagrangePoly (specTwo q qi 1) (t 1) = C (a - b)⁻¹ * (X - C b) := by
    simp only [lagrangePoly, specTwo, one_ne_zero, if_false, hS, ht1]
    rw [Finset.erase_insert (by simpa using hab), Finset.prod_singleton]
  have hpoly0 : lagrangePoly (specTwo q qi 0) (t 0) = 1 := by
    simp [lagrangePoly, specTwo, ht0]
  simp only [lagrangeProj, List.range_succ, List.range_zero, List.nil_append, List.singleton_append,
    List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one, hpoly0, hpoly1,
    map_one, one_mul, map_mul, map_sub, aeval_C, aeval_X, qJM_one_two hqi,
    Algebra.algebraMap_eq_smul_one]
  rw [smul_mul_assoc, one_mul, smul_sub, smul_add, smul_smul, smul_smul, smul_smul]
  module

omit [DecidableEq K] in
private theorem pair_congr {α β γ δ : K} (h1 : α = γ) (h2 : β = δ) :
    α • s0 q qi + β • (1 : Hecke K q qi 1) = γ • s0 q qi + δ • (1 : Hecke K q qi 1) := by
  rw [h1, h2]

open Classical in
/-- **The Murphy–Lagrange construction is complete in `H_2(q)`.** For `q·qi = 1` and
    `q² ≠ qi²` (i.e. `q⁴ ≠ 1`), the two Lagrange projectors in `L_1 = σ₀²` — for the
    tableaux of shapes `(2)` and `(1,1)` — are idempotent, mutually orthogonal, and sum
    to `1`. This is the `n = 2` case of `conj:explicit-central-idempotent`, proved. -/
theorem murphyLagrangeComplete_two (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2) :
    MurphyLagrangeComplete q qi 1 (specTwo q qi) {tTriv q, tSign qi} := by
  have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
  have hqi' : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
  have hd : q ^ 2 - qi ^ 2 ≠ 0 := sub_ne_zero.mpr hne
  have hd' : qi ^ 2 - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hne)
  have hP := lagrangeProj_two hqi (q ^ 2) (qi ^ 2) hne (tTriv q) (by simp [tTriv])
    (by simp [tTriv]) rfl
  have hQ := lagrangeProj_two hqi (qi ^ 2) (q ^ 2) (Ne.symm hne) (tSign qi) (by simp [tSign])
    (by simp [tSign]) (Finset.pair_comm _ _)
  have htne : tTriv q ≠ tSign qi := fun h => hne (by simpa [tTriv, tSign] using congrFun h 1)
  subst hqi'
  have h4 : q ^ 4 - 1 ≠ 0 := by
    intro h; apply hd
    have : q ^ 2 - q⁻¹ ^ 2 = (q ^ 4 - 1) / q ^ 2 := by field_simp
    rw [this, h, zero_div]
  have h4' : 1 - q ^ 4 ≠ 0 := fun h => h4 (by linear_combination -h)
  refine ⟨?_, ?_, ?_⟩
  · intro t ht
    rcases Finset.mem_insert.mp ht with rfl | ht
    · rw [hP, pair_mul hqi]
      apply pair_congr <;> (field_simp; ring)
    · rw [Finset.mem_singleton.mp ht, hQ, pair_mul hqi]
      apply pair_congr <;> (field_simp; ring)
  · intro t ht t' ht' htt'
    rcases Finset.mem_insert.mp ht with rfl | ht <;>
      rcases Finset.mem_insert.mp ht' with rfl | ht'
    · exact absurd rfl htt'
    · rw [Finset.mem_singleton.mp ht', hP, hQ, pair_mul hqi]
      rw [show (0 : Hecke K q q⁻¹ 1) = (0 : K) • s0 q q⁻¹ + (0 : K) • 1 by simp]
      apply pair_congr <;> (field_simp; ring)
    · rw [Finset.mem_singleton.mp ht, hQ, hP, pair_mul hqi]
      rw [show (0 : Hecke K q q⁻¹ 1) = (0 : K) • s0 q q⁻¹ + (0 : K) • 1 by simp]
      apply pair_congr <;> (field_simp; ring)
    · rw [Finset.mem_singleton.mp ht, Finset.mem_singleton.mp ht'] at htt'
      exact absurd rfl htt'
  · rw [Finset.sum_pair htne, hP, hQ, add_add_add_comm, ← add_smul, ← add_smul]
    have e1 : (q ^ 2 - q⁻¹ ^ 2)⁻¹ * (q - q⁻¹) + (q⁻¹ ^ 2 - q ^ 2)⁻¹ * (q - q⁻¹) = 0 := by
      field_simp; ring
    have e2 : (q ^ 2 - q⁻¹ ^ 2)⁻¹ * (1 - q⁻¹ ^ 2) + (q⁻¹ ^ 2 - q ^ 2)⁻¹ * (1 - q ^ 2) = 1 := by
      field_simp; ring
    rw [e1, e2, zero_smul, zero_add, one_smul]

omit [DecidableEq K] in
/-- The two projectors commute with the generator, hence lie in the centre of `H_2(q)`
    (which is generated by `σ₀`). -/
theorem lagrangeProj_two_comm (α β : K) :
    (α • s0 q qi + β • (1 : Hecke K q qi 1)) * s0 q qi
      = s0 q qi * (α • s0 q qi + β • (1 : Hecke K q qi 1)) := by
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]

end NTwo

end QOU.BraidKnot.ExplicitCentralIdempotentHecke

