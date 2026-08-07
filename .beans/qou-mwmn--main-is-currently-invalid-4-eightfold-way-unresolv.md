---
# qou-mwmn
title: 'main is currently INVALID: 4 eightfold-way unresolved-uses errors — PR #4640 owns the fix'
status: todo
type: task
priority: normal
created_at: 2026-08-07T10:41:28Z
updated_at: 2026-08-07T10:41:29Z
parent: qou-kemt
---

run-validate on the folio-assistant pipeline, 2026-08-07: 4 HARD errors, all in the eightfold-way chapter, all 'Unresolved uses':\n  a2-from-three-strands  -> def:hecke-algebra\n  schur-weyl-eightfold   -> def:hecke-algebra\n  color-su3-from-g2      -> def:octonion-algebra\n  meson-mass-splitting   -> prop:q-deformation-weight-lattice\n\nDO NOT FIX HERE -- draft PR #4640 (copilot/eight-fold) already owns these and has the fuller fix. Its body names them exactly: 'def:hecke-algebra (3 blocks, doesn't exist)', 'def:octonion-algebra does not exist anywhere in the corpus', a prop:/rem: prefix mismatch, and '8 hard validation errors -> 0'. It also fixes the ROOT CAUSE that a point fix would miss: a schema violation where 'lean:' was a bare string instead of { ref: ... } on three blocks, so q-deformation-weight-lattice failed to IMPORT entirely, silently unregistering its label and cascading -- which is why meson-mass-splitting cannot resolve prop:q-deformation-weight-lattice.\n\nACTION: get #4640 reviewed and merged rather than patching main piecemeal. Duplicating its fix would conflict with it.\n\nNOTE FOR THE RECORD: main being invalid is not caught by CI as a blocker today (validate is not gating), which is how it persisted.
