import QOU.BraidKnot.HeckeReebHolonomyLaplacian
import QOU.SchurWeyl.SeminormalContentCasimir

/-!
# Bridge between the two Hecke presentations, and the Reeb-holonomy Laplacian

The corpus carries two presentations of the type-`A` Iwahori–Hecke algebra:

* `QOU.BraidKnot.Hecke.HeckeGeneratorsBelow R A q n`: a *class* of generator families `σ₀ … σ_{n-2}`
  in some algebra `A`, satisfying the Hecke, braid and far-commutation relations of `H_n(q)`;
* `QOU.SchurWeyl.Hecke K q qi m`: the algebra itself, the `RingQuot` of a free algebra on `m`
  generators, i.e. `H_{m+1}(q)`, with a universal property (`Hecke.lift`, `Hecke.hom_ext`).

The Reeb-holonomy Laplacian `reebLaplacianB` lives on the first; the content Casimir
`contentCasimir`, its centrality and its eigenvalue on every seminormal block live on the second.
This file connects them.

## What is proved

* `toHeckeHom H` — every bounded family `H : HeckeGeneratorsBelow K A q (m + 1)` is the image of
  the universal one: an algebra map `Hecke K q q⁻¹ m →ₐ[K] A` with `σ i ↦ H.σ i`.
* `toHeckeHom_qJM`, `toHeckeHom_qJMInv` — it sends the Murphy elements `L_k` and their inverses to
  `jmRawB H k` and `jmRawInvB H k` (`k ≤ m`).
* `toHeckeHom_contentCasimir` — it sends the content Casimir to the Reeb-holonomy Laplacian on all
  `m + 1` strands: `reebLaplacianB H (m + 1)` **is** the image of `C_m`.
* `reebLaplacianB_comm_σ` — hence the Laplacian commutes with every generator, in **any** algebra
  carrying the bounded presentation.  `HeckeReebHolonomyLaplacian.lean` listed this as not proved.
* `heckeBelow` — the universal algebra carries the bounded presentation, and
  `reebLaplacianB_heckeBelow` identifies its Laplacian with `contentCasimir` on the nose.
* `seminormalRep_reebLaplacianB`, `heckeWedderburn_reebLaplacianB` — so the Laplacian acts on
  every seminormal block of `H_{m+1}(q)`, and on every Wedderburn factor, by the scalar
  `Σ_{c ∈ λ} (q − q⁻¹)² [c][c+1]`, for `q` not a root of unity.  No weight vector is assumed;
  this removes the hypothesis `IsJMWeightB` that `reebLaplacianB_smul_of_weight` carries.

Everything is algebraic: over any field `K` (and `CharZero K` only for the Wedderburn form, which
needs it for the Wedderburn isomorphism itself).

## What is NOT proved here

The geometric reading — that the full twist `Δ²_k` is the holonomy of the Reeb rotation loop of the
cluster of the first `k + 1` points — is untouched.  That is Bridge A.

Refs: [ram1997] Theorem 4.1; [kassel1995] Ch. XII.
-/

namespace QOU.BraidKnot.Hecke

open QOU.SchurWeyl

section Bridge

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {q : K} {m : ℕ}

/-- The generator images of a bounded family, indexed by `Fin m`. -/
def heckeGens (H : HeckeGeneratorsBelow K A q (m + 1)) (i : Fin m) : A := H.σ i

/-- **The bounded family is the image of the universal one.**  The algebra map
`H_{m+1}(q) →ₐ[K] A` sending `σ_i` to `H.σ i`. -/
noncomputable def toHeckeHom (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) :
    QOU.SchurWeyl.Hecke K q q⁻¹ m →ₐ[K] A :=
  QOU.SchurWeyl.Hecke.lift K q q⁻¹ m (heckeGens H)
    (fun i => by
      have h := H.hecke i (by omega)
      rw [mul_inv_cancel₀ hq, one_smul, ← Algebra.smul_def] at *
      exact h)
    (fun i hi => H.braid i (by omega))
    (fun i j hij => (H.far j i (by omega) (by omega)).symm)

theorem toHeckeHom_σ (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) (i : Fin m) :
    toHeckeHom H hq (QOU.SchurWeyl.Hecke.σ K q q⁻¹ m i) = H.σ i :=
  QOU.SchurWeyl.Hecke.lift_σ K q q⁻¹ m _ _ _ _ i

