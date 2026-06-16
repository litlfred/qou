# A=3 operator-form wiring — end-to-end ³He verified at 50-dps + the SVD bottleneck (2026-06-16)

**Branch:** `claude/wenzl-a3-recursion-wiring-2026-06-16` (PR #2371)
**Owns:** the closure-b wiring step after the foundation merged (#2358 derivation,
#2365 A=3 correctness, #2366 categorical rename).
**Compute:** `computations/wenzl_a3_combiner_end_to_end.py`; env built `pyhecke_native`
0.9.0 + numpy/mpmath/sympy in-container.

## Result — the operator-form combiner reconstructs the physical ³He χ^λ at 50-dps

Plugging the **operator-form** categorical combiner
`gauge_aligned_A_combiner_general(λ, 6, 3, q₀, 50)` (the `V_ξ⊗V_ν` matrix — the
speedup form) into the branching reconstruction of the **real ³He atomic braid**
(split (6,3) at the pn-averaged interface `σ₅ − h/2`, which is exactly what the
combiner bakes in):

$$\chi^\lambda(\beta_{\text{in}}^{H_6}\,I_{pn}\,\beta_{\text{out}}^{H_3})
  = \sum_{\xi\vdash6,\nu\vdash3}\mathrm{Tr}\big[A^\lambda_{\xi\nu}(I_{pn})\,
    (\rho_\xi(\beta_{\text{in}})\otimes\rho_\nu(\beta_{\text{out}}))\big]$$

Verified against the true `χ^λ` (full atomic word in `V_λ`) for **9 of the 13
λ⊢9 with dim ≤ 28** — all at the 50-dps floor:

| λ ⊢ 9 | dim V_λ | `\|χ_comb − χ_true\|` | combiner wall |
|---|---|---|---|
| (9), (1⁹) | 1 | ~1e-50 | ~0 s |
| (8,1), (2,1⁷) | 8 | ~5e-49 / 7e-50 | ~3.8 s |
| (7,2), (2,2,1⁵) | 27 | ~1e-48 / 2e-50 | ~325–355 s |
| (7,1,1), (3,1⁶) | 28 | ~7e-49 / 2e-50 | ~450–472 s |
| (5,4) | 42 | ~1e-48 | **8509 s** |

All **✓ at < 1e-25** (residuals 1e-48 → 1e-50). This extends the sibling's H_9
universality demo (abstract panel words, λ∈{(9),(8,1)}) to the **physical ³He
atomic words** across the feasible λ — confirming the operator-form path is exact
at production precision, not just on toy inputs.

## The bottleneck (profiled) — O(r⁶) pure-mpmath null-space SVD

The combiner wall time explodes super-polynomially with `dim V_λ`:

- flat to dim ≈ 28 (≤ 8 min/λ),
- **dim-42 `(5,4)` = 8509 s ≈ 2.4 h** for a single λ,
- single-threaded, pegged at 99.9 % CPU.

The cost is **`gauge_aligned_A_combiner_general`'s per-(μ,ν)-block intertwiner
solve**: the mpmath `_nullspace` SVD plus the `r×r` inverse `U⁻¹·Itil·U`, with
`r = c·d_μ·d_ν` the range-block dimension. This is ≈ **O(r⁶)** in pure mpmath at
50 dps. It is exactly the cost the closure-b author flagged when deferring the
full p(9)=30 sweep to the Rust kernel — now **quantified**: the remaining λ⊢9
(`(6,3)=48`, the other dim-42 partitions, …) would each take hours, so a full
50-dps Python sweep is infeasible (the math is correct; the linear algebra is the
wall).

## Status of the wiring

- **Correctness at A=3:** doubly confirmed — #2365 (JM-projector identity, all 30
  λ, f64, 1e-12) and now the operator-form combiner (9 λ, 50-dps, ~1e-49).
- **`DIM_CAP=28`** set in the script as the Python-feasible frontier (so it runs as
  a demonstrator in minutes, not hours).
- **`tr_M(³He)` full assembly** needs all 30 λ → blocked on the dim ≥ 42 SVDs →
  **Rust-kernel follow-up** (port the per-block null-space + inverse to
  `hecke-engine`/`pyhecke-native`, where the O(r⁶) is tractable). This is the
  natural next compute task.
- **Recursion edit** (`canonical_tr_m_via_branching.py:263` `return None` →
  consume the combiner; tritium needs the linear-in-interface generalization
  `A(σ−h)` from the same gauge `U`) follows once the Rust combiner makes the full
  per-level extracts cheap.

## Discipline

No production value changed (tr_M is already validated via the fine-Bratteli
transfer — this verifies the faster operator-form *route*). Not wired into the
canonical chain; no fit; no 4th calibration. 50-dps floor (compute-author §1);
long-compute progress logging added per §4.4 (PR #2371 Gemini review).
