---
# qou-noj1
title: 'QA-sidecar NEW criterion refs-prose-mentions (user ask): agent audit validating named objects mentioned in prose resolve to a uses[]/defterm ref OR are introduced-before-use — catches forward-refs detangler misses (DAG-only, e.g. ''Bring''s surface specialisation'' in ch4)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-07T21:43:46Z
updated_at: 2026-11-15T14:20:00Z
parent: qou-5vkl
---

## 2026-11-15 — report-only checker built (owner chose "report-only" on a card)

`scripts/prose-mention-ref-audit.py`. It indexes terms from definition-block
titles, `defines[]` and `glossary.json`, orders blocks by paper position, and
reports unlinked prose mentions. It edits nothing and proposes no `uses[]`
edge: per the `fwr10` ruling a mention ranks blocks for reading, it is never a
dependency source.

First run on `main` (baseline, re-measure rather than quote):
`python3 scripts/prose-mention-ref-audit.py` -> 3502 blocks, 205 terms;
**forward 154 mentions / 137 blocks**; undeclared (advisory) 1096 / 841;
preview (preview chapter or same-chapter intro) 82.

The worked example is caught: `ex:vacuum-state-su2` -> `def:brings-surface`
("Bring's surface", +185 positions). Known blind spots: single-word terms,
paraphrase, titles of non-definition blocks.

