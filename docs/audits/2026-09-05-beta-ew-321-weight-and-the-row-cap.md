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

> **🛑 RE-DERIVED, and "at least 5" was itself far too generous — it is 11 of
> 37 (2026-09-05, PR #6840).** The paragraph above reads as though one file had
> slipped through. Measured with a detector keyed on **provenance** — what each
> operand was assigned *from* — rather than on the local variable's spelling,
> **seven** files build `dim_q(...)² / q_factorial(...)` and **none** of them was
> visible to the regex:
>
> | spelling in the source | why the regex missed it |
> |---|---|
> | `dim_q_num(...) ** 2` | call — `(` stops `\w*` |
> | `q_dimension(...) ** 2` | word order: no `dim_q` substring at all |
> | `_q_dimension(...) ** 2` | word order + leading underscore |
> | `d_q_lam ** 2` | suffix after `d_q` — the instance found above |
> | `dq[l] ** 2` | subscript between the name and `**` |
> | `d ** 2` | single-letter local, assigned from `dim_q_via_hooks` |
> | `dim_q(part) ** 2` | **a call to `dim_q` itself** |
>
> The last one is the finding. `dim_?q\w*\s*\*\*` cannot cross a `(`, so the
> pattern could only ever have matched a *variable* named `dim_q`, never a
> *call* to the function it is named after — not an exotic alias but the
> ordinary spelling. So the `_lam` suffix diagnosed above is correct about its
> own instance and **wrong as a characterisation of the defect**: the detector
> was not narrow, it was looking at the wrong syntactic category.
>
> **Three of the seven are on the α_EM axis** (`alpha_5_jucys_murphy_central`,
> `alpha_em_b2_scalar_c_probe`, `alpha_em_b2_canonical_scale_ratio_probe`),
> which the `4 of 36` figure hid entirely — and that axis matters more than the
> count, because the corpus's one scoreable L2 result (`m_K/m_π`) is
> α_em-conditional.
>
> **Triaged in the same PR** ([`alpha_em_b2_weight_family_triage_probe.py`](../../computations/probes/alpha_em_b2_weight_family_triage_probe.py),
> 2/2). `alpha_em_b2_scalar_c_probe.py` pins the B2 scalar `c` on `w_(4,1)(q₀)`
> and its own verdict calls that *"the canonical **Markov** normalization"*. At
> λ = (4,1), n = 5, q₀, 50 dps:
>
> | family | value | role |
> |---|---|---|
> | Plancherel `d_q²/[5]_q!` | `0.12862000417524688333` | what it **computes** |
> | Molien `f^λ q^{−κ} d_q/[5]_q!` | `0.07429973308938433194` | canonical per `qou-oots` |
> | Markov `y_(4,1)` at N=2 | `0.12498539716794710592` | what it **calls** it |
>
> Three objects under one name — the collision the notation register warns
> about. The identification is *measured*, not inferred from the source shape:
> the assertion reproduces the consumer's printed value to 22 digits at 1e-18.
>
> **Molien moves this axis by −42.23 %, and no cancellation is available.** The
> `qou-oots` result that a λ-independent rescale drops out of a same-n ratio —
> which is why `dim_q²/[n]_q! → dim_q²/D²` is a no-op for the β_EW consumers —
> does **not** reach here: this consumer normalises on a **single** partition,
> so there is no ratio for anything to cancel from, and Molien's `q^{−κ}` is
> λ-dependent besides.
>
> The Markov row is the quiet one: **2.83 %** from Plancherel, close enough that
> the mislabel would never be caught by eye.
>
> **Not a claim that `c` is wrong.** That probe is explicit that
> `c = (Markov norm)/(Hodge polarization norm)` and that the Hodge denominator —
> the Braden–Northover period polarization of `Jac(Bring)` — is not supplied, so
> `c` is not a delivered number. What is measured is the size of the family
> choice on its numerator, and a mislabel in its verdict string.
>
> **The other two α_EM files are now triaged too, and neither needs a change.**
>
> `alpha_em_b2_canonical_scale_ratio_probe.py` is the **counter-example**: it
> tabulates `y_λ` and `w_wedderburn` side by side under explicit labels, and
> its own comment already states the distinction correctly — *"tr(1)=1 for the
> canonical Markov trace: `sum_lam y_lam * f^lam = 1`. (NOT `sum_lam w_lam` —
> that equals 1 only at q=1; the Wedderburn weight `w_lam` is a distinct corpus
> normalization, reported as-is.)"* So the mislabel is specific to the B2
> scalar probe, **not** general to the axis.
>
> `alpha_5_jucys_murphy_central.py` is **affected in principle, immaterial in
> fact**. Its headline compares `Σ_{λ ⊢ 3A, ht=6} w_λ c_5(λ)` across A = 2,3,4
> with `w = dim_q²/[n]_q!` — and since `n = 3A` that is a cross-atom metric at
> three different `n`, the use `AGENTS.md` and `qou-oots` R2 both exclude
> scope-(b). Measured
> ([`alpha5_jm_crossatom_budget_probe.py`](../../computations/probes/alpha5_jm_crossatom_budget_probe.py),
> 2/2): the height-6 partial budget `B_6(A)` spreads **222×** across those A,
> and `α_5(A) = B_6(A)·⟨c_5⟩_A` factorises exactly (to 1e-40), so a raw spread
> genuinely cannot separate *"c_5 moved"* from *"the budget moved"*.
>
> **But the conclusion is route-invariant and is a negative.** The producer's
> own three routes give relative spreads of **482.16 %** (normalised by
> `[3A]_q!`), **83.16** (raw) and **1327.18 %** (self-normalised — the route R2
> admits), and its verdict is *"strongly atom-dependent (mechanism orthogonal
> to JM-central)"*. The weight-family choice can neither rescue nor overturn a
> negative all three routes agree on, so the Molien ruling requires no change
> here. I was heading for a distortion finding; the measurement says the result
> is robust.
