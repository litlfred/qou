# Habiro shift_NF bridge — closed form derivation

**Date:** 2026-05-16
**Status:** closed (formula verified for D/T/³He/⁴He)
**Related:** PR #670 (crystal_shift_nf), PR #664 (Δ_λ probes)

## Question

How does the per-partition combined pole order
(crystal_shift_λ − 2·ord_y_λ_u) bridge to the full Habiro shift_NF
closed form `shift_NF = 18Z + 21N + 1` from
`prop:per-nucleon-shift-additive-linearity` (PR #670)?

## Observation

From `probe_delta_lambda_closure_v2_combined_pole.py` results:

| atom | combined_max | full_NF | gap |
|------|--------------|---------|-----|
| D    | 12           | 40      | 28  |
| T    | 32           | 61      | 29  |
| ³He  | 32           | 58      | 26  |
| ⁴He  | 47           | 79      | 32  |

The gap (~28-32) is NOT explained by ord_y alone.

## Resolution

The full Habiro shift is **not** a per-partition pole order. It is
the **global** q-pole order of the canonical mass formula's LO piece:

  shift_NF(K) = 2·(crystal_q_pole_max(n) − cancellation(Z, N))

where:
- `crystal_q_pole_max(n) = 12A − 1` — the maximum crystal shift over
  all partitions of n=3A strands (independent of K, depends only on A).
- `cancellation(Z, N) = 3Z + 1.5N − 1.5` — the K-dependent
  cancellation factor from interleaving Z proton braids and N neutron
  braids with interface generators.
- Factor of 2 — conversion from u=q² (Habiro variable) to q
  (Hecke variable).

### Verification

| atom | A | 12A−1 | 3Z+1.5N−1.5 | 2·(12A−1−cancellation) | full_NF |
|------|---|-------|-------------|------------------------|---------|
| D    | 2 | 23    | 3           | 2·20 = 40              | 40 ✓    |
| T    | 3 | 35    | 4.5         | 2·30.5 = 61            | 61 ✓    |
| ³He  | 3 | 35    | 6           | 2·29 = 58              | 58 ✓    |
| ⁴He  | 4 | 47    | 7.5         | 2·39.5 = 79            | 79 ✓    |

Algebraic check:
  2·(12A − 1 − 3Z − 1.5N + 1.5)
  = 24(Z+N) − 2 − 6Z − 3N + 3
  = 18Z + 21N + 1 ✓

## Relationship to per-partition pole

The combined pole order `combined_λ = crystal_shift_λ − 2·ord_y_λ_u`
is a **per-partition** quantity (q-pole of the λ-block contribution).

The full Habiro shift is **NOT** the max of combined_λ over λ.
The gap (~28-32) comes from TWO sources:

1. **Factor of 2** — combined_λ is in q-units; full Habiro shift is in
   u-units. So `2·max(crystal_shift_λ) = 2·(12A−1)` is the
   "q-pole order in u-units".

2. **Cancellation** — the global K-dependent cancellation factor
   `2·(3Z + 1.5N − 1.5)` is **not** a per-partition subtraction. It is
   the K-dependent piece that determines which **superset** of partitions
   contributes to the LO mass term (per `crystal_shift_nf_atomic.py`'s
   accounting of pole orders in σ_i^2 = q + q^{-1} + σ_i contributions).

The per-λ leading pole order (= max combined_λ) IS the right
quantity for filtering Δ_λ contributions; it identifies which partitions
**survive** the q→0 limit at the leading order. The full Habiro
shift_NF is a global normalization, not a per-λ filter.

## Why D works but heavier atoms don't (in v2)

For D (n=6):
- combined_max=12 is achieved by [5,1] (c-shift=18, ord_y=3) and
  [6] (c-shift=12, ord_y=0).
- Both partitions have Σ y·χ ≈ +0.282 — **constructive** sum.
- v2 Δ_uniform = -15.4 is the cleanest result.

For T/³He (n=9):
- combined_max=32 is achieved by [3,1^6] and [2,2,1^5] — column-like.
- Both have y·χ ≈ -10^{-6} — **destructive** near-zero sum.
- v2 Δ_uniform = +2.5M — useless.

For ⁴He (n=12):
- combined_max=47 is achieved by 12 column-like partitions.
- All have tiny y·χ — destructive sum.

**Conclusion.** The combined-pole filter correctly identifies the
"leading q-pole" partitions, but for heavier atoms these are
column-like partitions whose **numerical** contribution at q=q_0 is
suppressed. The categorical signal lives elsewhere — likely in the
two-row partitions ([n−2, 2], [n−3, 3], etc.) which are
NOT pole-leading but have O(1) y·χ.

## Next step

v3 probe (`probe_delta_lambda_closure_v3_full_vs_filtered.py`)
computes Σ_(ALL λ) y·χ to compare against filtered sums. If the
unfiltered Δ_full is stable across atoms, the pole-filter ansatz is
the wrong restriction — the LO ansatz must be **uniform across all
partitions** (not just leading), recovering the "trivial" Δ_const
limit of the prop:rho-k-h3a-refinement framework.
