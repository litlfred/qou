---
# qou-ctc3
title: 'B1: the RSZ closure audit names a CLASSICAL-ONLY file as the q-alien successor'
status: completed
type: task
priority: normal
created_at: 2026-09-07T06:35:10Z
updated_at: 2026-09-07T06:38:29Z
---

## DONE 2026-09-07

`docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md` §"Where the work goes
instead" cited `OneInstantonNormalization.lean` as evidence that alien calculus "is
already the corpus's route". That file is **CLASSICAL-ONLY** — theorems over
`{M Z : ℝ → ℝ}` with `HasDerivAt` in the hypotheses — while the same section warns
two paragraphs later that C1 **cannot** be confluenced to the classical setting. A
classical-only file cannot be the q-native route it recommends.

**The section's reasoning is untouched**, and is why the fix is worth making: alien
derivations genuinely need no slope filtration, which is exactly why they survive
where RSZ died. Only the pointer was wrong.

Added a correction note naming `QOU.Mathlib.QAlienBridgeEquation` / `QBridgeSystem`
— the carrier that actually fits (σ-conjugated `Derivation`, sorry-free, purely
algebraic import cone), and which the audit does not mention at all (0 grep hits).

**What is deliberately NOT claimed.** This clone is shallow, so `--diff-filter=A`
returns the fetch boundary for both the audit and the carrier — the same commit for
each. **It is undetermined here whether the carrier predated the audit**, so the note
records only that the text does not mention it, and does not assert the author
overlooked anything available at the time. That distinction is the same one this
session has been enforcing all day (a label is not a measurement); applying it to
someone else's work rather than only my own.

Also recorded: the carrier has **zero importers**, so the honest state of the
recommendation is not "untried" but "built, sorry-free, never instantiated".
