---
# qou-0hu2
title: 15 stalled PRs carry live unlanded work — needs per-PR disposition (not supersession)
status: todo
type: task
priority: normal
created_at: 2026-08-10T03:05:31Z
updated_at: 2026-08-10T03:42:06Z
parent: qou-531z
---

METHOD CONSTRAINT (learned from #4834): the unique-lines heuristic is UNSOUND for disposition. It measures textual difference, not unlanded substance - when main rewrites the same claim better, every rewritten line counts as branch-unique and a fully-superseded PR scores 'live'. #4834 scored 29/29 files live and was totally superseded. So '15 live' is an UPPER BOUND. Per-PR disposition must read content, not count lines. Blob-hash identity (used for #4589) remains sound.
