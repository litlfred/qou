---
# qou-ltal
title: Two declarations of QOU.Interactions.QIntegerMassFormula — one compiled with no consumers, one honest and uncompiled
status: todo
type: task
created_at: 2026-08-29T20:01:42Z
updated_at: 2026-08-29T20:01:42Z
---


Split out of `qou-tpt6` on 2026-08-29, during the merge of main into
`claude/mt7r-archimedean-eval-2026-08-24`.

## The situation

Two files declare the **same fully-qualified name** `QOU.Interactions.
QIntegerMassFormula` — same namespace, same class name — and they are not the
same class.

| | `lean/QOU/Interactions/QIntegerMassFormula.lean` | `content/…/mass-theory/q-integer-mass-formula.lean` |
|---|---|---|
| compiled by lake | **yes** (under `lean/`) | no (outside `lean/`) |
| states `fits_AME` | forwards it to `IsAMEValue.fits_bound` | **directly, as the conjecture** |
| `IsAMEValue` | yes — the conjecture lives in a class named for a lookup | none |
| instance | `canonical`, demoted to a `def` on main 2026-08-28 (`eaebcc286c4`) | **none**, so its conditional is genuinely conditional |
| consumers in the compiled tree | **zero** — verified 2026-08-29 | n/a |
| what a content block resolves to | — | **this one** (siblings resolve first) |

So the compiled declaration has no consumers, and the declaration the corpus
actually reads is the uncompiled sibling — which is also the honest one.

## Why this is filed rather than acted on

`qou-tpt6` (this branch) concluded the compiled file was not needed and deleted
it. During the merge that deletion was **reverted**, deliberately:
`eaebcc286c4` demoted its instance four days ago with a documented decision,
and overriding a fresh deliberate edit with a silent deletion inside a merge is
the wrong move. Main's version is restored and intact.

The deletion may still be right. It is a scoped decision for whoever owns that
file, not a merge artefact, and it needs one question answered that this bean
does not answer: **was the duplicate fully-qualified name known when the
instance was demoted?** If it was, there is a reason to keep both and it should
be written down. If it was not, the demotion was applied to the copy nothing
reads.

## Why it matters beyond tidiness

A block's `lean.ref` resolves to the sibling; `#print axioms` and `lake build`
see only the compiled one. Any statement of the form "the Lean says X" is
therefore ambiguous between two declarations that differ in exactly the field
carrying the conjecture. That is the same hazard as `qou-znut`'s three distinct
classes named `BorromeanQuark`, and the same hazard agent-B hit on
`CrystalRMatrixSubLemma`.

**The general question is the platform's, not QOU's:** should a
`content/*.lean` sibling be allowed to shadow a compiled module path? Nothing
today detects it.

- [ ] Answer whether the duplicate FQN was known at demotion time
- [ ] Decide: delete the compiled copy, rename one, or document why both exist
- [ ] Platform: consider a check for `content/*.lean` shadowing a compiled FQN
