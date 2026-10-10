---
# aj81
title: Resolve 5 placeholders/TODOs in qou/stochastic-mechanics
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-06-22T13:13:01Z
---

Audit (claude/amazing-mendel-k950fh): the 5 grep 'markers' were mostly false positives — matches on the phrase 'sorry-free', .qa.json reviewer notes, and two LEGITIMATE §3b conjecture-class sorrys (reverse-limit-q-to-infinity, lusztig-canonical-basis-q-eq-1) that must be retained. One genuine residual: lusztig lean.ref was already aligned in the .ts (QEqOne->QEq1, discharging proof-integration-watcher-queue #444), but the .lean header docstrings (x4) and definition-index.md cell still read QEqOne. Fixed both -> consistent with the declared class LusztigCanonicalBasisQEq1. NOTE: computations/audits/lean-ref-resolution-audit.witness.json still records the stale QEqOne ref; regenerate via CI/platform-enabled session. Compiled Lean byte-identical (comment-only).
