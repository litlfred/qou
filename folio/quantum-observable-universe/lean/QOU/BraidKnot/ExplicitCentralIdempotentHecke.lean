import QOU.SchurWeyl.QJucysMurphy
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Explicit central idempotents on the real Hecke algebra (bean `qou-2150`, owner ruling D2)

The former carrier `ExplicitCentralIdempotentConjecture` stated the Murphy–Lagrange conjecture
about an `opaque` element of a **commutative** ring, so no proof could be written against it. The
owner ruled on 2026-11-20 (D2) to re-state it over the real Iwahori–Hecke algebra
`QOU.SchurWeyl.Hecke`. The statement is now proved for every `n`
(`ExplicitCentralIdempotentGeneral.explicit_central_idempotent_cross_checks`), and the carrier was
retired the same day (owner, "2").

This module is the first step:

* `lagrangePoly`, `lagrangeProj` — the Murphy–Lagrange projector of the `.md` boxed formula, built
  in `Hecke K q qi n = H_{n+1}(q)` from the Murphy elements `qJM` (`L_0 = 1`,
  `L_{k+1} = σ_k L_k σ_k`) as a product over `k` of `aeval L_k` of a Lagrange polynomial.
* `MurphyLagrangeComplete` — what the conjecture asserts about a family of joint eigenvalue
  vectors: idempotent, pairwise orthogonal, summing to `1`.
* `murphyLagrangeComplete_two` — **proved** for `H_2(q)` with the two tableaux of shapes `(2)` and
  `(1,1)`, for `q·qi = 1` and `q² ≠ qi²`. Sorry-free.
* `bar_fixes_eTriv` — cross-check 4 (bar-pairing) is **false at `n = 2`** for the bar involution
  `σ ↦ σ⁻¹`, `q ↦ q⁻¹`: it fixes `e_(2)`, and `e_(2) ≠ e_(1,1)`. `hash_swaps_eTriv`: the linear
  `#`-involution `σ ↦ −σ⁻¹` is the one that sends `e_(2)` to `e_(1,1)`.

The general-`n` statement of cross-checks 1–2 and centrality is proved in
`QOU.BraidKnot.ExplicitCentralIdempotentGeneral`.


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

/-! ### Cross-check 4 fails at `n = 2`

The `.md` bar involution is `σ_i ↦ σ_i⁻¹`, `q ↦ q⁻¹`, extended antilinearly. It fixes the
trivial-block idempotent `e_(2)` instead of sending it to `e_(1,1)`. Since `(2)` is chiral
(`(2)' = (1,1)`), cross-check 4 (`*(e_λ) = e_{λ'}` for `λ ≠ λ'`) is false at `n = 2`. -/

/-- `e_(2)`, written in the basis `{σ₀, 1}`. -/
noncomputable def eTriv (q qi : K) : Hecke K q qi 1 :=
  ((q ^ 2 - qi ^ 2)⁻¹ * (q - qi)) • s0 q qi + ((q ^ 2 - qi ^ 2)⁻¹ * (1 - qi ^ 2)) • 1

/-- `e_(1,1)`, written in the basis `{σ₀, 1}`. -/
noncomputable def eSign (q qi : K) : Hecke K q qi 1 :=
  ((qi ^ 2 - q ^ 2)⁻¹ * (q - qi)) • s0 q qi + ((qi ^ 2 - q ^ 2)⁻¹ * (1 - q ^ 2)) • 1

theorem lagrangeProj_tTriv (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2) :
    lagrangeProj q qi 1 (specTwo q qi) (tTriv q) = eTriv q qi :=
  lagrangeProj_two hqi (q ^ 2) (qi ^ 2) hne (tTriv q) (by simp [tTriv]) (by simp [tTriv]) rfl

theorem lagrangeProj_tSign (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2) :
    lagrangeProj q qi 1 (specTwo q qi) (tSign qi) = eSign q qi :=
  lagrangeProj_two hqi (qi ^ 2) (q ^ 2) (Ne.symm hne) (tSign qi) (by simp [tSign])
    (by simp [tSign]) (Finset.pair_comm _ _)

