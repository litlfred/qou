/-!
# Fred2005.NoncommutativeFormalGroup — output of the integration theorem

**Sibling-resolution stub** for content block
[`def:non-commutative-formal-group`](non-commutative-formal-group.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §3`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005`.

Canonical declaration:

```lean
structure Fred2005.NoncommutativeFormalGroup where
  base        : Fred2005.CommutativeFormalGroup.{u}
  distAlgebra : Type u
  mul         : distAlgebra → distAlgebra → distAlgebra
  comul       : distAlgebra → distAlgebra × distAlgebra
  unit        : distAlgebra
  comul_hom   : ∀ x y, comul (mul x y) =
                  (mul (comul x).1 (comul y).1,
                   mul (comul x).2 (comul y).2)   -- strong multiplicativity
```

`G / ℤ_p` is the deformation of `Dist(base)` recovered by integrating a
[`def:skewed-poisson-structure`](skewed-poisson-structure.md) on `base`
via the Main Theorem of [`fred2005`].  The `comul_hom` field is the
"strong multiplicativity" condition of [fred2005, Theorem 4.12] —
the comultiplication is an algebra homomorphism, which is what
ensures the gauge connection (in QOU's downstream consumption)
survives the characteristic-`p` → characteristic-`0` passage.

-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005, Main Theorem
        & Theorem 4.12.
-/
