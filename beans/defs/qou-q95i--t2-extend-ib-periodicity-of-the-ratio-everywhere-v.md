---
# qou-q95i
title: 'T2: extend i/b-periodicity of the ratio everywhere via the identity theorem (hibinv input)'
status: in-progress
pr: 8224
updated_at: 2026-11-22T22:50:00Z
type: task
priority: normal
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T18:22:29Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---

PARTIAL (2026-07-18): the identity-theorem-free CORE landed — QOU/Common/PeriodicDense.lean periodic_of_continuous_of_eqOn_dense (continuous r + c-periodic on a DENSE set ⇒ c-periodic everywhere), lean-direct exit 0. So hibinv-everywhere does NOT need the full identity theorem: the dual pole lattice is discrete ⇒ complement dense, and continuity + dense agreement suffices. Remaining two inputs, both separable: (i) the ratio is continuous (from the entireness endowment, qou-2cvs); (ii) the dual-lattice complement is dense (a discreteness fact about {e^{2πz'/b}=-1}). Wire into FaddeevRigidityReduction once (i) lands.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-18 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8224)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8224` at `9725d15463b70fb5b273b6c495db79723640032c`).
- **Lean Formalization**: `QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope.faddeev_dual_shift_ratio_invariance` (Dual shift ratio invariance Psi_shift / Phi_shift = Psi / Phi under common nonvanishing shift multiplier.)
- **80-dps Witness**: `computations/probes/faddeev-halves-selection-and-q-gevrey-cauchy-envelope.witness.json` (`scriptHash: cea527e5468d`, `scriptCommitSha: 9d85aecf9640ed04a9fa33fe94c3662500eae503`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8224 (`QOU/QBeta/FaddeevHalvesSelectionAndQGevreyCauchyEnvelope.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8224 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**APPLIES.** pure mathematics; no retired premise found (grep for photon/trefoil/convention C/census/muon pin/virtual photon: none); claim is hollow (vacuous brick PR, see note above), the open work stands.
