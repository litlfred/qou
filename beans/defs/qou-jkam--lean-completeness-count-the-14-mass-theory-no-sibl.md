---
# qou-jkam
title: 'lean-completeness: count the 14 mass-theory ''no sibling .lean'' blocks by lean.ref RESOLUTION, not sibling presence'
status: completed
type: task
priority: normal
created_at: 2026-09-04T02:14:49Z
updated_at: 2026-09-04T02:53:42Z
---

Owner pick 2026-09-04 (option 2 of the qou-zmuu close-out). The wall-side re-adjudication (#6529) found that of 14 mass-theory blocks whose 2026-07-07 QA fail said 'sibling Lean file is missing', at least 11 have a .ts lean.ref that RESOLVES to a library declaration under lean/QOU/ (AGENTS.md s0a candidate 2, no-shadowing-stub rule). So 'missing sibling' was a resolution non-issue for most. This bean: for each of the 14 (plus the 3 class-C/other), resolve lean.ref mechanically (sibling -> library path -> grep fallback), record: resolves? decl present by exact name? sorry-free? statement shape matches .md? Produce a table and a follow-up list of the genuinely unformalised ones.



RESULT 2026-09-04 (branch claude/lean-ref-resolution-qvalue-2026-09-04, PR #6554): 17/17 resolve to an existing declaration; 0/17 proof sorries in the resolved files (comments stripped — my first per-file counts 13/7/7/5/2/2/1 were docstring mentions, corrected). So by RESOLUTION the mass-theory count is 15/15 present, 0 missing. Five rows resolve to a decl that is NOT the block's claim: content-scaling-correspondence (BoxContent.lean has no theorem at all — the one genuinely unformalised proposition), feynman-categorical-trace (claim is a structure field), feynman-markov-identification (theorem projects its premise), hadron-half-life and skein-mass-from-linking (proposition/lemma refs naming a def). Both definitions in the set (q-reeb-flow, q-value-transition) have a sibling WITHOUT the ref's decl plus a library file WITH it. Audit: docs/audits/2026-09-04-lean-ref-resolution-count-mass-theory.md (options A-D, recommendation C now / B as its own bean).
