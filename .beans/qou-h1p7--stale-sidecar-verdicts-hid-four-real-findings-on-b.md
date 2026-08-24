---
# qou-h1p7
title: Stale sidecar verdicts hid four real findings on blocks the voice fix touched
status: todo
type: task
created_at: 2026-08-24T19:37:40Z
updated_at: 2026-08-24T19:37:40Z
---

Found 2026-08-24 while refreshing the 71 sidecars affected by the
`voice-scholarly-default` checker fix (`folio-assistant-fl5m`). The refresh
was expected to flip that one criterion; it also re-ran every other SCRIPT
criterion on those blocks at its current version, and four blocks turned out
to have been carrying **passing verdicts stamped 2026-07-13 / 2026-08-09
against older checker versions** while the current checker fails them.

None of these was caused by the voice fix. They were already true; nothing had
re-run the checker that says so.

## The four

**1. `prop:fivetwo-saddle-sum-rule` — `lean-ref-owns-decl` FAIL.**
`lean.ref` `qou:QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule` is
**also claimed by `thm:five-two-saddle-sum-rule`**. A declaration can be owned
by only one statement-bearing block; the formal graph attaches it to one of
them and the other is silently unbacked. This is the most serious of the four
and the only one that is not a prose-register issue: deciding which block owns
it is an authoring call, and until it is made, one of the two blocks' Lean
backing is fictional.

**2. `rem:markov-axioms-primitive` — `voice-author-notes-pollution` FAIL.**
`markov-axioms-primitive.md:20` opens
`**Selection note (owner ruling 2026-08-09 — convention C excised).**` in the
published prose. Per §4d that is `authorNotes` material.

**3. `prop:centered-hecke-variance-positive` — `voice-author-notes-pollution`
FAIL.** Same shape, `centered-hecke-variance-positive.md:20`:
`**Corrected 2026-08-09.** This proposition previously read
$z = 1/(q^{1/2}+q^{-1/2})$ — convention C, excised by the owner ruling of
2026-08-09 — ...`. A dated correction banner in prose.

**4. `prop:centered-hecke-variance-positive` — `voice-editorializing` FAIL.**
`...md:11`: "the variance is not **merely** positive — it **is** a Wenzl
weight." Also a `uses-editorial-hygiene` warn on the same block (one
transitively redundant `uses` edge).

Items 2-4 are exactly the class `qou-cauj` dispositioned for
`q-beta-c3-continuum-geometry`: a dated `**CORRECTION**` banner sitting in
published prose instead of `authorNotes`. The remedy there was to move the
banner and keep the content.

## Why this is a bean and not a fix in that commit

Item 1 needs an owner decision (which block keeps the declaration). Items 2-3
need the correction's substance preserved while the register moves, and item 3
carries a live convention-C/D correction whose wording matters. None is
mechanical, and none is in scope for a checker fix.

## The general point

A `.qa.json` criterion holds a HISTORY of entries, not one verdict. A stale
`pass` from July sits there looking authoritative until something re-runs the
checker — and nothing does, unless a block is edited or someone sweeps it.
`check-sidecars.sh` reports staleness only for CHANGED files, so a block that
nobody touches keeps its July verdict indefinitely. Four of 71 blocks — 6 % —
were in that state. A corpus-wide sweep would say how large the class really
is; that has not been run.

