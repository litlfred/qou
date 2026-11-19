import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.QJucysMurphyEigen
import QOU.SchurWeyl.SytContentTuple
import QOU.BraidKnot.ExplicitCentralIdempotent
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Murphy–Lagrange central primitive idempotents

Algebraic formalization for `lem:explicit-central-idempotent-lagrange` and
`prop:explicit-central-idempotent`:

1. **Joint-eigenbasis Lagrange interpolation (`lagrangeEndProj`, `shapeCentralEnd`):**
   Given commuting linear endomorphisms `J : Fin m → Module.End K V` acting diagonally on a
   basis `b : Module.Basis ι K V` with simple joint eigenvalue tuples `c : ι → Fin m → K`, the
   Lagrange polynomial projector `lagrangeEndProj` acts on `b T'` as `δ_{T, T'} • b T'`.
   Summing over standard tableaux of shape `λ` produces `shapeCentralEnd`, satisfying
   completeness (`∑_λ e_λ = 1`), mutual orthogonality (`e_λ * e_μ = δ_{λ,μ} e_λ`), and
   idempotency (`e_λ * e_λ = e_λ`).
2. **Content inversion and transpose pairing (`qContent_transpose_eq_inv`, `shapeCentralEnd_comp_conjTab`):**
   Under cell transposition `(i, j) ↦ (j, i)`, `ExplicitCentralIdempotent.qContent` satisfies
   `qContent j i q = qContent i j q⁻¹` and `qContent i j q * qContent j i q = 1`. Substituting
   transposed contents `c ∘ conjTab` or conjugating by the transpose involution on the eigenbasis
   maps `e_λ` to `e_{λ'}`, fixing `e_λ` whenever `λ = λ'`; simultaneous ring-involution action
   on eigenvalues and content parameters respects each scalar Lagrange factor.
3. **Unconditional central primitive idempotents in `Hecke K q q⁻¹ n` (`murphyHeckeCentralIdem`):**
   Building the multiplicative Jucys–Murphy Lagrange projector `murphyTabProj` directly from
   `qJM K q q⁻¹ n k` and `q ^ (2 * d)` (`|d| ≤ n`) and summing over
   `StandardYoungTableau (partitionShape lam)` gives `murphyHeckeCentralIdem` inside
   `Hecke K q q⁻¹ n`, mapped by `heckeProduct` to `Pi.single lam 1`, yielding centrality in
   `Hecke K q q⁻¹ n`, mutual orthogonality, idempotency, and sum-to-identity for every `n : ℕ`
   at generic `q`.
4. **Concrete `H_2(q)` and `H_3(q)` verifications:**
   Explicit quadratic-relation idempotents in `H_2(q)` (comparing the transposing involution
   `σ ↦ -σ⁻¹` with simultaneous `σ ↦ σ⁻¹, q ↦ q⁻¹` bar inversion) and the four-tableau
   content separation and transpose pairing for `H_3(q)`.
-/

namespace QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents

open QOU.SchurWeyl
open QOU.SchurWeyl.TableauCells QOU.SchurWeyl.SeminormalRep
open QOU.Mathlib (StandardYoungTableau)
open QOU.BraidKnot.ExplicitCentralIdempotent (qContent)

/-! ## Part 1: Joint-eigenbasis Lagrange interpolation and shape idempotents -/

section JointEigenbasisLagrange

variable {K : Type*} [Field K]

/-- Scalar Lagrange interpolation factor over a finite spectrum `C`, normalized at `target` and
evaluated at `evalAt`. -/
noncomputable def lagrangeFactor [DecidableEq K] (C : Finset K) (target evalAt : K) : K :=
  ∏ x ∈ C.erase target, (target - x)⁻¹ * (evalAt - x)

theorem lagrangeFactor_self [DecidableEq K] {C : Finset K} {target : K} :
    lagrangeFactor C target target = 1 := by
  unfold lagrangeFactor
  refine Finset.prod_eq_one (fun x hx => ?_)
  have hne : target - x ≠ 0 := sub_ne_zero.mpr (Ne.symm (Finset.mem_erase.mp hx).1)
  exact inv_mul_cancel₀ hne

theorem lagrangeFactor_eq_zero_of_ne [DecidableEq K] {C : Finset K} {target evalAt : K}
    (heval : evalAt ∈ C) (hne : evalAt ≠ target) :
    lagrangeFactor C target evalAt = 0 := by
  unfold lagrangeFactor
  refine Finset.prod_eq_zero (Finset.mem_erase.mpr ⟨hne, heval⟩) ?_
  rw [sub_self, mul_zero]

