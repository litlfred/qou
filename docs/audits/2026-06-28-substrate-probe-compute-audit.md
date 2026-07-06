# Compute audit — substrate lever-1 / W_λ / binding probes (beans z3a2, f273)

**Date:** 2026-06-28
**Beans:** `z3a2` (shared cached module), `f273` (BlockCache/LaurentQ + slow-sympy hotspots)
**Scope:** the `computations/substrate/` probes authored across PRs #2899/#2929/#2941/#2951.

## Finding 1 — duplicated Young-diagram machinery (z3a2)

Seven probes each re-implement and re-compute the same `partitions / conj / hooks / dim_q / qint /
qfact / S(m)` machinery symbolically from scratch (the dominant per-probe cost):

| probe | duplicated defs |
|---|---|
| `lever1_qinvolution_kernel_test.py` | 4 |
| `lever1_qholonomic_kernel_fit.py` | 4 |
| `lever1_qholonomic_order3_fit.py` | 4 |
| `lever1_binding_habiro_qexponential.py` | 4 |
| `binding_qaskey_product_probe.py` | 4 |
| `wlambda_identity_i_structure_probe.py` | 2 |
| `lever1_lw_depth2_recurrence_test.py` | 3 |

**Fix (z3a2):** the shared `computations/substrate/young_qdim.py` (merged #2952) — `lru_cache`-memoised
`dim_q` / `S` / `qfact` / `qint`, so repeated and cross-probe calls are free after the first compute.
Migration of the seven probes to `from young_qdim import …` is the z3a2 deliverable.

## Finding 2 — `sp.simplify` where `sp.cancel` suffices (f273)

`sp.simplify` is general and slow; for rational functions in `q` (the entire substrate workload)
`sp.cancel` is the correct, far cheaper primitive, especially in `== 0` equality tests. Hotspot
counts (`sp.simplify` calls per probe):

| probe | `sp.simplify` | `sp.cancel` |
|---|---|---|
| `lever1_lw_depth2_recurrence_test.py` | **6** | 5 |
| `lever1_qinvolution_kernel_test.py` | **5** | 6 |
| others | ≤ 1 | 3–7 |

**Fix (f273):** in the two hotspot probes, replace `sp.simplify(expr) == 0` /
`sp.simplify(a - b) == 0` rational-equality tests with `sp.cancel(expr) == 0`. (Where `simplify`
guards a non-rational/transcendental, leave it.)

## Finding 3 — BlockCache / LaurentQ wiring (f273, deferred)

These probes are pure sympy symbolic-`q` work; they do **not** touch the Hecke/Markov-trace compute
where `BlockCache` and `LaurentQ` (the Rust/`pyhecke` fast paths) apply. So BlockCache/LaurentQ wiring
is **not applicable** to this probe family — the relevant speedups are the in-process `lru_cache`
(Finding 1) and the `simplify→cancel` swap (Finding 2). The BlockCache/LaurentQ audit axis stays open
for the `pyhecke`-consuming producers (a separate, larger f273 sub-scope, deferred).

## Disposition

- z3a2: migrate the seven probes to `young_qdim` (this PR, verified per-probe).
- f273: apply `simplify→cancel` in the two hotspot probes (this PR); BlockCache/LaurentQ axis deferred
  to the `pyhecke`-consuming producers.
