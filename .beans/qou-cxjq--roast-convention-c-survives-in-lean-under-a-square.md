---
# qou-cxjq
title: 'ROAST: convention C survives in Lean under a square-root variable — the 2026-08-10 all-clear is false'
status: todo
type: task
priority: normal
created_at: 2026-08-26T05:27:06Z
updated_at: 2026-08-26T05:27:44Z
---

Found by the F1 agent (`qou-39bx`) while tracing where the deuteron's 27%
lives. Verified independently by me before recording.

## The finding

`content/quantum-observable-universe/lean/QOU/Hecke/ClosedFormInterfaceFactors.lean`
lines 14-20, verbatim:

    To avoid `Real.sqrt` (which would cross the substrate->archimedean wall),
    everything is stated in the square-root variable `s` with `q = s^2` [...]
      z = s/(s^2+1) = 1/(s + s^-1)

`s/(s^2+1)` with `q = s^2` IS `sqrt(q)/(q+1)`. **That is convention C**, excised
by owner ruling R1 on 2026-08-15 and again on 2026-08-09.

Meanwhile `QOU/MathlibExt/MarkovBondRule.lean` exports:

    /-- The convention-D Markov parameter `z = q^3/(q^2+1)`. -/
    noncomputable def markovZ (q : R) : R := q ^ 3 / (q ^ 2 + 1)

**Two Lean modules. One name `markovZ`. Opposite conventions. Both live.**

The detector sees NEITHER: `scripts/convention-c-producer-audit.py` reports 7
actionable, all in `computations/`, zero in `.lean`.

## THE ROAST

**1. AGENTS.md states an all-clear that is false, and states it twice.** It
records the 2026-08-10 drain as `0 in .lean/.ts, which the drain did clear`.
It did not clear. A file whose own docstring says "convention C" in plain
English sat there through the drain, through R1, and through every subsequent
count. Every re-measurement since has been reported against a surface that was
never actually scanned.

**2. This is the FOURTEENTH spelling**, and the taxonomy predicted it.
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues thirteen
detector-blind spellings, *four of which were found by detectors written to
catch the previous blind spot*. We knew the class was open and kept quoting the
count anyway.

**3. It hides by CHANGE OF VARIABLE, not change of form.** Every detector to
date greps the shape of `z` in `q`. This one is algebraically identical to C
and lexically shares nothing with it -- no `sqrt`, no `q+1`, no half-power. A
grep-based detector cannot in principle catch it. **The counter-move already
exists in AGENTS.md and we did not apply it**: *"test the ANSWER, not the
source"* -- the Markov peel's deuteron denominator factors as
`192*q^23*(q^2+1)^3` under D, one `(q^2+1)` per peel, and C cannot produce it.
A value cannot be re-spelled.

**4. The specific cost is not hypothetical.** This module *looks* like the
formal backing for the production deuteron number that F1 just spent a session
proving is a parameter-free failure. Its theorems are correct FOR C. If anyone
had cited them as D-backing, the +27% analysis would have been built on a
different convention than the compute it describes.

**5. My own reporting is implicated.** I quoted "7 actionable, zero in .lean"
to the owner earlier this session as a measured fact. It was measured, and the
measurement was against a surface with a hole in it. Measuring carefully with
an instrument you have documented as blind is not the same as measuring.

## Fix, in priority order

1. **Correct the AGENTS.md all-clear.** It is load-bearing -- agents read it and
   stop looking.
2. **Add the square-root-variable spelling to the detector**, and to the
   blindness taxonomy as #14.
3. **Reconcile the two `markovZ` definitions.** Do NOT substitute `s^2 = q` --
   the C theorems are correct for C and need re-deriving, not renaming.
4. **Prefer the answer-shaped test** (`(q^2+1)` divides the denominator) over
   any further source-shaped detector, per AGENTS.md's own guidance.