/-- Joint-eigenvalue scalar Lagrange projector `∏_k lagrangeFactor C (c T k) (c T' k)`. -/
noncomputable def lagrangeProjScalar [DecidableEq K] {ι κ : Type*} [Fintype κ]
    (C : Finset K) (c : ι → κ → K) (T T' : ι) : K :=
  ∏ k : κ, lagrangeFactor C (c T k) (c T' k)

theorem lagrangeProjScalar_self [DecidableEq K] {ι κ : Type*} [Fintype κ]
    (C : Finset K) (c : ι → κ → K) (T : ι) :
    lagrangeProjScalar C c T T = 1 := by
  unfold lagrangeProjScalar
  exact Finset.prod_eq_one (fun _ _ => lagrangeFactor_self)

theorem lagrangeProjScalar_eq_zero_of_sep [DecidableEq K] {ι κ : Type*} [Fintype κ]
    (C : Finset K) (c : ι → κ → K) {T T' : ι}
    (hc' : ∀ k : κ, c T' k ∈ C) (hsep : ∃ k : κ, c T k ≠ c T' k) :
    lagrangeProjScalar C c T T' = 0 := by
  obtain ⟨k, hne⟩ := hsep
  unfold lagrangeProjScalar
  refine Finset.prod_eq_zero (Finset.mem_univ k) ?_
  exact lagrangeFactor_eq_zero_of_ne (hc' k) (Ne.symm hne)

/-- Under joint eigenvalue separation, `lagrangeProjScalar` evaluates to the Kronecker delta on
all pairs `(T, T')`. -/
theorem lagrangeProjScalar_eq_ite [DecidableEq K] {ι κ : Type*} [DecidableEq ι] [Fintype κ]
    (C : Finset K) (c : ι → κ → K)
    (hc : ∀ (T : ι) (k : κ), c T k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : κ, c T k ≠ c T' k)
    (T T' : ι) :
    lagrangeProjScalar C c T T' = if T = T' then 1 else 0 := by
  by_cases h : T = T'
  · subst h
    rw [if_pos rfl, lagrangeProjScalar_self]
  · rw [if_neg h]
    exact lagrangeProjScalar_eq_zero_of_sep C c (hc T') (hsep T T' h)

/-- Single-coordinate operator Lagrange factor in `Module.End K V` over an explicit spectrum list
`C : List K`. -/
noncomputable def lagrangeEndFactor [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    (C : List K) (Jk : Module.End K V) (target : K) : Module.End K V :=
  ((C.filter (fun x => x ≠ target)).map
    (fun x => (target - x)⁻¹ • (Jk - algebraMap K (Module.End K V) x))).prod

/-- Multi-variable Lagrange projector in `Module.End K V` built as an ordered product over
`k : Fin m` of the single-coordinate Lagrange factors of `J k`. -/
noncomputable def lagrangeEndProj [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V] {ι : Type*} {m : ℕ}
    (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K) (T : ι) :
    Module.End K V :=
  ((List.finRange m).map (fun k : Fin m => lagrangeEndFactor C (J k) (c T k))).prod

/-- Helper: a product of linear endomorphisms that each scale `v` by a scalar scales `v` by the
product of those scalars. -/
theorem list_prod_end_apply_eigenvector
    {V : Type*} [AddCommGroup V] [Module K V] {α : Type*}
    (l : List α) (F : α → Module.End K V) (f : α → K) (v : V)
    (heig : ∀ a ∈ l, F a v = f a • v) :
    (l.map F).prod v = (l.map f).prod • v := by
  induction l with
  | nil => simp
  | cons a tl ih =>
    rw [List.map_cons, List.prod_cons, Module.End.mul_apply,
      ih (fun x hx => heig x (List.mem_cons_of_mem a hx)),
      map_smul, heig a List.mem_cons_self, smul_smul, List.map_cons, List.prod_cons, mul_comm]

theorem lagrangeEndFactor_apply_eigenvector [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    (C : List K) (Jk : Module.End K V) (target eig : K) (v : V)
    (heig : Jk v = eig • v) :
    lagrangeEndFactor C Jk target v =
      (((C.filter (fun x => x ≠ target)).map (fun x => (target - x)⁻¹ * (eig - x))).prod) • v := by
  unfold lagrangeEndFactor
  refine list_prod_end_apply_eigenvector (C.filter (fun x => x ≠ target))
    (fun x => (target - x)⁻¹ • (Jk - algebraMap K (Module.End K V) x))
    (fun x => (target - x)⁻¹ * (eig - x)) v (fun x _ => ?_)
  simp only [LinearMap.smul_apply, LinearMap.sub_apply, Module.algebraMap_end_apply, heig,
     ← sub_smul, smul_smul]

/-- **Eigenbasis evaluation of `lagrangeEndProj`.** On any joint eigenvector `v T'` with
`J k (v T') = c T' k • v T'`, `lagrangeEndProj` acts as the Kronecker delta `δ_{T, T'}` whenever
distinct indices carry distinct eigenvalue tuples in `C`. -/
theorem lagrangeEndProj_apply_eigenvector [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V] {ι : Type*} [DecidableEq ι] {m : ℕ}
    (C : List K) (Jk : Fin m → Module.End K V) (c : ι → Fin m → K)
    (v : ι → V)
    (heig : ∀ (k : Fin m) (T' : ι), Jk k (v T') = c T' k • v T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (T T' : ι) :
    lagrangeEndProj C Jk c T (v T') = if T = T' then v T' else 0 := by
  unfold lagrangeEndProj
  rw [list_prod_end_apply_eigenvector (List.finRange m)
    (fun k => lagrangeEndFactor C (Jk k) (c T k))
    (fun k => ((C.filter (fun x => x ≠ c T k)).map
      (fun x => (c T k - x)⁻¹ * (c T' k - x))).prod)
    (v T')
    (fun k _ => lagrangeEndFactor_apply_eigenvector C (Jk k) (c T k) (c T' k) (v T') (heig k T'))]
  by_cases hTT : T = T'
  · subst hTT
    rw [if_pos rfl]
    suffices h1 : ((List.finRange m).map (fun k =>
        ((C.filter (fun x => x ≠ c T k)).map
          (fun x => (c T k - x)⁻¹ * (c T k - x))).prod)).prod = 1 by
      rw [h1, one_smul]
    refine List.prod_eq_one (fun s hs => ?_)
    obtain ⟨k, -, rfl⟩ := List.mem_map.mp hs
    refine List.prod_eq_one (fun r hr => ?_)
    obtain ⟨x, hx, rfl⟩ := List.mem_map.mp hr
    rw [List.mem_filter] at hx
    have hne : c T k - x ≠ 0 := sub_ne_zero.mpr (Ne.symm (of_decide_eq_true hx.2))
    exact inv_mul_cancel₀ hne
  · rw [if_neg hTT]
    obtain ⟨k, hkne⟩ := hsep T T' hTT
    suffices h0 : ((List.finRange m).map (fun j =>
        ((C.filter (fun x => x ≠ c T j)).map
          (fun x => (c T j - x)⁻¹ * (c T' j - x))).prod)).prod = 0 by
      rw [h0, zero_smul]
    refine List.prod_eq_zero (List.mem_map.mpr ⟨k, List.mem_finRange k, ?_⟩)
    refine List.prod_eq_zero (List.mem_map.mpr ⟨c T' k, ?_, ?_⟩)
    · rw [List.mem_filter]
      exact ⟨hc T' k, decide_eq_true (Ne.symm hkne)⟩
    · rw [sub_self, mul_zero]

/-- Shape-summed Murphy–Lagrange operator `e_λ = ∑_{shapeOf T = λ} lagrangeEndProj C J c T`
in `Module.End K V`. -/
noncomputable def shapeCentralEnd [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq Λ] {m : ℕ}
    (shapeOf : ι → Λ) (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (lam : Λ) : Module.End K V :=
  ∑ T ∈ Finset.univ.filter (fun T => shapeOf T = lam), lagrangeEndProj C J c T

theorem shapeCentralEnd_apply_eigenvector [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [DecidableEq Λ] {m : ℕ}
    (shapeOf : ι → Λ) (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (v : ι → V)
    (heig : ∀ (k : Fin m) (T' : ι), J k (v T') = c T' k • v T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (lam : Λ) (T' : ι) :
    shapeCentralEnd shapeOf C J c lam (v T') = if shapeOf T' = lam then v T' else 0 := by
  unfold shapeCentralEnd
  rw [LinearMap.sum_apply]
  simp_rw [lagrangeEndProj_apply_eigenvector C J c v heig hc hsep _ T']
  by_cases hsh : shapeOf T' = lam
  · rw [if_pos hsh]
    have hmem : T' ∈ Finset.univ.filter (fun T => shapeOf T = lam) :=
      Finset.mem_filter.mpr ⟨Finset.mem_univ T', hsh⟩
    rw [Finset.sum_eq_single T'
      (fun T _ hne => if_neg hne)
      (fun hnot => absurd hmem hnot), if_pos rfl]
  · rw [if_neg hsh]
    refine Finset.sum_eq_zero (fun T hT => ?_)
    have hTlam : shapeOf T = lam := (Finset.mem_filter.mp hT).2
    refine if_neg (fun hEq => hsh ?_)
    rw [← hEq, hTlam]

/-- **Cross-check 1 (Sum-to-identity on a joint eigenbasis):**
`∑_λ shapeCentralEnd ... λ = 1` in `Module.End K V`. -/
theorem shapeCentralEnd_sum_eq_one [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [Fintype Λ] [DecidableEq Λ] {m : ℕ}
    (b : Module.Basis ι K V)
    (shapeOf : ι → Λ) (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (heig : ∀ (k : Fin m) (T' : ι), J k (b T') = c T' k • b T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k) :
    (∑ lam : Λ, shapeCentralEnd shapeOf C J c lam) = 1 := by
  refine b.ext (fun T' => ?_)
  rw [LinearMap.sum_apply, Module.End.one_apply]
  simp_rw [shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep _ T']
  rw [Finset.sum_eq_single (shapeOf T')
    (fun lam _ hne => if_neg (Ne.symm hne))
    (fun hnot => absurd (Finset.mem_univ (shapeOf T')) hnot), if_pos rfl]

/-- **Cross-check 2 (Mutual orthogonality on a joint eigenbasis):**
`e_λ * e_μ = δ_{λ,μ} e_λ` in `Module.End K V`. -/
theorem shapeCentralEnd_mul [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [DecidableEq Λ] {m : ℕ}
    (b : Module.Basis ι K V)
    (shapeOf : ι → Λ) (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (heig : ∀ (k : Fin m) (T' : ι), J k (b T') = c T' k • b T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (lam mu : Λ) :
    shapeCentralEnd shapeOf C J c lam * shapeCentralEnd shapeOf C J c mu =
      if lam = mu then shapeCentralEnd shapeOf C J c lam else 0 := by
  refine b.ext (fun T' => ?_)
  rw [Module.End.mul_apply,
    shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep mu T']
  by_cases hlm : lam = mu
  · subst hlm
    rw [if_pos rfl, shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep lam T']
    by_cases hT : shapeOf T' = lam
    · rw [if_pos hT,
        shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep lam T', if_pos hT]
    · rw [if_neg hT, map_zero]
  · rw [if_neg hlm, LinearMap.zero_apply]
    by_cases hT : shapeOf T' = mu
    · rw [if_pos hT,
        shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep lam T',
        if_neg (fun h => hlm (h.symm.trans hT))]
    · rw [if_neg hT, map_zero]

/-- **Idempotency (`e_λ * e_λ = e_λ`):** diagonal specialization of `shapeCentralEnd_mul`. -/
theorem shapeCentralEnd_idem [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [DecidableEq Λ] {m : ℕ}
    (b : Module.Basis ι K V)
    (shapeOf : ι → Λ) (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (heig : ∀ (k : Fin m) (T' : ι), J k (b T') = c T' k • b T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (lam : Λ) :
    shapeCentralEnd shapeOf C J c lam * shapeCentralEnd shapeOf C J c lam =
      shapeCentralEnd shapeOf C J c lam := by
  rw [shapeCentralEnd_mul b shapeOf C J c heig hc hsep lam lam, if_pos rfl]

end JointEigenbasisLagrange

/-! ## Part 2: `q`-content inversion and transpose / bar pairing -/

section TransposeAndBarPairing

/-- Under cell transposition `(i, j) ↦ (j, i)`, `qContent` inverts `q` to `q⁻¹`. -/
theorem qContent_transpose_eq_inv {R : Type*} [CommRing R] (i j : ℤ) (q : Rˣ) :
    qContent j i q = qContent i j q⁻¹ := by
  unfold qContent
  congr 1
  rw [inv_zpow', show (2 * (j - i) : ℤ) = -(2 * (i - j)) by ring, neg_neg]

/-- Multiplicative pairing of transposed box `q`-contents: `c(i, j; q) * c(j, i; q) = 1`. -/
theorem qContent_mul_transpose_eq_one {R : Type*} [CommRing R] (i j : ℤ) (q : Rˣ) :
    qContent i j q * qContent j i q = 1 := by
  unfold qContent
  rw [← Units.val_mul, ← zpow_add]
  have h0 : (2 * (j - i) + 2 * (i - j) : ℤ) = 0 := by ring
  rw [h0, zpow_zero, Units.val_one]

/-- **Term-by-term bar covariance of `lagrangeFactor`.** For any ring involution `barK : K →+* K`
fixing the finite spectrum `C` setwise (`∀ x ∈ C, barK x ∈ C`), applying `barK` to
`lagrangeFactor C target evalAt` equals `lagrangeFactor C (barK target) (barK evalAt)`. -/
theorem map_lagrangeFactor_bar {K : Type*} [Field K] [DecidableEq K]
    (barK : K →+* K) (hbar_inv : Function.Involutive barK)
    {C : Finset K} (hC : ∀ x ∈ C, barK x ∈ C) (target evalAt : K) :
    barK (lagrangeFactor C target evalAt) =
      lagrangeFactor C (barK target) (barK evalAt) := by
  unfold lagrangeFactor
  rw [map_prod]
  refine Finset.prod_bij (fun x _ => barK x) ?_ ?_ ?_ ?_
  · intro x hx
    rw [Finset.mem_erase] at hx ⊢
    refine ⟨fun hEq => hx.1 (hbar_inv.injective hEq), hC x hx.2⟩
  · intro x₁ _ x₂ _ hEq
    exact hbar_inv.injective hEq
  · intro y hy
    rw [Finset.mem_erase] at hy
    refine ⟨barK y, Finset.mem_erase.mpr ⟨?_, hC y hy.2⟩, hbar_inv y⟩
    intro hEq
    apply hy.1
    rw [← hEq, hbar_inv y]
  · intro x _
    rw [map_mul, map_inv₀, map_sub, map_sub]

/-- **Cross-check 3 & 4 (Content-inversion / transpose pairing on `shapeCentralEnd`):**
Replacing the content family `c` by the inverted/transposed family `c ∘ conjTab` (where
`conjTab : ι ≃ ι` intertwines `shapeOf` with `conjShape : Λ ≃ Λ`) maps `shapeCentralEnd` at `λ`
to `shapeCentralEnd` at `conjShape λ`. -/
theorem shapeCentralEnd_comp_conjTab {K : Type*} [Field K] [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq Λ] {m : ℕ}
    (shapeOf : ι → Λ) (conjShape : Λ ≃ Λ) (conjTab : ι ≃ ι)
    (hsh : ∀ T : ι, shapeOf (conjTab T) = conjShape (shapeOf T))
    (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K) (lam : Λ) :
    shapeCentralEnd shapeOf C J (fun T => c (conjTab T)) lam =
      shapeCentralEnd shapeOf C J c (conjShape lam) := by
  unfold shapeCentralEnd lagrangeEndProj
  refine Finset.sum_bij (fun T _ => conjTab T) ?_ ?_ ?_ ?_
  · intro T hT
    rw [Finset.mem_filter] at hT ⊢
    exact ⟨Finset.mem_univ _, by rw [hsh T, hT.2]⟩
  · intro T₁ _ T₂ _ hEq
    exact conjTab.injective hEq
  · intro U hU
    rw [Finset.mem_filter] at hU
    refine ⟨conjTab.symm U, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩,
      conjTab.apply_symm_apply U⟩
    apply conjShape.injective
    rw [← hsh (conjTab.symm U), conjTab.apply_symm_apply, hU.2]
  · intro T _
    rfl

/-- **Transpose conjugation on the joint eigenbasis (`#`-involution):**
Let `tauV : V ≃ₗ[K] V` permute the joint eigenbasis by tableau transposition
`tauV (b T) = b (conjTab T)` with `conjTab` and `conjShape` involutive. Conjugating
`shapeCentralEnd ... lam` by `tauV` yields `shapeCentralEnd ... (conjShape lam)`. -/
theorem conj_shapeCentralEnd_eq_transpose {K : Type*} [Field K] [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [DecidableEq Λ] {m : ℕ}
    (b : Module.Basis ι K V)
    (shapeOf : ι → Λ) (conjShape : Λ ≃ Λ) (conjTab : ι ≃ ι)
    (hTabInv : Function.Involutive conjTab)
    (hShapeInv : Function.Involutive conjShape)
    (hsh : ∀ T : ι, shapeOf (conjTab T) = conjShape (shapeOf T))
    (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (heig : ∀ (k : Fin m) (T' : ι), J k (b T') = c T' k • b T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (tauV : V ≃ₗ[K] V) (htau : ∀ T : ι, tauV (b T) = b (conjTab T))
    (lam : Λ) :
    tauV.toLinearMap * shapeCentralEnd shapeOf C J c lam * tauV.symm.toLinearMap =
      shapeCentralEnd shapeOf C J c (conjShape lam) := by
  refine b.ext (fun T' => ?_)
  have hsymm : tauV.symm (b T') = b (conjTab T') := by
    apply tauV.injective
    rw [tauV.apply_symm_apply, htau, hTabInv T']
  rw [Module.End.mul_apply, Module.End.mul_apply, LinearEquiv.coe_toLinearMap,
    LinearEquiv.coe_toLinearMap, hsymm,
    shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep lam (conjTab T'),
    shapeCentralEnd_apply_eigenvector shapeOf C J c b heig hc hsep (conjShape lam) T']
  have hiff : shapeOf (conjTab T') = lam ↔ shapeOf T' = conjShape lam := by
    rw [hsh T']
    constructor
    · intro h; rw [← h, hShapeInv]
    · intro h; rw [h, hShapeInv]
  by_cases h : shapeOf T' = conjShape lam
  · rw [if_pos (hiff.mpr h), if_pos h, htau, hTabInv T']
  · rw [if_neg (mt hiff.mp h), if_neg h, map_zero]

/-- **Self-conjugate invariance (`λ = λ'`):** when `conjShape lam = lam`, transpose conjugation
fixes `shapeCentralEnd ... lam`. -/
theorem conj_shapeCentralEnd_self_conjugate {K : Type*} [Field K] [DecidableEq K]
    {V : Type*} [AddCommGroup V] [Module K V]
    {ι Λ : Type*} [Fintype ι] [DecidableEq ι] [DecidableEq Λ] {m : ℕ}
    (b : Module.Basis ι K V)
    (shapeOf : ι → Λ) (conjShape : Λ ≃ Λ) (conjTab : ι ≃ ι)
    (hTabInv : Function.Involutive conjTab)
    (hShapeInv : Function.Involutive conjShape)
    (hsh : ∀ T : ι, shapeOf (conjTab T) = conjShape (shapeOf T))
    (C : List K) (J : Fin m → Module.End K V) (c : ι → Fin m → K)
    (heig : ∀ (k : Fin m) (T' : ι), J k (b T') = c T' k • b T')
    (hc : ∀ (T' : ι) (k : Fin m), c T' k ∈ C)
    (hsep : ∀ T T' : ι, T ≠ T' → ∃ k : Fin m, c T k ≠ c T' k)
    (tauV : V ≃ₗ[K] V) (htau : ∀ T : ι, tauV (b T) = b (conjTab T))
    {lam : Λ} (hself : conjShape lam = lam) :
    tauV.toLinearMap * shapeCentralEnd shapeOf C J c lam * tauV.symm.toLinearMap =
      shapeCentralEnd shapeOf C J c lam := by
  rw [conj_shapeCentralEnd_eq_transpose b shapeOf conjShape conjTab hTabInv hShapeInv hsh
    C J c heig hc hsep tauV htau lam, hself]

end TransposeAndBarPairing

/-! ## Part 3: Unconditional all-`n` multiplicative Murphy–Lagrange idempotents in `Hecke K q q⁻¹ n` -/

section AllNHeckeCentralIdempotents

/-- Integer content range `[-n, n]` covering all cell contents of Young diagrams of size `n + 1`. -/
def contentWindow (n : ℕ) : List ℤ :=
  (List.range (2 * n + 1)).map (fun j : ℕ => (j : ℤ) - n)

theorem mem_contentWindow {n : ℕ} {d : ℤ} :
    d ∈ contentWindow n ↔ -(n : ℤ) ≤ d ∧ d ≤ n := by
  simp only [contentWindow, List.mem_map, List.mem_range]
  constructor
  · rintro ⟨j, hj, rfl⟩; omega
  · intro h; exact ⟨(d + n).toNat, by omega, by omega⟩

/-- Content vector `k ↦ cellContent (cellOf T (k + 1))` of a standard Young tableau `T`. -/
noncomputable def sytContentVec {μ : YoungDiagram} (T : StandardYoungTableau μ) (k : ℕ) : ℤ :=
  cellContent (cellOf T (k + 1))

theorem cellContent_in_window {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    {c : ℕ × ℕ} (hc : c ∈ μ.cells) : -(n : ℤ) ≤ cellContent c ∧ cellContent c ≤ n := by
  classical
  obtain ⟨i, j⟩ := c
  have hmem : (i, j) ∈ μ := by simpa using hc
  have hj : j + 1 ≤ n + 1 := by
    rw [← hN]
    have hsub : (Finset.range (j + 1)).image (fun t => (0, t)) ⊆ μ.cells := by
      intro x hx
      obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hx
      have := μ.up_left_mem (Nat.zero_le i) (Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)) hmem
      simpa using this
    have := Finset.card_le_card hsub
    rwa [Finset.card_image_of_injective _ (fun a b h => by simpa using h),
      Finset.card_range] at this
  have hi : i + 1 ≤ n + 1 := by
    rw [← hN]
    have hsub : (Finset.range (i + 1)).image (fun t => (t, 0)) ⊆ μ.cells := by
      intro x hx
      obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hx
      have := μ.up_left_mem (Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)) (Nat.zero_le j) hmem
      simpa using this
    have := Finset.card_le_card hsub
    rwa [Finset.card_image_of_injective _ (fun a b h => by simpa using h),
      Finset.card_range] at this
  simp only [cellContent]
  omega

theorem sytContentVec_mem_window {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    (T : StandardYoungTableau μ) {k : ℕ} (hk : k ∈ Finset.range (n + 1)) :
    sytContentVec T k ∈ contentWindow n := by
  rw [Finset.mem_range] at hk
  rw [mem_contentWindow]
  exact cellContent_in_window hN (cellOf_mem T (Set.mem_Icc.mpr ⟨by omega, by omega⟩))

theorem shape_eq_of_sytContentVec_eq {μ ν : YoungDiagram} {n : ℕ}
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (S : StandardYoungTableau μ) (T : StandardYoungTableau ν)
    (h : ∀ k ∈ Finset.range (n + 1), sytContentVec S k = sytContentVec T k) : μ = ν := by
  classical
  refine youngDiagram_eq_of_contentCount_eq (fun d => ?_)
  have hS := sum_cellOf_range S hμ (fun c => if cellContent c = d then (1 : ℕ) else 0)
  have hT := sum_cellOf_range T hν (fun c => if cellContent c = d then (1 : ℕ) else 0)
  have hST : ∑ k ∈ Finset.range (n + 1), (if cellContent (cellOf S (k + 1)) = d then 1 else 0)
      = ∑ k ∈ Finset.range (n + 1), (if cellContent (cellOf T (k + 1)) = d then 1 else 0) :=
    Finset.sum_congr rfl (fun k hk => by
      have := h k hk
      simp only [sytContentVec] at this
      rw [this])
  have e1 : (diagOf μ d).card = ∑ c ∈ μ.cells, (if cellContent c = d then (1 : ℕ) else 0) := by
    simp only [diagOf, Finset.card_filter]
  have e2 : (diagOf ν d).card = ∑ c ∈ ν.cells, (if cellContent c = d then (1 : ℕ) else 0) := by
    simp only [diagOf, Finset.card_filter]
  rw [e1, e2, ← hS, ← hT, hST]

theorem syt_eq_of_sytContentVec_eq {μ : YoungDiagram} {n : ℕ} (hμ : μ.cells.card = n + 1)
    (S T : StandardYoungTableau μ)
    (h : ∀ k ∈ Finset.range (n + 1), sytContentVec S k = sytContentVec T k) : S = T := by
  refine syt_eq_of_cellContent_eq S T (fun k hk1 hkn => ?_)
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  exact h j (Finset.mem_range.mpr (by omega))

section MultiplicativeProj

variable {K : Type*} [Field K]

/-- `k`-th multiplicative Jucys–Murphy Lagrange factor in `Hecke K q q⁻¹ n`:
`∏_{|d| ≤ n, d ≠ c} (J_k - q^{2d}) / (q^{2c} - q^{2d})`. -/
noncomputable def murphyMultFactor (q : K) (n : ℕ) (k : ℕ) (c : ℤ) : Hecke K q q⁻¹ n :=
  (((contentWindow n).filter (fun d => d ≠ c)).map
    (fun d => (q ^ (2 * c) - q ^ (2 * d))⁻¹ •
      (qJM K q q⁻¹ n k - algebraMap K (Hecke K q q⁻¹ n) (q ^ (2 * d))))).prod

/-- Per-tableau multiplicative Jucys–Murphy Lagrange projector in `Hecke K q q⁻¹ n`. -/
noncomputable def murphyTabProj (q : K) (n : ℕ) (c : ℕ → ℤ) : Hecke K q q⁻¹ n :=
  ((List.range (n + 1)).map (fun k => murphyMultFactor q n k (c k))).prod

/-- Scalar eigenvalue of `murphyTabProj` on a tableau with content vector `e`. -/
noncomputable def murphyProjVal (q : K) (n : ℕ) (c e : ℕ → ℤ) : K :=
  ((List.range (n + 1)).map (fun k =>
    (((contentWindow n).filter (fun d => d ≠ c k)).map
      (fun d => (q ^ (2 * c k) - q ^ (2 * d))⁻¹ * (q ^ (2 * e k) - q ^ (2 * d)))).prod)).prod

theorem list_prod_diag_matrix {m : Type*} [Fintype m] [DecidableEq m]
    {α : Type*} (l : List α) (F : α → m → K) :
    (l.map fun x => Matrix.diagonal (F x)).prod
      = Matrix.diagonal (fun T => (l.map fun x => F x T).prod) := by
  induction l with
  | nil => simp [Matrix.diagonal_one]
  | cons a tl ih =>
    rw [List.map_cons, List.prod_cons, ih, Matrix.diagonal_mul_diagonal]
    simp

theorem seminormalRep_murphyTabProj (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {μ : YoungDiagram} (n : ℕ)
    (hN : μ.cells.card = n + 1) (c : ℕ → ℤ) :
    seminormalRep q hq0 hq2 n hN (murphyTabProj q n c)
      = Matrix.diagonal (fun S => murphyProjVal q n c (sytContentVec S)) := by
  unfold murphyTabProj murphyMultFactor
  rw [map_list_prod, List.map_map]
  simp only [Function.comp_def]
  have hstep : ∀ k ∈ List.range (n + 1),
      (seminormalRep q hq0 hq2 n hN)
        ((((contentWindow n).filter (fun d => d ≠ c k)).map
          (fun d => (q ^ (2 * c k) - q ^ (2 * d))⁻¹ •
            (qJM K q q⁻¹ n k - algebraMap K (Hecke K q q⁻¹ n) (q ^ (2 * d))))).prod)
      = Matrix.diagonal (fun S =>
          (((contentWindow n).filter (fun d => d ≠ c k)).map
            (fun d => (q ^ (2 * c k) - q ^ (2 * d))⁻¹ *
              (q ^ (2 * sytContentVec S k) - q ^ (2 * d)))).prod) := by
    intro k hk
    rw [List.mem_range] at hk
    rw [map_list_prod, List.map_map]
    simp only [Function.comp_def]
    have hfactor : ∀ d : ℤ,
        (seminormalRep q hq0 hq2 n hN)
          ((q ^ (2 * c k) - q ^ (2 * d))⁻¹ •
            (qJM K q q⁻¹ n k - algebraMap K (Hecke K q q⁻¹ n) (q ^ (2 * d))))
        = Matrix.diagonal (fun S => (q ^ (2 * c k) - q ^ (2 * d))⁻¹ *
            (q ^ (2 * sytContentVec S k) - q ^ (2 * d))) := by
      intro d
      rw [map_smul, map_sub, AlgHom.commutes,
        seminormalRep_qJM q hq0 hq2 n hN k (by omega)]
      ext S U
      by_cases h : S = U
      · subst h
        simp [jmDiagVal, sytContentVec, Matrix.algebraMap_eq_diagonal]
      · simp [jmDiagVal, Matrix.algebraMap_eq_diagonal, Matrix.diagonal_apply_ne _ h]
    rw [List.map_congr_left (fun d _ => hfactor d), list_prod_diag_matrix]
  rw [List.map_congr_left (fun k hk => hstep k hk), list_prod_diag_matrix]
  rfl

theorem murphyProjVal_self (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) (c : ℕ → ℤ) :
    murphyProjVal q n c c = 1 := by
  unfold murphyProjVal
  refine List.prod_eq_one (fun s hs => ?_)
  obtain ⟨k, -, rfl⟩ := List.mem_map.mp hs
  refine List.prod_eq_one (fun r hr => ?_)
  obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hr
  rw [List.mem_filter] at hd
  have hdc : d ≠ c k := of_decide_eq_true hd.2
  have hne : q ^ (2 * c k) - q ^ (2 * d) ≠ 0 := by
    refine sub_ne_zero.mpr (fun hEq => ?_)
    have hz : q ^ (2 * c k - 2 * d) = 1 := by
      rw [zpow_sub₀ hq0, hEq, div_self (zpow_ne_zero _ hq0)]
    exact GenericParameter.zpow_ne_one hq2 (by omega) hz
  exact inv_mul_cancel₀ hne

theorem murphyProjVal_eq_zero (q : K) (n : ℕ) (c e : ℕ → ℤ)
    (he : ∀ k ∈ Finset.range (n + 1), e k ∈ contentWindow n)
    {k : ℕ} (hk : k ∈ Finset.range (n + 1)) (hne : e k ≠ c k) :
    murphyProjVal q n c e = 0 := by
  unfold murphyProjVal
  refine List.prod_eq_zero (List.mem_map.mpr ⟨k, List.mem_range.mpr (Finset.mem_range.mp hk), ?_⟩)
  refine List.prod_eq_zero (List.mem_map.mpr ⟨e k, ?_, ?_⟩)
  · rw [List.mem_filter]
    exact ⟨he k hk, decide_eq_true hne⟩
  · rw [sub_self, mul_zero]

theorem matrix_sum_single_diag_eq_one {m : Type*} [Fintype m] [DecidableEq m] :
    (∑ T : m, Matrix.single T T (1 : K)) = (1 : Matrix m m K) := by
  ext S U
  rw [Matrix.sum_apply]
  by_cases hSU : S = U
  · subst hSU
    rw [Matrix.one_apply_eq, Finset.sum_eq_single S
      (fun T _ hne => Matrix.single_apply_of_ne T T 1 S S (fun h => hne h.1))
      (fun hnot => absurd (Finset.mem_univ S) hnot),
      Matrix.single_apply_same]
  · rw [Matrix.one_apply_ne hSU]
    exact Finset.sum_eq_zero (fun T _ =>
      Matrix.single_apply_of_ne T T 1 S U (fun h => hSU (h.1.symm.trans h.2)))

end MultiplicativeProj

section WedderburnIdempotents

variable {K : Type*} [Field K] [CharZero K]

/-- **All-`n` multiplicative Murphy–Lagrange central primitive idempotent in `Hecke K q q⁻¹ n`.**
For any `n : ℕ` and partition `lam : Partition (n + 1)`, `murphyHeckeCentralIdem q n lam` is the
sum over `T : StandardYoungTableau (partitionShape lam)` of `murphyTabProj q n (sytContentVec T)`. -/
noncomputable def murphyHeckeCentralIdem (q : K) (n : ℕ) (lam : Partition (n + 1)) :
    Hecke K q q⁻¹ n :=
  ∑ T : StandardYoungTableau (QOU.Mathlib.partitionShape lam),
    murphyTabProj q n (sytContentVec T)

/-- `heckeProduct` sends the multiplicative Murphy projector of `T` to the matrix unit
`Pi.single lam (Matrix.single T T 1)`. -/
theorem heckeProduct_murphyTabProj (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (lam : Partition (n + 1))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    heckeProduct q hq0 hq2 n (murphyTabProj q n (sytContentVec T))
      = Pi.single lam (Matrix.single T T 1) := by
  classical
  funext mu
  rw [heckeProduct_apply, seminormalRep_murphyTabProj]
  ext S U
  by_cases hmu : mu = lam
  · subst hmu
    rw [Pi.single_eq_same]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      by_cases hST : S = T
      · subst hST
        rw [murphyProjVal_self q hq0 hq2 n]
        exact (Matrix.single_apply_same _ _ _).symm
      · have hdiff : ∃ k ∈ Finset.range (n + 1), sytContentVec S k ≠ sytContentVec T k := by
          by_contra hcon
          push_neg at hcon
          exact hST (syt_eq_of_sytContentVec_eq (partitionShape_card_succ mu) S T hcon)
        obtain ⟨k, hk, hne⟩ := hdiff
        rw [murphyProjVal_eq_zero q n _ _
          (fun j hj => sytContentVec_mem_window (partitionShape_card_succ mu) S hj) hk hne]
        exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hST h.1.symm)).symm
    · rw [Matrix.diagonal_apply_ne _ hSU]
      exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hSU (h.1.symm.trans h.2))).symm
  · rw [Pi.single_eq_of_ne hmu]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      have hdiff : ∃ k ∈ Finset.range (n + 1), sytContentVec S k ≠ sytContentVec T k := by
        by_contra hcon
        push_neg at hcon
        exact hmu (QOU.Mathlib.partitionShape_injective
          (shape_eq_of_sytContentVec_eq (partitionShape_card_succ mu)
            (partitionShape_card_succ lam) S T hcon))
      obtain ⟨k, hk, hne⟩ := hdiff
      rw [murphyProjVal_eq_zero q n _ _
        (fun j hj => sytContentVec_mem_window (partitionShape_card_succ mu) S hj) hk hne]
      rfl
    · rw [Matrix.diagonal_apply_ne _ hSU]
      rfl

/-- Under `heckeProduct`, `murphyHeckeCentralIdem q n lam` maps to the `lam`-block identity
`Pi.single lam 1`. -/
theorem heckeProduct_murphyHeckeCentralIdem (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (lam : Partition (n + 1)) :
    heckeProduct q hq0 hq2 n (murphyHeckeCentralIdem q n lam) = Pi.single lam 1 := by
  classical
  unfold murphyHeckeCentralIdem
  rw [map_sum]
  simp_rw [heckeProduct_murphyTabProj q hq0 hq2 n lam]
  funext mu
  rw [Finset.sum_apply]
  by_cases hmu : mu = lam
  · subst hmu
    simp_rw [Pi.single_eq_same]
    exact matrix_sum_single_diag_eq_one
  · simp_rw [Pi.single_eq_of_ne hmu]
    exact Finset.sum_const_zero

/-- **All-`n` mutual orthogonality in `Hecke K q q⁻¹ n`:**
`e_λ * e_μ = if λ = μ then e_λ else 0`. -/
theorem murphyHeckeCentralIdem_mul (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (lam mu : Partition (n + 1)) :
    murphyHeckeCentralIdem q n lam * murphyHeckeCentralIdem q n mu =
      if lam = mu then murphyHeckeCentralIdem q n lam else 0 := by
  classical
  apply (heckeProduct_bijective q hq0 hq2 n).1
  rw [map_mul, heckeProduct_murphyHeckeCentralIdem, heckeProduct_murphyHeckeCentralIdem]
  by_cases h : lam = mu
  · subst h
    rw [if_pos rfl, heckeProduct_murphyHeckeCentralIdem]
    funext nu
    rw [Pi.mul_apply]
    by_cases hnu : nu = lam
    · subst hnu; simp
    · simp [Pi.single_eq_of_ne hnu]
  · rw [if_neg h, map_zero]
    funext nu
    rw [Pi.mul_apply, Pi.zero_apply]
    by_cases hnu : nu = lam
    · subst hnu
      rw [Pi.single_eq_same, Pi.single_eq_of_ne h, mul_zero]
    · rw [Pi.single_eq_of_ne hnu, zero_mul]

/-- **All-`n` idempotency in `Hecke K q q⁻¹ n`:** `e_λ * e_λ = e_λ`. -/
theorem murphyHeckeCentralIdem_idem (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (lam : Partition (n + 1)) :
    murphyHeckeCentralIdem q n lam * murphyHeckeCentralIdem q n lam =
      murphyHeckeCentralIdem q n lam := by
  classical
  rw [murphyHeckeCentralIdem_mul q hq0 hq2 n lam lam, if_pos rfl]

/-- **All-`n` completeness in `Hecke K q q⁻¹ n`:** `∑_λ e_λ = 1`. -/
theorem murphyHeckeCentralIdem_sum_eq_one (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    (∑ lam : Partition (n + 1), murphyHeckeCentralIdem q n lam) = 1 := by
  classical
  apply (heckeProduct_bijective q hq0 hq2 n).1
  rw [map_sum, map_one]
  simp_rw [heckeProduct_murphyHeckeCentralIdem q hq0 hq2 n]
  funext mu
  rw [Finset.sum_apply, Pi.one_apply, Finset.sum_eq_single mu
    (fun lam _ hne => Pi.single_eq_of_ne (Ne.symm hne) 1)
    (fun hnot => absurd (Finset.mem_univ mu) hnot),
    Pi.single_eq_same]

/-- **All-`n` centrality in `Hecke K q q⁻¹ n`:** `e_λ` commutes with every element of
`Hecke K q q⁻¹ n`. -/
theorem murphyHeckeCentralIdem_comm (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (lam : Partition (n + 1)) (x : Hecke K q q⁻¹ n) :
    murphyHeckeCentralIdem q n lam * x = x * murphyHeckeCentralIdem q n lam := by
  classical
  apply (heckeProduct_bijective q hq0 hq2 n).1
  rw [map_mul, map_mul, heckeProduct_murphyHeckeCentralIdem]
  funext mu
  rw [Pi.mul_apply, Pi.mul_apply]
  by_cases hmu : mu = lam
  · subst hmu
    rw [Pi.single_eq_same, one_mul, mul_one]
  · rw [Pi.single_eq_of_ne hmu, zero_mul, mul_zero]

end WedderburnIdempotents

end AllNHeckeCentralIdempotents

/-! ## Part 4: Concrete `H_2(q)` and `H_3(q)` algebraic verifications -/

section ConcreteH2AndH3

variable {K : Type*} [Field K]

/-- In `H_2(q)`, with generator `s` satisfying `s * s = (q - q⁻¹) • s + 1`, the `(2)` central
idempotent is `(q + q⁻¹)⁻¹ • (s + q⁻¹ • 1)`. -/
noncomputable def h2IdemSym {A : Type*} [Ring A] [Algebra K A] (q : K) (s : A) : A :=
  (q + q⁻¹)⁻¹ • (s + algebraMap K A q⁻¹)

/-- In `H_2(q)`, the `(1, 1)` central idempotent is `(q + q⁻¹)⁻¹ • (-s + q • 1)`. -/
noncomputable def h2IdemAnti {A : Type*} [Ring A] [Algebra K A] (q : K) (s : A) : A :=
  (q + q⁻¹)⁻¹ • (-s + algebraMap K A q)

/-- The Murphy–Lagrange formula `(q² - q⁻²)⁻¹ • (J₂ - q⁻²)` with `J₂ = s * s` simplifies to
`h2IdemSym q s` under the Hecke quadratic relation `s * s = (q - q⁻¹) • s + 1`. -/
theorem h2_murphy_eq_h2IdemSym {A : Type*} [Ring A] [Algebra K A]
    (q : K) (hq0 : q ≠ 0) (hq_sub : q - q⁻¹ ≠ 0)
    (s : A) (hquad : s * s = (q - q⁻¹) • s + 1) :
    (q ^ 2 - (q⁻¹) ^ 2)⁻¹ • (s * s - algebraMap K A ((q⁻¹) ^ 2)) = h2IdemSym q s := by
  unfold h2IdemSym
  rw [hquad]
  have h1 : (1 : A) - algebraMap K A ((q⁻¹) ^ 2) =
      algebraMap K A ((q - q⁻¹) * q⁻¹) := by
    rw [← map_one (algebraMap K A), ← map_sub]
    congr 1
    field_simp
  rw [add_sub_assoc, h1]
  have hfactor : (q - q⁻¹) • s + algebraMap K A ((q - q⁻¹) * q⁻¹) =
      (q - q⁻¹) • (s + algebraMap K A q⁻¹) := by
    rw [smul_add, map_mul, Algebra.smul_def, Algebra.smul_def]
  rw [hfactor, smul_smul]
  congr 1
  have hdiff : q ^ 2 - (q⁻¹) ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
  rw [hdiff, mul_inv_rev, mul_assoc, inv_mul_cancel₀ hq_sub, mul_one]

/-- Sum-to-identity in `H_2(q)`: `h2IdemSym q s + h2IdemAnti q s = 1`. -/
theorem h2Idem_add_eq_one {A : Type*} [Ring A] [Algebra K A]
    (q : K) (hq_add : q + q⁻¹ ≠ 0) (s : A) :
    h2IdemSym q s + h2IdemAnti q s = 1 := by
  unfold h2IdemSym h2IdemAnti
  rw [← smul_add]
  have hsum : (s + algebraMap K A q⁻¹) + (-s + algebraMap K A q) =
      algebraMap K A (q + q⁻¹) := by
    rw [map_add]
    abel
  rw [hsum, Algebra.algebraMap_eq_smul_one, smul_smul, inv_mul_cancel₀ hq_add, one_smul]

/-- Mutual orthogonality in `H_2(q)`: `h2IdemSym q s * h2IdemAnti q s = 0`. -/
theorem h2IdemSym_mul_h2IdemAnti {A : Type*} [Ring A] [Algebra K A]
    (q : K) (hq0 : q ≠ 0) (s : A) (hquad : s * s = (q - q⁻¹) • s + 1) :
    h2IdemSym q s * h2IdemAnti q s = 0 := by
  unfold h2IdemSym h2IdemAnti
  rw [smul_mul_smul]
  have hprod : (s + algebraMap K A q⁻¹) * (-s + algebraMap K A q) = 0 := by
    have hcomm1 : algebraMap K A q⁻¹ * s = s * algebraMap K A q⁻¹ := Algebra.commutes q⁻¹ s
    have hcomm2 : s * algebraMap K A q = algebraMap K A q * s := (Algebra.commutes q s).symm
    calc
      (s + algebraMap K A q⁻¹) * (-s + algebraMap K A q)
          = -(s * s) + s * algebraMap K A q - algebraMap K A q⁻¹ * s +
              algebraMap K A q⁻¹ * algebraMap K A q := by noncomm_ring
      _ = -((q - q⁻¹) • s + 1) + (q - q⁻¹) • s + 1 := by
            rw [hquad, hcomm2, ← Algebra.smul_def, ← Algebra.smul_def, add_sub_assoc, ← sub_smul,
              ← map_mul, inv_mul_cancel₀ hq0, map_one]
      _ = 0 := by abel
  rw [hprod, smul_zero]

/-- Idempotency in `H_2(q)`: `h2IdemSym q s * h2IdemSym q s = h2IdemSym q s`. -/
theorem h2IdemSym_idem {A : Type*} [Ring A] [Algebra K A]
    (q : K) (hq0 : q ≠ 0) (hq_add : q + q⁻¹ ≠ 0)
    (s : A) (hquad : s * s = (q - q⁻¹) • s + 1) :
    h2IdemSym q s * h2IdemSym q s = h2IdemSym q s := by
  have h1 := congrArg (fun x => h2IdemSym q s * x) (h2Idem_add_eq_one q hq_add s)
  dsimp only at h1
  rw [mul_add, h2IdemSym_mul_h2IdemAnti q hq0 s hquad, add_zero, mul_one] at h1
  exact h1

/-- Under the transposing involution `s ↦ -s⁻¹ = -(s - (q - q⁻¹) • 1)` at fixed `q`,
`h2IdemSym` maps to `h2IdemAnti` (`(2) ↔ (1, 1)`), whereas under simultaneous inversion
`s ↦ s - (q - q⁻¹) • 1` and `q ↦ q⁻¹`, `h2IdemSym` is fixed. -/
theorem h2Idem_transpose_and_bar {A : Type*} [Ring A] [Algebra K A]
    (q : K) (s : A) :
    h2IdemSym q (-(s - algebraMap K A (q - q⁻¹))) = h2IdemAnti q s ∧
      h2IdemSym q⁻¹ (s - algebraMap K A (q - q⁻¹)) = h2IdemSym q s := by
  constructor
  · unfold h2IdemSym h2IdemAnti
    congr 1
    rw [map_sub]
    abel
  · unfold h2IdemSym
    rw [inv_inv, add_comm q⁻¹ q]
    congr 1
    rw [map_sub]
    abel

/-- Enumeration of the four standard Young tableaux of size `3`:
`tab3` of shape `(3)`, `tab21a` and `tab21b` of self-conjugate shape `(2, 1)`, and `tab111`
of shape `(1, 1, 1)`. -/
inductive H3Tab where
  | tab3
  | tab21a
  | tab21b
  | tab111
  deriving DecidableEq, Fintype

/-- Partition shapes of size `3`. -/
inductive H3Shape where
  | sh3
  | sh21
  | sh111
  deriving DecidableEq, Fintype

/-- Shape map on `H3Tab`. -/
def h3ShapeOf : H3Tab → H3Shape
  | .tab3 => .sh3
  | .tab21a => .sh21
  | .tab21b => .sh21
  | .tab111 => .sh111

/-- Tableau transposition on `H3Tab`: swaps `tab3 ↔ tab111` and `tab21a ↔ tab21b`. -/
def h3ConjTab : H3Tab ≃ H3Tab where
  toFun
    | .tab3 => .tab111
    | .tab21a => .tab21b
    | .tab21b => .tab21a
    | .tab111 => .tab3
  invFun
    | .tab3 => .tab111
    | .tab21a => .tab21b
    | .tab21b => .tab21a
    | .tab111 => .tab3
  left_inv T := by cases T <;> rfl
  right_inv T := by cases T <;> rfl

/-- Partition transposition on `H3Shape`: swaps `(3) ↔ (1, 1, 1)` and fixes `(2, 1)`. -/
def h3ConjShape : H3Shape ≃ H3Shape where
  toFun
    | .sh3 => .sh111
    | .sh21 => .sh21
    | .sh111 => .sh3
  invFun
    | .sh3 => .sh111
    | .sh21 => .sh21
    | .sh111 => .sh3
  left_inv s := by cases s <;> rfl
  right_inv s := by cases s <;> rfl

/-- Multiplicative `q`-content tuples `(c_T(1), c_T(2), c_T(3))` for the four SYTs of `H_3(q)`. -/
def h3QContent {R : Type*} [CommRing R] (q : Rˣ) : H3Tab → Fin 3 → R
  | .tab3, 0 => qContent 0 0 q
  | .tab3, 1 => qContent 0 1 q
  | .tab3, 2 => qContent 0 2 q
  | .tab21a, 0 => qContent 0 0 q
  | .tab21a, 1 => qContent 0 1 q
  | .tab21a, 2 => qContent 1 0 q
  | .tab21b, 0 => qContent 0 0 q
  | .tab21b, 1 => qContent 1 0 q
  | .tab21b, 2 => qContent 0 1 q
  | .tab111, 0 => qContent 0 0 q
  | .tab111, 1 => qContent 1 0 q
  | .tab111, 2 => qContent 2 0 q

/-- Tableau transposition inverts every `H_3(q)` box content:
`h3QContent q (h3ConjTab T) k = h3QContent q⁻¹ T k`. -/
theorem h3QContent_conjTab_eq_inv {R : Type*} [CommRing R] (q : Rˣ) (T : H3Tab) (k : Fin 3) :
    h3QContent q (h3ConjTab T) k = h3QContent q⁻¹ T k := by
  fin_cases k <;> cases T <;> exact qContent_transpose_eq_inv _ _ q

/-- At any `q : Kˣ` with `q ^ 4 ≠ 1` and `q ^ 6 ≠ 1`, the four `H_3(q)` content tuples
pairwise separate `H3Tab`. -/
theorem h3QContent_separates (q : Kˣ) (hq4 : (q : K) ^ 4 ≠ 1) (hq6 : (q : K) ^ 6 ≠ 1) :
    ∀ T T' : H3Tab, T ≠ T' → ∃ k : Fin 3, h3QContent q T k ≠ h3QContent q T' k := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hq2_ne_inv : qContent 0 1 q ≠ qContent 1 0 q := by
    unfold qContent
    intro h
    apply hq4
    have h1 : (q : K) ^ (2 : ℤ) = (q : K) ^ (-2 : ℤ) := by
      simpa using h
    rw [zpow_ofNat, zpow_neg, zpow_ofNat] at h1
    have h2 := congrArg (fun x => x * (q : K) ^ 2) h1
    dsimp at h2
    rw [inv_mul_cancel₀ (pow_ne_zero 2 hq0)] at h2
    linear_combination h2
  have hq4_ne_inv2 : qContent 0 2 q ≠ qContent 1 0 q := by
    unfold qContent
    intro h
    apply hq6
    have h1 : (q : K) ^ (4 : ℤ) = (q : K) ^ (-2 : ℤ) := by
      simpa using h
    rw [zpow_ofNat, zpow_neg, zpow_ofNat] at h1
    have h2 := congrArg (fun x => x * (q : K) ^ 2) h1
    dsimp at h2
    rw [inv_mul_cancel₀ (pow_ne_zero 2 hq0)] at h2
    linear_combination h2
  have hqinv4_ne_2 : qContent 2 0 q ≠ qContent 0 1 q := by
    unfold qContent
    intro h
    apply hq6
    have h1 : (q : K) ^ (-4 : ℤ) = (q : K) ^ (2 : ℤ) := by
      simpa using h
    rw [zpow_neg, zpow_ofNat, zpow_ofNat] at h1
    have h2 := congrArg (fun x => (q : K) ^ 4 * x) h1
    dsimp at h2
    rw [mul_inv_cancel₀ (pow_ne_zero 4 hq0)] at h2
    linear_combination -h2
  intro T T' hne
  cases T <;> cases T'
  · exact absurd rfl hne
  · exact ⟨2, hq4_ne_inv2⟩
  · exact ⟨1, hq2_ne_inv⟩
  · exact ⟨1, hq2_ne_inv⟩
  · exact ⟨2, Ne.symm hq4_ne_inv2⟩
  · exact absurd rfl hne
  · exact ⟨1, hq2_ne_inv⟩
  · exact ⟨1, hq2_ne_inv⟩
  · exact ⟨1, Ne.symm hq2_ne_inv⟩
  · exact ⟨1, Ne.symm hq2_ne_inv⟩
  · exact absurd rfl hne
  · exact ⟨2, Ne.symm hqinv4_ne_2⟩
  · exact ⟨1, Ne.symm hq2_ne_inv⟩
  · exact ⟨1, Ne.symm hq2_ne_inv⟩
  · exact ⟨2, hqinv4_ne_2⟩
  · exact absurd rfl hne

end ConcreteH2AndH3

end QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents
