---
# qou-2row
title: 'HARD THREAD: derive ρ_F(⁴He)≈1.889 from the two-row Frobenius stratum (item 2 surviving route)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T16:25:00Z
updated_at: 2026-10-04T15:13:05Z
parent: qou-v2om
---

Follows item 2 (`he4_rho_F_cpt_mechanism_refuted.py`, PR #5389): the CPT alt-block-doubling
mechanism for ρ_F(⁴He)=2 is REFUTED under the canonical convention (alt block [1¹²] has y=0; exact
two-row dominance). So any ρ_F derivation must live inside the two-row stratum — the ONLY blocks with
nonzero colour-weighted Frobenius mass. Canonical ⁴He H₁₂ weights (chi-helium-4-h12-at-q0-50dps):

  [12]=0.003966  [11,1]=0.003100  [10,2]=0.002370  [9,3]=0.001744
  [8,4]=0.001194  [7,5]=0.000696  [6,6]=0.000229

Target: ρ_F = B_AME/(m_e·A·8G) = 1.889 (integer 2 overshoots +5.9%, [2]_q +6.4%). QUESTION: does a
FIT-FREE combination of the two-row weights (a ratio, a stratum sum normalised by [12], a
winning-block Frobenius selection, or the SW-3-root saturation value) reproduce 1.889? Anti-fit: do
NOT tune a combination onto 1.889; test PRINCIPLED candidates only (e.g. Σ_2row y_λ / y_[12],
tr_M-normalised stratum mass, the two-row/one-row ratio). Honest outcome expected: either a
principled quantity lands near 1.889 (report as scope-a, numerology-guarded) or none does (report the
negative and the two-row stratum is refuted too). Formalize-first where a structural claim prunes.
Complements qou-58r5 (ρ_F open content). No wiring.

## 2026-08-21 — ATTEMPTED, honest wall: ρ_F is not a constant
Ran the derivation attempt (he4_rho_F_two_row_stratum_search.py; audit 2026-08-21-rho-F-derivation-
attempt-not-a-constant.md). (1) No fit-free two-row ratio reproduces 1.889 (closest 1.78, −5.7%,
cherry-picks blocks). (2) DECISIVE: ρ_F=B_AME/(m_e·A·8G) drifts 1.889→2.130→2.284 across
⁴He/¹⁶O/⁴⁰Ca (21% spread); Coulomb makes it worse (1.95→2.80). So ρ_F is a per-nucleus A-dependent
effective prefactor — '2' is the rounded ⁴He value, no constant to derive. The real open target is
ρ_F(A), harder than 'which integer'. Status stays open; re-posed. No wiring.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-21 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 75 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean` (`two_row_frobenius_stratum_drift_and_non_constant_obstruction`)
- **Summary**: Proved non-constant obstruction across `4He` (`rho_4`) and `16O` (`rho_16`) when `rho_4 != rho_16`, non-vanishing drift `rho_16 - rho_4 != 0`, and `twoRowPartitionCount 12 = 7`.
- **80-dps Probe & Witness**: `computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py` -> `computations/probes/two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json` (`scriptCommitSha: 2463220ce5c89b017aafd3bf4d0ccffbad829f4f`, PR head `9ae0c19dfa3265ac670ac5d85777be275271ab28`)
