---
# qou-lwyo
title: 'QOU run-validate is RED as of 2026-08-21: a correct de-laundering deleted a definition''s Lean sibling, and lake build cannot see it'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:53:13Z
updated_at: 2026-08-21T22:55:49Z
---

`bun run scripts/run-validate.ts content/quantum-observable-universe` exits
**non-zero** on current `main`. One error, four warnings; UGB and Fred2005 are
both **0**. Verified on a pristine `origin/main` worktree, so it is not a
branch artifact.

```
✗ [qou-motivic-galois-instance]: Definition "def:qou-motivic-galois-instance"
  requires Lean formalization. Expected sibling file:
  .../mass-endomorphism/qou-motivic-galois-instance.lean
  (or Lake-tree resolution from lean.ref
   "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar")
```

## The cause is a good commit, and that is the point

`73a21ac34a` (2026-08-21 20:08) deleted
`mass-endomorphism/qou-motivic-galois-instance.lean` because it had **three
type mismatches, a bare `axiom` on line 87, and had never compiled**. It also
demoted `almost_everywhere_nontrivial` from a `MotivicGaloisCharacter` class
field to a standalone theorem, so instances stop being forced to "either prove
it or launder an axiom". That is textbook de-laundering and it should stay.

The block is a **`definition`**, where the Lean sibling is *enforced*. Deleting
the sibling made the `lean.ref` unresolvable, and the whole paper's content
validation went red.

**The commit's verification could not have caught it.** It records
`lake build QOU.LiftingDescent: exit 0, 3139 jobs, sorry-free` — correct, and
blind to this: the broken thing is a **content-pipeline** constraint, not a Lean
one, and the deleted file was never in the Lean build to begin with. Two
verification surfaces, and the failure landed in the one that was not run.

This is the mirror of the sibling-masking hazard recorded on `qou-2u26`: there,
a co-located sibling stub **hides** a dead library ref from every gate; here,
**deleting** the sibling exposes one, paper-wide and immediately.

## Repointing is not available — I checked

The obvious cheap fix is to aim the ref at the replacement. It does not exist.
`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean` declares
**five theorems** about the perpetual obstruction —
`galois_trace_not_unit`, `perpetual_obstruction_from_trace`,
`qou_proton_perpetual_obstruction`, `qou_deuteron_perpetual_obstruction`,
`perpetual_obstruction_from_collapse_invariant` — and **zero `instance`**.

The block is titled *"QOU `MotivicGaloisCharacter` instance via Habiro
$\to \mathrm{Frob}_p$"*. None of those five is that instance. Pointing the ref
at one would put a block's label on a declaration proving something else — the
mislabelling failure `qou-2u26` is already tracking, committed deliberately.

Dropping the `lean` field does not work either: the constraint is on a
*definition having resolvable Lean*, not on the field being present, so the
error persists.

## What is actually left

Write the instance: `frobenius_at : Nat.Primes → Mhat` for the QOU substrate,
from the Habiro evaluation $\mathrm{Frob}_p = f(u)|_{u=\zeta_{2p}}$. The
computational side already exists —
[`habiro_frobenius_probe.py`](https://github.com/litlfred/qou/blob/main/computations/probes/habiro_frobenius_probe.py)
plus a 57 KB witness, marked `status: "verified"` on the block. Formalising it
is real mathematics and **must not be discharged with a trivial instance**;
that is exactly what `73a21ac34a` removed.

Until it is written, the honest state is that a `definition` wired into the
paper asserts a Lean instance nobody has built, and the red is the corpus
correctly saying so. Two blocks depend on it — `…-per-cell` (`example`) and
`…-verification` (`remark`) — both non-provable kinds, so no §3b propagation
breach.

**Decision for the owner.** Either (a) it gets formalised, or (b) the red is
accepted as a standing honest signal and every branch keeps stepping over it.
It is nine hours old, not nine days; but it is paper-wide, and it is already
being reported as inherited noise in at least three separate sessions —
including twice by me before I read the commit.

## Follow-on

The narrative's own status note is now stale in the other direction: the `.md`
says *"Lean status (2026-08-12): the co-located `.lean` file … has been
deleted"*, describing an **earlier** round. The file `73a21ac34a` deleted today
is a different one, and the note reads as if today's deletion were already
accounted for. Worth a line when this is next touched.


## The label test was run, and it agrees

The decisive test from `qou-2u26` — *does any Lean declaration carry the
block's own `\label`?* — is the one that repaired `thm:su2-emergence`,
`def:mass-identity`, `def:ns-regular-qou` and `prop:descent-eigenspaces`, each
time by finding the right declaration hiding under a wrong name. Run here:

```
grep -rln 'def:qou-motivic-galois-instance' --include=*.lean content/
→ (no matches)
```

**No `.lean` anywhere under `content/` carries this block's label** — not the
library tree, not any chapter directory. So the one route that has produced a
cheap repoint four times produces nothing here, which is the expected answer if
the declaration genuinely does not exist rather than merely being misnamed.

That closes the three cheap dispositions: no resolvable ref target (the named
decl was deleted), no label-carrying decl to repoint to, and no relief from
dropping the field. Writing the instance is what is left.
