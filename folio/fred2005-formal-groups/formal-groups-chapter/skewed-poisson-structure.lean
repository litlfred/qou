/-!
# Fred2005.SkewedPoissonStructure — biderivation driving the deformation

**Sibling-resolution stub** for content block
[`def:skewed-poisson-structure`](skewed-poisson-structure.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §2`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005`.

Canonical declaration:

```lean
structure Fred2005.SkewedPoissonStructure
    (H : Fred2005.CommutativeFormalGroup) where
  bracket          : H.coordRing → H.coordRing → H.coordRing
  neg              : H.coordRing → H.coordRing
  antisymmetric    : ∀ f g, bracket f g = neg (bracket g f)
  jacobi_truncated : -- p-truncated Jacobi (long expression — see §2)
                     …
```

A biderivation `π_< : 𝒪(H) ⊗ 𝒪(H) → 𝒪(H)` satisfying graded
anti-symmetry and a `p`-truncated Jacobi condition.  This is the
**infinitesimal datum** encoding the non-commutativity to be
integrated into a [`def:non-commutative-formal-group`](non-commutative-formal-group.md)
via [`thm:skew-poisson-integrates`].

-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005, §2 Def 2.3.
-/
