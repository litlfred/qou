import QOU.IwahoriHecke.RMatrixSl2
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Reindex
import Mathlib.Tactic.FieldSimp

/-!
# `U_q(sl₂)`: representation data, the fundamental, and Jimbo's `Ř` as an intertwiner

The corpus had Jimbo's `Ř` (`QOU.IwahoriHecke.RMatrix.rCheck`, `QOU.Mass.KohnoTwoPoint.rCheck`)
and its Hecke/Yang–Baxter relations, but no `U_q(sl₂)` for it to intertwine. This file
supplies the quantum group side at the level of **representation data** and proves the
intertwining half of `q`-Schur–Weyl.

## Conventions

* Base: a generic field `𝕜` (§7c), `q ≠ 0`, `q − q⁻¹ ≠ 0` (equivalently `q² ≠ 1`).
* `U_q(sl₂)` relations: `KK⁻¹ = K⁻¹K = 1`, `KEK⁻¹ = q²E`, `KFK⁻¹ = q⁻²F`,
  `[E,F] = (K − K⁻¹)/(q − q⁻¹)`. A representation on `𝕜^ι` is the structure `Rep q ι`
  (four matrices satisfying these). The algebra `U_q(sl₂)` itself is **not** constructed.
* Coproduct (`Rep.tensor`): `Δ(E) = E⊗K + 1⊗E`, `Δ(F) = F⊗1 + K⁻¹⊗F`, `Δ(K^{±1}) = K^{±1}⊗K^{±1}`;
  proved to respect every relation, for arbitrary representations.
* With this `Δ`, the corpus's `RMatrix.rCheck q q⁻¹` intertwines `fund`
  (`K = diag(q⁻¹, q)`, `E e₀ = e₁`: highest weight on `e₁`), while the `KohnoTwoPoint` form
  intertwines `fund'` (`K = diag(q, q⁻¹)`, `E e₁ = e₀`, the textbook one). The two matrices
  differ by the relabelling `0 ↔ 1`. (Checked symbolically: the requested `Δ` paired with the
  *other* fundamental fails for both `Ř`s.)

## Results

* `Rep.tensor`, `Rep.coassoc` (coassociativity), `Rep.trivial` (counit).
* `isEndo_rCheck`: `[Ř, Δ(X)] = 0` on `V ⊗ V` for `X ∈ {E, F, K, K⁻¹}` — `n = 2`.
* `isEndo_kohnoRCheck`: the same for the `KohnoTwoPoint` matrix (copied verbatim; that module
  has no olean in the restored cache, so it is not imported).
* `isEndo_rCheckAt`: for every `n` and every adjacent pair, `Ř_{i,i+1}` on `V^{⊗n}` commutes
  with `Δ^{(n)}` of all four generators; `rCheckAt_sq`: each satisfies the Hecke quadratic.

## Not proved here

* The algebra `U_q(sl₂)` (e.g. a `RingQuot` of `FreeAlgebra`) and the fact that `Rep` data is
  the same as an algebra map out of it.
* Yang–Baxter / far commutation of the `Ř_{i,i+1}` on `V^{⊗n}` for general `n` (only `n = 3`
  exists, in `RMatrixSl2`), hence no `H_n(q) → End(V^{⊗n})` for general `n` here.
* The *double-commutant* half of Schur–Weyl (that the `Ř_i` generate the full commutant).

-- Ref: [jimbo1986] Jimbo, "A q-difference analogue of U(g) and the Yang-Baxter equation"
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII (`U_q(sl₂)`) and VIII
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-- **Representation data of `U_q(sl₂)`** on `𝕜^ι`: four matrices `E, F, K, K⁻¹`
satisfying the defining relations `KK⁻¹ = K⁻¹K = 1`, `KEK⁻¹ = q²E`, `KFK⁻¹ = q⁻²F`,
`[E,F] = (K − K⁻¹)/(q − q⁻¹)`. -/
structure Rep (q : 𝕜) (ι : Type*) [Fintype ι] [DecidableEq ι] where
  E : Matrix ι ι 𝕜
  F : Matrix ι ι 𝕜
  Kp : Matrix ι ι 𝕜
  Km : Matrix ι ι 𝕜
  Kp_Km : Kp * Km = 1
  Km_Kp : Km * Kp = 1
  KE : Kp * E * Km = q ^ 2 • E
  KF : Kp * F * Km = q⁻¹ ^ 2 • F
  EF : E * F - F * E = (q - q⁻¹)⁻¹ • (Kp - Km)

