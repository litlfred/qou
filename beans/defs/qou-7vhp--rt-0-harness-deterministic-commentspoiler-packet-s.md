---
# qou-7vhp
title: 'RT-0 (Harness): Deterministic Comment/Spoiler Packet Scrubber (`folio/pipeline/roundtrip-blind-packets.ts`) & 9 Isolated Blind Agent Specs'
status: completed
type: task
priority: critical
created_at: 2026-11-19T16:50:58Z
updated_at: 2026-11-19T17:42:00Z
parent: qou-ncxf
---

Build `folio/pipeline/roundtrip-blind-packets.ts` (+ unit tests) resolving `(stmt .md/.ts) <-> (prf:* .md or inline Proof) <-> (resolved .lean via resolveCanonicalLean)`, stripping all `--` and `/- ... -/` comments/docstrings, cross-references, and spoilers into isolated JSON packets for RT-1, RT-2, and RT-3, and wiring verdicts into `.qa.json`.

## Resolution (2026-11-19)

Completed: Built `folio/pipeline/roundtrip-blind-packets.ts` + `roundtrip-blind-packets.test.ts` (4/4 unit tests pass, <2s full-corpus scan across 741 provable blocks) + 9 isolated tool-disabled blind subagent definitions.
