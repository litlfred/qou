---
# qou-o922
title: 'GAP: two lever1 producers flip muon->proton and drop q0Anchor on re-run (qou-po7i, measured)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:13:38Z
updated_at: 2026-08-21T22:14:11Z
---

Measured 2026-08-21 while fixing the wrap_legacy `computation` clobber (PR #5436).
A concrete, end-to-end instance of bean qou-po7i's argv[0] finding.

## The two producers

  computations/substrate/lever1_binding_core_characterization.py
  computations/substrate/lever1_binding_habiro_single_element_test.py

Neither is listed in computations/q0_anchor_manifest.json.

## What re-running them does

Both LOSE `q0Anchor` + `q0Value`. The second also flips its physics input:

    params.q0   1.10997859555733 (muon)  ->  1.10997858275138 (proton)

Mechanism, both halves of it:

1. `q_parameter` resolves the anchor from the argv[0] stem. No manifest entry
   => falls through to the PROTON default. The committed witness was written
   under MUON, so the input silently changes.
2. `WitnessBuilder.build()` stamps `q0Anchor` only when
   `q0_anchor_is_declared(script_path)` is true, which is False for an
   unlisted producer. So the label that would have made the flip visible is
   dropped in the SAME step.

That second half is what makes it dangerous: the pin changes and the audit
trail for the pin change disappears together. The anchor audit then reports
Q0_ANCHOR_MISSING -- "pre-backfill; not a failure" -- for a witness whose pin
just moved 11.5 ppb.

## Not fixed in #5436, deliberately

#5436 regenerates four other producers affected by the clobber; these two were
REVERTED rather than committed, because landing their regenerated witnesses
would commit a silent muon->proton flip inside a PR about a provenance key.

## Next step

Decide the intended pin for each, add a manifest entry under `ideal_muon` or
`physical_proton`, THEN re-run. Do not re-run first -- the run is what destroys
the evidence of which pin was intended.

Worth checking whether the pattern is wider: any producer that (a) is absent
from the manifest and (b) has a committed witness carrying a muon `q0Value` is
a candidate for the same silent flip on its next re-run. That intersection has
not been measured.
