/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.IwahoriHecke.TensorEmbedding
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.QBeta.MarkovTraceQuotient
import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.TraceQuotCatalan
import Mathlib.RingTheory.TwoSidedIdeal.Kernel

/-!
# The kernel of the Jimbo action on `V^{⊗(m+1)}`, `dim V = 2`

`TensorEmbedding.heckeActionN` is the Jimbo `Ř`-matrix action
`H_{m+1}(q) → End(V^{⊗(m+1)})` and its own docstring records its kernel as open
(item 1 of "What `heckeActionN` does NOT say").  This file identifies it.

## Results

* `skeinCoxAEquiv : Hecke K q q⁻¹ m ≃ₐ[K] BalancedHecke (coxA m) q` — the presentation
  bridge.  `heckeActionN` is stated on `BalancedHecke (coxA m) q`, the trace theory on
  `QOU.SchurWeyl.Hecke`.  Built directly against `coxA` (generators to generators, both
  directions, by the two universal properties), so no `coxA = AMat` bridge is needed.
  `jimbo := heckeActionN ∘ skeinCoxAEquiv`.
* `jimboMarkov` — over **any field**, with `q ≠ 0`, `q² + 1 ≠ 0`: the weighted trace
  `x ↦ Tr(K^{⊗(n+1)} ρ(x)) / (1+q²)^{n+1}`, `K = diag(1, q²)`, is a Markov trace family
  with parameter `q³/(q²+1)` — convention D.  The Markov property is the partial-trace
  identity `partial_last`: `Σ_x K_x Ř_{(u,x),(v,x)} = q³ δ_{uv}`.
* `jimboTrace_eq_wtrace` — over any field (with `q` not a root of unity, `q² + 1 ≠ 0`)
  it IS the Ocneanu trace (`eq_wtrace_of_markov`).
* `ker_jimbo_eq_traceRadicalIdeal` — over any linearly ordered field:
  `ker(jimbo) = rad(wtrace)` as two-sided ideals.  The inclusion `rad ⊆ ker` is the only
  non-formal step: the image is closed under transpose (`Ř` is a symmetric matrix) and
  `X ↦ Tr(K^{⊗n} X Xᵀ)` is positive definite because `K` is positive diagonal.  No
  `q`-antisymmetriser computation and no ideal theory were needed.
* `jimbo_eq_zero_iff_twoRow_blocks_vanish` / `heckeActionN_eq_zero_iff_twoRow_blocks_vanish` —
  `x` acts by zero iff every seminormal block with at most two rows kills it: every
  block with `≥ 3` rows acts by zero and every two-row block acts faithfully.
* `finrank_range_jimbo` — `dim (image) = Σ_{λ ⊢ m+1, ℓ(λ) ≤ 2} (#SYT λ)²`
  (any linearly ordered field).
* `finrank_range_jimbo_eq_catalan` — `dim (image) = catalan (m+1)` (over `ℝ`, because
  `TraceQuotCatalan.finrank_traceQuot_eq_catalan` is stated over `ℝ`).

## Scope and what is NOT here

* The kernel, block and dimension statements need an ordered field: positivity of the
  weighted trace form is the whole argument for `rad ⊆ ker`.  Whether the kernel
  identification holds over an arbitrary field (e.g. `ℂ` with `q` generic) is not
  settled here; the transpose/positivity route does not reach it.
* Surjectivity onto the `U_q(sl₂)` commutant (Schur–Weyl proper) is not claimed: only the
  image's dimension and the kernel.

-- Ref: [jimbo1986]; [leitner2026] bean qou-k4oq
-/

namespace QOU.SchurWeyl.JimboActionKernel

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.MathlibExt.SkeinRelation
open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.IwahoriHecke.Balanced

variable {K : Type*} [Field K]

section Bridge

theorem hqi {q : K} (hq : q ≠ 0) : q * q⁻¹ = 1 := mul_inv_cancel₀ hq

/-- Skein generators → balanced generators. -/
noncomputable def toBal (q : K) (hq : q ≠ 0) (m : ℕ) : Hecke K q q⁻¹ m →ₐ[K] BalancedHecke (coxA m) q :=
  Hecke.lift K q q⁻¹ m (fun i => sigma (coxA m) q q⁻¹ i)
    (fun i => by
      have h := (isHeckeGenerator_sigma (M := coxA m) (hqi hq) i).eq
      rw [h, hqi hq, Algebra.smul_def, Algebra.smul_def, map_one, one_mul])
    (fun i hi => by
      have hne : i ≠ ⟨(i : ℕ) + 1, hi⟩ := by simp [Fin.ext_iff]
      have h := sigma_braid (R := K) (q := q) (qi := q⁻¹) (M := coxA m) coxA_symm i
        ⟨(i : ℕ) + 1, hi⟩
      rw [show coxA m i ⟨(i : ℕ) + 1, hi⟩ = 3 from by simp [coxA, hne],
        show coxA m ⟨(i : ℕ) + 1, hi⟩ i = 3 from by simp [coxA, Ne.symm hne],
        QOU.MathlibExt.IwahoriHecke.altProd_three,
        QOU.MathlibExt.IwahoriHecke.altProd_three] at h
      simpa only [mul_assoc] using h)
    (fun i j hij => by
      have hne : i ≠ j := by intro h; subst h; omega
      have h := sigma_braid (R := K) (q := q) (qi := q⁻¹) (M := coxA m) coxA_symm i j
      rw [show coxA m i j = 2 from by simp [coxA, hne]; omega,
        show coxA m j i = 2 from by simp [coxA, Ne.symm hne]; omega,
        QOU.MathlibExt.IwahoriHecke.altProd_two,
        QOU.MathlibExt.IwahoriHecke.altProd_two] at h
      exact h)

