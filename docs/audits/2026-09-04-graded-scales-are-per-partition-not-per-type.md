# The mass formula's scales are per-partition, not per-type — so the type-two asymmetry has nowhere to be scaled from

**Date:** 2026-09-04 · **Bean:** `qou-eqwg` (closed by this), `qou-oooq`, `qou-zlra`
· **Scope:** reading of existing blocks plus one exact check. Nothing wired, nothing fitted.

## The question

`qou-oooq` found an exact closed form for the chain's type-two Vassiliev
coefficient, `c_2/c_0 = (N-Z)^2/2 + (5-A)/8`, whose two terms have the SEMF's
asymmetry and volume shapes. `qou-eqwg` then measured that **one overall scale
cannot fit both**: rescaling `alpha` by the `30.2x` that fixes the volume-like
term overshoots the asymmetry by 22x at `A = 8`, 55x at `A = 20` and 154x at
`A = 56`, worsening with `A` because the model's asymmetry is `A`-independent
while the SEMF's falls like `1/A`.

That left one way out. If the framework carries an independent scale **per
Vassiliev type**, the two terms are not competing for one knob.
`vassiliev-filtration-mass-tower` seemed to offer it: the filtration supplies
"a canonical cost-vector basis at each type" and "a graded hierarchy of
independent linear programs".

## The answer: per-partition, and there is a logarithm in the way

`unified-iterative-correction` states the assembly:

```
B_lambda(Z, N) = m_e * H_q(lambda) * u_lambda * ( ln|tr M_lambda^(0..A)| - ln d_lambda )
```

and `prop:mass-coefficient-shadow-price` fixes what the scales index: "each
coefficient of the QOU mass formula is the shadow price (LP dual variable) of
the corresponding **partition's** Frobenius positivity constraint".

So the free scales are `H_q(lambda) * u_lambda`, indexed by **partition
`lambda`**, and the sum runs over partitions. The Vassiliev types index the
cost-vector *basis* the LP is posed in; the shadow prices it returns are
`lambda`-indexed. "Independent linear programs" is not "independent units", and
nothing in the assembly attaches a scale to a type.

**There is no per-type scale.** The two-scale escape is unavailable, and
`qou-eqwg`'s arithmetic therefore stands as a closing argument rather than an
open question.

## And the logarithm removes the term anyway, for the chain

The assembly applies `ln|tr M_lambda|`. For the canonical chain that is decisive,
because `qou-m3sh` proved (measured to `~1e-59`, and the affine law formalised
in `QOU.Mass.ChainTraceFactor`) that the chain's Markov trace is exactly the
**product of scalar two-strand factors**. A product of scalars has
`ln(prod) = sum of ln`, exactly additive — so the pair-convolution term
`sum_{i<j} f_i' f_j'` that carries the `(N-Z)^2` cannot survive the logarithm.
Verified directly in `the_asymmetry_term_lives_at_vassiliev_type_two_probe` §2:
the additive `L`'s type-two piece is linear in `Z`, all second differences zero.

## A retraction, recorded because it nearly went the other way

While closing this I ran a matrix version of the test, multiplying the corpus's
`M_2` transfer matrices and forming `V = z M_11 + M_21`, and it appeared to show
that the logarithm does **not** kill the quadratic — second differences of
`[h^2] ln|V|` constant at `3/4` rather than zero. That would have reversed the
conclusion.

It was wrong. My transfer matrix was mis-transcribed (indices swapped): with
`T = [[c h + d, c],[c, d]]` a single `pp` crossing gives `V = 1.128089` at `q_0`,
where the proved single-crossing bond factor is `z = 0.612688`. The object I
tested was not the corpus's. Retracted in full.

Two things follow for anyone repeating this. The corpus's `T` convention must be
pinned against the known single-crossing value `z + d` **before** any matrix
computation is trusted — that check takes one line and I did it only after
getting an exciting answer. And the genuine open question is narrower than the
retracted claim: the corpus multiplies transfer matrices *within* a generator
and then takes a scalar product *across* generators, so whether non-commutativity
inside a generator can carry a quadratic is untested, and is not what I tested.

## Status

- `qou-eqwg`: **closed negative.** No per-type scale exists; the type-two shape
  result cannot be scaled to data.
- `qou-oooq`'s type-two line: closed for the chain, on two independent grounds —
  the scale count, and the logarithm acting on a proved scalar product.
- `qou-zlra` (the `+c_k` / `-c_k` sign) is now moot for the chain and stays open
  only for whatever object the within-generator question turns up.
- Untouched: `qou-bygw`'s ordering ambiguity, and the all-pairs case generally.
