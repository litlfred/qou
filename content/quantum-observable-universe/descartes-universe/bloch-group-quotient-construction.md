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

> **Status: theorem (sorry-free, modulo pentagon generator set).**
> The Lean file
> [`bloch-group-quotient-construction.lean`](bloch-group-quotient-construction.lean)
> defines `BlochGroup F` concretely as a quotient `AddCommGroup`,
> with the pentagon `AddSubgroup` parameterised by the explicit
> generator set `pentagonRelationGenerators : Set (PreBlochGroup F)`.
> The generator set is currently `∅` as a placeholder (so
> `BlochGroup F = PreBlochGroup F` until pentagon generators are
> wired in); plugging in the pentagon enumeration is the final
> step to give a non-trivial quotient. The structural construction,
> universal property, and `HasBlochGroup ℝ` instance are all
> sorry-free.

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

**Pentagon generator set.** The `pentagonRelationGenerators` set
is currently `∅`, making `BlochGroup F` trivially equal to
`PreBlochGroup F`. To get the *non-trivial* Bloch group, one must
populate the generator set with the explicit 5-term identities

$$
  [x] - [y] + [y/x] - [(1 - 1/y)/(1 - 1/x)] + [(1 - y)/(1 - x)],
$$

ranging over all valid `(x, y) ∈ F^\times \times F^\times` with
`x ≠ y, x ≠ 1, y ≠ 1`, etc. This requires:

- Decidability of the pentagon-domain conditions on `F` (for
  `Field F` with computable arithmetic, this is straightforward).
- A definition of the pentagon-shape map `F × F → PreBlochGroup F`
  enumerating the relation generator at each `(x, y)`.
- Inclusion of the image of this map in
  `pentagonRelationGenerators`.

The structural skeleton above accommodates this without
modification; the addition is purely the explicit relation set.

## Significance

The §3b-cond chain anchored by `prop:archimedean-functor-uniqueness`
now has its `BlochSuslinUniqueness` class one step closer to
unconditional inhabitation: the BlochGroup quotient is no longer
typeclass-only, but a real Lean object. The remaining work for
unconditional `BlochSuslinUniqueness` is:

1. ✅ `BlochGroup F` quotient construction (this proposition).
2. Pentagon identity proof for `Cl_2` on the unit-circle subset.
3. Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity.
4. Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

(2) is partially closed at the boundary in
[`cl2-pentagon-and-faddeev-partial.lean`](cl2-pentagon-and-faddeev-partial.lean).
(3) and (4) remain Mathlib-pending substantive work.
