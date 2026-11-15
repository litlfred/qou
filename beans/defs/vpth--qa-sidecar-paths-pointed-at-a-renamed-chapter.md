---
# vpth
title: QA sidecar `paths` pointed into a chapter directory that no longer exists — 598 dead entries across 252 files
status: completed
type: bug
priority: high
tags:
    - qa
    - data-integrity
created_at: 2026-08-08T17:25:00Z
updated_at: 2026-09-26T11:03:15Z
---

Claimed and finished on `claude/sidecar-path-drift-2026-08-08`.

Fallout from the same chapter rename that produced the undefined
`chap:particle-interactions` warnings (#4786). Fixing those made this visible.

## Measured

    sidecars with at least one dead `paths` entry   252
    dead entries                                    598
      into particle-interactions/                   574
      elsewhere (observations, braids-and-knots, …)  24

Resolving each dead path by basename against the corpus:

    unique match   588
    ambiguous        0
    no match        10

**Zero ambiguity**, which is what made the sweep safe to automate rather than
triage by hand.

## Applied

- **584 entries repointed** across 248 sidecars to the file's real location.
- **2 dead `lean` entries dropped** — the block exists, the Lean sibling never
  did.
- **`linking-operations.qa.json` moved**, not deleted: it sat in the vanished
  directory and was its block's **only** QA record. Now beside the block in
  `knots-particles-confinement/`, with `paths` written from what actually
  exists.
- **`hecke-satisfies-blitvic-hypothesis`** had two sidecars, and the stale one
  carried three criteria the live one lacked — `voice-statement-no-interpretation`,
  `wall-side-statement`, `wall-side-proof`. Those were **merged into the live
  sidecar before the stale copy was deleted.** Deleting first would have
  silently dropped three verdicts.
- **4 sidecars deleted**: two stale duplicates (the second, `trace-locality-meets-gs-nonlocality`,
  carried nothing unique — checked, not assumed) and two whose block no longer
  exists anywhere (`reading-a-conditional-linking-weight`,
  `conj-chirality-ribbon-frobenius`).
- **The unregistered `particle-interactions/` chapter manifest removed.** It
  named 309 blocks; **all 309 exist elsewhere** — 156 in
  `knots-particles-confinement`, 153 in `nuclear-interactions`. The chapter was
  split into two live chapters and this is the pre-split original, absent from
  the paper manifest. Nothing unique was lost, and leaving it guarantees the
  next agent repeats the "the chapter is missing" confusion it caused here.

## Deliberately NOT rewritten: 94 sidecars still name the old path

They name it inside `criteria.<axis>[].evidence` and `referee_argument` — e.g.

    reviewed_at: 2026-07-07T14:26:57Z
    reviewer:    QA Drain Agent (gemini-3.1-pro)
    evidence:    content/…/particle-interactions/localized-hadron.ts:1

These are **dated verdicts citing the path as it stood when the review ran**,
and on that date it was correct. Rewriting a reviewer's citation to a path that
did not exist at review time falsifies the audit trail.

The distinction that matters: `paths` is the **structural** pointer tooling
follows, and it is now correct everywhere. `evidence` is prose inside a
timestamped verdict, and it stays as written.

## Verification

    remaining dead `paths` entries corpus-wide: 0
    validate: ✓ Valid — 5 issue(s)   (unchanged)
    check-sidecars: clean
