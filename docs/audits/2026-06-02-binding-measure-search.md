# The binding measure w_λ^bind — content-weight carries the A-extensive scaling

**Date:** 2026-06-02
**Probe:** [`probe_binding_measure_search.py`](../../computations/probe_binding_measure_search.py)
→ `probe-binding-measure-search.witness.json`
**Status:** EXPLORATORY; asserts the refutation. A≥3-absolute binding still open,
but the search returns a **strong structural lead**.

## Context

The prior probes localized the gap precisely: the per-block q-Reeb phase
`θ_λ = arccos(χ^λ/d_λ)` is the right CARRIER, but the Markov/trace measure `y_λ`
is the wrong MEASURE for absolute binding — `Σ y_λ|Δθ_λ|` *anti*-correlates with A
because `y_λ` suppresses the growth channels
([2026-06-02-full-theta-binding-probe.md](2026-06-02-full-theta-binding-probe.md)).
This probe searches for a parameter-free per-block weight `w_λ^bind` such that
`B = E·Σ_λ w_λ |Δθ_λ|` tracks the extensive A-growth (binding ratio ⁴He/D = 12.72).

## Result — `abs_content` matches the A-growth

| weight `w_λ` | worst \|err\| (1 scale) | **S(⁴He)/S(D)** | T/³He diff err |
|---|---|---|---|
| `y_λ` (trace measure) | 198.8 % | 0.04 | −102.7 % |
| `dim_classical` (d_λ) | 97.9 % | 627.5 | −116.2 % |
| `dim_q` (q-hook) | 99.0 % | 1235.9 | −110.2 % |
| `1/y_λ` | 100.0 % | 90545.7 | −100.1 % |
| `bar-y` (q→q⁻¹ dim) | 99.0 % | 1235.9 | −110.2 % |
| **`abs_content`** (Σ\|j−i\|) | **19.9 %** | **13.40** | −190.1 % |

**target `S(⁴He)/S(D)` = 12.72** (binding grows ~13× D→⁴He).

`abs_content` — the total |content| of the Young diagram, a **parameter-free
combinatorial invariant** — is the unique candidate whose A-scaling matches the
binding (**13.40 vs 12.72, ~5 %**); all others are off by 1–4 orders of
magnitude or anti-correlated. It cuts the worst absolute error from 199 % (`y_λ`)
to 20 %.

## Interpretation — w_λ^bind factorizes

- ✅ **Extensive A-scaling = content-weighted phase.** The binding's growth with
  mass number is carried by `Σ |content_λ| · |Δθ_λ|` — content is the q-grading /
  eigenvalue-spread of the block, and it emphasises exactly the long-row/column
  (growth) reps that `y_λ` suppresses.
- 🔴 **Differences need the signed structure.** `abs_content` is transpose- and
  isospin-blind, so it breaks the T/³He difference (−190 %), which the *signed*
  bar-symmetric phase combination got to +8 %.

So the per-block binding measure **factorizes**:
`w_λ^bind ≈ (content-weight; extensive A-scaling) × (signed phase; differences)`,
distinct from the scalar-trace `y_λ`. This is the refined target for the
operator-valued combiner (#1698): a content-weighted, sign-aware per-block
measure on the emitted `θ_λ` vector — NOT `y_λ`.

## Caveat (discipline)

20 % worst error is **not a closure**, and `abs_content` was *selected* from a
6-candidate list — so the A-growth match is a **structural lead, not a derived
result**. The next step is to (a) derive why `|content|` is the extensive weight
(it is the `L₀`/energy grading of the Hecke module — plausibly the "Hecke
energy" density itself), and (b) combine it with the signed bar-symmetric phase
and re-test for joint closure of *both* absolute and differences. Δ_λ /
A≥3-absolute remains an open gate; this narrows `w_λ^bind` to a content × sign
factorization.
