import QOU.Transcendental.MassTheory.BridgeAStokesNBody
import QOU.Transcendental.MassTheory.KohnoAssemblyGL

/-!
# Bridge A on colour ⊗ flavour: the transport and the monodromy split

Workstream W7 of the L2 1-ppQ plan; beans `qou-x09k`, `qou-et5f`.

`BridgeAStokesNBody.ColourTubeBraided` assumes that the strand monodromy on
colour ⊗ flavour is `Ř_colour ⊗ B`, with `B` the flavour monodromy. This file derives the
splitting part of that assumption from the connection.

Take the `n`-body connection on `End(V_c^{⊗n}) ⊗ End(V_f^{⊗n})` whose pair residue is

  `M_ab = (α_c + α_f)·1 + β_c·ρ_c(s_ab) ⊗ 1 + β_f·1 ⊗ ρ_f(s_ab)`,

i.e. the Arnold form (P2) of `ω_c ⊗ 1 + 1 ⊗ ω_f` (`colourFlavourForm_eq_nbodyForm`). By
Schur–Weyl for `𝔤𝔩_c × 𝔤𝔩_f`, an equivariant pair residue lies in the span of
`1, P_c, P_f, P_c P_f`. The splitting needs the coefficient of the mixed term `P_c P_f` to vanish,
and this form is exactly that case.

## What is proved (sorry-free, no new axiom)

* `isFundSol_kron`: if `U_c' = X_c U_c` and `U_f' = X_f U_f`, then
  `(U_c ⊗ U_f)' = (X_c ⊗ 1 + 1 ⊗ X_f)(U_c ⊗ U_f)`. The two pieces act on different tensor
  factors, so they commute, and no commutation hypothesis is needed.
* `colourFlavour_transport`: the transport of the colour ⊗ flavour form along `γ_j` is
  `U_c ⊗ U_f`, the tensor product of the colour and flavour transports. The colour transport
  exists for every coupling (`nbody_transport_exists`).
* `colourFlavour_generator_monodromy`: with strand permutation `ρ_c(s) ⊗ ρ_f(s)`, the generator
  monodromy of any transport of the form is `K_c(σ_j) ⊗ K_f(σ_j)`, the tensor product of the
  colour and flavour KZ holonomies. Each holonomy is read off its own residue.
* `colourFlavour_monodromy_conj`: if the colour holonomy is conjugate to a family `C_j` (one
  invertible matrix for all `j`), the full monodromy is conjugate to `C_j ⊗ Ř_{j,j+1}(q_f)`. The
  flavour half is Drinfeld–Kohno for `ℂ²`, already proved (`kz_conj_jimbo_complex_σ`).

## What is still assumed

* For colour `ℂ³` the colour Drinfeld–Kohno step is now proved:
  `colourC3_flavour_monodromy_conj` discharges `hcol` with Drinfeld–Kohno for `ℂ^d`
  (`KohnoAssemblyGL.kz_conj_jimboN_complex_σ`, at `d = 3`). It needs the colour coupling generic,
  i.e. `e^{πiβ_c}` not a root of unity, just as the flavour step does.
* The vanishing of the mixed `P_c P_f` term in the Lagrangian's pair residue. This is a statement
  about the Lagrangian, and it is not derived here.

So `ColourTubeBraided` is reduced to that residue condition (plus genericity of the two
couplings). It appears here in matrix form; `ColourFlavourMirror` writes the same tensors as
functions `Fin 3 → Fin 3 → Fin 3 → M`, and that change of notation is not formalised.

No empirical number enters.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987).
-/

namespace QOU.Mass.BridgeAColourSplit

open QOU.Mass.KZHolonomy QOU.Mass.KohnoAssembly QOU.Mass.BridgeAStokes
open QOU.IwahoriHecke.TensorEmbed QOU.MathlibExt.Braid QOU.SchurWeyl
open Matrix Set
open scoped Kronecker

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

section Kron

variable {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]

/-- `x ↦ x ⊗ 1` as a linear map. -/
noncomputable def kronLeftL : Matrix a a ℂ →ₗ[ℝ] Matrix (a × b) (a × b) ℂ where
  toFun x := x ⊗ₖ (1 : Matrix b b ℂ)
  map_add' x y := Matrix.add_kronecker x y 1
  map_smul' r x := Matrix.smul_kronecker r x 1

