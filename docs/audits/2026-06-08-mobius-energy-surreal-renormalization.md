# Möbius energy as a difference of infinite surreals — the surreal counterpart of KS/UGB→PBW

**Date:** 2026-06-08 · **Branch:** `claude/vigilant-fermat-SROph` · **PR:** #1995
**Status:** derivation note. The **surreal-essential candidate**: a tricky
analytic *renormalization* (the finiteness of the Möbius energy) recovered by
surreal *arithmetic*. Same spirit as the Gröbner–Shirshov/Diamond-Lemma proof of
PBW and the KS algebraic shortcuts — but here the algebra that "surfaces" is the
**surreal** (`ε^ω`/Hahn) structure, which is what makes this the keep-justifying
showcase for surreals.

## The prior analytic result

The **Möbius (knot) energy** ([`def:mobius-energy`](../../content/quantum-observable-universe/climax-volume-mass/mobius-energy.md);
O'Hara 1991; Freedman–He–Wang 1994) is a *renormalized* quadratic interaction:

$$
  E(\varrho) = \iint_{S^1\times S^1}\Big(\frac{1}{|\varrho(s)-\varrho(t)|^2}
  - \frac{1}{D(s,t)^2}\Big)\,|\varrho'(s)|\,|\varrho'(t)|\,ds\,dt,
$$

`D` = intrinsic arc-length distance. **Each term diverges** on the diagonal
(`∫∫|s-t|^{-2}` is non-integrable); the **difference is finite** because the two
divergences cancel. Proving that finiteness/well-definedness is a genuine
analytic lemma (Hadamard finite part / principal value, careful excision of the
diagonal) — and it is one of the two analytic obstructions the surreal appendix
flagged.

## The surreal recasting

Lift the integral to `No`; excise a diagonal band of width `ε = 1/ω`:

- `I_1 := \iint_{|s-t|>1/ω}|\varrho(s)-\varrho(t)|^{-2}\,|\varrho'||\varrho'|` is a
  **literal infinite surreal**: as the cutoff `ε→0` it diverges like `c/ε = c·ω`,
  so `ord_ω(I_1) = +1` ([Conway normal form](../../content/quantum-observable-universe/appendix-surreals/conway-normal-form.md);
  `ε = 1/ω`, [surreal blow-up calculus](../../content/quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.md)).
- `I_2 := \iint_{|s-t|>1/ω} D(s,t)^{-2}\,|\varrho'||\varrho'|` is infinite of the
  **same `ord_ω = +1`** and the **same leading coefficient** `c`, because near the
  diagonal `|\varrho(s)-\varrho(t)| = D(s,t) + O(|s-t|^3)`, so the two integrands
  agree to leading order.

Therefore the difference `I_1 - I_2` has its `ord_ω = +1` parts **cancel**, leaving
an **appreciable** (finite, `ord_ω ≤ 0`) surreal, and

$$
  \boxed{\;E(\varrho) \;=\; \operatorname{std}\big(I_1 - I_2\big).\;}
$$

**The renormalization is surreal arithmetic.** The tricky analytic finite-part
becomes: *subtract two infinite surreals of equal leading `ω`-order; the leading
terms cancel by construction; take the standard part.* And the **finiteness bound
itself** — the hard analytic content — reduces to an **algebraic leading-`ω`-
coefficient match** (`[ω^{+1}]I_1 = [ω^{+1}]I_2`), i.e. checking the
near-diagonal expansion `|\varrho(s)-\varrho(t)| = D + O(|s-t|^3)`. That is the
"manage the quadratic/infinite interaction's bound algebraically with surreals"
move.

This also recovers the QOU **categorical** Möbius energy
([`def:mobius-energy`](../../content/quantum-observable-universe/climax-volume-mass/mobius-energy.md),
which excises the diagonal and gives `¼E + const` at `q→1`): the categorical
"exclude diagonal + take limit" is exactly "excise a width-`1/ω` band + take
`std`", made into one algebraic statement.

## The general principle: Hausdorff dimension = a surreal critical order

The same move runs the **Frostman/Riesz `s`-energy** `I_s(μ) = \iint|x-y|^{-s}\,
dμ\,dμ` (again a quadratic interaction): `I_s = +∞` below the dimension, finite
above. Lifted to `No`, the family `{I_s}` is graded by `s`, and

$$
  \dim_H(\mathrm{supp}\,μ) \;=\; \text{the } ord_ω\text{-boundary where } I_s
  \text{ flips from infinite to appreciable.}
$$

So the analytic `\dim_H = \sup\{s : I_s<∞\}` becomes a single **valuation** (`ω`-
order) statement. QOU's in-repo instance is the Julia-set dimension
`d_H(q) = (2q-1)^2/q^3` ([`julia-set-reeb`](../../content/quantum-observable-universe/information-theory/julia-set-reeb.md))
— notably *rational* (generic quadratic-Julia dimensions are transcendental;
treat the exact formula as QOU-specific/idealised, not leaned on here).

**Lebesgue vs Hausdorff (the clean line):** Lebesgue *measure-value* — no (`No` has
no Lebesgue measure). Hausdorff *dimension* and *renormalized energies* — yes,
because dimension is an *exponent* (= `ω`-order) and renormalization is a
*difference of infinite surreals*.

## Honest verdict (for the keep decision)

- **Strong** on *simpler / cleaner / algebraic*: the Möbius finiteness lemma →
  a leading-`ω`-coefficient match is a real reduction, and it is *in the exact
  area surreals were supposed to be load-bearing* — it turns the appendix's
  flagged obstruction into a feature.
- **Weaker** on *impossible-without*: Hadamard finite-part over `ℝ` is the
  classical equivalent, so a skeptic calls it "cleaner, not essential."

**This is the best surreal showcase available — the honest counterpart of
KS/UGB→PBW.** It justifies keeping surreals as the *renormalization/dimension
language*. If even this reads as "language not necessity", the *reconsider/purge*
instinct is fair.

## Promotion path

A `remark` interpreting [`def:mobius-energy`](../../content/quantum-observable-universe/climax-volume-mass/mobius-energy.md)
(`E = std(I_1 - I_2)`; finiteness = leading-`ω`-coefficient match) + a `proposition`
"Hausdorff dimension = `ord_ω`-boundary of the `s`-energy" (Lean-able over the
`No`-valuation, gated on toolchain restore). Cites: O'Hara 1991, Freedman–He–Wang
1994 (Möbius energy); Falconer (Frostman/`s`-energy).
