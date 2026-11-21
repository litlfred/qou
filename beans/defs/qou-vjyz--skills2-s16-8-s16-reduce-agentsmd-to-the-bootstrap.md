---
# qou-vjyz
title: '[SKILLS2 S16] Reduce AGENTS.md to the bootstrap pointer (≤150 lines, outline in §1)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - skills2
created_at: 2026-10-04T16:35:53Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S16. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

8. S16 Reduce AGENTS.md to the bootstrap pointer (≤150 lines, outline in §1). Done when: every one of the 101 sections in `SKILLS2_agents_sections.tsv` has a resolvable target, the STALE removals are owner-confirmed, and the RULING-MATH text exists byte-identical at its new home. Size L. Depends on S11–S15.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Measured: `AGENTS.md` is **6,413** lines today (target ≤150). Depends on S11–S15, none landed. Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