/-- `y ↦ 1 ⊗ y` as a linear map. -/
noncomputable def kronRightL : Matrix b b ℂ →ₗ[ℝ] Matrix (a × b) (a × b) ℂ where
  toFun y := (1 : Matrix a a ℂ) ⊗ₖ y
  map_add' x y := Matrix.kronecker_add 1 x y
  map_smul' r y := Matrix.kronecker_smul r 1 y

/-- `x ↦ x ⊗ 1`, colour operators acting on colour ⊗ flavour. -/
noncomputable def kronLeft : Matrix a a ℂ →L[ℝ] Matrix (a × b) (a × b) ℂ :=
  { toLinearMap := kronLeftL, cont := LinearMap.continuous_of_finiteDimensional _ }

/-- `y ↦ 1 ⊗ y`, flavour operators acting on colour ⊗ flavour. -/
noncomputable def kronRight : Matrix b b ℂ →L[ℝ] Matrix (a × b) (a × b) ℂ :=
  { toLinearMap := kronRightL, cont := LinearMap.continuous_of_finiteDimensional _ }

omit [DecidableEq a] [Fintype b] in
@[simp] theorem kronLeft_apply (x : Matrix a a ℂ) :
    (kronLeft (b := b) x) = x ⊗ₖ (1 : Matrix b b ℂ) := rfl

omit [Fintype a] [DecidableEq b] in
@[simp] theorem kronRight_apply (y : Matrix b b ℂ) :
    (kronRight (a := a) y) = (1 : Matrix a a ℂ) ⊗ₖ y := rfl

/-- **The transport splits.** If `U_c' = X_c U_c` and `U_f' = X_f U_f` on `[0,1]`, then
`U_c ⊗ U_f` solves `U' = (X_c ⊗ 1 + 1 ⊗ X_f) U`. -/
theorem isFundSol_kron {Xc Uc : ℝ → Matrix a a ℂ} {Xf Uf : ℝ → Matrix b b ℂ}
    (hc : IsFundSol Xc Uc) (hf : IsFundSol Xf Uf) :
    IsFundSol (fun t => Xc t ⊗ₖ (1 : Matrix b b ℂ) + (1 : Matrix a a ℂ) ⊗ₖ Xf t)
      (fun t => Uc t ⊗ₖ Uf t) := by
  refine ⟨by simp [hc.1, hf.1], fun t ht => ?_⟩
  have hL : HasDerivWithinAt (fun s => kronLeft (b := b) (Uc s)) (kronLeft (Xc t * Uc t))
      (Icc 0 1) t := (kronLeft (a := a) (b := b)).hasFDerivAt.comp_hasDerivWithinAt t (hc.2 t ht)
  have hR : HasDerivWithinAt (fun s => kronRight (a := a) (Uf s)) (kronRight (Xf t * Uf t))
      (Icc 0 1) t := (kronRight (a := a) (b := b)).hasFDerivAt.comp_hasDerivWithinAt t (hf.2 t ht)
  have hprod := hL.fun_mul hR
  have hfun : (fun s => kronLeft (b := b) (Uc s) * kronRight (a := a) (Uf s)) =
      fun s => Uc s ⊗ₖ Uf s := by
    funext s
    simp only [kronLeft_apply, kronRight_apply, ← Matrix.mul_kronecker_mul, Matrix.mul_one,
      Matrix.one_mul]
  rw [hfun] at hprod
  convert hprod using 1
  simp only [kronLeft_apply, kronRight_apply, add_mul, ← Matrix.mul_kronecker_mul,
    Matrix.mul_one, Matrix.one_mul]

end Kron

/-- Conjugacy is compatible with `⊗`. -/
theorem kron_conj {a b : Type*} [Fintype a] [Fintype b]
    {Wc Mc C : Matrix a a ℂ} {Wf Mf B : Matrix b b ℂ}
    (hc : Wc * Mc = C * Wc) (hf : Wf * Mf = B * Wf) :
    (Wc ⊗ₖ Wf) * (Mc ⊗ₖ Mf) = (C ⊗ₖ B) * (Wc ⊗ₖ Wf) := by
  rw [← Matrix.mul_kronecker_mul, hc, hf, Matrix.mul_kronecker_mul]

