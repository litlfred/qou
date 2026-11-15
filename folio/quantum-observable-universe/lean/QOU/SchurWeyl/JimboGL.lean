/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.IwahoriHecke.TensorEmbeddingGL
import QOU.SchurWeyl.JimboActionKernel
import QOU.SchurWeyl.WenzlMarkovTraceInstance

/-!
# Level `d` is `gl_d` Schur–Weyl: the Jimbo action on `(K^d)^{⊗(m+1)}`

`QOU.SchurWeyl.JimboActionKernel` identified the kernel and image of the Jimbo `Ř`-action of the
Hecke algebra on `V^{⊗(m+1)}` for `dim V = 2`, and identified its weighted trace with the
convention-D (level-2) Ocneanu trace.  This file does the same for **every** `d = dim V ≥ 1`, using
the `gl_d` action `TensorEmbedGL.heckeActionGL`.

## Results

* `jimboMarkov` — over any field, with `[d]_{q²} = 1 + q² + ⋯ + q^{2(d−1)} ≠ 0`: the weighted trace
  `x ↦ Tr(K^{⊗(n+1)} ρ(x)) / [d]_{q²}^{n+1}`, `K = diag(1, q², …, q^{2(d−1)})`, is a Markov trace
  family with parameter `z_d = q^{2d−1} / [d]_{q²}` — Wenzl's level-`d` parameter
  `(q²)^d / (q · [d]_{q²})`.  The Markov property is the partial-trace identity `partial_last`:
  `q · Σ_x K_x Ř_{(u,x),(v,x)} = (q²)^d δ_{uv}` (`curl`).
* `jimboTrace_eq_wenzl` — with `q` not a root of unity, it IS the level-`d` Wenzl trace
  `wtraceW (wenzlWeight d (q²))` of `WenzlMarkovTraceInstance`, by uniqueness of the Markov trace.
  At `d = 2` this is `JimboActionKernel.jimboTrace_eq_wtrace` again (`wenzlMarkovTrace_two_tr`).
* `ker_jimbo_eq_traceRadicalIdeal` — over any linearly ordered field: `ker ρ = rad(tr)`.  Same
  argument as at `d = 2`: the image is closed under transpose (`Ř` is symmetric) and
  `X ↦ Tr(K^{⊗n} X Xᵀ)` is positive definite (`K` is positive diagonal).
* `jimbo_eq_zero_iff_rowCap_blocks_vanish` — `ρ(x) = 0` iff every seminormal block with at most
  `d` rows kills `x`: blocks with more than `d` rows act by zero, the others faithfully.
* `finrank_range_jimbo` — `dim (image) = Σ_{λ ⊢ m+1, ℓ(λ) ≤ d} (f^λ)²`.

## Scope

* Kernel, block and dimension statements need an ordered field (positivity).
* Surjectivity onto the `U_q(gl_d)` commutant — the full double-centraliser statement — is **not**
  claimed: only the kernel and the image dimension.

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.SchurWeyl.JimboGL

open QOU.IwahoriHecke.TensorEmbedGL QOU.MathlibExt.SkeinRelation
open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.IwahoriHecke.Balanced
open QOU.SchurWeyl.JimboActionKernel (skeinCoxAEquiv skeinCoxAEquiv_σ hqi)
open QOU.IwahoriHecke.TensorEmbed (tensorIdHom tensorId)

variable {K : Type*} [Field K] {d : ℕ}

section Bridge

