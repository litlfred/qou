# Is the Habiro cyclotomic evaluation a ring homomorphism?

**Bean:** `qou-ix0x`. **Hinge for:** PR #7216 (`qou-brng` class D).

## The question, and why it is the whole question

PR #7216 excludes class D — "fibre-level / higher order in `q`: a Habiro element
whose order-zero rendering is the observable" — as an *independent* escape from
the pair-additive bond-count caps. Its lead invariant is `bondSum_map`: a bond
count is a polynomial with integer coefficients in its energies and counts, so
it commutes with **every ring homomorphism**. The rendering of a fibre-level
bond count is therefore itself a bond count, and every cap applies to it.

That exclusion carries one undischarged hypothesis, stated in the PR body:

> *that the rendering is a ring homomorphism* — evaluation of an analytic
> function at `q₀` is; evaluation of a general Habiro element at a
> non-root-of-unity point is **not defined at all** (bean `qou-ix0x`, item 4).
> Where the rendering is not a ring map, `bondSum_map` says nothing, and that is
> the one genuinely open door class D still has.

`qou-ix0x` proposes the Habiro/cyclotomic summation on the other side of exactly
that door. So the two fronts meet at one decidable question, and this document
records the answer.

## Status

In progress on `claude/habiro-cyclotomic-binding-2026-09-12`.
