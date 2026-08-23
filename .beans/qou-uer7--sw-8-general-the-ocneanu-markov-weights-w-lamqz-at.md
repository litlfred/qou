---
# qou-uer7
title: 'SW-8 general: the Ocneanu Markov weights w_lam(q,z) at every n'
status: todo
type: task
priority: normal
created_at: 2026-08-23T16:51:49Z
updated_at: 2026-08-23T16:52:30Z
parent: qou-59vq
---

## What SW-7 left, and what it did not

`heckeWedderburnDataOfWeights` (PR to follow) builds `HeckeWedderburnData` at
EVERY n from `heckeWedderburn` (SW-7, merged c18a357142). But the weight family
`w : Partition (n+1) -> R` is a **parameter of that construction, not a result of
it**. `markov_eq` holds by `rfl` because `markov` is DEFINED as
`sum_lam w_lam chi_lam`. So the structural half is done and the content is not.

## The actual open item

Which `w` makes the functional a genuine MARKOV TRACE. Two properties single it
out:

- trace property: `tr(xy) = tr(yx)`;
- Markov condition: `tr(x . sigma_n) = z . tr(x)`.

At n=3 both are proved — `HeckeMarkov3.markovWeight0/1/2 (q z)` with
`markovWeights_markov_sigma1`. At general n they are open. The classical answer is
Ocneanu's weight, a ratio of q-hook products over the diagram, and getting it
will want the branching rule rather than more linear algebra.

## Do not read the structure instance as delivering this

`heckeWedderburnDataOfWeights` will happily accept ANY `w`, including nonsense,
and the resulting term is still a well-typed `HeckeWedderburnData`. A downstream
consumer could therefore call `markov` a Markov trace without it being one. The
naming keeps `weight` visibly an input and the module docstring says so; anyone
wiring this into an R2 result should supply a `w` with the two properties PROVED,
not merely chosen.
