---
# qou-demm
title: 'B2-lift infra (1): land PeriodMapWeight Lean reduction — collapse 2-field TauRhoHodgeLift interface to the single MOC existence field, sorry-free'
status: todo
type: task
created_at: 2026-08-02T19:31:31Z
updated_at: 2026-08-02T19:31:31Z
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
