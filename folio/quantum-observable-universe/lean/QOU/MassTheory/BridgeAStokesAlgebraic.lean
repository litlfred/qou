import QOU.Transcendental.MassTheory.BridgeAStokesNBody

/-!
# Bridge A: `StokesToBraiding` replaced by the KZ realisation alone

`BridgeAStokesNBody` derives the corrected form of `hL` from P1–P3 plus one named analytic
assumption, `StokesToBraiding`: the monodromy of the Lagrangian's algebraic fundamental solution
`F_L` on `σ_j` is `ρ(s_j)` times the analytic transport of the `n`-body form along the half-turn
`γ_j`. That assumption is about the Lagrangian. This file removes it, and leaves only an
assumption about KZ.

## The argument

Read P2 and P3 in the algebraic setting of `BridgeADeligneGauge`: a differential ring `S` with
derivations `D_j = ∂/∂z_j` and elements `w_jb ∈ S` (standing for `(z_j − z_b)⁻¹`). The Arnold form
with constant residues `M_ab` is

    ω_M(j) = Σ_{b ≠ j} w_jb · M_jb                               (`algArnold`).

1. **Same form.** With `M_ab = α + β·ρ(s_ab)` (P3) and `β ≠ 0`, this is the algebraic KZ form
   `2κ Σ_{b≠j} w_jb (ρ(s_jb) − c)` at `κ = β/2`, `c = −α/β` (`algArnold_lag_eq_kz`). This is the
   algebraic twin of `nbodyForm_eq_kzForm`: `κ` and `c` are read off the residue, nothing is
   chosen, and no coordinate identity for `w` is needed because only the residues are compared.
2. **Same form ⇒ conjugate monodromy.** Two fundamental solutions `F₁, F₂` of one form `ω`
   have monodromies conjugate by a constant invertible matrix (`monodromy_conj_of_same_form`).
   The matrix is `C = Φ₂⁻¹ Φ₁`: it is horizontal (`∂C = −Φ₂⁻¹ω Φ₁ + Φ₂⁻¹ ω Φ₁ = 0`), so its
   entries are constants, and the deck action gives `M₂(γ) C = C M₁(γ)`. The one hypothesis is
   that `S` has **no new constants** (`NoNewConstants`): an element killed by every `D_j` comes
   from `K`. This is the defining property of a Picard–Vessiot ring.
3. **Consequences.** With `F_KZ` an algebraic KZ fundamental solution whose generator monodromy is
   the analytic KZ holonomy `kzBraidRep(σ_j)` (`hKZ`, already a hypothesis of
   `lagrangian_gauge_to_KZ_of_stokes`):
   * `F_L.M(σ_j)` is conjugate to `kzBraidRep(σ_j)` by one constant `C` for all `j`
     (`lagrangian_monodromy_conj_kz`); this is `lagrangian_monodromy_eq_kz` in its correct,
     basis-free form;
   * one invertible `W C` conjugates every Jimbo-normalised Lagrangian generator to
     `Ř_{j,j+1}(q)` (`lagrangian_monodromy_conj_jimbo_of_kz`), which is
     `lagrangian_monodromy_conj_jimbo` without `StokesToBraiding`;
   * the algebraic gauge from the Lagrangian form to KZ is the identity
     (`lagrangian_gauge_to_KZ_algebraic`), with no Deligne full faithfulness and no monodromy
     input at all. Once P2 and P3 are read algebraically there is nothing left to gauge.

## What is still assumed, and why it is smaller

`hKZ` is exactly `StokesToBraiding` for the KZ fundamental solution (`stokesToBraiding_iff_kz`).
So the assumption has moved from the Lagrangian to KZ, and nothing else is assumed beyond P1–P3
and no new constants. In words, `hKZ` says: an algebraic fundamental solution of the KZ form has, on `σ_j`, the monodromy
`kzBraidRep(σ_j) = ρ(s_j) T_j(1)` computed analytically in `KZHolonomy`. This is the
Riemann–Hilbert comparison for **KZ alone**: the deck action on `S` must be analytic continuation
on the universal cover of the unordered configuration space, which needs a ring of multivalued
functions with a braid-group deck action (not in Mathlib). It is a standard theorem about one
named connection (Kohno 1987), and it no longer mentions the Lagrangian. `StokesToBraiding` made
the same comparison for the Lagrangian connection, before anyone knew it was KZ.