@[simp] theorem toBal_σ (q : K) (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    toBal q hq m (Hecke.σ K q q⁻¹ m i) = sigma (coxA m) q q⁻¹ i :=
  Hecke.lift_σ _ _ _ _ _ _ _ _ i


theorem isHeckeGenerator_σ {q : K} (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    IsHeckeGenerator q q⁻¹ (Hecke.σ K q q⁻¹ m i) := by
  show _ = _
  rw [Hecke.σ_quadratic, hqi hq, Algebra.smul_def, Algebra.smul_def, map_one, one_mul]

/-- Balanced generators → skein generators. -/
noncomputable def fromBal (q : K) (hq : q ≠ 0) (m : ℕ) :
    BalancedHecke (coxA m) q →ₐ[K] Hecke K q q⁻¹ m :=
  liftBalanced (hqi hq) (Hecke.σ K q q⁻¹ m) (isHeckeGenerator_σ hq m)
    (fun a b => by
      by_cases hab : a = b
      · subst hab; rfl
      · have hba : b ≠ a := Ne.symm hab
        by_cases hadj : (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ)
        · rw [show coxA m a b = 3 from by simp [coxA, hab, hadj],
            show coxA m b a = 3 from by simp [coxA, hba, hadj.symm],
            QOU.MathlibExt.IwahoriHecke.altProd_three,
            QOU.MathlibExt.IwahoriHecke.altProd_three]
          rcases hadj with h | h
          · have hi : (a : ℕ) + 1 < m := by omega
            have hb : (⟨(a : ℕ) + 1, hi⟩ : Fin m) = b := Fin.ext h
            have e := Hecke.σ_braid K q q⁻¹ m a hi
            rw [hb] at e
            rw [← mul_assoc, ← mul_assoc]; exact e
          · have hi : (b : ℕ) + 1 < m := by omega
            have ha : (⟨(b : ℕ) + 1, hi⟩ : Fin m) = a := Fin.ext h
            have e := Hecke.σ_braid K q q⁻¹ m b hi
            rw [ha] at e
            rw [← mul_assoc, ← mul_assoc]; exact e.symm
        · have hadj' : ¬((b : ℕ) + 1 = (a : ℕ) ∨ (a : ℕ) + 1 = (b : ℕ)) :=
            fun hc => hadj hc.symm
          rw [show coxA m a b = 2 from by simp [coxA, hab, hadj],
            show coxA m b a = 2 from by simp [coxA, hba, hadj'],
            QOU.MathlibExt.IwahoriHecke.altProd_two,
            QOU.MathlibExt.IwahoriHecke.altProd_two]
          have hne : (a : ℕ) ≠ (b : ℕ) := fun h => hab (Fin.ext h)
          rcases lt_or_gt_of_ne hne with h | h
          · exact (Hecke.σ_commute K q q⁻¹ m b a (by omega)).symm
          · exact Hecke.σ_commute K q q⁻¹ m a b (by omega))
    coxA_symm

@[simp] theorem fromBal_sigma (q : K) (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    fromBal q hq m (sigma (coxA m) q q⁻¹ i) = Hecke.σ K q q⁻¹ m i :=
  liftBalanced_sigma _ _ _ _ _ i

/-- **The skein Hecke algebra is the balanced algebra on `coxA`.** -/
noncomputable def skeinCoxAEquiv (q : K) (hq : q ≠ 0) (m : ℕ) :
    Hecke K q q⁻¹ m ≃ₐ[K] BalancedHecke (coxA m) q :=
  AlgEquiv.ofAlgHom (toBal q hq m) (fromBal q hq m)
    (hom_ext_sigma (hqi hq) _ _ fun i => by simp)
    (Hecke.hom_ext K q q⁻¹ m fun i => by simp)

@[simp] theorem skeinCoxAEquiv_σ (q : K) (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    skeinCoxAEquiv q hq m (Hecke.σ K q q⁻¹ m i) = sigma (coxA m) q q⁻¹ i := by
  simp [skeinCoxAEquiv]

/-- The Jimbo action on the skein algebra: `heckeActionN` read through the bridge. -/
noncomputable def jimbo (q : K) (hq : q ≠ 0) (m : ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) K :=
  (heckeActionN q q⁻¹ (hqi hq)).comp (skeinCoxAEquiv q hq m).toAlgHom

@[simp] theorem jimbo_σ (q : K) (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    jimbo q hq m (Hecke.σ K q q⁻¹ m i) = strandBraid q q⁻¹ i := by
  simp [jimbo]

theorem jimbo_apply (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo q hq m x = heckeActionN q q⁻¹ (hqi hq) (skeinCoxAEquiv q hq m x) := rfl

end Bridge

section Weights

/-- The site weight `K = diag(1, q²)`. -/
def wt (q : K) (x : Fin 2) : K := if x = 0 then 1 else q ^ 2

/-- The diagonal of `K^{⊗N}` on the monomial basis. -/
def dWeight (q : K) {N : ℕ} (a : Fin N → Fin 2) : K := ∏ s, wt q (a s)

/-- The weighted (quantum) trace `Tr(K^{⊗N} X)`. -/
def qtr (q : K) {N : ℕ} (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) : K :=
  ∑ a, dWeight q a * X a a

theorem qtr_add (q : K) {N : ℕ} (X Y : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) :
    qtr q (X + Y) = qtr q X + qtr q Y := by
  simp only [qtr, Matrix.add_apply, mul_add, Finset.sum_add_distrib]

theorem qtr_smul (q : K) {N : ℕ} (c : K) (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) :
    qtr q (c • X) = c * qtr q X := by
  simp only [qtr, Matrix.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun _ _ => by ring

theorem qtr_zero (q : K) {N : ℕ} : qtr q (0 : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) = 0 := by
  simp [qtr]

theorem dWeight_snoc (q : K) {N : ℕ} (a : Fin N → Fin 2) (x : Fin 2) :
    dWeight q (Fin.snoc (α := fun _ => Fin 2) a x) = dWeight q a * wt q x := by
  simp only [dWeight, Fin.prod_univ_castSucc, Fin.snoc_castSucc, Fin.snoc_last]

theorem sum_snoc {N : ℕ} (F : (Fin (N + 1) → Fin 2) → K) :
    ∑ a, F a = ∑ a : Fin N → Fin 2, ∑ x : Fin 2, F (Fin.snoc (α := fun _ => Fin 2) a x) := by
  rw [← (Fin.snocEquiv fun _ => Fin 2).sum_comp, Fintype.sum_prod_type, Finset.sum_comm]
  rfl

theorem sum_wt (q : K) : ∑ x : Fin 2, wt q x = 1 + q ^ 2 := by
  simp [wt, Fin.sum_univ_two]

theorem sum_dWeight (q : K) : ∀ N : ℕ, ∑ a : Fin N → Fin 2, dWeight q a = (1 + q ^ 2) ^ N
  | 0 => by simp [dWeight]
  | N + 1 => by
      rw [sum_snoc]
      simp only [dWeight_snoc, ← Finset.mul_sum, sum_wt, ← Finset.sum_mul, sum_dWeight q N,
        pow_succ]

theorem qtr_one (q : K) (N : ℕ) :
    qtr q (1 : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) = (1 + q ^ 2) ^ N := by
  simp [qtr, sum_dWeight]

end Weights

section Extension

variable {N : ℕ}

/-- `(Fin N → Fin 2) × Fin 2 ≃ (Fin (N+1) → Fin 2)`, the new site appended last. -/
def snocE (N : ℕ) : (Fin N → Fin 2) × Fin 2 ≃ (Fin (N + 1) → Fin 2) :=
  (Equiv.prodComm _ _).trans (Fin.snocEquiv fun _ => Fin 2)

/-- `X ↦ X ⊗ 1`, the new tensor factor appended last, as an algebra map. -/
noncomputable def extLast (N : ℕ) :
    Matrix (Fin N → Fin 2) (Fin N → Fin 2) K →ₐ[K]
      Matrix (Fin (N + 1) → Fin 2) (Fin (N + 1) → Fin 2) K :=
  (Matrix.reindexAlgEquiv K K (snocE N)).toAlgHom.comp
    (tensorIdHom (σ := Fin N → Fin 2) (ρ := Fin 2))

theorem extLast_apply (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K)
    (a b : Fin (N + 1) → Fin 2) :
    extLast N X a b = X (Fin.init a) (Fin.init b)
      * (if a (Fin.last N) = b (Fin.last N) then 1 else 0) := by
  simp [extLast, snocE, Matrix.reindexAlgEquiv_apply, tensorIdHom, Matrix.reindex_apply,
    Matrix.submatrix_apply, Equiv.prodComm]

theorem extLast_snoc (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K)
    (a b : Fin N → Fin 2) (x y : Fin 2) :
    extLast N X (Fin.snoc (α := fun _ => Fin 2) a x) (Fin.snoc (α := fun _ => Fin 2) b y)
      = X a b * (if x = y then 1 else 0) := by
  rw [extLast_apply, Fin.init_snoc, Fin.init_snoc, Fin.snoc_last, Fin.snoc_last]

theorem qtr_extLast (q : K) (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) :
    qtr q (extLast N X) = (1 + q ^ 2) * qtr q X := by
  rw [qtr, sum_snoc]
  simp only [extLast_snoc, if_true, mul_one, dWeight_snoc, qtr, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [← sum_wt q, Finset.sum_mul]
  exact Finset.sum_congr rfl fun x _ => by ring

/-- A two-site operator at sites `i, j < N` of `V^{⊗(N+1)}` is the extension of the same
operator on `V^{⊗N}`. -/
theorem embedPair_castSucc (i j : Fin N) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) K) :
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

/-- The partial `K`-trace of `Ř` over the appended last site is `q³` times the identity. -/
theorem partial_last (q qi : K) (hqi : q * qi = 1) {N : ℕ} (c a : Fin (N + 1) → Fin 2) :
    ∑ x : Fin 2, wt q x * embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheck q qi)
        (Fin.snoc (α := fun _ => Fin 2) c x) (Fin.snoc (α := fun _ => Fin 2) a x)
      = q ^ 3 * (if c = a then 1 else 0) := by
  have hcond : ∀ x : Fin 2,
      (∀ k : Fin (N + 2), k ≠ (Fin.last N).castSucc → k ≠ Fin.last (N + 1) →
          Fin.snoc (α := fun _ => Fin 2) c x k = Fin.snoc (α := fun _ => Fin 2) a x k)
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
    fin_cases u <;> fin_cases v <;> simp [wt, rCheck, Fin.sum_univ_two, Prod.ext_iff]
    all_goals
      · have hq0 : q ≠ 0 := left_ne_zero_of_mul_eq_one hqi
        have hqi' : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
        subst hqi'
        field_simp
        try ring
  · have hca : c ≠ a := fun h => hP fun k _ => by rw [h]
    simp [if_neg hP, hca]

theorem qtr_extLast_mul_last (q qi : K) (hqi : q * qi = 1) {N : ℕ}
    (X : Matrix (Fin (N + 1) → Fin 2) (Fin (N + 1) → Fin 2) K) :
    qtr q (extLast (N + 1) X
        * embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheck q qi))
      = q ^ 3 * qtr q X := by
  set B := embedPair (Fin.last N).castSucc (Fin.last (N + 1)) (rCheck q qi) with hB
  have h1 : ∀ (a : Fin (N + 1) → Fin 2) (x : Fin 2),
      (extLast (N + 1) X * B) (Fin.snoc (α := fun _ => Fin 2) a x)
          (Fin.snoc (α := fun _ => Fin 2) a x)
        = ∑ c, X a c * B (Fin.snoc (α := fun _ => Fin 2) c x)
            (Fin.snoc (α := fun _ => Fin 2) a x) := by
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
  have e : ∀ x : Fin 2, dWeight q a * wt q x * ∑ c, X a c
        * B (Fin.snoc (α := fun _ => Fin 2) c x) (Fin.snoc (α := fun _ => Fin 2) a x)
      = ∑ c, dWeight q a * X a c * (wt q x
        * B (Fin.snoc (α := fun _ => Fin 2) c x) (Fin.snoc (α := fun _ => Fin 2) a x)) := by
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
    (S : Subalgebra K (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) K))
    (h : ∀ i, strandBraid q q⁻¹ i ∈ S) (x : Hecke K q q⁻¹ m) : jimbo q hq m x ∈ S := by
  have hx : x ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ m)) := by
    rw [adjoin_range_σ_eq_top K q q⁻¹ m]; trivial
  have h2 : jimbo q hq m x
      ∈ (Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ m))).map (jimbo q hq m) :=
    Subalgebra.mem_map.mpr ⟨x, hx, rfl⟩
  rw [AlgHom.map_adjoin] at h2
  refine Algebra.adjoin_le ?_ h2
  rintro _ ⟨_, ⟨i, rfl⟩, rfl⟩
  simpa using h i

