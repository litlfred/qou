import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic

/-!
# QOU.KnotComplement — visualiser hooks for hyperbolic knot complements

Lightweight data structures for the **knot-complement viewer** in
`content/visualizer/overview/viz-knot-complement.{ts,md}`.  Geometric
invariants (volume, homology, fundamental-group presentation) are
delegated to the SnapPea kernel via WASM at runtime; this module
fixes the *types* of the data the SnapPea bridge emits, so downstream
content blocks can refer to them with stable Lean refs.

LaTeX label: `def:viz-knot-complement`.

This file is intentionally **kept out of the top-level `QOU.lean`
umbrella** (cf. the `QOU.MathlibExt.SDPRankEquality` opt-out): its
declarations are pure data and not required by the mathematical
content of QOU.  Consumers import directly via
`import QOU.KnotComplement`.

## References

- SnapPea kernel: https://snappy.computop.org/
- [thurston1978] W. Thurston, *The Geometry and Topology of 3-Manifolds*,
  Princeton Lecture Notes, 1979 — §4 hyperbolic structures on knot
  complements.
-/


namespace QOU

/-- Cusp shape of a hyperbolic knot complement: a complex modulus
    `τ = x + i y` (with `y > 0`) describing the conformal class of
    the cusp torus.  SnapPea returns this as a pair of reals. -/
structure CuspShape where
  /-- Real part of the cusp modulus τ. -/
  re : ℝ
  /-- Imaginary part of the cusp modulus τ.  Strictly positive for
      a genuinely-hyperbolic cusp. -/
  im : ℝ

/-- A presentation of the fundamental group of a knot complement
    in terms of `numGenerators` Wirtinger generators and a list of
    relator words.  Generators are abstract; the SnapPea bridge
    instantiates them concretely. -/
structure FundamentalGroupPresentation where
  /-- Number of generators in the presentation. -/
  numGenerators : ℕ
  /-- Relators, each encoded as a list of `(generator-index, sign)`
      pairs.  `sign = .pos` is the generator, `.neg` is its inverse. -/
  relators      : List (List (Fin numGenerators × Bool))

/-- **Knot complement** (visualiser data structure).

    Lightweight Lean side of the SnapPea bridge: bundles the
    geometric invariants the visualiser needs (hyperbolic volume,
    cusp shape, π₁ presentation, first homology rank) into a single
    serialisable record.  All fields are populated at runtime by
    the SnapPea kernel; this Lean structure pins the schema. -/
-- Ref: [thurston1978] §4 hyperbolic structures on knot complements
structure KnotComplement where
  /-- Display name of the knot (e.g. `"4_1"`, `"trefoil"`, `"5_2"`). -/
  name             : String
  /-- Hyperbolic volume `Vol(S³ \ K)`.  Zero when the complement is
      not hyperbolic (e.g. torus knots, unknot). -/
  hyperbolicVolume : ℝ
  /-- Cusp shape modulus τ (positive imaginary part for hyperbolic
      complements). -/
  cuspShape        : CuspShape
  /-- Wirtinger-style π₁ presentation. -/
  pi1              : FundamentalGroupPresentation
  /-- Rank of `H₁(S³ \ K; ℤ) = ℤ` (always 1 for a knot). -/
  h1Rank           : ℕ

end QOU
