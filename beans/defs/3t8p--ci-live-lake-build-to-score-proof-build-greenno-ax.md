---
# 3t8p
title: CI live lake build to score proof-build-green/no-axiom-growth/lean-compiles
status: completed
type: task
priority: normal
tags:
    - lightning-followup
    - reorg-2026-10-04
created_at: 2026-07-06T04:11:12Z
updated_at: 2026-11-21T22:41:42Z
parent: qou-5vkl
---

3 CI-only Lean criteria n/a on path (214/118/191). Need proof-objects.json+axiom-report.txt from full lake build. Run in lean_ci.yml.


## Update 2026-07-06
Local `lake build QOU` FAILS on `proofwidgets/widgetJsAll` (JS-widget target needs npm/node, absent in sandbox) even with github egress + `cache get`. Genuinely CI-only: run in lean_ci.yml (has node) to produce proof-objects.json + axiom-report.txt for proof-build-green / proof-no-axiom-growth.

## 🛑 Correction 2026-09-27 — the remedy in this bean is INERT, and the artefact it asks for is already here

**`proof-objects.json` is present in this repo** — 114 311 bytes, dated Sep 4 —
and `proof-build-green` is still **1037 of 1037 `n/a`**. The artefact whose
absence this bean blames exists and is ignored.

The reason is that two of the three checkers perform **no file access at all**.
`cat-harness/content/pipeline/qa-checkers-extended.ts`, at the live pin
`37a36ce`:

```ts
export function checkProofNoAxiomGrowth(_leanPath: string | undefined): CheckerResult {
  return { result: "n/a", hits: [] };            // :2783 — no comment, no TODO
}
export function checkProofBuildGreen(_leanPath: string | undefined): CheckerResult {
  return { result: "n/a", hits: [] };            // :2789 — likewise
}
```

Single parameter, underscore-prefixed, unread; one statement. **No
`proof-objects.json`, no `axiom-report.txt`, no `lake build` output can change
their verdict** — so running `lean_ci.yml` to produce those files, which is this
bean's entire remedy, would not move one verdict. That is now demonstrated
rather than argued: the input is on disk and the output did not change.

### The 2026-07-06 update's investigation was sound and was about the wrong thing

Establishing that a local `lake build QOU` dies on `proofwidgets/widgetJsAll`
(npm/node absent) is a real measurement, and it is not why these criteria are
`n/a`. It explains an obstacle on a path that does not lead here.

### And ONE of the three is genuinely artefact-driven — this bean treats all three alike

`proof-lean-compiles` reads `docs/audits/lean-compile-diagnostics.json`
(per the comment at `:2795`) and reports **131 pass / 1078 n/a** on this corpus.
It works exactly as this bean imagines the other two do. So the three split
1 real + 2 stubs, and the shared cause does not exist.

Re-measured entry counts, versus the `214/118/191` recorded above:

| criterion | this bean | measured 2026-09-27 | real? |
|---|---:|---:|---|
| `proof-build-green` | 214 | 1035 | **stub** |
| `proof-no-axiom-growth` | 118 | 752 | **stub** |
| `proof-lean-compiles` | 191 | 1209 (131 pass) | **yes** |

### Status — stays `todo`, with the remedy replaced

The criteria are still unscored, so nothing here is closed. What changes is
where the work lives: **implement or retire the two checkers upstream in
`folio-assistant`**, not spend a CI run in `lean_ci.yml`. Note also that qou CI
auto-triggers are disabled repo-wide (owner directive 2026-06-30), so the
`lean_ci.yml` route would need a manual dispatch to fail at.

Full measurement, the two further stub checkers found the same way
(`detangler-no-xchapter-fwd`, `detangler-archimedean-wall`), and the knock-on
into `ab_methodology_metrics` M5: bean `qou-306p`.

- **Round 93 PR (`litlfred/qou#8497`)**: Formalized `InertCheckerVerdictLedger`, `canonicalInertCheckerVerdictLedger`, `inert_checker_quadratic_balance`, `inert_checker_imbalance_sq_nonneg`, and `inert_checker_active_and_evaluated_recovery` in `QOU.Foundations.InertCheckerVerdictAuditPerPartitionAtomWordGateNoFitChiralitySeparationNormalFormHypothesisBridgeSeventySevenPartitionCompletion` with 80-dps witness (`HEAD = 25e6a2cd52af041cf68fa20d385161f4542be774`, `scriptCommitSha = b25d0e225db433dedb54ef57a788c05ae89960c1`, `scriptHash = 8abb07ac1693146e31fad47a5cfd80a80064de9f2fffcba92912d9ae413ecf74`).

## 2026-11-21 — owner chose RETIRE (issue litlfred/qou#8914)

The two stubs now live in folio-assistant-sci `pipeline/qa-checkers-extended.ts`. Retired in litlfred/folio-assistant-sci#211 (functions, dispatch entries, qa-checkers JSONs, test, skill docs) and litlfred/cat-harness-tools#2484 (registry entries). Tests in a mounted platform: sci 301/0, registry + sci 426/0. `proof-lean-compiles` stays; axiom status is `scripts/lean-axiom-guard.py`. Out of scope: the two detangler stubs (bean qou-306p).

Complete after: both PRs merge, the folio-assistant lock is bumped, and qou's `.folio-assistant-pin` moves past it.

## 2026-11-21T22:41:42Z — completed

Both stub checkers retired and the pins moved, owner go-ahead at each step (2026-11-21): folio-assistant-sci#211 and cat-harness-tools#2484 merged; folio-assistant#3189 re-pinned them in the index (main ba3914bec); qou#8970 moved qou's pin there. run-validate on the same corpus: 120 -> 166 issues (+46 warn-only defterm-forward-ref; two broken cross-paper uses fixed in #8970). The detangler stubs remain out of scope (qou-306p).
