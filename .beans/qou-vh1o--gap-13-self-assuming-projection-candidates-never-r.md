---
# qou-vh1o
title: 'GAP: 13 self-assuming-projection candidates never reach the review ledger (derivation-pending exemption arms)'
status: todo
type: task
priority: high
created_at: 2026-09-13T19:43:07Z
updated_at: 2026-09-13T19:43:45Z
---

## The finding

`content/pipeline/lean-vacuity-axiom-audit.ts` seeds the agent-inspection review
ledger only from candidates whose `exempt_reason` matches
`LEDGER_TRACKED_EXEMPT = /triage pending/` (line ~1697; consumed at the seeding
site ~3576 and at the promotion site ~3411).

Two exemption arms emit the string **"canonical §3b placeholder projection
(tracked; derivation pending)"**. That does not match. So every candidate taking
those arms is dropped at the seeding site, never reaches an agent, and can never
be promoted back to a counted defect by a `genuine` verdict.

Measured on `origin/main` (full corpus, 3841 `.lean`): flipping the wording to
"triage pending" seeds **34** previously-invisible candidates. **21** of them are
`applied-field-projection` and are adjudicated in the PR that files this bean.
The **other 13 are this bean**, and they are pre-existing — they predate the
`applied-field-projection` pattern entirely:

- **`applied-tuple-projection` — 6**
  - `lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean:43` `acoustic_horizon_conditions`
  - `lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` `discrete_vortex_spectrum`
  - `lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` `root_of_unity_truncation`
  - `lifting-and-descent/ccg-crossed-module-structure.lean:35` `ccg_crossed_module_structure`
  - `mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:131` `qbeta_c_k_closed_forms_derived`
  - `mass-theory/crystal-basis-resolves-mass-tower-open-problems.lean:122` `crystal_basis_reduction`
- **`tuple-projection` reaching the arm as a `def` proof (`isDefProof && !nameGateMatched`) — 7**
  - `fluid-dynamics/acoustic-horizon-conditions.lean:98` `acoustic_horizon_regularity`
  - `fluid-dynamics/discrete-vortex-spectrum.lean:91` `discrete_vortex_spectrum`
  - `fluid-dynamics/root-of-unity-truncation.lean:73` `root_of_unity_truncation_conditional`
  - `fluid-dynamics/vorticity-lower-bound.lean:85` `vorticity_lower_bound_conditional`
  - `lifting-and-descent/ccg-cosimplicial-identities.lean:43` `ccg_cosimplicial_identities`
  - `mass-theory/q-beta-bar-even-kernel-typeclass.lean:123` `bar_even_kernel_implies_q_one_shadow`
  - `mass-theory/q-beta-q-eq-one-shadow-gate.lean:86` `qbeta_q_eq_one_shadow_anchors`

## Why it was left rather than absorbed

Each needs its own agent verdict (`genuine` / `legit` / `advisory`) — 13 more
file reads in a different domain (fluid dynamics, cosimplicial identities) from
the tranche that found it. Absorbing them would have tripled the PR and buried
the applied-field adjudication. AGENTS.md §"Small-moderate fixes for related
bugs ride on the active PR" — 13 adjudications is not small.

Two of the 7 `tuple-projection` entries have a **counterpart already in the
ledger** under a different declaration in the same file (e.g.
`q-beta-bar-even-kernel-typeclass.lean::bar_even_kernel_implies_direction_sanity`
is ledgered `genuine`), so the prior is that this group skews `genuine` too —
but that is a prior, not a verdict.

## What to do

1. Change the second arm's `exempt_reason` to "triage pending" (one string).
2. Run `--review-ledger` scoped to the 13 files (the scope guard added in #7332
   makes a scoped run non-destructive — verified: a 18-file run added 21 and
   removed 0).
3. Adjudicate the 13 per the rubric stated in the PR body.
4. `--check-ledger` must stay green.

## Related, NOT this bean

- **Scope leak in `seedProbeInhabitedCandidates`.** It ignores the scan scope,
  so a run scoped to 18 files reset a `proof-carrier-inhabited-by-probe` entry
  in a 19th file that was never scanned
  (`transfer-matrix-level-independence.lean::…CrystalGraphRealization`). Same
  class as the deletion-scope bug fixed in #7332, one seeder over. That entry
  was re-adjudicated in this PR rather than restored, because its file had
  genuinely changed (`70af9415e22d` → `b635d218c86a`, commit `8ea4e5479f`).
- **The committed ledger is stale by ~53 entries against a full-corpus run**:
  33 adjudications whose candidate no longer fires (spot-checked three — all
  genuinely repaired by `qou-9yt9` / `qou-ghy5`, so deletion is correct) and
  ~20 whose `.lean` changed since the verdict. `--check-ledger` reads green on
  `main` only because nobody has re-run `--review-ledger` whole-corpus. That is
  `qou-metc` item 3.
