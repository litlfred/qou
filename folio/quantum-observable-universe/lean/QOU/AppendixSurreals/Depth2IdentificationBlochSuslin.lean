import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic

/-!
# Depth-2 identification: G^(2)(H_q) ≅ K_3^ind(F) ⊗ ℚ

Compiled formalisation of `prop:depth-2-identification-bloch-suslin`.

Models the commutative diagram of `ℚ`-vector spaces from the four-step
Bloch–Suslin proof chain:
1. **Bloch generation (`blochGen`)**: the depth-2 grouplike space
   `G2modP1` (`G^{(2)}(H_q)|_F / P_1`) surjects onto the rationalized Bloch
   group `B_F` (`𝔅(F) ⊗ ℚ`) via the dilogarithm generators `Li_2^q(z)`.
2. **Suslin's isomorphism (`suslinIso`)**: `B_F ≃ₗ[ℚ] K3_F`
   (`𝔅(F) ⊗ ℚ ≅ K_3^{\mathrm{ind}}(F) ⊗ ℚ`, Suslin 1986).
3. **Bloch–Suslin regulator (`regulator`)**: an injective `ℚ`-linear map
   `K3_F →ₗ[ℚ] Target` (`K_3^{\mathrm{ind}}(F) ⊗ ℚ → ℝ / π²ℚ`, Borel + Suslin).
4. **Archimedean evaluation (`tauArch`)**: `G2modP1 →ₗ[ℚ] Target`
   commuting with `regulator ∘ suslinIso ∘ blochGen`
   (`τ_arch(Li_2^q(z)) ≡ D(z) (mod π²ℚ)`).

From these structural hypotheses (`Function.Surjective blochGen`,
`Function.Injective regulator`, and `tauArch = regulator ∘ suslinIso ∘ blochGen`),
we **derive**:
- `tauArch_range_eq_regulator_range`: the archimedean image
  `LinearMap.range tauArch` coincides identically with the Bloch–Suslin
  regulator image `LinearMap.range regulator`;
- `ker_tauArch_eq_ker_blochGen`: the kernel of `tauArch` is exactly the kernel
  of `blochGen` (the 5-term dilogarithm relations);
- `quotKerEquivK3`: a canonical `ℚ`-linear isomorphism
  `(G2modP1 ⧸ LinearMap.ker tauArch) ≃ₗ[ℚ] K3_F`;
- `depth_2_identification`: both the range equality
  `LinearMap.range tauArch = LinearMap.range regulator` and the dimension
  equality `Module.finrank ℚ (G2modP1 ⧸ LinearMap.ker tauArch) = Module.finrank ℚ K3_F`
  (equal to the Borel rank `r₂`).
-/

namespace QOU.AppendixSurreals.Depth2IdentificationBlochSuslin

/-- Structural context for the 4-step Bloch–Suslin depth-2 identification
    diagram over `ℚ`. All fields are the upstream mathematical ingredients
    (Bloch generation, Suslin isomorphism, Borel–Suslin regulator injectivity,
    and diagram commutativity); the range equality, quotient isomorphism, and
    finrank equality are **derived** below. -/
class Depth2IdentificationContext where
  /-- Depth-2 grouplike space modulo depth-1 periods: `G^{(2)}(H_q)|_F / P_1`. -/
  G2modP1 : Type
  /-- Rationalized Bloch group: `𝔅(F) ⊗ ℚ`. -/
  B_F : Type
  /-- Rationalized indecomposable K-group: `K_3^{\mathrm{ind}}(F) ⊗ ℚ`. -/
  K3_F : Type
  /-- Regulator target period quotient: `ℝ / π²ℚ` (as a `ℚ`-vector space). -/
  Target : Type
  [addCommGroupG2 : AddCommGroup G2modP1]
  [moduleG2 : Module ℚ G2modP1]
  [addCommGroupBF : AddCommGroup B_F]
  [moduleBF : Module ℚ B_F]
  [addCommGroupK3 : AddCommGroup K3_F]
  [moduleK3 : Module ℚ K3_F]
  [addCommGroupTarget : AddCommGroup Target]
  [moduleTarget : Module ℚ Target]
  /-- Step 1: Surjective projection from depth-2 grouplikes onto the Bloch group `𝔅(F) ⊗ ℚ`. -/
  blochGen : G2modP1 →ₗ[ℚ] B_F
  blochGen_surjective : Function.Surjective blochGen
  /-- Step 2: Suslin's theorem `𝔅(F) ⊗ ℚ ≃ₗ[ℚ] K_3^{\mathrm{ind}}(F) ⊗ ℚ`. -/
  suslinIso : B_F ≃ₗ[ℚ] K3_F
  /-- Step 3: Bloch–Suslin regulator `K_3^{\mathrm{ind}}(F) ⊗ ℚ →ₗ[ℚ] Target`, rationally injective (Borel). -/
  regulator : K3_F →ₗ[ℚ] Target
  regulator_injective : Function.Injective regulator
  /-- Step 4: Archimedean evaluation `τ_arch : G^{(2)}(H_q)|_F / P_1 →ₗ[ℚ] Target`
      factoring through the Bloch–Wigner dilogarithm on `𝔅(F) ⊗ ℚ`. -/
  tauArch : G2modP1 →ₗ[ℚ] Target
  diagram_commutes : ∀ x : G2modP1, tauArch x = regulator (suslinIso (blochGen x))