/-- The `gl_d` Jimbo action on the skein Hecke algebra. -/
noncomputable def jimbo (d : ℕ) (q : K) (hq : q ≠ 0) (m : ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K :=
  (heckeActionGL q q⁻¹ (hqi hq)).comp (skeinCoxAEquiv q hq m).toAlgHom

@[simp] theorem jimbo_σ (q : K) (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    jimbo d q hq m (Hecke.σ K q q⁻¹ m i) = strandBraid q q⁻¹ i := by
  simp [jimbo]

theorem jimbo_apply (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x = heckeActionGL q q⁻¹ (hqi hq) (skeinCoxAEquiv q hq m x) := rfl

end Bridge

section Weights

/-- The site weight `K = diag(1, q², …, q^{2(d−1)})`. -/
def wt (q : K) (x : Fin d) : K := (q ^ 2) ^ (x : ℕ)

/-- The diagonal of `K^{⊗N}` on the monomial basis. -/
def dWeight (q : K) {N : ℕ} (a : Fin N → Fin d) : K := ∏ s, wt q (a s)

/-- The weighted (quantum) trace `Tr(K^{⊗N} X)`. -/
def qtr (q : K) {N : ℕ} (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K) : K :=
  ∑ a, dWeight q a * X a a

theorem qtr_add (q : K) {N : ℕ} (X Y : Matrix (Fin N → Fin d) (Fin N → Fin d) K) :
    qtr q (X + Y) = qtr q X + qtr q Y := by
  simp only [qtr, Matrix.add_apply, mul_add, Finset.sum_add_distrib]

theorem qtr_smul (q : K) {N : ℕ} (c : K) (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K) :
    qtr q (c • X) = c * qtr q X := by
  simp only [qtr, Matrix.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun _ _ => by ring

theorem qtr_zero (q : K) {N : ℕ} : qtr q (0 : Matrix (Fin N → Fin d) (Fin N → Fin d) K) = 0 := by
  simp [qtr]

theorem dWeight_snoc (q : K) {N : ℕ} (a : Fin N → Fin d) (x : Fin d) :
    dWeight q (Fin.snoc (α := fun _ => Fin d) a x) = dWeight q a * wt q x := by
  simp only [dWeight, Fin.prod_univ_castSucc, Fin.snoc_castSucc, Fin.snoc_last]

theorem sum_snoc {N : ℕ} (F : (Fin (N + 1) → Fin d) → K) :
    ∑ a, F a = ∑ a : Fin N → Fin d, ∑ x : Fin d, F (Fin.snoc (α := fun _ => Fin d) a x) := by
  rw [← (Fin.snocEquiv fun _ => Fin d).sum_comp, Fintype.sum_prod_type, Finset.sum_comm]
  rfl

/-- `Σ_x K_x = [d]_{q²}`. -/
theorem sum_wt (q : K) : ∑ x : Fin d, wt q x = levelBracket d (q ^ 2) :=
  Fin.sum_univ_eq_sum_range (fun i => (q ^ 2) ^ i) d

theorem sum_dWeight (q : K) : ∀ N : ℕ,
    ∑ a : Fin N → Fin d, dWeight q a = levelBracket d (q ^ 2) ^ N
  | 0 => by simp [dWeight]
  | N + 1 => by
      rw [sum_snoc]
      simp only [dWeight_snoc, ← Finset.mul_sum, sum_wt, ← Finset.sum_mul, sum_dWeight q N,
        pow_succ]

theorem qtr_one (q : K) (N : ℕ) :
    qtr q (1 : Matrix (Fin N → Fin d) (Fin N → Fin d) K) = levelBracket d (q ^ 2) ^ N := by
  simp [qtr, sum_dWeight]

end Weights

section Extension

variable {N : ℕ} [NeZero d]

/-- `(Fin N → Fin d) × Fin d ≃ (Fin (N+1) → Fin d)`, the new site appended last. -/
def snocE (N : ℕ) : (Fin N → Fin d) × Fin d ≃ (Fin (N + 1) → Fin d) :=
  (Equiv.prodComm _ _).trans (Fin.snocEquiv fun _ => Fin d)

/-- `X ↦ X ⊗ 1`, the new tensor factor appended last, as an algebra map. -/
noncomputable def extLast [NeZero d] (N : ℕ) :
    Matrix (Fin N → Fin d) (Fin N → Fin d) K →ₐ[K]
      Matrix (Fin (N + 1) → Fin d) (Fin (N + 1) → Fin d) K :=
  (Matrix.reindexAlgEquiv K K (snocE N)).toAlgHom.comp
    (tensorIdHom (σ := Fin N → Fin d) (ρ := Fin d))

theorem extLast_apply (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K)
    (a b : Fin (N + 1) → Fin d) :
    extLast N X a b = X (Fin.init a) (Fin.init b)
      * (if a (Fin.last N) = b (Fin.last N) then 1 else 0) := by
  simp [extLast, snocE, Matrix.reindexAlgEquiv_apply, tensorIdHom, Matrix.reindex_apply,
    Matrix.submatrix_apply, Equiv.prodComm]

theorem extLast_snoc (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K)
    (a b : Fin N → Fin d) (x y : Fin d) :
    extLast N X (Fin.snoc (α := fun _ => Fin d) a x) (Fin.snoc (α := fun _ => Fin d) b y)
      = X a b * (if x = y then 1 else 0) := by
  rw [extLast_apply, Fin.init_snoc, Fin.init_snoc, Fin.snoc_last, Fin.snoc_last]

theorem qtr_extLast (q : K) (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K) :
    qtr q (extLast N X) = levelBracket d (q ^ 2) * qtr q X := by
  rw [qtr, sum_snoc]
  simp only [extLast_snoc, if_true, mul_one, dWeight_snoc, qtr, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [← sum_wt q, Finset.sum_mul]
  exact Finset.sum_congr rfl fun x _ => by ring

/-- A two-site operator at sites `i, j < N` of `V^{⊗(N+1)}` is the extension of the same
operator on `V^{⊗N}`. -/
theorem embedPair_castSucc (i j : Fin N) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) K) :
    embedPair i.castSucc j.castSucc M = extLast N (embedPair i j M) := by
  ext a b
  rw [extLast_apply, embedPair_apply, embedPair_apply]
  simp only [Fin.init]
  by_cases hl : a (Fin.last N) = b (Fin.last N)
  · rw [if_pos hl, mul_one]
    by_cases h : ∀ k : Fin N, k ≠ i → k ≠ j → a k.castSucc = b k.castSucc
    · rw [if_pos h, if_pos]
      intro k hki hkj
      induction k using Fin.lastCases with
      | last => exact hl
      | cast k => exact h k (fun e => hki (by rw [e])) (fun e => hkj (by rw [e]))
    · rw [if_neg h, if_neg]
      intro h'
      exact h (fun k hki hkj => h' k.castSucc
        (fun e => hki (Fin.castSucc_injective _ e))
        (fun e => hkj (Fin.castSucc_injective _ e)))
  · rw [if_neg hl, mul_zero, if_neg]
    intro h'
    exact hl (h' (Fin.last N) (Fin.castSucc_lt_last i).ne' (Fin.castSucc_lt_last j).ne')

end Extension

section Markov

/-- The curl identity over `ℕ`: `q · Σ_{x<D} q^{2x} c(u,x) = q^{2D}` for `u < D`, where
`c(u,u) = q`, `c(u,x) = q − qi` for `u < x`, and `0` for `x < u`. -/
theorem curl_nat (q qi : K) (hqi : q * qi = 1) (u : ℕ) :
    ∀ D : ℕ, u < D → q * ∑ x ∈ Finset.range D,
      (q ^ 2) ^ x * (if u = x then q else if u < x then q - qi else 0) = (q ^ 2) ^ D
  | 0, h => absurd h (Nat.not_lt_zero u)
  | D + 1, h => by
      rw [Finset.sum_range_succ, mul_add]
      rcases Nat.lt_succ_iff_lt_or_eq.mp h with h' | h'
      · rw [curl_nat q qi hqi u D h', if_neg h'.ne, if_pos h']
        linear_combination (-(q ^ 2) ^ D) * hqi
      · subst h'
        rw [Finset.sum_eq_zero fun x hx => by
          have hx' := Finset.mem_range.mp hx
          rw [if_neg (by omega), if_neg (by omega), mul_zero], if_pos rfl]
        ring

/-- The curl identity on `Fin d`. -/
theorem curl (q qi : K) (hqi : q * qi = 1) (u : Fin d) :
    q * ∑ x : Fin d, wt q x * (if u = x then q else if u < x then q - qi else 0) = (q ^ 2) ^ d := by
  have e : ∀ x : Fin d, wt q x * (if u = x then q else if u < x then q - qi else 0)
      = (fun i : ℕ => (q ^ 2) ^ i * (if (u : ℕ) = i then q else if (u : ℕ) < i then q - qi else 0))
          x := by
    intro x
    simp only [wt, Fin.ext_iff, Fin.lt_iff_val_lt_val]
  rw [Finset.sum_congr rfl fun x _ => e x, Fin.sum_univ_eq_sum_range
    (fun i : ℕ => (q ^ 2) ^ i * (if (u : ℕ) = i then q else if (u : ℕ) < i then q - qi else 0)) d]
  exact curl_nat q qi hqi u d u.2

/-- The partial `K`-trace of `Ř` over the second factor. -/
theorem sum_wt_diag (q qi : K) (hqi : q * qi = 1) (u v : Fin d) :
    ∑ x : Fin d, wt q x * rCheckN q qi (u, x) (v, x)
      = q⁻¹ * (q ^ 2) ^ d * (if u = v then 1 else 0) := by
  have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
  by_cases huv : u = v
  · subst huv
    rw [if_pos rfl, mul_one, ← curl q qi hqi u, ← mul_assoc, inv_mul_cancel₀ hq0, one_mul]
    refine Finset.sum_congr rfl fun x _ => ?_
    simp
  · rw [if_neg huv, mul_zero]
    refine Finset.sum_eq_zero fun x _ => ?_
    have : rCheckN q qi (u, x) (v, x) = 0 := by
      simp only [rCheckN_apply, Prod.ext_iff]
      rw [if_neg (fun h => huv h.1), if_neg (fun h => huv (h.1.trans h.2))]
    rw [this, mul_zero]

/-- The partial `K`-trace of `Ř` over the appended last site is `q^{2d−1}` times the identity. -/
theorem partial_last [NeZero d] (q qi : K) (hqi : q * qi = 1) {N : ℕ} (c a : Fin (N + 1) → Fin d) :
    ∑ x : Fin d, wt q x * embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheckN q qi)
        (Fin.snoc (α := fun _ => Fin d) c x) (Fin.snoc (α := fun _ => Fin d) a x)
      = q⁻¹ * (q ^ 2) ^ d * (if c = a then 1 else 0) := by
  have hcond : ∀ x : Fin d,
      (∀ k : Fin (N + 2), k ≠ (Fin.last N).castSucc → k ≠ Fin.last (N + 1) →
          Fin.snoc (α := fun _ => Fin d) c x k = Fin.snoc (α := fun _ => Fin d) a x k)
        ↔ ∀ k : Fin (N + 1), k ≠ Fin.last N → c k = a k := by
    intro x
    constructor
    · intro h k hk
      have := h k.castSucc (fun e => hk (Fin.castSucc_injective _ e))
        (Fin.castSucc_lt_last k).ne
      simpa [Fin.snoc_castSucc] using this
    · intro h k hk1 hk2
      induction k using Fin.lastCases with
      | last => exact absurd rfl hk2
      | cast k =>
          rw [Fin.snoc_castSucc, Fin.snoc_castSucc]
          exact h k (fun e => hk1 (by rw [e]))
  simp only [embedPair_apply, hcond, Fin.snoc_castSucc, Fin.snoc_last]
  by_cases hP : ∀ k : Fin (N + 1), k ≠ Fin.last N → c k = a k
  · have hca : c = a ↔ c (Fin.last N) = a (Fin.last N) := by
      constructor
      · intro h; rw [h]
      · intro h; funext k
        by_cases hk : k = Fin.last N
        · rw [hk]; exact h
        · exact hP k hk
    simp only [if_pos hP, hca]
    generalize c (Fin.last N) = u
    generalize a (Fin.last N) = v
    exact sum_wt_diag q qi hqi u v
  · have hca : c ≠ a := fun h => hP fun k _ => by rw [h]
    simp [if_neg hP, hca]

theorem qtr_extLast_mul_last [NeZero d] (q qi : K) (hqi : q * qi = 1) {N : ℕ}
    (X : Matrix (Fin (N + 1) → Fin d) (Fin (N + 1) → Fin d) K) :
    qtr q (extLast (N + 1) X
        * embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheckN q qi))
      = q⁻¹ * (q ^ 2) ^ d * qtr q X := by
  set B := embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheckN q qi) with hB
  have h1 : ∀ (a : Fin (N + 1) → Fin d) (x : Fin d),
      (extLast (N + 1) X * B) (Fin.snoc (α := fun _ => Fin d) a x)
          (Fin.snoc (α := fun _ => Fin d) a x)
        = ∑ c, X a c * B (Fin.snoc (α := fun _ => Fin d) c x)
            (Fin.snoc (α := fun _ => Fin d) a x) := by
    intro a x
    rw [Matrix.mul_apply, sum_snoc]
    refine Finset.sum_congr rfl fun c _ => ?_
    simp only [extLast_snoc, mul_ite, mul_one, mul_zero, ite_mul, zero_mul]
    rw [Finset.sum_ite_eq]
    simp
  rw [qtr, sum_snoc]
  simp only [dWeight_snoc, h1]
  rw [qtr, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  have e : ∀ x : Fin d, dWeight q a * wt q x * ∑ c, X a c
        * B (Fin.snoc (α := fun _ => Fin d) c x) (Fin.snoc (α := fun _ => Fin d) a x)
      = ∑ c, dWeight q a * X a c * (wt q x
        * B (Fin.snoc (α := fun _ => Fin d) c x) (Fin.snoc (α := fun _ => Fin d) a x)) := by
    intro x
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun _ _ => by ring
  simp only [e]
  rw [Finset.sum_comm]
  simp only [← Finset.mul_sum, hB, partial_last q qi hqi]
  rw [Finset.sum_eq_single a]
  · simp; ring
  · intro c _ hc; simp [hc]
  · simp

end Markov

section Image

open QOU.SchurWeyl.HeckeInclusion
open scoped Matrix

/-- Everything in the image of `jimbo` lies in any subalgebra containing the strand
braidings. -/
theorem jimbo_mem (q : K) (hq : q ≠ 0) (m : ℕ)
    (S : Subalgebra K (Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K))
    (h : ∀ i, strandBraid q q⁻¹ i ∈ S) (x : Hecke K q q⁻¹ m) : jimbo d q hq m x ∈ S := by
  have hx : x ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ m)) := by
    rw [adjoin_range_σ_eq_top K q q⁻¹ m]; trivial
  have h2 : jimbo d q hq m x
      ∈ (Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ m))).map (jimbo d q hq m) :=
    Subalgebra.mem_map.mpr ⟨x, hx, rfl⟩
  rw [AlgHom.map_adjoin] at h2
  refine Algebra.adjoin_le ?_ h2
  rintro _ ⟨_, ⟨i, rfl⟩, rfl⟩
  simpa using h i

