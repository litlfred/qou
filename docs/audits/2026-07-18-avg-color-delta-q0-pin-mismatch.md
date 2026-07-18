# `_avg_color_delta()` evaluates the color split at the *proton* q₀ — a mixed-pin (bean-`tnjb`) hazard for muon-q₀ 1ppQ computes

**Date:** 2026-07-18 · **Axis:** q₀-anchor convention / L1 precision hygiene ·
**Tier:** finding + guidance (scope-(a); no mass migration — owner-gated per
AGENTS.md). **Branch:** `claude/focused-euler-ez3iu4`.

## The finding

`computations/canonical_braid_crossings._avg_color_delta()` caches

```python
from q_parameter import Q as _Q0
_AVG_COLOR_DELTA = flavor_split_leading(mp.mpf(str(_Q0)))
```

`q_parameter.Q` is the **proton-pinned** q₀ (the package layer,
`tools/qou-substrate/.../constants.py`, `_solve_q_proton_f64`). But the canonical
`computations/` derivation layer — including the L1 Markov-trace certification —
is **muon-pinned** (`q-pinning-50-digit.witness.json`,
`1.109978595557…`, −11.5 ppb from the proton pin). See AGENTS.md
§"q₀ anchor convention (STRICT)".

So a compute that reads the **muon** q₀ for its trace but takes its color split δ
from `_avg_color_delta()` gets δ at the **proton** q₀ — a **mixed pin**.

## Why it is exactly 3.2e-7 in δ (and ~5.86e-11 in tr_M)

`flavor_split_leading(q) = (q−1)²(1−q⁻⁴)/3` is the **exact** closed form — it
equals `markov_peel._color_delta`'s δ_symbolic to 2.6e-54 at a fixed q₀ (verified).
The error is **not** the formula; it is the q₀ argument. With
δ ∝ (q−1)² to leading order,

$$\frac{\partial \delta}{\delta} \approx \frac{2\,\Delta q_0}{q_0-1} \approx \frac{2\,(11.5\text{ ppb})}{0.11} \approx 3.2\times10^{-7},$$

matching the measured `|Δδ|/δ = 3.220e-7` between `_avg_color_delta()` and
`flavor_split_leading(q₀_muon)`. Propagated through the color-weighted seam of an
atomic Markov trace this is **≈ 5.86e-11** — the exact residual seen in the L1
third-method investigation
([`2026-07-18-l1-third-method-cw-seminormal.md`](2026-07-18-l1-third-method-cw-seminormal.md)),
whose earlier "leading-order approximation" framing this audit **corrects**.

## The fix (per consumer, trivial — no shared-util change, no mass migration)

`flavor_split_leading(q)` already takes q as an argument. A muon-q₀ 1ppQ compute
should call

```python
delta = flavor_split_leading(q0_muon)   # q0 from q-pinning-50-digit.witness.json
```

instead of `_avg_color_delta()`. **Do NOT** change `_avg_color_delta()`'s default
or mass-migrate consumers: per AGENTS.md §"q₀ anchor convention" STRICT rule 4
and bean `tnjb`, the muon/proton split is deliberate and owner-gated. This is a
**reporting/precision-layer** correction applied only where 1ppQ is asserted on a
muon-q₀ trace — not a rewrite of the ~840 muon-q₀ witnesses.

## Consumer classification

*Background classification sweep in progress (~40 `_avg_color_delta` consumers →
MIXED-PIN-1ppQ / MIXED-PIN-scopeA / CONSISTENT buckets); the table is filled in a
follow-up commit.* Preliminary: the L1 cert path is CONSISTENT (peel + the new
seminormal leg both use the muon q₀); the ⁴He binding stage-2 probe is
MIXED-PIN-scopeA (uses `_avg_color_delta` on a muon-q₀ trace but is not
1ppQ-gated, so the ~5.86e-11 is within tolerance — the trailing ~15 digits of its
serialized tr_M(K) are not pin-independent, but no precision claim rests on them).

## Scope note

The L1 certification path is **not** affected: `cross_check_trM_1ppb.py` uses
`markov_peel` (exact δ at the muon q₀) and the chi-cache combiner; the new L1
third method (`cross_check_trM_cw_seminormal_leg.py`) computes δ inline as
`(q₀−1)²(1−q₀⁻⁴)/3` at the **muon** q₀ — both correct. The mixed-pin hazard is
latent in `_avg_color_delta()` consumers, quantified and bucketed above so any
future 1ppQ work on those paths uses the local-q₀ δ.

## Cross-references

- L1 third method + the corrected framing: [`2026-07-18-l1-third-method-cw-seminormal.md`](2026-07-18-l1-third-method-cw-seminormal.md)
- q₀ convention: AGENTS.md §"q₀ anchor convention (STRICT)"; bean `tnjb`
- δ closed form: `computations/_li_2_q_util.py::flavor_split_leading` (`prop:flavor-split-substrate`)