theorem rCheck_ne_zero {q qi : K} {u v : Fin 2 × Fin 2} (h : rCheck q qi u v ≠ 0) :
    u = v ∨ u = (v.2, v.1) := by
  by_contra hc
  push_neg at hc
  exact h (by simp [rCheck_apply, hc.1, hc.2])

theorem dWeight_eq_of_embedPair_ne_zero (q qi : K) {n : ℕ} {i j : Fin n} (hij : i ≠ j)
    {a b : Fin n → Fin 2} (h : embedPair i j (rCheck q qi) a b ≠ 0) :
    dWeight q a = dWeight q b := by
  classical
  rw [embedPair_apply] at h
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab] at h
    have hpair : wt q (a i) * wt q (a j) = wt q (b i) * wt q (b j) := by
      rcases rCheck_ne_zero h with e | e
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
def dMat (q : K) (N : ℕ) : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K :=
  Matrix.diagonal (dWeight q)

theorem dMat_commute_embedPair (q qi : K) {n : ℕ} {i j : Fin n} (hij : i ≠ j) :
    dMat q n * embedPair i j (rCheck q qi) = embedPair i j (rCheck q qi) * dMat q n := by
  ext a b
  rw [dMat, Matrix.diagonal_mul, Matrix.mul_diagonal]
  by_cases h : embedPair i j (rCheck q qi) a b = 0
  · rw [h, mul_zero, zero_mul]
  · rw [dWeight_eq_of_embedPair_ne_zero q qi hij h, mul_comm]