theorem rCheckN_ne_zero {q qi : K} {u v : Fin d × Fin d} (h : rCheckN q qi u v ≠ 0) :
    u = v ∨ u = (v.2, v.1) := by
  by_contra hc
  push_neg at hc
  exact h (by simp [rCheckN_apply, hc.1, hc.2])

theorem dWeight_eq_of_embedPair_ne_zero (q qi : K) {n : ℕ} {i j : Fin n} (hij : i ≠ j)
    {a b : Fin n → Fin d} (h : embedPair i j (rCheckN q qi) a b ≠ 0) :
    dWeight q a = dWeight q b := by
  classical
  rw [embedPair_apply] at h
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab] at h
    have hpair : wt q (a i) * wt q (a j) = wt q (b i) * wt q (b j) := by
      rcases rCheckN_ne_zero h with e | e
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2]
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2, mul_comm]
    unfold dWeight
    rw [← Finset.prod_mul_prod_compl {i, j} (fun s => wt q (a s)),
      ← Finset.prod_mul_prod_compl {i, j} (fun s => wt q (b s)),
      Finset.prod_pair hij, Finset.prod_pair hij, hpair]
    congr 1
    refine Finset.prod_congr rfl fun s hs => ?_
    simp only [Finset.mem_compl, Finset.mem_insert, Finset.mem_singleton, not_or] at hs
    rw [hab s hs.1 hs.2]
  · rw [if_neg hab] at h; exact absurd rfl h