/-- The tensor product of two invertible matrices, as a unit. -/
noncomputable def kronUnit {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]
    (Wc : (Matrix a a ℂ)ˣ) (Wf : (Matrix b b ℂ)ˣ) : (Matrix (a × b) (a × b) ℂ)ˣ where
  val := (Wc : Matrix a a ℂ) ⊗ₖ (Wf : Matrix b b ℂ)
  inv := ((Wc⁻¹ : (Matrix a a ℂ)ˣ) : Matrix a a ℂ) ⊗ₖ ((Wf⁻¹ : (Matrix b b ℂ)ˣ) : Matrix b b ℂ)
  val_inv := by rw [← Matrix.mul_kronecker_mul, Units.mul_inv, Units.mul_inv,
    Matrix.one_kronecker_one]
  inv_val := by rw [← Matrix.mul_kronecker_mul, Units.inv_mul, Units.inv_mul,
    Matrix.one_kronecker_one]

/-! ## The colour ⊗ flavour `n`-body connection -/

section ColourFlavour

variable {n : ℕ} {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]

/-- The colour ⊗ flavour connection `ω_c ⊗ 1 + 1 ⊗ ω_f`. -/
noncomputable def colourFlavourForm (Mc : Fin n → Fin n → Matrix a a ℂ)
    (Mf : Fin n → Fin n → Matrix b b ℂ) (z : Fin n → ℂ) :
    (Fin n → ℂ) →L[ℝ] Matrix (a × b) (a × b) ℂ :=
  kronLeft.comp (nbodyForm Mc z) + kronRight.comp (nbodyForm Mf z)

/-- It is the Arnold-class form (P2) whose pair residue is `M^c_ab ⊗ 1 + 1 ⊗ M^f_ab`; with
P3 residues on each factor this is `(α_c + α_f) + β_c P_c + β_f P_f`, the case of the
Schur–Weyl commutant with no mixed `P_c P_f` term. -/
theorem colourFlavourForm_eq_nbodyForm (Mc : Fin n → Fin n → Matrix a a ℂ)
    (Mf : Fin n → Fin n → Matrix b b ℂ) :
    colourFlavourForm Mc Mf =
      nbodyForm (fun i j => Mc i j ⊗ₖ (1 : Matrix b b ℂ) + (1 : Matrix a a ℂ) ⊗ₖ Mf i j) := by
  funext z
  refine ContinuousLinearMap.ext fun u => ?_
  simp only [colourFlavourForm, ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply,
    nbodyForm_apply, map_sum, kronLeft_apply, kronRight_apply, smul_add, Finset.sum_add_distrib]
  congr 1 <;> refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  · exact Matrix.smul_kronecker _ _ _
  · exact Matrix.kronecker_smul _ _ _

end ColourFlavour

/-! ## Transport and generator monodromy on colour ⊗ flavour -/

section Monodromy

variable {m : ℕ} {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]

