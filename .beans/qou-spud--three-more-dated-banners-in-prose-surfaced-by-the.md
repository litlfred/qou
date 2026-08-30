---
# qou-spud
title: Three more dated banners in prose, surfaced by the 360-block hygiene re-sweep
status: completed
type: task
priority: normal
created_at: 2026-08-24T21:07:21Z
updated_at: 2026-08-24T21:18:07Z
---

Surfaced 2026-08-24 by re-sweeping the 360 blocks whose
`uses-editorial-hygiene: warn` the folio-assistant fix
(`folio-assistant-ckpe`) made obsolete. Re-running every script criterion at
its current version cleared 360 warns and 57 other stale verdicts, and left
**three** blocks newly failing `voice-author-notes-pollution` — dated banners
sitting in published prose (§4d says `authorNotes`). All three predate this
work; nothing had re-run the checker that says so.

Same class as the two fixed under `qou-h1p7`, and the same trap: **none is a
mechanical banner strip.** Each carries substance a reader needs, and only the
dated/versioning wrapper belongs in `authorNotes`.

## 1. `rem:bar-involution-c5-algebraic-identities`

`...md:3` — `**Corrected 2026-08-09.** The second factor is **not** $1/z$.`

The substance is a live warning against a specific conflation: under production
convention D, `1/z = (q^2+1)/q^3 = 1.632151991505175166202` at `q_0`, whereas
`q^{1/2} + q^{-1/2} = 2.0027...` is the reciprocal of the **excised** convention
C — a Temperley-Lieb loop parameter at half-argument, not a Markov parameter of
the Hecke generator. Keep all of that. What is `authorNotes` material is the
clause about how the error hid ("written as `1/z = ...` this identity escaped
every search for the convention-C formula") and the date.

## 2. `prop:qbeta-canonical-markov-weights-explicit-instance`

`...md:11` — the date is a parenthetical inside a scope statement that is
entirely reader-facing: this instance is built on `z(q) = 1/(q^{1/2}+q^{-1/2})`,
the excised convention C, it exists to show the class is non-empty, and nothing
downstream reads its `z` as the paper's. Only "(owner ruling 2026-08-09)" trips
P4. Cheapest of the three: name the convention without the date.

## 3. `rem:qou-motivic-galois-instance-verification`

`...md:12` — `- **Lean status (2026-08-23): there is no instance.**`

Load-bearing: the block previously asserted a Lean instance discharging
`def:motivic-galois-character` for the QOU substrate, and all three parts of
that claim have been false since 2026-08-12 — the `.lean` file was deleted (it
laundered the perpetual obstruction through a bare `axiom`) and
`almost_everywhere_nontrivial` was removed from `MotivicGaloisCharacter` the
same day. A reader must not be left thinking the instance exists. Keep the
fact; move "This bullet used to read ..." to `authorNotes`.

## Why a bean and not a drive-by

Each edit has to preserve a correction whose wording matters, and item 3
touches what the block claims about Lean. That is authoring, not lint. The
sweep is committed with the three failures **recorded rather than hidden** —
which is the point of `qou-h1p7`: a stale `pass` is worse than a visible fail.

---

## RESOLVED 2026-08-24 — all three, substance kept, versioning moved

* **`rem:bar-involution-c5-algebraic-identities`** — the "Corrected 2026-08-09"
  wrapper and the "escaped every search" clause are now an `authorNotes`
  entry. The prose keeps everything a reader needs: that the second factor is
  **not** `1/z`, both numbers that separate them (`1/z = 1.632151991505175166202`
  under D against `q^{1/2}+q^{-1/2} = 2.0027...`), that the latter is the
  reciprocal of the excised convention C and a Temperley-Lieb loop parameter at
  half-argument rather than a Markov parameter of the Hecke generator, and that
  identifying the two is what the notation register forbids.
* **`prop:qbeta-canonical-markov-weights-explicit-instance`** — only the
  parenthetical date tripped P4. Removed; an `authorNotes` entry records the
  ruling and, more usefully, why the instance is **deliberately** left on
  convention C: it exists to witness that `CanonicalMarkovWeightsH3` is
  inhabitable, so rebuilding it on the production `z` would be a different
  construction rather than a correction.
* **`rem:qou-motivic-galois-instance-verification`** — the bullet is now
  present-tense fact: `MotivicGaloisCharacter` carries one field,
  `frobenius_at`, nothing in the Lake tree supplies it for the QOU substrate,
  and `def:motivic-galois-character` is therefore not discharged. The design
  reason survives too — `almost_everywhere_nontrivial` was removed because
  encoding it as a class field forced every instance either to prove it or to
  launder the perpetual obstruction through a bare `axiom`. No new
  `authorNotes` needed: the block's 2026-08-23 entry already records the
  correction verbatim.

`voice-author-notes-pollution` passes on all three.

## What is left on them is not mine and not live

Two stale AGENT verdicts quoting prose these edits deleted —
`trap-meta-commentary` (2026-08-15) on the first and `trap-superlative`
(2026-08-22) on the third. Verified by grepping each verdict's own quoted
string against the current `.md`: 0 matches. A script sweep cannot clear an
agent verdict, so both will keep presenting as current until an agent
re-adjudicates. Opened as `qou-4sdp` — it is now three instances, which is a
class rather than an oddity.
