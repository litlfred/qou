---
# qou-lksc
title: 'GAP: QOU.Mass.qInt (balanced) SHADOWS the opened MathlibExt.qInt (geometric) — two red modules on main'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T08:41:28Z
updated_at: 2026-08-30T08:42:07Z
---

## The defect

Two modules are RED on main. Both sit in `namespace QOU.Mass.*` and both `open QOU.MathlibExt`:

    QOU/Mass/ColorCurveQIntegerForm.lean:66,74
    QOU/Mass/QDiffProlongationBaseOperator.lean:71

Their statements say `qInt`. They MEAN the geometric one — their own docstrings define it as
`[k]_z = sum_{i<k} z^i`, and ColorCurveQIntegerForm's whole content is that the colour spectral
cubic's coefficients are truncated geometric sums. Their proofs supply the geometric one.

But `QOU.Mass.qInt` exists (QHookDimension.lean:67) and is the **BALANCED** q-integer

    qInt q n = sum_{i in range n} q ^ (2*i - (n-1))

Lean resolves a bare name to the ENCLOSING namespace before an opened one, so `qInt` in these
files silently means `QOU.Mass.qInt`, not the opened `QOU.MathlibExt.qInt`. Measured error:

    has type      colorSpectralCubic z X = X^3 + (z+1)*X^2 + (sum range 3 z^i)*X + sum range 4 z^i
    but expected  colorSpectralCubic z X = X^3 + (sum x in range 2, z^(2x-1))*X^2 + ...

and at line 74, `qInt_succ` (about `MathlibExt.qInt`) offered against a goal about `qInt`.

## Why this class is worse than a missing import

The two fixes that landed earlier today (5479e2141a9 and 68dc39ba729) were the SAME commit's
victims by a LOUDER mechanism: a name that stopped resolving. This one still resolves — to
different mathematics. It fails late, at proof-checking rather than at elaboration of the
reference, and it would fail SILENTLY (compile green, mean the wrong thing) on any statement
where the two conventions happen to agree. Here they disagree at n=2 and the proof caught it;
that is luck, not a guard.

`1646b5d6d3` is now known to have broken FOUR modules by three different mechanisms:
  - QIntegerBarParity     — `open` of a namespace that was removed  (fixed 5479e2141a9, sibling)
  - QIntegerCanonical      — a qualified path to a def that was removed (fixed 68dc39ba729, mine)
  - ColorCurveQIntegerForm — shadowing, this bean
  - QDiffProlongationBaseOperator — shadowing, this bean

## Scope, measured

Exactly these two files. Scanned every file under QOU/Mass/ that is in `namespace QOU.Mass`,
opens `QOU.MathlibExt`, and mentions `qInt`: the two above and no others. 4 and 5 occurrences
respectively.

## Why it was invisible

Both were in the BLOCKED set behind QIntegerCanonical until 68dc39ba729 landed. A blocked cone
never compiles, so no error was ever reported and `grep -c sorry` read 0. They surfaced only in
the post-merge whole-corpus run: blocked 210 -> 3, error 1 -> 2. Nothing "regressed" — unblocking
converted two invisible errors into two visible ones.
