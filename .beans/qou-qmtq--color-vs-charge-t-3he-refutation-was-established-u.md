---
# qou-qmtq
title: color-vs-charge T-3He refutation was established under convention C and does not survive D
status: todo
type: task
created_at: 2026-08-24T19:48:18Z
updated_at: 2026-08-24T19:48:18Z
---

NOT ADJUDICATED. This is a scientific verdict changing, not a mechanical
defect, and the producer's conclusion is owner/sibling territory. Recording
the evidence.

Surfaced by the drain (1e18c44fd) regenerating a stale witness, and caught by
the failed-assertion ratchet as a GROWN entry (1 -> 2 failures) in
probes/binding-color-vs-charge-tn3he-perknot-rerun.witness.json.

THE PRODUCER NOW CONTRADICTS ITSELF
Its computed output:
    color T-3He split = +0.309319 MeV  = +40.50 % of needed +0.76380 MeV
Its hardcoded verdict prose, unchanged:
    "Both forms give the identical split (~ -0.034 MeV, ~ 4.5 % of the needed
     +0.764 MeV): color at the delta = flavor-split scale is ~20x too small
     either way; the T-3He split remains CHARGE/Coulomb (alpha_EM sector)."
The magnitude moved by 9x AND THE SIGN REVERSED, -0.034 -> +0.309 MeV.

The assertion `color_too_small_under_perknot_base` is
    too_small = abs(frac_pk) < mp.mpf("0.10")
frac_pk is now 0.4050, so it correctly evaluates False and correctly fails.
THE ASSERTION IS NOT THE BUG -- it is doing its job.

WHY IT MOVED: THE C -> D CONVENTION MIGRATION
    split = B0["nn"]*w["nn"] - B0["pp"]*w["pp"]
(the two 2*B0["pn"]*w["pn"] terms cancel exactly), with weights ~0.9995, so
this is a difference of two nearly-equal bond energies -- a catastrophic
cancellation, which is why a 7% move in B0 becomes a 9x move plus a sign
flip in the split. B0_bonds_MeV.pp went 2.28608750851925910722618784769 ->
2.12836094575708300298497824949.

B0 is built from `_per_block`, which sums y_lambda * |Re chi| over the
partitions of 6. Under convention D the row cap y_lambda = 0 for l(lambda) > 2
is active -- verified directly at q0:
    [6] [5,1] [4,2] [3,3]                              nonzero
    [4,1,1] [3,2,1] [3,1,1,1] [2,2,2] [2,2,1,1]
    [2,1,1,1,1] [1,1,1,1,1,1]                          ALL 0.0
Seven of eleven partitions dropped out. The committed witness predated the
migration; the drain regenerated it under D.

WHAT NEEDS DECIDING
Under D this producer's own numbers say color supplies 40.5% of the needed
T-3He split, not 4.5%, and with the opposite sign. "Color at the delta =
flavor-split scale is ~20x too small" is not supported by them any more.
Either the refutation is convention-C-specific and must be restated, or the
producer's inputs need revisiting under D. I have not touched the verdict
prose: editing it to match the new numbers would be me adjudicating the
claim, and leaving it is at least visibly inconsistent rather than quietly
wrong.

SEPARATELY, and not mine: delta-lambda-canonical-residual.witness.json also
shows GROWN 1 -> 2 in the same ratchet. Neither main nor this branch has
touched it since the merge-base (0 commits each), so it predates this branch
entirely.
