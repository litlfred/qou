import QOU.Hecke.Generators
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.RingTheory.Adjoin.Basic

/-!
# Hecke algebra `H_n(q)` — class-based formulation

The Iwahori–Hecke algebra of type `A_{n-1}` is presented as a
typeclass over a commutative ring `R` and parameter `q : R`:

  ```
  class HeckeAlgebra (R : Type u) (n : ℕ) (q : R) (A : Type u)
      [CommRing R] [Inv R] [Ring A] [Algebra R A] where
    embed      : Generator n → A
    quadratic  : HeckeQuadratic q embed
    braid      : BraidRelation embed
    farCommute : FarCommutativity embed
    spans      : Algebra.adjoin R (Set.range embed) = ⊤
  ```

Provability of statements about H_n(q) takes the algebra as an
instance hypothesis.

## References

- [prop:braiding-eigenvalue-extraction]
- Kassel (1995), Theorem XII.1.4 (presentation of H_n(q)).
- Mathas (1999), Definition 1.13.
-/

namespace QOU.Hecke

universe u

/--
The Iwahori–Hecke algebra `H_n(q)` over `R`, axiomatised as a
typeclass. An instance asserts: an `R`-algebra `A` with a chosen
generator embedding `embed : Generator n → A` satisfying the three
Hecke relations.

The `spans` field captures that `A` is generated as an `R`-algebra
by `embed`'s image (every element is a finite `R`-linear combination
of monomials in the generators). Stated existentially to keep the
class lightweight.
-/
class HeckeAlgebra (R : Type u) (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A] where
  /-- The generator embedding σ_i ↦ embed i. -/
  embed : Generator n → A
  /-- Hecke quadratic relation: σ_i² = (q - q⁻¹)σ_i + 1. -/
  quadratic : HeckeQuadratic q embed
  /-- Braid relation: σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}. -/
  braid : BraidRelation embed
  /-- Far-commutativity: σ_i σ_j = σ_j σ_i for |i - j| ≥ 2. -/
  farCommute : FarCommutativity embed
  /-- Spanning property: `A` is generated as an `R`-algebra by the
  image of `embed`. Captured via `Algebra.adjoin` for compatibility
  with Mathlib's subalgebra API. Without this field the typeclass
  would admit any algebra containing the generators rather than the
  Hecke quotient itself. -/
  spans : Algebra.adjoin R (Set.range embed) = ⊤

namespace HeckeAlgebra

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A] [HA : HeckeAlgebra R n q A]

/-- The image of generator `i` in the algebra. Convenience alias for
`HeckeAlgebra.embed i`. -/
@[reducible]
def gen (i : Generator n) : A := HA.embed i

/-- The inverse of σ_i is σ_i - (q - q⁻¹), derivable from the Hecke
quadratic relation: σ_i · (σ_i - (q - q⁻¹)) = σ_i² - (q-q⁻¹)σ_i = 1. -/
theorem inv_formula (i : Generator n) :
    HA.embed i * (HA.embed i - (q - q⁻¹) • 1) = 1 ∧
    (HA.embed i - (q - q⁻¹) • 1) * HA.embed i = 1 := by
  -- Ref: [leitner2026] Kassel (1995), §XII.1; Hecke quadratic ⇒ σ_i^{-1} = σ_i - (q-q⁻¹).
  -- Proof: from HeckeQuadratic, σ_i² = (q-q⁻¹)·σ_i + 1.
  -- LHS1: σ_i·(σ_i - (q-q⁻¹)·1) = σ_i² - (q-q⁻¹)·σ_i = 1. ✓
  -- LHS2: (σ_i - (q-q⁻¹)·1)·σ_i = σ_i² - (q-q⁻¹)·σ_i = 1. ✓
  have hq := HA.quadratic i
  refine ⟨?_, ?_⟩
  · -- embed i * (embed i - (q - q⁻¹) • 1) = 1
    rw [mul_sub, mul_smul_comm, mul_one, hq]
    abel
  · -- (embed i - (q - q⁻¹) • 1) * embed i = 1
    rw [sub_mul, smul_mul_assoc, one_mul, hq]
    abel

end HeckeAlgebra

end QOU.Hecke
