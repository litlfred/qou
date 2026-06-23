---
# 8ehe
title: Resolve 5 placeholders/TODOs in qou/lean/MathlibExt
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-23T12:55:00Z
---

RESOLVED 2026-06-23 (#2637): the lone actionable item was a compile breakage
in QOU/MathlibExt/SDPRankEquality.lean (6 errors, not a cosmetic TODO). All
fixed + lean-direct-verified green (EXIT=0): mulVec_mulVec direction;
mulVec_transpose vecMul form; + added the missing Matrix.rank_eq_finrank_range_toLin'
shim (real Mathlib lemma is basis-general, no prime — found via GitHub
code-search). CI Lean build to confirm. See
docs/audits/2026-06-23-sdprankequality-broken-on-main.md.


resweep 2026-06-22: honest counter = 1 actionable (claimed 5) via scripts/count-actionable-placeholders.ts.

triage 2026-06-23 (idle-backlog-drain): the "1 actionable" is NOT a cosmetic
TODO — it sits on `QOU/MathlibExt/SDPRankEquality.lean`, which **fails to
compile on main** (6 errors, lean-direct verified against lake-cache/qou-v4-24-0).
Two errors fixed + verified (mulVec_mulVec direction; mulVec_transpose vecMul
form); blocker = unknown constant `Matrix.rank_eq_finrank_range_toLin'` (×6),
needs a Mathlib lemma lookup (LSP/search MCP was down this session). Full
diagnosis + verbatim fixes: docs/audits/2026-06-23-sdprankequality-broken-on-main.md.
Un-claimed (todo) — needs an LSP-equipped session to finish.
