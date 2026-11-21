---
# qou-5mxd
title: Port far-commutativity ([A_a,A_b]=0 for |a-b|>=2) from the sparse He4 Magnus probe to the dense deuteron/triton probes
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:07:55Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

## VERIFIED 2026-09-08: triton 14/14, the maximal overlap

unpatched 14, patched 19, overlapping 14 (max possible 14) -> ALL IDENTICAL on
dim / y_lambda / tr_rho_Omega2 / tr_Omega2_ctrl. Control (perturbed row) caught,
so the comparison is live. 5 further patched partitions have no baseline.
Still unmeasured: any speedup at H9 (none found at H6), and the 30/30 witness.

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8269, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). No superseded premise for the port itself (far-commutativity is a property of the Magnus generators, basis-independent). The 14/14 verification was on the closed batch PR #8269 and never landed. Not redone this pass.