attribute [instance]
  Depth2IdentificationContext.addCommGroupG2
  Depth2IdentificationContext.moduleG2
  Depth2IdentificationContext.addCommGroupBF
  Depth2IdentificationContext.moduleBF
  Depth2IdentificationContext.addCommGroupK3
  Depth2IdentificationContext.moduleK3
  Depth2IdentificationContext.addCommGroupTarget
  Depth2IdentificationContext.moduleTarget

variable [ctx : Depth2IdentificationContext]

/-- The composite map `suslinIso ∘ blochGen : G2modP1 →ₗ[ℚ] K3_F`. -/
def toK3 : ctx.G2modP1 →ₗ[ℚ] ctx.K3_F :=
  ctx.suslinIso.toLinearMap.comp ctx.blochGen

/-- `toK3` is surjective because `blochGen` is surjective and `suslinIso` is an equivalence. -/
theorem toK3_surjective : Function.Surjective toK3 :=
  ctx.suslinIso.surjective.comp ctx.blochGen_surjective

/-- `tauArch` factors as `regulator ∘ toK3`. -/
theorem tauArch_eq_regulator_comp_toK3 :
    ctx.tauArch = ctx.regulator.comp toK3 := by
  ext x
  exact ctx.diagram_commutes x

/-- **Derived image equality:** the archimedean image of `G^{(2)}(H_q)|_F / P_1`
    equals the Bloch–Suslin regulator image of `K_3^{\mathrm{ind}}(F) ⊗ ℚ`. -/
theorem tauArch_range_eq_regulator_range :
    LinearMap.range ctx.tauArch = LinearMap.range ctx.regulator := by
  ext y
  simp only [LinearMap.mem_range]
  constructor
  · rintro ⟨x, rfl⟩
    exact ⟨ctx.suslinIso (ctx.blochGen x), (ctx.diagram_commutes x).symm⟩
  · rintro ⟨k, rfl⟩
    obtain ⟨x, hx⟩ := toK3_surjective k
    refine ⟨x, ?_⟩
    rw [ctx.diagram_commutes x]
    change ctx.regulator (toK3 x) = ctx.regulator k
    rw [hx]

/-- **Derived kernel identification:** because `regulator` is injective, the kernel
    of `tauArch` coincides with the kernel of `toK3` (and of `blochGen`). -/
theorem ker_tauArch_eq_ker_toK3 :
    LinearMap.ker ctx.tauArch = LinearMap.ker toK3 := by
  ext x
  simp only [LinearMap.mem_ker, ctx.diagram_commutes x]
  change ctx.regulator (toK3 x) = 0 ↔ toK3 x = 0
  constructor
  · intro h
    apply ctx.regulator_injective
    rw [h, map_zero]
  · intro h
    rw [h, map_zero]

/-- **Canonical quotient isomorphism:** `(G2modP1 ⧸ ker tauArch) ≃ₗ[ℚ] K_3^{\mathrm{ind}}(F) ⊗ ℚ`
    induced by `toK3` via the First Isomorphism Theorem. -/
noncomputable def quotKerEquivK3 :
    (ctx.G2modP1 ⧸ LinearMap.ker ctx.tauArch) ≃ₗ[ℚ] ctx.K3_F :=
  (Submodule.quotEquivOfEq _ _ ker_tauArch_eq_ker_toK3).trans
    (toK3.quotKerEquivOfSurjective toK3_surjective)

/-- **Proposition (`prop:depth-2-identification-bloch-suslin`).**
    From the 4-step Bloch–Suslin commutative diagram, the archimedean image of
    `G^{(2)}(H_q)|_F / P_1` coincides with the Bloch–Suslin regulator image of
    `K_3^{\mathrm{ind}}(F) ⊗ ℚ`, and the quotient by `ker τ_arch` has the exact
    same `ℚ`-dimension (`Module.finrank ℚ`) as `K_3^{\mathrm{ind}}(F) ⊗ ℚ`. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/depth-2-identification-bloch-suslin.md
theorem depth_2_identification :
    LinearMap.range ctx.tauArch = LinearMap.range ctx.regulator ∧
    Module.finrank ℚ (ctx.G2modP1 ⧸ LinearMap.ker ctx.tauArch) =
      Module.finrank ℚ ctx.K3_F :=
  ⟨tauArch_range_eq_regulator_range, quotKerEquivK3.finrank_eq⟩

end QOU.AppendixSurreals.Depth2IdentificationBlochSuslin
