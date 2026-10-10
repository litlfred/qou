/-!
# Fred2005.UnitRootFCrystal — Frobenius acts invertibly

**Sibling-resolution stub** for content block
[`def:unit-root-f-crystal`](unit-root-f-crystal.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §8`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005`.

Canonical declaration:

```lean
structure Fred2005.UnitRootFCrystal (H : Fred2005.CommutativeFormalGroup) where
  frobenius            : H.coordRing → H.coordRing
  frobenius_injective  : ∀ x y, frobenius x = frobenius y → x = y
  frobenius_surjective : ∀ y, ∃ x, frobenius x = y
```

An F-crystal is **unit-root** when the Frobenius endomorphism acts
invertibly on the coordinate ring — i.e. there is no nilpotent
component in the Dieudonné–Manin decomposition.  The unit-root
condition is equivalent to integrability of the associated
[skewed-Poisson structure](skewed-poisson-structure.md): a
biderivation `π_<` integrates iff its F-crystal is unit-root
(`Fred2005.unit_root_iff_integrable`).

-- Ref: [hazewinkel1978] M. Hazewinkel, *Formal Groups and
        Applications*, Academic Press, 1978, Ch. V.
-- Ref: [zink2002] T. Zink, *The Display of a Formal p-Divisible
        Group*, Astérisque 278.
-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005,
        Corollary 5.3.
-/
