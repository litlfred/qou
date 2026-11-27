import QOU.Core.FlavouredQuantumObservableUniverse
import Mathlib.CategoryTheory.Monoidal.Linear

/-!
# QOU.Core.FlavourCentralPhase — the non-self-duality of `W` from a central cube-root phase

Bean `qou-x08k` (epic: construct the flavour fundamental `W` from the aether).

`FlavouredQuantumObservableUniverse` postulates `W` with three properties: `Λ³W` is a
quotient of `W^{⊗3}`, `Λ³W ≅ 𝟙`, and `Hom(𝟙, W ⊗ W) = 0`.  The last one is a bare vanishing
statement.  This file replaces it by a *reason*: a **central phase**, i.e. a monoidal
natural automorphism `z` of the identity functor, acting on `W` by a scalar `ω`.

## Results (all over a generic commutative ring `R`, sorry-free)

* `phase_pow_of_volume` — **degree-`n` volume forces `ωⁿ = 1`**.  If `W^{⊗n} ↠ 𝟙` and
  `z_W = ω • 𝟙`, then `(ωⁿ - 1) • 𝟙_𝟙 = 0`.  Applied at `n = 3` (the flavour volume form)
  the phase is a cube root of unity; at `n = 2` (condition (iii) for `V`) it is a square
  root of unity.  The phase is *not chosen*: the volume form fixes its order.
* `not_selfDual_of_phase` — **phase gives non-self-duality**.  If `1 - ω²` acts without
  torsion on `Hom(𝟙, W ⊗ W)`, every morphism `𝟙 → W ⊗ W` is zero.
* `fundamental_phase_cannot_separate` — on `V` the same argument gives `ω² = 1`, so a
  central phase can **never** separate `V` from its dual.  This is the central-phase form
  of "the single fibre is self-dual": order-2 phases are useless, and the first degree whose
  volume form admits a useful phase is `n = 3`.
* `FlavouredQuantumObservableUniverse.ofCentralPhase` — a constructor: a quantum observable
  universe plus `W`, `π₃`, `Λ³W ≅ 𝟙` and a central phase with `1 - ω²` regular on
  `Hom(𝟙, W ⊗ W)` **is** a flavoured quantum observable universe.

## Honest label

This is a **reduction of the axiom datum, not a derivation of `W`**.  The field
`flavour_not_selfDual` is traded for "W carries a central phase of order 3" (the `N`-ality
of `SU(3)`).  The object `W` and the phase are still supplied, not built from
`(C, A, τ)` and `q`.  Over `R = ℤ[ω]` the element `1 - ω²` has norm `3` and is not a unit,
which is why the hypothesis is regularity (no torsion) rather than invertibility.

The phase is not the balancing twist `θ`: `θ` is natural but **not** monoidal
(`θ_{X⊗Y} = (θ_X ⊗ θ_Y) ∘ c_{Y,X} ∘ c_{X,Y}`), so the twist of the aether does not supply it.
Whether the aether's grouplikes can supply an order-3 central phase is the remaining open
step; `fundamental_phase_cannot_separate` shows the `SU(2)` centre `{±1}` cannot.
-/

namespace QOU.FlavourCentralPhase

open CategoryTheory MonoidalCategory

universe v u

/-- A **central phase**: a monoidal natural automorphism of the identity functor, written
as its components.  (Invertibility of the components is not needed below.) -/
structure CentralPhase (C : Type u) [Category.{v} C] [MonoidalCategory C] where
  /-- The component at `X`. -/
  app : ∀ X : C, X ⟶ X
  /-- Naturality: `z` commutes with every morphism. -/
  naturality : ∀ {X Y : C} (f : X ⟶ Y), app X ≫ f = f ≫ app Y
  /-- `z` is trivial on the unit. -/
  app_unit : app (𝟙_ C) = 𝟙 _
  /-- `z` is monoidal. -/
  app_tensor : ∀ X Y : C, app (X ⊗ Y) = app X ⊗ₘ app Y

section

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]
  [Preadditive C] [Linear R C] [MonoidalPreadditive C] [MonoidalLinear R C]