theorem dMat_commute_jimbo (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    dMat q (m + 1) * jimbo q hq m x = jimbo q hq m x * dMat q (m + 1) := by
  have := jimbo_mem q hq m (Subalgebra.centralizer K {dMat q (m + 1)})
    (fun i => by
      rw [Subalgebra.mem_centralizer_iff]
      rintro g rfl
      exact dMat_commute_embedPair q q⁻¹ (by simp [Fin.ext_iff])) x
  rw [Subalgebra.mem_centralizer_iff] at this
  exact this _ rfl

theorem qtr_eq_trace (q : K) {N : ℕ} (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K) :
    qtr q X = (dMat q N * X).trace := by
  simp [qtr, dMat, Matrix.trace, Matrix.diagonal_mul]

theorem qtr_jimbo_comm (q : K) (hq : q ≠ 0) (m : ℕ) (x y : Hecke K q q⁻¹ m) :
    qtr q (jimbo q hq m (x * y)) = qtr q (jimbo q hq m (y * x)) := by
  rw [map_mul, map_mul, qtr_eq_trace, qtr_eq_trace, ← mul_assoc,
    Matrix.trace_mul_comm, ← mul_assoc, ← dMat_commute_jimbo, mul_assoc]

theorem rCheck_transpose (q qi : K) : (rCheck q qi)ᵀ = rCheck q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;> simp [rCheck]

theorem embedPair_transpose {n : ℕ} (i j : Fin n) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) K) :
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
    ∃ y, jimbo q hq m y = (jimbo q hq m x)ᵀ := by
  have := jimbo_mem q hq m (transposeSub (jimbo q hq m).range)
    (fun i => by
      show (strandBraid q q⁻¹ i)ᵀ ∈ (jimbo q hq m).range
      rw [strandBraid, braidAt, embedPair_transpose, rCheck_transpose]
      exact ⟨Hecke.σ K q q⁻¹ m i, jimbo_σ q hq m i⟩) x
  exact this