/-- `K^{⊗n}` as a diagonal matrix. -/
def dMat (d : ℕ) (q : K) (N : ℕ) : Matrix (Fin N → Fin d) (Fin N → Fin d) K :=
  Matrix.diagonal (dWeight q)

theorem dMat_commute_embedPair (q qi : K) {n : ℕ} {i j : Fin n} (hij : i ≠ j) :
    dMat d q n * embedPair i j (rCheckN q qi) = embedPair i j (rCheckN q qi) * dMat d q n := by
  ext a b
  rw [dMat, Matrix.diagonal_mul, Matrix.mul_diagonal]
  by_cases h : embedPair i j (rCheckN q qi) a b = 0
  · rw [h, mul_zero, zero_mul]
  · rw [dWeight_eq_of_embedPair_ne_zero q qi hij h, mul_comm]

theorem dMat_commute_jimbo (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    dMat d q (m + 1) * jimbo d q hq m x = jimbo d q hq m x * dMat d q (m + 1) := by
  have := jimbo_mem q hq m (Subalgebra.centralizer K {dMat d q (m + 1)})
    (fun i => by
      rw [Subalgebra.mem_centralizer_iff]
      rintro g rfl
      exact dMat_commute_embedPair q q⁻¹ (by simp [Fin.ext_iff])) x
  rw [Subalgebra.mem_centralizer_iff] at this
  exact this _ rfl

theorem qtr_eq_trace (q : K) {N : ℕ} (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K) :
    qtr q X = (dMat d q N * X).trace := by
  simp [qtr, dMat, Matrix.trace, Matrix.diagonal_mul]

theorem qtr_jimbo_comm (q : K) (hq : q ≠ 0) (m : ℕ) (x y : Hecke K q q⁻¹ m) :
    qtr q (jimbo d q hq m (x * y)) = qtr q (jimbo d q hq m (y * x)) := by
  rw [map_mul, map_mul, qtr_eq_trace, qtr_eq_trace, ← mul_assoc,
    Matrix.trace_mul_comm, ← mul_assoc, ← dMat_commute_jimbo, mul_assoc]

theorem rCheckN_transpose (q qi : K) : (rCheckN (d := d) q qi)ᵀ = rCheckN q qi := by
  ext a b
  rcases a with ⟨a1, a2⟩
  rcases b with ⟨b1, b2⟩
  simp only [Matrix.transpose_apply, rCheckN_apply, Prod.ext_iff]
  by_cases h1 : a1 = b1 <;> by_cases h2 : a2 = b2 <;> by_cases h3 : a1 = b2 <;>
    by_cases h4 : a2 = b1 <;> simp_all [eq_comm]

theorem embedPair_transpose {n : ℕ} (i j : Fin n) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) K) :
    (embedPair i j M)ᵀ = embedPair i j Mᵀ := by
  ext a b
  rw [Matrix.transpose_apply, embedPair_apply, embedPair_apply, Matrix.transpose_apply]
  by_cases h : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos h, if_pos fun k h1 h2 => (h k h1 h2).symm]
  · rw [if_neg h, if_neg fun h' => h fun k h1 h2 => (h' k h1 h2).symm]

