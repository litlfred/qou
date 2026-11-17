---
# qou-demm
title: 'B2-lift infra (1): land PeriodMapWeight Lean reduction — collapse 2-field TauRhoHodgeLift interface to the single MOC existence field, sorry-free'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T19:31:31Z
updated_at: 2026-10-04T15:16:33Z
parent: b9cj
---

## Scope (from audit 2026-08-02-hodge-lift-bring-h1-model.md §3 + the agent proposal)
The corpus `TauRhoHodgeLiftInterface.lean` states the B2 lift as a 2-field class/interface
(the involution-match field + the mode-space/period field). This session PROVED the
involution-match (rho<->Hodge conjugation, c=SWAP.conj) and the nome equivariance are
CANONICAL/automatic (hodge_lift_bring_model.py, 10/10). So the interface can be sharpened:
- Introduce a SINGLE-field class `PeriodMapWeight` carrying only the MOC existence field
  (the holomorphic period map Phi: q |-> H^1(E_{tau(q)}) subset H^1(Bring), nome-normalized,
  landing in the rank-2 conjugate-pair sub-object, with the conformal Laplacian as a real
  self-adjoint weight).
- DERIVE equal_split + doubled_total from that single field, mirroring the already-merged
  proved lemmas (rho_forced_equal_split, channel_share_is_half in
  PerLoopMeasureShadowAssembly.lean). Verify sorry-free (lean-direct exit 0).
- The point: reduce the wall from 2 open fields to 1, with the other two proved automatic.
DISCIPLINE: no instance fabricated (leave PeriodMapWeight uninstantiated = honest open
state). This is an INTERFACE SHARPENING, not a closure. Env note: Mathlib oleans may be
churned; restore lake-cache/qou-<slug> + lean-direct with LEAN_PATH, or wait for bg build.

## LANDED (2026-08-02): PeriodMapWeightReduction.lean — verified sorry-free (lean-direct exit 0)
Single-field class PeriodMapWeight (selfAdjoint) replaces the 2-field TauRhoHodgeLift.
Derived from the one field (reusing merged sorry-free shadow lemmas): equal_split
(old `conjugated` field, now DERIVED via rho_forced_equal_split), doubled_total
(channel_share_is_half), sharpened_assembly (discharges shadow_assembly's f/hnorm/hint).
Recorded automatic (not fields): involution_match_automatic (=shadow_intertwines.1),
nome_equivariance_automatic. NO instance fabricated (uninstantiated content-bearing Prop
= the honest open MOC). Wired into QOU.lean umbrella (Copilot lesson: else CI won't build).
Interface sharpening, NOT a closure; 1/(8pi) stays phase-4. Re-verified by orchestrator.

## Round 56 Update (PR #8271)
- Opened PR https://github.com/litlfred/qou/pull/8271 (`b2cbd4734e5f10beb2130e3555212a3d78a87989`, C1 `22c4bf632182163314cbb930ffed44b139fa5265`).
- Compiled under Lean 4.24.0 (`0` `sorry`, `0` `axiom`, `0` warnings) and verified `0` advisories across all 6 static vacuity & borrowed-name audits, with 80-dps `mpmath` witness `computations/probes/round56-devacuify-6qbv-b9cj.witness.json` (`scriptHash = c44bdf430d4f`).
