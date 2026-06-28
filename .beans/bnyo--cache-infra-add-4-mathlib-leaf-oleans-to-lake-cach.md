---
# bnyo
title: 'Cache infra: add 4 Mathlib leaf oleans to lake-cache cone (5 cache-artifact files genuinely use them)'
status: todo
type: task
created_at: 2026-06-27T13:09:47Z
updated_at: 2026-06-27T13:09:47Z
---

## Analysis (2026-06-28) — uneven cost; recommend BATCHING, not piecemeal reseed

Missing-olean closure of each leaf (computed against codeload source at the
pinned rev vs the restored `lake-cache/qou-v4-24-0` cone):

| Leaf | missing oleans | dependent file | status |
|---|---|---|---|
| `Analysis.SpecialFunctions.Trigonometric.Complex` | **1** | ScratchZeta5, zeta5_residue_monodromy | **built ✓ → both files lean-direct GREEN** (pure cache-artifacts) |
| `Algebra.Quaternion` | **1** | QuaternionFromHecke | built ✓ BUT file has its OWN reds (reserved-`λ` + parse) → leaf-build insufficient; needs a SkewSYT-style λ-repair (cross-ref bean 5wld) |
| `Analysis.SpecialFunctions.Log.Summable` | **30** | PhiQConvergence | deferred (moderate build; file may also have own reds) |
| `NumberTheory.LSeries.RiemannZeta` | **140** | ClassicalRiemannHypothesis | deferred (heavy NT cone; not worth a from-source build for 1 CI-green file) |

Build method PROVEN: `lean --root=<codeload-src> -o <cache>/<Mod>.olean <src>`
with `LEAN_PATH` = cached oleans. The source-rev-vs-olean-rev mismatch does
NOT bite for the 1-olean leaves (their deps are cached + interface-compatible).

**Recommendation:** do NOT do a piecemeal 852 MB cache re-push to persist 2
small oleans (disproportionate bandwidth/risk on load-bearing infra). Fold
`Trigonometric.Complex` + `Quaternion` (+ optionally `Log.Summable`) into the
**next full cache refresh** (the `lake-cache-refresh.yml` workflow, or a reseed
batched with other improvements). RiemannZeta (140) stays out-of-scope.
Net correctness value is low regardless — all 5 files are green in CI; this is
sandbox-DX only. QuaternionFromHecke's own λ-reds are the only real bug here
(handle under red-drain, not cache infra).