/-- The matrices whose transpose lies in a given subalgebra form a subalgebra. -/
def transposeSub {ι : Type*} [Fintype ι] [DecidableEq ι]
    (A : Subalgebra K (Matrix ι ι K)) : Subalgebra K (Matrix ι ι K) where
  carrier := {X | Xᵀ ∈ A}
  mul_mem' {X Y} hX hY := by
    simp only [Set.mem_setOf_eq, Matrix.transpose_mul]; exact A.mul_mem hY hX
  add_mem' {X Y} hX hY := by
    simp only [Set.mem_setOf_eq, Matrix.transpose_add]; exact A.add_mem hX hY
  algebraMap_mem' r := by
    simp only [Set.mem_setOf_eq, Algebra.algebraMap_eq_smul_one, Matrix.transpose_smul,
      Matrix.transpose_one]
    exact A.smul_mem A.one_mem r

/-- **The image of the Jimbo action is closed under transpose.** -/
theorem transpose_jimbo_mem_range (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    ∃ y, jimbo d q hq m y = (jimbo d q hq m x)ᵀ := by
  have := jimbo_mem q hq m (transposeSub (jimbo d q hq m).range)
    (fun i => by
      show (strandBraid q q⁻¹ i)ᵀ ∈ (jimbo d q hq m).range
      rw [strandBraid, braidAt, embedPair_transpose, rCheckN_transpose]
      exact ⟨Hecke.σ K q q⁻¹ m i, jimbo_σ q hq m i⟩) x
  exact this

end Image
section Trace

variable [NeZero d]

theorem jimbo_heckeIncl (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m x) = extLast (m + 1) (jimbo d q hq m x) := by
  have h : (jimbo d q hq (m + 1)).comp (heckeIncl K q q⁻¹ m)
      = (extLast (m + 1)).comp (jimbo d q hq m) := by
    apply Hecke.hom_ext
    intro i
    simp only [AlgHom.comp_apply, heckeIncl_σ, jimbo_σ, strandBraid, braidAt]
    rw [Fin.succ_castSucc]
    exact embedPair_castSucc _ _ _
  exact AlgHom.congr_fun h x

theorem jimbo_last (q : K) (hq : q ≠ 0) (m : ℕ) :
    jimbo d q hq (m + 1) (Hecke.σ K q q⁻¹ (m + 1) (Fin.last m))
      = embedPair (Fin.last m).castSucc (Fin.last (m + 1)) (rCheckN q q⁻¹) := by
  rw [jimbo_σ, strandBraid, braidAt, Fin.succ_last]

/-- `qtr` as a linear functional. -/
def qtrLin (d : ℕ) (q : K) (N : ℕ) : Matrix (Fin N → Fin d) (Fin N → Fin d) K →ₗ[K] K where
  toFun := qtr q
  map_add' := qtr_add q
  map_smul' c X := qtr_smul q c X

/-- **The normalised weighted trace of the `gl_d` Jimbo action**
`x ↦ Tr(K^{⊗(n+1)} ρ(x)) / [d]_{q²}^{n+1}`. -/
noncomputable def jimboTrace (d : ℕ) (q : K) (hq : q ≠ 0) (n : ℕ) : Hecke K q q⁻¹ n →ₗ[K] K :=
  (levelBracket d (q ^ 2) ^ (n + 1))⁻¹ • ((qtrLin d q (n + 1)).comp (jimbo d q hq n).toLinearMap)

theorem jimboTrace_apply (q : K) (hq : q ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    jimboTrace d q hq n x = (levelBracket d (q ^ 2) ^ (n + 1))⁻¹ * qtr q (jimbo d q hq n x) := rfl

/-- **The weighted trace of the `gl_d` Jimbo action is a Markov trace** with Wenzl's level-`d`
parameter `z_d = (q²)^d / (q · [d]_{q²})`.  Any field; `[d]_{q²} ≠ 0`. -/
noncomputable def jimboMarkov (q : K) (hq : q ≠ 0) (hL : levelBracket d (q ^ 2) ≠ 0) :
    HeckeCoset.MarkovTraceFamily K q q⁻¹ ((q ^ 2) ^ d / (q * levelBracket d (q ^ 2))) where
  tr := jimboTrace d q hq
  tr_one n := by
    rw [jimboTrace_apply, map_one, qtr_one]
    exact inv_mul_cancel₀ (pow_ne_zero _ hL)
  tr_cyclic n x y := by rw [jimboTrace_apply, jimboTrace_apply, qtr_jimbo_comm]
  tr_incl n x := by
    rw [jimboTrace_apply, jimboTrace_apply, jimbo_heckeIncl, qtr_extLast]
    field_simp
    ring
  tr_markov n x := by
    rw [jimboTrace_apply, jimboTrace_apply, map_mul, jimbo_heckeIncl, jimbo_last,
      qtr_extLast_mul_last q q⁻¹ (hqi hq)]
    field_simp
    ring

/-- **The `gl_d` Jimbo trace is the level-`d` Wenzl trace**, by uniqueness of the Markov trace at
`z_d`.  Any field, `q` not a root of unity. -/
theorem jimboTrace_eq_wenzl (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) (x : Hecke K q q⁻¹ n) :
    jimboTrace d q hq n x = SeminormalRep.wtraceW q hq hq2 (wenzlWeight d (q ^ 2)) n x :=
  SeminormalRep.eq_wenzlWtrace_of_markov q hq hq2 (gen_of_notRootOfUnity hq2) (NeZero.ne d)
    (jimboMarkov q hq (levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)))
    n x

end Trace

/-! From here on the base field carries a linear order: positivity of the weighted trace form. -/

section Kernel

open scoped Matrix
open QOU.QBeta.MarkovTraceQuotient

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] [NeZero d]

