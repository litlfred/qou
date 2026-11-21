import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.Tactic.LinearCombination

/-!
# Zero derivative means constant, from integration

The `const` axiom of `DolbeaultStructure` ("`d f = 0` on a connected open set makes `f`
constant") is the dual of an integration statement, in the shape of the QOU axiom of
non-degenerate integration. This file proves the duality as pure linear algebra over a
commutative ring.

Data: functions `F` with a constant `one`, compactly supported top forms `Ω`, the pairing
`P f ω = ∫ f ω` (so `∫ ω = P one ω`), and the exterior derivative `dc : Ω₁ → Ω` on compactly
supported 1-forms. Hypotheses:

* **non-degenerate integration**: `P f = 0` forces `f = 0`;
* **exactness**: a top form with `∫ ω = 0` is `dc η` (compactly supported Poincaré lemma; this is
  where connectedness lives: on two disjoint discs it fails exactly as `const` does);
* **normalisation**: some `ω₀` has `∫ ω₀ = 1`.

Then `f` orthogonal to every exact form is the constant `(P f ω₀) • one`
(`eq_smul_one_of_integration`). With **Stokes** as integration by parts,
`∫ f · dc η = -⟪d f, η⟫`, a function with `d f = 0` is such an `f`
(`eq_smul_one_of_stokes`).
-/

namespace QOU.Archimedean.BlochRigidity

variable {R F Ω₁ Ω : Type*} [CommRing R] [AddCommGroup F] [Module R F]
  [AddCommGroup Ω₁] [Module R Ω₁] [AddCommGroup Ω] [Module R Ω]

/-- **Bridge lemma.** Non-degenerate integration plus exactness: a function orthogonal to all
exact top forms is constant. -/
theorem eq_smul_one_of_integration (P : F →ₗ[R] Ω →ₗ[R] R) (one : F) (dc : Ω₁ →ₗ[R] Ω)
    (hnd : ∀ f : F, (∀ ω, P f ω = 0) → f = 0)
    (hexact : ∀ ω : Ω, P one ω = 0 → ∃ η, dc η = ω)
    {ω₀ : Ω} (hω₀ : P one ω₀ = 1)
    {f : F} (hflat : ∀ η, P f (dc η) = 0) :
    f = P f ω₀ • one := by
  apply sub_eq_zero.1
  apply hnd
  intro ω
  obtain ⟨η, hη⟩ := hexact (ω - P one ω • ω₀) (by simp [hω₀])
  have h := hflat η
  rw [hη, map_sub, map_smul, smul_eq_mul] at h
  simp only [map_sub, map_smul, LinearMap.sub_apply, LinearMap.smul_apply, smul_eq_mul]
  linear_combination h

/-- **Bridge lemma, with Stokes.** If integration by parts holds,
`∫ f · dc η = -⟪d f, η⟫`, then `d f = 0` makes `f` constant. -/
theorem eq_smul_one_of_stokes {Ω₁' : Type*} [AddCommGroup Ω₁'] [Module R Ω₁']
    (P : F →ₗ[R] Ω →ₗ[R] R) (one : F) (dc : Ω₁ →ₗ[R] Ω)
    (d : F →ₗ[R] Ω₁') (Q : Ω₁' →ₗ[R] Ω₁ →ₗ[R] R)
    (hstokes : ∀ f η, P f (dc η) = -Q (d f) η)
    (hnd : ∀ f : F, (∀ ω, P f ω = 0) → f = 0)
    (hexact : ∀ ω : Ω, P one ω = 0 → ∃ η, dc η = ω)
    {ω₀ : Ω} (hω₀ : P one ω₀ = 1)
    {f : F} (hdf : d f = 0) :
    f = P f ω₀ • one :=
  eq_smul_one_of_integration P one dc hnd hexact hω₀ fun η => by
    rw [hstokes, hdf, map_zero, LinearMap.zero_apply, neg_zero]

end QOU.Archimedean.BlochRigidity
