---
# qou-jmet
title: 'GAP: precision-gates.sh --changed clobbers 3 corpus-wide audit witnesses with scoped output'
status: todo
type: task
created_at: 2026-08-15T15:05:15Z
updated_at: 2026-08-15T15:05:15Z
---


## Closed — landed by a sibling (`qou-pgdw`), whose fix was better

A sibling session found the same bug independently and landed it first:
`70835094` + `7668b998` on main. My PR #5147 carried the same idea and is
withdrawn to a doc-only change.

**Their version is strictly better, in two ways I missed:**

1. **Self-exclusion.** `SELF_OUTPUT_PREFIX` keeps the derived witness out of
   the scan. Mine wrote a new witness under `computations/` that the NEXT run
   would then scan and re-detect as the audit's own output.
2. **The `-audit.witness.json` suffix is load-bearing.** `AUDIT_SUFFIXES` in
   `computations/audits/q0_anchor_consistency_audit.py` classifies audit
   self-outputs by SUFFIX. My name ended in the scan slug, which would have
   filed it as `Q0_ANCHOR_MISSING` — they measured the consequence, 1889 →
   1890. They infix the slug instead.

Both are real defects in mine, not stylistic differences.

**My title for this bean was also wrong**: it says `--changed` clobbers.
`--changed` is only a short-circuit deciding whether to run at all and scopes
no gate; the mechanism is the shared output path, which is why it also fired
on full runs. Corrected in `local/compute-author` §5.1, which still carried
my wrong version on main after their code fix landed — the docs were the one
thing the sibling did not touch, and the only part of #5147 worth keeping.

Lesson for the overlap rule: this was **mechanical** work, which AGENTS.md
says has one owner. I did not check whether a sibling was on it before
starting. A `git log origin/main --since` on the touched file would have cost
seconds and saved the duplicate.
