# Co-Casimir compute bottleneck investigation

**Date:** 2026-05-19
**Trigger:** Repo-owner directive 2026-05-19 "investigate bottleneck in compute" (while ⁴He bg run was at 32+ min CPU per worker, ~26 min wall).

## Profile data

### Per-partition χ^λ cost at n=12 (⁴He, 47 crossings)

| λ | dim_λ | wall (60 dps) |
|---|---:|---:|
| [12] | 1 | 0.00 s |
| [6, 6] | 132 | 56.7 s |
| [5, 4] (n=9, ³He benchmark) | 42 | 1.79 s |
| [4, 4, 4] | 462 | (timed out at >120s) |

Scaling: cost ∝ dim_λ³ × n_crossings (matrix multiplication cubic in dim, applied per crossing).

For n=12 with the largest partitions (dim ~462 for [4,4,4] / [3,3,3,3]), expected wall is ~50-60× the dim=132 case = **30-60 min per partition**. With ~5 such large-dim partitions, total ⁴He compute is several hours sequential, ~30-90 min on 4-way parallel.

### Precision has NO impact on wall time

| dps | wall (n=9, λ=[5,4]) |
|---:|---:|
| 60 | 1.788 s |
| 30 | 1.800 s |
| 20 | 1.758 s |

The bottleneck is **Python object overhead in `mp.matrix` operations**, not the actual mpmath precision. mpmath's matrix multiplication loops in pure Python; each element op carries Python-call overhead independent of the underlying precision (until very high dps where the per-op mpf cost dominates).

## Bottleneck root cause

`hoefsmit_matrices_numeric` (in `rho_k_h3a_refinement.py`) returns `mp.matrix` instances. The matrix product `M = M * sigma` inside `chi_numeric` is `mp.matrix.__mul__`, which loops:

```python
# mpmath's matrix.__mul__ pseudocode
result = mp.matrix(rows_a, cols_b)
for i in range(rows_a):
    for j in range(cols_b):
        total = mpf(0)
        for k in range(cols_a):
            total += self[i, k] * other[k, j]   # ← Python attribute lookup + mpmath mul
        result[i, j] = total
return result
```

For dim=132 (n=12 [6,6]): 132³ = 2.3M element ops × 47 crossings = **108M mpmath element multiplications**, each carrying ~10-15 μs of Python overhead → 1000-1500 s sequential. Matches observed 57 s per partition (with multi-loop dispatch).

For dim=462: 462³ = 100M element ops × 47 crossings = **4.6 BILLION** element multiplications → tens of minutes per partition.

## Optimization candidates (ranked by effort:payoff)

| # | Approach | Effort | Estimated speedup |
|---|---|---|---|
| 1 | **Use `numpy` for matrix multiply, `mpmath` only at the trace** | 1-2 hours | 10-50× on large-dim partitions (numpy's C-level matmul vs Python loop) |
| 2 | **Drop precision to 30 dps** | minutes | NONE (this audit's finding) |
| 3 | **Skip negligible-contribution partitions** (Plancherel weight × dim_q⁻¹ < ε) | 1 hour | 30-50% (drops 1-2 large-dim partitions whose final contribution is < 1e-12) |
| 4 | **Rust `hecke-atomic` / `hecke-tr-m-wenzl-lr`** | days (convention adapter) | 100-1000× (no Python overhead) |
| 5 | **Custom C extension with mpmath types** | 1-2 weeks | 50-200× |

**Recommendation**: implement #1 (numpy-based matmul). The Hoefsmit matrix entries at q_0 are real floats; can use `numpy.float64` for the heavy lifting, then convert to `mpmath` only for the final trace sum (which IS precision-sensitive — `chi = Σ M_ii` over dim entries, each tiny, total can be order 1).

Risk: dropping to float64 loses precision in intermediates. But the FINAL χ^λ values are O(1) and the accumulated rounding from 132 or 462 matrix mults at f64 (16 digits) is bounded by dim · 10⁻¹⁶ ≈ 5×10⁻¹⁴ — well within the 50 dps witness output. Worth verifying empirically.

## Action items (next session)

1. Replace `mp.matrix` matrix products in `hoefsmit_matrices_numeric` + `chi_numeric` with `numpy.float64` operations; only convert to mp.mpf for the final trace.
2. Add a `--precision` flag so callers can opt into the slower mpmath path if needed (e.g. for n > 30 where rounding accumulates).
3. Validate the numpy path against the mpmath path on n=6, 9, 12 (current witness data).
4. If validation passes, rerun co-Casimir on ⁴He, ⁵Li, ⁶Li, ⁷Li, ⁸Be, ⁹Be, ¹⁰B. Expected 10-50× wall reduction = ⁴He in ~3-5 min instead of 30-60.

This is the path to extending substrate-derived co-Casimir to all-nucleotides scope.
