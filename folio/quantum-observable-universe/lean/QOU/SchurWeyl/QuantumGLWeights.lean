/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLIntertwine

/-!
# Weight spaces and highest-weight spaces of `(K^d)^{⊗n}`

G3.2 and G3.3 (beans `qou-gl32`, `qou-gl33`), building on G3.1 (`QuantumGLAction`,
`QuantumGLIntertwine`).

## Weight spaces (G3.2)

The weight (content) of a basis vector `e_a`, `a : Fin n → Fin d`, is `content a : Fin d → ℕ`,
the number of sites carrying each letter.  `weightProj μ` is the diagonal projector onto
`V_μ = span {e_a : content a = μ}`.

* `content_eq_of_embedPair_ne_zero`: `Ř` only moves `e_a` to vectors of the same content.
* `jimbo_commute_weightProj`: **every `ρ(x)` preserves every weight space**.
* `cartan_mul_weightProj`: the Cartan element `cartan c` acts on `V_μ` by the scalar
  `∏_x c(x)^{μ(x)}`.  With `c = (q on letter y, 1 elsewhere)` this is `K_y = q^{μ(y)}`.
* `content_of_raiseOp_ne_zero`: `E_i` moves content by `α_i = e_{i+1} − e_i`: a nonzero entry
  `E_i(a, b)` has one more `i+1` and one fewer `i` in `a` than in `b`.
  `weightProj_mul_raiseOp_mul_weightProj`: hence `P_ν E_i P_μ = 0` unless `ν = μ + α_i`.

## Highest-weight spaces (G3.3)

`hwSpace μ = V_μ ∩ ⋂_i ker E_i` — the `gl_d` analogue of the `d = 2` space
`W_{r,j} = ker E ∩ V_{r−j}` of `Archimedean/SchurWeylTrace`.

* `jimbo_mem_hwSpace`: **`ρ(H)` maps each highest-weight space into itself**, so each `hwSpace μ`
  is an `H_n(q)`-module.  This is the module that G3.4 must identify with the Specht module `S_μ`.

## Not here

That `hwSpace μ = 0` unless `μ` is dominant, `hwSpace λ ≅ S_λ`, and the decomposition
`V^{⊗n} = ⊕ W_λ ⊗ S_λ` are G3.4 (bean `qou-gl34`).

## Base ring (§7c)

`content`, the projectors and the entry lemmas: any commutative ring.  The `ρ(H)` statements:
any field, as for the Jimbo action.

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.IwahoriHecke.TensorEmbedGL QOU.SchurWeyl.JimboGL Matrix

section Content

variable {d n : ℕ}

/-- The weight (content) of a basis word: how many sites carry each letter. -/
def content (a : Fin n → Fin d) (x : Fin d) : ℕ := (Finset.univ.filter fun k => a k = x).card

theorem content_eq_sum (a : Fin n → Fin d) (x : Fin d) :
    content a x = ∑ k, if a k = x then 1 else 0 := by
  rw [content, Finset.card_filter]

/-- A product weight is a function of the content. -/
theorem prod_eq_prod_pow_content {R : Type*} [CommMonoid R] (c : Fin d → R)
    (a : Fin n → Fin d) : ∏ k, c (a k) = ∏ x, c x ^ content a x := by
  rw [← Finset.prod_fiberwise Finset.univ a (fun k => c (a k))]
  refine Finset.prod_congr rfl fun x _ => ?_
  rw [Finset.prod_congr rfl (fun k hk => by rw [(Finset.mem_filter.mp hk).2]), Finset.prod_const,
    content]

/-- **`Ř` preserves content**: a nonzero entry of `Ř` at sites `i, j` joins two words with the
same content. -/
theorem content_eq_of_embedPair_ne_zero {R : Type*} [CommRing R] (q qi : R) {i j : Fin n}
    (hij : i ≠ j) {a b : Fin n → Fin d} (h : embedPair i j (rCheckN q qi) a b ≠ 0) :
    content a = content b := by
  classical
  funext x
  rw [content_eq_sum, content_eq_sum]
  rw [embedPair_apply] at h
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab] at h
    have hpair : ((if a i = x then 1 else 0) + if a j = x then 1 else 0 : ℕ)
        = (if b i = x then 1 else 0) + if b j = x then 1 else 0 := by
      rcases rCheckN_commute_wDiag2.rCheckN_ne_zero' q qi h with e | e
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2]
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2, add_comm]
    rw [← Finset.sum_add_sum_compl {i, j} (fun s => if a s = x then 1 else 0),
      ← Finset.sum_add_sum_compl {i, j} (fun s => if b s = x then 1 else 0),
      Finset.sum_pair hij, Finset.sum_pair hij, hpair]
    congr 1
    refine Finset.sum_congr rfl fun s hs => ?_
    simp only [Finset.mem_compl, Finset.mem_insert, Finset.mem_singleton, not_or] at hs
    rw [hab s hs.1 hs.2]
  · rw [if_neg hab] at h; exact absurd rfl h