end Image

section Trace

open QOU.SchurWeyl.HeckeInclusion

theorem jimbo_heckeIncl (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo q hq (m + 1) (heckeIncl K q q⁻¹ m x) = extLast (m + 1) (jimbo q hq m x) := by
  have h : (jimbo q hq (m + 1)).comp (heckeIncl K q q⁻¹ m)
      = (extLast (m + 1)).comp (jimbo q hq m) := by
    apply Hecke.hom_ext
    intro i
    simp only [AlgHom.comp_apply, heckeIncl_σ, jimbo_σ, strandBraid, braidAt]
    rw [Fin.succ_castSucc]
    exact embedPair_castSucc _ _ _
  exact AlgHom.congr_fun h x

theorem jimbo_last (q : K) (hq : q ≠ 0) (m : ℕ) :
    jimbo q hq (m + 1) (Hecke.σ K q q⁻¹ (m + 1) (Fin.last m))
      = embedPair (Fin.last m).castSucc (Fin.last (m + 1)) (rCheck q q⁻¹) := by
  rw [jimbo_σ, strandBraid, braidAt, Fin.succ_last]

/-- `qtr` as a linear functional. -/
def qtrLin (q : K) (N : ℕ) : Matrix (Fin N → Fin 2) (Fin N → Fin 2) K →ₗ[K] K where
  toFun := qtr q
  map_add' := qtr_add q
  map_smul' c X := qtr_smul q c X

/-- **The normalised weighted trace of the Jimbo action**
`x ↦ Tr(K^{⊗(n+1)} ρ(x)) / (1 + q²)^{n+1}`, `K = diag(1, q²)`. -/
noncomputable def jimboTrace (q : K) (hq : q ≠ 0) (n : ℕ) : Hecke K q q⁻¹ n →ₗ[K] K :=
  ((1 + q ^ 2) ^ (n + 1))⁻¹ • ((qtrLin q (n + 1)).comp (jimbo q hq n).toLinearMap)

theorem jimboTrace_apply (q : K) (hq : q ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    jimboTrace q hq n x = ((1 + q ^ 2) ^ (n + 1))⁻¹ * qtr q (jimbo q hq n x) := rfl

/-- **The weighted trace of the Jimbo action is a Markov trace at convention D**,
`z = q³/(q² + 1)`. -/
noncomputable def jimboMarkov (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) :
    HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)) where
  tr := jimboTrace q hq
  tr_one n := by
    have h : (1 + q ^ 2) ≠ 0 := by rwa [add_comm]
    rw [jimboTrace_apply, map_one, qtr_one]
    exact inv_mul_cancel₀ (pow_ne_zero _ h)
  tr_cyclic n x y := by rw [jimboTrace_apply, jimboTrace_apply, qtr_jimbo_comm]
  tr_incl n x := by
    have h : (1 + q ^ 2) ≠ 0 := by rwa [add_comm]
    rw [jimboTrace_apply, jimboTrace_apply, jimbo_heckeIncl, qtr_extLast]
    field_simp
    ring
  tr_markov n x := by
    have h : (1 + q ^ 2) ≠ 0 := by rwa [add_comm]
    rw [jimboTrace_apply, jimboTrace_apply, map_mul, jimbo_heckeIncl, jimbo_last,
      qtr_extLast_mul_last q q⁻¹ (hqi hq)]
    field_simp
    ring

