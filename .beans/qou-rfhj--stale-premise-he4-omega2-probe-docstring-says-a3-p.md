---
# qou-rfhj
title: 'STALE PREMISE: he4 Omega2 probe docstring says A=3 P<0 ''NO flip vs A=2''; both committed and fresh triton witnesses say sign=+1, sign_flip_vs_A2=True'
status: todo
type: bug
priority: high
created_at: 2026-09-08T06:44:54Z
updated_at: 2026-09-13T13:02:45Z
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

## Verified 2026-09-13 post-merge — resolved, extended by main, and the STATUS is stale

Checked while merging main's 218 commits, because main's new `y_lambda`
conflation gate makes a claim that looked like it *reversed* this bean's
resolution. It does not reverse it; it deepens it, and the probe already says so.

**The worry.** `y_lambda_conflation_audit`'s own gate comment records that
re-weighting these probes' committed traces with the real Wenzl bridge **flips
P_total at A=3 and A=4** — *"Plancherel −,+,+ over A=2,3,4; Wenzl −,−,−"*. Taken
alone that would mean the 2026-09-11 correction here (A=2 −, A=3 +, A=4 +, so
"flips positive at A≥3") was computed under the wrong weight family, and the
*original* stale line — "A=3 P<0, NO flip vs A=2" — was accidentally right.

**It was already handled.** `he4_magnus_omega2_sign_sparse_probe.py`'s docstring
on the merged tree carries **both** readings and names the measure for each:

> Under the production Wenzl/Markov weight this probe now also reports … −20.466
> over A = 2, 3, 4: **NO sign change anywhere**, so the "sign moved at A=3"
> premise the A=4 question is built on is a property of the measure … which is
> why the verdict below states its arm rather than saying "the sign".

That is the correct resolution and it is stronger than this bean's: the sign
story is **measure-dependent**, so neither "flips at A≥3" nor "no flip" is *the*
answer, and the verdict now names its arm instead of asserting one. Main's gate
comment puts it the same way — *"a mislabelled weight was a mislabelled result"*.

**So nothing is owed here.** Two things worth flagging to whoever owns it:

1. **The status is `todo` while the body says "RESOLVED 2026-09-11".** Not
   changed by me — it is not my bean. But an idle-backlog sweep reads the
   status, not the body, so this sits in the ready list advertising work that
   was done two days ago and has since been superseded by a better answer.
2. **The 2026-09-11 fix would have gone stale on 2026-09-13 had main not
   extended it.** It replaced one hardcoded sign narrative with another
   hardcoded sign narrative — correct at the time, under a measure nobody had
   yet noticed was mislabelled. The durable form is the one the probe now has:
   report the arm, name the measure, and let the verdict be derived. Same
   lesson as `qou-n62l` — a description that hardcodes a finding keeps
   asserting it after the ground moves.
