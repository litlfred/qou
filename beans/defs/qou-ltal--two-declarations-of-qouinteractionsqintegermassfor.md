---
# qou-ltal
title: Two declarations of QOU.Interactions.QIntegerMassFormula — one compiled with no consumers, one honest and uncompiled
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T20:01:42Z
updated_at: 2026-10-04T15:25:13Z
parent: qou-wp3h
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

- [x] Answer whether the duplicate FQN was known at demotion time
- [x] Decide: delete the compiled copy, rename one, or document why both exist
- [ ] Platform: consider a check for `content/*.lean` shadowing a compiled FQN


## Resolved 2026-08-30 — the sibling WAS known; the collision was not written down

The question this bean turned on is answered by the demotion commit itself,
`eaebcc286c4`:

> Measured: library file + **content-block sibling** +
> `wigner_coefficient_conditional` (the only outside consumer, binding the class
> as a HYPOTHESIS) all exit 0, 0 errors.

So the sibling was known, compiled and measured. Keeping both is a **standing
decision, not an oversight**, and the deletion `qou-tpt6` proposed would have
overridden a considered call. Good that the merge reverted it.

What was missing is not a decision — it is the **note**. Nothing in either file
said the other existed, and nothing detects a `content/*.lean` sibling shadowing
a compiled module path, so a reader of either had no way to know that
"the Lean says X" is ambiguous between two declarations differing in exactly
the field that carries the conjecture.

**Fixed by documenting the collision in both files**, each from its own side:

- `lean/QOU/Interactions/QIntegerMassFormula.lean` — compiled, zero consumers in
  the compiled tree, and the note says a content block's `lean.ref` resolves
  siblings first so the manuscript does not reach this file.
- `content/…/mass-theory/q-integer-mass-formula.lean` — not compiled, is what
  the block resolves to, states `fits_AME` directly and supplies no instance.

Cone compiles, `ok=1`.

The split is now explicit: **`#print axioms` and `lake build` see one file; the
manuscript sees the other.**

- [ ] Platform: a check for `content/*.lean` shadowing a compiled FQN — still
      open, and the general form of `qou-znut`'s three `BorromeanQuark` classes
      and the `CrystalRMatrixSubLemma` case. Nothing detects this today.

## Progress Update (PR litlfred/qou#8231)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8231 (`513987e80ae041a6d8bc835ffbdda5371ccac289`, scriptCommitSha `9bd895c1b028c3d1abf67e3de52aeade9e9e5ccc`)
- **Summary**: Added `asym_minus_volume_eq_half_volume`, `shell_eq_cube_q2_mul_exchange`, and `pairing_volume_cross_relation` in `QOU/Interactions/QIntegerMassFormula.lean`, verified by 80-dps mpmath probe `hyperbolic_planck_oneloop_qint_dilog_probe.py` (`scriptHash: 83d59661279d`).
