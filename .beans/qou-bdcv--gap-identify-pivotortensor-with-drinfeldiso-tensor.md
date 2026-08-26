---
# qou-bdcv
title: 'GAP: identify pivotorTensor with drinfeldIso ≫ tensorDoubleDualIso'
status: completed
type: task
priority: normal
created_at: 2026-08-26T20:06:56Z
updated_at: 2026-08-26T20:18:46Z
---

Blocks the `PivotalCategory` monoidality field (qou-ezas).

**What is open.** `QOU.MathlibExt.pivotorTensor X Y : X ⊗ Y ≅ Xᘁᘁ ⊗ Yᘁᘁ` is built by
dual-uniqueness between two pairings of `Yᘁ ⊗ Xᘁ`.  `drinfeldIso (X ⊗ Y) ≫ (tensorDoubleDualIso X Y).hom`
is the same map — both are the monoidal structure map of the double-dual functor — but the two are
characterised against pairings on DIFFERENT base objects (`Yᘁ ⊗ Xᘁ` vs `(X ⊗ Y)ᘁ`), so
`rightDualIso_hom_unique` does not directly compare them.

**Route.** Transport a pairing along `tensorRightDualIso X Y : (X ⊗ Y)ᘁ ≅ Yᘁ ⊗ Xᘁ`.  Mathlib already
has `CategoryTheory.exactPairingCongrLeft` (`{X X' Y} [ExactPairing X' Y] (i : X ≅ X') : ExactPairing X Y`,
`evaluation' := Y ◁ i.hom ≫ ε_ _ _`) — I found it while looking for something else, so the transport
itself is free.  What is missing is the compatibility lemma: how `rightDualIso` behaves under
`exactPairingCongrLeft`.  Mathlib has no lemma about `rightDualIso` at all beyond `rightDualIso_id`;
PR #5848 added three (`rightDualIso_hom_evaluation` / `_unique` / `_trans`), and this would be a fourth
in the same family.

**Why it matters.** Only after this can a monoidality field be STATED in the form a
`PivotalCategory` instance would need.  The mathematics is already done (`twist_drinfeld_monoidal`,
merged in bfdedc68e6); this is the bridge from the convenient formulation to the canonical one.

Not urgent, and deliberately not bundled into #5848 — that PR was already 11 files, and the honest
scope note in the `pivotorTensor` docstring is what a reader needs meanwhile.



## DONE 2026-08-26 — PR #5859, and the proposed route was NOT the one that worked

`drinfeldIso_comp_tensorDoubleDualIso` proves the identification.

**Correction to this bean's own plan.** It said the route needs Mathlib's
`exactPairingCongrLeft` plus an unwritten `rightDualIso` compatibility lemma.  **Neither was
needed.** `tensorRightDualIso` is itself a `rightDualIso`, so it already carries an evaluation
identity; `braiding_naturality_right` then moves it across the braiding `drinfeldIso`
contributes.  Four evaluation identities and one interchange.

Unblocks qou-ezas.
