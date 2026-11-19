---
# qou-d6zx
title: 'Checkpoint 4: 418-Table Caption Drain & Deterministic Block Title/Caption QA Guard'
status: completed
type: task
priority: high
created_at: 2026-11-19T12:46:13Z
updated_at: 2026-11-19T12:46:13Z
parent: qou-10v9
---

Drained all 418 raw label prefixes, mechanical `Data table` / `Table N from` placeholders, and truncated trailing prepositions/articles across monograph table `.ts` manifests, and wired deterministic `scanBlockTitleAndCaption` / `commentary-title-placeholder` checks into `cat-harness-tools` (`qa-checkers-voice.ts`, `qa-checkers-extended.ts`, commit `291f790c`) and `folio/pipeline/paper-commentary-audit.ts` (`0 of 3,635` blocks failing).