/-- Tensoring two scalar morphisms multiplies the scalars. -/
theorem smul_id_tensor_smul_id (a b : R) (X Y : C) :
    ((a • 𝟙 X) ⊗ₘ (b • 𝟙 Y)) = (a * b) • 𝟙 (X ⊗ Y) := by
  rw [tensorHom_def, MonoidalLinear.smul_whiskerRight, MonoidalLinear.whiskerLeft_smul,
    Linear.smul_comp, Linear.comp_smul, smul_smul, id_whiskerRight, whiskerLeft_id,
    Category.id_comp, mul_comm]

/-- The tensor power `W^{⊗n}`, bracketed to the left: `W^{⊗0} = 𝟙`, `W^{⊗(n+1)} = W^{⊗n} ⊗ W`. -/
def tpow (W : C) : ℕ → C
  | 0 => 𝟙_ C
  | n + 1 => tpow W n ⊗ W

/-- On `W^{⊗n}` the phase acts by `ωⁿ`. -/
theorem app_tpow (z : CentralPhase C) {W : C} {ω : R} (hW : z.app W = ω • 𝟙 W) :
    ∀ n, z.app (tpow W n) = ω ^ n • 𝟙 (tpow W n)
  | 0 => by simp [tpow, z.app_unit]
  | n + 1 => by
    simp only [tpow]
    rw [z.app_tensor, app_tpow z hW n, hW, smul_id_tensor_smul_id, pow_succ]

/-- **Degree-`n` volume forces `ωⁿ = 1`** (on `End 𝟙`).  If some epimorphism
`W^{⊗n} ↠ 𝟙` exists, the phase scalar satisfies `(ωⁿ - 1) • 𝟙_𝟙 = 0`. -/
theorem phase_pow_of_volume (z : CentralPhase C) {W : C} {ω : R} (hW : z.app W = ω • 𝟙 W)
    {n : ℕ} (g : tpow W n ⟶ 𝟙_ C) [Epi g] : (ω ^ n - 1) • 𝟙 (𝟙_ C) = 0 := by
  have hnat := z.naturality g
  rw [app_tpow z hW n, z.app_unit, Linear.smul_comp, Category.id_comp, Category.comp_id] at hnat
  have : g ≫ ((ω ^ n - 1) • 𝟙 (𝟙_ C)) = g ≫ 0 := by
    rw [Linear.comp_smul, Category.comp_id, sub_smul, hnat, one_smul, sub_self,
      Limits.comp_zero]
  exact (cancel_epi g).1 this

/-- **A central phase with `1 - ω²` regular separates `W` from its dual**:
`Hom(𝟙, W ⊗ W)` is a subsingleton. -/
theorem not_selfDual_of_phase (z : CentralPhase C) {W : C} {ω : R}
    (hW : z.app W = ω • 𝟙 W)
    (hreg : ∀ f : 𝟙_ C ⟶ W ⊗ W, (1 - ω ^ 2) • f = 0 → f = 0) :
    Subsingleton (𝟙_ C ⟶ W ⊗ W) := by
  have key : ∀ f : 𝟙_ C ⟶ W ⊗ W, f = 0 := by
    intro f
    apply hreg
    have hnat := z.naturality f
    rw [z.app_unit, Category.id_comp, z.app_tensor, hW, smul_id_tensor_smul_id,
      Linear.comp_smul, Category.comp_id] at hnat
    rw [sub_smul, one_smul, pow_two, ← hnat, sub_self]
  exact ⟨fun f g => by rw [key f, key g]⟩

/-- **A central phase cannot separate a fundamental with a degree-2 volume form.**  If
`V ⊗ V ↠ 𝟙` (condition (iii)) and `z_V = ω • 𝟙`, then `(ω² - 1) • 𝟙_𝟙 = 0`; whenever
`R` acts faithfully on `End 𝟙` this is `ω² = 1`, so `1 - ω² = 0` and the hypothesis of
`not_selfDual_of_phase` fails for every nonzero hom-module. -/
theorem fundamental_phase_cannot_separate (z : CentralPhase C) {V : C} {ω : R}
    (hV : z.app V = ω • 𝟙 V) (g : V ⊗ V ⟶ 𝟙_ C) [Epi g]
    (hfaith : ∀ r : R, r • 𝟙 (𝟙_ C) = 0 → r = 0) : ω ^ 2 = 1 := by
  have hpow : z.app (V ⊗ V) = ω ^ 2 • 𝟙 (V ⊗ V) := by
    rw [z.app_tensor, hV, smul_id_tensor_smul_id, pow_two]
  have hnat := z.naturality g
  rw [hpow, z.app_unit, Linear.smul_comp, Category.id_comp, Category.comp_id] at hnat
  have : g ≫ ((ω ^ 2 - 1) • 𝟙 (𝟙_ C)) = g ≫ 0 := by
    rw [Linear.comp_smul, Category.comp_id, sub_smul, hnat, one_smul, sub_self,
      Limits.comp_zero]
  exact sub_eq_zero.1 (hfaith _ ((cancel_epi g).1 this))

