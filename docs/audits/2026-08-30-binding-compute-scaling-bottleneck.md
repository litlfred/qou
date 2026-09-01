# Where the binding-energy compute actually goes, and why it will not scale

**Measured 2026-08-30** on `origin/main`, container with `pyhecke_native 0.9.0`
installed. Every number below is measured in this session unless marked
otherwise. Bean `qou-i7ju` (the `hadron-knot-table` regeneration) is blocked on
this; the regeneration is not the problem, the producer is.

## Executive summary

| # | Finding | Severity |
|---|---|---|
| 1 | The `O(dim·nnz)` sparse path is **unreachable** — its guard is false exactly when it would help. Everything runs `O(dim³)` instead, at dims up to **2310**. | blocker |
| 2 | The hot file **never calls Rust**. `grep pyhecke_native\|hecke_engine computations/hecke_core_legacy.py` → **0 hits**. | blocker |
| 3 | The Rust MPFR matmul (`dense_dense_mul_mpfr`) **exists and is not exported** to Python. | blocker |
| 4 | Half the matmuls run in **float64**. Measured relative error **1.40e-16** against an all-mpf reference, in a 50-dps producer. | correctness |
| 5 | The `dim >= 8` numpy branch is a **pessimization** — measured 31 % *slower* than the Python loop it replaces. | perf |
| 6 | The q-Gaussian approximation tier is **dead by default** (`k_exact == k_max`). | design |

**Is everything in Rust?** No. The entire bottleneck is pure-Python `mpmath`.
The Rust crate is large and capable — `dense_la_mpfr.rs`, `seminormal_mpfr.rs`,
`matrix_m_mpfr.rs` — and the binding path touches none of it.

## How the bottleneck was localised

Stage timing of one atom (`hadron_knot_table`'s `compute_atom`), A=1 and A=2:

```
build_atom_nf           0.000s      classify_nuclear_knot   0.000s
nf_tr / nf_net          0.000s      binding_energy          >50 min, never returns
check_frobenius         0.000s
```

Everything except `binding_energy` is sub-millisecond. Splitting it three ways,
`unified_iterative_correction(1,1)` is the whole cost. **11 of 11 py-spy samples**
land on `hecke_core_legacy.py:1102`, reached from lines 1506/1507:

```python
def _matmul_dim(A, B, dim):
    if dim >= 8:
        return np.asarray(A) @ np.asarray(B)     # line 1102 — 100 % of samples
```

## Finding 1 — the fast path is gated off exactly when it is needed

```python
exact_chain = any(not isinstance(c, float) or not isinstance(d, float)
                  for c, d, _g in chain)
if s['sparse'] and not exact_chain:
    ...  # scipy sparse BLAS  -- O(dim·nnz)
    ...  # AND the COO object-arithmetic fallback, also O(dim·nnz)
else:
    ...  # _matmul_dim -- O(dim³)
```

Measured over every `(nucleon, prev_types, n_gens)` combination:
**`exact_chain` is True for every physical chain**, because the coefficient
histogram is `('int','int') 132`, `('int','mpf') 132`, `('float','float') 48` —
the `mpf` entries are real (they carry 50 digits), and `c` is the Python **int**
`1`, which is not a `float`.

So `not exact_chain` is never true, and **both** branches inside the guard are
unreachable — including the COO object-arithmetic accumulator whose own comment
says it exists for this case:

> *"Accumulating over σ's nonzeros is O(dim·nnz), the same complexity the
> float64 branch gets from sparse BLAS."*

That fix was written for exact chains and is gated behind a condition that
excludes exact chains. The inner `M_run.dtype == object` test already dispatches
correctly, so the guard should be `if s['sparse']:` alone.

**Consequence.** All 193 active partitions take the dense path, including the
124 built as `csr_matrix` — `_crossing_in_partition` densifies them
(`if hasattr(sig, "toarray"): sig = sig.toarray()`). Cost of one dense matmul at
the dims actually reached, at the measured mpmath rate of **2.3e-6 s per scalar
multiply-add**:

| dim | scalar ops | one matmul |
|---|---|---|
| 56 | 175,616 | 0.4 s |
| 162 | 4.25e6 | 10 s |
| 990 | 9.70e8 | 37 min |
| 1540 | 3.65e9 | 2.3 h |
| **2310** | **1.23e10** | **7.9 h** |

Summed over all active partitions, one crossing costs `Σ dim³ = 5.85e10` scalar
ops. Deuterium has 13 crossings × 2 matmuls → **~40 days**. Fe-56 has 1876
crossings → **~16 years**. Confirmed empirically: the call rate collapses as the
dims climb — 648 calls in the first 60 s, then 26 in the following 30 s.

### The one-line fix is necessary but NOT sufficient — tested

Changing the guard to `if s['sparse']:` was applied and run. py-spy confirms it
now takes the COO path (lines 1495/1500, no `_matmul_dim`). **Deuterium still
had not completed after 9 minutes.** The complexity drops `O(dim³) → O(dim·nnz)`
(~500× at dim 2310) but every scalar op is still a Python-level `mpmath` call.
Both layers have to be fixed. The patch was **reverted, not committed** — with
neither version completing there is no way to verify it preserves the number,
and this is a binding-energy producer.

## Finding 2 / 3 — Rust exists, is capable, and is not wired in

`hecke_core_legacy.py` contains **zero** references to `pyhecke_native` or
`hecke_engine`. `hadron_knot_table.py` imports `HeckeEngine` only for the
q-independent ground-state ordering.

`tools/hecke-engine/src/dense_la_mpfr.rs` already provides
`dense_dense_mul_mpfr`, `sparse_to_dense_mpfr`, `inverse_mpfr`, `rref_mpfr`,
`nullspace_mpfr`, `kron_mpfr`. `dense_dense_mul_mpfr` is called **16+ times
inside Rust** — and has **no `#[pyfunction]` wrapper**. Python gets
`mat_inverse_mpfr`, `mat_kron_mpfr`, `mat_nullspace_mpfr`: inverse, Kronecker,
nullspace — **not multiply**.

**Measured Rust speed.** `chi_lambda_braid_mpfr` runs `dense_dense_mul_mpfr` in a
loop; λ=(3,2,1), dim 16, 20 crossings → 8.024 ms total = **401 µs per matmul**,
against **9,600 µs** for the Python path at the same dim: **≥24×**. That is a
lower bound — the 401 µs also absorbs PyO3 crossing and seminormal construction.

## Finding 4 — half the matmuls are float64, in a 50-dps producer

The instrumented counter over `unified_iterative_correction(1,1)` recorded
`{'float64': 275, 'object': 271}` numpy dtypes. `_identity(dim)` returns
`np.eye(dim)` and `_crossing_in_partition` builds `c*sig_np + d*np.eye(dim)`, so
the product accumulates in float64 until the first `mpf` coefficient promotes it
— and the 53-bit truncation is then carried forward.

Measured against an all-mpf reference on partition (4,2), dim 9, a 4-crossing
chain:

```
max |current - all_mpf|   = 1.72817e-16
max |all_mpf|             = 1.23205
RELATIVE ERROR            = 1.40268e-16      (float64 eps = 2.2e-16)
```

Separately, `q_parameter.Q` is a **Python float** (`1.1099785827513808`, 17
digits) and `hecke_core_legacy.h` is a **float**. The intra-nucleon coefficients
`_PROTON_G1`/`_NEUTRON_G1` *are* full 50-dps `mpf`, but the **inter-nucleon `nn`
crossing** is appended as `(1.0, -h, ...)` with float `h`. So the chain straddles
two precision layers within a single product.

## Finding 5 — the `dim >= 8` numpy branch is slower than what it replaces

Its docstring claims *"Uses numpy for dim ≥ 8 (significant speedup for higher
Hecke levels)"*. `np.asarray` on `mpf` entries yields **dtype=object**, which has
no BLAS — it is a Python loop with numpy dispatch overhead on top:

| dim | numpy(object) | pure Python loop | verdict |
|---|---|---|---|
| 8 | 0.0012 s | 0.0012 s | wash |
| 16 | 0.0126 s | 0.0096 s | **numpy 31 % SLOWER** |
| 24 | 0.0380 s | 0.0316 s | numpy 20 % slower |
| 32 | 0.0736 s | 0.0748 s | wash |

float64 numpy at dim 32 is 7 µs — ~10,000× faster per scalar op, which is the
size of the prize if the arithmetic moves to a compiled MPFR kernel.

## Finding 6 — the approximation tier is dead

`unified_iterative_correction(Z, N, k_max=K_PARTITION_MAX, k_exact=K_PARTITION_MAX)`.
Since `active_gaussian = [e for e in table if k_exact < e['k'] <= k_max]` and both
default to 11, that list is **empty**. The Bozejko–Speicher q-Gaussian
approximation for high-k partitions is implemented and never runs. Measured:
`active_exact = 193`, `active_gaussian = 0`.

## Scaling law

- **Partition set is fixed**: 193 active partitions at `k ≤ 11`, dims 1…2310.
  It does *not* grow with A. Materialising it alone costs **37 s**.
- **Crossings grow as O(A²)**: `A(A−1)/2` inter-nucleon + ~6A intra.
- So cost ≈ `A² × Σ_λ f(dim_λ)`, with `f = dim³` today and `dim·nnz` after fix 1.

Relative to deuterium (13 crossings): ⁷Li ≈ 5×, ¹⁶O ≈ 17×, ⁵⁶Fe ≈ **144×**.

## Recommended order of work

1. **Fix the guard** (`if s['sparse']:`). One line, ~500× at dim 2310. Must be
   landed with a value-equality check against a case that completes both ways —
   pick a small partition subset via `k_exact`, do not use deuterium.
2. **Export `dense_dense_mul_mpfr` via PyO3** and route `_matmul_dim` and the COO
   accumulator through it. ≥24× measured, on top of (1). This is the change that
   makes higher isotopes reachable.
3. **Fix the precision straddle**: make `Q` and `h` `mpf` from
   `Q_50_DIGIT_STR`, and stop seeding accumulators with `np.eye` / `0.0`. This is
   a correctness fix and is independent of (1) and (2).
4. **Delete the `dim >= 8` numpy branch** — measured pessimization.
5. **Decide on the q-Gaussian tier**: either give `k_exact` a real default below
   `k_max`, or delete it. Right now it is untested dead code.

Only after 1–3 is regenerating `hadron-knot-table.witness.json` (`qou-i7ju`) worth
attempting; today the producer cannot finish its second atom.