theorem sub_kronecker' {ι κ : Type*} (A B : Matrix ι ι 𝕜) (C : Matrix κ κ 𝕜) :
    (A - B) ⊗ₖ C = A ⊗ₖ C - B ⊗ₖ C := by
  ext i j; simp [sub_mul]

theorem kronecker_sub' {ι κ : Type*} (A : Matrix ι ι 𝕜) (B C : Matrix κ κ 𝕜) :
    A ⊗ₖ (B - C) = A ⊗ₖ B - A ⊗ₖ C := by
  ext i j; simp [mul_sub]

namespace Rep

variable {q : 𝕜} {ι κ ν : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
  [Fintype ν] [DecidableEq ν]

/-- `E K⁻¹ = q² K⁻¹ E`. -/
theorem E_Km (ρ : Rep q ι) : ρ.E * ρ.Km = q ^ 2 • (ρ.Km * ρ.E) := by
  have h : ρ.Km * (ρ.Kp * ρ.E * ρ.Km) = ρ.Km * (q ^ 2 • ρ.E) := by rw [ρ.KE]
  rw [mul_smul_comm] at h
  rw [← h, ← mul_assoc, ← mul_assoc, ρ.Km_Kp, one_mul]

/-- `K F = q⁻² F K`. -/
theorem Kp_F (ρ : Rep q ι) : ρ.Kp * ρ.F = q⁻¹ ^ 2 • (ρ.F * ρ.Kp) := by
  have h : (ρ.Kp * ρ.F * ρ.Km) * ρ.Kp = (q⁻¹ ^ 2 • ρ.F) * ρ.Kp := by rw [ρ.KF]
  rw [smul_mul_assoc] at h
  rw [← h, mul_assoc, ρ.Km_Kp, mul_one]

/-- `T` commutes with all four generators: an endomorphism of the representation. -/
def IsEndo (ρ : Rep q ι) (T : Matrix ι ι 𝕜) : Prop :=
  Commute T ρ.E ∧ Commute T ρ.F ∧ Commute T ρ.Kp ∧ Commute T ρ.Km

/-- **The coproduct.** Convention:
`Δ(E) = E ⊗ K + 1 ⊗ E`, `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F`, `Δ(K^{±1}) = K^{±1} ⊗ K^{±1}`.
This is proved to be a representation, i.e. `Δ` respects all the relations. -/
def tensor (hq : q ≠ 0) (ρ : Rep q ι) (σ : Rep q κ) : Rep q (ι × κ) where
  E := ρ.E ⊗ₖ σ.Kp + 1 ⊗ₖ σ.E
  F := ρ.F ⊗ₖ 1 + ρ.Km ⊗ₖ σ.F
  Kp := ρ.Kp ⊗ₖ σ.Kp
  Km := ρ.Km ⊗ₖ σ.Km
  Kp_Km := by rw [← mul_kronecker_mul, ρ.Kp_Km, σ.Kp_Km, one_kronecker_one]
  Km_Kp := by rw [← mul_kronecker_mul, ρ.Km_Kp, σ.Km_Kp, one_kronecker_one]
  KE := by
    simp only [mul_add, add_mul, ← mul_kronecker_mul, mul_one]
    rw [ρ.KE, σ.KE, mul_assoc σ.Kp σ.Kp σ.Km, σ.Kp_Km, mul_one, ρ.Kp_Km,
      smul_kronecker, kronecker_smul, smul_add]
  KF := by
    simp only [mul_add, add_mul, ← mul_kronecker_mul, mul_one]
    rw [ρ.KF, σ.KF, σ.Kp_Km, mul_assoc ρ.Kp ρ.Km ρ.Km, ← mul_assoc ρ.Kp ρ.Km,
      ρ.Kp_Km, one_mul, smul_kronecker, kronecker_smul, smul_add]
  EF := by
    simp only [mul_add, add_mul, ← mul_kronecker_mul, mul_one, one_mul]
    have hc : (ρ.E * ρ.Km) ⊗ₖ (σ.Kp * σ.F) = (ρ.Km * ρ.E) ⊗ₖ (σ.F * σ.Kp) := by
      rw [ρ.E_Km, σ.Kp_F, smul_kronecker, kronecker_smul, smul_smul, ← mul_pow,
        mul_inv_cancel₀ hq, one_pow, one_smul]
    have h1 : (ρ.E * ρ.F) ⊗ₖ σ.Kp - (ρ.F * ρ.E) ⊗ₖ σ.Kp
        = (q - q⁻¹)⁻¹ • ((ρ.Kp - ρ.Km) ⊗ₖ σ.Kp) := by
      rw [← sub_kronecker', ρ.EF, smul_kronecker]
    have h2 : ρ.Km ⊗ₖ (σ.E * σ.F) - ρ.Km ⊗ₖ (σ.F * σ.E)
        = (q - q⁻¹)⁻¹ • (ρ.Km ⊗ₖ (σ.Kp - σ.Km)) := by
      rw [← kronecker_sub', σ.EF, kronecker_smul]
    have h3 : (ρ.Kp - ρ.Km) ⊗ₖ σ.Kp + ρ.Km ⊗ₖ (σ.Kp - σ.Km)
        = ρ.Kp ⊗ₖ σ.Kp - ρ.Km ⊗ₖ σ.Km := by
      rw [sub_kronecker', kronecker_sub']; abel
    rw [← h3, smul_add, ← h1, ← h2, hc]
    abel

/-- Endomorphisms of the left factor extend: `T ⊗ 1`. -/
theorem isEndo_kronecker_one (hq : q ≠ 0) (ρ : Rep q ι) (σ : Rep q κ) {T : Matrix ι ι 𝕜}
    (hT : ρ.IsEndo T) : (ρ.tensor hq σ).IsEndo (T ⊗ₖ (1 : Matrix κ κ 𝕜)) := by
  obtain ⟨hE, hF, hP, hM⟩ := hT
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [Commute, SemiconjBy, tensor, mul_add, add_mul, ← mul_kronecker_mul,
      mul_one, one_mul] <;>
    simp only [hE.eq, hF.eq, hP.eq, hM.eq]

/-- Endomorphisms of the right factor commuting with `K^{±1}` extend: `1 ⊗ T`. -/
theorem isEndo_one_kronecker (hq : q ≠ 0) (ρ : Rep q ι) (σ : Rep q κ) {T : Matrix κ κ 𝕜}
    (hT : σ.IsEndo T) : (ρ.tensor hq σ).IsEndo ((1 : Matrix ι ι 𝕜) ⊗ₖ T) := by
  obtain ⟨hE, hF, hP, hM⟩ := hT
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [Commute, SemiconjBy, tensor, mul_add, add_mul, ← mul_kronecker_mul,
      mul_one, one_mul] <;>
    simp only [hE.eq, hF.eq, hP.eq, hM.eq]

/-! ### Coassociativity, and transport of endomorphisms along the associator -/

/-- The associator `(ι × κ) × ν ≃ ι × (κ × ν)` acting on matrices, as an algebra equivalence. -/
abbrev assoc (ι κ ν : Type*) [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    [Fintype ν] [DecidableEq ν] :
    Matrix ((ι × κ) × ν) ((ι × κ) × ν) 𝕜 ≃ₐ[𝕜] Matrix (ι × κ × ν) (ι × κ × ν) 𝕜 :=
  reindexAlgEquiv 𝕜 𝕜 (Equiv.prodAssoc ι κ ν)

theorem one_eq_kron (ι κ : Type*) [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] :
    (1 : Matrix (ι × κ) (ι × κ) 𝕜) = (1 : Matrix ι ι 𝕜) ⊗ₖ (1 : Matrix κ κ 𝕜) :=
  one_kronecker_one.symm

/-- **Coassociativity of `Δ`**, generator by generator: the associator carries
`(Δ ⊗ id) ∘ Δ` to `(id ⊗ Δ) ∘ Δ`. -/
theorem coassoc (hq : q ≠ 0) (ρ : Rep q ι) (σ : Rep q κ) (τ : Rep q ν) :
    assoc ι κ ν (((ρ.tensor hq σ).tensor hq τ).E) = (ρ.tensor hq (σ.tensor hq τ)).E ∧
    assoc ι κ ν (((ρ.tensor hq σ).tensor hq τ).F) = (ρ.tensor hq (σ.tensor hq τ)).F ∧
    assoc ι κ ν (((ρ.tensor hq σ).tensor hq τ).Kp) = (ρ.tensor hq (σ.tensor hq τ)).Kp ∧
    assoc ι κ ν (((ρ.tensor hq σ).tensor hq τ).Km) = (ρ.tensor hq (σ.tensor hq τ)).Km := by
  simp only [tensor]
  rw [one_eq_kron ι κ, one_eq_kron κ ν]
  simp only [add_kronecker, kronecker_add, map_add, reindexAlgEquiv_apply, kronecker_assoc]
  exact ⟨add_assoc _ _ _, add_assoc _ _ _, trivial, trivial⟩

/-- Endomorphisms of `ρ ⊗ (σ ⊗ τ)` pull back along the associator to endomorphisms of
`(ρ ⊗ σ) ⊗ τ`. -/
theorem isEndo_assoc_symm (hq : q ≠ 0) (ρ : Rep q ι) (σ : Rep q κ) (τ : Rep q ν)
    {T : Matrix (ι × κ × ν) (ι × κ × ν) 𝕜} (hT : (ρ.tensor hq (σ.tensor hq τ)).IsEndo T) :
    ((ρ.tensor hq σ).tensor hq τ).IsEndo ((assoc ι κ ν).symm T) := by
  obtain ⟨h1, h2, h3, h4⟩ := coassoc hq ρ σ τ
  obtain ⟨hE, hF, hP, hM⟩ := hT
  have key : ∀ X, Commute T (assoc ι κ ν X) → Commute ((assoc ι κ ν).symm T) X := by
    intro X hX
    simpa using hX.map (assoc ι κ ν).symm.toRingHom
  exact ⟨key _ (h1 ▸ hE), key _ (h2 ▸ hF), key _ (h3 ▸ hP), key _ (h4 ▸ hM)⟩

/-- The trivial one-dimensional representation (the counit): `E = F = 0`, `K^{±1} = 1`. -/
def trivial (q : 𝕜) : Rep q Unit where
  E := 0
  F := 0
  Kp := 1
  Km := 1
  Kp_Km := one_mul 1
  Km_Kp := one_mul 1
  KE := by simp
  KF := by simp
  EF := by simp

end Rep

/-! ## The fundamental representation -/

section Fundamental

variable (q : 𝕜)

/-- **The fundamental of `U_q(sl₂)`, highest weight on `e₁`** (the convention matching
`QOU.IwahoriHecke.RMatrix.rCheck`): `K = diag(q⁻¹, q)`, `E e₀ = e₁`, `F e₁ = e₀`.
Note `q · K = diag(1, q²)`, the weight operator of `QOU.MassTheory.WeightedPermutationCharacter`. -/
def fund (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) : Rep q (Fin 2) where
  E := !![0, 0; 1, 0]
  F := !![0, 1; 0, 0]
  Kp := !![q⁻¹, 0; 0, q]
  Km := !![q, 0; 0, q⁻¹]
  Kp_Km := by ext i j; fin_cases i <;> fin_cases j <;> simp [hq]
  Km_Kp := by ext i j; fin_cases i <;> fin_cases j <;> simp [hq]
  KE := by ext i j; fin_cases i <;> fin_cases j <;> simp; ring
  KF := by ext i j; fin_cases i <;> fin_cases j <;> simp; ring
  EF := by
    have h1 : (q - q⁻¹)⁻¹ * (q - q⁻¹) = 1 := inv_mul_cancel₀ hq2
    have h2 : (q - q⁻¹)⁻¹ * (q⁻¹ - q) = -1 := by
      rw [show q⁻¹ - q = -(q - q⁻¹) by ring, mul_neg, h1]
    ext i j; fin_cases i <;> fin_cases j <;> simp [h1, h2]

/-- **The fundamental, textbook convention** (highest weight on `e₀`): `K = diag(q, q⁻¹)`,
`E e₁ = e₀`, `F e₀ = e₁`. This is the one matching `QOU.Mass.KohnoTwoPoint.rCheck`. -/
def fund' (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) : Rep q (Fin 2) where
  E := !![0, 1; 0, 0]
  F := !![0, 0; 1, 0]
  Kp := !![q, 0; 0, q⁻¹]
  Km := !![q⁻¹, 0; 0, q]
  Kp_Km := by ext i j; fin_cases i <;> fin_cases j <;> simp [hq]
  Km_Kp := by ext i j; fin_cases i <;> fin_cases j <;> simp [hq]
  KE := by ext i j; fin_cases i <;> fin_cases j <;> simp; ring
  KF := by ext i j; fin_cases i <;> fin_cases j <;> simp; ring
  EF := by
    have h1 : (q - q⁻¹)⁻¹ * (q - q⁻¹) = 1 := inv_mul_cancel₀ hq2
    have h2 : (q - q⁻¹)⁻¹ * (q⁻¹ - q) = -1 := by
      rw [show q⁻¹ - q = -(q - q⁻¹) by ring, mul_neg, h1]
    ext i j; fin_cases i <;> fin_cases j <;> simp [h1, h2]

end Fundamental

/-! ## `n = 2` quantum Schur–Weyl: Jimbo's `Ř` is an intertwiner of `V ⊗ V` -/

section TwoSite

open QOU.IwahoriHecke.RMatrix

set_option maxHeartbeats 1000000 in
set_option linter.unnecessarySeqFocus false in
theorem rCheck_commute_E (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (rCheck q q⁻¹) ((fund q hq hq2).tensor hq (fund q hq hq2)).E := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund, rCheck, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

set_option maxHeartbeats 1000000 in
set_option linter.unnecessarySeqFocus false in
theorem rCheck_commute_F (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (rCheck q q⁻¹) ((fund q hq hq2).tensor hq (fund q hq hq2)).F := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund, rCheck, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

set_option maxHeartbeats 1000000 in
theorem rCheck_commute_Kp (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (rCheck q q⁻¹) ((fund q hq hq2).tensor hq (fund q hq hq2)).Kp := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund, rCheck, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two] <;>
    ring

set_option maxHeartbeats 1000000 in
theorem rCheck_commute_Km (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (rCheck q q⁻¹) ((fund q hq hq2).tensor hq (fund q hq hq2)).Km := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund, rCheck, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two] <;>
    ring

/-- **Jimbo's `Ř` commutes with `Δ(E)`, `Δ(F)`, `Δ(K^{±1})` on `V ⊗ V`.**
`Ř = QOU.IwahoriHecke.RMatrix.rCheck q q⁻¹` (the corpus's matrix, imported, not copied),
`V = fund`, `Δ` as in `Rep.tensor`. This is the `n = 2` intertwining half of `q`-Schur–Weyl. -/
theorem isEndo_rCheck (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    ((fund q hq hq2).tensor hq (fund q hq hq2)).IsEndo (rCheck q q⁻¹) :=
  ⟨rCheck_commute_E q hq hq2, rCheck_commute_F q hq hq2, rCheck_commute_Kp q hq hq2,
    rCheck_commute_Km q hq hq2⟩

/-- A verbatim copy of `QOU.Mass.KohnoTwoPoint.rCheck` (that module has no olean in the
restored cache, so it is not imported; the body is the same `!![…]` literal). -/
def kohnoRCheck (q : 𝕜) : Matrix (Fin 4) (Fin 4) 𝕜 :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- The same matrix, indexed by `Fin 2 × Fin 2`: `q` on `e_i ⊗ e_i`, the flip off the
diagonal, and `q − q⁻¹` on `e₁ ⊗ e₀`. -/
def kohnoRCheck₂ (q : 𝕜) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) 𝕜 :=
  Matrix.of fun a b =>
    if a = b then (if b.1 = b.2 then q else if b.1 < b.2 then 0 else q - q⁻¹)
    else if a = (b.2, b.1) then 1 else 0

/-- The lexicographic identification `Fin 2 × Fin 2 ≃ Fin 4` carries `kohnoRCheck` to
`kohnoRCheck₂`. -/
theorem reindex_kohnoRCheck (q : 𝕜) :
    Matrix.reindex finProdFinEquiv.symm finProdFinEquiv.symm (kohnoRCheck q)
      = kohnoRCheck₂ q := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> rfl

set_option maxHeartbeats 1000000 in
set_option linter.unnecessarySeqFocus false in
theorem kohnoRCheck₂_commute_E (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (kohnoRCheck₂ q) ((fund' q hq hq2).tensor hq (fund' q hq hq2)).E := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund', kohnoRCheck₂, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

set_option maxHeartbeats 1000000 in
set_option linter.unnecessarySeqFocus false in
theorem kohnoRCheck₂_commute_F (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (kohnoRCheck₂ q) ((fund' q hq hq2).tensor hq (fund' q hq hq2)).F := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund', kohnoRCheck₂, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

set_option maxHeartbeats 1000000 in
theorem kohnoRCheck₂_commute_Kp (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (kohnoRCheck₂ q) ((fund' q hq hq2).tensor hq (fund' q hq hq2)).Kp := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund', kohnoRCheck₂, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two] <;>
    ring

set_option maxHeartbeats 1000000 in
theorem kohnoRCheck₂_commute_Km (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    Commute (kohnoRCheck₂ q) ((fund' q hq hq2).tensor hq (fund' q hq hq2)).Km := by
  show _ = _
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Rep.tensor, fund', kohnoRCheck₂, Matrix.mul_apply, Fintype.sum_prod_type,
      Fin.sum_univ_two] <;>
    ring

/-- **The `KohnoTwoPoint` form of `Ř` commutes with `Δ` of the textbook fundamental**
(`K = diag(q, q⁻¹)`), after the lexicographic identification `Fin 2 × Fin 2 ≃ Fin 4`. -/
theorem isEndo_kohnoRCheck (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    ((fund' q hq hq2).tensor hq (fund' q hq hq2)).IsEndo
      (Matrix.reindex finProdFinEquiv.symm finProdFinEquiv.symm (kohnoRCheck q)) := by
  rw [reindex_kohnoRCheck]
  exact ⟨kohnoRCheck₂_commute_E q hq hq2, kohnoRCheck₂_commute_F q hq hq2,
    kohnoRCheck₂_commute_Kp q hq hq2, kohnoRCheck₂_commute_Km q hq hq2⟩

end TwoSite


/-! ## `V^{⊗n}`: every adjacent `Ř_{i,i+1}` commutes with `Δ^{(n)}` -/

section TensorPower

/-- Index type of `V^{⊗n}`, left-nested: `TP 0 = Unit`, `TP (n+1) = TP n × Fin 2`. -/
def TP : ℕ → Type
  | 0 => Unit
  | n + 1 => TP n × Fin 2

instance TP.instFintype : ∀ n, Fintype (TP n)
  | 0 => inferInstanceAs (Fintype Unit)
  | n + 1 => @instFintypeProd (TP n) (Fin 2) (TP.instFintype n) _

instance TP.instDecidableEq : ∀ n, DecidableEq (TP n)
  | 0 => inferInstanceAs (DecidableEq Unit)
  | n + 1 => @instDecidableEqProd (TP n) (Fin 2) (TP.instDecidableEq n) _

variable (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)

/-- `V^{⊗n}` with the iterated coproduct `Δ^{(n)}`, built as `(…((𝟙 ⊗ V) ⊗ V)…) ⊗ V`. -/
def powRep : (n : ℕ) → Rep q (TP n)
  | 0 => Rep.trivial q
  | n + 1 => (powRep n).tensor hq (fund q hq hq2)

open QOU.IwahoriHecke.RMatrix in
/-- **`Ř` acting on tensor factors `m+1, m+2` of `V^{⊗(m+2+k)}`** (1-indexed), i.e. on
`V^{⊗m} ⊗ (V ⊗ V) ⊗ V^{⊗k}`: `1 ⊗ Ř` re-associated, then `⊗ 1` on each of the `k`
trailing factors. -/
def rCheckAt (m : ℕ) : (k : ℕ) → Matrix (TP (m + 2 + k)) (TP (m + 2 + k)) 𝕜
  | 0 => (Rep.assoc (TP m) (Fin 2) (Fin 2)).symm
      ((1 : Matrix (TP m) (TP m) 𝕜) ⊗ₖ rCheck q q⁻¹)
  | k + 1 => rCheckAt m k ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) 𝕜)

/-- **`q`-Schur–Weyl, intertwining half, all `n`.** Every adjacent Jimbo `Ř_{i,i+1}` on
`V^{⊗n}` commutes with `Δ^{(n)}(E)`, `Δ^{(n)}(F)`, `Δ^{(n)}(K^{±1})`. -/
theorem isEndo_rCheckAt (m k : ℕ) :
    (powRep q hq hq2 (m + 2 + k)).IsEndo (rCheckAt q m k) := by
  induction k with
  | zero =>
    exact Rep.isEndo_assoc_symm hq (powRep q hq hq2 m) (fund q hq hq2) (fund q hq hq2)
      (Rep.isEndo_one_kronecker hq _ _ (isEndo_rCheck q hq hq2))
  | succ k ih =>
    exact Rep.isEndo_kronecker_one hq (powRep q hq hq2 (m + 2 + k)) (fund q hq hq2) ih

include hq in
open QOU.IwahoriHecke.RMatrix in
/-- Each `Ř_{i,i+1}` on `V^{⊗n}` still satisfies the §7a Hecke quadratic
`Ř² = (q − q⁻¹)Ř + 1` (from `QOU.IwahoriHecke.RMatrix.rCheck_sq`). -/
theorem rCheckAt_sq (m k : ℕ) :
    rCheckAt q m k * rCheckAt q m k = (q - q⁻¹) • rCheckAt q m k + 1 := by
  induction k with
  | zero =>
    simp only [rCheckAt]
    rw [← map_mul (Rep.assoc (TP m) (Fin 2) (Fin 2)).symm, ← mul_kronecker_mul, one_mul, rCheck_sq q q⁻¹ (mul_inv_cancel₀ hq),
      kronecker_add, kronecker_smul, ← Rep.one_eq_kron, map_add, map_smul, map_one]
  | succ k ih =>
    simp only [rCheckAt]
    rw [← mul_kronecker_mul, ih, one_mul, add_kronecker, smul_kronecker, ← Rep.one_eq_kron]

end TensorPower

end QOU.Mass.QuantumSl2
