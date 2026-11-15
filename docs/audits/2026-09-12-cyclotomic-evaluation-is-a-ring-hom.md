# Is the Habiro cyclotomic evaluation a ring homomorphism?

**Bean:** `qou-ix0x`. **Hinge for:** PR #7216 (`qou-brng` class D).
**Answered:** 2026-09-12 (Lean), salvaged and re-verified onto `main` 2026-10-12.

## The question, and why it is the whole question

PR #7216 excludes class D — *"fibre-level / higher order in `q`: a Habiro element
whose order-zero rendering is the observable"* — as an *independent* escape from
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
that door, on the ground that cyclotomic summation converges at *every* root of
unity rather than along a ray. So the two fronts meet at one decidable question.

## The answer: a dichotomy, and it shuts both branches

Formalised in
[`QOU/Habiro/CyclotomicEvaluationRingHom.lean`](../../folio/quantum-observable-universe/lean/QOU/Habiro/CyclotomicEvaluationRingHom.lean),
sorry-free, generic `[CommRing R]`.

**At a root of unity, `ev_ζ` IS a ring homomorphism.** `cyclotomicEvalHom` is
`Polynomial.evalRingHom ζ`; `qPochPoly_mem_ker` shows it kills `(q;q)_N` when
`ζ^N = 1`; `cyclotomicQuotientEval` is the induced `→+*` out of the level-`N`
truncation `R[q]/((q;q)_N)` — which is exactly the object the Habiro ring
`Ẑ[q] = lim_← R[q]/((q;q)_N)` is the inverse limit of. So `bondSum_map` applies
verbatim and **class D's exclusion extends through the cyclotomic rendering**.
`map_bondCount` and `quotientEval_bondCount` state the transport directly, so
this file does not depend on #7216 being merged.

**Off the roots of unity there is no rendering at all** — nothing to be, or fail
to be, a ring map. Over a domain, `exists_pow_eq_one_of_qPochDiag_eq_zero` shows
that the truncation `(ζ;ζ)_N = 0` which makes `habiroEval` level-independent
*forces* `ζ^k = 1` for some `1 ≤ k ≤ N`. Contrapositively,
`habiroEval_one_ne_succ_of_not_root` gives that at a non-root-of-unity `ζ` the
all-ones series has level `N+1` differing from level `N` **for every `N`**: the
truncations never stabilise, `habiroEval_stable` is unavailable, and there is no
value to render.

**So `qou-ix0x` is a negative result for its own proposal, which is the useful
kind.** The door class D had is shut on both sides.

## ROAST item 4, answered in the negative

The bean's own item 4 asks how root-of-unity data is supposed to reach an
evaluation at `q₀ ≈ 1.11`, which is not a root of unity. For
**evaluation-shaped** renderings the answer is: *it does not reach it by
evaluating*. That is a statement about where an object can live, not a
derivation of one — ROAST-1, as the bean scopes it.

## Scope — AGENTS.md §"Before declaring refuted"

**Scope (b)** for the evaluation-shaped renderings, resting on a proved
structural invariant (a ring hom's compatibility with a polynomial, plus
`Finset.prod_eq_zero_iff` in a domain), not on any numerical estimate.

**It does NOT exclude every fibre-level rendering.** Explicitly untouched:

* **a rendering that is not an evaluation** — a pairing, a state integral, or a
  coefficient extraction. Coefficient extraction is genuinely *not* a ring hom
  (linear, not multiplicative); that channel is covered by #7216's second
  invariant `bondSum_tower`, not by anything here;
* **an evaluation into a ring where `(ζ;ζ)_N` is a zero divisor** without `ζ`
  being a root of unity — the dichotomy assumes `IsDomain`;
* **anything about magnitudes.** Nothing here computes `b₃`.

**Nothing is fitted.** No root of unity, truncation order or completion is
selected anywhere; `ζ` and `N` are arbitrary throughout. The figures
`b₃ = +1.4262225` MeV and `tripleMutual = −8.09991876` MeV are targets to check
against, never search directions, and no number in this file is compared to
either.

## The corpus caveat this corrects, and the sense in which it was right

`QOU.Habiro.CyclotomicEvaluation`'s docstring says:

> **Multiplicativity is NOT proved here.** The Habiro product in cyclotomic
> coordinates is not termwise, so `ev_ζ` being a *ring* hom is a larger build. …
> **Do not cite it as a ring hom.**

That is correct **about the coordinates** and wrong if read as a statement about
the map. `habiroEval a ζ N` is the coordinate map `a ↦ value`, and it is indeed
only additive: the `(q;q)_m` do not multiply termwise, so there is no
coefficientwise product on sequences. **The map on the ring is a different
object**, and `habiroEval_eq_cyclotomicEvalHom` factors the coordinate map
through it. `habiroEval_mul_of_repr` restates multiplicativity in coordinates
with the Habiro product supplied as a *hypothesis* (`hc`, which is its
definition — the product taken in `R[q]/((q;q)_N)`) rather than assumed as a
conclusion, and `habiroPoly_one_mul` supplies an instance so that hypothesis
class is not empty.

Read the caveat as *"the cyclotomic coordinates are not a multiplicative
basis"* — true, and Habiro's own point — not as *"`ev_ζ` is not a ring map"*,
which is false.

## One defect found while salvaging

The 2026-09-12 draft's own docstring closed with *"the archimedean instance at
the substrate pin lives in `QOU.Habiro.CyclotomicEvaluationAtSubstrate`"*. **No
such declaration exists**, and a corpus-wide grep returns zero hits — but the
interesting part is that this is not a missing file to be written later. The
substrate pin is not a root of unity, so §4 of the very same file proves there
is no value to instantiate: a file of that name would have to contradict the
theorem three sections above it. Corrected in place.

This is the `qou-a3qo` trap one level over — a reference that decays
independently of the sentence carrying it — except that here the reference was
never live, and what exposes it is not a stale link but the file's own result.
