import QOU.Core.CategoricalFoundations
import QOU.Core.VolumeFormDegree
import QOU.StandardModel.OctonionColourTripletComplexType

/-!
# QOU.Core.FlavouredQuantumObservableUniverse — the flavour fundamental `W` as an axiom datum

**Owner ruling 2026-11-27** (bean `qou-j3w6`, option A; supersedes owner decision 4d of
2026-10-10): keep condition (iii) of `def:quantum-observable-universe` as it is
(`Λ²V ≅ 𝟙`, so the fibre has `N = 2`) and add a **second fundamental object** `W` with
`Λ³W ≅ 𝟙`.

**This is an axiom datum, not a derivation.**  Nothing below produces `W` from the
substrate.  Every flavour-`SU(3)` statement that consumes this structure is a consequence of
the *extended* axioms, and the honest label is "flavour `SU(3)_f` is postulated".  The
anti-laundering rule of the corpus applies: do not cite a result proved from this structure
as "derived from QOU".

## The fields

`W` comes with the same three pieces of data that condition (iii) attaches to `V`, one
degree up, plus the property that the eightfold way actually needs:

* `exteriorCube`, a quotient `π₃ : (W ⊗ W) ⊗ W ↠ Λ³W` (same convention as
  `exteriorSquare`: deliberately no braiding eigenvalue condition, so `q` stays free);
* `flavourVolumeIso : Λ³W ≅ 𝟙`, the `SL(3)`-type volume form;
* `flavour_not_selfDual : Hom(𝟙, W ⊗ W)` is trivial — `W` carries no invariant pairing, so
  `W ≇ W^∨`.

## Why the last field is part of the datum

Without it the datum is satisfied **inside the fibre's own category**: the spin-1 object
`V₁ = Sym²V` is, at `q = 1`, 3-dimensional with `Λ³V₁ ≅ 𝟙`.  But `V₁` is self-dual, its
symmetric square carries the Killing form, and it gives `SO(3)`, not `SU(3)`.  The
non-self-duality field excludes it, and by `Sym2GateComplexType` / `Sym2GateMultiplicity`
(every `SU(2)` irrep is self-dual) it excludes **every** object of the single-fibre category.
So the datum forces genuinely new structure, which is the content of the `N = 3` problem.

## What is proved here

* `flavourVolume_hom_ne_zero` — the flavour volume form is not zero (non-vacuity, as for `V`).
* `epi_flavourProj_comp_volume` — `(W ⊗ W) ⊗ W` surjects onto the unit.
* `flavour_fibre_rank_three` — at the level of a fibre of dimension `n`, `Λ³ ≅ 𝟙` forces
  `n = 3` (`C(n,3) = 1 ↔ n = 3`), as `Λ²V ≅ 𝟙` forces `N = 2`.
* `fibre_and_flavour_ranks` — the two volume forms cannot sit on one object: `C(n,2) = 1`
  and `C(n,3) = 1` are incompatible, so `V` and `W` are different objects.
* `octonionTriple_realises_not_selfDual` — **the non-self-duality clause is realised** by the
  octonionic colour triple (`OctonionColourTripletComplexType`): over `ℚ`, it carries no
  nonzero `𝔰𝔲(3)`-invariant `ℂ`-bilinear pairing.  This is a linear-algebra model of the
  clause, not an instance of the structure (this tree still has no instance of
  `QuantumObservableUniverse`).
-/

namespace QOU

open CategoryTheory MonoidalCategory
open QOU.QuantumObservableUniverse.VolumeFormDegree

universe u v

/-- **Flavoured quantum observable universe** (owner ruling 2026-11-27, axiom datum).

