---
# qou-ju05
title: 'B (convention C): 14 actionable z_C sites + 2 C-specialised closed forms'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T16:31:28Z
updated_at: 2026-10-04T15:16:31Z
parent: qou-cdx1
---

## Result 2026-08-25 (PR #5767): 14 -> 11, and 11 is the FLOOR for a mechanical drain

Migrated 3: `lepton_tower_core.markov_z` (the one genuine live producer; now
delegates to the canonical definition rather than holding a second copy),
`pauli_young_spin_isospin_delta_lambda_probe` deuteron block, `probes/probe_alpha`.

The remaining 11 are **not a queue**:

- **9 in the qbeta/decay cone — z-swap FORBIDDEN, not merely unreviewed.**
  `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame
  ladder and the mass channel's two-row forcing mutually exclusive. Needs the S1
  re-derivation (`qou-cds1`). Substituting z_D is invalid, not cheap.
- **1 adjudicated**: `probes/markov_reduction_h3_to_h4_verify.py` documents in its
  own header that it is deliberately left in C + float64 as the historical record
  the Lean docstring cites, with a live both-conventions companion. The detector's
  actionable flag is a FALSE NEGATIVE on `deliberate`.
- **1 needs re-derivation**: `deltalambda/mirror_split_milnor_one_third_probe.py`
  carries three C-specialised closed forms (sqrt(q0), q0**1.5) beside its z.

So the detector's ACTIONABLE count overstates the drainable surface. Treat it as
an alarm, not a work queue.


## Merged-tree state 2026-08-25: 9 actionable, and braid-registry retired

Post-merge the count is 9 (main's work removed 2 more and added a
'BLOCKED on C by design (registry)' bucket that formalises the distinction).

Additionally retired `computations/braid-registry/` -> `_deprecated/`: 269 JSON
records, 268 carrying z_markov = 0.4993200830735895 at q = 1.11 — which is C
evaluated at a rounded q that is NEITHER pin, so not even C's value at a real
anchor (z_C at the proton pin is 0.49932033418369445). Dead producer, zero
readers. Changes no detector count (the audit is AST-over-*.py; these are JSON)
— the risk it closes is the next person to grep the corpus for a C value and
conclude axis B reopened. Found by the sibling on PR #5765, verified here first.

CORROBORATION: their bean qou-lp5d reaches this bean's 'unmigratable by
substitution' conclusion by symbolic measurement — z_C is bar-EVEN, z_D is
neither, and ord(z - 1/2) at q=1 is 2 for C against 1 for D — where this bean
argued it from decayLadder_zC_threeRow_ne_zero. Two independent routes.
