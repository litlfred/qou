import QOU.BraidKnot.ExplicitCentralIdempotentGeneral
import QOU.SchurWeyl.HeckeProductInjective

/-!
# The involution of `conj:explicit-central-idempotent` (owner ruling, option C; bean `qou-2150`)

The conjecture's cross-checks 3–4 use an involution `*` that the block never defines. On
2026-11-20 the owner chose to name two involutions separately:

* **bar** (`σ_i ↦ σ_i⁻¹`, `q ↦ q⁻¹`, antilinear) — the mirror image. It is the symmetry of the
  convention-D mass trace (`markov_bar_equivariant_zD`), and non-abelian Stokes path reversal is bar
  composed with word reversal.
* **#** (`σ_i ↦ −σ_i⁻¹`, `q` fixed) — the sign twist that pairs `λ` with `λ'`.

This file proves the bar half for every `n`:

* `IsBar.fixes_proj`, `IsBar.fixes_centralIdem` — any bar involution (`IsBar`) fixes every
  Murphy–Lagrange projector `π_T` and every `e_λ`, chiral or self-conjugate. So cross-check 3
  holds for all `λ`, and cross-check 4 fails for bar at every `n` (`e_λ ≠ e_λ'` for `λ ≠ λ'`,
  `centralIdem_orth` + `centralIdem_ne_zero`).

Route: `IsBar.map_qJM` gives `φ(L_k) = L_k⁻¹`; the bar image of the `.md` formula is then the
Lagrange product in `L_k⁻¹` with targets `q^{−2d}` (`IsBar.map_mulProj`); the seminormal
representation sends `L_k⁻¹` to `diag(q^{−2c})` (`seminormalRep_qJMInv`), so that product is the
matrix unit `E^λ_{TT}` (`heckeProduct_lagrInv`), hence equal to `π_T`.

**Scope.** `IsBar` is a hypothesis: the file does not construct a bar involution (that needs a
field automorphism with `q ↦ q⁻¹`, e.g. on `ℚ(q)`). The statements are about every map with the
stated properties. The word-reversal half of Stokes reversal is not formalised here; the probe
`computations/probes/central_idempotent_involution_probe.py` checks it at `n ≤ 4`. The `#` half
needs a transpose map on standard tableaux and is not in this file.
-/

namespace QOU.BraidKnot.CentralIdempotentInvolution

open QOU.SchurWeyl QOU.SchurWeyl.JMProjector QOU.SchurWeyl.TableauCells
open QOU.BraidKnot.ExplicitCentralIdempotentGeneral
open QOU.SchurWeyl.SeminormalRep QOU.SchurWeyl.Seminormal

variable {K : Type*} [Field K]

/-! ## A Lagrange product in any diagonal-acting family -/

/-- `∏_{k ≤ n} ∏_{d ≠ c k, |d| ≤ n} (M_k − g d)/(g (c k) − g d)` in an algebra `A`. -/
noncomputable def lagr {A : Type*} [Ring A] [Algebra K A] (n : ℕ) (M : ℕ → A) (g : ℤ → K)
    (c : ℕ → ℤ) : A :=
  ((List.range (n + 1)).map (fun k =>
    (((contentRange n).filter (fun d => d ≠ c k)).map
      (fun d => (g (c k) - g d)⁻¹ • (M k - algebraMap K A (g d)))).prod)).prod

/-- Its scalar on a diagonal entry where `M_k` has eigenvalue `f (e k)`. -/
noncomputable def lagrVal (n : ℕ) (f g : ℤ → K) (c e : ℕ → ℤ) : K :=
  ((List.range (n + 1)).map (fun k =>
    (((contentRange n).filter (fun d => d ≠ c k)).map
      (fun d => (g (c k) - g d)⁻¹ * (f (e k) - g d))).prod)).prod

theorem map_lagr {A B : Type*} [Ring A] [Algebra K A] [Ring B] [Algebra K B] (φ : A →ₐ[K] B)
    (n : ℕ) (M : ℕ → A) (g : ℤ → K) (c : ℕ → ℤ) :
    φ (lagr n M g c) = lagr n (fun k => φ (M k)) g c := by
  simp only [lagr, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun k _ => ?_)
  simp only [Function.comp_apply, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun d _ => ?_)
  simp only [Function.comp_apply, map_smul, map_sub, AlgHom.commutes]

theorem lagr_diagonal {m : Type*} [Fintype m] [DecidableEq m] (n : ℕ) (f g : ℤ → K)
    (c : ℕ → ℤ) (e : m → ℕ → ℤ) (M : ℕ → Matrix m m K)
    (hM : ∀ k ∈ List.range (n + 1), M k = Matrix.diagonal (fun S => f (e S k))) :
    lagr n M g c = Matrix.diagonal (fun S => lagrVal n f g c (e S)) := by
  unfold lagr lagrVal
  have hY : ∀ k ∈ List.range (n + 1), ∀ d : ℤ,
      (g (c k) - g d)⁻¹ • (M k - algebraMap K (Matrix m m K) (g d))
      = Matrix.diagonal (fun S => (g (c k) - g d)⁻¹ * (f (e S k) - g d)) := by
    intro k hk d
    rw [hM k hk]
    ext S U
    by_cases h : S = U
    · subst h; simp [Matrix.algebraMap_eq_diagonal]
    · simp [Matrix.algebraMap_eq_diagonal, Matrix.diagonal_apply_ne _ h]
  rw [List.map_congr_left (fun k hk => by
    rw [List.map_congr_left (fun d _ => hY k hk d), list_prod_diagonal])]
  rw [list_prod_diagonal]