A quantum observable universe together with a second fundamental object `W` carrying an
`SL(3)`-type volume form `Λ³W ≅ 𝟙` and no invariant self-pairing. -/
structure FlavouredQuantumObservableUniverse (R : Type*) [CommRing R]
    extends QuantumObservableUniverse.{u, v} R where
  /-- The flavour fundamental `W`.  **Postulated.** -/
  flavourObj : C
  /-- The exterior cube `Λ³W`, as a quotient of `W^{⊗3}` (next two fields). -/
  exteriorCube : C
  /-- The antisymmetrisation `π₃ : (W ⊗ W) ⊗ W ↠ Λ³W`. -/
  exteriorCubeProj : ((flavourObj ⊗ flavourObj) ⊗ flavourObj) ⟶ exteriorCube
  /-- `Λ³W` is a quotient of `W^{⊗3}`.  No braiding eigenvalue condition, as for `Λ²V`. -/
  exteriorCube_epi : Epi exteriorCubeProj
  /-- **Flavour volume constraint**: `Λ³W ≅ 𝟙` (iso reading, as condition (iii) for `V`). -/
  flavourVolumeIso : exteriorCube ≅ (𝟙_ C)
  /-- **`W` is not self-dual**: every morphism `𝟙 → W ⊗ W` is equal to every other, i.e.
  `Hom(𝟙, W ⊗ W) = 0` in the linear category.  Excludes `Sym²V` and every other object of
  the single-fibre category. -/
  flavour_not_selfDual : Subsingleton ((𝟙_ C) ⟶ (flavourObj ⊗ flavourObj))
  /-- **Twist scalar on `W`**: `θ_W = t • 𝟙_W`. -/
  flavourTwistScalar : R
  twist_flavour : _root_.QOU.MathlibExt.BalancedCategory.twist flavourObj
    = flavourTwistScalar • 𝟙 flavourObj
  /-- The scalar `c` by which each adjacent crossing acts on `Λ³W`. -/
  flavourBraidScalar : R
  /-- **`Λ³W` is an antisymmetric quotient** (adopted 2026-11-27, proposal
      `docs/audits/2026-11-27-pin-exterior-quotients-proposal.md`): the first crossing acts
      by `c`. -/
  exteriorCube_antisym₁ : (β_ flavourObj flavourObj).hom ▷ flavourObj ≫ exteriorCubeProj
    = flavourBraidScalar • exteriorCubeProj
  /-- The second crossing acts by the same `c`. -/
  exteriorCube_antisym₂ : (α_ flavourObj flavourObj flavourObj).hom ≫
      flavourObj ◁ (β_ flavourObj flavourObj).hom ≫ (α_ flavourObj flavourObj flavourObj).inv ≫
      exteriorCubeProj = flavourBraidScalar • exteriorCubeProj
  /-- **`c` is not the symmetric value `1`**: `1 - c` acts without torsion on `End 𝟙`.  Without
      it a one-dimensional `W` with trivial braiding (`c = 1`) met every field
      (`FlavourLabelCarrier.unit_flavour_meets_axioms`).  The normalisation of `c` is fixed by
      the twist only up to a cube root of unity, `(c²t)³ = 1`
      (`ExteriorQuotientNormalisation.exteriorCube_balancing_unit`); no field chooses the root. -/
  flavourBraid_regular : ∀ f : 𝟙_ C ⟶ 𝟙_ C, (1 - flavourBraidScalar) • f = 0 → f = 0

namespace FlavouredQuantumObservableUniverse

variable {R : Type*} [CommRing R] (F : FlavouredQuantumObservableUniverse.{u, v} R)

attribute [local instance] QuantumUniverse.catInst QuantumUniverse.monInst
  QuantumUniverse.preInst

/-- The flavour volume form is not zero whenever `𝟙` has a nonzero identity. -/
theorem flavourVolume_hom_ne_zero
    (h : (CategoryStruct.id (𝟙_ F.C)) ≠ 0) : F.flavourVolumeIso.hom ≠ 0 :=
  iso_unit_hom_ne_zero F.flavourVolumeIso h

/-- `W ⊗ W ⊗ W` surjects onto the unit through `Λ³W`. -/
theorem epi_flavourProj_comp_volume :
    Epi (C := F.C) (F.exteriorCubeProj ≫ F.flavourVolumeIso.hom) := by
  haveI := F.exteriorCube_epi
  exact epi_comp _ _

end FlavouredQuantumObservableUniverse

/-! ## Fibre-level consequences (dimension arithmetic, as for `V`) -/

/-- At the level of a fibre of dimension `n`, the flavour volume form forces `n = 3`. -/
theorem flavour_fibre_rank_three {n : ℕ} (h : extPowerDim n 3 = 1) : n = 3 :=
  degree_three_forces_rank_three h

/-- The two volume constraints cannot hold on one fibre: `V` and `W` are different objects. -/
theorem fibre_and_flavour_ranks {n : ℕ} (h2 : extPowerDim n 2 = 1) :
    extPowerDim n 3 ≠ 1 := by
  intro h3
  have := degree_two_forces_rank_two h2
  have := degree_three_forces_rank_three h3
  omega

/-! ## A model of the non-self-duality clause -/

open QOU.MathlibExt.OctonionDerivations QOU.StandardModel
  QOU.StandardModel.ColourTripletComplexType in
/-- The octonionic colour triple realises the clause `flavour_not_selfDual` at the level of
linear algebra over `ℚ`: it carries no nonzero `𝔰𝔲(3)`-invariant `ℂ`-bilinear pairing
`𝟑 ⊗ 𝟑 → 𝟏`.  (Whether *flavour* and *colour* triples coincide is the separate open item
"flavour versus colour".) -/
theorem octonionTriple_realises_not_selfDual :
    ¬ ∃ B : Matrix (Fin 6) (Fin 6) ℚ, B ≠ 0 ∧
      (∀ x y, β B (J6 x) y = β B x (J6 y)) ∧
      (∀ D : ↥(su3 stdIm), ∀ x y,
        β B (su3ToEndTriplet D x) y + β B x (su3ToEndTriplet D y) = 0) :=
  colourTriple_not_selfConjugate

end QOU