/-- **The transport splits on colour ⊗ flavour.** -/
theorem colourFlavour_transport {Mc : Fin (m + 1) → Fin (m + 1) → Matrix a a ℂ}
    {Mf : Fin (m + 1) → Fin (m + 1) → Matrix b b ℂ} {γ γ' : ℝ → Fin (m + 1) → ℂ}
    {Uc : ℝ → Matrix a a ℂ} {Uf : ℝ → Matrix b b ℂ}
    (hc : IsTransport (nbodyForm Mc) γ γ' Uc) (hf : IsTransport (nbodyForm Mf) γ γ' Uf) :
    IsTransport (colourFlavourForm Mc Mf) γ γ' (fun t => Uc t ⊗ₖ Uf t) := by
  have h := isFundSol_kron hc hf
  simpa [IsTransport, colourFlavourForm] using h

/-- The strand permutation on colour ⊗ flavour, `s ↦ ρ_c(s) ⊗ ρ_f(s)`. -/
noncomputable def kronRep (ρc : Equiv.Perm (Fin (m + 1)) →* Matrix a a ℂ)
    (ρf : Equiv.Perm (Fin (m + 1)) →* Matrix b b ℂ) :
    Equiv.Perm (Fin (m + 1)) →* Matrix (a × b) (a × b) ℂ where
  toFun s := ρc s ⊗ₖ ρf s
  map_one' := by simp
  map_mul' x y := by simp [Matrix.mul_kronecker_mul]

variable {αc βc αf βf : ℂ}

/-- **The generator monodromy splits.** For any transport `U` of the colour ⊗ flavour form along
`γ_j`, `ρ(s_j) U(1)` is the colour KZ holonomy of `σ_j` tensored with the flavour one, each read
off its own residue: `κ_c = β_c/2`, `c_c = −α_c/β_c` and `κ_f = β_f/2`, `c_f = −α_f/β_f`. -/
theorem colourFlavour_generator_monodromy (ρc : Equiv.Perm (Fin (m + 1)) →* Matrix a a ℂ)
    (ρf : Equiv.Perm (Fin (m + 1)) →* Matrix b b ℂ) (hβc : βc ≠ 0) (hβf : βf ≠ 0)
    (j : Fin m) {U : ℝ → Matrix (a × b) (a × b) ℂ}
    (hU : IsTransport (colourFlavourForm (pairResid ρc αc βc) (pairResid ρf αf βf))
      (genPath j) (genPath' j) U) :
    genMonodromy (kronRep ρc ρf) U j =
      (kzBraidRep ρc (βc / 2) (-αc / βc) (σ j) : Matrix a a ℂ) ⊗ₖ
        (kzBraidRep ρf (βf / 2) (-αf / βf) (σ j) : Matrix b b ℂ) := by
  obtain ⟨Uc, hUc⟩ := nbody_transport_exists (α := αc) ρc hβc j
  obtain ⟨Uf, hUf⟩ := nbody_transport_exists (α := αf) ρf hβf j
  have hV := colourFlavour_transport hUc hUf
  have hcont : ContinuousOn (fun t => colourFlavourForm (pairResid ρc αc βc)
      (pairResid ρf αf βf) (genPath j t) (genPath' j t)) (Icc 0 1) := by
    have h1 := continuousOn_genCoeff ρc (βc / 2) (-αc / βc) j
    have h2 := continuousOn_genCoeff ρf (βf / 2) (-αf / βf) j
    rw [← nbodyForm_eq_kzForm ρc hβc] at h1
    rw [← nbodyForm_eq_kzForm ρf hβf] at h2
    simp only [colourFlavourForm, ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply]
    exact (kronLeft.continuous.comp_continuousOn h1).add
      (kronRight.continuous.comp_continuousOn h2)
  have hEq : U 1 = Uc 1 ⊗ₖ Uf 1 :=
    IsFundSol.eqOn hcont hU hV ⟨zero_le_one, le_rfl⟩
  have hc := nbody_generator_monodromy ρc hβc j hUc
  have hf := nbody_generator_monodromy ρf hβf j hUf
  rw [← hc, ← hf, genMonodromy, genMonodromy, genMonodromy, hEq]
  exact (Matrix.mul_kronecker_mul _ _ _ _).symm

end Monodromy

/-! ## Conjugacy: the colour Drinfeld–Kohno step as a hypothesis -/

section Conj

variable {m : ℕ} {a : Type*} [Fintype a] [DecidableEq a] {αc βc αf βf : ℂ}

/-- **The colour-tube monodromy, given colour Drinfeld–Kohno.** Flavour is `V = ℂ²` with the
strand permutation action. If one invertible `W_c` conjugates the scalar-normalised colour
holonomy to a family `C_j` (hypothesis `hcol`: Kohno's theorem for the colour factor), then one
invertible `W` conjugates the normalised colour ⊗ flavour monodromy of every transport to
`C_j ⊗ Ř_{j,j+1}(q_f)`, `q_f = e^{iπβ_f}`. The flavour half is proved
(`kz_conj_jimbo_complex_σ`); only `hcol` is assumed. -/
theorem colourFlavour_monodromy_conj (ρc : Equiv.Perm (Fin (m + 1)) →* Matrix a a ℂ)
    (hβc : βc ≠ 0) (hβf : βf ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (βf / 2))) (C : Fin m → Matrix a a ℂ)
    (hcol : ∃ Wc : (Matrix a a ℂ)ˣ, ∀ j : Fin m,
      (Wc : Matrix a a ℂ) * (Complex.exp (2 * (βc / 2) * (Real.pi * Complex.I) * (-αc / βc)) •
        (kzBraidRep ρc (βc / 2) (-αc / βc) (σ j) : Matrix a a ℂ)) = C j * (Wc : Matrix a a ℂ))
    (U : Fin m → ℝ → Matrix (a × (Fin (m + 1) → Fin 2)) (a × (Fin (m + 1) → Fin 2)) ℂ)
    (hU : ∀ j, IsTransport (colourFlavourForm (pairResid ρc αc βc) (pairResid permRep αf βf))
      (genPath j) (genPath' j) (U j)) :
    ∃ W : (Matrix (a × (Fin (m + 1) → Fin 2)) (a × (Fin (m + 1) → Fin 2)) ℂ)ˣ, ∀ j : Fin m,
      (W : Matrix _ _ ℂ) * ((Complex.exp (2 * (βc / 2) * (Real.pi * Complex.I) * (-αc / βc)) *
          Complex.exp (2 * (βf / 2) * (Real.pi * Complex.I) * (-αf / βf))) •
          genMonodromy (kronRep ρc permRep) (U j) j) =
        (C j ⊗ₖ strandBraid (qC (βf / 2)) (qC (βf / 2))⁻¹ j) * (W : Matrix _ _ ℂ) := by
  obtain ⟨Wc, hWc⟩ := hcol
  obtain ⟨Wf, hWf⟩ := kz_conj_jimbo_complex_σ (m := m) (-αf / βf) (βf / 2) hκ
  refine ⟨kronUnit Wc Wf, fun j => ?_⟩
  rw [colourFlavour_generator_monodromy ρc permRep hβc hβf j (hU j), MulAction.mul_smul,
    ← Matrix.kronecker_smul, ← Matrix.smul_kronecker]
  exact kron_conj (hWc j) (hWf j)

/-- **Colour `ℂ³` ⊗ flavour `ℂ²`, with no colour hypothesis.** Take colour `V_c = ℂ³` with the
strand permutation action, and both couplings generic (`e^{πiβ_c}`, `e^{πiβ_f}` not roots of
unity). Then the full rescaled monodromy of the colour ⊗ flavour form is conjugate, by one
invertible matrix for all `j`, to `Ř^{𝔤𝔩_3}_{j,j+1}(q_c) ⊗ Ř^{𝔤𝔩_2}_{j,j+1}(q_f)`.

The colour step `hcol` of `colourFlavour_monodromy_conj` is discharged by Drinfeld–Kohno for
`ℂ³` (`KohnoAssemblyGL.kz_conj_jimboN_complex_σ`).
-- Ref: [kohno1987] https://doi.org/10.5802/aif.1114 -/
theorem colourC3_flavour_monodromy_conj (hβc : βc ≠ 0) (hβf : βf ≠ 0)
    (hκc : GenericParameter.NotRootOfUnity (qC (βc / 2)))
    (hκ : GenericParameter.NotRootOfUnity (qC (βf / 2)))
    (U : Fin m → ℝ → Matrix ((Fin (m + 1) → Fin 3) × (Fin (m + 1) → Fin 2))
      ((Fin (m + 1) → Fin 3) × (Fin (m + 1) → Fin 2)) ℂ)
    (hU : ∀ j, IsTransport
      (colourFlavourForm (pairResid (KohnoAssemblyGL.permRepN (d := 3)) αc βc)
        (pairResid permRep αf βf)) (genPath j) (genPath' j) (U j)) :
    ∃ W : (Matrix ((Fin (m + 1) → Fin 3) × (Fin (m + 1) → Fin 2))
      ((Fin (m + 1) → Fin 3) × (Fin (m + 1) → Fin 2)) ℂ)ˣ, ∀ j : Fin m,
      (W : Matrix _ _ ℂ) * ((Complex.exp (2 * (βc / 2) * (Real.pi * Complex.I) * (-αc / βc)) *
          Complex.exp (2 * (βf / 2) * (Real.pi * Complex.I) * (-αf / βf))) •
          genMonodromy (kronRep (KohnoAssemblyGL.permRepN (d := 3)) permRep) (U j) j) =
        (QOU.IwahoriHecke.TensorEmbedGL.strandBraid (d := 3) (qC (βc / 2)) (qC (βc / 2))⁻¹ j ⊗ₖ
          strandBraid (qC (βf / 2)) (qC (βf / 2))⁻¹ j) * (W : Matrix _ _ ℂ) :=
  colourFlavour_monodromy_conj _ hβc hβf hκ _
    (KohnoAssemblyGL.kz_conj_jimboN_complex_σ (d := 3) (m := m) (-αc / βc) (βc / 2) hκc) U hU

end Conj

end QOU.Mass.BridgeAColourSplit
