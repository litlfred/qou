/-!
# Fred2005.WittVectorLift — characteristic-zero lift of `(H, π)`

**Sibling-resolution stub** for content block
[`def:witt-vector-lift`](witt-vector-lift.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §7`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005`.

Canonical declaration:

```lean
structure Fred2005.WittVectorLift where
  base    : Fred2005.CommutativeFormalGroup.{u}
  poisson : Fred2005.SkewedPoissonStructure base
  lifted  : Fred2005.NoncommutativeFormalGroup.{u}
  reduces : lifted.base = base       -- G mod p ≅ H
```

Given a [commutative formal group](commutative-formal-group.md)
`H / 𝔽_p` equipped with a [skewed-Poisson
structure](skewed-poisson-structure.md), the Witt vector functor `W`
produces a formal group `Ĝ / ℤ_p` whose generic fibre is a
[non-commutative formal group](non-commutative-formal-group.md) over
`ℚ_p` and whose mod-`p` reduction recovers `H`.  Existence is
witnessed by `Fred2005.witt_vector_lift_exists` (constructive,
via `skew_poisson_integrates`).

-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005, §5 +
        Main Theorem.
-- Ref: [hazewinkel1978] M. Hazewinkel, *Formal Groups and
        Applications*, Academic Press, 1978, Ch. V.
-/
