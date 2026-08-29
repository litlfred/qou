# The determinacy filter is half wrong — what survives is falsifiability, not correctness

**Date** 2026-08-27 · **Branch** `claude/determinacy-filter-binding-candidates-2026-08-27` ·
**PR** [#5868](https://github.com/litlfred/qou/pull/5868) · **Bean** `qou-pjq5` ·
**Scope** (a) throughout — a triage heuristic excludes nothing.

## The heuristic under test, and whose it was

PR [#5863](https://github.com/litlfred/qou/pull/5863) closed two fronts that came
out structurally opposite, and **I** proposed a filter from the contrast:

> Prefer candidate binding terms carrying a genuine **extremal or structural
> determinacy**; treat a **free continuous parameter with no optimum** as a
> warning sign.

The author authorised testing it. It is my own generalisation from two cases —
exactly the shape of claim this repository's disciplines exist to catch — so the
task was to break it before applying it. **It breaks in both halves.**

## Defect 1 — "extremal" was doing no work

An extremal principle over an underdetermined constraint carries **zero**
information about which coordinate wins. For a single constraint
$\sum_i a_i x_i = b$, the cheapest single-support solution at coordinate $i$
costs $w_i |b| / |a_i|$, so the ordering between two coordinates is governed by
$w_i / |a_i|$ alone — and $a$ is fixed by the constraint while $w$ is not.

`QOU.MassTheory.both_orderings_achievable` proves **both** orderings are
reachable by choosing the cost, for **any** constraint whatsoever. The optimum
determines nothing; the objective does, and the objective is a modelling choice.

**Measured on the real Hecke objects**, not just proved in the abstract. Taking
$a_\lambda = y_\lambda \chi^\lambda(\beta)$ for the two-row $\lambda \vdash 6$ at
the proton-pinned $q_0$:

| $\lambda$ | $\lvert a_\lambda \rvert$ | $w/\lvert a\rvert$ (Plancherel-style) | $w/\lvert a\rvert$ (Frobenius-style) |
|---|---:|---:|---:|
| $(6)$ | 0.215679 | **0.534703** | 5.401796 |
| $(5,1)$ | 0.198041 | 1.993347 | **1.126895** |
| $(4,2)$ | 0.064726 | 6.400714 | 1.861592 |
| $(3,3)$ | 0.011614 | 6.510861 | 18.410605 |

The two costs select **different partitions** — $(6)$ against $(5,1)$ — on the
same feasible set.

**The corpus said this in May and I had not read it.** Option D of the Δ_λ
programme is recorded as *"reproduces Occam exactly (L∞ = 1.91e-15); **moves the
underdetermination to the choice of cost** rather than eliminating it"*, with a
second cost picking a different singleton
([`2026-05-09-mass-table-fitting-audit.md`](2026-05-09-mass-table-fitting-audit.md)).
Those specific numbers are **cited, not re-run**; the measurement above is an
independent instance of the same phenomenon, and the generality comes from the
Lean.

## Defect 2 — "structural" does not predict success

Option B, the Frobenius co-Casimir $1/\dim_q(\lambda)$, is recorded in that same
table as **"theorem-forced (no free params)"** — maximally structural by my
filter — and it **failed** (residual $-2.30$ MeV, wrong sign). Later confirmed
*"PROVED-INSUFFICIENT … vortex-blind"*
([`2026-06-01-e0-lambda-substrate-derivation-options.md`](2026-06-01-e0-lambda-substrate-derivation-options.md)).
Two more structural candidates are in the same position (Demazure-fibre;
PROBE-4 KL crystal weights). **Three of eight.**

The reason is computable from the formula rather than from the fit. The per-block
slot genuinely varies with the braid word — measured
$\max_\lambda \lvert \chi^\lambda(w_A) - \chi^\lambda(w_B) \rvert = 1.3301$ over
the two-row $\lambda \vdash 6$ — but $1/\dim_q(\lambda)$ **has no word argument at
all**, so it contributes the same number to every atom. That is what
"vortex-blind" means, recomputed here rather than taken on trust.

## What survives, and it is the opposite of what I claimed

> **The filter separates DETERMINATE from UNDERDETERMINED. It does not separate
> right from wrong, and it never could.**

Its value is *falsifiability*, not correctness. A candidate with no free choice
yields a definite prediction and therefore becomes **testable** — co-Casimir was
promoted to a testable claim and refuted in one measurement, which is the filter
working, not failing. An underdetermined candidate can never be falsified,
because it absorbs any residual into its free choice. So the warning sign means
**"this cannot be tested"**, not "this will be wrong".

And the free choice hides in **three** places, not one:

| where the freedom sits | worked example |
|---|---|
| a free **parameter** | the growing-width cut's $w$ (Addendum 42) |
| a free **objective** | Option D's cost — Plancherel vs Frobenius |
| a free **selection rule** | Occam's "single-support + min $\lvert\Delta\rvert$" |

My original phrasing named only the first, which is why "extremal" looked like an
escape from it. It is not: **an optimum relocates the freedom into the
objective.**

## The tautology charge, answered

Every classification above is read off the candidate's **specification** — does a
parameter, objective or selection rule remain unfixed? — so it is available
*before* the fit is run. Co-Casimir's blindness is computable from
$1/\dim_q(\lambda)$ alone, with no reference to the outcome. The rule is not a
post-hoc re-description.

## 🛑 Do not quote the 8/8

The refined rule scores 8/8 on the settled table, and **that number is not
evidence**. I assigned *both* axes of that table — the free-choice label and the
outcome class — so it checks my own bookkeeping, not the rule. The two
load-bearing results are:

- **A1**, three structural candidates that failed, recorded by *other* agents at
  the time; and
- **A3**, the two costs measurably selecting different partitions on freshly
  built Hecke objects.

For the refined rule ever to earn a hit-rate, it needs candidates classified
**before** their outcomes are known. That is a future test, not this one.

## Artifacts

- Probe: [`determinacy_filter_calibration_probe.py`](../../computations/meson/determinacy_filter_calibration_probe.py) — 6/6.
- Lean: [`ExtremalPrincipleDoesNotDetermine.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ExtremalPrincipleDoesNotDetermine.lean)
  — 4 declarations, sorry-free (`cost_lt_iff`, `both_orderings_achievable`,
  `two_costs_two_minimisers`, and the non-vacuity guard
  `equal_costs_are_decided_by_the_constraint`, which shows equal costs *are*
  decided by the constraint, so the theorem is about the modelling choice and not
  an ill-posed comparison).

## Scope

**Scope (a).** Nothing here refutes any candidate — a triage heuristic cannot
exclude anything; only a proved invariant can. The one general theorem
(`both_orderings_achievable`) is about single-constraint L1 extrema, not about
LP methods in general, and says only that *having an optimum is not the same as
being determined*. Whether any particular objective is itself derived is a
separate question this document does not touch.
