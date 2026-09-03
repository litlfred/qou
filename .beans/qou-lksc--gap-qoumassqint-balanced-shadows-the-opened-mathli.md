---
# qou-lksc
title: 'GAP: QOU.Mass.qInt (balanced) SHADOWS the opened MathlibExt.qInt (geometric) — two red modules on main'
status: completed
type: task
priority: high
created_at: 2026-08-30T08:41:28Z
updated_at: 2026-08-30T11:03:20Z
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


## 2026-08-30 — fixed, and a THIRD defect in the same chain

Both qInt shadowings fixed by full qualification (`QOU.MathlibExt.qInt`) plus a
disambiguation note per file. PR #6140.

Whole-corpus after that fix: up-to-date 2128, ok 210, **blocked 0**, error 1. The 179
sorry-free-but-unverifiable modules are FULLY DRAINED.

### The remaining error was the next layer down

`QOU` — the root aggregator — was `blocked` in BOTH earlier runs (behind QIntegerCanonical,
then behind QDiffProlongationBaseOperator) and only reached elaboration once those were
fixed:

    import QOU.Archimedean.ParticleKnots failed, environment already contains
    'QOU.Archimedean.R_q' from QOU.Archimedean.GroundRing

GroundRing and ParticleKnots both declared `abbrev R_q := LaurentPolynomial ℤ` — same name,
same namespace, same body, neither importing the other. Each compiles ALONE; they collide
only where something imports both, and the only thing that does is the root aggregator that
nothing had been able to check. Fixed: ParticleKnots imports GroundRing and drops the
duplicate.

### What this sharpens

The corpus was carrying THREE independent breaks stacked behind one another:

    QIntegerCanonical  hid  the two qInt shadowings  hid  the R_q collision

So the "179 sorry-free but unverifiable" figure UNDERSTATED the damage. A blocked cone hides
not only unverified modules but **other errors**, and each fix reveals the next layer. Any
future sweep of this class should expect to iterate, not to measure once.

### A correction on my own diagnosis

My first hand-run of QOU.lean reported `unknown module prefix 'UGB'` and I nearly recorded
that as the defect. It was my LEAN_PATH omitting the sibling path-packages (ugb, fred2005)
that `scripts/lean-direct-cone.sh` adds from `content/*/lean/.lake/build/lib/lean`. Wrong
environment, not wrong code. Use the script, or copy its WHOLE path construction — the
fetched-packages loop alone is not enough.


## 2026-08-30 — the finding is now a standing measurement, and my count was off by one

Added the **sorry-free illusion** cross-check to `scripts/lean_cone_triage.py` — the tool
that already summarises a `lean-direct-cone.sh --all -k --report` run into measured-red vs
blocked vs env-gap. Corpus-grepped BEFORE writing this time; the tool existed and was better
than my ad-hoc analysis (it separates environment olean gaps from genuine corpus reds, which
mine did not). The one number it lacked is the one this session established.

It reports, over every module that never type-checked: how many carry zero `sorry` tokens
(the illusion — screen green, no verdict available) vs how many are honestly marked.

### CORRECTION: 180, not 179

I quoted **179** all session. That counted `blocked` only. The correct denominator is
everything that never type-checked, which includes the errored module itself — and
QIntegerCanonical also reads sorry-free. Validated against the three snapshots:

    snapshot     blocked&clean   errored&clean   never-checked&clean
    pre-#6108        179              1                 180
    post-#6108         2              2                   4
    post-#6140         0              0                   0

So: **180 -> 4 -> 0**. The arc is unchanged and the fixes did what was claimed; the peak
figure was understated by one, and the mechanism of the understatement is worth keeping —
I split on `blocked` because that was the category I was chasing, and silently excluded the
red module that started it.

### Why it lives in the triage tool rather than a new script

The count is only meaningful against a whole-corpus `-k` run, which is exactly this tool's
input. A standalone script would have to reproduce the cone build, the env-gap distinction
and the blocker attribution — all of which already exist here and are better than what I
would have rebuilt.


---

## CLOSED 2026-08-30 — all three defects fixed and merged

`QOU/Mass/ColorCurveQIntegerForm.lean` and
`QOU/Mass/QDiffProlongationBaseOperator.lean` now fully qualify
`QOU.MathlibExt.qInt` with a disambiguation note; `QOU/Archimedean/ParticleKnots.lean`
dropped its duplicate `abbrev R_q` and imports `QOU.Archimedean.GroundRing`
(PR #6140, `6e771d6f7ce`). `lean QOU.lean` exits 0; the corpus went from 180
modules reading sorry-free while never type-checked, to 0.

The generalisation — 26 further module pairs that can never both be imported —
is measured and guarded in `qou-kfcl` / PR #6191, not here.
