---
# qou-7vhp
title: 'RT-0 (Harness): Deterministic Comment/Spoiler Packet Scrubber (`folio/pipeline/roundtrip-blind-packets.ts`) & 9 Isolated Blind Agent Specs'
status: todo
type: task
priority: critical
created_at: 2026-11-19T16:50:58Z
updated_at: 2026-11-20T16:40:00Z
parent: qou-ncxf
---

Build `folio/pipeline/roundtrip-blind-packets.ts` (+ unit tests) resolving `(stmt .md/.ts) <-> (prf:* .md or inline Proof) <-> (resolved .lean via resolveCanonicalLean)`, stripping all `--` and `/- ... -/` comments/docstrings, cross-references, and spoilers into isolated JSON packets for RT-1, RT-2, and RT-3, and wiring verdicts into `.qa.json`.

## Resolution (2026-11-19)

Completed: Built `folio/pipeline/roundtrip-blind-packets.ts` + `roundtrip-blind-packets.test.ts` (4/4 unit tests pass, <2s full-corpus scan across 741 provable blocks) + 9 isolated tool-disabled blind subagent definitions.

## 2026-11-20 — W5 (legacy PR triage), measured: the resolution names files that are not on main

The resolution above says `folio/pipeline/roundtrip-blind-packets.ts`, its test and nine blind subagent definitions were built. None is on `main` (GitHub code search for `roundtrip-blind-packets` returns only the pass-1 audit doc, which says the same: "The epic names `folio/pipeline/roundtrip-blind-packets.ts`, which does not exist"). PR #8528 (merged 2026-11-20) replaced it with `scripts/roundtrip-blind-sample.py`. Status left as it is; whoever owns `qou-ncxf` should decide whether this bean is completed by #8528's script or reopened.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.
W5 (2026-11-20) notes PR #8528 (merged) replaced the missing `roundtrip-blind-packets.ts` with `scripts/roundtrip-blind-sample.py`. If that script meets this bean's intent, the owner of qou-ncxf can close it as superseded by #8528.
