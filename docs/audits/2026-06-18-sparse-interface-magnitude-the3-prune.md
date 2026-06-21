# Sparse interface-operator magnitude — refuted parameter-free by the T/³He mirror ratio

**Date:** 2026-06-18
**Probe:** [`probe_sparse_interface_magnitude_the3_prune.py`](../../computations/probe_sparse_interface_magnitude_the3_prune.py)
→ `probe-sparse-interface-magnitude-the3-prune.witness.json`
**Status:** EXPLORATORY / formalize-first prune (per `production-vs-exploratory-discipline`); asserts the
refutation. Δ_λ magnitude remains an open gate (GAP-A-3).
**Discipline:** formalize-first — a sharp parameter-free test prunes a structural class *before* any fit.

## The hypothesis pruned (H_sparse)

The binding-magnitude gap
([`2026-05-26-delta-lambda-binding-formula-closure.md`](2026-05-26-delta-lambda-binding-formula-closure.md)):
the proved `Δ_λ = sgn(w₀^{S_λ'})·dim` has the right SIGN but wrong MAGNITUDE (−83% to −89% on D/T/³He/⁴He).
That doc's stated reason — *"the LP-dual concentrates binding on a SINGLE partition per atom with a per-knot Δ
value (not the uniform sgn×dim weight)"*, and the §"What is NOT yet first-principles" direction *"B(A) for A≥3
needs SDP + iterative knot building"* — is the **sparse interface-operator** hypothesis:

> **H_sparse.** `B(K) ≈ m_e · |y_{λ*}·χ^{λ*}(β_K)·Δ_{λ*}|` — binding dominated by one Wedderburn block `λ*(K)`.

## The parameter-free prune (T/³He mirror pair)

T (³H) and ³He share `n=9`, the same 30 partitions, and the same `y_λ`. **If** the dominant block is common to
the mirror pair (`λ*(T)=λ*(³He)`, the natural case), then `Δ_{λ*}` and `y_{λ*}` **cancel** in the binding ratio:

$$\frac{B_T}{B_{^3\mathrm{He}}} = \frac{|\chi^{\lambda^*}(\beta_T)|}{|\chi^{\lambda^*}(\beta_{^3\mathrm{He}})|}
  \;\overset{!}{=}\; \frac{8.4818}{7.7180} = 1.0990 .$$

A zero-parameter consequence: *some trace-dominant block must have character-ratio 1.0990.* Testing all 30 blocks:

| Finding | Value |
|---|---|
| Trace dominance — top block `[6,3]` share of Σ\|y·χ\| | **33.7%** (T), 31.9% (³He) — **not sparse** |
| Dominant block common to T & ³He? | **yes** (`[6,3]` both) ✓ |
| Dominant block `[6,3]` character-ratio `\|χ_T/χ_³He\|` | **0.633** → **MISS** (target 1.099) |
| Only block with ratio ≈ 1.099 | `[5,1,1,1,1]` (1.103), carrying **0.1%** of \|trace\| |

## Verdict — refuted

H_sparse in its only parameter-free form (common dominant block) is **refuted**:

1. **The trace is not sparse.** The top block carries 34%, not ~100%; binding is spread across ~4 blocks
   (`[6,3] 34%`, `[8,1] 20%`, `[7,2] 15%`, `[9] 8%`).
2. **The dominant block gives the wrong mirror ratio** (0.633 vs 1.099).
3. **The only block with the right ratio is trace-negligible** (`[5,1,1,1,1]`, 0.1%). Concentrating binding there
   needs a per-knot `Δ` ~10³× the others on a near-zero-weight block — an implausible fit, not a concentration.
4. **The escape is a fit.** Allowing different dominant blocks per atom (`λ*(T)≠λ*(³He)`) un-cancels `Δ` and `y`
   → two free parameters → gated (no 23rd ansatz).

## What survives — the redirect

The binding magnitude is **irreducibly multi-block**: it cannot be a single-partition concentration that also
respects the T/³He mirror. So the productive object is the *full-sum* `Σ_λ y_λ χ^λ Δ_λ` with a multi-block
magnitude rule — which returns to the open magnitude question (the sign is proved/icosahedral chirality, the
*spread* magnitude is open). This prune removes the "find the per-knot Δ on the LP-dominant block" sub-direction
from the live set; it does **not** refute SDP/iterative-knot-building per se, only its single-dominant-block
reading.

## Cross-references

- [`2026-05-26-delta-lambda-binding-formula-closure.md`](2026-05-26-delta-lambda-binding-formula-closure.md) — the magnitude gap + the LP-sparsity claim pruned here
- [`2026-06-18-pauli-young-delta-lambda-the3-refutation.md`](2026-06-18-pauli-young-delta-lambda-the3-refutation.md) — sibling T/³He refutation (non-negative symmetry projection)
- [`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md) — the proved sign = chirality (magnitude is the open part)
- [`docs/coordination/gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) — the GAP-A Path-B ledger
