---
# qou-jkam
title: 'lean-completeness: count the 14 mass-theory ''no sibling .lean'' blocks by lean.ref RESOLUTION, not sibling presence'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T02:14:49Z
updated_at: 2026-09-04T02:20:28Z
---

Owner pick 2026-09-04 (option 2 of the qou-zmuu close-out). The wall-side re-adjudication (#6529) found that of 14 mass-theory blocks whose 2026-07-07 QA fail said 'sibling Lean file is missing', at least 11 have a .ts lean.ref that RESOLVES to a library declaration under lean/QOU/ (AGENTS.md s0a candidate 2, no-shadowing-stub rule). So 'missing sibling' was a resolution non-issue for most. This bean: for each of the 14 (plus the 3 class-C/other), resolve lean.ref mechanically (sibling -> library path -> grep fallback), record: resolves? decl present by exact name? sorry-free? statement shape matches .md? Produce a table and a follow-up list of the genuinely unformalised ones.
