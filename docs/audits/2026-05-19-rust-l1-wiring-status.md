# Rust L1 wiring — partial (paper follow-up)

**Date:** 2026-05-19
**Trigger:** Repo-owner directive 2026-05-19 "5 we will need all nucleotides" — the Python `markov_peel` chain bottoms out at ⁶Li (n=18) due to compute time; Rust binary path was queued to extend coverage.

## What landed this PR

1. **Cherry-picked the duplicate-fn fix** (commit `688dd7587`, originally `efb328031`):
   PR #683's merge into main left two definitions of
   `chi_lambda_canonical_h_n_mpfr` and `chi_lambda_canonical_all_partitions_mpfr`
   in `tools/hecke-engine/src/wenzl_lr.rs`. The cherry-picked fix deletes the
   older 2^k-expansion implementations, keeping the new direct-averaging path.

2. **Rust binaries now build cleanly** — `cargo build --release` produces
   the full set: `hecke`, `hecke-allparts`, `hecke-atomic`, `hecke-bigint`,
   `hecke-canonical-chi`, `hecke-crt`, `hecke-engine`, `hecke-float`,
   `hecke-gram`, `hecke-hapower`, `hecke-irrep`, `hecke-mass`, `hecke-modular`,
   `hecke-molecular`, `hecke-pergen`, `hecke-qvalues`, `hecke-stream`,
   `hecke-tensor`, `hecke-tr-m-wenzl-lr` (and a few more).

3. **Smoke-tested `hecke-tr-m-wenzl-lr`** via the existing Python wrapper
   `markov_trace_via_wenzl_lr.py` — produces per-partition χ^λ values for
   the 4-way decomposition (p, p, n, n) at H_12 with 77 partitions in ~seconds.

## Why L1 extension is NOT wired in this PR

The Rust binaries use a **different strand-count convention** than the
canonical Python pipeline:

| Quantity | Python (`canonical_braid_crossings`) | Rust (`hecke-atomic`) |
|---|---|---|
| Strands per nucleon | 3 (color-tube) | 1 |
| Strands for proton (Z=1, N=0) | 3 | 1 |
| Strands for ⁴He | 12 | 4 |

The Rust `hecke-atomic`'s output `net` value for D (Z=1, N=1, 2 strands) is
0.895. Our canonical |tr_M(D, q_0)| from `canonical-mass-table-extended` is
0.388. **These are not directly comparable** — they're traces of different
braids (1-strand-per-nucleon vs 3-strand-per-nucleon), in different Hecke
algebras (H_2 vs H_6).

A correct wiring would:

1. Decide which convention the canonical pipeline should consume (the paper's
   3-strands-per-nucleon framing in `def:color-tube-cubic` is the established
   choice).
2. Either (a) rewrite the Rust binary to take a generic braid word in 3·A
   strands, OR (b) build a Python→Rust adapter that converts between the
   two conventions.
3. Verify the converted values reproduce the Python pipeline at A ≤ 6 (where
   both can be computed).
4. Run for A = 7..12 (⁷Li, ⁷Be, ⁸Be, …, ¹²C) where Python `markov_peel`
   becomes intractable.

This is a non-trivial wiring task (estimated 1-2 days), not a quick fix.
Filed as follow-up.

## Production wiring already on main: `hecke-mass`

The Rust binary `hecke-mass` (visible in `target/release/`) is a self-contained
Z=1..20 mass-table computer. Sample output:

```
Atom   Z   N    M_const    binding     M_pred      M_obs     err%
   H   1   0    938.783    -0.9978    938.273    938.272  +0.000%
  He   2   2   3756.697    -3.0024   3755.163   3727.379  +0.745%
  Li   3   4   6574.611    -7.1003   6570.983   6533.833  +0.569%
  Be   4   5   8452.959    -4.7690   8450.523   8392.751  +0.688%
   B   5   6  10331.308   -16.5139  10322.869  10252.548  +0.686%
   C   6   6  11270.091   -12.9534  11263.472  11174.863  +0.793%
   N   7   7  13148.440    -0.5720  13148.147  13040.204  +0.828%
   O   8   8  15026.788   -14.8699  15019.190  14895.081  +0.833%
   F   9  10  17844.702   -29.9344  17829.406  17692.302  +0.775%
  Ne  10  10  18783.485   -15.1651  18775.736  18617.730  +0.849%
```

Errors are 0.5-0.85% — comparable to mass-table-ppb's L2 α-cluster
predictions. Not currently consumed by the canonical-isotope-witness
pipeline; could be wired as a separate predictor track if useful.

## Open follow-ups

1. **Convention adapter** (Python ↔ Rust braid representation) to wire
   `hecke-atomic` / `hecke-tr-m-wenzl-lr` into `canonical_mass_table_extended.py`.
2. **`hecke-mass` integration** — produces 20-atom binding predictions
   directly; could be added as an L1.5 layer in `canonical_isotope_witness.py`
   alongside L1 / L2 / L3.
3. **Validation** — once wired, cross-check Rust |tr_M| against Python
   `markov_peel` at A ≤ 6 to confirm conventions match.

The infrastructure is now buildable (build fix landed); the wiring is
the next session's work.
