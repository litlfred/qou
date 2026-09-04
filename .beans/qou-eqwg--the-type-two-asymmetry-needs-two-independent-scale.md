---
# qou-eqwg
title: The type-two asymmetry needs two independent scales and the framework has one
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:02:09Z
updated_at: 2026-09-04T12:23:03Z
---


Opened 2026-09-04 from the `qou-oooq` type-two result, and it is close to a
falsification of that result rather than a follow-on to it.

## The finding it constrains

`the_asymmetry_term_lives_at_vassiliev_type_two_probe` established, exactly:

    c_2 / c_0  =  (N - Z)^2 / 2  +  (5 - A)/8      [chain, A = 3..10, every Z]

read as `-alpha c_2/c_0` = `-alpha(N-Z)^2/2 + alpha A/8 - 5alpha/8`, i.e. an
asymmetry term and a volume-like term with the SEMF's signs and forms.

## The constraint, measured

**One overall scale cannot fit both terms.** With `alpha = 4.185981 MeV`:

| | model | SEMF | |
|---|---|---|---|
| volume-like | `alpha/8 = 0.5232` MeV/nucleon | `a_V ~ 15.8` | 30x low |
| asymmetry | `alpha/2 = 2.093` per `(N-Z)^2` | `-a_A(N-Z)^2/A`, `a_A ~ 23` | no `1/A` |

Scale `alpha` by the `30.2x` that fixes the volume and the asymmetry becomes
`63.20` per `(N-Z)^2`, against SEMF's `a_A/A`:

| A | SEMF needs | model gives | over by |
|---|---|---|---|
| 8 | 2.875 | 63.20 | 22x |
| 20 | 1.150 | 63.20 | 55x |
| 56 | 0.411 | 63.20 | 154x |

and it gets worse with `A`, because the model's asymmetry is `A`-independent
while SEMF's falls like `1/A`. **There is no `alpha` making this a SEMF.**

## So the question is not "where does the 1/A come from"

It is: does the framework have a SECOND independent scale for the graded terms,
or does it not? If every graded coefficient is multiplied by the same `alpha`,
this direction is dead on arithmetic and no amount of `1/A`-hunting rescues it.

- [x] **ANSWERED: per-PARTITION, not per-type.** `unified-iterative-correction`
      assembles `B_lambda = m_e H_q(lambda) u_lambda (ln|tr M_lambda| - ln d_lambda)`,
      and `prop:mass-coefficient-shadow-price` says each mass-formula coefficient
      is the shadow price of the corresponding PARTITION's Frobenius positivity
      constraint. The Vassiliev types index the cost-vector BASIS the LP is posed
      in; the shadow prices it returns are lambda-indexed. "Independent linear
      programs" is not "independent units". Superseded: `vassiliev-filtration-mass-tower`'s "independent linear
      programs" phrasing suggests per-type cost vectors, which would supply
      per-type scales — but "independent programs" is not the same as
      "independent units", and this has to be read, not assumed.
- [ ] If one scale: close this and `qou-oooq`'s type-two line negative, and say
      plainly that the shape result cannot be scaled to data.
- [ ] If per-type scales: the `1/A` question becomes live again, and the place
      to look is the `c_0` normalisation (`z0^(A-1)`, exponential in `A`) rather
      than the coefficient itself.
- [ ] Either way, do NOT report the type-two result as "SEMF-shaped" without
      this attached. The shapes match and the scales cannot.


## Closed negative (2026-09-04)

Audit: `docs/audits/2026-09-04-graded-scales-are-per-partition-not-per-type.md`.

**No per-type scale exists.** The free scales are `H_q(lambda) * u_lambda`,
indexed by partition, and the sum runs over partitions. So the two-scale escape
is unavailable and this bean's arithmetic (22x / 55x / 154x) is a closing
argument rather than an open question.

**And the logarithm removes the term anyway, for the chain.** The assembly
applies `ln|tr M_lambda|`, and `qou-m3sh` proved the chain's Markov trace is
exactly the product of scalar two-strand factors (~1e-59). `ln` of a product of
scalars is exactly additive, so the pair-convolution carrying `(N-Z)^2` cannot
survive. Verified: the additive `L`'s type-two piece is linear in `Z`.

**Retraction recorded in the audit.** A matrix version of the test appeared to
reverse this — `[h^2] ln|V|` second differences constant at `3/4` — but used a
mis-transcribed transfer matrix (`V = 1.128089` at `q_0` where the proved
single-crossing factor is `z = 0.612688`). Retracted in full. The narrower
question it should have asked is untested and left open in the audit: the corpus
multiplies transfer matrices WITHIN a generator and takes a scalar product
ACROSS generators, so whether non-commutativity inside a generator can carry a
quadratic is not settled by anything here.
