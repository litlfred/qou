# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: routing the second literature batch, and what is still needed for the *bulk* rate

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-sine-kernel-rate-2026-08-29` · **Tier:**
literature routing + primary-source grep + a pointwise-rate probe (honest negative) · **Discipline:**
no fake closure. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

## The bulk rate must be argued at the *determinant* level (probe finding)

`wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py` measured the pointwise error
`|J(x, x+k; θ) − S(k, a)|` (discrete Bessel vs discrete sine kernel) in the bulk. **Honest negative:**
it does **not** decay cleanly — the log-log slope scatters in `[−2, +2]` across `r, k, θ` — because
(i) the local density `a = x/√θ` rounds by `O(1/√θ)` and `S` is sensitive to it, and (ii) the
discrete-Bessel→discrete-sine convergence carries an **oscillatory** sub-leading term (the same
Airy-edge oscillation seen in the `V_A` remainder). So a naive *"pointwise kernel bound, then
integrate"* route is not clean. The bulk rate must be argued at the **integrated** level — the
variance / Fredholm- or Toeplitz-determinant, where the oscillations cancel. The clean integrated rate
is already measured: `Var(Σ|c|)/θ² → 8/π²` at `θ^{−1}` (`qou-tvok`, PR #5959). This **redirects** the
open citation from a pointwise Olver bound to the Toeplitz-determinant route.

## What the second batch (owner upload `ae1c51be`, 23 papers) provides

| cluster | docs | relevance to `qou-k5r5` |
|---|---|---|
| **Tracy–Widom edge kernels** | `hep-th-9211141` (Airy), `hep-th-9304063` (Bessel / hard edge) | the Painlevé / Fredholm-determinant **method** at the *determinant* level — the right level per the probe. Airy is the **edge**; Bessel is the **hard edge**. They bound the *oscillatory edge* part of the remainder, not the bulk. |
| **hard/soft-edge transitions** | `cond-mat-9811142` (O–U / S–U transitions at hard & soft edge) | edge-crossover correlations; edge, not bulk. |
| **TW resurgence** | `2509.20302` (universality in resurgence of generalized TW) | edge distribution tails; not a bulk rate. |
| **chiral RMT / QCD Dirac spectrum** | Verbaarschot `hep-ph-0003017`, `hep-th-9212088`, `hep-th-9609174`, `hep-th-9711057`, `hep-th-9803007`, Damgaard `hep-th-0006111`, Wilson-Dirac `1001.2937`/`1108.3035`, `hep-lat-*` | the microscopic Dirac spectrum **is** the hard-edge Bessel kernel in a QCD setting — same kernel as Gorbunov's, methodology-adjacent, but hard-edge, and QCD-specific. |
| **off-topic (not routed to `qou-k5r5`)** | symbiotic-star X-ray `0907.4143`, magnetar mergers `1202.0461`, quantum repeater `1312.3086`, Walnut theorem-proving `1603.06017`, epidemic models `1712.03058`, Landen transformations `0707.3910`, Euclidean QG `72-4-841` | ingested for completeness; may serve other framework areas or be misdirected. Flagged, not used here. |

**Corpus-grep of the batch** for `sine kernel` / `toeplitz` / `discrete sine` / `widom` / `bulk
scaling` / `szegő`: the TW and cond-mat papers *mention* the (bulk) sine kernel as the companion case
but **none carries the bulk discrete-sine-kernel rate** for the Plancherel descent process.

## Answer to "need lit?" — YES, for the bulk specifically

This batch strengthens the **edge** side (Airy/Bessel Painlevé machinery, useful for bounding the
oscillatory edge part of the `θ^{−1}` remainder) and the **method** (determinant-level), but it does
**not** supply the **bulk** discrete-sine-kernel rate. The precise remaining targets, in decreasing
directness:

1. **Widom's Toeplitz-determinant asymptotics for the discrete sine kernel** — the paper BOO Remark
   1.6 cites as `[41]` ("answering a question of Dyson"). This is the *discrete* case and the most
   direct: the Plancherel descent process *is* this Toeplitz determinant.
2. **Tracy–Widom, "Level-spacing distributions and the sine kernel"** (`hep-th/9303139`, the bulk
   companion of the two edge papers now in the batch — **not yet uploaded**). Painlevé V representation
   for the bulk gap probability; the bulk analogue of `9211141`/`9304063`.
3. **Gorbunov 2024** (`sm10137`, already in corpus) + **Borodin–Okounkov** Toeplitz identity — the
   *continuous* Bessel rate via Kac–Akhiezer, which must be **transported to the discrete Plancherel
   variance**. This is the analytic step, not a drop-in.
4. **Deift–Its–Krasovsky** Toeplitz+Hankel determinant asymptotics *with error term* — the general
   engine for such rates (not in corpus).

If the goal is to *cite* the bulk rate, uploading (1) Widom or (2) `hep-th/9303139` is the highest-
value next step. If the goal is to *derive* it, the route is (3): apply Gorbunov's Kac–Akhiezer +
Borodin–Okounkov machinery to the discrete descent variance — a genuine analytic step this corpus now
has the tools for.

## Status of `qou-k5r5`

Unchanged in verdict, sharper in detail: the leading margin is **proved** (rigorous `V_D` ceiling),
the **tail** and **de-Poissonization** are **cited** (Johansson), the bulk rate's **method** is now
well-represented (Tracy–Widom determinant machinery + Gorbunov), and the one open input is the **bulk
discrete-sine-kernel rate**, whose most direct citation (Widom / TW-sine) is named and not yet in the
corpus. Gap **OPEN**. No fake closure.

## Compute + sources

- [`wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py) (exit 0; NO float64; honest-negative pointwise measurement).
- Batch: `library/arxiv-hep-th-9211141v1` (TW Airy), `library/arxiv-hep-th-9304063v2` (TW Bessel), `library/arxiv-cond-mat-9811142v1`, `library/arxiv-2509.20302v1`, chiral-RMT cluster; full list in `library/INDEX.md`.

## Cross-references

- Prior gap statement + first batch: [`2026-08-29-covariance-kernel-M1-k5r5-tail-half-and-ingested-kernel-rate-lit.md`](2026-08-29-covariance-kernel-M1-k5r5-tail-half-and-ingested-kernel-rate-lit.md)
- Cited-inputs Lean class: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/M1DescentDPPConvergence.lean`
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
