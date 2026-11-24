import QOU.MassTheory.BridgeADeligneKZ
import QOU.MassTheory.LagrangianKZIdentification
import QOU.BraidsAndKnots.ColourFlavourMirror

/-!
# Bridge A without `hL`: the `n`-body connection of `𝒟_∇`, its local monodromy, colour singlets

Workstream W7 of the L2 1-ppQ plan; bean `qou-x09k`, owner goal `qou-ywyq`.

`BridgeADeligneKZ.lagrangian_gauge_to_KZ` takes as hypothesis `hL`: the monodromy of the
Lagrangian connection on `σ_j` *is* Jimbo's `Ř_{j,j+1}(q)`. That is the conclusion Bridge A is
meant to reach, so the theorem is circular as a derivation. It is also stronger than what holds
for KZ itself: the KZ monodromy is only *conjugate* to Jimbo's, after the scalar `e^{2πiκc}`.

This file replaces `hL` by the three postulates P1–P3 of `LagrangianKZIdentification` plus one
named analytic assumption, and proves the rest.

## What is proved (sorry-free, no new axiom)

* **The `n`-body connection.** Under P1 (fibre `V^{⊗n}` over `Conf_n` with the strand
  permutation action `ρ`), P2 (Arnold class with constant residues `M_ab`) and P3 (pair residue
  `M_ab = α + β·ρ(s_ab)`; `schurWeyl_two` derives this on one pair and
  `LagrangianKZInputs.residue_uniform` spreads it to every pair), the connection form
  of `∇` is `nbodyForm (pairResid ρ α β)`. It is the Arnold form of `LagrangianKZ`
  (`nbodyForm_eq_arnoldForm`) and, for `β ≠ 0`, **equals the KZ form** of `KZHolonomy` with
  coupling `κ = β/2` and shift `c = −α/β` (`nbodyForm_eq_kzForm`). Nothing is chosen: `κ` and
  `c` are read off the residue. It is flat on `Conf_n` (`nbodyForm_isFlatOn`).
* **Its local monodromy.** The transport of that form along the half-turn `γ_j` exchanging
  strands `j, j+1`, composed with `ρ(s_j)`, is the KZ holonomy `kzBraidRep ρ (β/2) (−α/β) (σ_j)`
  (`nbody_generator_monodromy`). For `V = ℂ²` and `q = e^{iπβ}` not a root of unity, one
  invertible `W` conjugates all the rescaled generators to Jimbo's `Ř_{j,j+1}(q)`
  (`nbody_monodromy_conj_jimbo`, by the Drinfeld–Kohno theorem already proved in
  `KohnoAssembly`), so each satisfies the Hecke quadratic `B² = (q − q⁻¹)B + 1`
  (`nbody_monodromy_hecke`).
* **Bridge A, non-circular.** `lagrangian_gauge_to_KZ_of_stokes` gives the algebraic gauge to
  KZ with `hL` removed, and `lagrangian_monodromy_conj_jimbo` *derives* the corrected form of
  `hL` (conjugacy to Jimbo after the scalar).