`StokesToBraiding` also asked for an *equality* of `F_L.M(σ_j)` with a transport, which depends
on the choice of `Φ` and fails for `Φ C` with `C` not commuting with the monodromy. The
conjugacy statements here hold for every choice.

No empirical number enters. `q = e^{iπβ}` is a free complex parameter, constrained only to not
be a root of unity, and `α, β` are free.

The source for `hKZ` is Kohno 1987, Theorem 1.2.8 (p. 145), in the case `𝔤 = sl(m, ℂ)` with
its vector representation `W = ℂ^m`. There the KZ form is `λ Σ (p⊗p)(t) dlog(z_a − z_b)` with
`t` the Casimir, which on `W ⊗ W` is the swap minus a scalar; the scalar is the `c` of
`kzResidAlg`. Kohno's monodromy is `σ_i ↦ T_i(q)`, with `T(q)` the Hecke matrix (1.2.9) (p. 146).
Two points of scope:
* Kohno states the result as an identity in `End(W^{⊗n}) ⊗ ℂ{λ}`, i.e. for the KZ parameter in a
  neighbourhood of `0` (the proof in §1.3 uses Theorem 1.3.4, which needs `‖θ(γ_ab) − 1‖` small).
  Extending to every `q` that is not a root of unity is analytic continuation in the parameter.
* Kohno's statement is about the analytic monodromy. `hKZ` asks for it on an algebraic
  fundamental solution, which is the Riemann–Hilbert step this file does not supply.

-- Ref: [kohno1987] https://doi.org/10.5802/aif.1114 Theorem 1.2.8, p. 145; (1.2.9), p. 146
-/

set_option linter.unusedSectionVars false

namespace QOU.Mass.BridgeAStokesAlgebraic

open QOU.Mass.KZHolonomy QOU.Mass.KohnoAssembly QOU.Mass.BridgeADeligneGauge
open QOU.Mass.BridgeADeligneKZ QOU.Mass.BridgeAStokes
open QOU.IwahoriHecke.TensorEmbed QOU.MathlibExt.Braid QOU.SchurWeyl
open Complex

/-! ## Same form, conjugate monodromy -/

section General

variable {S : Type*} [CommRing S] {n : Type*} [Fintype n] [DecidableEq n]
variable {ι : Type*} {D : ι → Derivation ℤ S S}
variable {K : Type*} [CommRing K] [Algebra K S]
variable {Γ : Type*} [Monoid Γ] [MulSemiringAction Γ S]

/-- **No new constants**: an element of `S` killed by every derivation comes from `K`. The
defining property of a Picard–Vessiot ring over a field of constants `K`. -/
def NoNewConstants (D : ι → Derivation ℤ S S) (K : Type*) [CommRing K] [Algebra K S] : Prop :=
  ∀ s : S, (∀ j, D j s = 0) → ∃ c : K, algebraMap K S c = s

/-- A matrix over `S` killed entrywise by every `D_j` is a constant matrix. -/
theorem exists_cst_of_der_zero (hconst : NoNewConstants D K) {X : Matrix n n S}
    (hX : ∀ j, X.map (D j) = 0) : ∃ C : Matrix n n K, cst C = X := by
  have h : ∀ i k, ∃ c : K, algebraMap K S c = X i k := fun i k =>
    hconst (X i k) fun j => by simpa using congrFun (congrFun (hX j) i) k
  exact ⟨Matrix.of fun i k => (h i k).choose, by ext i k; exact (h i k).choose_spec⟩

/-- `Φ₂⁻¹ Φ₁` is horizontal for two fundamental solutions of the same form. -/
theorem der_ratio_eq_zero {ω : ι → Matrix n n S}
    (F₁ F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω) (j : ι) :
    (F₂.Φinv * F₁.Φ).map (D j) = 0 := by
  rw [map_mul_der, horiz_inv F₂ j, F₁.horiz j, Matrix.neg_mul, Matrix.mul_assoc,
    neg_add_cancel]