/-- **Order bookkeeping.**  If `ω³ = 1` and `ω² = 1` then `ω = 1`: a phase compatible with
both volume forms on one object is trivial.  (Together with `fibre_and_flavour_ranks`.) -/
theorem phase_cube_and_square {ω : R} (h3 : ω ^ 3 = 1) (h2 : ω ^ 2 = 1) : ω = 1 := by
  have : ω ^ 3 = ω * ω ^ 2 := by ring
  rw [this, h2, mul_one] at h3
  exact h3

end

end QOU.FlavourCentralPhase

namespace QOU.FlavouredQuantumObservableUniverse

universe u v

open CategoryTheory MonoidalCategory QOU.FlavourCentralPhase

attribute [local instance] QuantumUniverse.catInst QuantumUniverse.monInst
  QuantumUniverse.preInst QuantumUniverse.linInst

/-- **Constructor from a central phase.**  A quantum observable universe, an object `W` with
`π₃ : W^{⊗3} ↠ Λ³W ≅ 𝟙`, and a central phase acting on `W` by `ω` with `1 - ω²` regular on
`Hom(𝟙, W ⊗ W)`, form a flavoured quantum observable universe.  The non-self-duality field
is *proved*, not postulated.  (`W` and the phase are still data: see the module doc.) -/
def ofCentralPhase {R : Type*} [CommRing R] (Q : QuantumObservableUniverse.{u, v} R)
    [MonoidalPreadditive Q.C] [MonoidalLinear R Q.C]
    (W L3 : Q.C) (π₃ : (W ⊗ W) ⊗ W ⟶ L3) [Epi π₃] (vol : L3 ≅ 𝟙_ Q.C)
    (z : CentralPhase Q.C) (ω : R) (hW : z.app W = ω • 𝟙 W)
    (hreg : ∀ f : 𝟙_ Q.C ⟶ W ⊗ W, (1 - ω ^ 2) • f = 0 → f = 0) :
    FlavouredQuantumObservableUniverse.{u, v} R :=
  { Q with
    flavourObj := W
    exteriorCube := L3
    exteriorCubeProj := π₃
    exteriorCube_epi := inferInstance
    flavourVolumeIso := vol
    flavour_not_selfDual := not_selfDual_of_phase z hW hreg }

/-- In the constructor's setting the phase is a cube root of unity on `End 𝟙`:
the flavour volume form forces `(ω³ - 1) • 𝟙_𝟙 = 0`. -/
theorem ofCentralPhase_cube {R : Type*} [CommRing R] (Q : QuantumObservableUniverse.{u, v} R)
    [MonoidalPreadditive Q.C] [MonoidalLinear R Q.C]
    (W L3 : Q.C) (π₃ : (W ⊗ W) ⊗ W ⟶ L3) [Epi π₃] (vol : L3 ≅ 𝟙_ Q.C)
    (z : CentralPhase Q.C) (ω : R) (hW : z.app W = ω • 𝟙 W) :
    (ω ^ 3 - 1) • 𝟙 (𝟙_ Q.C) = 0 := by
  haveI : Epi (π₃ ≫ vol.hom) := epi_comp _ _
  -- `tpow W 3` is `((𝟙 ⊗ W) ⊗ W) ⊗ W`; transport along the left unitor.
  let u : tpow W 3 ⟶ (W ⊗ W) ⊗ W := ((λ_ W).hom ▷ W) ▷ W
  haveI : Epi u := by dsimp [u]; infer_instance
  haveI : Epi (u ≫ π₃ ≫ vol.hom) := epi_comp _ _
  exact phase_pow_of_volume z hW (u ≫ π₃ ≫ vol.hom)

end QOU.FlavouredQuantumObservableUniverse
