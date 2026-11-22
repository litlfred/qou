import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.Data.Matrix.Basic
import Mathlib.RingTheory.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Polynomial

/-!
# Bridge A, step A2 — the Lagrangian's connection and the KZ connection

Audit `qou-derivation-chain/derivation-chain-audit-2026-11-15.md`, §2.5 (gap G2.1) and §8
step 8; bean `qou-d0qq`.

The categorical Lagrangian (`def:categorical-lagrangian`) is built from the Dirac operator

  `𝒟_∇ = q⁻¹ ∇ + ℏ_q · ι_ξ ∇`,   `ℏ_q = 1 − q⁻¹`   (`def:categorical-dirac-operator-exists`).

Step A2 asks whether `∇` can be identified with the Knizhnik–Zamolodchikov connection
`∇_KZ = d − ℏ Σ_{i<j} Ω_{ij} d log(z_i − z_j)` on `Conf_n` with fibre `V^{⊗n}`. This file proves
the algebraic parts of that identification and isolates the one analytic input.

## Part I — `𝒟` is an invertible reweighting of `∇` (`reweight`, `dirac_*`)

Fix a point of the base, its tangent space `T`, a covector `η` and a vector `ξ` with `η ξ = 1`
(on `Conf_n`: `ξ` is the Euler field, whose rotation part is the Reeb field of the link
`S^{2N−1}`; `η` is any 1-form dual to it). A covariant derivative at the point is a linear map
`φ : T → F` into the fibre. `𝒟` sends `φ` to `P φ = q⁻¹ φ + ℏ_q · η ⊗ φ(ξ)`. We prove:

* `reweight_reeb`: the Reeb component is scaled by `a + b`; for the Dirac weights `a + b = 1`, so
  `(𝒟 s)(ξ) = (∇ s)(ξ)` (`dirac_reeb`), and transverse components are scaled by `q⁻¹`.
* `reweight_comp`, `dirac_left_inverse`: `P` is invertible with inverse weights `(q, 1 − q)`.
* `dirac_eq_zero_iff`: `𝒟 s = 0 ↔ ∇ s = 0` at every point. **`𝒟` and `∇` have the same flat
  sections**, so any identification of `∇` with KZ (flat sections, monodromy) passes to `𝒟`.
* `reweight_sum_eq_one_of_reeb`: `q⁻¹ + ℏ_q = 1` is exactly the condition that `𝒟` leaves the
  Reeb component unchanged. This is the algebraic content of the "convex pair".

## Part II — an Arnold-class form is determined by its residues (`arnold_*`)

For residues `M : Fin n → Fin n → A` (`A` any `K`-algebra, e.g. `End(V^{⊗n})`) the form
`ω_M = Σ_m f_m dz_m`, `f_m(z) = Σ_j (z_m − z_j)⁻¹ M_{mj}`, equals `½ Σ_{i,j} M_{ij} d log(z_i − z_j)`
when `M` is symmetric (`arnoldForm_eq_half_dlog`), i.e. it is the sibling file's
`Σ_{i<j} ω_{ij} M_{ij}`. `arnoldCoeff_injective` proves that the coefficients `f_m`, as functions on
`Conf_n`, determine every off-diagonal `M_{mj}`. The proof is a partial-fraction uniqueness
(`partialFraction_unique`, over any infinite field) plus separation by linear functionals.

## Part III — the identification, and gauge (`eq_kz_iff`, `const_gauge_iff`)

* `eq_kz_iff`: an Arnold-class form equals `ω_KZ = ℏ Σ Ω_{ij} d log(z_i − z_j)` on all of
  `Conf_n` **iff** its residues are `ℏ Ω_{ij}`.
* `const_gauge_iff`: a constant gauge transformation `g` carries `ω_M` to `ω_N` iff
  `N_{ij} = g M_{ij} g⁻¹` for all `i ≠ j`. So "KZ up to constant gauge" means "residues
  simultaneously conjugate to the Casimirs".
* `arnold_euler`: the Euler contraction is the constant `½ Σ_{i≠j} M_{ij}`. With Part I,
  `(𝒟 s)(E) = E·s − ½ Σ_{i≠j} M_{ij} s`: the Reeb part of the Dirac operator on the KZ sector is
  the total pair Casimir, unweighted by `q`.

## Part IV — the analytic input, isolated (`RiemannHilbertInput`)

Outside the Arnold class the residues are not enough. A non-constant gauge leaves the class,
so "KZ up to gauge" is a statement about a larger class, and there the local data (residues up
to conjugacy) do not in general fix the gauge class: non-rigid Fuchsian systems with the same
local monodromy classes need not be gauge equivalent (Katz). Whether residues equal to `Ω_{ij}`
in a fixed trivialisation, on every diagonal, already force the gauge class is not settled here. What does determine the gauge class of a regular-singular flat
connection is its monodromy: that is the Riemann–Hilbert correspondence (Deligne). It is the one
analytic proposition here and it enters only as the hypothesis structure `RiemannHilbertInput`;
`gauge_equiv_kz_iff_monodromy` is the consequence used downstream.