/-- **Same form ⇒ conjugate monodromy.** Two fundamental solutions of one connection form, over
a differential ring with no new constants, have monodromies conjugate by one constant invertible
matrix: `M₂(γ) C = C M₁(γ)` for every `γ`. -/
theorem monodromy_conj_of_same_form
    (hΓK : ∀ (γ : Γ) (c : K), γ • algebraMap K S c = algebraMap K S c)
    (hinj : Function.Injective (algebraMap K S)) (hconst : NoNewConstants D K)
    {ω : ι → Matrix n n S} (F₁ F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω) :
    ∃ C Cinv : Matrix n n K, C * Cinv = 1 ∧ Cinv * C = 1 ∧
      ∀ γ, F₂.M γ * C = C * F₁.M γ := by
  obtain ⟨C, hC⟩ := exists_cst_of_der_zero hconst (der_ratio_eq_zero F₁ F₂)
  obtain ⟨Cinv, hCinv⟩ := exists_cst_of_der_zero hconst (der_ratio_eq_zero F₂ F₁)
  have hmul : ∀ A B : Matrix n n K, (cst (S := S) (A * B)) = cst A * cst B := fun A B =>
    Matrix.map_mul (f := algebraMap K S)
  have hcinj : Function.Injective (cst (S := S) (n := n) (K := K)) := fun A B h => by
    ext i k; exact hinj (congrFun (congrFun h i) k)
  have hone : cst (S := S) (1 : Matrix n n K) = 1 := Matrix.map_one _ (map_zero _) (map_one _)
  refine ⟨C, Cinv, hcinj ?_, hcinj ?_, fun γ => hcinj ?_⟩
  · rw [hmul, hC, hCinv, hone, Matrix.mul_assoc, ← Matrix.mul_assoc F₁.Φ, F₁.mul_inv,
      Matrix.one_mul, F₂.inv_mul]
  · rw [hmul, hC, hCinv, hone, Matrix.mul_assoc, ← Matrix.mul_assoc F₂.Φ, F₂.mul_inv,
      Matrix.one_mul, F₁.inv_mul]
  · -- `cst M₂ · actM(Φ₂⁻¹) = Φ₂⁻¹`, and `actM` fixes constant matrices.
    have hfix : actM γ (cst (S := S) C) = cst C := by ext i k; simp [actM, cst, hΓK]
    have hinv : cst (F₂.M γ) * actM γ F₂.Φinv = F₂.Φinv := by
      have h := congrArg (F₂.Φinv * ·) (deck_inv F₂ γ)
      simp only [Matrix.mul_one, ← Matrix.mul_assoc, F₂.inv_mul, Matrix.one_mul] at h
      exact h
    rw [hmul, hmul, hC]
    calc cst (F₂.M γ) * (F₂.Φinv * F₁.Φ)
        = cst (F₂.M γ) * actM γ (F₂.Φinv * F₁.Φ) := by rw [← hC, hfix]
      _ = cst (F₂.M γ) * actM γ F₂.Φinv * actM γ F₁.Φ := by rw [actM_mul, Matrix.mul_assoc]
      _ = F₂.Φinv * F₁.Φ * cst (F₁.M γ) := by rw [hinv, F₁.deck γ, Matrix.mul_assoc]

/-- `monodromy_conj_of_same_form` for two forms proved equal. -/
theorem monodromy_conj_of_eq_form
    (hΓK : ∀ (γ : Γ) (c : K), γ • algebraMap K S c = algebraMap K S c)
    (hinj : Function.Injective (algebraMap K S)) (hconst : NoNewConstants D K)
    {ω₁ ω₂ : ι → Matrix n n S} (hω : ω₁ = ω₂)
    (F₁ : FundamentalSolution (Γ := Γ) (K := K) D ω₁)
    (F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω₂) :
    ∃ C Cinv : Matrix n n K, C * Cinv = 1 ∧ Cinv * C = 1 ∧
      ∀ γ, F₂.M γ * C = C * F₁.M γ := by
  subst hω
  exact monodromy_conj_of_same_form hΓK hinj hconst F₁ F₂

end General

/-! ## The algebraic `n`-body form is the algebraic KZ form -/

section Forms

variable {S : Type*} [CommRing S] {N : ℕ} {n : Type*} [Fintype n] [DecidableEq n]
variable {K : Type*} [CommRing K] [Algebra K S]

