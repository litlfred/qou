---
# qou-ezas
title: 'Step 3: state monoidality as a PivotalCategory field'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T18:37:57Z
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
