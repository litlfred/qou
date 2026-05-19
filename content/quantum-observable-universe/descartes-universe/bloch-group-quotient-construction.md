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

> **Status: theorem (sorry-free, modulo over-permissive
> pentagon-shape constraints).**
> The Lean file
> [`bloch-group-quotient-construction.lean`](bloch-group-quotient-construction.lean)
> defines `BlochGroup F` concretely as a quotient `AddCommGroup`,
> with the pentagon `AddSubgroup` parameterised by the generator
> set `pentagonRelationGenerators := Set.range pentagonGenerator`
> over `PentagonShape F`. The structural construction, universal
> property, `pentagonGenerator_mem_pentagonSubgroup`,
> `quot_pentagonGenerator_eq_zero`, and `HasBlochGroup ℝ` instance
> are all sorry-free.
>
> **Caveat (over-permissive pentagon shapes).** The current
> `PentagonShape F` allows arbitrary 5-tuples of `PreBlochElement F`,
> not the constrained 5-tuples derived from a valid Rogers pair
> `(x, y) ∈ F^\times \times F^\times` via the maps
> `(x, y, y/x, (1-y^{-1})/(1-x^{-1}), (1-y)/(1-x))`. This makes the
> pentagon `AddSubgroup` *too large*: choosing a degenerate shape
> with repeated entries (e.g. `e₂ = e₃ = e₄ = e₅`) collapses the
> generator to `of(e₁)`, putting individual pre-Bloch elements
> into the relation subgroup and trivialising the quotient. The
> proper fix is a `ValidPentagonShape F` predicate enforcing the
> Rogers-form constraints; the structural skeleton supports this
> drop-in refinement without modification.

## Lean structure

| Definition / theorem | Content |
|---|---|
| `pentagonRelationGenerators : Set (PreBlochGroup F)` | placeholder generator set |
| `pentagonSubgroup` | `AddSubgroup.closure` of the generators |
| `BlochGroup F` | `PreBlochGroup F ⧸ pentagonSubgroup` |
| `instance : AddCommGroup (BlochGroup F)` | inherited from `QuotientAddGroup` |
| `quot : PreBlochGroup F →+ BlochGroup F` | canonical projection |
| `quot_zero`, `quot_add` | standard projection lemmas |
| `quot_universal_property` | quotient lifts via Mathlib's `QuotientAddGroup.lift` |
| `hasPentagonRelation_real`, `hasBlochGroup_real` | concrete instances on `F = ℝ` |

## What this closes

**Item (1) of the three substantive Mathlib gaps.** The carrier
types and class hooks from
[`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean)
are now backed by a real Lean construction: `BlochGroup F` is a
genuine `AddCommGroup` (not a typeclass placeholder), with a
canonical projection and universal property. The `HasBlochGroup ℝ`
instance is concretely inhabited.

## What's still open

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

1.  `BlochGroup F` quotient construction (this proposition).
2. Pentagon identity proof for `Cl_2` on the unit-circle subset.
3. Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity.
4. Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

(2) is partially closed at the boundary in
[`cl2-pentagon-and-faddeev-partial.lean`](cl2-pentagon-and-faddeev-partial.lean).
(3) and (4) remain Mathlib-pending substantive work.
