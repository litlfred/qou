> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# SDP H_5+ status — post-#444 bug resolution

**Status**: H_5 algorithmic bug **resolved** (was our svec encoding
error, not Clarabel-rs). Subsequent scaling blocked by memory at
H_10+.

## Per-#444 status (closed bug)

PR #444 merged the diagnostic + early-abort. The "Clarabel-rs H_5
bug at PSD-cone dim ≥ 4" was post-mortem-attributed to **our own
svec encoding error** in
[`tools/hecke-engine/R5_5_BUG_REPORT.md`](../../tools/hecke-engine/R5_5_BUG_REPORT.md):

- Code packed lower-triangular column-major; Clarabel's
  `PSDTriangleConeT(n)` expects upper-triangular column-major
  with `√2` off-diagonal scaling.
- For symmetric matrices the conventions coincide at d ∈ {2, 3} and
  for the identity at d = 5 specifically — masking the bug in
  existing tests.
- At d ≥ 4 the orderings diverge: `svec(I_4) = [1,0,0,0,1,0,0,1,0,1]`
  was interpreted by Clarabel as a different (indefinite) matrix.
- **Fix**: write svec entries at positions `k(k+3)/2` (upper-tri
  column-major), not `k(k+1)/2 + k` (lower-tri). After fix the
  minimal reproducer returns c = 1 for d ∈ {2, …, 8}.

## Current state (verified 2026-04-29)

| n | filtration cutoff L | n_vars | max d_λ | monolithic SDP |
|---:|---:|---:|---:|---|
| 3 | any | ~5 | 2 | works, sub-ms |
| 4 | any | ~10 | 3 | works, ms |
| 5 | 2 | ~15 | 5 | **works** post-fix |
| 8 | 2 | ~30 | 14 | **works**, ~10s |
| 10 | 2 | ~50 | 42 | OOM |
| 18 | 8 | ~10⁵ | 4862 | infeasible (single machine) |

## Outstanding scaling work

R5.6 (Wedderburn-block decomposition) is the next algorithmic
level required to break the H_10+ memory wall. Per
[`tools/hecke-engine/R5_6_DECOMPOSITION_PLAN.md`](../../tools/hecke-engine/R5_6_DECOMPOSITION_PLAN.md):

- **Design**: documented (split monolithic SDP into per-Wedderburn-block
  SDPs sharing variable set; sequential intersection via fixed-c
  anchors at the end).
- **Strategy A implementation**: `tools/hecke-engine/src/sdp_per_block.rs`
  + `tools/hecke-engine/src/bin/r5_6_smoke.rs` landed in this PR.
  Public API `solve_per_block(n, q, anchors, cutoff)` is a drop-in
  replacement for `solve_canonical_t_w` with the same `SolverReport`
  shape.
- **Smoke test results**: H_3 / H_4 (full + filtration cutoffs)
  agree with monolithic solver to ≤ 3e-9 absolute on every recovered
  `c_w` and ≤ 3e-8 on `‖c‖_1`. 107/107 lib tests pass under
  `cargo test --features clarabel-sdp`.
- **Strategy A caveat**: sequential intersection is JOINT FEASIBLE
  but not necessarily JOINT ‖c‖_1-OPTIMAL.  Larger `n` may require
  Strategy B (ADMM consensus iteration) — that's R5.7.
- **Production target (R5.7, separate session)**: ⁶Li at H_18 with
  filtration cutoff L = 8 + AME anchor.

## Family-4 atoms (⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F)

These need T_w from H_18+ SDP search; blocked on R5.6 + R5.7.

| atom | Z | N | A | n = 3A | required H_n |
|---|---:|---:|---:|---:|---:|
| ⁶Li | 3 | 3 | 6 | 18 | H_18 |
| ⁷Li | 3 | 4 | 7 | 21 | H_21 |
| ⁹Be | 4 | 5 | 9 | 27 | H_27 |
| ¹¹B | 5 | 6 | 11 | 33 | H_33 |
| ¹⁴N | 7 | 7 | 14 | 42 | H_42 |
| ¹⁹F | 9 | 10 | 19 | 57 | H_57 |

Without GB-NF derivation of T_w, these atoms continue to use the
volume-match knot id heuristic for B-prediction (Family-3 tier in
the canonical predictor). Per the unified per-3A predictor, this
gives ⁶Li to within −0.08% — but the knot id is hyp:census-assigned
rather than algebraically derived.

## Bottom line — answers user's question "is there still an error?"

**No.** The H_5 bug is fixed; H_8 monolithic SDP works in ~10s.
What remains is **scaling to H_10+**, which is a separate
algorithmic problem (R5.6 Wedderburn decomp), not a bug.
