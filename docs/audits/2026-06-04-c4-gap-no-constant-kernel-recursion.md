# c_4 structural-vs-fitted gap CANNOT be closed by any constant-kernel recursion

**Date:** 2026-06-04
**Branch:** `claude/qbeta-c8-c10-pell-lucas-closed-forms-2026-06-04`
**Probe:** [`computations/probes/qbeta_constant_kernel_depth_test.py`](../../computations/probes/qbeta_constant_kernel_depth_test.py)
**Status:** EXPLORATORY. Decisive negative result.

## Question

User 2026-06-04: *"specifically the c_4 structural-vs-fitted gap — can't we use the recursive formula?"*

## Setup

I derived `c_{k+2} = b² · c_k` for k ≥ 6 (PR #1793). This is the depth-2 constant-kernel instance of the on-`main` `QOU.QBeta.CKRecursion ℝ` scaffold. The question: can this (or any constant-kernel) recursion be extended back through c_4, c_5 to give a unified derivation from c_2 / c_3 to all c_k?

## Test

**Test 1: Does `c_{k+2} = b² · c_k` hold for ALL k?**

| k | c_k | b²·c_{k-2} | match |
|---|---|---|---|
| 4 | −1.133 | −0.753 | ✗ |
| 5 | −1.253 | −1.505 | ✗ |
| 6 | 3.011 | −0.853 | ✗ |
| 7 | −8.000 | −0.943 | ✗ |
| 8 | 2.266 | 2.266 | **✓** |
| 9 | −6.022 | −6.022 | **✓** |
| 10 | 1.706 | 1.706 | **✓** |

**Conclusion 1:** the recursion only holds for k ≥ 8 (i.e. once the pure-σ-action regime sets in). It FAILS at c_4→c_6, c_5→c_7, etc.

**Test 2: Does a depth-3 constant-kernel recursion `c_{k+1} = α·c_k + β·c_{k-1} + γ·c_{k-2}` fitted to c_5, c_6, c_7 predict c_8, c_9, c_10?**

Solving for the kernel:
```
α = −2.167, β = +2.690, γ = −1.672
```

Predictions vs closed forms:
| k | predicted | actual | rel err |
|---|---|---|---|
| 8 | 27.53 | 2.266 | **+1114.85 %** |
| 9 | −31.47 | −6.022 | **+422.59 %** |
| 10 | 32.52 | 1.706 | **+1806.67 %** |

**Conclusion 2:** depth-3 constant-kernel FAILS catastrophically. The lower rungs (c_4..c_7) and the σ-action tower (c_6..) are governed by **different structural patterns**.

## Result

**The c_4 structural-vs-fitted gap CANNOT be closed by any constant-kernel recursion** at depths ≤ 3, even using the silver-exact closed-form values. The c_4 closed form (`c_4 = c_3 · b⁴ = −2·b⁴`) and the σ-action tower (`c_{k+2} = b² · c_k` for k ≥ 6) are **structurally separate categorical objects**.

This matches PR #1786's empirical refutation of constant-kernel through depth 4 at q₀ — but extends it: the refutation holds *even at the structural (closed-form) level*, not just at the SDP-extracted q₀-noise level.

## What this means

The framework's Q_β-prediction error (3.27 % at the closed-form level, 1279 ppb on the L2 scoreboard at the CODATA-fitted level) is dominated by **c_2..c_4 mismatch**, and there is no constant-kernel-recursion route to fix it. Closing the gap requires either:

1. A **k-dependent kernel** (depth-d, kernel : Fin d → R but each `kernel j` depends on k) — what `CKRecursion R` allows in principle, but no instantiation has yet matched all c_k.
2. A **separate categorical derivation** of c_4 (specifically: of why c_3 · b⁴ is the right structural form and *why this value matches CODATA to 3 % but not better*).
3. **Acceptance** of the 3.3 % derivation-only floor with an honest "Q_β CAL-3-anchored" framing (which is what PR #1770 already did).

Net: the recursion is real and Lean-proved at silver (this branch), but it does not unlock the c_4 gap.