omit [DecidableEq K] in
/-- The trivial representation `σ₀ ↦ q` of `H_2(q)`. -/
noncomputable def trivRep (q qi : K) : Hecke K q qi 1 →ₐ[K] K :=
  Hecke.lift K q qi 1 (fun _ => q) (fun _ => by simp only [smul_eq_mul, mul_one]; ring)
    (fun i hi => absurd hi (by omega)) (fun i j h => absurd h (by omega))

omit [DecidableEq K] in
theorem trivRep_s0 : trivRep q qi (s0 q qi) = q := by
  simp [trivRep, s0]

omit [DecidableEq K] in
/-- `e_(2) ≠ e_(1,1)`: the trivial representation sends them to `1` and `0`. -/
theorem eTriv_ne_eSign (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2) : eTriv q qi ≠ eSign q qi := by
  intro h
  have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
  have hqi' : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
  have h1 := congrArg (trivRep q qi) h
  simp only [eTriv, eSign, map_add, map_smul, map_one, trivRep_s0, smul_eq_mul, mul_one] at h1
  subst hqi'
  have hd : q ^ 2 - q⁻¹ ^ 2 ≠ 0 := sub_ne_zero.mpr hne
  have hd' : q⁻¹ ^ 2 - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hne)
  have h4 : q ^ 4 - 1 ≠ 0 := by
    intro h; apply hd
    have : q ^ 2 - q⁻¹ ^ 2 = (q ^ 4 - 1) / q ^ 2 := by field_simp
    rw [this, h, zero_div]
  have h4' : -1 + q ^ 4 ≠ 0 := fun h => h4 (by linear_combination h)
  have h4'' : 1 - q ^ 4 ≠ 0 := fun h => h4 (by linear_combination -h)
  have e1 : (q ^ 2 - q⁻¹ ^ 2)⁻¹ * (q - q⁻¹) * q + (q ^ 2 - q⁻¹ ^ 2)⁻¹ * (1 - q⁻¹ ^ 2) = 1 := by
    field_simp; ring
  have e2 : (q⁻¹ ^ 2 - q ^ 2)⁻¹ * (q - q⁻¹) * q + (q⁻¹ ^ 2 - q ^ 2)⁻¹ * (1 - q ^ 2) = 0 := by
    field_simp; ring
  rw [e1, e2] at h1
  exact one_ne_zero h1

