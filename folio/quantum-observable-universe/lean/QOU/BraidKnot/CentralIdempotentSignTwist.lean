import QOU.BraidKnot.CentralIdempotentInvolution

/-!
# The sign twist `#` pairs `e_λ` with `e_λ'` (owner ruling option C, bean `qou-2150`)

Second half of option C (the first, bar fixes every `e_λ`, is in
`QOU.BraidKnot.CentralIdempotentInvolution`).

* `sytTranspose` — the transpose of a standard Young tableau; its content vector is the negation
  (`contentVec_sytTranspose`). `conjPart` is the conjugate partition `λ'`, `tr` the transposed
  tableau as one of shape `λ'`, and `tr_bijective` shows `T ↦ T'` is a bijection
  `SYT(λ) ≃ SYT(λ')`.
* `hashMap` — the `K`-algebra endomorphism `σ_i ↦ −σ_i⁻¹`, constructed from the universal property
  (`σInv_braid` supplies the braid relation for the inverses).
* `IsHash.map_proj` — `#(π_T) = π_{T'}`; `IsHash.map_centralIdem` / `hashMap_centralIdem` —
  **`#(e_λ) = e_λ'` for every `λ`**: cross-check 4 holds for `#`, and cross-check 3 for `#` is the
  special case `λ = λ'`.

Route: `#` is linear and sends `L_k ↦ L_k⁻¹`, so `#(π_T)` is the Lagrange product in `L_k⁻¹` with
targets `q^{2d}`. On a seminormal vector `S` that product is `1` exactly when the content vector
of `S` is the negation of `T`'s, i.e. `S = T'`, and `0` otherwise.

Scope: generic `q` (`q ≠ 0`, not a root of unity), any characteristic. `#` is not a symmetry of
the convention-D mass trace (it relates the trace at `q` to the trace at `−1/q`; see the probe
`computations/probes/central_idempotent_involution_probe.py`).
-/

namespace QOU.BraidKnot.CentralIdempotentInvolution

open QOU.SchurWeyl QOU.SchurWeyl.JMProjector QOU.SchurWeyl.TableauCells

theorem card_cells_transpose (μ : YoungDiagram) : μ.transpose.cells.card = μ.cells.card := by
  rw [YoungDiagram.transpose, YoungDiagram.cells]
  simp

/-- The transpose of a standard Young tableau: `T'(i, j) = T(j, i)`. -/
def sytTranspose {μ : YoungDiagram} (T : QOU.Mathlib.StandardYoungTableau μ) :
    QOU.Mathlib.StandardYoungTableau μ.transpose where
  toSsyt :=
    { entry := fun i j => T.entry j i
      row_weak' := fun {i j1 j2} hlt hcell => by
        rw [YoungDiagram.mem_transpose] at hcell
        exact le_of_lt (T.toSsyt.col_strict hlt hcell)
      col_strict' := fun {i1 i2 j} hlt hcell => by
        rw [YoungDiagram.mem_transpose] at hcell
        exact T.row_strict hlt hcell
      zeros' := fun {i j} hnot => by
        rw [YoungDiagram.mem_transpose] at hnot
        exact T.toSsyt.zeros hnot }
  bijOn := by
    rw [card_cells_transpose]
    have hT := T.bijOn
    refine ⟨fun c hc => ?_, fun a ha b hb hab => ?_, fun k hk => ?_⟩
    · have : (c.2, c.1) ∈ (μ.cells : Set (ℕ × ℕ)) := by
        simpa [YoungDiagram.mem_transpose] using hc
      exact hT.mapsTo this
    · have ha' : (a.2, a.1) ∈ (μ.cells : Set (ℕ × ℕ)) := by
        simpa [YoungDiagram.mem_transpose] using ha
      have hb' : (b.2, b.1) ∈ (μ.cells : Set (ℕ × ℕ)) := by
        simpa [YoungDiagram.mem_transpose] using hb
      have := hT.injOn ha' hb' hab
      simp only [Prod.mk.injEq] at this
      exact Prod.ext this.2 this.1
    · obtain ⟨c, hc, hck⟩ := hT.surjOn hk
      refine ⟨(c.2, c.1), by simpa [YoungDiagram.mem_transpose] using hc, hck⟩

