# `y_λ` is not `f^λ·q^{−κ_λ}/[n]_q!` — and a float trap that flipped the test twice

**Date:** 2026-08-22
**Status:** NEGATIVE RESULT (scope (a)) + a producer precision trap.
**Follows:** [`2026-08-21-molien-mining-the-correct-q-analogue-of-rsk.md`](2026-08-21-molien-mining-the-correct-q-analogue-of-rsk.md)
**Bean:** `qou-3quc` (parent arc)

## The conjecture, and its refutation

The Molien note established, in the balanced convention,

```text
  Σ_λ  f^λ · q^{−κ_λ} · d_q(λ)  =  [n]_q!
```

Dividing by `[n]_q!` puts it in the same *shape* as the Markov normalisation
`Σ_λ y_λ · (dim) = tr_M(𝟙) = 1`. That suggested

```text
  y_λ  ?=  f^λ · q^{−κ_λ} / [n]_q!
```

**Refuted.** At `q = 2`, `n = 4`, where the producer returns exactly-representable
values:

| λ | `y_λ` | predicted |
|---|---|---|
| (4) | 0.5456 | 1/8925 ≈ 0.000112 |
| (3,1) | 0.1344 | 16/2975 ≈ 0.00538 |
| (2,2) | 0.0256 | 128/8925 ≈ 0.0143 |

Orders of magnitude apart — far outside any numerical tolerance. Also refuted at
`n = 3` and at `q = 3/2`.

**Why the inference was wrong, and it is an instructive error.** `Σ_λ c_λ · (dim) = 1`
is **one linear equation in `p(n)` unknowns**; it does not determine the
coefficients, so two families can both satisfy it and be different. Worse, the two
sums do not even pair against the same dimension function — `y_λ` pairs with the
SU(2) quantum dimension (the producer's own docstring says so), while `w_λ(q)`
carries the q-hook dimension. Reading "same shape" as "same object" is exactly the
claim-shape conflation `da-arity-conflation` names.

Scope: this is a **(a) scope-limited negative** — that particular closed form is
wrong. It excludes no *ingredient*; `f^λ`, `q^{−κ_λ}` and `[n]_q!` may all appear in
some correct relation between the families. No such relation is claimed here.

## The float trap — the part worth carrying forward

`wedderburn_jones_markov.y_lambda_at(n, q)` returns sympy **`Float`** even when `q`
is an exact `sympy.Rational`:

```text
  y_lambda_at(4, Rational(3,2))[(2,1,1)]  ->  type=Float, repr=0.0

     sympy.simplify(that) == 0   ->   False
     sympy.nsimplify(that) == 0  ->   True
```

Two standard normalisations **disagree about whether the same value is zero**, and
neither is wrong: `simplify` leaves a `Float(0.0)`, which does not compare equal to
the integer `0` under that path, while `nsimplify` rationalises it to `Zero`.

This is not academic. It flipped a structural test in this very session **twice**:

1. A first pass (using `nsimplify`) reported `y_λ = 0` for every λ with more than
   two rows — read as the SU(2) truncation.
2. A second pass (using `simplify`) reported those same values as **non-zero**, and
   the truncation reading was retracted as a `q = 2` artefact.
3. A third pass showed the retraction was itself the artefact: the values *are*
   zero, and pass 2 was reading float residue.

Both of my intermediate conclusions were wrong, in opposite directions, from the
same producer output. Recorded rather than quietly resolved, because the failure
mode is reusable and the corrected reading is not the interesting part.

**Guidance for anyone probing these weights:** do not zero-test `y_lambda_at`
output with a bare `== 0`. Rationalise first (`nsimplify`), or compare against a
tolerance and *say which*. Better, get an exact path: the producer's float return
on exact input is the AGENTS.md §"PROBES ARE NOT EXEMPT" hazard inside a canonical
producer, and it means no probe over `y_λ` can currently claim an exact identity.

## What is *not* claimed

- No claim that `y_λ` vanishes on >2-row partitions. It is consistent with every
  reading above, but the float path cannot separate "exactly 0" from "1e-31", so
  this note does not settle it.
- No claim about *why* the two families differ beyond the dimension-pairing
  observation, which is read off the producer's docstring, not derived.
- Nothing downstream changes. The Molien identity is unaffected — it does not
  mention `y_λ`.
