import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Algebra.Ring.Basic

/-!
# QOU.AlgebraicSubstrate.BringsCoordinateRing

Non-commutative coordinate ring of Bring's curve, with genus and
S₅ symmetry data.

LaTeX label: `def:brings-coordinate-ring`
-/

set_option autoImplicit false


namespace QOU.AlgebraicSubstrate

/-- **BringsCoordinateRing**: the non-commutative coordinate ring
    `𝒪_q(ℬ)` of Bring's curve, equipped with its genus and
    `S₅` symmetry action.

    LaTeX: `\label{def:brings-coordinate-ring}` -/
structure BringsCoordinateRing where
  /-- The underlying ring of `𝒪_q(ℬ)`. -/
  carrier : Type*
  /-- Ring structure on the coordinate ring. -/
  [ringInst : Ring carrier]
  /-- The genus of Bring's curve. -/
  genus : ℕ
  /-- Genus equals 4. -/
  genus_eq : genus = 4
  /-- The number of independent cycles `2g`. -/
  spectralModes : ℕ := 2 * genus
  /-- `S₅` acts on the coordinate ring by permutation
      of homogeneous coordinates. -/
  -- Ref: [manuscript] Chapter 5
  s5_action : Equiv.Perm (Fin 5) → carrier → carrier
  /-- The `S₅` action is compatible with multiplication. -/
  -- Ref: [manuscript] Chapter 5
  s5_mul_compat :
    ∀ (σ : Equiv.Perm (Fin 5)) (a b : carrier),
      s5_action σ (a * b) = s5_action σ a * s5_action σ b

attribute [instance] BringsCoordinateRing.ringInst

end QOU.AlgebraicSubstrate