theorem entry_sytTranspose {μ : YoungDiagram} (T : QOU.Mathlib.StandardYoungTableau μ) (i j : ℕ) :
    (sytTranspose T).entry i j = T.entry j i := rfl

theorem cellOf_sytTranspose {μ : YoungDiagram} (T : QOU.Mathlib.StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) :
    cellOf (sytTranspose T) k = ((cellOf T k).2, (cellOf T k).1) := by
  apply cellOf_unique
  · have := cellOf_mem T hk
    simpa [YoungDiagram.mem_transpose] using this
  · rw [entry_sytTranspose]
    exact entry_cellOf T hk

theorem contentVec_sytTranspose {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    (T : QOU.Mathlib.StandardYoungTableau μ) {k : ℕ} (hk : k ∈ Finset.range (n + 1)) :
    contentVec (sytTranspose T) k = -contentVec T k := by
  rw [Finset.mem_range] at hk
  simp only [contentVec]
  rw [cellOf_sytTranspose T (by rw [Set.mem_Icc, hN]; omega)]
  simp only [cellContent]
  ring

theorem contentVec_cast {μ ν : YoungDiagram} (h : μ = ν) (X : QOU.Mathlib.StandardYoungTableau μ)
    (k : ℕ) : contentVec (h ▸ X) k = contentVec X k := by
  subst h; rfl

theorem mem_contentRange_neg {n : ℕ} {d : ℤ} (h : d ∈ contentRange n) : -d ∈ contentRange n := by
  rw [mem_contentRange] at h ⊢; omega

theorem lagrVal_one {K : Type*} [Field K] (n : ℕ) (f g : ℤ → K)
    (hinj : Set.InjOn g {d | d ∈ contentRange n}) (c e : ℕ → ℤ)
    (hc : ∀ k ∈ Finset.range (n + 1), c k ∈ contentRange n)
    (hfe : ∀ k ∈ Finset.range (n + 1), f (e k) = g (c k)) :
    lagrVal n f g c e = 1 := by
  unfold lagrVal
  refine List.prod_eq_one (fun x hx => ?_)
  obtain ⟨k, hk, rfl⟩ := List.mem_map.mp hx
  have hk' : k ∈ Finset.range (n + 1) := by simpa [Finset.mem_range, List.mem_range] using hk
  refine List.prod_eq_one (fun y hy => ?_)
  obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hy
  rw [List.mem_filter] at hd
  have hdc : d ≠ c k := by simpa using hd.2
  have hne : g (c k) - g d ≠ 0 :=
    sub_ne_zero.mpr (fun h => hdc (hinj (hc k hk') hd.1 h).symm)
  rw [hfe k hk']
  exact inv_mul_cancel₀ hne

/-! ## The sign twist `#` pairs `e_λ` with `e_λ'` -/

section Hash

variable {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

open QOU.BraidKnot.ExplicitCentralIdempotentGeneral QOU.SchurWeyl.SeminormalRep

/-- `d ↦ q^{2d}`, the eigenvalue of `L_k` on a box of content `d`. -/
noncomputable def gPos (d : ℤ) : K := q ^ (2 * d)

include hq0 hq2 in
theorem gPos_injective : Function.Injective (gPos q) := by
  intro a b h
  have := zpow_injective_of_not_root_of_unity hq0 hq2 h
  omega

/-- The sign twist: a `K`-algebra endomorphism with `σ_i ↦ −σ_i⁻¹`. -/
structure IsHash (φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n) : Prop where
  map_sigma : ∀ i : Fin n, φ (Hecke.σ K q q⁻¹ n i) = -Hecke.σInv K q q⁻¹ n i

theorem IsHash.map_qJM {φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n} (hφ : IsHash q n φ) :
    ∀ k, φ (qJM K q q⁻¹ n k) = qJMInv K q q⁻¹ n k
  | 0 => by rw [qJM_zero, qJMInv_zero, map_one]
  | k + 1 => by
      by_cases hk : k < n
      · rw [qJM_succ K q q⁻¹ n hk, qJMInv_succ K q q⁻¹ n hk, map_mul, map_mul,
          hφ.map_qJM k, hφ.map_sigma, neg_mul, mul_neg, neg_mul, neg_neg]
      · have h1 : qJM K q q⁻¹ n (k + 1) = qJM K q q⁻¹ n k := by simp only [qJM, dif_neg hk]
        have h2 : qJMInv K q q⁻¹ n (k + 1) = qJMInv K q q⁻¹ n k := by
          simp only [qJMInv, dif_neg hk]
        rw [h1, h2, hφ.map_qJM k]

theorem mulProj_eq_lagr {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    mulProj q n T = lagr n (qJM K q q⁻¹ n) (gPos q) (contentVec T) := rfl

theorem IsHash.map_mulProj {φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n} (hφ : IsHash q n φ)
    {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    φ (mulProj q n T) = lagr n (qJMInv K q q⁻¹ n) (gPos q) (contentVec T) := by
  rw [mulProj_eq_lagr, map_lagr]
  congr 1
  funext k
  exact IsHash.map_qJM q n hφ k

/-- The conjugate partition `λ'`: the one whose shape is the transpose of `λ`'s. -/
noncomputable def conjPart (lam : Nat.Partition (n + 1)) : Nat.Partition (n + 1) :=
  (QOU.Mathlib.exists_partitionShape_eq (QOU.Mathlib.partitionShape lam).transpose
    (by rw [card_cells_transpose, QOU.Mathlib.partitionShape_card])).choose

theorem partitionShape_conjPart (lam : Nat.Partition (n + 1)) :
    QOU.Mathlib.partitionShape (conjPart n lam) = (QOU.Mathlib.partitionShape lam).transpose :=
  (QOU.Mathlib.exists_partitionShape_eq (QOU.Mathlib.partitionShape lam).transpose
    (by rw [card_cells_transpose, QOU.Mathlib.partitionShape_card])).choose_spec

/-- The transposed tableau, as a tableau of shape `λ'`. -/
noncomputable def tr {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape (conjPart n lam)) :=
  (partitionShape_conjPart n lam).symm ▸ sytTranspose T

theorem contentVec_tr {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) {k : ℕ}
    (hk : k ∈ Finset.range (n + 1)) : contentVec (tr n T) k = -contentVec T k := by
  rw [tr, contentVec_cast, contentVec_sytTranspose (partitionShape_card_succ lam) T hk]

include hq0 hq2 in
theorem heckeProduct_lagrHash (lam : Nat.Partition (n + 1))
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    AnyChar.heckeProductF q hq0 hq2 n (lagr n (qJMInv K q q⁻¹ n) (gPos q) (contentVec T))
      = Pi.single (conjPart n lam) (Matrix.single (tr n T) (tr n T) 1) := by
  classical
  have hinj : Set.InjOn (gPos q) {d | d ∈ contentRange n} := (gPos_injective q hq0 hq2).injOn
  have hfg : ∀ x, gInv q x = gPos q (Neg.neg x) := fun x => by simp [gInv, gPos]
  have hTr : ∀ k ∈ Finset.range (n + 1), contentVec T k ∈ contentRange n :=
    fun k hk => contentVec_mem (partitionShape_card_succ lam) T hk
  funext mu
  rw [AnyChar.heckeProductF_apply, map_lagr]
  rw [lagr_diagonal n (gInv q) (gPos q) (contentVec T) (fun S => contentVec S) _
    (fun k hk => seminormalRep_qJMInv_diag q hq0 hq2 n (partitionShape_card_succ mu) k
      (by rw [List.mem_range] at hk; omega))]
  ext S U
  by_cases hSU : S ≠ U
  · rw [Matrix.diagonal_apply_ne _ hSU]
    by_cases hmu : mu = conjPart n lam
    · subst hmu
      rw [Pi.single_eq_same]
      exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hSU (h.1.symm.trans h.2))).symm
    · rw [Pi.single_eq_of_ne hmu]; rfl
  push_neg at hSU
  subst hSU
  rw [Matrix.diagonal_apply_eq]
  have hSr : ∀ k ∈ Finset.range (n + 1), -contentVec S k ∈ contentRange n :=
    fun k hk => mem_contentRange_neg (contentVec_mem (partitionShape_card_succ mu) S hk)
  by_cases hall : ∀ k ∈ Finset.range (n + 1), contentVec S k = contentVec (tr n T) k
  · have hmu : mu = conjPart n lam := QOU.Mathlib.partitionShape_injective
      (shape_eq_of_contentVec_eq (partitionShape_card_succ mu)
        (partitionShape_card_succ (conjPart n lam)) S (tr n T) hall)
    subst hmu
    have hST : S = tr n T := eq_of_contentVec_eq (partitionShape_card_succ _) S (tr n T) hall
    subst hST
    rw [Pi.single_eq_same, Matrix.single_apply_same]
    refine lagrVal_one n (gInv q) (gPos q) hinj _ _ hTr (fun k hk => ?_)
    rw [hfg, hall k hk, contentVec_tr n T hk, neg_neg]
  · push_neg at hall
    obtain ⟨k, hk, hne⟩ := hall
    have hne' : Neg.neg (contentVec S k) ≠ contentVec T k := by
      intro h; apply hne; rw [contentVec_tr n T hk, ← h, neg_neg]
    rw [lagrVal_eq_zero n (gInv q) (gPos q) (contentVec T) (contentVec S) Neg.neg hfg hSr hk hne']
    by_cases hmu : mu = conjPart n lam
    · subst hmu
      rw [Pi.single_eq_same]
      refine (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hne ?_)).symm
      rw [← h.1]
    · rw [Pi.single_eq_of_ne hmu]; rfl

include hq0 hq2 in
/-- **`#(π_T) = π_{T'}`**, with `T'` the transposed tableau. -/
theorem IsHash.map_proj {φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n} (hφ : IsHash q n φ)
    {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    φ (proj q n T) = proj q n (tr n T) := by
  rw [← mulProj_eq_proj q hq0 hq2 n T, hφ.map_mulProj]
  apply AnyChar.heckeProductF_injective q hq0 hq2 n
  rw [heckeProduct_lagrHash q hq0 hq2 n lam T, proj_eq_symm q hq0 hq2 n]
  exact ((AnyChar.heckeWedderburnF q hq0 hq2 n).apply_symm_apply _).symm

theorem tr_bijective (lam : Nat.Partition (n + 1)) :
    Function.Bijective (tr n (lam := lam)) := by
  constructor
  · intro T U h
    apply eq_of_contentVec_eq (partitionShape_card_succ lam) T U
    intro k hk
    have := congrArg (fun X => contentVec X k) h
    simp only at this
    rw [contentVec_tr n T hk, contentVec_tr n U hk] at this
    exact neg_injective this
  · intro U
    have hsh : (QOU.Mathlib.partitionShape (conjPart n lam)).transpose
        = QOU.Mathlib.partitionShape lam := by
      rw [partitionShape_conjPart, YoungDiagram.transpose_transpose]
    refine ⟨hsh ▸ sytTranspose U, ?_⟩
    apply eq_of_contentVec_eq (partitionShape_card_succ (conjPart n lam))
    intro k hk
    have hk' := hk
    rw [contentVec_tr n _ hk, contentVec_cast,
      contentVec_sytTranspose (partitionShape_card_succ _) U hk',
      neg_neg]

include hq0 hq2 in
/-- **Cross-check 4 for the sign twist: `#(e_λ) = e_λ'`**, for every `λ ⊢ n+1`. -/
theorem IsHash.map_centralIdem {φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n} (hφ : IsHash q n φ)
    (lam : Nat.Partition (n + 1)) :
    φ (centralIdem q n lam) = centralIdem q n (conjPart n lam) := by
  unfold centralIdem
  rw [map_sum]
  rw [Finset.sum_congr rfl (fun T _ => IsHash.map_proj q hq0 hq2 n hφ T)]
  exact Fintype.sum_bijective _ (tr_bijective n lam) _ _ (fun _ => rfl)

include hq0 in
/-- The braid relation for the inverse generators `σ_i⁻¹ = σ_i − h`. -/
theorem σInv_braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    Hecke.σInv K q q⁻¹ n i * Hecke.σInv K q q⁻¹ n ⟨(i : ℕ) + 1, hi⟩ * Hecke.σInv K q q⁻¹ n i
      = Hecke.σInv K q q⁻¹ n ⟨(i : ℕ) + 1, hi⟩ * Hecke.σInv K q q⁻¹ n i
          * Hecke.σInv K q q⁻¹ n ⟨(i : ℕ) + 1, hi⟩ := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  set a := Hecke.σ K q q⁻¹ n i
  set b := Hecke.σ K q q⁻¹ n ⟨(i : ℕ) + 1, hi⟩
  set h := q - q⁻¹
  have ha : a * a = h • a + 1 := Hecke.σ_quadratic_qou K q q⁻¹ n hqi i
  have hb : b * b = h • b + 1 := Hecke.σ_quadratic_qou K q q⁻¹ n hqi _
  have hab : a * b * a = b * a * b := Hecke.σ_braid K q q⁻¹ n i hi
  simp only [Hecke.σInv]
  -- (a - h)(b - h)(a - h) = aba - h(ab + ba) - h a² + h²(2a + b) - h³, and a² = h a + 1
  have e1 : (a - h • 1) * (b - h • 1) * (a - h • 1)
      = a * b * a - h • (a * b + b * a) - h • (a * a) + (h * h) • (a + a + b)
        - (h * h * h) • (1 : Hecke K q q⁻¹ n) := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
      smul_sub, smul_add]
    module
  have e2 : (b - h • 1) * (a - h • 1) * (b - h • 1)
      = b * a * b - h • (b * a + a * b) - h • (b * b) + (h * h) • (b + b + a)
        - (h * h * h) • (1 : Hecke K q q⁻¹ n) := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
      smul_sub, smul_add]
    module
  rw [e1, e2, ha, hb, hab, add_comm (b * a) (a * b)]
  module

include hq0 in
/-- **The sign twist exists**: `σ_i ↦ −σ_i⁻¹` extends to a `K`-algebra endomorphism. -/
noncomputable def hashMap : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n :=
  Hecke.lift K q q⁻¹ n (fun i => -Hecke.σInv K q q⁻¹ n i)
    (fun i => by
      have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
      have ha := Hecke.σ_quadratic_qou K q q⁻¹ n hqi i
      simp only [Hecke.σInv, neg_mul_neg, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
        one_mul, mul_one, hqi, ha]
      module)
    (fun i hi => by
      simp only [neg_mul, mul_neg, neg_neg]
      rw [σInv_braid q hq0 n i hi])
    (fun i j h => by
      simp only [neg_mul, mul_neg, Hecke.σInv, sub_mul, mul_sub, smul_mul_assoc,
        mul_smul_comm, one_mul, mul_one, Hecke.σ_commute K q q⁻¹ n i j h]
      module)

include hq0 in
theorem isHash_hashMap : IsHash q n (hashMap q hq0 n) :=
  ⟨fun i => by simp [hashMap]⟩

include hq0 hq2 in
/-- **Unconditional: the sign twist `σ_i ↦ −σ_i⁻¹` sends `e_λ` to `e_λ'`** for every `λ ⊢ n+1`,
at generic `q`, in any characteristic. -/
theorem hashMap_centralIdem (lam : Nat.Partition (n + 1)) :
    hashMap q hq0 n (centralIdem q n lam) = centralIdem q n (conjPart n lam) :=
  IsHash.map_centralIdem q hq0 hq2 n (isHash_hashMap q hq0 n) lam

end Hash

end QOU.BraidKnot.CentralIdempotentInvolution
