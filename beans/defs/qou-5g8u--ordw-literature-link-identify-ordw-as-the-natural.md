---
# qou-5g8u
title: 'ordw literature link: identify ordw as the NATURAL VALUATION of an ordered field (Rosenlicht / Aschenbrenner-van den Dries-van der Hoeven H-fields). Residue field = R => the growth CONSTANT is the residue the valuation discards, the growth RATE is the valuation. Formalize the val-vs-residue separation'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T02:26:45Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---

## Round 76 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8266 (`103b9c7f621cbb1d51b8b69b196c5e468a1ad112`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralTwoSidedLatticeAndValuationResidueBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/state_integral_two_sided_lattice_and_valuation_residue_brick_probe.py` (`scriptCommitSha: 10898ce23cb1e64bafb36d0437d31d88a2b0d683`) and `computations/probes/state-integral-two-sided-lattice-and-valuation-residue-brick.witness.json` (`allPassed: true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8266, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
