---
# qou-5axo
title: Regenerate 4 muon-anchored witnesses still carrying the proton-y_lambda straddle
status: todo
type: task
priority: normal
created_at: 2026-08-17T01:01:34Z
updated_at: 2026-08-17T01:02:37Z
---

## Origin (PR #5260, bean qou-tzsp)

`tr_M_via_wenzl_bridge_mpfr` defaulted its y_λ table to the **proton** witness
(`_Y_LAMBDA_DEFAULT`), so every caller evaluating at the **muon** pin combined
proton y_λ with muon χ. Fixed at the producer on #5260 — the bridge now selects
the table by the layer of `q_str`.

`atomic-tr-m-mpfr-50dps.witness.json` was regenerated there and its
bridge-vs-peel gap collapsed from ~1e-9 to the 50-dps floor on all five atoms.
**Four muon-anchored witnesses from the same 14 importers were NOT regenerated**
and still carry values computed under the straddle:

  * `binding-canonical.witness.json`         (binding_canonical.py)
  * `mass-table-comprehensive.witness.json`  (mass_table_comprehensive.py)
  * `wedderburn-lp-ew-wiring.witness.json`   (wedderburn_lp_ew_wiring.py)
  * `ame-2020-binding-energies.witness.json`

Expected size of the correction, from the atomic case: ~3e-10 to ~2.2e-9
absolute on tr_M, i.e. the 11.54 ppb μ–p tension propagated through y_λ. That
is **above** the L1 1 ppQ compute-precision target, so these are not
below-noise; whether any downstream *conclusion* moves is unmeasured and is the
first thing to check per witness.

Not done on #5260 because each needs its producer re-run and its own
before/after diff read, and #5260 was already carrying three unrelated items.
Not a blocker for it: the defect is fixed at the producer, so anything
regenerated from here on is correct.

Check the q₀-anchor stamp on each before assuming it is muon — the list came
from `q0Anchor == "muon"`, and witnesses without the stamp were not surveyed,
so this list is a lower bound.