/-- **The Jimbo trace is the Ocneanu weighted seminormal trace**, by uniqueness of the
convention-D Markov trace.  Any field. -/
theorem jimboTrace_eq_wtrace (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1)
    (n : ℕ) (x : Hecke K q q⁻¹ n) :
    jimboTrace q hq n x = SeminormalRep.wtrace q hq hq2 n x :=
  SeminormalRep.eq_wtrace_of_markov q hq hq2 hq21 hgen (jimboMarkov q hq hq21) n x

end Trace

/-! From here on the base field carries a linear order: the one non-formal step is that
`X ↦ Tr(K^{⊗N} X Xᵀ)` is positive definite, which needs `K` positive. -/

section Kernel

open scoped Matrix
open QOU.QBeta.MarkovTraceQuotient

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]

theorem dWeight_pos (q : L) (hq : q ≠ 0) {N : ℕ} (a : Fin N → Fin 2) : 0 < dWeight q a :=
  Finset.prod_pos fun s _ => by
    unfold wt
    split_ifs
    · exact one_pos
    · positivity

/-- **The weighted trace form is positive definite on `X ↦ X Xᵀ`.** -/
theorem eq_zero_of_qtr_mul_transpose (q : L) (hq : q ≠ 0) {N : ℕ}
    (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) L) (h : qtr q (X * Xᵀ) = 0) : X = 0 := by
  have hdiag : ∀ a, (X * Xᵀ) a a = ∑ c, X a c * X a c := fun a => by
    simp [Matrix.mul_apply, Matrix.transpose_apply]
  have hnn : ∀ a ∈ (Finset.univ : Finset (Fin N → Fin 2)), 0 ≤ dWeight q a * (X * Xᵀ) a a :=
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
    jimbo q hq m x = 0 ↔ ∀ y, qtr q (jimbo q hq m (x * y)) = 0 := by
  constructor
  · intro h y; rw [map_mul, h, zero_mul, qtr_zero]
  · intro h
    obtain ⟨y, hy⟩ := transpose_jimbo_mem_range q hq m x
    apply eq_zero_of_qtr_mul_transpose q hq
    rw [← hy, ← map_mul]
    exact h y

