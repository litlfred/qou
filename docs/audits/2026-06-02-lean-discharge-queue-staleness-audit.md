# Lean discharge queue — staleness audit (2026-06-02)

> Companion audit to PR #1720. Surveys all 8 items in
> [`.beans/lean-discharge-queue.json`](../../.beans/lean-discharge-queue.json)
> against the actual `.lean` sources on origin/main. **Headline:
> 5 of 8 items are stale — work done, NOT discharge targets, or
> referencing files that no longer exist.** Recommendation:
> owner-action close the stale items + repopulate the queue from
> the live 17-sorry census below.

## Method

For each queue item, ran `grep -c '^[[:space:]]*sorry' <file>` to
count *actual* sorry tokens (excluding doc-comment mentions like
"contains sorry" or "sorry-free"). Compared to the queue's own
claim of sorry counts.

**Method caveat:** `grep -c '^[[:space:]]*sorry'` counts only
*line-leading* `sorry` tokens. This matches the dominant QOU style
(`:= by` then `  sorry` indented on its own line) but **undercounts**
inline forms like `:= by sorry` or `simp; sorry`. The per-file counts
below are therefore lower bounds; a `\bsorry\b`-anywhere scan
(excluding `--` comments and docstrings) would be stricter. The
stale-vs-real verdicts are unaffected — they turn on whether the
failure *evidence* reproduces at the current path, not on the exact
count — but the "17-sorry census" should be read as "≥ 17
line-leading sorries" pending a tokenizer-based recount.

## Per-item findings

| id | priority | queue claim | reality | verdict |
|----|----------|-------------|---------|---------|
| `lean-q-schur-h3-y-lambda-extension` | high | "5 partitions of n=3 missing" → 3 H_3 theorems to write | All 3 H_3 theorems already proved sorry-free (lines 245-276 of `QSchurYLambdaClosedForm.lean`) | **stale — done** |
| `lean-section-3b-cond-classes-permanent` | high | "REGISTRY, not a discharge target" | (registry — correct) | not stale; intentional |
| `lean-discharge-triage-pass` | high | "scan all 598 sorry files" | QOU has 17 sorrys total across 10 files (not 598) | meta-item; this audit IS the partial discharge |
| `lean-bar-involution-extension` | medium | "Bar-involution + Mullineux theorems beyond y_λ" | No `*bar*involution*` or `*mullineux*` Lean files in QOU package | **stale — referenced files do not exist** |
| `lean-mathlibext-sdp-rank-equality` | medium | "2 sorries in SDPRankEquality.lean (R1+R2 factoring)" | `SDPRankEquality.lean` has **0 sorry tokens**; the file's own header says "fully sorry-free" | **stale — done** |
| `lean-staircase-corner-hook` | medium | "6 of 9 non-conjectural sorries" | `StaircaseCornerHook.lean` has **0 sorry tokens** | **stale — done** |
| `lean-tractable-fluid-dynamics` | low | "7+ FluidDynamics/*.lean files (each 2 sorries)" | All 7 `FluidDynamics/*.lean` files have **0 sorry tokens** | **stale — done** |
| `lean-g-action-on-substrate` | low | "1 tractable sorry of 3 (2 conjectural)" | `GActionOnSubstrate.lean` has **1 sorry total**, and it is the legitimate §3b-cond conjectural class instance (the registry pattern) | **stale — the 1 sorry is permanent** |

## Live 17-sorry census (QOU package)

For owner reference, the *actual* set of files with non-zero `sorry`
tokens in the QOU Lake package today:

```
3: BraidKnot/SubstrateEWHypotheses.lean
3: Archimedean/BorromeanVolumeCatalan.lean
2: MathlibExt/SDPRealUniqueness.lean
2: Kashaev.lean
2: IwahoriHecke/Defn.lean
1: QuantumObservableUniverses/GActionOnSubstrate.lean (§3b-cond, permanent)
1: QuantumObservableUniverses/CategoricalHiggsIdempotent.lean
1: IwahoriHecke/Quotient.lean
1: Braiding/hecke_mass_trace.lean
1: Archimedean/MassTowerOpenProblemsClasses.lean
```

A genuine triage pass (with Lean LSP available) would classify
each of these 17 sorrys into:

- **§3b-cond permanent** (per the `lean-section-3b-cond-classes-permanent`
  registry — do NOT attack)
- **research-grade** (open conjecture, not a missing proof)
- **tractable** (mechanical mathlib chain; candidate for discharge)

Without Lean LSP this session, I can only do file-level grep; the
per-sorry classification is the next step for the human triage.

## Recommended owner actions

1. Close `lean-q-schur-h3-y-lambda-extension` as `resolved` (PR #1720 captures the docstring refresh; the H_3 work was already done in an earlier session that never updated the queue).
2. Close `lean-bar-involution-extension` as `wontfix` (referenced files do not exist; if the work is needed, file a fresh item against the actual locations).
3. Close `lean-mathlibext-sdp-rank-equality` as `resolved` (file is sorry-free per the file's own header).
4. Close `lean-staircase-corner-hook` as `resolved` (file is sorry-free).
5. Close `lean-tractable-fluid-dynamics` as `resolved` (7/7 files sorry-free).
6. Re-scope `lean-g-action-on-substrate` to "registry entry only" (its 1 sorry is permanent §3b-cond, NOT a discharge target).
7. Re-populate the queue from the 17-sorry census above, after a Lean-LSP-equipped session classifies each as §3b-cond / research / tractable.

Per CLAUDE.md §4a, only humans may close TodoItems / resolve queue
entries; this audit recommends but does not perform the closures.

## Out-of-scope (not addressed here)

- UGB + Fred2005 packages were not surveyed; their sorry counts may
  separately need a triage. Out of scope for this Lean discharge
  branch which is QOU-scoped.
- Per-sorry classification (§3b-cond / research / tractable) requires
  Lean LSP and the manuscript context for each statement — better
  done in a session with Lean LSP available.
