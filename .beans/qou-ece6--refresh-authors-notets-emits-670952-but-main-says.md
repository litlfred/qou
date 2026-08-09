---
# qou-ece6
title: 'refresh-authors-note.ts emits 670/95.2% but main says 661/93.9% — the script silently reverts #4862'
status: todo
type: task
priority: high
created_at: 2026-08-09T12:05:00Z
updated_at: 2026-08-09T12:05:00Z
---

**A booby trap: running a documented maintenance command reverts a landed
correction, and nothing flags it.**

## What happened

PR #4862 corrected the authors-note Lean-coverage headline by hand:

> `docs(authors-note): the Lean-coverage headline overclaims by 23 proofs`
> — 97.2% → **93.9%**, i.e. **661 of 704** provable claims sorry-free.

It changed **only** `authors-note.md` and `lean-coverage.json` (2 files,
6 insertions). It did **not** change `scripts/refresh-authors-note.ts`.

The script still computes **670 of 704 (95.2%)**. So the generator and the
committed file now disagree by 9 proofs, with the *file* being the corrected
side and the *script* being the wrong side.

## Why it is a trap rather than mere drift

The normal preflight actively steers agents into it. `scripts/check-sidecars.sh`
reports:

```
▸ authors-note Lean-coverage stats STALE (proved-counts drifted)
    → bun run scripts/refresh-authors-note.ts   (rewrites note + lean-coverage.json; commit both)
```

An agent that follows that instruction regenerates 670/95.2%, silently undoing
#4862. There is no conflict, no warning, and the diff looks like a routine
chore refresh — which is exactly how it reads in a review.

Caught on PR #4846: that branch had run the refresh as an idle-time chore
*before* #4862 landed, then rebased. Git reported **zero conflicts** (the two
edits never met in a three-way merge), so merging would have reverted the
correction invisibly. The commit was dropped from the branch instead. It was
only noticed because that PR happened to be auditing this exact class of
silent loss.

## What needs deciding (do not guess)

Which side is right? The two possibilities need different fixes:

1. **The script overcounts by 9.** Then fix the counting logic in
   `scripts/refresh-authors-note.ts` so it emits 661, and #4862's file stands.
   Likely candidates: what counts as a "provable claim", whether conditional
   `sorry`-carrying declarations are excluded, whether orphaned modules (see
   `qou-kljb` — 785 QOU modules are never built) are being counted as proved
   without ever having been elaborated.
2. **#4862 undercounted.** Then the file should go back to the script's number
   and #4862's reasoning needs revisiting.

Read #4862's rationale first — it claims a specific overclaim of 23 proofs
against the *then-current* headline, so its arithmetic is the primary evidence.

## Until it is resolved

- **Do not run `scripts/refresh-authors-note.ts`** and commit the result. If
  `check-sidecars.sh` tells you the authors-note is stale, that warning is
  currently untrustworthy — leave the file alone and reference this bean.
- Consider making the script refuse to write when its computed value disagrees
  with the committed file by more than a threshold, so the divergence surfaces
  as an error instead of a silent overwrite.

## Interaction with qou-kljb

If the script counts declarations in modules that `lake build QOU` never
elaborates (785 of 1659 — see `qou-kljb`), then "sorry-free" is being asserted
for files nothing ever checked. That would make the script's number wrong in a
way that matters well beyond the headline, and it is the first hypothesis worth
testing under option 1.
