# 2026-09-05 — The (3,2,1) Weinberg construction: its weight is not a Markov trace, and its block is unoccupied

Bean `qou-wapd`. Follow-on from `qou-oots` (the Molien weight made canonical for
`Φ_k`, merged in #6771).

## Why this was opened, and why the question changed under it

The `qou-oots` consumer audit named
[`beta_ew_delta_I_321_and_wedderburn.py`](../../computations/beta_ew_delta_I_321_and_wedderburn.py)
as the one live non-harness file still carrying the superseded
`dim_q²/[n]_q!` weight. The intended follow-on was to migrate it to Molien.

Reading it first turned up a prior question, and then the corpus-grep turned up
that the corpus had **already adjudicated** it. Both are recorded here, in that
order, because the second supersedes the first.

## Finding 1 — the aggregate is not a Markov trace

The file computes, and labels, a *"Wedderburn-weighted Markov trace"*:

```
tr_M(β_EW Δ_I) = Σ_λ w_λ · χ^λ,     w_λ = dim_q²/[n]_q!
```

The canonical Frobenius pairing of this framework is `tr_M = Σ_λ y_λ χ_λ` with
the **Ocneanu** weights. Measured
([`probes/beta_ew_weight_is_not_markov_probe.py`](../../computations/probes/beta_ew_weight_is_not_markov_probe.py),
4/4, n = 6, q₀, 50 dps):

| quantity | value |
|---|---|
| `Σ y_λ · χ^λ(1)` | **1.000000000000000000…** |
| `Σ (dim_q²/[n]_q!) · χ^λ(1)` | **11.13944754035206007** |

A Markov trace is normalised — `tr_M(1) = 1` by definition — so this is a fact
about the object, not a choice of convention. The exact `1.000…` also confirms
the `y` weights were read correctly, so the comparison does not rest on a
reconstruction of them.

**They do not share a support.** At n = 6, `y_λ` is exactly zero on **7 of the
11** partitions — every λ with more than two rows — while the weight in use is
nonzero on all 11. A weight that vanishes where another is positive cannot be
reached from it by any λ-independent rescaling, so these are sums over
different index sets rather than two normalisations of one sum.

**It is not the q-deformation.** The notation register says the three
partition-weight families coincide at `q = 1`. Control at `q = 1 + 1e-25`:
`y_λ` is still zero on the same 7 partitions and the shared-support ratio spread
is still **189**. The support difference is the row cap — a statement about `N`
— and it survives the classical limit. *"The families coincide at q = 1"* does
not extend to `y_λ` at `N = 2`.

## Finding 2 — which the corpus already had: the block is unoccupied

[`appendix-standard-model/sm-params-gauge-couplings.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-params-gauge-couplings.md)
states it directly:

> $(3,2,1)$ has three rows, and the Schur–Weyl row cap gives $\dim V_\lambda = 0$
> whenever $\ell(\lambda) > N$; the fibre is the fundamental of
> $\mathrm{SU}_q(2)$, so $N = 2$ and that block carries no states. Its Ocneanu
> weight vanishes identically … Every route from such a block to a physical
> number is either a Markov trace, which the row cap sends to zero, or a
> spectrum, which has no states to act on; a quantity recovered by subtraction
> is a difference of Markov traces and so, by linearity, is itself the first
> kind.

Confirmed numerically here: `y_(3,2,1) = 0` exactly at `N = 2`;
`0.0103939752433` at `N = 3`; `0.0147953354077` at `N = 4`.

That appendix also records that the resulting `cot θ_W ≈ 1.8208` **"must not be
cited as a framework accuracy result"**: its own witness reports the ansatz as
*neither supported at 10⁻³ nor falsified at 10⁻²*, and the residual factor was
selected as the closest of **74 enumerated candidates**.

**Consequence for the original task: the migration question is moot.** Moving
this file to Molien would move a physics-facing number inside a construction the
paper has already placed outside the carrier. Not done, deliberately.

## What was actually changed

Documentation only. No production number moves.

- Both consumer files carry a module-docstring note stating that the aggregate
  is not a Markov trace, that the block is unoccupied at `N = 2`, that the file
  was deliberately **not** migrated to Molien, and what remains open.
- The user-visible output labels no longer call the aggregate a Markov trace.

## What is open, and the one route with a number attached

At `N = 3` the block **is** occupied (`ℓ(λ) = 3 ≤ N`) and a genuine Markov trace
exists, so the row-cap objection is scoped to `N = 2` and does not exclude an
`N = 3` reading. The corpus separately holds every piece of that route without
having connected them here: the flavour sector **requires** `N = 3`
(`y_lambda_su_n.py`; `RowCapObstruction.lean`, sorry-free); the mass channel
**cannot** be retuned to `N = 3` (`ocneanu_N_lockin_probe.py`); therefore
flavour needs a **second trace on the same `H_n(q)`**, which
`HnMarkovTrace.lean` already makes typeable by carrying the Markov parameter as
a free class field.

Measured
([`probes/beta_ew_n3_second_trace_probe.py`](../../computations/probes/beta_ew_n3_second_trace_probe.py)),
characters taken exactly through the consumers' own Hoefsmit path:

| N | `tr_M(β_EW Δ_I)` | occupied blocks | `y_(3,2,1)` |
|---|---|---|---|
| 2 | 4.83789085692050323822 | 4 / 11 | 0 |
| **3** | **2.90062956640672874659** | 7 / 11 | 0.0103939752433 |
| 4 | 2.19236562357645905376 | 9 / 11 | 0.0147953354077 |

**Do not read the N = 3 row as either confirmation or refutation.** A Markov
trace is normalised and is not dimensionally a cotangent; the consumers build
`cot θ_W` from *ratios* of weighted quantities, not from a bare trace. The row
is recorded so the magnitude is on file and the route can later be judged on a
number rather than on an idea.

**Not claimed:** that `N = 3` is the right reading of the electroweak sector.
The corpus's own preferred lever is elsewhere — the Milnor triple linking
`μ̄₁₂₃`, which supplies the writhe-independent second crossing invariant and
separates the two U(1)'s that `θ_W` mixes. What `μ̄₁₂₃` does not yet supply is
their relative coupling normalisation, which inherits the open flavour SU(3)
sector.

## A defect in the `qou-oots` audit, found by this work

[`audits/w_lambda_family_consumer_audit.py`](../../computations/audits/w_lambda_family_consumer_audit.py)
reported the blast radius of the Molien ruling as **4 of 36 files**. It is at
least **5**. [`close_321_weinberg_gap.py`](../../computations/close_321_weinberg_gap.py)
builds `w_lam = d_q_lam ** 2 / fact_n` — the identical superseded weight — and
the classifier filed it under **NAME-ONLY** ("token present, no construction"),
because the detector's pattern expected `dim_q**2` and the variable is named
`d_q_lam`; the `_lam` suffix defeated the match.

Two things follow. The **NAME-ONLY bucket is not a safe bucket** — it is a lower
bound on "computes no weight", exactly as that audit's own limits section says,
and this is the first measured instance. And the 4 was an undercount, so the
figure should be re-derived rather than quoted.

This is the same detector-blindness class `AGENTS.md` catalogues, and this
instance is the audit author's own.
