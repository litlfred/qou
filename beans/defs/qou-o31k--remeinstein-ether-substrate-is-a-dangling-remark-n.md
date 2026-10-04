---
# qou-o31k
title: rem:einstein-ether-substrate is a dangling remark (no interprets field)
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T10:39:25Z
updated_at: 2026-10-04T15:23:22Z
parent: qou-hqo3
---

run-validate warning 2026-08-07. Per AGENTS.md section 3a, a remark making a mathematical claim without an 'interprets' field is a DANGLING REMARK. Resolve by one of the three sanctioned dispositions: (a) promote the claim to a proposition/lemma with Lean, (b) add interprets: pointing at the provable block it interprets, or (c) demote to kind 'prose' if it carries no logical content. Given the title (Einstein ether substrate) this is most likely (c) or (b). Do NOT add a stub Lean file to satisfy it -- section 0a bans shadowing stubs.
