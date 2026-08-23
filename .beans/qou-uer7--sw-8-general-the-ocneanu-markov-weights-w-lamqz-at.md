---
# qou-uer7
title: 'SW-8 general: the Ocneanu Markov weights w_lam(q,z) at every n'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T16:51:49Z
updated_at: 2026-08-23T17:18:15Z
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


## Attempted 2026-08-23 — NOT closed; the corpus's candidate formula FAILS validation

Went to formalise the general weight and validated the existing candidate first.
It does not hold up.

### Established exactly (sympy over Q(q,z), no floats)

1. **The normalisation is `sum_lam d_lam . w_lam = 1`, not `sum_lam w_lam = 1`.**
   Verified against the Lean-proved n=3 weights. This is what `markovTrace3_one`
   encodes (trace of the identity in block lam is d_lam) and what
   `HeckeWedderburnData.markov_eq` expects. Landing exactly on 1 also
   cross-checks that the weights were transcribed correctly.
2. **The denominator of every proved weight IS the q-hook product**
   `prod_x [h(x)]_{q^2}`: (3) and (1^3) give [2]_{q^2}[3]_{q^2}, (2,1) gives
   [3]_{q^2}. The Ocneanu SHAPE is right at n=3.

### What fails

`computations/mass_at_3A_proper.py::jones_wenzl_weight` implements

    omega_lam = z^(n-1) prod_x (1 - z q^{2c(x)}) / (1 - q^{2h(x)})

and its docstring claims `sum_lam omega_lam = 1`. Across **160 convention
combinations** — exponent in {1,2}, q -> {q, q^2, -q, 1/q}, ten z-substitutions,
both plausible targets (w_lam and d_lam.w_lam) — it NEVER reproduces the proved
n=3 weights and NEVER sums to 1.

Probe: `computations/schurweyl/ocneanu_weight_validation.py` (exact arithmetic).

### Why nothing was formalised

The candidate is the only general formula in the corpus and it fails the one case
that is Lean-proved. Formalising it would launder a fit. This area already
produced a correction cycle (`qou-2tuv`) — a reason for more care, not less.

### Next honest step

DERIVE rather than recall: solve the defining conditions (trace property,
`tr(x.sigma_n) = z tr(x)`, normalisation) at n=4 in exact arithmetic, read the
numerator structure off against the hook-product denominator that IS confirmed,
and only then formalise.

**Separable finding:** the `jones_wenzl_weight` defect is a live bug in a
production compute path, independent of SW-8.
