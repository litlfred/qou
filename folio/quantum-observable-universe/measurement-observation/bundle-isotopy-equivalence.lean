import Mathlib.Data.Real.Basic


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

end QOU