omit [DecidableEq K] in
/-- **Any bar involution of the `.md`'s kind fixes `e_(2)`.** Let `τ` be a ring endomorphism of
`K` with `τ q = qi` and `τ qi = q`, and `φ` a ring endomorphism of `H_2(q)` that is `τ`-semilinear
on scalars and sends `σ₀ ↦ σ₀⁻¹`. Then `φ(e_(2)) = e_(2)`, and `e_(2) ≠ e_(1,1)`, so `φ` does not
pair the chiral block `(2)` with `(1,1)`. -/
theorem bar_fixes_eTriv (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2) (τ : K →+* K)
    (hτq : τ q = qi) (hτqi : τ qi = q) (φ : Hecke K q qi 1 →+* Hecke K q qi 1)
    (hφσ : φ (s0 q qi) = Hecke.σInv K q qi 1 ⟨0, Nat.one_pos⟩)
    (hφs : ∀ a : K, φ (a • (1 : Hecke K q qi 1)) = τ a • (1 : Hecke K q qi 1)) :
    φ (eTriv q qi) = eTriv q qi ∧ φ (eTriv q qi) ≠ eSign q qi := by
  have hfix : φ (eTriv q qi) = eTriv q qi := by
    have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
    have hqi' : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
    have hsm : ∀ (a : K) (x : Hecke K q qi 1), a • x = (a • (1 : Hecke K q qi 1)) * x :=
      fun a x => (smul_one_mul a x).symm
    have hL : φ (eTriv q qi)
        = (τ ((q ^ 2 - qi ^ 2)⁻¹ * (q - qi))) • s0 q qi
          + (τ ((q ^ 2 - qi ^ 2)⁻¹ * (1 - qi ^ 2)) - (q - qi) * τ ((q ^ 2 - qi ^ 2)⁻¹ * (q - qi)))
            • (1 : Hecke K q qi 1) := by
      unfold eTriv
      rw [hsm _ (s0 q qi), map_add, map_mul, hφs, hφs, hφσ, Hecke.σInv]
      rw [mul_sub, smul_mul_assoc, one_mul, mul_smul_comm, mul_one, smul_smul, sub_smul]
      abel
    rw [hL]
    simp only [map_mul, map_sub, map_inv₀, map_pow, map_one, hτq, hτqi]
    unfold eTriv
    subst hqi'
    have hd : q ^ 2 - q⁻¹ ^ 2 ≠ 0 := sub_ne_zero.mpr hne
    have hd' : q⁻¹ ^ 2 - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hne)
    have h4 : q ^ 4 - 1 ≠ 0 := by
      intro h; apply hd
      have : q ^ 2 - q⁻¹ ^ 2 = (q ^ 4 - 1) / q ^ 2 := by field_simp
      rw [this, h, zero_div]
    have h4' : -1 + q ^ 4 ≠ 0 := fun h => h4 (by linear_combination h)
    have h4'' : 1 - q ^ 4 ≠ 0 := fun h => h4 (by linear_combination -h)
    apply pair_congr <;> (field_simp; ring)
  exact ⟨hfix, by rw [hfix]; exact eTriv_ne_eSign hqi hne⟩

omit [DecidableEq K] in
/-- **The `#`-involution does pair the chiral blocks.** A `K`-linear algebra endomorphism with
`σ₀ ↦ −σ₀⁻¹` (scalars fixed) sends `e_(2)` to `e_(1,1)`. So the pairing `λ ↔ λ'` of
cross-check 4 holds for `σ ↦ −σ⁻¹`, not for the bar involution `σ ↦ σ⁻¹, q ↦ q⁻¹`. -/
theorem hash_swaps_eTriv (hqi : q * qi = 1) (hne : q ^ 2 ≠ qi ^ 2)
    (φ : Hecke K q qi 1 →ₐ[K] Hecke K q qi 1)
    (hφσ : φ (s0 q qi) = -Hecke.σInv K q qi 1 ⟨0, Nat.one_pos⟩) :
    φ (eTriv q qi) = eSign q qi := by
  have hL : φ (eTriv q qi)
      = (-((q ^ 2 - qi ^ 2)⁻¹ * (q - qi))) • s0 q qi
        + ((q ^ 2 - qi ^ 2)⁻¹ * (1 - qi ^ 2) + (q - qi) * ((q ^ 2 - qi ^ 2)⁻¹ * (q - qi)))
          • (1 : Hecke K q qi 1) := by
    unfold eTriv
    rw [map_add, map_smul, map_smul, map_one, hφσ, Hecke.σInv, neg_sub, smul_sub, smul_smul,
      add_smul, neg_smul]
    module
  rw [hL]
  unfold eSign
  have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
  have hqi' : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
  subst hqi'
  have hd : q ^ 2 - q⁻¹ ^ 2 ≠ 0 := sub_ne_zero.mpr hne
  have hd' : q⁻¹ ^ 2 - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hne)
  have h4 : q ^ 4 - 1 ≠ 0 := by
    intro h; apply hd
    have : q ^ 2 - q⁻¹ ^ 2 = (q ^ 4 - 1) / q ^ 2 := by field_simp
    rw [this, h, zero_div]
  have h4' : -1 + q ^ 4 ≠ 0 := fun h => h4 (by linear_combination h)
  have h4'' : 1 - q ^ 4 ≠ 0 := fun h => h4 (by linear_combination -h)
  apply pair_congr <;> (field_simp; ring)

end NTwo

end QOU.BraidKnot.ExplicitCentralIdempotentHecke


