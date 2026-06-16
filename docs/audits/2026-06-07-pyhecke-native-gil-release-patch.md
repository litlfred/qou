# pyhecke_native — GIL release + batched Geck-Pfeiffer patch (2026-06-07)

> **Two ready-to-apply Rust patches** to `tools/pyhecke-native/src/lib.rs`
> + (optional) `tools/hecke-engine/src/geck_pfeiffer.rs`. Combined
> expected speedup on the `derived_chi_catalogue_sweep` heavy atoms
> (⁷Li → ⁹Be): **~50-100×** wall-time. Without the patches, the
> in-Python multiprocessing wrapper
> ([`derived_chi_catalogue_parallel.py`](../../computations/derived_chi_catalogue_parallel.py))
> already delivers ~Nx (N = cpu_count) via ProcessPoolExecutor — but
> threads give 0× because the current binding holds the GIL.

## Problem

`pyhecke_native.chi_q_via_gp(lambda, n, word)` is the catalogue's
canonical character-derivation entry point. The Phase 3 production
isotope sweep
([`derived_chi_catalogue_sweep.py`](../../computations/derived_chi_catalogue_sweep.py))
calls it once per `(λ, n_strands, word)` triple — for ⁹Be (`n=27`),
that's **3,010 calls** (p(27) = 3010 partitions).

Two issues today:

1. **GIL hold.** The PyO3 binding has no `py.allow_threads(...)` wrap,
   so during the Geck-Pfeiffer compute the Python interpreter cannot
   release control. **ThreadPoolExecutor → 0× speedup measured 2026-06-07.**
2. **No batched-GP endpoint.** Each call to `chi_q_via_gp` re-runs
   the Geck-Pfeiffer reduction of `T_β` to the canonical basis — the
   expensive part. For a full atom sweep, that's wasted: the GP
   reduction depends only on `(n, word)`, not on `λ`.

Measured baseline (4-core CPU box, 2026-06-07):

| atom | n | partitions | sequential | 4-process pool | ratio |
|---|---|---|---|---|---|
| ⁴He | 12 | 77 | 3.11s | 1.05s | **3.0×** |
| total A≤4 sweep | — | 154 | 3.40s | 1.23s | **2.8×** |

Extrapolating per-cell `O(n^10)` empirical scaling, ⁹Be in the current
sequential pipeline: **~4 days**.

## Patch 1 — GIL release on `chi_q_via_gp` (1-line equivalent)

Letting Python threads parallelise is sufficient on its own to take
⁹Be from ~4 days → ~6 hours (16-core box, threads). Combined with
multiprocessing it doesn't add more; but threads are lighter (no IPC
overhead, shared memory), so worth doing.

**File:** `tools/pyhecke-native/src/lib.rs`

**Before** (current source — confirmed in this audit):

```rust
#[pyfunction]
fn chi_q_via_gp(
    lambda: Vec<usize>,
    n: usize,
    word: Vec<(i32, u32)>,
) -> Vec<(i32, String)> {
    let poly = geck_pfeiffer::chi_lambda_via_geck_pfeiffer(&lambda, n, &word);
    poly.terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect()
}
```

**After**:

```rust
#[pyfunction]
fn chi_q_via_gp(
    py: Python<'_>,
    lambda: Vec<usize>,
    n: usize,
    word: Vec<(i32, u32)>,
) -> Vec<(i32, String)> {
    py.allow_threads(|| {
        let poly = geck_pfeiffer::chi_lambda_via_geck_pfeiffer(&lambda, n, &word);
        poly.terms
            .into_iter()
            .map(|(he, c)| (he, c.to_string()))
            .collect()
    })
}
```

Apply the same wrap to: `mn_chi_q`, `chi_q_via_gp` (this one),
`chi_lambda_braid`, `chi_lambdas_braid`, `chi_q_word`,
`chi_q_via_gp` (alt names if any).

Rebuild:

```bash
cd tools/pyhecke-native
maturin develop --release
```

Verify after rebuild:

```python
import time
from concurrent.futures import ThreadPoolExecutor
import pyhecke_native as ph

# ... build word, parts as in the sweep
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(lambda lam: ph.chi_q_via_gp(lam, n, word), parts))
# Should be ~8× faster than sequential on an 8-core box.
```

## Patch 2 — Batched `chi_lambdas_via_gp` (Rayon-parallel, single GP reduction)

The bigger win. New function: take **all partitions at once**, do GP
reduction once, then evaluate the character on each partition by
multiplying the canonical-basis coefficients against the partition's
seminormal characters.

This requires factoring `chi_lambda_via_geck_pfeiffer` into two parts:
1. `canonical_basis_decomposition(n, word) -> CanonicalBasisExpansion`
   — the expensive part.
2. `chi_from_canonical_expansion(lambda, n, &expansion) -> LaurentPoly`
   — cheap per partition.

**File:** `tools/hecke-engine/src/geck_pfeiffer.rs` — refactor needed.

**File:** `tools/pyhecke-native/src/lib.rs` — new binding:

```rust
#[pyfunction]
fn chi_lambdas_via_gp(
    py: Python<'_>,
    shapes: Vec<Vec<usize>>,
    n: usize,
    word: Vec<(i32, u32)>,
) -> Vec<Vec<(i32, String)>> {
    use rayon::prelude::*;
    py.allow_threads(|| {
        // Do GP reduction ONCE for this (n, word).
        let expansion = geck_pfeiffer::canonical_basis_decomposition(n, &word);
        // Then loop characters in parallel.
        shapes.par_iter().map(|shape| {
            let poly = geck_pfeiffer::chi_from_canonical_expansion(
                shape, n, &expansion);
            poly.terms.into_iter()
                .map(|(he, c)| (he, c.to_string()))
                .collect()
        }).collect()
    })
}
```

Expected combined speedup over current sequential:

| atom | n | partitions | current | + Patch 1 | + Patch 2 |
|------|---|-----------|---------|-----------|-----------|
| ⁴He | 12 | 77 | 3.1s | ~0.4s | **~0.08s** |
| ⁷Be | 21 | 792 | 2.5h | ~20 min | **~3 min** |
| ⁹Be | 27 | 3010 | 4 days | ~6 hours | **~30 min** |

(`+ Patch 1` assumes threads; `+ Patch 2` assumes Rayon par_iter inside
Rust + 8 cores effective.)

## Why these patches are safe

- Patch 1 is purely additive — `py.allow_threads` doesn't change the
  function's input/output, just permits other Python threads to run
  during the Rust compute.
- Patch 2 adds a new function; existing `chi_q_via_gp` callers are
  unaffected. The Python sweep can gate on `hasattr(ph,
  'chi_lambdas_via_gp')` and fall back.

## Risk

- Rebuild of pyhecke_native takes ~minutes; if it fails, the system
  install at `/usr/local/lib/python3.11/dist-packages/pyhecke_native/`
  remains intact.
- The GP refactor (Patch 2) is the larger code change. Stage it
  separately from Patch 1.

## Path to apply

1. Branch off `main`, apply Patch 1, run `maturin develop --release`.
2. Sanity-test: existing `chi_q_via_gp` calls return identical results;
   `ThreadPoolExecutor` now scales linearly.
3. Apply Patch 2, run `maturin develop --release` again.
4. Add to `derived_chi_catalogue_parallel.py` a `parallel_chi_q_via_gp_batch`
   fast-path: `if hasattr(ph, 'chi_lambdas_via_gp'): return ph.chi_lambdas_via_gp(...)`.
5. Run the full A≤9 production sweep; expect ~30 min for ⁹Be.

## In-Python fallback (already landed)

While the Rust patches are pending,
[`derived_chi_catalogue_parallel.py`](../../computations/derived_chi_catalogue_parallel.py)
uses `ProcessPoolExecutor` to spawn N Python subprocesses (each with
its own pyhecke_native), bypassing the GIL via process isolation. This
gives ~Nx speedup (3× measured on 4 cores) with zero Rust changes —
sufficient for A ≤ 6 sweep in foreground, and a manageable overnight
run for A=8, 9.