* **Colour singlets.** With a colour index the strand braid is `X = Ř_colour ⊗ B` and satisfies
  a cubic; on the colour singlet `ε_q ⊗ f` it acts as `−q⁻¹ B` (#9130, `X12_singlet`). Given
  the flavour Hecke quadratic proved above, `X` restricted to singlets satisfies
  `(X + 1)(X − q⁻²) = 0` (`singlet_quadratic_12`, `_23`), and the q-exterior singlets are
  exactly the totally q-symmetric flavour states (`lagrangian_singlet_bridge`, using
  `singlet_exterior_iff`). So `b = −qX` on singlets is the Hecke generator, as the plan asks.

## Named assumptions (not proved here)

1. **`StokesToBraiding`.** The monodromy of the Lagrangian's fundamental solution on `σ_j` is
   `ρ(s_j)` times the transport of the `n`-body connection form along `γ_j`. This is the
   non-abelian Stokes step: holonomy of `𝒟_∇` read as the braid monodromy of a flat connection on
   `Conf_n`. `LagrangianKZ.dirac_eq_zero_iff` already shows `𝒟_∇` and `∇` have the same flat
   sections, so the assumption is about `∇`; what is missing is a continuous multiplicative
   integral in Lean and the packaging of analytic transport as an algebraic
   `FundamentalSolution`.
2. **`ColourTubeBraided`.** The strand monodromy on colour ⊗ flavour is `Ř_colour ⊗ B` with
   `B` the flavour monodromy (`conj:colour-tube-monodromy-braided`, bean `qou-et5f`).
3. P1–P3 themselves (as in `LagrangianKZIdentification`), and, for the gauge statement only,
   Deligne full faithfulness and a KZ `FundamentalSolution` with the KZ monodromy (unchanged
   from `BridgeADeligneKZ`).

No empirical number enters. `q` is a free complex parameter, constrained only to not be a root
of unity.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987).
-- Ref: [drinfeld1990] Drinfeld, Quasi-Hopf algebras, Leningrad Math. J. 1 (1990).
-/

namespace QOU.Mass.BridgeAStokes

open QOU.Mass.KZHolonomy QOU.Mass.KohnoAssembly QOU.Mass.BridgeADeligneGauge
open QOU.Mass.BridgeADeligneKZ
open QOU.IwahoriHecke.TensorEmbed QOU.MathlibExt.Braid QOU.SchurWeyl
open Complex Set

/-! ## The `n`-body connection form (P1–P3) -/

section NBody

variable {n : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]

/-- P3: the pair residue `α + β·ρ(s_ab)`. -/
noncomputable def pairResid (ρ : Equiv.Perm (Fin n) →* A) (α β : ℂ) (a b : Fin n) : A :=
  algebraMap ℂ A α + β • ρ (Equiv.swap a b)

theorem pairResid_symm (ρ : Equiv.Perm (Fin n) →* A) (α β : ℂ) (a b : Fin n) :
    pairResid ρ α β a b = pairResid ρ α β b a := by
  simp only [pairResid, Equiv.swap_comm]

/-- P2: the Arnold-class form with constant residues `M`,
`ω_M(z)(u) = ½ Σ_{a,b} (u_a − u_b)/(z_a − z_b) · M_ab`, as a real-linear map of `u`. -/
noncomputable def nbodyForm (M : Fin n → Fin n → A) (z : Fin n → ℂ) : (Fin n → ℂ) →L[ℝ] A :=
  ∑ a, ∑ b, ((2 : ℂ)⁻¹ * (z a - z b)⁻¹) • (pairDiff a b).smulRight (M a b)

theorem nbodyForm_apply (M : Fin n → Fin n → A) (z u : Fin n → ℂ) :
    nbodyForm M z u = ∑ a, ∑ b, ((2 : ℂ)⁻¹ * (z a - z b)⁻¹ * (u a - u b)) • M a b := by
  simp only [nbodyForm, ContinuousLinearMap.coe_sum', Finset.sum_apply,
    ContinuousLinearMap.coe_smul', Pi.smul_apply, ContinuousLinearMap.smulRight_apply,
    pairDiff_apply, smul_smul]