## Parts V–VI — deriving the postulates

* `schurWeyl_two` (P3): a pair residue on `K^N ⊗ K^N` commuting with the diagonal `𝔤𝔩_N` is
  `α + β·P`. With permutation symmetry, `arnoldForm_split` writes the form as an abelian part plus
  the KZ form with `ℏ = β`.
* `eval_const_of_dilation_invariant` (P2, key step): a polynomial residue invariant under the
  Euler dilation is constant.

## What this does not do

It does not construct a connection on `Conf_n` from the corpus. The corpus's `∇` is an abstract
connection on the algebra `A` of one universe; there is no `n`-body base. Three postulates are
needed to reach KZ, and none is derived here: (P1) the `n`-body sector is the trivial bundle
`V^{⊗n}` over `Conf_n`; (P2) its connection form is in the Arnold class (two-body locality with
constant residues); (P3) the pair residue is `ℏ Ω_{ij}`. Given P1–P3, `∇ = ∇_KZ` on the nose
(`eq_kz_iff`), it is flat for every `n` (sibling `InfinitesimalPureBraid.casimir_curvature_zero`),
and `𝒟` has the same flat sections (`dirac_eq_zero_iff`).

Base ring §7c: Part I over any field; Parts II–III over any infinite field with `2 ≠ 0` where a
half appears. Nothing archimedean except the hypothesis structure of Part IV.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987), §1.1.
-- Ref: [deligne1970] Deligne, Équations différentielles à points singuliers réguliers, LNM 163.
-- Ref: [arnold1969] Arnold, The cohomology ring of the colored braid group, Mat. Zametki 5.
-/

namespace QOU.Mass.LagrangianKZ

/-! ## Part I — the Dirac operator as a reweighting -/

section Dirac

variable {K : Type*} [Field K] {T F : Type*} [AddCommGroup T] [Module K T]
  [AddCommGroup F] [Module K F]

/-- The reweighting `P_{a,b}(φ)(u) = a φ(u) + b η(u) φ(ξ)` of a fibre-valued covector `φ`. -/
def reweight (a b : K) (η : T →ₗ[K] K) (ξ : T) (φ : T →ₗ[K] F) : T →ₗ[K] F :=
  a • φ + b • η.smulRight (φ ξ)

@[simp] theorem reweight_apply (a b : K) (η : T →ₗ[K] K) (ξ : T) (φ : T →ₗ[K] F) (u : T) :
    reweight a b η ξ φ u = a • φ u + b • (η u • φ ξ) := by
  simp [reweight]

/-- The Reeb component is scaled by `a + b`. -/
theorem reweight_reeb (a b : K) {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1) (φ : T →ₗ[K] F) :
    reweight a b η ξ φ ξ = (a + b) • φ ξ := by
  simp [h, add_smul]

/-- Transverse components (`η u = 0`) are scaled by `a`. -/
theorem reweight_transverse (a b : K) {η : T →ₗ[K] K} (ξ : T) (φ : T →ₗ[K] F) {u : T}
    (hu : η u = 0) : reweight a b η ξ φ u = a • φ u := by
  simp [hu]