/-- **Kernel of the Jimbo action = radical of the Ocneanu trace form** (pointwise). -/
theorem jimbo_eq_zero_iff_wtrace (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1) (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo q hq m x = 0 ↔ ∀ y, SeminormalRep.wtrace q hq hq2 m (x * y) = 0 := by
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  have hc : ((1 + q ^ 2) ^ (m + 1))⁻¹ ≠ 0 := by positivity
  rw [jimbo_eq_zero_iff_qtr]
  refine forall_congr' fun y => ?_
  rw [← jimboTrace_eq_wtrace q hq hq2 hq21 hgen, jimboTrace_apply, mul_eq_zero,
    or_iff_right hc]

/-- **The kernel of the Jimbo action is the trace-radical ideal of `wtrace`**, as
two-sided ideals. -/
theorem ker_jimbo_eq_traceRadicalIdeal (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) :
    TwoSidedIdeal.ker (jimbo q hq m)
      = traceRadicalIdeal (SeminormalRep.wtrace q hq hq2 m)
          (SeminormalRep.wtrace_cyclic q hq hq2 m) := by
  ext x
  rw [TwoSidedIdeal.mem_ker, mem_traceRadicalIdeal, jimbo_eq_zero_iff_wtrace q hq hq2 hgen]
  rfl

/-- **The same statement for `heckeActionN` itself**, read through the presentation
equivalence `skeinCoxAEquiv : Hecke L q q⁻¹ m ≃ₐ BalancedHecke (coxA m) q`. -/
theorem heckeActionN_eq_zero_iff_wtrace (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (b : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    heckeActionN q q⁻¹ (hqi hq) b = 0
      ↔ ∀ y, SeminormalRep.wtrace q hq hq2 m ((skeinCoxAEquiv q hq m).symm b * y) = 0 := by
  rw [← jimbo_eq_zero_iff_wtrace q hq hq2 hgen, jimbo_apply, AlgEquiv.apply_symm_apply]

end Kernel

section Blocks

open YoungDiagram QOU.Mathlib SeminormalRep

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]

/-- **Every block with three or more rows acts by zero.** An element killed by every
at-most-two-row seminormal block is killed by the Jimbo action. -/
theorem jimbo_eq_zero_of_twoRow_blocks_vanish (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (x : Hecke L q q⁻¹ m)
    (hx : ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq hq2 m hd x = 0) :
    jimbo q hq m x = 0 := by
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [jimbo_eq_zero_iff_wtrace q hq hq2 hgen]
  intro y
  rw [wtrace_apply]
  refine Finset.sum_eq_zero fun ν _ => ?_
  by_cases h : ν.1.rowLen 2 = 0
  · rw [map_mul, hx ν.1 ν.2 h, zero_mul, Matrix.trace_zero, mul_zero]
  · rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 ν.1 (Nat.pos_of_ne_zero h),
      zero_mul]

/-- **Every at-most-two-row block survives.** If the Jimbo action kills `x`, so does every
seminormal block with at most two rows. -/
theorem twoRow_block_eq_zero_of_jimbo_eq_zero (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (x : Hecke L q q⁻¹ m) (hx : jimbo q hq m x = 0)
    (d : YoungDiagram) (hd : d.cells.card = m + 1) (hrow : d.rowLen 2 = 0) :
    seminormalRep q hq hq2 m hd x = 0 := by
  classical
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  by_contra hne
  have hrad := (jimbo_eq_zero_iff_wtrace q hq hq2 hgen m x).mp hx
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq d hd
  subst hlam₀
  obtain ⟨N, hN⟩ := WtraceRadicalTwoRow.exists_trace_mul_ne_zero hne
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq hq2 m (Function.update 0 lam₀ N)
  apply hN.elim
  have h0 := hrad b
  rw [wtrace_apply] at h0
  rw [← Equiv.sum_comp (partitionShapeEquiv (m + 1))
    (fun ν : {ν : YoungDiagram // ν.cells.card = m + 1} =>
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1
        * (seminormalRep q hq hq2 m ν.2 (x * b)).trace)] at h0
  have hρ : ∀ (lam : Nat.Partition (m + 1)) (y : Hecke L q q⁻¹ m),
      seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam).2 y
        = heckeProduct q hq hq2 m y lam := fun _ _ => rfl
  rw [Finset.sum_eq_single_of_mem lam₀ (Finset.mem_univ lam₀)] at h0
  · have hbN : heckeProduct q hq hq2 m b lam₀ = N := by rw [hb]; simp
    have htr : (seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam₀).2 (x * b)).trace
        = (seminormalRep q hq hq2 m hd x * N).trace := by
      rw [map_mul, hρ lam₀ b, hbN]
      rfl
    rw [htr] at h0
    exact (mul_eq_zero.mp h0).resolve_left
      (ocneanuWeight_conventionD_ne_zero_of_two_rows q hq hq21 hgen _ hrow)
  · intro lam _ hlam
    have hbz : heckeProduct q hq hq2 m b lam = 0 := by rw [hb]; simp [hlam]
    have hz : seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) lam).2 (x * b) = 0 := by
      rw [map_mul, hρ lam b, hbz, mul_zero]
    rw [hz, Matrix.trace_zero, mul_zero]

