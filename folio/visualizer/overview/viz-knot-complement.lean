/-!
# QOU.KnotComplement — knot-complement visualiser state

**Sibling-resolution stub** for content block
[`def:viz-knot-complement`](viz-knot-complement.md).  The buildable
formalisation lives in
[`QOU/KnotComplement.lean`](../../quantum-observable-universe/lean/QOU/KnotComplement.lean)
and is compiled by `lake build QOU` via direct
`import QOU.KnotComplement` (intentionally not pulled into the
`QOU.lean` umbrella, since it carries pure data — same opt-out
pattern as `QOU.MathlibExt.SDPRankEquality`).

Canonical declarations:

```lean
structure QOU.CuspShape where
  re, im : ℝ                  -- cusp modulus τ = x + iy

structure QOU.FundamentalGroupPresentation where
  numGenerators : ℕ
  relators      : List (List (Fin numGenerators × Bool))

structure QOU.KnotComplement where
  name             : String
  hyperbolicVolume : ℝ                            -- Vol(S³ ∖ K)
  cuspShape        : QOU.CuspShape
  pi1              : QOU.FundamentalGroupPresentation
  h1Rank           : ℕ                            -- always 1 for a knot
```

Geometric invariants (volume, homology, fundamental group) are
computed at runtime by the SnapPea kernel (WASM); this Lean
structure pins the schema so URL-embedded viewer state and the
typed back-end agree on shape.

-- Ref: [thurston1978] W. Thurston, *The Geometry and Topology of
        3-Manifolds*, Princeton Lecture Notes 1979, §4.
-- Ref: [culler2024] SnapPea kernel — https://snappy.computop.org/
-/