theorem dWeight_pos (q : L) (hq : q ≠ 0) {N : ℕ} (a : Fin N → Fin d) : 0 < dWeight q a :=
  Finset.prod_pos fun s _ => by unfold wt; positivity

/-- **The weighted trace form is positive definite on `X ↦ X Xᵀ`.** -/
theorem eq_zero_of_qtr_mul_transpose (q : L) (hq : q ≠ 0) {N : ℕ}
    (X : Matrix (Fin N → Fin d) (Fin N → Fin d) L) (h : qtr q (X * Xᵀ) = 0) : X = 0 := by
  have hdiag : ∀ a, (X * Xᵀ) a a = ∑ c, X a c * X a c := fun a => by
    simp [Matrix.mul_apply, Matrix.transpose_apply]
  have hnn : ∀ a ∈ (Finset.univ : Finset (Fin N → Fin d)), 0 ≤ dWeight q a * (X * Xᵀ) a a :=
    fun a _ => by
      rw [hdiag]
      exact mul_nonneg (dWeight_pos q hq a).le
        (Finset.sum_nonneg fun c _ => mul_self_nonneg _)
  have hterm := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp h
  ext a b
  have h1 := hterm a (Finset.mem_univ _)
  rw [hdiag] at h1
  have h2 : ∑ c, X a c * X a c = 0 :=
    (mul_eq_zero.mp h1).resolve_left (dWeight_pos q hq a).ne'
  have h3 := (Finset.sum_eq_zero_iff_of_nonneg (fun c _ => mul_self_nonneg (X a c))).mp h2 b
    (Finset.mem_univ _)
  simpa using mul_self_eq_zero.mp h3

