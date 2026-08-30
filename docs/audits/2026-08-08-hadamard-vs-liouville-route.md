# `uniqueUpToScalar` has two routes in this corpus, and the expensive one is mis-targeted

**Date:** 2026-08-08 · **Beans:** `qou-v4if`, `qou-c3if`, `qou-lv34`, `qou-cons`, `qou-rp5f`
**Follows:** `docs/audits/2026-08-08-per-cusp-factor-dissolves.md` (unrelated arc),
the Hadamard work in PRs on `claude/dg-scope-correction`

## The question that produced this

After proving that `phiBProd` is not entire and that its two halves are, the
open item was: *does the minimality principle survive being restated about the
halves rather than the quotient?*

It does not need to. **`PentagonRigidity.uniqueUpToScalar` does not need Hadamard
factorization at all**, and the corpus already contains the route that replaces
it — sorry-free, and further along.

## Two routes to the same target

| | route A — Hadamard | route B — doubly-periodic Liouville |
|---|---|---|
| file | `QOU/Mathlib/HadamardFactorization.lean` | `QOU/MathlibExt/DoublyPeriodicLiouville.lean` |
| bean | `qou-v4if` (in-progress) | `qou-lv34` (in-progress), `qou-cons`, `qou-rp5f` |
| sorries | 1 (PI-5, the whole theorem) | **0** |
| prerequisites | Jensen, zero-counting, Borel–Carathéodory, canonical products, genus/order theory | Liouville + `Basis.repr` + `Int.fract` |
| status of the core step | open | **proved** (`const_of_doublyPeriodic`) |
| what remains | the entire factorization theorem | two named smaller inputs, each beaned |

Route B's own docstring states the reduction plainly:

> *"It converts the bespoke `uniqueUpToScalar` hypothesis into two smaller,
> standard facts (entire ratio + independent periods), with the Liouville-elliptic
> step now a proved lemma."*

Those two facts are `hratio` (`qou-cons`: two `FaddeevPhi` solutions share their
divisor, so the ratio is entire) and `hibinv` (`qou-rp5f`: `i/b`-periodicity of
the ratio everywhere). Bean `qou-lv34` calls this **"the only honest route to
A_omega=3"**.

**Neither remaining input is Hadamard factorization.** Nor is either one made
easier by having it.

## The two files disagree, and one of them is right

`DoublyPeriodicLiouville.lean` knows exactly what `Φ_b` is:

> *"Faddeev's quantum dilogarithm `Φ_b` does **not** satisfy that: it is
> meromorphic with a genuine zero/pole lattice (poles at `c_b + i(mb + nb⁻¹)`,
> zeros at the reflected lattice), so the bridge as stated does not apply to it
> directly — a hypothesis/application mismatch worth naming rather than working
> around."*

`HadamardFactorization.lean` opens by asserting the opposite in effect — that the
selection principle "is a special case of the **Hadamard factorization
theorem**" — and defines `IsEntireOfOrderLE` to carry it. Its only mention of
the word "meromorphic" is in a list of what Mathlib already has.

So the meromorphy of `Φ_b` was **already documented in this corpus**, in a
sibling file, before the Hadamard chain was written. The finding recorded in
`QOU/Mathlib/HadamardApplicability.lean` — an explicit vanishing point of the
`phiBProd` denominator factor — is a machine-checked instance of a fact route B
had already stated in prose. What is new is only its consequence for route A's
hypothesis.

## What this does and does not retract

**Retracted:** the motivation at the top of `HadamardFactorization.lean`. The
Hadamard chain is not the route to `uniqueUpToScalar`, and finishing PI-4/PI-5
would not discharge it.

**Not retracted:** the Hadamard bricks themselves. `WeierstrassFactorEstimate`
(PI-2), `multipliable_canonicalProduct` (PI-3), `BorelCaratheodory` and the
`differentiable_tprod_one_add` / `differentiable_numProd` / `differentiable_denProd`
results are all correct, sorry-free, Mathlib-gap-shaped, and reusable. They
simply do not serve the purpose the chain's docstring claims.

**Also not retracted:** the possibility that Hadamard is wanted elsewhere.
`ArgumentPrinciple.lean` records that PI-1 (Hadamard) and PI-2 (elliptic divisor
degree) both reduce to the argument principle, which is sorry-free in its
elementary bricks. If canonical products are needed for a *different* target,
that target should be named — the current one does not hold.

## ADDENDUM 2026-08-08 — the target got named, and it is the halves

The line below — "good infrastructure with no current consumer" — **is no longer
true**, and this addendum is the correction rather than a silent edit.

Restating `qou-cons` (see the bean) produced the consumer. Route B's remaining
gap is not `hratio` at all; it is a *selection principle* picking `Φ_b` out of
`Φ_b · {elliptic}`, and the divisor-plus-order form of that principle closes
through Hadamard applied to `numProd` and `denProd`:

```
N_Ψ = N_Φ·e^g ,  D_Ψ = D_Φ·e^h      (Hadamard, on the entire halves)
  ⇒  Ψ/Φ = e^(g−h)                  entire, nowhere zero
  ⇒  constant                        (hper + const_of_doublyPeriodic)
```

So routes A and B are not rivals; B needs a brick that only A supplies. What
stays retracted is the **target**: Hadamard applies to `numProd`/`denProd`, which
are proved entire, and never to `phiBProd`, which is not. That distinction was
the actual content of this audit and it survives intact — only the "no consumer"
disposal was wrong.

## Recommended action

1. Fix `HadamardFactorization.lean`'s motivation to point at route B, so the
   next agent does not resume PI-4/PI-5 believing it discharges
   `uniqueUpToScalar`. (Done in this change.)
2. Put effort on `qou-cons` **as restated** — T2a/T2b first, which are cheap and
   establish that the route closes, before T2c (PI-4/PI-5), which is the hard
   analytic core and now has a legitimate reason to be worked.
3. Keep the Hadamard bricks. ~~They are good infrastructure with no current
   consumer.~~ Superseded by the addendum above: they are the mechanism the
   restated `qou-cons` runs on. Still do not finish them on the *original*
   justification, which remains retracted.
4. **Check first whether `numProd`/`denProd` have finite order**, and what ρ is.
   Nothing in the corpus computes it, and the whole route above is conditional
   on it. If the order is infinite the route dies and only a pinned-divisor
   argument survives — so this is cheap insurance against a wasted PI-5.

## The pattern, since it is the third instance in two sessions

Route A was built on a claim about its target that a sibling file in the same
repository already contradicted. The earlier two instances in this arc were the
"DG §4.5" misread and the ℕ-indexed Hadamard statement that is false for `exp`.
In all three the refutation cost minutes: read the source, instantiate at the
simplest object, grep the corpus for the same target. None had been done.
