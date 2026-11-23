---
# qou-mr7s
title: 'EPIC [Q-Drain-10]: Exposition, Milnor Voice Ratchet, Liquid :val Wiring & Citation/Library Sweeps'
status: todo
type: epic
priority: high
created_at: 2026-11-23T20:55:51Z
updated_at: 2026-11-23T20:55:51Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Exposition, Milnor Voice Ratchet, Liquid :val Wiring & Citation/Library Sweeps
**Rationale:** Drains remaining voice-branch-jargon blocks (after #9202), resolves missing bibliography/library citations, and wires :val[...] witnesses.
**Child Beans (14):** `qou-vbjg`, `qou-x4nh`, `qou-mlnr`, `qou-9aar`, `qou-6bla`, `qou-lm62`, `qou-cite`, `qou-2hc7`, `qou-g71v`, `qou-hfwb`, `qou-iryu`, `qou-h59j`, `qou-h1lc`, `qou-7p89`

### Prioritized Beans in This Batch
- **`qou-vbjg`** (`high`, `todo`) — One-voice remediation: 386 blocks fail voice-branch-jargon *(Rule 13a: 0-instance classes: `BindingPerRepReebPhase, CFromColorFlavorSwap, CPTClosure`)*
- **`qou-x4nh`** (`high`, `todo`) — V2 [Part I Foundations Drain]: Fix All L1-L4 Lean, Voice & Anachronism Leaks in Ch 1 (quantum-universes) & Ch 2 (quantum-observable-universes) *(Rule 13a: 0-instance classes: `IsQGeneric`)*
- **`qou-mlnr`** (`high`, `todo`) — Milnor exposition drain — whole-paper H1–H8 audit+resolve (expo-milnor-clarity) + milnor-brevity
- **`qou-9aar`** (`high`, `in-progress`) — V1 [QA Checkers & Claude QA Gate]: Tighten paper-commentary-audit.ts, qa-checkers-voice.ts & claude-redteam-and-qa.ts for L1-L4 Leaks *(Rule 13a: 0-instance classes: `IsQGeneric`)*
- **`qou-6bla`** (`high`, `todo`) — One notation per object — consolidate the ℏ_q spelling family; the q-integer split is the literature carve-out
- **`qou-lm62`** (`high`, `todo`) — GS-1: Monograph overhaul on current rulings (front matter, knot periodic table, glossary, block audit) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-cite`** (`high`, `todo`) — 13 citations point at bibliography entries that do not exist — the check had never run
- **`qou-2hc7`** (`high`, `todo`) — CITE: Thurston GT3M is held as a 33-page Ch.1-2 excerpt — M — 113 citers, several at Ch.4 / §4.5 gluing equations *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-g71v`** (`high`, `todo`) — CITE: Murakami-Murakami 2001 (Acta Math. 186) is not held — U — 63 citers, the volume conjecture''s founding statement
- **`qou-hfwb`** (`high`, `todo`) — CITE: Woronowicz''s differential-calculus papers are not held and the 4D bicovariant classification carries no Ref key — U+C — CalculusDimensionObstruction.lean:89-94, SelfDualityDegree.lean:89-90
- **`qou-iryu`** (`high`, `todo`) — CITE: no CR / contact / Sasakian source is held OR registered — U — 34 content files, 10 uncited blocks, ContactDistributionRank.lean:91
- **`qou-h59j`** (`high`, `todo`) — VS-1 (Pipeline): Subdirectory Witness Resolution in liquid-values.ts, :val[...] Markdown Site Rendering, and ValueRegistry Repair
- **`qou-h1lc`** (`high`, `todo`) — Fix High-Impact Wrong-Edition & Stale Prose Blocks via Liquid Variable Substitution
- **`qou-7p89`** (`high`, `todo`) — VS-3 (P1 Dashboards & Status Docs): Wire Live Wave-2 Compute and Liquid Variable Substitution Across Status Scorecards & Appendix Dashboards

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
