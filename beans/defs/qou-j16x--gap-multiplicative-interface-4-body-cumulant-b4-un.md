---
# qou-j16x
title: 'GAP: multiplicative interface 4-body cumulant b4 undershoots He4 target (6.3% production / 36% bar-invariant)'
status: in-progress
pr: 8295
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T18:36:28Z
updated_at: 2026-10-04T15:20:14Z
parent: qou-v2om
---


## What was attempted (Option-E front 4, 2026-08-02, PR #4605)

The **multiplicative** connected 4-body Ursell cumulant of the canonical
interface binding `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)`, evaluated 0-fit at q₀ on the
complete-graph K_A topology, `b₄ = fourthDiff(B(A))` with isospin-symmetric B(3).

- **Result (scope-a undershoot):** production `pn=z` → b₄ = 0.5826 MeV = **6.30 %**
  of the ⁴He AME target (9.243 MeV); bar-invariant `pn=z−h/2` → 3.369 MeV = **36.4 %**.
- **Cause:** `(1−∏f)` saturates (∏f→0 with more bonds), so B→E₀·τ_vac and the only
  A-growth is the weak τ_p^Z τ_n^N. A *multiplicative* interface product cannot be
  the missing operator.
- **NOT scope-b:** the multiplicative form *does* carry connected 4-body content
  (Lean `multBinding_b4_nonvacuous` = 3 ≠ 0), unlike the additive forms
  (`BodyOrderCumulant.fourthDiff_linear/pairwise` = 0).

## Surviving gap / next honest step

The missing ~94 % (retained) / ~64 % (bar-mixed) needs a **non-saturating**
connected 4-body operator (4-body cumulant that *grows*, not saturates). On the
board, not re-attacked here:
- `A4InterfaceMagnitude` one-scalar gate: a categorical principle fixing the
  `[1⁴]` exchange magnitude `m ∈ (0,1/√5)` strictly below the naive `z`.
- The anti-self-adjoint GGM/Stokes off-block the branching leaves free
  (`A3OffBlockDerivation`, `conj:qdifference-kernel-prolongation-symbol`, bean qou-jqof).

## Artifacts
- Probe: `computations/deltalambda/b4_multiplicative_cumulant_probe.py` (+witness)
- Lean: `folio/quantum-observable-universe/lean/QOU/MassTheory/B4MultiplicativeCumulant.lean`
- Audit: `docs/audits/2026-08-02-option-e-b4-multiplicative-cumulant.md`
- PR: #4605  ·  Nothing wired; B_AME diagnostic-only; free_parameters=0.