/-- The image of the inverse generator is `σInvB`. -/
theorem toHeckeHom_σInv (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) (i : Fin m) :
    toHeckeHom H hq (QOU.SchurWeyl.Hecke.σInv K q q⁻¹ m i) = σInvB H i := by
  rw [QOU.SchurWeyl.Hecke.σInv, map_sub, map_smul, map_one, toHeckeHom_σ, σInvB,
    Algebra.algebraMap_eq_smul_one]

/-- **Murphy elements correspond.** -/
theorem toHeckeHom_qJM (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) :
    ∀ k, k ≤ m → toHeckeHom H hq (qJM K q q⁻¹ m k) = jmRawB H k
  | 0, _ => by simp
  | k + 1, hk => by
    rw [qJM_succ K q q⁻¹ m (by omega), map_mul, map_mul, toHeckeHom_σ,
      toHeckeHom_qJM H hq k (by omega), jmRawB_succ]

/-- **Inverse Murphy elements correspond.** -/
theorem toHeckeHom_qJMInv (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) :
    ∀ k, k ≤ m → toHeckeHom H hq (qJMInv K q q⁻¹ m k) = jmRawInvB H k
  | 0, _ => by simp [jmRawInvB]
  | k + 1, hk => by
    rw [qJMInv_succ K q q⁻¹ m (by omega), map_mul, map_mul, toHeckeHom_σInv,
      toHeckeHom_qJMInv H hq k (by omega)]
    rfl

/-- **The content Casimir maps to the Reeb-holonomy Laplacian.** -/
theorem toHeckeHom_contentCasimir (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0) :
    toHeckeHom H hq (contentCasimir K q q⁻¹ m) = reebLaplacianB H (m + 1) := by
  have hL : ∀ k ∈ Finset.range (m + 1), toHeckeHom H hq (qJM K q q⁻¹ m k) = jmRawB H k :=
    fun k hk => toHeckeHom_qJM H hq k (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))
  have hLi : ∀ k ∈ Finset.range (m + 1),
      toHeckeHom H hq (qJMInv K q q⁻¹ m k) = jmRawInvB H k :=
    fun k hk => toHeckeHom_qJMInv H hq k (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))
  rw [contentCasimir, map_sub, map_add, map_smul, map_smul, map_sum, map_sum,
    Finset.sum_congr rfl hL, Finset.sum_congr rfl hLi, AlgHom.commutes, reebLaplacianB,
    Finset.sum_sub_distrib, Finset.sum_add_distrib, Finset.smul_sum, Finset.smul_sum,
    Finset.sum_const, Finset.card_range, map_mul, map_natCast, ← nsmul_eq_mul]

/-- **Centrality on the bounded presentation.**  In any algebra carrying `H_{m+1}(q)`'s relations,
the Reeb-holonomy Laplacian on all strands commutes with every generator. -/
theorem reebLaplacianB_comm_σ (H : HeckeGeneratorsBelow K A q (m + 1)) (hq : q ≠ 0)
    (i : ℕ) (hi : i < m) :
    H.σ i * reebLaplacianB H (m + 1) = reebLaplacianB H (m + 1) * H.σ i := by
  have hc := congrArg (toHeckeHom H hq)
    (contentCasimir_comm_σ K q q⁻¹ m (mul_inv_cancel₀ hq) ⟨i, hi⟩)
  rwa [map_mul, map_mul, toHeckeHom_σ, toHeckeHom_contentCasimir] at hc

end Bridge

section Universal

variable {K : Type*} [Field K] (q : K) (m : ℕ)

/-- The universal generator family, extended by `0` past the last generator. -/
noncomputable def heckeBelowσ (i : ℕ) : QOU.SchurWeyl.Hecke K q q⁻¹ m :=
  if h : i < m then QOU.SchurWeyl.Hecke.σ K q q⁻¹ m ⟨i, h⟩ else 0

theorem heckeBelowσ_of_lt {i : ℕ} (h : i < m) :
    heckeBelowσ q m i = QOU.SchurWeyl.Hecke.σ K q q⁻¹ m ⟨i, h⟩ := dif_pos h

