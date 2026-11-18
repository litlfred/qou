---
# qou-m8zb
title: 'GAP: deprecated aliases + call-site migration for the 10 cellContent / 3 axialDistance copies (cdup follow-up)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:50:56Z
updated_at: 2026-10-04T15:19:55Z
parent: qou-5vkl
---

Follow-up to `qou-cdup`, opened from PR #5704 (additive tranche). Two halves of
the bean's suggested disposition were **not** done there, deliberately, and this
records why so the next agent does not redo the reasoning.

## What #5704 did do

Added `axialDistance` to `QOU.MathlibExt.YoungDiagramCells` and bridged every
remaining copy. Measured from the tree, the counts in `cdup` were understated:
**ten** reachable `content` copies in the library, not eight, four of them never
recorded anywhere (`QOU.SchurWeyl.cellContent` -- which a `cdup` note claimed does
not exist; `QOU.QBeta.WenzlWeight.content`; `QOU.Hecke.content`;
`QOU.HeckeAlgebra.JonesMarkovWenzl.cellContent`, which hides behind an unused
`Partition` argument). Three `axialDistance` copies, all now bridged, including
`QOU.Hecke.axialDistance`, which was set aside as out of scope on signature
grounds and is not.

## What is left, and why it was not done

**1. `@[deprecated]` aliases.** The `cdup` disposition asks for the existing
names to become deprecated aliases. Not done: attaching `@[deprecated]` to ten
declarations makes every one of their 80+ call sites emit a warning, across eight
files whose dependent cones were not verifiable in that session (restored olean
cache, no CI). A warning is not a break, but landing 80+ of them unverified is
not obviously better than leaving them silent. Wants a session with a real build.

**2. Call-site migration.** `cdup` part 3 measured this at 80+ occurrences across
eight files, several of them `rw` / `simp only` definitional unfolds inside live
sorry-free proofs, and **declined it with the numbers on the table**. That
recommendation still stands as far as the measurement goes -- but note the
measurement predates the four unrecorded copies, so 80+ is itself a floor, not a
total.

**3. The two standalone content-block siblings** (`QOU.BraidsAndKnots.cellContent`
in `y-lambda-recipe-from-partition.lean`, and the `cellContent` in
`jucys-murphy-central-elements-qou.lean`) remain unbridgeable -- nothing can import
them. Draining those needs a content-block sibling promoted to a library module
first, which is a different and larger task than a `rfl` lemma.

## What changed in the argument

`cdup`'s "close the drain half, this is cosmetic" verdict was reached before the
`axialDistance` escalation. The hazard there is not duplicated effort: the
enclosing namespace beats `open`, so a `rw` across two rfl-equal-but-distinct
`axialDistance` constants **fails silently**, printing both sides identically.
That is a correctness hazard rather than tidiness -- but it is now *mitigated by
the bridges*, so it argues for finishing the aliases, not for forcing the
migration.
