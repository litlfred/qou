import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Fintype.Basic

/-!
# Hecke generators and braid / Hecke relations

For `n ≥ 1`, the Iwahori–Hecke algebra `H_n(q)` is generated over
a base ring `R` by `σ_1, ..., σ_{n-1}` subject to:

  (H1) Hecke quadratic:    `σ_i² = (q - q⁻¹) σ_i + 1`
  (H2) Braid:              `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`
  (H3) Far-commutativity:  `σ_i σ_j = σ_j σ_i`  if `|i - j| ≥ 2`

This file provides the abstract generator type and relation
predicates. The full algebra (quotient of free algebra by these
relations) lives in `Algebra.lean`.

## References

- [prop:braiding-eigenvalue-extraction]
- Kassel (1995), Quantum Groups, §XII.1
-/

namespace QOU.Hecke

universe u

/-- A Hecke generator at index `i` for an algebra of strand count `n`.
The condition `1 ≤ i ≤ n - 1` is encoded via `Fin (n - 1)`. -/
structure Generator (n : ℕ) where
  /-- Generator index, 0-based; corresponds to σ_{idx+1} in the
  literature's 1-based convention. -/
  idx : Fin (n - 1)
  deriving DecidableEq

namespace Generator

/-- Two generators are *adjacent* iff their indices differ by exactly 1. -/
def adjacent {n : ℕ} (i j : Generator n) : Prop :=
  (i.idx.val + 1 = j.idx.val) ∨ (j.idx.val + 1 = i.idx.val)

/-- Two generators are *far-commuting* iff their indices differ by
at least 2 (equivalently, are not equal and not adjacent). -/
def farCommuting {n : ℕ} (i j : Generator n) : Prop :=
  i ≠ j ∧ ¬ adjacent i j

end Generator

/-- Hecke relation predicate (H1):
    σ_i² = (q - q⁻¹) σ_i + 1
in any algebra `A` over `R` with σ_i interpreted via `embed`. -/
def HeckeQuadratic
    {R : Type u} {n : ℕ} (q : R) [Ring R]
    {A : Type u} [Ring A] [Algebra R A]
    (embed : Generator n → A) : Prop :=
  ∀ i : Generator n,
    embed i * embed i = (q - q⁻¹) • embed i + 1

/-- Braid relation predicate (H2):
    σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}
for adjacent generators. -/
def BraidRelation
    {n : ℕ} {A : Type u} [Mul A]
    (embed : Generator n → A) : Prop :=
  ∀ i j : Generator n,
    Generator.adjacent i j →
      embed i * embed j * embed i = embed j * embed i * embed j

/-- Far-commutativity (H3):
    σ_i σ_j = σ_j σ_i  whenever |i - j| ≥ 2. -/
def FarCommutativity
    {n : ℕ} {A : Type u} [Mul A]
    (embed : Generator n → A) : Prop :=
  ∀ i j : Generator n,
    Generator.farCommuting i j → embed i * embed j = embed j * embed i

end QOU.Hecke