end Content

section Projectors

variable {R : Type*} [CommRing R] {d n : ℕ}

/-- The projector onto the weight space `V_μ`. -/
def weightProj (μ : Fin d → ℕ) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.diagonal fun a => if content a = μ then 1 else 0

theorem weightProj_mul_self (μ : Fin d → ℕ) :
    (weightProj μ : Matrix (Fin n → Fin d) (Fin n → Fin d) R) * weightProj μ = weightProj μ := by
  rw [weightProj, Matrix.diagonal_mul_diagonal]
  congr 1; funext a; split_ifs <;> simp

theorem weightProj_mul_weightProj_of_ne {μ ν : Fin d → ℕ} (h : μ ≠ ν) :
    (weightProj μ : Matrix (Fin n → Fin d) (Fin n → Fin d) R) * weightProj ν = 0 := by
  rw [weightProj, weightProj, Matrix.diagonal_mul_diagonal]
  ext a b
  rw [Matrix.diagonal_apply, Matrix.zero_apply]
  split_ifs with h1 h2 h3 <;> simp_all

theorem embedPair_commute_weightProj (q qi : R) (μ : Fin d → ℕ) {i j : Fin n} (hij : i ≠ j) :
    embedPair i j (rCheckN q qi) * weightProj μ = weightProj μ * embedPair i j (rCheckN q qi) := by
  ext a b
  rw [weightProj, Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases h : embedPair i j (rCheckN q qi) a b = 0
  · rw [h, zero_mul, mul_zero]
  · rw [content_eq_of_embedPair_ne_zero q qi hij h, mul_comm]

/-- **The Cartan element `cartan c` acts on `V_μ` by `∏_x c(x)^{μ(x)}`.** -/
theorem cartan_mul_weightProj (c : Fin d → R) (μ : Fin d → ℕ) :
    (cartan c : Matrix (Fin n → Fin d) (Fin n → Fin d) R) * weightProj μ
      = (∏ x, c x ^ μ x) • weightProj μ := by
  rw [cartan, weightProj, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_smul]
  congr 1
  funext a
  rw [Pi.smul_apply, smul_eq_mul, prod_eq_prod_pow_content]
  split_ifs with h
  · rw [h]
  · simp

end Projectors

section Raise

variable {R : Type*} [CommRing R] {d n : ℕ}

/-- **`E_i` shifts content by `α_i`.**  A nonzero entry `E_i(a, b)` changes one letter `i` of `b`
into `j = i + 1`. -/
theorem content_of_raiseOp_ne_zero (q qi : R) {i j : Fin d} (hij : (j : ℕ) = i + 1)
    {a b : Fin n → Fin d} (h : raiseOp (n := n) q qi i j a b ≠ 0) :
    content a j = content b j + 1 ∧ content a i + 1 = content b i ∧
      ∀ x, x ≠ i → x ≠ j → content a x = content b x := by
  classical
  have hji : j ≠ i := fun e => by rw [e] at hij; omega
  rw [raiseOp, siteOp, Matrix.sum_apply] at h
  obtain ⟨s, -, hs⟩ := Finset.exists_ne_zero_of_sum_ne_zero h
  simp only [siteTerm, Matrix.of_apply] at hs
  split_ifs at hs with hag
  swap
  · exact absurd rfl hs
  have hX : Matrix.single j i (1 : R) (a s) (b s) ≠ 0 := left_ne_zero_of_mul hs
  rw [single_apply'] at hX
  split_ifs at hX with hX'
  · obtain ⟨has, hbs⟩ := hX'
    have key : ∀ x, ((content a x : ℕ) + if b s = x then 1 else 0)
        = content b x + if a s = x then 1 else 0 := by
      intro x
      rw [content_eq_sum, content_eq_sum,
        ← Finset.add_sum_erase _ _ (Finset.mem_univ s),
        ← Finset.add_sum_erase _ (fun k => if b k = x then 1 else 0) (Finset.mem_univ s)]
      have hrest : ∑ k ∈ Finset.univ.erase s, (if a k = x then 1 else 0 : ℕ)
          = ∑ k ∈ Finset.univ.erase s, (if b k = x then 1 else 0) :=
        Finset.sum_congr rfl fun k hk => by rw [hag k (Finset.ne_of_mem_erase hk)]
      rw [hrest]; ring
    refine ⟨?_, ?_, fun x hxi hxj => ?_⟩
    · have := key j
      simp only [has, hbs, hji, Ne.symm hji, if_true, if_false] at this; omega
    · have := key i
      simp only [has, hbs, hji, Ne.symm hji, if_true, if_false] at this; omega
    · have := key x
      simp only [has, hbs, Ne.symm hxi, Ne.symm hxj, if_false] at this; omega
  · exact absurd rfl hX

/-- **`E_i` maps `V_μ` into `V_{μ+α_i}`**: `P_ν E_i P_μ = 0` unless `ν(j) = μ(j) + 1`,
`ν(i) + 1 = μ(i)` and `ν = μ` off `{i, j}`. -/
theorem weightProj_mul_raiseOp_mul_weightProj (q qi : R) {i j : Fin d} (hij : (j : ℕ) = i + 1)
    {μ ν : Fin d → ℕ}
    (h : ¬ (ν j = μ j + 1 ∧ ν i + 1 = μ i ∧ ∀ x, x ≠ i → x ≠ j → ν x = μ x)) :
    (weightProj ν : Matrix (Fin n → Fin d) (Fin n → Fin d) R) * raiseOp q qi i j * weightProj μ
      = 0 := by
  ext a b
  rw [weightProj, weightProj, Matrix.mul_diagonal, Matrix.diagonal_mul, Matrix.zero_apply]
  by_cases hE : raiseOp (n := n) q qi i j a b = 0
  · rw [hE, mul_zero, zero_mul]
  · obtain ⟨h1, h2, h3⟩ := content_of_raiseOp_ne_zero q qi hij hE
    by_cases ha : content a = ν
    · by_cases hb : content b = μ
      · exfalso; apply h; subst ha; subst hb; exact ⟨h1, h2, h3⟩
      · rw [if_neg hb, mul_zero]
    · rw [if_neg ha, zero_mul, zero_mul]

end Raise

section Hecke

variable {K : Type*} [Field K] {d : ℕ}

theorem strandBraid_commute_weightProj {m : ℕ} (q qi : K) (a : Fin m) (μ : Fin d → ℕ) :
    strandBraid q qi a * weightProj μ = weightProj μ * strandBraid q qi a := by
  rw [strandBraid, braidAt]
  exact embedPair_commute_weightProj q qi μ (by simp [Fin.ext_iff])

/-- **Every `ρ(x)` preserves every weight space.** -/
theorem jimbo_commute_weightProj (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ)
    (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x * weightProj μ = weightProj μ * jimbo d q hq m x :=
  jimbo_commute_of q hq m _ (fun a => strandBraid_commute_weightProj q q⁻¹ a μ) x

/-- **The highest-weight space** `V_μ ∩ ⋂_i ker E_i` of `(K^d)^{⊗(m+1)}`. -/
def hwSpace (q : K) (m : ℕ) (μ : Fin d → ℕ) : Submodule K ((Fin (m + 1) → Fin d) → K) where
  carrier := {v | weightProj μ *ᵥ v = v ∧
    ∀ i j : Fin d, (j : ℕ) = i + 1 → raiseOp q q⁻¹ i j *ᵥ v = 0}
  add_mem' {v w} hv hw := ⟨by rw [mulVec_add, hv.1, hw.1], fun i j hij => by
    rw [mulVec_add, hv.2 i j hij, hw.2 i j hij, add_zero]⟩
  zero_mem' := ⟨mulVec_zero _, fun _ _ _ => mulVec_zero _⟩
  smul_mem' c v hv := ⟨by rw [mulVec_smul, hv.1], fun i j hij => by
    rw [mulVec_smul, hv.2 i j hij, smul_zero]⟩

/-- **`ρ(H)` preserves every highest-weight space**: each `hwSpace μ` is an `H_{m+1}(q)`-module. -/
theorem jimbo_mem_hwSpace (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ)
    (x : Hecke K q q⁻¹ m) {v : (Fin (m + 1) → Fin d) → K} (hv : v ∈ hwSpace q m μ) :
    jimbo d q hq m x *ᵥ v ∈ hwSpace q m μ := by
  refine ⟨?_, fun i j hij => ?_⟩
  · rw [mulVec_mulVec, ← jimbo_commute_weightProj q hq m μ x, ← mulVec_mulVec, hv.1]
  · rw [mulVec_mulVec, ← jimbo_commute_raise q hq m hij x, ← mulVec_mulVec, hv.2 i j hij,
      mulVec_zero]

end Hecke

end QOU.SchurWeyl.QuantumGL