/-- `x` acts by zero iff it is in the radical of the weighted trace form. -/
theorem jimbo_eq_zero_iff_qtr (q : L) (hq : q ≠ 0) (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo d q hq m x = 0 ↔ ∀ y, qtr q (jimbo d q hq m (x * y)) = 0 := by
  constructor
  · intro h y; rw [map_mul, h, zero_mul, qtr_zero]
  · intro h
    obtain ⟨y, hy⟩ := transpose_jimbo_mem_range q hq m x
    apply eq_zero_of_qtr_mul_transpose q hq
    rw [← hy, ← map_mul]
    exact h y

/-- **Kernel of the `gl_d` Jimbo action = radical of the level-`d` Wenzl trace form.** -/
theorem jimbo_eq_zero_iff_wenzl (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo d q hq m x = 0
      ↔ ∀ y, SeminormalRep.wtraceW q hq hq2 (wenzlWeight d (q ^ 2)) m (x * y) = 0 := by
  have hL : levelBracket d (q ^ 2) ≠ 0 :=
    levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)
  have hc : (levelBracket d (q ^ 2) ^ (m + 1))⁻¹ ≠ 0 := inv_ne_zero (pow_ne_zero _ hL)
  rw [jimbo_eq_zero_iff_qtr]
  refine forall_congr' fun y => ?_
  rw [← jimboTrace_eq_wenzl q hq hq2, jimboTrace_apply, mul_eq_zero, or_iff_right hc]

/-- **The kernel of the `gl_d` Jimbo action is the trace-radical ideal of the level-`d` trace.** -/
theorem ker_jimbo_eq_traceRadicalIdeal (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    TwoSidedIdeal.ker (jimbo d q hq m)
      = traceRadicalIdeal (SeminormalRep.wtraceW q hq hq2 (wenzlWeight d (q ^ 2)) m)
          (SeminormalRep.wtraceW_cyclic q hq hq2 _ m) := by
  ext x
  rw [TwoSidedIdeal.mem_ker, mem_traceRadicalIdeal, jimbo_eq_zero_iff_wenzl q hq hq2]
  rfl

end Kernel

section Blocks

open YoungDiagram QOU.Mathlib SeminormalRep

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] [NeZero d]

theorem wenzlWeight_eq_zero_of_rows (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (μ : YoungDiagram) (h : d < μ.colLen 0) : wenzlWeight d (q ^ 2) μ = 0 :=
  (wenzlWeight_eq_zero_iff (pow_ne_zero 2 hq) (gen_of_notRootOfUnity hq2)
    (levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)) μ).mpr h

theorem wenzlWeight_ne_zero_of_rows (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (μ : YoungDiagram) (h : μ.colLen 0 ≤ d) : wenzlWeight d (q ^ 2) μ ≠ 0 :=
  wenzlWeight_ne_zero_of_le_rows (pow_ne_zero 2 hq) (gen_of_notRootOfUnity hq2)
    (levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)) μ h

/-- **Every block with more than `d` rows acts by zero.** -/
theorem jimbo_eq_zero_of_rowCap_blocks_vanish (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (x : Hecke L q q⁻¹ m)
    (hx : ∀ (μ : YoungDiagram) (hμ : μ.cells.card = m + 1), μ.colLen 0 ≤ d →
      seminormalRep q hq hq2 m hμ x = 0) :
    jimbo d q hq m x = 0 := by
  rw [jimbo_eq_zero_iff_wenzl q hq hq2]
  intro y
  rw [wtraceW_apply]
  refine Finset.sum_eq_zero fun ν _ => ?_
  by_cases h : ν.1.colLen 0 ≤ d
  · rw [map_mul, hx ν.1 ν.2 h, zero_mul, Matrix.trace_zero, mul_zero]
  · rw [wenzlWeight_eq_zero_of_rows q hq hq2 ν.1 (by omega), zero_mul]

/-- **Every block with at most `d` rows survives.** -/
theorem rowCap_block_eq_zero_of_jimbo_eq_zero (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (x : Hecke L q q⁻¹ m) (hx : jimbo d q hq m x = 0)
    (μ : YoungDiagram) (hμ : μ.cells.card = m + 1) (hrow : μ.colLen 0 ≤ d) :
    seminormalRep q hq hq2 m hμ x = 0 := by
  classical
  by_contra hne
  have hrad := (jimbo_eq_zero_iff_wenzl q hq hq2 m x).mp hx
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq μ hμ
  subst hlam₀
  obtain ⟨N, hN⟩ := WtraceRadicalTwoRow.exists_trace_mul_ne_zero hne
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq hq2 m (Function.update 0 lam₀ N)
  apply hN.elim
  have h0 := hrad b
  rw [wtraceW_apply] at h0
  rw [← Equiv.sum_comp (partitionShapeEquiv (m + 1))
    (fun ν : {ν : YoungDiagram // ν.cells.card = m + 1} =>
      wenzlWeight d (q ^ 2) ν.1 * (seminormalRep q hq hq2 m ν.2 (x * b)).trace)] at h0
  have hρ : ∀ (lam : Nat.Partition (m + 1)) (y : Hecke L q q⁻¹ m),
      seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam).2 y
        = heckeProduct q hq hq2 m y lam := fun _ _ => rfl
  rw [Finset.sum_eq_single_of_mem lam₀ (Finset.mem_univ lam₀)] at h0
  · have hbN : heckeProduct q hq hq2 m b lam₀ = N := by rw [hb]; simp
    have htr : (seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam₀).2 (x * b)).trace
        = (seminormalRep q hq hq2 m hμ x * N).trace := by
      rw [map_mul, hρ lam₀ b, hbN]
      rfl
    rw [htr] at h0
    exact (mul_eq_zero.mp h0).resolve_left (wenzlWeight_ne_zero_of_rows q hq hq2 _ hrow)
  · intro lam _ hlam
    have hbz : heckeProduct q hq hq2 m b lam = 0 := by rw [hb]; simp [hlam]
    have hz : seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam).2 (x * b) = 0 := by
      rw [map_mul, hρ lam b, hbz, mul_zero]
    rw [hz, Matrix.trace_zero, mul_zero]

/-- **`gl_d` Schur–Weyl, kernel form.** The Jimbo action kills `x` exactly when every seminormal
block with at most `d` rows does: the kernel is the sum of the blocks with more than `d` rows. -/
theorem jimbo_eq_zero_iff_rowCap_blocks_vanish (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo d q hq m x = 0 ↔ ∀ (μ : YoungDiagram) (hμ : μ.cells.card = m + 1), μ.colLen 0 ≤ d →
      seminormalRep q hq hq2 m hμ x = 0 :=
  ⟨fun h μ hμ hrow => rowCap_block_eq_zero_of_jimbo_eq_zero q hq hq2 m x h μ hμ hrow,
    jimbo_eq_zero_of_rowCap_blocks_vanish q hq hq2 m x⟩

end Blocks

section Dimension

open YoungDiagram QOU.Mathlib SeminormalRep

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] [NeZero d]

/-- Partitions of `m + 1` with at most `d` rows. -/
abbrev RowCapIdx (d m : ℕ) : Type :=
  {lam : Nat.Partition (m + 1) // (partitionShape lam).colLen 0 ≤ d}

/-- The projection onto the at-most-`d`-row seminormal blocks. -/
noncomputable def rowCapProd (d : ℕ) (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) :
    Hecke L q q⁻¹ m →ₐ[L] (∀ lam : RowCapIdx d m,
      Matrix (StandardYoungTableau (partitionShape lam.1))
        (StandardYoungTableau (partitionShape lam.1)) L) :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq hq2 m (partitionShape_card_succ lam.1))

theorem rowCapProd_surjective (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Surjective (rowCapProd d q hq hq2 m) := by
  classical
  intro f
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq hq2 m
    (fun lam => if h : (partitionShape lam).colLen 0 ≤ d then f ⟨lam, h⟩ else 0)
  refine ⟨b, ?_⟩
  funext lam
  have h1 : rowCapProd d q hq hq2 m b lam = heckeProduct q hq hq2 m b lam.1 := rfl
  rw [h1, hb]
  simp only [dif_pos lam.2]

theorem jimbo_eq_zero_iff_rowCapProd (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo d q hq m x = 0 ↔ rowCapProd d q hq hq2 m x = 0 := by
  rw [jimbo_eq_zero_iff_rowCap_blocks_vanish q hq hq2]
  constructor
  · intro h
    funext lam
    exact h _ (partitionShape_card_succ lam.1) lam.2
  · intro h μ hμ hrow
    obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq μ hμ
    subst hlam₀
    exact congrFun h ⟨lam₀, hrow⟩

/-- **Dimension of the image of the `gl_d` Jimbo action** = `∑_{ℓ(λ) ≤ d} (f^λ)²`. -/
theorem finrank_range_jimbo (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Module.finrank L (LinearMap.range (jimbo d q hq m).toLinearMap)
      = ∑ lam : RowCapIdx d m,
          Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2 := by
  haveI := finiteDimensional_hecke q q⁻¹ m
  have hker : LinearMap.ker (jimbo d q hq m).toLinearMap
      = LinearMap.ker (rowCapProd d q hq hq2 m).toLinearMap := by
    ext x
    simp only [LinearMap.mem_ker, AlgHom.toLinearMap_apply]
    exact jimbo_eq_zero_iff_rowCapProd q hq hq2 m x
  have h1 := LinearMap.finrank_range_add_finrank_ker (jimbo d q hq m).toLinearMap
  have h2 := LinearMap.finrank_range_add_finrank_ker (rowCapProd d q hq hq2 m).toLinearMap
  have hr : LinearMap.range (rowCapProd d q hq hq2 m).toLinearMap = ⊤ :=
    LinearMap.range_eq_top.mpr (rowCapProd_surjective q hq hq2 m)
  rw [hr, finrank_top, Module.finrank_pi_fintype] at h2
  rw [hker] at h1
  have h3 : Module.finrank L (LinearMap.range (jimbo d q hq m).toLinearMap)
      = ∑ lam : RowCapIdx d m, Module.finrank L
          (Matrix (StandardYoungTableau (partitionShape lam.1))
            (StandardYoungTableau (partitionShape lam.1)) L) := by omega
  rw [h3]
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [Module.finrank_matrix, Module.finrank_self, mul_one, sq]

end Dimension

end QOU.SchurWeyl.JimboGL
