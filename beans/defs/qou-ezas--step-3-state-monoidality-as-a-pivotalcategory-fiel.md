---
# qou-ezas
title: 'Step 3: state monoidality as a PivotalCategory field'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T20:51:57Z
---


## Half done 2026-08-26: the comparison iso exists; the FIELD is deliberately not added

tensorDoubleDualIso is built and verified (QOU/MathlibExt/RigidTensorDual.lean),
and the monoidality statement TYPECHECKS against it:

    (drinfeldIso (X tensor Y)).hom >> (tensorDoubleDualIso X Y).hom
      = (drinfeldIso X).hom tensorHom (drinfeldIso Y).hom

The FIELD is not added to PivotalCategory, on purpose. That class is already
merged to main, so adding a field breaks pivotalOfBraided unless the proof
(qou-wqst) lands in the same commit. Field and proof go together or not at all --
do not add the field speculatively.

BLOCKED 2026-08-26: see qou-wqst — the monoidality field is unprovable for pivotalOfBraided because drinfeldIso is not monoidal.



## UNBLOCKED 2026-08-26 (PR #5859)

The blocker was formulational and is gone: `twist_drinfeld_monoidal_tensorDoubleDualIso` states
the monoidality in the exact shape a field would take.

**Still not a mechanical edit.** The field cannot be added while `pivotalOfBraided` is an
instance — it is unprovable there because it is FALSE.  Landing the field means replacing that
instance with a ribbon-hypothesis one, i.e. a behavioural change to a class already on main.
Own PR, own review.



## DONE 2026-08-26 — PR #5860 (Option A, owner-chosen)

`PivotalCategory` now carries `pivotor_tensor`.  `pivotalOfBraided` removed (unconstructible
because false); `pivotalOfRibbon` added, requiring `[BalancedCategory C]`.

**Measured, not assumed:** instance search confirmed a symmetric right-rigid category still
resolves `PivotalCategory` automatically (Ribbon.lean's symmetric ⇒ balanced), so the apparent
cost of dropping the braided instance is near-zero in this corpus.  Zero code consumers existed;
five stale prose claims corrected across two files.

Required a prerequisite split — `rightDualIso_hom_unique`/`_evaluation`/`_trans` moved to
`RightDualIsoUnique.lean` to break a circular import (the field must mention
`tensorDoubleDualIso`, which lives downstream of where the class sat).
