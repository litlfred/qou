---
# qou-4b6g
title: Atlas provenance block cites two deprecated producers; 'no entry is maintained by hand' is unenforced
status: todo
type: task
priority: normal
created_at: 2026-08-25T22:10:29Z
updated_at: 2026-08-25T22:11:06Z
---

MEASURED 2026-08-25, bean qou-qpj9's arc.

content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-interpretation.md asserts:
  - 'The atlas is auto-rendered by [recursive_atom_knot_atlas_render.py]'
  - '[witness_staleness_tracker.py] marks the affected entries stale and the
     atlas is recomputed from the sources above; no entry is maintained by hand.'

BOTH producers are DEPRECATED. Neither exists at the linked path
computations/<name>.py; both are in computations/_deprecated/. So both links in
a published content block are dead.

Meanwhile the LIVE producer of computations/per-atom-hyperbolic-volume.witness.json
is per_atom_hyperbolic_volume_witness.py, which carries a HAND-WRITTEN ATLAS dict
with hardcoded knot names and braid words -- precisely what the sentence promises
does not exist. So the guarantee is unenforced and nothing currently detects drift
between the particle registry's canonical T_w and the hardcoded words.

SCOPE (a). This does NOT say any atlas volume is wrong. The p/n
'principled-derivation' tag was checked in the same pass and IS sound: those
volumes come from the registry's sigma-braid word via
hp_volume_of_link_closure(braid_word, digits=50), a genuine braid with a genuine
Markov closure. Three of six entries are an admitted fit (sibling's
docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md), not six.

NOT FIXED IN PR #5782: repairing the content block needs a .qa.json sidecar
refresh plus the render-QA gate, which would widen a docs-and-probes PR.

NEXT: decide whether the fix is (i) repoint the block at the live producer and
drop the 'no entry is maintained by hand' claim, or (ii) restore an automated
render so the claim becomes true again. (ii) is the better end state; (i) is the
honest interim.