/-- Composition of reweightings. -/
theorem reweight_comp (a b a' b' : K) {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1)
    (φ : T →ₗ[K] F) :
    reweight a' b' η ξ (reweight a b η ξ φ) = reweight (a' * a) (a' * b + b' * (a + b)) η ξ φ := by
  ext u
  simp only [reweight_apply, h, one_smul]
  module

theorem reweight_one_zero (η : T →ₗ[K] K) (ξ : T) (φ : T →ₗ[K] F) :
    reweight (1 : K) 0 η ξ φ = φ := by
  ext u; simp

/-- `P_{a,b}` is injective when `a ≠ 0` and `a + b ≠ 0`. -/
theorem reweight_eq_zero_iff {a b : K} (ha : a ≠ 0) (hab : a + b ≠ 0) {η : T →ₗ[K] K} {ξ : T}
    (h : η ξ = 1) (φ : T →ₗ[K] F) : reweight a b η ξ φ = 0 ↔ φ = 0 := by
  constructor
  · intro h0
    have key := reweight_comp a b a⁻¹ (-(a⁻¹ * b) / (a + b)) h φ
    rw [h0] at key
    have e1 : a⁻¹ * a = 1 := inv_mul_cancel₀ ha
    have e2 : a⁻¹ * b + -(a⁻¹ * b) / (a + b) * (a + b) = 0 := by
      rw [div_mul_cancel₀ _ hab]; ring
    rw [e1, e2, reweight_one_zero] at key
    rw [← key]; ext u; simp
  · rintro rfl; ext u; simp

/-- If some `φ` has a nonzero Reeb component and `P_{a,b}` preserves Reeb components, then
`a + b = 1`: the convex-pair condition is forced. -/
theorem reweight_sum_eq_one_of_reeb {a b : K} {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1)
    {φ : T →ₗ[K] F} (hφ : φ ξ ≠ 0) (hpres : reweight a b η ξ φ ξ = φ ξ) : a + b = 1 := by
  rw [reweight_reeb a b h] at hpres
  have : (a + b - 1) • φ ξ = 0 := by rw [sub_smul, hpres, one_smul, sub_self]
  exact sub_eq_zero.mp ((smul_eq_zero.mp this).resolve_right hφ)

/-- The reweighting acts by scalars on the fibre, so it commutes with every fibre map `f`.
In particular it commutes with the total `𝔰𝔩₂` (isospin): `𝒟` cannot split what `∇` does not. -/
theorem reweight_comp_fibre {G : Type*} [AddCommGroup G] [Module K G] (a b : K)
    (η : T →ₗ[K] K) (ξ : T) (f : F →ₗ[K] G) (φ : T →ₗ[K] F) :
    reweight a b η ξ (f ∘ₗ φ) = f ∘ₗ reweight a b η ξ φ := by
  ext u; simp

/-- The Dirac reweighting: weights `q⁻¹` and `ℏ_q = 1 − q⁻¹`. -/
def dirac (q : K) (η : T →ₗ[K] K) (ξ : T) (φ : T →ₗ[K] F) : T →ₗ[K] F :=
  reweight q⁻¹ (1 - q⁻¹) η ξ φ

/-- `(𝒟 s)(ξ) = (∇ s)(ξ)`: the Dirac operator does not reweight the Reeb direction. -/
theorem dirac_reeb (q : K) {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1) (φ : T →ₗ[K] F) :
    dirac q η ξ φ ξ = φ ξ := by
  rw [dirac, reweight_reeb _ _ h]; simp

/-- Transverse directions are scaled by `q⁻¹`. -/
theorem dirac_transverse (q : K) {η : T →ₗ[K] K} (ξ : T) (φ : T →ₗ[K] F) {u : T}
    (hu : η u = 0) : dirac q η ξ φ u = q⁻¹ • φ u :=
  reweight_transverse _ _ ξ φ hu

/-- The inverse of `𝒟`'s reweighting has weights `(q, 1 − q)`. -/
theorem dirac_left_inverse {q : K} (hq : q ≠ 0) {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1)
    (φ : T →ₗ[K] F) : reweight q (1 - q) η ξ (dirac q η ξ φ) = φ := by
  rw [dirac, reweight_comp _ _ _ _ h]
  have e1 : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have e2 : q * (1 - q⁻¹) + (1 - q) * (q⁻¹ + (1 - q⁻¹)) = 0 := by
    rw [mul_sub, e1]; ring
  rw [e1, e2, reweight_one_zero]

/-- **`𝒟 s = 0 ↔ ∇ s = 0`** at every point: the Dirac operator and the connection have the
same flat sections. -/
theorem dirac_eq_zero_iff {q : K} (hq : q ≠ 0) {η : T →ₗ[K] K} {ξ : T} (h : η ξ = 1)
    (φ : T →ₗ[K] F) : dirac q η ξ φ = 0 ↔ φ = 0 :=
  reweight_eq_zero_iff (inv_ne_zero hq) (by simp) h φ

end Dirac

/-! ## Part II — partial fractions and the Arnold class -/

section PartialFraction

open Polynomial

variable {K : Type*} [Field K]

/-- **Partial-fraction uniqueness.** Over an infinite field, if `Σ_{j ∈ s} c_j / (t − p_j)`
vanishes for every `t` outside the finite set `p(s)`, and `p` is injective on `s`, then every
`c_j = 0`. -/
theorem partialFraction_unique [Infinite K] {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (p : ι → K) (hp : Set.InjOn p s) (c : ι → K)
    (h : ∀ t : K, (∀ j ∈ s, t ≠ p j) → ∑ j ∈ s, c j / (t - p j) = 0) :
    ∀ j ∈ s, c j = 0 := by
  classical
  set g : K[X] := ∑ j ∈ s, C (c j) * ∏ k ∈ s.erase j, (X - C (p k)) with hg
  have hg0 : g = 0 := by
    apply Polynomial.eq_zero_of_infinite_isRoot
    have hsub : ((s.image p : Finset K) : Set K)ᶜ ⊆ {t | g.IsRoot t} := by
      intro t ht
      have ht' : ∀ j ∈ s, t ≠ p j := by
        intro j hj e
        exact ht (Finset.mem_coe.mpr (Finset.mem_image.mpr ⟨j, hj, e.symm⟩))
      simp only [Set.mem_setOf_eq, IsRoot.def, hg, eval_finset_sum, eval_mul, eval_C,
        eval_prod, eval_sub, eval_X]
      have hne : ∀ j ∈ s, t - p j ≠ 0 := fun j hj => sub_ne_zero.mpr (ht' j hj)
      have hmul : ∑ j ∈ s, (∏ k ∈ s, (t - p k)) * (c j / (t - p j)) = 0 := by
        rw [← Finset.mul_sum, h t ht', mul_zero]
      refine (Finset.sum_congr rfl fun j hj => ?_).trans hmul
      rw [show ∏ k ∈ s, (t - p k) = (t - p j) * ∏ k ∈ s.erase j, (t - p k) from
        (Finset.mul_prod_erase s (fun k => t - p k) hj).symm]
      field_simp [hne j hj]
    exact ((s.image p).finite_toSet.infinite_compl).mono hsub
  intro j hj
  have hev := congrArg (Polynomial.eval (p j)) hg0
  simp only [hg, eval_finset_sum, eval_mul, eval_C, eval_prod, eval_sub, eval_X,
    eval_zero] at hev
  rw [Finset.sum_eq_single j] at hev
  · have hprod : ∏ k ∈ s.erase j, (p j - p k) ≠ 0 := by
      rw [Finset.prod_ne_zero_iff]
      intro k hk
      have hkj : k ≠ j := Finset.ne_of_mem_erase hk
      exact sub_ne_zero.mpr fun e => hkj (hp (Finset.mem_of_mem_erase hk) hj e.symm)
    exact (mul_eq_zero.mp hev).resolve_right hprod
  · intro i hi hij
    apply mul_eq_zero_of_right
    exact Finset.prod_eq_zero (Finset.mem_erase.mpr ⟨Ne.symm hij, hj⟩) (sub_self _)
  · intro hj'; exact absurd hj hj'

/-- Module-valued partial-fraction uniqueness, for a vector space `M`. -/
theorem partialFraction_unique_module [Infinite K] {M : Type*} [AddCommGroup M] [Module K M]
    {ι : Type*} [DecidableEq ι] (s : Finset ι) (p : ι → K) (hp : Set.InjOn p s) (c : ι → M)
    (h : ∀ t : K, (∀ j ∈ s, t ≠ p j) → ∑ j ∈ s, (t - p j)⁻¹ • c j = 0) :
    ∀ j ∈ s, c j = 0 := by
  intro j hj
  rw [← Module.forall_dual_apply_eq_zero_iff K]
  intro ℓ
  refine partialFraction_unique s p hp (fun i => ℓ (c i)) (fun t ht => ?_) j hj
  have := congrArg ℓ (h t ht)
  simpa [map_sum, div_eq_inv_mul] using this

end PartialFraction

section Arnold

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- The coefficient of `dz_m` in the Arnold-class form with residues `M`:
`f_m(z) = Σ_j (z_m − z_j)⁻¹ M_{mj}` (the `j = m` term is `0⁻¹ M_{mm} = 0`). -/
def arnoldCoeff (M : Fin n → Fin n → A) (z : Fin n → K) (m : Fin n) : A :=
  ∑ j, (z m - z j)⁻¹ • M m j

/-- The Arnold-class form `ω_M(z)(u) = Σ_m u_m f_m(z)`. -/
def arnoldForm (M : Fin n → Fin n → A) (z u : Fin n → K) : A :=
  ∑ m, u m • arnoldCoeff M z m

/-- For symmetric `M`, `ω_M = ½ Σ_{i,j} M_{ij} d log(z_i − z_j)`, the sibling file's
`Σ_{i<j} ω_{ij} M_{ij}`. -/
theorem arnoldForm_eq_half_dlog (h2 : (2 : K) ≠ 0) {M : Fin n → Fin n → A}
    (hM : ∀ i j, M i j = M j i) (z u : Fin n → K) :
    arnoldForm M z u = (2 : K)⁻¹ • ∑ i, ∑ j, ((u i - u j) / (z i - z j)) • M i j := by
  have hswap : ∑ i, ∑ j, (u j / (z i - z j)) • M i j =
      -∑ i, ∑ j, (u i / (z i - z j)) • M i j := by
    rw [Finset.sum_comm, ← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [hM j i, ← neg_sub (z i) (z j), div_neg, neg_smul]
  have hsplit : ∑ i, ∑ j, ((u i - u j) / (z i - z j)) • M i j
      = ∑ i, ∑ j, (u i / (z i - z j)) • M i j - ∑ i, ∑ j, (u j / (z i - z j)) • M i j := by
    rw [← Finset.sum_sub_distrib]; refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_sub_distrib]; refine Finset.sum_congr rfl fun j _ => ?_
    rw [sub_div, sub_smul]
  have hS : arnoldForm M z u = ∑ i, ∑ j, (u i / (z i - z j)) • M i j := by
    unfold arnoldForm arnoldCoeff
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.smul_sum]; refine Finset.sum_congr rfl fun j _ => ?_
    rw [smul_smul, div_eq_mul_inv]
  rw [hS, hsplit, hswap, sub_neg_eq_add, ← two_smul K, smul_smul, inv_mul_cancel₀ h2, one_smul]

/-- **Residues determine an Arnold-class form.** If `ω_M` and `ω_N` have the same
`dz_m`-coefficients at every configuration with distinct coordinates, then `M_{mj} = N_{mj}` for
all `m ≠ j`. -/
theorem arnoldCoeff_injective [Infinite K] {M N : Fin n → Fin n → A}
    (h : ∀ z : Fin n → K, Function.Injective z → ∀ m, arnoldCoeff M z m = arnoldCoeff N z m) :
    ∀ m j, m ≠ j → M m j = N m j := by
  classical
  intro m j hmj
  -- a base configuration with distinct coordinates
  let z0 : Fin n → K := fun i => Infinite.natEmbedding K (i : ℕ)
  have hz0 : Function.Injective z0 := fun a b hab =>
    Fin.ext ((Infinite.natEmbedding K).injective hab)
  have key : M m j - N m j = 0 := by
    refine partialFraction_unique_module (M := A) (Finset.univ.erase m) z0 hz0.injOn
      (fun i => M m i - N m i) (fun t ht => ?_) j
      (Finset.mem_erase.mpr ⟨Ne.symm hmj, Finset.mem_univ _⟩)
    -- move `z_m` to `t`
    let z : Fin n → K := Function.update z0 m t
    have hz : Function.Injective z := by
      intro a b hab
      by_contra hne
      by_cases ha : a = m
      · have hb : b ≠ m := fun hb => hne (ha.trans hb.symm)
        have : t = z0 b := by simpa [z, ha, Function.update_of_ne hb] using hab
        exact ht b (Finset.mem_erase.mpr ⟨hb, Finset.mem_univ _⟩) this
      · by_cases hb : b = m
        · have : z0 a = t := by simpa [z, hb, Function.update_of_ne ha] using hab
          exact ht a (Finset.mem_erase.mpr ⟨ha, Finset.mem_univ _⟩) this.symm
        · have : z0 a = z0 b := by
            simpa [z, Function.update_of_ne ha, Function.update_of_ne hb] using hab
          exact hne (hz0 this)
    have hzm := h z hz m
    simp only [arnoldCoeff] at hzm
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ m),
      ← Finset.add_sum_erase _ _ (Finset.mem_univ m)] at hzm
    simp only [sub_self, inv_zero, zero_smul, zero_add] at hzm
    have hmove : ∀ X : Fin n → Fin n → A,
        ∑ i ∈ Finset.univ.erase m, (z m - z i)⁻¹ • X m i =
          ∑ i ∈ Finset.univ.erase m, (t - z0 i)⁻¹ • X m i := fun X =>
      Finset.sum_congr rfl fun i hi => by
        simp [z, Function.update_of_ne (Finset.ne_of_mem_erase hi)]
    rw [hmove M, hmove N] at hzm
    simp only [smul_sub, Finset.sum_sub_distrib, hzm, sub_self]
  exact sub_eq_zero.mp key

/-- The KZ form with coupling `ℏ` and pair Casimirs `Ω`. -/
def kzForm (ℏ : K) (Ω : Fin n → Fin n → A) (z u : Fin n → K) : A :=
  arnoldForm (fun i j => ℏ • Ω i j) z u

theorem arnoldForm_congr_offDiag {M N : Fin n → Fin n → A} (h : ∀ i j, i ≠ j → M i j = N i j)
    (z u : Fin n → K) : arnoldForm M z u = arnoldForm N z u := by
  unfold arnoldForm arnoldCoeff
  refine Finset.sum_congr rfl fun m _ => congrArg (u m • ·) (Finset.sum_congr rfl fun j _ => ?_)
  by_cases hmj : m = j
  · subst hmj; simp
  · rw [h m j hmj]

/-- Coefficients of `dz_m` are read off the form by `u = e_m`. -/
theorem arnoldForm_single (M : Fin n → Fin n → A) (z : Fin n → K) (m : Fin n) :
    arnoldForm M z (Pi.single m 1) = arnoldCoeff M z m := by
  classical
  unfold arnoldForm
  rw [Finset.sum_eq_single m]
  · simp
  · intro b _ hb; simp [hb]
  · intro hm; exact absurd (Finset.mem_univ m) hm

/-- **Identification.** An Arnold-class form equals the KZ form on all of `Conf_n` iff its
off-diagonal residues are `ℏ Ω_{ij}`. -/
theorem eq_kz_iff [Infinite K] (ℏ : K) (Ω M : Fin n → Fin n → A) :
    (∀ z : Fin n → K, Function.Injective z → ∀ u, arnoldForm M z u = kzForm ℏ Ω z u) ↔
      ∀ i j, i ≠ j → M i j = ℏ • Ω i j := by
  constructor
  · intro h
    refine arnoldCoeff_injective (K := K) (N := fun i j => ℏ • Ω i j) fun z hz m => ?_
    rw [← arnoldForm_single, ← arnoldForm_single]
    exact h z hz _
  · intro h z _ u
    exact arnoldForm_congr_offDiag h z u

/-- A constant gauge transformation conjugates the residues. -/
theorem arnoldForm_conj (g : Aˣ) (M : Fin n → Fin n → A) (z u : Fin n → K) :
    (g : A) * arnoldForm M z u * ↑g⁻¹ = arnoldForm (fun i j => (g : A) * M i j * ↑g⁻¹) z u := by
  unfold arnoldForm arnoldCoeff
  simp only [Finset.mul_sum, Finset.sum_mul, mul_smul_comm, smul_mul_assoc]

/-- **KZ up to constant gauge.** `g` carries `ω_M` to `ω_N` on all of `Conf_n` iff
`N_{ij} = g M_{ij} g⁻¹` for every `i ≠ j`. -/
theorem const_gauge_iff [Infinite K] (g : Aˣ) (M N : Fin n → Fin n → A) :
    (∀ z : Fin n → K, Function.Injective z → ∀ u,
        (g : A) * arnoldForm M z u * ↑g⁻¹ = arnoldForm N z u) ↔
      ∀ i j, i ≠ j → N i j = (g : A) * M i j * ↑g⁻¹ := by
  simp only [arnoldForm_conj]
  constructor
  · intro h i j hij
    exact (arnoldCoeff_injective (K := K) (M := N) (N := fun i j => (g : A) * M i j * ↑g⁻¹)
      (fun z hz m => by
        rw [← arnoldForm_single, ← arnoldForm_single]; exact (h z hz _).symm) i j hij)
  · intro h z _ u
    exact (arnoldForm_congr_offDiag (fun i j hij => (h i j hij).symm) z u)

/-- **Euler contraction.** At a configuration with distinct coordinates, contracting with the
Euler field `E = Σ z_m ∂_m` gives the constant `½ Σ_{i ≠ j} M_{ij}` (symmetric `M`). -/
theorem arnold_euler (h2 : (2 : K) ≠ 0) {M : Fin n → Fin n → A} (hM : ∀ i j, M i j = M j i)
    {z : Fin n → K} (hz : Function.Injective z) :
    arnoldForm M z z = (2 : K)⁻¹ • ∑ i, ∑ j, (if i = j then (0 : A) else M i j) := by
  rw [arnoldForm_eq_half_dlog h2 hM]
  congr 1
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  by_cases hij : i = j
  · subst hij; simp
  · rw [if_neg hij, div_self (sub_ne_zero.mpr (hz.ne hij)), one_smul]

end Arnold


/-! ## Part V — deriving P3: the pair residue from equivariance (`schurWeyl_two`)

The corpus makes `∇` a morphism in `C` (`categorical-dirac-operator-exists-proof`), so its pair
residue `X ∈ End(V ⊗ V)` commutes with the symmetry. For `V = K^N` (the fundamental of `𝔤𝔩_N`)
we prove Schur–Weyl at `n = 2` directly: if `X` commutes with every coproduct
`E_{ab} ⊗ 1 + 1 ⊗ E_{ab}` then `X = α · 1 + β · P` with `P` the flip. Hence, with permutation
symmetry, every pair residue is `α + β s_{ij}` with the same `α, β` (`arnoldForm_split`): an
abelian part plus KZ with `ℏ = β`. Characteristic zero, `N ≥ 2`. -/

section SchurWeylTwo

variable {K : Type*} [Field K] {N : ℕ}

/-- The diagonal action of `E_{ab}` on `V ⊗ V`, `V = K^N`, as a matrix on `Fin N × Fin N`. -/
def coprodE (a b : Fin N) : Matrix (Fin N × Fin N) (Fin N × Fin N) K :=
  fun p q => (if p.1 = a ∧ q.1 = b ∧ p.2 = q.2 then 1 else 0) +
    (if p.1 = q.1 ∧ p.2 = a ∧ q.2 = b then 1 else 0)

/-- The flip `P : u ⊗ v ↦ v ⊗ u`. -/
def swapM : Matrix (Fin N × Fin N) (Fin N × Fin N) K :=
  fun p q => if p.1 = q.2 ∧ p.2 = q.1 then 1 else 0

theorem coprod_rel {X : Matrix (Fin N × Fin N) (Fin N × Fin N) K} {a b : Fin N}
    (h : Commute X (coprodE a b)) (i j k l : Fin N) :
    (if b = k then X (i, j) (a, l) else 0) + (if b = l then X (i, j) (k, a) else 0) =
      (if a = i then X (b, j) (k, l) else 0) + (if a = j then X (i, b) (k, l) else 0) := by
  have := congrFun (congrFun h.eq (i, j)) (k, l)
  simp only [Matrix.mul_apply, coprodE, Fintype.sum_prod_type, mul_add, add_mul, mul_ite,
    ite_mul, mul_one, one_mul, mul_zero, zero_mul, Finset.sum_add_distrib, ite_and] at this
  simpa [Finset.sum_ite_eq, eq_comm] using this

theorem coprod_weight [CharZero K] {X : Matrix (Fin N × Fin N) (Fin N × Fin N) K}
    (h : ∀ a b, Commute X (coprodE a b)) (i j k l : Fin N)
    (hne : ¬ ((k = i ∧ l = j) ∨ (k = j ∧ l = i))) : X (i, j) (k, l) = 0 := by
  by_contra hx
  have h1 := coprod_rel (h k k) i j k l
  have h2 := coprod_rel (h l l) i j k l
  by_cases hki : k = i <;> by_cases hkj : k = j <;> by_cases hli : l = i <;>
    by_cases hlj : l = j <;> by_cases hkl : k = l <;>
    simp_all [eq_comm, ← two_mul]

theorem schurWeyl_two [CharZero K] (hN : 2 ≤ N) {X : Matrix (Fin N × Fin N) (Fin N × Fin N) K}
    (h : ∀ a b, Commute X (coprodE a b)) :
    ∃ α β : K, X = α • (1 : Matrix (Fin N × Fin N) (Fin N × Fin N) K) + β • swapM := by
  -- pair relations
  have E1 : ∀ a b : Fin N, a ≠ b → X (a, b) (a, b) + X (a, b) (b, a) = X (b, b) (b, b) := by
    intro a b hab; have := coprod_rel (h a b) a b b b; simpa [hab, Ne.symm hab] using this
  have E2 : ∀ a b : Fin N, a ≠ b → X (b, a) (a, b) + X (b, a) (b, a) = X (b, b) (b, b) := by
    intro a b hab; have := coprod_rel (h a b) b a b b; simpa [hab, Ne.symm hab] using this
  have E3 : ∀ a b : Fin N, a ≠ b → X (a, a) (a, a) = X (b, a) (b, a) + X (a, b) (b, a) := by
    intro a b hab; have := coprod_rel (h a b) a a b a; simpa [Ne.symm hab] using this
  have E4 : ∀ a b : Fin N, a ≠ b → X (a, a) (a, a) = X (b, a) (a, b) + X (a, b) (a, b) := by
    intro a b hab; have := coprod_rel (h a b) a a a b; simpa [Ne.symm hab] using this
  have E5 : ∀ a b j : Fin N, a ≠ b → j ≠ a → j ≠ b → X (a, j) (a, j) = X (b, j) (b, j) := by
    intro a b j hab hja hjb; have := coprod_rel (h a b) a j b j
    simpa [Ne.symm hjb, hja, Ne.symm hja] using this
  have E6 : ∀ a b j : Fin N, a ≠ b → j ≠ a → j ≠ b → X (a, j) (j, a) = X (b, j) (j, b) := by
    intro a b j hab hja hjb; have := coprod_rel (h a b) a j j b
    simpa [Ne.symm hjb, hja, Ne.symm hja] using this
  have two : (2 : K) ≠ 0 := two_ne_zero
  -- symmetry of p and r
  have Sp : ∀ a b : Fin N, a ≠ b → X (a, b) (a, b) = X (b, a) (b, a) := by
    intro a b hab
    have e1 := E1 a b hab; have e2 := E2 a b hab; have e3 := E3 a b hab; have e4 := E4 a b hab
    have : (2 : K) * (X (a, b) (a, b) - X (b, a) (b, a)) = 0 := by linear_combination e1 - e2 + e3 - e4
    exact sub_eq_zero.mp ((mul_eq_zero.mp this).resolve_left two)
  have Sr : ∀ a b : Fin N, a ≠ b → X (a, b) (b, a) = X (b, a) (a, b) := by
    intro a b hab
    have e1 := E1 a b hab; have e2 := E2 a b hab; have := Sp a b hab
    linear_combination e1 - e2 - this
  set z : Fin N := ⟨0, by omega⟩
  set o : Fin N := ⟨1, by omega⟩
  have hzo : z ≠ o := by simp [z, o, Fin.ext_iff]
  refine ⟨X (z, o) (z, o), X (z, o) (o, z), ?_⟩
  -- every pair has the same p and r
  have P0 : ∀ y, y ≠ z → X (z, y) (z, y) = X (z, o) (z, o) ∧
      X (z, y) (y, z) = X (z, o) (o, z) := by
    intro y hy
    by_cases hyo : y = o
    · subst hyo; exact ⟨rfl, rfl⟩
    · refine ⟨?_, ?_⟩
      · rw [Sp z y (Ne.symm hy), E5 y o z hyo (Ne.symm hy) hzo, Sp o z (Ne.symm hzo)]
      · rw [Sr z y (Ne.symm hy), E6 y o z hyo (Ne.symm hy) hzo, Sr o z (Ne.symm hzo)]
  have Pall : ∀ x y, x ≠ y → X (x, y) (x, y) = X (z, o) (z, o) ∧
      X (x, y) (y, x) = X (z, o) (o, z) := by
    intro x y hxy
    by_cases hx : x = z
    · rw [hx] at hxy ⊢; exact P0 y (Ne.symm hxy)
    · by_cases hy : y = z
      · rw [hy] at hxy ⊢
        rw [Sp x z hxy, Sr x z hxy]; exact P0 x hx
      · rw [E5 x z y hx (Ne.symm hxy) hy, E6 x z y hx (Ne.symm hxy) hy]
        exact P0 y hy
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, swapM, Prod.mk.injEq,
    smul_eq_mul]
  by_cases hc : (k = i ∧ l = j) ∨ (k = j ∧ l = i)
  · by_cases hij : i = j
    · have hk : k = i ∧ l = i := by rcases hc with h | h <;> rw [← hij] at * <;> exact h
      rw [hk.1, hk.2, ← hij]
      have hy : ∃ y, y ≠ i := ⟨if i = z then o else z, by
        by_cases hiz : i = z
        · rw [if_pos hiz, hiz]; exact Ne.symm hzo
        · rw [if_neg hiz]; exact Ne.symm hiz⟩
      obtain ⟨y, hyi⟩ := hy
      have e := E1 y i hyi
      obtain ⟨p1, p2⟩ := Pall y i hyi
      simp only [and_self, if_true, mul_one]
      rw [← e, p1, p2]
    · rcases hc with ⟨hk, hl⟩ | ⟨hk, hl⟩
      · rw [hk, hl]
        obtain ⟨p1, _⟩ := Pall i j hij
        simp [hij, p1]
      · rw [hk, hl]
        obtain ⟨_, p2⟩ := Pall i j hij
        simp [hij, Ne.symm hij, p2]
  · rw [coprod_weight h i j k l hc]
    push_neg at hc
    have h1 : ¬ (i = k ∧ j = l) := fun ⟨a, b⟩ => hc.1 a.symm b.symm
    have h2 : ¬ (i = l ∧ j = k) := fun ⟨a, b⟩ => hc.2 b.symm a.symm
    simp [h1, h2]