theorem lagrVal_self (n : ℕ) (g : ℤ → K) (hinj : Set.InjOn g {d | d ∈ contentRange n})
    (c : ℕ → ℤ) (hc : ∀ k ∈ Finset.range (n + 1), c k ∈ contentRange n) :
    lagrVal n g g c c = 1 := by
  unfold lagrVal
  refine List.prod_eq_one (fun x hx => ?_)
  obtain ⟨k, hk, rfl⟩ := List.mem_map.mp hx
  refine List.prod_eq_one (fun y hy => ?_)
  obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hy
  rw [List.mem_filter] at hd
  have hdc : d ≠ c k := by simpa using hd.2
  have hne : g (c k) - g d ≠ 0 := by
    refine sub_ne_zero.mpr (fun h => hdc (hinj ?_ hd.1 h).symm)
    exact hc k (by simpa [Finset.mem_range, List.mem_range] using hk)
  exact inv_mul_cancel₀ hne

theorem lagrVal_eq_zero (n : ℕ) (f g : ℤ → K) (c e : ℕ → ℤ) (r : ℤ → ℤ)
    (hfg : ∀ x, f x = g (r x))
    (he : ∀ k ∈ Finset.range (n + 1), r (e k) ∈ contentRange n)
    {k : ℕ} (hk : k ∈ Finset.range (n + 1)) (hne : r (e k) ≠ c k) :
    lagrVal n f g c e = 0 := by
  unfold lagrVal
  refine List.prod_eq_zero (List.mem_map.mpr ⟨k, by simpa using hk, ?_⟩)
  refine List.prod_eq_zero (List.mem_map.mpr ⟨r (e k), ?_, by simp [hfg]⟩)
  rw [List.mem_filter]
  exact ⟨he k hk, by simpa using hne⟩

/-! ## The bar involution fixes every `π_T` and every `e_λ` -/

section Bar

variable [CharZero K] (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- `d ↦ q^{−2d}`, the eigenvalue of `L_k⁻¹` on a box of content `d`. -/
noncomputable def gInv (d : ℤ) : K := q ^ (-(2 * d))

omit [CharZero K] in
include hq0 hq2 in
theorem gInv_injective : Function.Injective (gInv q) := by
  intro a b h
  have := zpow_injective_of_not_root_of_unity hq0 hq2 h
  omega

omit [CharZero K] in
include hq0 hq2 in
theorem seminormalRep_qJMInv_diag {μ : YoungDiagram} (hN : μ.cells.card = n + 1) (k : ℕ)
    (hk : k ≤ n) :
    seminormalRep q hq0 hq2 n hN (qJMInv K q q⁻¹ n k)
      = Matrix.diagonal (fun S => gInv q (contentVec S k)) := by
  rw [seminormalRep_qJMInv q hq0 hq2 n hN k hk]
  rfl

include hq0 hq2 in
/-- The Lagrange product in the inverse Murphy elements is the matrix unit `E^λ_{TT}`. -/
theorem heckeProduct_lagrInv (lam : Nat.Partition (n + 1))
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    heckeProduct q hq0 hq2 n (lagr n (qJMInv K q q⁻¹ n) (gInv q) (contentVec T))
      = Pi.single lam (Matrix.single T T 1) := by
  classical
  have hinj : Set.InjOn (gInv q) {d | d ∈ contentRange n} := (gInv_injective q hq0 hq2).injOn
  funext mu
  rw [heckeProduct_apply, map_lagr]
  rw [lagr_diagonal n (gInv q) (gInv q) (contentVec T) (fun S => contentVec S) _
    (fun k hk => seminormalRep_qJMInv_diag q hq0 hq2 n (partitionShape_card_succ mu) k
      (by rw [List.mem_range] at hk; omega))]
  ext S U
  by_cases hmu : mu = lam
  · subst hmu
    rw [Pi.single_eq_same]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      by_cases hST : S = T
      · subst hST
        rw [lagrVal_self n (gInv q) hinj _
          (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)]
        exact (Matrix.single_apply_same _ _ _).symm
      · have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
          by_contra hcon
          push_neg at hcon
          exact hST (eq_of_contentVec_eq (partitionShape_card_succ mu) S T hcon)
        obtain ⟨k, hk, hne⟩ := this
        rw [lagrVal_eq_zero n (gInv q) (gInv q) (contentVec T) (contentVec S) id (fun _ => rfl)
          (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk) hk hne]
        exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hST h.1.symm)).symm
    · rw [Matrix.diagonal_apply_ne _ hSU]
      exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hSU (h.1.symm.trans h.2))).symm
  · rw [Pi.single_eq_of_ne hmu]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
        by_contra hcon
        push_neg at hcon
        exact hmu (QOU.Mathlib.partitionShape_injective
          (shape_eq_of_contentVec_eq (partitionShape_card_succ mu) (partitionShape_card_succ lam)
            S T hcon))
      obtain ⟨k, hk, hne⟩ := this
      rw [lagrVal_eq_zero n (gInv q) (gInv q) (contentVec T) (contentVec S) id (fun _ => rfl)
        (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk) hk hne]
      rfl
    · rw [Matrix.diagonal_apply_ne _ hSU]
      rfl

