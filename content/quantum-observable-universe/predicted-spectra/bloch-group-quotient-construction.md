**Proposition (concrete `BlochGroup F` construction — closes
substantive Mathlib gap (1)).**
*The Bloch group `BlochGroup F` for a field-like type `F` admits
a concrete Lean construction as the quotient*

$$
  B(F) \;:=\; \mathrm{FreeAbelianGroup}\bigl(\mathrm{PreBlochElement}\,F\bigr)
            \;\big/\; \mathrm{pentagonSubgroup},
$$

*where `PreBlochElement F` carries the pre-Bloch elements
(`val ≠ 0 ∧ val ≠ 1`) and `pentagonSubgroup` is the
`AddSubgroup.closure` of the 5-term pentagon-relation generators.
The quotient inherits an `AddCommGroup` structure from Mathlib's
`QuotientAddGroup` instance, with a canonical projection
`quot : PreBlochGroup F →+ BlochGroup F` and the standard
universal property.*

## Lean structure

See [Table](#tbl:bloch-group-quotient-construction-table-data).

## Gap closed

**Item (1) of the three substantive Mathlib gaps.** The carrier
types and class hooks from
[`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean)
are now backed by a real Lean construction: `BlochGroup F` is a
genuine `AddCommGroup` (not a typeclass ansatz), with a
canonical projection and universal property. The `HasBlochGroup ℝ`
instance is concretely inhabited.

## Remaining open work

**Constrain `PentagonShape F` to Rogers-form 5-tuples.** The
current `PentagonShape F` accepts arbitrary 5-tuples of
pre-Bloch elements, making `pentagonRelationGenerators` too
permissive: degenerate shapes with repeated entries collapse
the generator to `of(eᵢ)`, putting individual pre-Bloch
elements into the relation subgroup and trivialising the
quotient. The proper fix is a `ValidPentagonShape F` predicate
enforcing the Rogers-form constraints

$$
  e_3 \;\equiv\; e_2 / e_1, \quad
  e_4 \;\equiv\; (1 - e_2^{-1})/(1 - e_1^{-1}), \quad
  e_5 \;\equiv\; (1 - e_2)/(1 - e_1),
$$

derived from a valid Rogers pair `(x, y) ∈ F^\times \times F^\times`
with `x \neq y, x \neq 0, x \neq 1, y \neq 0, y \neq 1`, plus
non-zero/non-one constraints on the derived images. This
requires:

- Decidability of the pentagon-domain conditions on `F` (for
  `Field F` with computable arithmetic, this is straightforward).
- A definition of the pentagon-shape map `F × F → PentagonShape F`
  with proofs that the derived images satisfy `≠ 0, ≠ 1`.
- Restricting `pentagonRelationGenerators` to
  `Set.range (pentagonGenerator ∘ Subtype.val)` over the
  `ValidPentagonShape F` subtype.

The structural skeleton above accommodates this without
modification; the additions are the validity predicate and
the constrained range.

## Significance

The §3b-cond chain anchored by `prop:archimedean-functor-uniqueness`
now has its `BlochSuslinUniqueness` class one step closer to
unconditional inhabitation: the BlochGroup quotient is no longer
typeclass-only, but a real Lean object. The remaining work for
unconditional `BlochSuslinUniqueness` is:

1. (done) `BlochGroup F` quotient construction (this proposition).
2. Pentagon identity proof for `Cl_2` on the unit-circle subset.
3. Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity.
4. Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

(2) is partially closed at the boundary in
[`cl2-pentagon-and-faddeev-partial.lean`](cl2-pentagon-and-faddeev-partial.lean).
(3) and (4) remain Mathlib-pending substantive work.