end SchurWeylTwo

section Split

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- With pair residues `α + β S_{ij}`, the Arnold form is an abelian part plus a KZ form. -/
theorem arnoldForm_split (α β : K) (S : Fin n → Fin n → A) (z u : Fin n → K) :
    arnoldForm (fun i j => α • (1 : A) + β • S i j) z u =
      α • arnoldForm (fun _ _ => (1 : A)) z u + kzForm β S z u := by
  unfold kzForm arnoldForm arnoldCoeff
  simp only [smul_add, Finset.sum_add_distrib, Finset.smul_sum, smul_comm α]

end Split

/-! ## Part VI — deriving P2: dilation invariance makes a regular residue constant

The partial-fraction step (written proof in the audit note) reduces two-body locality to: the
residue along a diagonal is a polynomial function that is invariant under the Euler (Reeb)
dilation. `eval_const_of_dilation_invariant` shows such a function is constant. -/

section Dilation

open Polynomial in
theorem eval_aeval_line {K : Type*} [Field K] {σ : Type*} (x : σ → K) (c : K)
    (R : MvPolynomial σ K) :
    (MvPolynomial.aeval (fun i => C (x i) * X) R).eval c = MvPolynomial.eval (c • x) R := by
  induction R using MvPolynomial.induction_on with
  | C a => simp
  | add f g hf hg => simp only [map_add, eval_add, hf, hg]
  | mul_X f i hf => simp only [map_mul, eval_mul, hf, MvPolynomial.aeval_X, eval_C, eval_X,
      MvPolynomial.eval_X, Pi.smul_apply, smul_eq_mul]; ring

