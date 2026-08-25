---
# qou-jmet
title: precision-gates.sh double-run clobbers 3 corpus-wide audit witnesses (shared output path, NOT --changed) — CLOSED
status: completed
type: task
priority: normal
created_at: 2026-08-15T15:05:15Z
updated_at: 2026-08-21T17:02:30Z
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



## Update 2026-08-21 — doc half confirmed closed

Verified: `.claude/skills/local/compute-author.md` §5.1 and the §7 gotchas
table row already carry the corrected mechanism on `main`
(`git diff origin/main -- .claude/skills/local/compute-author.md` is
0 lines against this branch's checkout). The corrected text — "The cause is
a shared output path, not a scoping flag" / "`--changed` is NOT the
mechanism" — matches the reference wording in `qou-pgdw`. No other site in
`.claude/skills/`, `docs/`, or other beans carries the wrong
(`--changed`-clobbers) description; a repo-wide grep for that phrasing
returns only this bean's own (retrospective, correct-in-context) title and
body text. Title corrected above to name the real mechanism, since titles
are what people grep. Both the code half (landed by `qou-pgdw`,
`70835094` + `7668b998`) and the doc half are now closed; no code or
witness files were touched for this update.
