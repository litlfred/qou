---
# qou-u8ji
title: 'b_pred''s agreement with the measured mirror slope exists ONLY in the grouped ordering: canonical moves the plateau 1.42 -> 2.69 and flips the sign of kappa_AME'
status: in-progress
pr: 8321
branch: feat/qou-ai7v-cgyn-k12x-u8ji-y2np
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T06:47:34Z
updated_at: 2026-10-04T15:16:38Z
parent: qou-v2om
---

## OWNER CALL. Do not resolve this mechanically.

`probes/b_pred_mirror_slope_closed_form.py` is one of the 18 sites in
`qou-t29k` that assemble the grouped intra-nucleon word by construction. I went
to switch it to `nucleon_word_letters` as a mechanical drain and stopped,
because the switch does not preserve the result — it destroys it.

## Measured, both orderings, same entry point (Wenzl bridge, H_3, 50 dps)

| ordering | tau_p | tau_n | plateau `log_q0(tau_p/tau_n)` | `kappa_FW = -plateau/4` |
|---|---|---|---|---|
| grouped (**as committed**) | 1.14575969246 | 0.987743688116 | **1.4223** | **-0.3556** |
| borromean (**canonical**) | 0.629328402203 | 0.475133517156 | **2.6936** | **-0.6734** |

Both legs land exactly on known canonical constants (the grouped p/n pins and
the borromean p/n pins), so neither is a mis-run.

Measured mirror slope, from the IMME triplet/quartet witnesses:
1.326 (A=6) rising to 1.372 (A=12). The probe's claim is that the plateau plus
the vanishing epsilon correction reproduces those to <= 1e-3.

- **Grouped**: plateau 1.4223, epsilon correction brings finite-A down onto the
  measured curve. The claim holds.
- **Canonical**: plateau 2.6936 — **96 % above** the measured 1.372. The
  epsilon term is geometrically vanishing and cannot absorb that.

## Why this is not a tolerance question

The probe's stated consequence is that the framework half of the writhe
coefficient is DERIVED: `kappa = kappa_FW + kappa_AME` with observable
`kappa ~ -0.437`, leaving `kappa_AME ~ -0.094` as genuinely experimental
(Coulomb isovector). Under the canonical ordering `kappa_FW = -0.6734`, so

    kappa_AME = -0.437 - (-0.6734) = **+0.236**

— not a shifted residual but a **sign flip**, and 2.5x the magnitude. The
quantity attributed to experiment changes character entirely.

## Why I did not pick the ordering that works

Because that is the failure AGENTS.md names as "Selection against the target",
and it sits directly against the standing owner directive of no fitting outside
CAL-1/2/3. The ordering was ruled on 2026-09-05 (`qou-hu1f`) on structural
grounds — sigma_0 and sigma_1 are adjacent and do not commute, and the
confinement core is `(sigma_0 sigma_1^-1)^3` — with no reference to this
observable. Re-opening that ruling *because* the legacy frame matches a
measured slope would be choosing the frame from the answer.

Note also that this ratio is **not** in the invariant class.
`nucleon_word_letters` documents that log-ratios are ordering-invariant, but
that covers `tr_M(W_atom)/tr_M(W_free)` — the same nucleus over its own free
word. `tau_p/tau_n` is a ratio between two *different* nucleons and moves
freely: 1.1600 grouped against 1.3245 canonical.

## The three ways out, none of which I should choose

1. **The probe is a legacy-frame result.** Scope it explicitly — call
   `nucleon_word_letters(..., intra_order="grouped")`, say in the docstring
   that its agreement is frame-conditional, and stop presenting `kappa_FW` as
   derived in the canonical frame.
2. **The canonical result is right and the agreement was coincidence.** Switch
   it, record that `kappa_FW` overshoots by 96 %, and treat the 1.37 match as
   an artifact of the superseded ordering.
3. **Something upstream is wrong** — e.g. `tau_p/tau_n` is the wrong framework
   object for this slope, and the near-match under grouped was pointing at a
   different identity. This is the only branch that would rescue a derivation.

## Status

Left **as committed** (grouped), unswitched, and excluded from the qou-t29k
drain until this is decided. The probe is marked "Not wired" in its own
docstring, so nothing in production consumes it — this is a claim problem, not
a pipeline problem.

Parent: `16ax` (derive b_pred A->inf closed form). Mechanism: `qou-t29k`.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`FallbackTierWindowZeroingAndPerGeneratorGroupedVolume.lean`, `CanonicalBraidLinkingNonUniformityAndMirrorSlopeFlip.lean`, `SymmetryEnergyBarBranchContinuumAndBetaBlindness.lean`) and verified at 50 dps in `computations/probes/fallback_tier_grouped_volume_braid_linking_mirror_slope_symmetry_branch_probe.py` (`computations/probes/fallback-tier-grouped-volume-braid-linking-mirror-slope-symmetry-branch-probe.witness.json`, `allPassed = true`). Opened PR #8321 (`ready: cde173d67efbd687c4f51cce6847a870b6c300f4`).
