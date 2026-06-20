# Gap-narrowing with forced y_λ weights DEFLATES the Reeb-flow correction (~1–6% of binding)

**Date:** 2026-06-20
**Branch:** `claude/qbk2-rigorous-log-neumann-2026-06-20`
**Status:** Honest deflation — the forced physical weighting kills the binding-scale match. No fit, nothing wired.
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Follows:** PR #2549 (rigorous, raw unweighted ratio 2.23×)
**Script:** [`computations/qbeta/qbessel_reeb_yweighted_gap.py`](../../computations/qbeta/qbessel_reeb_yweighted_gap.py) (`GAP-NARROWING TEST COMPLETE`)

## What was tested

#2549 gave the rigorous, resonance-free, proxy-free correction at ratio **2.23×** the
deuteron binding — but **unweighted**. The binding sum is
`B = m_e Σ_λ y_λ χ_λ Δ_λ`, so the physical correction must carry the canonical Markov
weights `y_λ` (`wedderburn_jones_markov.y_lambda_at`, substrate-fixed → **no knob**).
This applies them.

## Result — the correction collapses

| form | value | ratio to `B(D)/m_e ≈ 4.35` |
|------|-------|----------------------------|
| raw, unweighted (#2549) | 9.72 | **2.23** |
| **(A) `Σ_λ y_λ·ΔG`** | −0.056 | **−0.013** |
| **(B) `Σ_λ y_λ·χ_λ·ΔG`** | −0.244 | **−0.056** |

Both forced-weighted forms are **~1–6% of the deuteron binding — i.e. ~20–80× too
small.**

### Why (mechanism of the deflation)
The Markov measure `y_λ` concentrates on the **low blocks** (`[6]`, `[5,1]` with
`y≈0.059`), which have small `ΔG`; the **large** `ΔG` blocks that drove the unweighted
2.23× (e.g. `[3,2,1]`, `ΔG=8.5`, but `y=0.0073`; `[4,1,1]`, `ΔG=−9.3`, `y=0.010`) carry
**tiny** weight. The forced physical weighting suppresses exactly the blocks the
unweighted sum was riding on. So the on-scale appearance at #2545/#2547/#2549 was an
artifact of omitting the Markov measure.

## Verdict — the quadratic-action Reeb-flow correction is NOT the binding mechanism

The full progression, each stage removing an artifact:

| stage | ratio | what it was |
|-------|-------|-------------|
| #2545 (`ν±0.5` proxy) | 6.16 | proxy/pole artifact |
| #2547 (PV, dim≥2 only, unweighted) | 1.27 | confluent blocks excluded |
| #2549 (rigorous, all blocks, unweighted) | 2.23 | **unweighted** |
| **y-weighted (forced)** | **0.01–0.06** | the physical object |

**With the forced Markov weights — the binding sum's actual measure — the rigorous
Reeb-flow / quadratic-action correction is ~20–80× too small to be the deuteron
binding.** The earlier on-scale ratios were unweighted-sum artifacts. No fit could close
a 20–80× gap without abandoning the forced weights (which would be a fit).

Secondary flag: forms (A) and (B) **diverge** (62% relative spread), so the propagator's
*place* in the binding sum (does it multiply `χ_λ`?) is itself unpinned — but this is
moot, since **both** forms are far too small.

## What stands, and what doesn't

- **Stands (valid results):** the owner's Reeb-flow steer correctly identified the
  radial argument (forced, real); the reduction-of-order construction is rigorous and
  resonance-free (PR #2549); the q-Casoratian/Abel **Lean lemma**
  (`QOU/QBeta/QCasoratianAbel.lean`, sorry-free) is sound q-special-function machinery.
- **Does not stand (the physics claim):** the q-Bessel "quadratic action" does **not**
  supply the binding-energy correction — once the forced `y_λ` measure is applied it is
  two orders of magnitude too small. The lead, pursued rigorously through five PRs, is
  **refuted as a binding mechanism** by its own forced weighting.

This is the honest end of the binding thread: the machinery is real and Lean-backed, but
the physical correction is too small. No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.
The owner closes the bean (§4a).
