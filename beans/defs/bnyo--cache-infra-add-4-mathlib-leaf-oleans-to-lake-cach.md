---
# bnyo
title: 'Cache infra: add 4 Mathlib leaf oleans to lake-cache cone (5 cache-artifact files genuinely use them)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-27T13:09:47Z
updated_at: 2026-11-21T15:20:54Z
parent: qou-5vkl
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

## Update (2026-06-28) — scope reduced to 2 leaves

- **`Quaternion` leaf MOOTED.** `QuaternionFromHecke` (PR #2927, merged) had a
  *dead* `import Mathlib.Algebra.Quaternion` (the only non-comment "Quaternion"
  mentions were its own title + class name). Dropping it red-drained the file to
  green AND removed its cache-artifact dependency — so the `Quaternion` leaf is
  no longer needed by anything.
- **`Trigonometric.Complex` (1 olean)** — built + proven this session; the 2
  dependents (`ScratchZeta5`, `zeta5_residue_monodromy`) are pure cache-artifacts
  that go green with just this leaf.
- **`Log.Summable` (30) + `RiemannZeta` (140) CONFIRMED genuinely needed** —
  verified empirically: `PhiQConvergence` uses `Summable`/`Multipliable`
  (L186-215), `ClassicalRiemannHypothesis` uses `riemannZeta` (L38, faithful §3b
  conjecture class). NOT dead imports. Their dependents stay deferred.

**Net remaining bnyo:** fold `Trigonometric.Complex` (+ optionally `Log.Summable`,
`RiemannZeta`) into the next full cache refresh. Still recommend NOT a piecemeal
852 MB reseed. Sandbox-DX only.

## Update (2026-06-29) — `Data.Complex.Exponential` is the high-value leaf (swarm session)

The orphan-drain swarm session confirmed the single highest-value cache leaf:

- **`Mathlib.Data.Complex.Exponential` (1 missing olean; all 1206 deps already
  in the restored `lake-cache/qou-v4-24-0` cone).** Building it (seconds, no CDN)
  flipped **86 of 92** non-active-chapter content-sibling orphans from
  neutral-skip (un-cached `Complex.exp`/`Real.pi`/trig) to **0 missing oleans /
  cache-verifiable**. `Complex.Circle` + `Trigonometric.Basic` oleans are already
  fully present (0 missing) — only `Exponential` was the gap.
- **Egress reality (2026-06-29):** github.com clone egress is OPEN (bypass the
  qou-scoped relay with `GIT_CONFIG_GLOBAL=/dev/null` + `--cacert /root/.ccr/ca-bundle.crt`),
  but the olean CDN `lakecache.blob.core.windows.net` AND `mathlib4.lean-cache.cloud`
  are egress-BLOCKED (403); the R2 origin returns 400 (reachable, needs auth). So
  `lake exe cache get` cannot pull prebuilt oleans — but a per-leaf source build
  works because the deps are cached.
- **Proven 1-command build** (needs a mathlib source clone at the pinned rev
  `f897ebcf` in `../mathlib4` + `elan override set lean-v4.24.0` there):
  ```
  LP=$(bash -c 'source scripts/lib/lean-env.sh; lean_leanpath')
  CONE=.lake/packages/mathlib/.lake/build/lib/lean
  env LEAN_PATH="$LP" lean --root=../mathlib4 \
    -o "$CONE/Mathlib/Data/Complex/Exponential.olean" \
    ../mathlib4/Mathlib/Data/Complex/Exponential.lean
  ```
- **Recommendation unchanged:** prioritise `Exponential` (above `Trigonometric.Complex`)
  for the next full cache refresh; still NOT a piecemeal 852 MB reseed.

## Update (2026-06-30, PR #3167 finding) — add NormCast + Omega to the refresh leaf-set

The orphan-drain PR #3167 surfaced two MORE missing-from-cone leaves while
addressing a Gemini import-narrowing review:

- **`Mathlib.Tactic.NormCast`** — needed by `polynomial-bar-involution` if it
  narrows off the `Mathlib.Tactic` umbrella (uses `push_cast`).
- **`Mathlib.Tactic.Omega`** — needed by `predicted-spectra/hadron-q-self-correction`
  if narrowed (uses `omega`).

Both leaf oleans are absent from the restored `lake-cache/qou-v4-24-0` cone
(the umbrella `Mathlib/Tactic.olean` IS present, but these leaves are not
separately resolvable). Consequence: narrowing those two files from
`import Mathlib.Tactic` to the specific tactics turned a fully-compiled
`pass` into an unverifiable `neutral-skip` — so PR #3167 KEPT the umbrella
import there (coverage > import hygiene for orphan siblings outside the
lake build). Fold `Tactic.NormCast` + `Tactic.Omega` into the same next
full cache refresh as `Data.Complex.Exponential` / `Trigonometric.Complex`
so future narrowings stay fully verifiable. Still NOT a piecemeal reseed.

## Folded into the base by the 2026-07-02 reseed

The 2026-07-02 reseed of `lake-cache/qou-v4-24-0` (859 QOU / 19 UGB / 1 Fred2005 /
2962 mathlib oleans, restore-checked) packed `.lake/packages/mathlib/.lake/build`
AFTER restoring the repthy-wedderburn addon — so the 11 addon oleans are now IN the
base branch (mathlib count 2962 = 2951 + 11, verified in the restore-check). The
separate `lake-cache/qou-v4-24-0-repthy-wedderburn` addon branch is redundant for
restores from this seed onward (kept per the never-delete-branches directive).
Skill note updated. Bean goal achieved; closing is the owner's call.

- **Round 94 PR (`litlfred/qou#8500`)**: Formalized `LeafOleanConeBatchingLedger`, `canonicalLeafOleanConeBatchingLedger`, `leaf_cone_parallelogram_identity`, `leaf_cone_discrepancy_sq_nonneg`, and `leaf_cone_positive_leverage_and_recovery` in `QOU.Foundations.LeafOleanConeBatchingDeferredStructuralCleanupSiblingVerificationClassificationFamilyChainErrorPartitionSubstrateProbeCancelHotspot` with 80-dps witness (`HEAD = 37841388326f8fad43c7ffaa9f1c59e901153736`, `scriptCommitSha = 79b2648932653702ea6a8cbefa5ff6493ff25e46`, `scriptHash = 310095425a857ae1cba47494cdbd7491b7846f82f292c4df8b8288ba0a130fe0`).

2026-11-21 (lean-build-red drain, issue #8817): closed. Body says goal achieved: the 2026-07-02 reseed folded the leaf oleans into the base branch. Gap addon fe9ce69 adds 66 more.
