/-!
# Fred2005.CommutativeFormalGroup — base object of the integration theorem

**Sibling-resolution stub** for content block
[`def:commutative-formal-group`](commutative-formal-group.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §1`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005` via the `fred2005` Lake package.

Canonical declaration:

```lean
structure Fred2005.CommutativeFormalGroup where
  p              : ℕ           -- prime characteristic
  p_prime        : Nat.Prime p
  coordRing      : Type u      -- carrier of 𝒪(H)
  formalGroupLaw : coordRing → coordRing → coordRing
  commutative    : ∀ x y, formalGroupLaw x y = formalGroupLaw y x
  zero           : coordRing
```

This is the base object `H / 𝔽_p` in the dissertation's integration
theorem: a formal group whose coordinate ring carries a commutative
formal group law.  The non-commutative output `G / ℤ_p` is the
[`def:non-commutative-formal-group`](non-commutative-formal-group.md);
the bridge between them is the [skewed-Poisson
structure](skewed-poisson-structure.md) and the integration theorem
[`thm:skew-poisson-integrates`].

-- Ref: [hazewinkel1978] M. Hazewinkel, *Formal Groups and
        Applications*, Academic Press, 1978, Ch. I.
-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005, §2.
-/
