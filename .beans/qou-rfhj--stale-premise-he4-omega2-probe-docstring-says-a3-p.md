---
# qou-rfhj
title: 'STALE PREMISE: he4 Omega2 probe docstring says A=3 P<0 ''NO flip vs A=2''; both committed and fresh triton witnesses say sign=+1, sign_flip_vs_A2=True'
status: completed
type: bug
priority: high
created_at: 2026-09-08T06:44:54Z
updated_at: 2026-09-12T08:23:31Z
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


## RESOLVED 2026-09-11 — and the premise had reached the GENERATED VERDICT

Not just the docstring. Both verdict branches hardcoded "A=2 and A=3 were both
negative", so the A=4 run emitted, beside its own printed `A2=-1 A3=+1 A4=+1`:

  "NO MOVE — P(A=4) has the SAME sign as A=2 and A=3 (all positive; A2=-1 ...)
   the 'flips positive at A>=3' reading fails not just at the triton but at He4 too"

Three errors: A=2 does not share the sign; they are not all positive (contradicted
inside the same string); and A=3,A=4 both positive CONFIRMS "flips positive at
A>=3" rather than failing it. The comparison logic was always right
(flip = P_sign != a3_sign) — only the prose asserted an unchecked claim about A=2.
Verdict now derived from the measured signs; docstring corrected with the measured
A=3 value and the A=4 result.


---

## VERIFIED 2026-09-12 — the fix is in the producer, not only in the bean body. CLOSING.

This bean's own `## RESOLVED 2026-09-11` section is a claim; checked against the
file it names:

* `computations/deltalambda/he4_magnus_omega2_sign_sparse_probe.py:658` —
  `a3_sign = _sign("triton-magnus-omega2-sign.witness.json")`. The baseline sign
  is **read from the witness**, not hardcoded, and is passed at `:664` as
  `a_baseline_sign=a3_sign`.
* `triton_magnus_omega2_sign_probe.py:338-339` — `flip = (P_sign != a2_sign)`,
  guarded on both signs being non-zero, with a separate `P_sign == 0` branch. So
  "an absence" is no longer reported as a sign.
* The hardcoded premise survives **only** as a historical note in the `he4`
  docstring at `:14` — *"which asserted 'A=2 and A=3 were both negative' without
  checking. Fixed"* — which is a record, not a live assertion.

So all three errors this bean identified are gone from the verdict path: A=2's
sign is no longer assumed to match, the string can no longer contradict itself,
and the A≥3 reading is no longer reported as failing on data that confirms it.

**The deferral this bean recorded also resolved correctly.** It says the edit
waits for 77/77 because the he4 probe was mid-run with a source-blind
checkpoint (`qou-z3q9`) — the fix landed in the same commit that stamped both
caches on source, which is the condition the deferral was waiting on rather than
a decision to override it.

**Closeable under rule 13a**: the subject is a stale premise in a docstring and
a generated verdict — a mechanical defect, not an open conjecture. Nothing here
turns on unproved mathematics.