/-- **Kohno comparison at `sl₂`, kernel form.** The Jimbo action kills `x` exactly when every
seminormal block with at most two rows does: the kernel is the sum of the blocks with three
or more rows. -/
theorem jimbo_eq_zero_iff_twoRow_blocks_vanish (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo q hq m x = 0 ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq hq2 m hd x = 0 :=
  ⟨fun h d hd hrow => twoRow_block_eq_zero_of_jimbo_eq_zero q hq hq2 hgen m x h d hd hrow,
    jimbo_eq_zero_of_twoRow_blocks_vanish q hq hq2 hgen m x⟩

/-- The same, for `heckeActionN` itself. -/
theorem heckeActionN_eq_zero_iff_twoRow_blocks_vanish (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (b : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    heckeActionN q q⁻¹ (hqi hq) b = 0 ↔
      ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
        seminormalRep q hq hq2 m hd ((skeinCoxAEquiv q hq m).symm b) = 0 := by
  rw [← jimbo_eq_zero_iff_twoRow_blocks_vanish q hq hq2 hgen, jimbo_apply,
    AlgEquiv.apply_symm_apply]

end Blocks

section Dimension

open YoungDiagram QOU.Mathlib SeminormalRep
open QOU.SchurWeyl.WtraceRadicalIdeal (TwoRowIdx)

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]

/-- The projection onto the at-most-two-row seminormal blocks (any ordered field;
`WtraceRadicalIdeal.twoRowProduct` is the `ℝ` instance of the same map). -/
noncomputable def twoRowProd (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) :
    Hecke L q q⁻¹ m →ₐ[L] (∀ lam : TwoRowIdx m,
      Matrix (StandardYoungTableau (partitionShape lam.1))
        (StandardYoungTableau (partitionShape lam.1)) L) :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq hq2 m (partitionShape_card_succ lam.1))

theorem twoRowProd_surjective (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Surjective (twoRowProd q hq hq2 m) := by
  classical
  intro f
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq hq2 m
    (fun lam => if h : (partitionShape lam).rowLen 2 = 0 then f ⟨lam, h⟩ else 0)
  refine ⟨b, ?_⟩
  funext lam
  have h1 : twoRowProd q hq hq2 m b lam = heckeProduct q hq hq2 m b lam.1 := rfl
  rw [h1, hb]
  simp only [dif_pos lam.2]

theorem jimbo_eq_zero_iff_twoRowProd (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) (x : Hecke L q q⁻¹ m) :
    jimbo q hq m x = 0 ↔ twoRowProd q hq hq2 m x = 0 := by
  rw [jimbo_eq_zero_iff_twoRow_blocks_vanish q hq hq2 hgen]
  constructor
  · intro h
    funext lam
    exact h _ (partitionShape_card_succ lam.1) lam.2
  · intro h d hd hrow
    obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq d hd
    subst hlam₀
    exact congrFun h ⟨lam₀, hrow⟩

/-- **Dimension of the image of the Jimbo action** = `∑_{ℓ(λ) ≤ 2} (#SYT λ)²`. -/
theorem finrank_range_jimbo (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : L) ^ i ≠ 1)
    (m : ℕ) :
    Module.finrank L (LinearMap.range (jimbo q hq m).toLinearMap)
      = ∑ lam : TwoRowIdx m,
          Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2 := by
  haveI := finiteDimensional_hecke q q⁻¹ m
  have hker : LinearMap.ker (jimbo q hq m).toLinearMap
      = LinearMap.ker (twoRowProd q hq hq2 m).toLinearMap := by
    ext x
    simp only [LinearMap.mem_ker, AlgHom.toLinearMap_apply]
    exact jimbo_eq_zero_iff_twoRowProd q hq hq2 hgen m x
  have h1 := LinearMap.finrank_range_add_finrank_ker (jimbo q hq m).toLinearMap
  have h2 := LinearMap.finrank_range_add_finrank_ker (twoRowProd q hq hq2 m).toLinearMap
  have hr : LinearMap.range (twoRowProd q hq hq2 m).toLinearMap = ⊤ :=
    LinearMap.range_eq_top.mpr (twoRowProd_surjective q hq hq2 m)
  rw [hr, finrank_top, Module.finrank_pi_fintype] at h2
  rw [hker] at h1
  have h3 : Module.finrank L (LinearMap.range (jimbo q hq m).toLinearMap)
      = ∑ lam : TwoRowIdx m, Module.finrank L (Matrix (StandardYoungTableau (partitionShape lam.1))
          (StandardYoungTableau (partitionShape lam.1)) L) := by omega
  rw [h3]
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [Module.finrank_matrix, Module.finrank_self, mul_one, sq]

/-- **The image of the Jimbo action has dimension `catalan (m+1)`.**  The block count of
`finrank_range_jimbo` is the one `TraceQuotCatalan.finrank_traceQuot_eq_catalan` evaluates
(via `twoRowIdxEquiv`, `numSYT_twoRow_eq_ballot`, `dimHLF_two_row_sq_sum`).  Over `ℝ`
because that evaluation is stated over `ℝ`. -/
theorem finrank_range_jimbo_eq_catalan (q : ℝ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (m : ℕ) :
    Module.finrank ℝ (LinearMap.range (jimbo q hq m).toLinearMap) = catalan (m + 1) := by
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  have h := QOU.SchurWeyl.TraceQuotCatalan.finrank_traceQuot_eq_catalan hq hq2 hq21 hgen m
  rw [QOU.SchurWeyl.WtraceRadicalSemisimple.finrank_traceQuot hq hq2 hq21 hgen m] at h
  rw [finrank_range_jimbo q hq hq2 hgen m]
  simp_rw [sq]
  exact_mod_cast h

end Dimension

end QOU.SchurWeyl.JimboActionKernel
