---
# qou-0a8e
title: 'Formalize-first: state the structural invariant (q-diff eqn or its absence) + Lean if found'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-13T10:01:08Z
updated_at: 2026-11-17T07:56:00Z
parent: b9cj
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 76 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8266 (`103b9c7f621cbb1d51b8b69b196c5e468a1ad112`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralTwoSidedLatticeAndValuationResidueBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/state_integral_two_sided_lattice_and_valuation_residue_brick_probe.py` (`scriptCommitSha: 10898ce23cb1e64bafb36d0437d31d88a2b0d683`) and `computations/probes/state-integral-two-sided-lattice-and-valuation-residue-brick.witness.json` (`allPassed: true`).

