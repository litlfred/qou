import Mathlib.Data.Real.Basic
import Mathlib.Logic.Function.Basic


/-!
# QOU.BundleIsotopyEquiv — Isotopy equivalence of bundle initial conditions

Two bundle initial conditions are isotopy equivalent if they are related
by a permutation of indices and ambient isotopy within each fibre.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- Isotopy equivalence of bundle initial conditions.
    Two configurations {(pᵢ, Hᵢ)} and {(p_{σ(i)}, H'_{σ(i)})} are
    equivalent if related by a permutation σ and ambient isotopy.

    LaTeX: `\label{def:bundle-isotopy-equivalence}` -/
-- Ref: [leitner2026] §3, Definition: Isotopy equivalence
structure BundleIsotopyEquiv where
  /-- Number of initial conditions. -/
  numPoints : ℕ
  /-- The permutation relating the two configurations. -/
  perm : Fin numPoints → Fin numPoints
  /-- The permutation is bijective. -/
  perm_bijective : Function.Bijective perm

/-- Reflexive (identity) bundle isotopy equivalence on `n` localized knots. -/
def BundleIsotopyEquiv.refl (n : ℕ) : BundleIsotopyEquiv where
  numPoints := n
  perm := id
  perm_bijective := Function.bijective_id

/-- Transitive composition of two bijective index permutations on `n` localized knots. -/
def BundleIsotopyEquiv.ofComp (n : ℕ)
    (perm₁ perm₂ : Fin n → Fin n)
    (h₁ : Function.Bijective perm₁) (h₂ : Function.Bijective perm₂) :
    BundleIsotopyEquiv where
  numPoints := n
  perm := perm₂ ∘ perm₁
  perm_bijective := Function.Bijective.comp h₂ h₁

/-- The identity bundle isotopy equivalence fixes every particle index. -/
theorem BundleIsotopyEquiv.refl_apply (n : ℕ) (i : Fin n) :
    (BundleIsotopyEquiv.refl n).perm i = i :=
  rfl

end QOU
