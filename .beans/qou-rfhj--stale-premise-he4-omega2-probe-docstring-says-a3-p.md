---
# qou-rfhj
title: 'STALE PREMISE: he4 Omega2 probe docstring says A=3 P<0 ''NO flip vs A=2''; both committed and fresh triton witnesses say sign=+1, sign_flip_vs_A2=True'
status: todo
type: bug
priority: high
created_at: 2026-09-08T06:44:54Z
updated_at: 2026-09-08T06:44:54Z
parent: qou-9c80
---

## Measured 2026-09-08

`he4_magnus_omega2_sign_sparse_probe.py` docstring:

    A=3 (triton_magnus_omega2_sign_probe.py, PR #6107): P<0 — NO flip vs A=2. The
         simple "negative→positive at A≥3" reading fails at the triton.
    A=4 (this probe...): does P(A=4) continue the negative run, or does the sign
         finally move at the alpha particle?

Both the COMMITTED and a FRESH 30/30 run of the triton probe report:

    P_total      = 2.470192708298933...   P_total_sign = +1
    A2_P_total_sign = -1                  sign_flip_vs_A2 = True
    [verdict] SIGN FLIP CONFIRMED — P(A=3) is POSITIVE while P(A=2) was NEGATIVE.

So the flip happens at A=3, not "fails at the triton". The he4 probe's framing
question ("does A=4 continue the negative run") is built on the stale premise:
there is no negative run past A=2 to continue. The live question is whether A=4
STAYS positive or flips back.

Corroboration: the he4 probe's own gate2 reproduces the committed triton datum
as `sparse P_total = 2.4701927083 ... sign sparse=+1 committed=+1`. The probe
therefore CONTRADICTS ITS OWN DOCSTRING at run time, in its own output.

## Fix deferred, deliberately

The he4 probe is mid-run and its checkpoint is source-blind (qou-z3q9), so
editing the file risks a later resume mixing code versions. Docstring-only edits
cannot move a number, but the hazard is exactly the one qou-z3q9 documents, so
the edit waits for 77/77 rather than relying on "it's only a comment".