open Polynomial in
theorem eval_const_of_dilation_invariant {K : Type*} [Field K] [Infinite K] {σ : Type*}
    (R : MvPolynomial σ K) (h : ∀ c : K, c ≠ 0 → ∀ x : σ → K,
      MvPolynomial.eval (c • x) R = MvPolynomial.eval x R) (x : σ → K) :
    MvPolynomial.eval x R = MvPolynomial.eval 0 R := by
  set p : K[X] := MvPolynomial.aeval (fun i => C (x i) * X) R with hp
  have hev : ∀ c : K, p.eval c = MvPolynomial.eval (c • x) R := fun c => eval_aeval_line x c R
  have hconst : p = C (MvPolynomial.eval x R) := by
    apply Polynomial.eq_of_infinite_eval_eq
    refine Set.Infinite.mono (s := ({0} : Set K)ᶜ) (fun c hc => ?_) (Set.finite_singleton 0).infinite_compl
    simp only [Set.mem_setOf_eq, eval_C, hev]
    exact h c hc x
  have := hev 0
  rw [hconst, eval_C, zero_smul] at this
  exact this

end Dilation

/-! ## Part IV — the Riemann–Hilbert input, isolated -/

/-- **The one analytic proposition.** For a class `Conn` of regular-singular flat connections
on `Conf_n` with fibre `V^{⊗n}`, gauge equivalence is detected by monodromy up to conjugacy
(Deligne's Riemann–Hilbert correspondence). Carried as data, never proved here. -/
structure RiemannHilbertInput (Conn Rep : Type*) where
  /-- Holomorphic gauge equivalence on `Conf_n`. -/
  gaugeEquiv : Conn → Conn → Prop
  /-- Monodromy representation of the pure braid group. -/
  monodromy : Conn → Rep
  /-- Conjugacy of representations. -/
  conj : Rep → Rep → Prop
  /-- Riemann–Hilbert: gauge class ↔ monodromy class. -/
  rh : ∀ c c', gaugeEquiv c c' ↔ conj (monodromy c) (monodromy c')

/-- A flat regular-singular connection is KZ up to gauge iff its monodromy is conjugate to the
KZ monodromy (by Drinfeld–Kohno, the `R`-matrix representation; sibling thread A4). -/
theorem gauge_equiv_kz_iff_monodromy {Conn Rep : Type*} (H : RiemannHilbertInput Conn Rep)
    (c kz : Conn) : H.gaugeEquiv c kz ↔ H.conj (H.monodromy c) (H.monodromy kz) :=
  H.rh c kz

end QOU.Mass.LagrangianKZ