/-- For symmetric residues the form is the Arnold form `Σ_m u_m Σ_j (z_m − z_j)⁻¹ M_mj` of
`LagrangianKZ`, so P2 is exactly the Arnold class used there. -/
theorem nbodyForm_eq_arnoldForm {M : Fin n → Fin n → A} (hM : ∀ i j, M i j = M j i)
    (z u : Fin n → ℂ) : nbodyForm M z u = QOU.Mass.LagrangianKZ.arnoldForm M z u := by
  rw [QOU.Mass.LagrangianKZ.arnoldForm_eq_half_dlog (K := ℂ) two_ne_zero hM, nbodyForm_apply,
    Finset.smul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [smul_smul, div_eq_mul_inv]
  congr 1
  ring

/-- **The `n`-body connection of `𝒟_∇` is the KZ connection.** For `β ≠ 0` the Arnold form
with residues `α + β·ρ(s_ab)` equals `kzForm ρ (β/2) (−α/β)`. The coupling and the shift are
read off the residue; nothing is chosen. -/
theorem nbodyForm_eq_kzForm (ρ : Equiv.Perm (Fin n) →* A) {α β : ℂ} (hβ : β ≠ 0) :
    nbodyForm (pairResid ρ α β) = kzForm ρ (β / 2) (-α / β) := by
  funext z
  refine ContinuousLinearMap.ext fun u => ?_
  rw [nbodyForm_apply]
  simp only [kzForm, ContinuousLinearMap.coe_sum', Finset.sum_apply,
    ContinuousLinearMap.coe_smul', Pi.smul_apply, kzL_apply, smul_smul]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  simp only [pairResid, resid, Algebra.algebraMap_eq_smul_one]
  match_scalars <;> field_simp

/-- The `n`-body connection is flat on `Conf_n`, for every `n`. -/
theorem nbodyForm_isFlatOn (ρ : Equiv.Perm (Fin n) →* A) {α β : ℂ} (hβ : β ≠ 0) :
    IsFlatOn (nbodyForm (pairResid ρ α β)) (kzForm' ρ (β / 2) (-α / β)) (confSet n) := by
  rw [nbodyForm_eq_kzForm ρ hβ]
  exact kzForm_isFlatOn ρ _ _

end NBody

/-! ## Local monodromy of the `n`-body connection -/

section Monodromy

variable {m : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A]
variable (ρ : Equiv.Perm (Fin (m + 1)) →* A) {α β : ℂ}

/-- The generator monodromy read off a transport `U` along `γ_j`: `ρ(s_j) U(1)`. -/
noncomputable def genMonodromy (U : ℝ → A) (j : Fin m) : A := ρ (adjSwap j) * U 1

/-- The `n`-body connection has a transport along every generator half-turn. -/
theorem nbody_transport_exists (hβ : β ≠ 0) (j : Fin m) :
    ∃ U : ℝ → A, IsTransport (nbodyForm (pairResid ρ α β)) (genPath j) (genPath' j) U := by
  refine ⟨genFund ρ (β / 2) (-α / β) j, ?_⟩
  rw [nbodyForm_eq_kzForm ρ hβ]
  exact genFund_spec ρ _ _ j

/-- **Local monodromy of the `n`-body connection.** Whatever transport `U` of the form along
`γ_j` is taken, `ρ(s_j) U(1)` is the KZ holonomy of `σ_j` at `κ = β/2`, `c = −α/β`. -/
theorem nbody_generator_monodromy (hβ : β ≠ 0) (j : Fin m) {U : ℝ → A}
    (hU : IsTransport (nbodyForm (pairResid ρ α β)) (genPath j) (genPath' j) U) :
    genMonodromy ρ U j = (kzBraidRep ρ (β / 2) (-α / β) (σ j) : A) := by
  rw [nbodyForm_eq_kzForm ρ hβ] at hU
  rw [genMonodromy, kzBraidRep_σ]
  congr 1
  exact IsFundSol.eqOn (continuousOn_genCoeff ρ _ _ j) hU (genFund_spec ρ _ _ j)
    ⟨zero_le_one, le_rfl⟩

end Monodromy

/-! ## Two strands' worth of algebra: conjugation preserves a quadratic relation -/

section Quad

variable {B : Type*} [Ring B] [Algebra ℂ B]

theorem quad_of_conj (W : Bˣ) {X Y : B} (a b : ℂ) (hW : (W : B) * X = Y * W)
    (hY : Y * Y = a • Y + b • (1 : B)) : X * X = a • X + b • (1 : B) := by
  have hX : X = ((W⁻¹ : Bˣ) : B) * Y * W := by
    rw [mul_assoc, ← hW, ← mul_assoc, Units.inv_mul, one_mul]
  have key : X * X = ((W⁻¹ : Bˣ) : B) * (Y * Y) * W := by
    rw [hX]
    simp only [mul_assoc]
    rw [← mul_assoc (W : B) ((W⁻¹ : Bˣ) : B), Units.mul_inv, one_mul]
  rw [key, hY, mul_add, add_mul, mul_smul_comm, smul_mul_assoc, mul_smul_comm, smul_mul_assoc,
    mul_one, Units.inv_mul, ← hX]

end Quad

/-! ## `V = ℂ²`: conjugacy to Jimbo and the Hecke quadratic -/

section Jimbo

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ} {α β : ℂ}

/-- Shorthand for `End(V^{⊗(m+1)})`, `V = ℂ²`. -/
abbrev Mat (m : ℕ) := Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ

/-- The Jimbo-normalised generator: the scalar `e^{2πiκc}` times the generator monodromy, at
`κ = β/2`, `c = −α/β`. -/
noncomputable def jimboNormalised (α β : ℂ) (G : Mat m) : Mat m :=
  Complex.exp (2 * (β / 2) * (Real.pi * I) * (-α / β)) • G

/-- **The `n`-body monodromy is conjugate to Jimbo's braiding.** No `hL`: the monodromy is
computed from the connection, and Drinfeld–Kohno (`kz_conj_jimbo_complex_σ`) supplies `W`. -/
theorem nbody_monodromy_conj_jimbo (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2))) (U : Fin m → ℝ → Mat m)
    (hU : ∀ j, IsTransport (nbodyForm (pairResid permRep α β)) (genPath j) (genPath' j) (U j)) :
    ∃ W : (Mat m)ˣ, ∀ j : Fin m,
      (W : Mat m) * jimboNormalised α β (genMonodromy permRep (U j) j) =
        strandBraid (qC (β / 2)) (qC (β / 2))⁻¹ j * (W : Mat m) := by
  obtain ⟨W, hW⟩ := kz_conj_jimbo_complex_σ (m := m) (-α / β) (β / 2) hκ
  refine ⟨W, fun j => ?_⟩
  have h := nbody_generator_monodromy (A := Mat m) permRep hβ j (hU j)
  unfold jimboNormalised
  rw [h]
  exact hW j

/-- **The Hecke quadratic for the `n`-body monodromy**, `B² = (q − q⁻¹)B + 1`, `q = e^{iπβ}`. -/
theorem nbody_monodromy_hecke (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2))) (U : Fin m → ℝ → Mat m)
    (hU : ∀ j, IsTransport (nbodyForm (pairResid permRep α β)) (genPath j) (genPath' j) (U j))
    (j : Fin m) :
    jimboNormalised α β (genMonodromy permRep (U j) j) *
        jimboNormalised α β (genMonodromy permRep (U j) j) =
      (qC (β / 2) - (qC (β / 2))⁻¹) • jimboNormalised α β (genMonodromy permRep (U j) j) +
        (1 : ℂ) • (1 : Mat m) := by
  obtain ⟨W, hW⟩ := nbody_monodromy_conj_jimbo hβ hκ U hU
  have hq := strandBraid_quad (m := m) (qC_ne_zero (β / 2)) j
  rw [mul_inv_cancel₀ (qC_ne_zero (β / 2))] at hq
  exact quad_of_conj W _ _ (hW j) hq

/-- `q = e^{iπβ}` as a unit of `ℂ`. -/
noncomputable def qUnit (β : ℂ) : ℂˣ := Units.mk0 (qC (β / 2)) (qC_ne_zero (β / 2))

/-- Specialisation `ℤ[q, q⁻¹] → ℂ`, `q ↦ e^{iπβ}`. -/
noncomputable def specialise (β : ℂ) : LaurentPolynomial ℤ →+* ℂ :=
  LaurentPolynomial.eval₂ (Int.castRingHom ℂ) (qUnit β)

/-- The Laurent-ring Jimbo generator `Ř_{j,j+1}(q, q⁻¹)` over `ℤ[q, q⁻¹]`, specialised at
`q = e^{iπβ}`, is the Jimbo generator at that `q`. -/
theorem specialise_strandBraid (β : ℂ) (j : Fin m) :
    (strandBraid (LaurentPolynomial.T 1 : LaurentPolynomial ℤ) (LaurentPolynomial.T (-1)) j).map
        (specialise β) = strandBraid (qC (β / 2)) (qC (β / 2))⁻¹ j := by
  rw [strandBraid_map]
  congr 1
  · simp [specialise, LaurentPolynomial.eval₂_T, qUnit]
  · simp [specialise, LaurentPolynomial.eval₂_T, qUnit]

/-- **The bridge for a Laurent-family `HeckeMonodromy` instance.** At every generic `β`, one
invertible `W` conjugates the Jimbo-normalised `n`-body monodromy, on every generator, to the
specialisation at `q = e^{iπβ}` of the single family `Ř_{j,j+1}(q, q⁻¹)` over `ℤ[q, q⁻¹]`.
The family carries the Hecke relations; the substrate enters only through this statement. -/
theorem nbody_monodromy_specialises (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2))) (U : Fin m → ℝ → Mat m)
    (hU : ∀ j, IsTransport (nbodyForm (pairResid permRep α β)) (genPath j) (genPath' j) (U j)) :
    ∃ W : (Mat m)ˣ, ∀ j : Fin m,
      (W : Mat m) * jimboNormalised α β (genMonodromy permRep (U j) j) =
        (strandBraid (LaurentPolynomial.T 1 : LaurentPolynomial ℤ)
          (LaurentPolynomial.T (-1)) j).map (specialise β) * (W : Mat m) := by
  obtain ⟨W, hW⟩ := nbody_monodromy_conj_jimbo hβ hκ U hU
  exact ⟨W, fun j => by rw [specialise_strandBraid]; exact hW j⟩

end Jimbo

/-! ## Bridge A with the Stokes step named -/

section Bridge

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ} {S : Type*} [CommRing S] [Nontrivial S] [Algebra ℂ S]
  [MulSemiringAction (BraidGroup m) S] {ι : Type*} {D : ι → Derivation ℤ S S}

/-- **Named assumption: Stokes → braiding.** The monodromy of a fundamental solution `F` on the
Artin generator `σ_j` is `ρ(s_j)` times the transport of the connection form `Ω` on `Conf_{m+1}`
along the half-turn `γ_j`. For the Lagrangian, `Ω` is the `n`-body form of `𝒟_∇` (P1–P3), and
this is the non-abelian Stokes step. It is a hypothesis, not a theorem. -/
def StokesToBraiding {ω : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (F : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ω)
    (Ω : (Fin (m + 1) → ℂ) → (Fin (m + 1) → ℂ) →L[ℝ] Mat m) : Prop :=
  ∀ j : Fin m, ∃ U : ℝ → Mat m, IsTransport Ω (genPath j) (genPath' j) U ∧
    F.M (σ j) = genMonodromy permRep U j

variable {α β : ℂ}

omit [Nontrivial S] in
/-- Under `StokesToBraiding`, the Lagrangian monodromy on `σ_j` is the KZ holonomy. -/
theorem lagrangian_monodromy_eq_kz (hβ : β ≠ 0)
    {ωL : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωL)
    (hS : StokesToBraiding FL (nbodyForm (pairResid permRep α β))) (j : Fin m) :
    FL.M (σ j) = ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m) := by
  obtain ⟨U, hU, hM⟩ := hS j
  have h := nbody_generator_monodromy (A := Mat m) permRep hβ j hU
  rw [hM, h]

omit [Nontrivial S] in
/-- **`hL`, derived (in its correct, conjugacy form).** Under P1–P3 and `StokesToBraiding`, one
invertible `W` conjugates every Jimbo-normalised Lagrangian generator to `Ř_{j,j+1}(q)`. -/
theorem lagrangian_monodromy_conj_jimbo (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2)))
    {ωL : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωL)
    (hS : StokesToBraiding FL (nbodyForm (pairResid permRep α β))) :
    ∃ W : (Mat m)ˣ, ∀ j : Fin m,
      (W : Mat m) * jimboNormalised α β (FL.M (σ j)) =
        strandBraid (qC (β / 2)) (qC (β / 2))⁻¹ j * (W : Mat m) := by
  obtain ⟨W, hW⟩ := kz_conj_jimbo_complex_σ (m := m) (-α / β) (β / 2) hκ
  refine ⟨W, fun j => ?_⟩
  unfold jimboNormalised
  rw [lagrangian_monodromy_eq_kz hβ FL hS j]
  exact hW j

omit [Nontrivial S] in
/-- The Lagrangian form of `nbody_monodromy_specialises`: under `StokesToBraiding`, the
Jimbo-normalised Lagrangian monodromy is conjugate to the specialisation of the
`ℤ[q, q⁻¹]` family. -/
theorem lagrangian_monodromy_specialises (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2)))
    {ωL : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωL)
    (hS : StokesToBraiding FL (nbodyForm (pairResid permRep α β))) :
    ∃ W : (Mat m)ˣ, ∀ j : Fin m,
      (W : Mat m) * jimboNormalised α β (FL.M (σ j)) =
        (strandBraid (LaurentPolynomial.T 1 : LaurentPolynomial ℤ)
          (LaurentPolynomial.T (-1)) j).map (specialise β) * (W : Mat m) := by
  obtain ⟨W, hW⟩ := lagrangian_monodromy_conj_jimbo hβ hκ FL hS
  exact ⟨W, fun j => by rw [specialise_strandBraid]; exact hW j⟩

/-- **Bridge A, route B, without `hL`.** The Lagrangian connection is algebraically gauge
equivalent to KZ (same coupling and shift), given P1–P3, `StokesToBraiding`, Deligne full
faithfulness, and a KZ fundamental solution with the KZ holonomy. The intertwiner is `1`: the
two monodromies agree on the generators, hence everywhere. -/
theorem lagrangian_gauge_to_KZ_of_stokes (hβ : β ≠ 0)
    (hDK : ∀ j (z : ℂ), D j (algebraMap ℂ S z) = 0)
    (hΓK : ∀ (γ : BraidGroup m) (z : ℂ), γ • algebraMap ℂ S z = algebraMap ℂ S z)
    (R : Type*) [CommRing R] [Algebra R S] (hinj : Function.Injective (algebraMap R S))
    {ωKZ ωL : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (FKZ : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωKZ)
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωL)
    (hKZ : ∀ j : Fin m,
      FKZ.M (σ j) = ((kzBraidRep permRep (β / 2) (-α / β) (σ j) : (Mat m)ˣ) : Mat m))
    (hS : StokesToBraiding FL (nbodyForm (pairResid permRep α β)))
    (hFF₁ : DeligneFullyFaithful D R (BraidGroup m) ωKZ ωL)
    (hFF₂ : DeligneFullyFaithful D R (BraidGroup m) ωL ωKZ) :
    ∃ g gInv : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R,
      g * gInv = 1 ∧ gInv * g = 1 ∧
      ∀ j, (g.map (algebraMap R S)).map (D j)
        = ωL j * g.map (algebraMap R S) - g.map (algebraMap R S) * ωKZ j := by
  have hinjK : Function.Injective (algebraMap ℂ S) := (algebraMap ℂ S).injective
  have hC : ∀ γ, FL.M γ * (1 : Mat m) = (1 : Mat m) * FKZ.M γ :=
    intertwine_of_closure hΓK hinjK FKZ FL _ closure_range_σ (by
      rintro _ ⟨j, rfl⟩
      rw [lagrangian_monodromy_eq_kz hβ FL hS j, hKZ j, Matrix.mul_one, Matrix.one_mul])
  exact gauge_of_conj_monodromy hDK hΓK R hinj FKZ FL (1 : Mat m) (1 : Mat m)
    (Matrix.mul_one 1) (Matrix.mul_one 1) hC hFF₁ hFF₂

end Bridge

/-! ## Colour singlets: the Hecke quadratic survives as `(X + 1)(X − q⁻²) = 0` -/

section Singlet

open QOU.Braiding.ColourFlavourMirror QOU.Braiding.JimboGl3Singlet

variable {K : Type*} [Field K] {M : Type*} [AddCommGroup M] [Module K M]

theorem pure_add (e : T3 K) (f g : M) : Braiding.ColourFlavourMirror.pure e (f + g) = Braiding.ColourFlavourMirror.pure e f + Braiding.ColourFlavourMirror.pure e g := by
  funext a b c; simp [Braiding.ColourFlavourMirror.pure, smul_add]

theorem pure_smul (e : T3 K) (r : K) (f : M) : Braiding.ColourFlavourMirror.pure e (r • f) = r • Braiding.ColourFlavourMirror.pure e f := by
  funext a b c; simp [Braiding.ColourFlavourMirror.pure, smul_comm (e a b c) r f]

/-- The flavour Hecke quadratic in Jimbo normalisation. -/
def FlavourHecke (q : K) (B : M →ₗ[K] M) : Prop := ∀ f, B (B f) = (q - q⁻¹) • B f + f

theorem singlet_sq_aux (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (hB : FlavourHecke q B) (f : M) :
    (-q⁻¹) • B ((-q⁻¹) • B f) = (-(1 - q⁻¹ ^ 2)) • ((-q⁻¹) • B f) + (q⁻¹ ^ 2) • f := by
  rw [map_smul, hB f]
  match_scalars <;> field_simp

/-- **On the colour singlet, `X₁₂` satisfies `(X + 1)(X − q⁻²) = 0`** once the flavour
operator satisfies the Hecke quadratic. -/
theorem singlet_quadratic_12 (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (hB : FlavourHecke q B)
    (f : M) :
    X12 q B (X12 q B (Braiding.ColourFlavourMirror.pure (eps q) f)) =
      (-(1 - q⁻¹ ^ 2)) • X12 q B (Braiding.ColourFlavourMirror.pure (eps q) f) + (q⁻¹ ^ 2) • Braiding.ColourFlavourMirror.pure (eps q) f := by
  rw [X12_singlet q hq, X12_singlet q hq, ← pure_smul, ← pure_smul, ← pure_add,
    singlet_sq_aux q hq B hB f]

theorem singlet_quadratic_23 (q : K) (hq : q ≠ 0) (B : M →ₗ[K] M) (hB : FlavourHecke q B)
    (f : M) :
    X23 q B (X23 q B (Braiding.ColourFlavourMirror.pure (eps q) f)) =
      (-(1 - q⁻¹ ^ 2)) • X23 q B (Braiding.ColourFlavourMirror.pure (eps q) f) + (q⁻¹ ^ 2) • Braiding.ColourFlavourMirror.pure (eps q) f := by
  rw [X23_singlet q hq, X23_singlet q hq, ← pure_smul, ← pure_smul, ← pure_add,
    singlet_sq_aux q hq B hB f]

/-- **Named assumption: the colour tube is braided.** The strand monodromies `T₁, T₂` on
colour ⊗ flavour are `Ř_colour ⊗ B₁` and `Ř_colour ⊗ B₂`, with `B_i` the flavour monodromy
(`conj:colour-tube-monodromy-braided`, bean `qou-et5f`). A hypothesis, not a theorem. -/
def ColourTubeBraided (q : K) (B₁ B₂ : M →ₗ[K] M) (T₁ T₂ : St M → St M) : Prop :=
  T₁ = X12 q B₁ ∧ T₂ = X23 q B₂

end Singlet

section SingletBridge

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

open QOU.Braiding.ColourFlavourMirror QOU.Braiding.JimboGl3Singlet

variable {α β : ℂ}

/-- The flavour operator of a three-strand matrix, acting on `(ℂ²)^{⊗3}` as vectors. -/
noncomputable def flav (G : Mat 2) : ((Fin 3 → Fin 2) → ℂ) →ₗ[ℂ] ((Fin 3 → Fin 2) → ℂ) :=
  Matrix.toLin' G

theorem flavourHecke_of_matrix {q : ℂ} {G : Mat 2}
    (hG : G * G = (q - q⁻¹) • G + (1 : ℂ) • (1 : Mat 2)) : FlavourHecke q (flav G) := by
  intro f
  simp only [flav, Matrix.toLin'_apply, Matrix.mulVec_mulVec, hG, Matrix.add_mulVec,
    Matrix.smul_mulVec, Matrix.one_mulVec, one_smul]

/-- **Bridge A on colour singlets (three strands).** Under P1–P3 for flavour, the named
assumption `ColourTubeBraided` for colour, and `q = e^{iπβ}` not a root of unity:
* each strand monodromy, restricted to colour singlets, satisfies `(X + 1)(X − q⁻²) = 0`;
* a singlet `ε_q ⊗ f` is q-exterior iff `f` is totally q-symmetric for the derived flavour
  monodromies.
The flavour monodromies are the Jimbo-normalised transports of the `n`-body form; their Hecke
quadratic is proved above (`nbody_monodromy_hecke`), not assumed. -/
theorem lagrangian_singlet_bridge (hβ : β ≠ 0)
    (hκ : GenericParameter.NotRootOfUnity (qC (β / 2))) (U : Fin 2 → ℝ → Mat 2)
    (hU : ∀ j, IsTransport (nbodyForm (pairResid permRep α β)) (genPath j) (genPath' j) (U j))
    (T₁ T₂ : St ((Fin 3 → Fin 2) → ℂ) → St ((Fin 3 → Fin 2) → ℂ))
    (hCT : ColourTubeBraided (qC (β / 2))
      (flav (jimboNormalised α β (genMonodromy permRep (U 0) 0)))
      (flav (jimboNormalised α β (genMonodromy permRep (U 1) 1))) T₁ T₂)
    (f : (Fin 3 → Fin 2) → ℂ) :
    T₁ (T₁ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f)) =
        (-(1 - (qC (β / 2))⁻¹ ^ 2)) • T₁ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f) +
          ((qC (β / 2))⁻¹ ^ 2) • Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f ∧
      T₂ (T₂ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f)) =
        (-(1 - (qC (β / 2))⁻¹ ^ 2)) • T₂ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f) +
          ((qC (β / 2))⁻¹ ^ 2) • Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f ∧
      ((T₁ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f) = -Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f ∧
          T₂ (Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f) = -Braiding.ColourFlavourMirror.pure (eps (qC (β / 2))) f) ↔
        (flav (jimboNormalised α β (genMonodromy permRep (U 0) 0)) f = qC (β / 2) • f ∧
          flav (jimboNormalised α β (genMonodromy permRep (U 1) 1)) f = qC (β / 2) • f)) := by
  have hq := qC_ne_zero (β / 2)
  obtain ⟨h1, h2⟩ := hCT
  subst h1 h2
  have H : ∀ j : Fin 2, FlavourHecke (qC (β / 2))
      (flav (jimboNormalised α β (genMonodromy permRep (U j) j))) := fun j =>
    flavourHecke_of_matrix (nbody_monodromy_hecke hβ hκ U hU j)
  exact ⟨singlet_quadratic_12 _ hq _ (H 0) f, singlet_quadratic_23 _ hq _ (H 1) f,
    singlet_exterior_iff _ hq _ _ f⟩

end SingletBridge

end QOU.Mass.BridgeAStokes