/-- **The universal algebra carries the bounded presentation.** -/
noncomputable def heckeBelow (hq : q ≠ 0) :
    HeckeGeneratorsBelow K (QOU.SchurWeyl.Hecke K q q⁻¹ m) q (m + 1) where
  σ := heckeBelowσ q m
  hecke i hi := by
    rw [heckeBelowσ_of_lt q m (by omega : i < m), ← Algebra.smul_def]
    exact QOU.SchurWeyl.Hecke.σ_quadratic_qou K q q⁻¹ m (mul_inv_cancel₀ hq) _
  braid i hi := by
    rw [heckeBelowσ_of_lt q m (by omega : i < m), heckeBelowσ_of_lt q m (by omega : i + 1 < m)]
    exact QOU.SchurWeyl.Hecke.σ_braid K q q⁻¹ m ⟨i, by omega⟩ (by simp; omega)
  far i j hij hj := by
    rw [heckeBelowσ_of_lt q m (by omega : i < m), heckeBelowσ_of_lt q m (by omega : j < m)]
    exact (QOU.SchurWeyl.Hecke.σ_commute K q q⁻¹ m ⟨j, by omega⟩ ⟨i, by omega⟩
      (by simp; omega)).symm

/-- On the universal family the bridge map is the identity. -/
theorem toHeckeHom_heckeBelow (hq : q ≠ 0) :
    toHeckeHom (heckeBelow q m hq) hq = AlgHom.id K _ := by
  apply QOU.SchurWeyl.Hecke.hom_ext
  intro i
  rw [toHeckeHom_σ, AlgHom.id_apply]
  exact heckeBelowσ_of_lt q m i.isLt

/-- **The two operators are the same element.**  On the universal algebra, the Reeb-holonomy
Laplacian on all `m + 1` strands equals the content Casimir. -/
theorem reebLaplacianB_heckeBelow (hq : q ≠ 0) :
    reebLaplacianB (heckeBelow q m hq) (m + 1) = contentCasimir K q q⁻¹ m := by
  rw [← toHeckeHom_contentCasimir (heckeBelow q m hq) hq, toHeckeHom_heckeBelow,
    AlgHom.id_apply]

end Universal

section Spectrum

open QOU.Mathlib (StandardYoungTableau)
open QOU.SchurWeyl.TableauCells QOU.SchurWeyl.SeminormalRep
open scoped Classical

/-- **Eigenvalue on every seminormal block, unconditionally.**  For `q` not a root of unity, the
Reeb-holonomy Laplacian of `H_{m+1}(q)` acts on the seminormal representation of shape `μ` by the
scalar `Σ_{c ∈ μ} (q − q⁻¹)² [c][c+1]`. -/
theorem seminormalRep_reebLaplacianB {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (m : ℕ) {μ : YoungDiagram}
    (hN : μ.cells.card = m + 1) :
    seminormalRep q hq0 hq2 m hN (reebLaplacianB (heckeBelow q m hq0) (m + 1))
      = (∑ c ∈ μ.cells, cellCasimirVal q c)
          • (1 : Matrix (_root_.QOU.Mathlib.StandardYoungTableau μ)
            (_root_.QOU.Mathlib.StandardYoungTableau μ) K) := by
  rw [reebLaplacianB_heckeBelow]
  exact seminormalRep_contentCasimir q hq0 hq2 m hN

/-- **Eigenvalue on every Wedderburn factor.**  Under `H_{m+1}(q) ≃ ∏_{λ ⊢ m+1} M_{d_λ}(K)`, the
Reeb-holonomy Laplacian is the tuple of block scalars `Σ_{c ∈ λ} (q − q⁻¹)² [c][c+1]`. -/
theorem heckeWedderburn_reebLaplacianB {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
    (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (m : ℕ) (lam : Partition (m + 1)) :
    heckeWedderburn q hq0 hq2 m (reebLaplacianB (heckeBelow q m hq0) (m + 1)) lam
      = (∑ c ∈ (QOU.Mathlib.partitionShape lam).cells, cellCasimirVal q c) • 1 := by
  rw [reebLaplacianB_heckeBelow]
  exact heckeWedderburn_contentCasimir q hq0 hq2 m lam

end Spectrum

end QOU.BraidKnot.Hecke