include hq0 hq2 in
theorem lagrInv_eq_proj (lam : Nat.Partition (n + 1))
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    lagr n (qJMInv K q q⁻¹ n) (gInv q) (contentVec T) = proj q n T := by
  apply heckeProduct_injective q hq0 hq2 n
  rw [heckeProduct_lagrInv q hq0 hq2 n lam T, proj_eq_symm q hq0 hq2 n]
  exact ((heckeWedderburn q hq0 hq2 n).apply_symm_apply _).symm

/-- The hypotheses defining the bar involution of `H_{n+1}(q)`: a ring endomorphism `φ` that is
`τ`-semilinear on scalars, where `τ` is a ring endomorphism of `K` with `τ q = q⁻¹`, and sends each
generator `σ_i` to its inverse. (The `.md`'s `*`: `σ_i ↦ σ_i⁻¹`, `q ↦ q⁻¹`, extended antilinearly.) -/
structure IsBar (τ : K →+* K) (φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n) : Prop where
  tau_q : τ q = q⁻¹
  map_scalar : ∀ a : K, φ (algebraMap K _ a) = algebraMap K _ (τ a)
  map_sigma : ∀ i : Fin n, φ (Hecke.σ K q q⁻¹ n i) = Hecke.σInv K q q⁻¹ n i

omit [CharZero K] in
theorem IsBar.map_qJM {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) : ∀ k, φ (qJM K q q⁻¹ n k) = qJMInv K q q⁻¹ n k
  | 0 => by rw [qJM_zero, qJMInv_zero, map_one]
  | k + 1 => by
      by_cases hk : k < n
      · rw [qJM_succ K q q⁻¹ n hk, qJMInv_succ K q q⁻¹ n hk, map_mul, map_mul,
          hφ.map_qJM k, hφ.map_sigma]
      · have h1 : qJM K q q⁻¹ n (k + 1) = qJM K q q⁻¹ n k := by simp only [qJM, dif_neg hk]
        have h2 : qJMInv K q q⁻¹ n (k + 1) = qJMInv K q q⁻¹ n k := by
          simp only [qJMInv, dif_neg hk]
        rw [h1, h2, hφ.map_qJM k]

omit [CharZero K] in
theorem IsBar.map_smul {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) (a : K) (x : Hecke K q q⁻¹ n) : φ (a • x) = τ a • φ x := by
  rw [Algebra.smul_def, map_mul, hφ.map_scalar, ← Algebra.smul_def]

omit [CharZero K] in
theorem IsBar.tau_zpow {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) (d : ℤ) : τ (q ^ (2 * d)) = gInv q d := by
  rw [map_zpow₀, hφ.tau_q, inv_zpow', gInv]

omit [CharZero K] in
/-- The bar image of the `.md`'s projector is the Lagrange product in `L_k⁻¹`. -/
theorem IsBar.map_mulProj {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    φ (mulProj q n T) = lagr n (qJMInv K q q⁻¹ n) (gInv q) (contentVec T) := by
  unfold mulProj mulFactor lagr
  rw [map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun k _ => ?_)
  rw [Function.comp_apply, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun d _ => ?_)
  rw [Function.comp_apply, hφ.map_smul, map_sub, hφ.map_qJM, hφ.map_scalar, map_inv₀, map_sub,
    hφ.tau_zpow, hφ.tau_zpow]

include hq0 hq2 in
/-- **The bar involution fixes every Murphy–Lagrange projector `π_T`.** -/
theorem IsBar.fixes_proj {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    φ (proj q n T) = proj q n T := by
  rw [← mulProj_eq_proj q hq0 hq2 n T, hφ.map_mulProj, lagrInv_eq_proj q hq0 hq2 n lam T,
    mulProj_eq_proj q hq0 hq2 n T]

include hq0 hq2 in
/-- **Cross-check 3, strengthened: the bar involution fixes EVERY `e_λ`**, self-conjugate or
not. So bar does not pair `λ` with `λ'` (cross-check 4 fails for bar, at every `n`). -/
theorem IsBar.fixes_centralIdem {τ : K →+* K} {φ : Hecke K q q⁻¹ n →+* Hecke K q q⁻¹ n}
    (hφ : IsBar q n τ φ) (lam : Nat.Partition (n + 1)) :
    φ (centralIdem q n lam) = centralIdem q n lam := by
  unfold centralIdem
  rw [map_sum]
  exact Finset.sum_congr rfl (fun T _ => hφ.fixes_proj q hq0 hq2 n T)

end Bar

end QOU.BraidKnot.CentralIdempotentInvolution

