---
# qou-9m7v
title: 'Step 2: the comparison iso (X⊗Y)ᘁᘁ ≅ Xᘁᘁ ⊗ Yᘁᘁ'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T20:06:56Z
---


## CLOSED 2026-08-26, in the same file as qou-l8az

tensorRightDualIso in QOU/MathlibExt/RigidTensorDual.lean:

    (X tensor Y)dual  iso  Ydual tensor Xdual

Both sides are right duals of X tensor Y -- the canonical one and the one
tensorExactPairing builds -- so rightDualIso compares them. One line once the
pairing exists. Sorry-free, axioms clean.

Note this is the ONE-fold iso. The comparison iso monoidality actually needs is
the DOUBLE dual, (X tensor Y)dualdual iso Xdualdual tensor Ydualdual, obtained by
applying this twice (and note the order un-reverses). That composition is not
yet written -- it belongs with step 3 (qou-ezas), where the statement of
monoidality is assembled.
