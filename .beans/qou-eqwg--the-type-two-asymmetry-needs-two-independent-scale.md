---
# qou-eqwg
title: The type-two asymmetry needs two independent scales and the framework has one
status: todo
type: task
priority: normal
created_at: 2026-09-04T12:02:09Z
updated_at: 2026-09-04T12:03:01Z
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

- [ ] Establish whether the corpus's graded/LP-SDP reading applies one scale or
      a per-type scale. `vassiliev-filtration-mass-tower`'s "independent linear
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