/-- P2, algebraically: the Arnold form with constant residues `M`,
`ω_M(j) = Σ_{b ≠ j} w_jb · M_jb`, where `w_jb ∈ S` stands for `(z_j − z_b)⁻¹`. -/
def algArnold (w : Fin N → Fin N → S) (M : Fin N → Fin N → Matrix n n K) (j : Fin N) :
    Matrix n n S :=
  ∑ b ∈ Finset.univ.erase j, w j b • cst (M j b)

/-- The Arnold form depends only on the off-diagonal residues. -/
theorem algArnold_congr (w : Fin N → Fin N → S) {M M' : Fin N → Fin N → Matrix n n K}
    (h : ∀ a b, a ≠ b → M a b = M' a b) : algArnold w M = algArnold w M' := by
  funext j
  refine Finset.sum_congr rfl fun b hb => ?_
  rw [h j b (Finset.ne_of_mem_erase hb).symm]

end Forms

section Lagrangian

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ}

/-- P3: the Lagrangian pair residue `α + β·ρ(s_ab)` on `V^{⊗(m+1)}`, `V = ℂ²`. -/
noncomputable def lagResid (α β : ℂ) (a b : Fin (m + 1)) : Mat m :=
  α • (1 : Mat m) + β • permRep (Equiv.swap a b)

/-- The algebraic KZ residue `2κ (ρ(s_ab) − c)`: `∂_j` of `κ Σ_{a,b} log(z_a − z_b)(ρ(s_ab) − c)`. -/
noncomputable def kzResidAlg (κ c : ℂ) (a b : Fin (m + 1)) : Mat m :=
  (2 * κ) • (permRep (Equiv.swap a b) - c • (1 : Mat m))

/-- The Lagrangian residue is the KZ residue at `κ = β/2`, `c = −α/β`. -/
theorem lagResid_eq_kzResidAlg {α β : ℂ} (hβ : β ≠ 0) (a b : Fin (m + 1)) :
    lagResid (m := m) α β a b = kzResidAlg (β / 2) (-α / β) a b := by
  unfold lagResid kzResidAlg
  rw [smul_sub, smul_smul, sub_eq_add_neg, ← neg_smul, add_comm]
  congr 2
  · field_simp
  · field_simp

variable {S : Type*} [CommRing S] [Algebra ℂ S]

/-- **The algebraic `n`-body form of `𝒟_∇` is the algebraic KZ form** (P2 + P3, `β ≠ 0`). -/
theorem algArnold_lag_eq_kz {α β : ℂ} (hβ : β ≠ 0) (w : Fin (m + 1) → Fin (m + 1) → S) :
    algArnold w (lagResid (m := m) α β) = algArnold w (kzResidAlg (β / 2) (-α / β)) :=
  algArnold_congr w fun a b _ => lagResid_eq_kzResidAlg hβ a b

variable [MulSemiringAction (BraidGroup m) S] {D : Fin (m + 1) → Derivation ℤ S S}
variable {α β : ℂ}

/-- **The Lagrangian monodromy is conjugate to the KZ holonomy**, without `StokesToBraiding`.
`F_L` solves the algebraic `n`-body form (P1–P3), `F_KZ` the algebraic KZ form with the analytic
KZ holonomy on the generators (`hKZ`); `S` has no new constants. One constant invertible `C`
conjugates every generator: `C · F_L.M(σ_j) = kzBraidRep(σ_j) · C`. -/
theorem lagrangian_monodromy_conj_kz (hβ : β ≠ 0)
    (hΓK : ∀ (γ : BraidGroup m) (z : ℂ), γ • algebraMap ℂ S z = algebraMap ℂ S z)
    (hconst : NoNewConstants D ℂ) [Nontrivial S] (w : Fin (m + 1) → Fin (m + 1) → S)
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D (algArnold w (lagResid α β)))
    (FKZ : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D
      (algArnold w (kzResidAlg (β / 2) (-α / β))))
    (hKZ : ∀ j : Fin m,
      FKZ.M (σ j) = ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m)) :
    ∃ C : (Mat m)ˣ, ∀ j : Fin m,
      (C : Mat m) * FL.M (σ j) =
        ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m) * (C : Mat m) := by
  obtain ⟨C, Cinv, h1, h2, hC⟩ := monodromy_conj_of_eq_form hΓK (algebraMap ℂ S).injective
    hconst (algArnold_lag_eq_kz hβ w) FL FKZ
  exact ⟨⟨C, Cinv, h1, h2⟩, fun j => by rw [← hKZ j]; exact (hC (σ j)).symm⟩

