---
# qou-hz0e
title: 'PR #4884: rebase 21 commits onto main (381 commits behind)'
status: completed
type: task
priority: normal
created_at: 2026-08-10T07:07:52Z
updated_at: 2026-08-10T12:53:10Z
parent: qou-aemy
---

Rebased `claude/algebraic-independence-obstruction-e8hiex` onto current `main`
and force-with-lease pushed. Final head `a8677cb287c0f6`.

**Outcome: clean.** All 21 authoring commits replayed, **zero conflicts**, and
the diff was preserved exactly — 57 files / +4924 / −1181, unchanged before and
after. `mergeable_state` went `behind` → `clean`. No science claim was touched
by the rebase, which is what made the rest of the pickup a verification job
rather than a re-derivation.

**The gap was 381 commits.** That number is the point of this record: it is
large enough that two things which look like formalities are not.

1. *Restored oleans cannot be trusted across it.* The `lake-cache` branch was
   seeded 2026-08-07 00:11; `HyperbolicVolumeTranscendence.lean` changed 08-09
   and `MassGap.lean` later on 08-07, and then the rebase moved the branch
   across 381 further commits on top of that. `lean`-direct reads imports from
   oleans, so verifying against the restored cache would have re-run the exact
   error the authoring session had already caught and documented mid-branch
   (bean `qou-fjcd`). See `qou-rok2` for what was done instead.
2. *Generated artifacts go stale from the base, not from your own edits.* Three
   audit witnesses and the authors-note coverage stats came back red purely
   because the base moved (`73090b045`, `5c7cac6fc`). The authors-note drift
   is **inherited** — this branch adds no content blocks, so a +22 block delta
   cannot originate here — and saying so explicitly is what stops a later
   reader from attributing it to the branch.

**Cost note.** A rebase this far back is cheap in conflicts and expensive in
re-verification: the zero-conflict replay took minutes, and the from-source
Lean rebuild it forced took the better part of an hour (`qou-rok2`). Price the
second one, not the first, when deciding whether to rebase or merge-forward.