/-- **`hL`, derived, without `StokesToBraiding`.** Under P1–P3, no new constants and the KZ
realisation `hKZ`, one invertible matrix conjugates every Jimbo-normalised Lagrangian generator
to Jimbo's `Ř_{j,j+1}(q)`, `q = e^{iπβ}` not a root of unity. -/
theorem lagrangian_monodromy_conj_jimbo_of_kz (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2)))
    (hΓK : ∀ (γ : BraidGroup m) (z : ℂ), γ • algebraMap ℂ S z = algebraMap ℂ S z)
    (hconst : NoNewConstants D ℂ) [Nontrivial S] (w : Fin (m + 1) → Fin (m + 1) → S)
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D (algArnold w (lagResid α β)))
    (FKZ : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D
      (algArnold w (kzResidAlg (β / 2) (-α / β))))
    (hKZ : ∀ j : Fin m,
      FKZ.M (σ j) = ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m)) :
    ∃ W : (Mat m)ˣ, ∀ j : Fin m,
      (W : Mat m) * jimboNormalised α β (FL.M (σ j)) =
        strandBraid (qC (β / 2)) (qC (β / 2))⁻¹ j * (W : Mat m) := by
  obtain ⟨C, hC⟩ := lagrangian_monodromy_conj_kz hβ hΓK hconst w FL FKZ hKZ
  obtain ⟨W, hW⟩ := kz_conj_jimbo_complex_σ (m := m) (-α / β) (β / 2) hκ
  refine ⟨W * C, fun j => ?_⟩
  unfold jimboNormalised
  rw [Units.val_mul, Matrix.mul_assoc, Matrix.mul_smul, hC j, ← Matrix.smul_mul,
    ← Matrix.mul_assoc, hW j, Matrix.mul_assoc]

/-- **What is left is `StokesToBraiding` for KZ alone.** For any fundamental solution `F`,
`StokesToBraiding F` for the `n`-body form is equivalent to `F` having the analytic KZ holonomy
on every generator (`hKZ`). So the hypothesis `hKZ` above is exactly the Stokes step for the
KZ connection, and the Lagrangian's own Stokes step is no longer assumed. -/
theorem stokesToBraiding_iff_kz (hβ : β ≠ 0) {ι : Type*} {D' : ι → Derivation ℤ S S}
    {ω : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (F : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D' ω) :
    StokesToBraiding F (nbodyForm (pairResid permRep α β)) ↔
      ∀ j : Fin m, F.M (σ j) = ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m) := by
  constructor
  · intro hS j
    obtain ⟨U, hU, hM⟩ := hS j
    rw [hM, nbody_generator_monodromy (A := Mat m) permRep hβ j hU]
  · intro hK j
    obtain ⟨U, hU⟩ := nbody_transport_exists (A := Mat m) permRep (α := α) hβ j
    exact ⟨U, hU, by rw [hK j, nbody_generator_monodromy (A := Mat m) permRep hβ j hU]⟩

/-- **The algebraic gauge from the Lagrangian form to KZ is the identity.** Once P2 and P3 are
read in the differential ring, the two forms coincide (`algArnold_lag_eq_kz`), so `g = 1`
satisfies `∂_j g = ω_L j · g − g · ω_KZ j`. No monodromy input and no Deligne full faithfulness
are used. -/
theorem lagrangian_gauge_to_KZ_algebraic (hβ : β ≠ 0) (R : Type*) [CommRing R] [Algebra R S]
    (w : Fin (m + 1) → Fin (m + 1) → S) :
    ∃ g gInv : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R,
      g * gInv = 1 ∧ gInv * g = 1 ∧
      ∀ j, (g.map (algebraMap R S)).map (D j)
        = algArnold w (lagResid α β) j * g.map (algebraMap R S)
          - g.map (algebraMap R S) * algArnold w (kzResidAlg (β / 2) (-α / β)) j := by
  refine ⟨1, 1, Matrix.mul_one 1, Matrix.mul_one 1, fun j => ?_⟩
  rw [Matrix.map_one _ (map_zero _) (map_one _), map_one_der, Matrix.mul_one, Matrix.one_mul,
    algArnold_lag_eq_kz hβ w, sub_self]

end Lagrangian

end QOU.Mass.BridgeAStokesAlgebraic
