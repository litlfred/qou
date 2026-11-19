---
# qou-9aar
title: 'V1 [QA Checkers & Claude QA Gate]: Tighten paper-commentary-audit.ts, qa-checkers-voice.ts & claude-redteam-and-qa.ts for L1-L4 Leaks'
status: todo
type: task
priority: high
tags:
    - voice-audit
    - fourth-wall-lean
    - qa-checkers
created_at: 2026-11-19T08:35:24Z
updated_at: 2026-11-19T08:35:24Z
parent: qou-d4kh
---

## Scope & Root Causes

Close the four automated checker gaps identified by `computations/audits/monograph_lean_and_voice_leak_audit.py` (`computations/audits/monograph-lean-and-voice-leak-audit.witness.json`) and coordinate deterministic regex checking with `scripts/claude-redteam-and-qa.ts qa-prose`:

1. **`folio/pipeline/paper-commentary-audit.ts` (Class L1 & L2):**
   - Remove the exemption in lines 11–12 (`"Naming the Lean declaration that states a result is fine; grading the Lean is not"`) and line 74 (`\bLean\s+(?:backing|carrier|sibling|file)\b[^.]{0,80}\b(?:does\s+not|doesn't|cannot)\b`).
   - Flag **all** prose mentions of `\bLean\b`, `Lean carrier`, `Lean sibling`, `Lean backing`, `Lean file`, `Lean module`, `Lean structure`, `Mathlib`, `proved formally`, `formally proved`, `formali[sz]ed in`, `discharges? the axiom`, and `## Lean structure` headers in reader-facing `.md` prose (where the $\forall$ badge and `.ts` `lean:` metadata are the sole formalization link).
2. **`folio-assistant/cat-harness-tools/pipeline/qa-checkers-voice.ts` (Class L2 & L3):**
   - **Pre-strip backtick scan (Class L2):** Before `scanProse` (line 180) and `stripInlineCode` (line 572) strip `` `...` `` spans, scan backticked tokens outside fenced code blocks for Lean FQNs (`` `QOU.Foo...` ``, `` `Mathlib...` ``), `.lean` filenames (`` `Foo.lean` ``), Lean typeclass/type expressions (`` `CommRing` ``, `` `IsQGeneric` ``, `` `HochschildZero R A` ``, `` `[Add H]` ``), raw block-ID backticks (`` `def:foo` ``), and Lean snake/camel declaration names (`` `dimQK0_eq_evDimQ_chernCharacter` ``, `` `su2Character_one` ``, `` `exteriorSquareDim_ne_zero_iff` ``).
   - **General first-person pronoun check (Class L3):** Extend `checkFirstPersonWork` / `checkScholarlyDefault` so general first-person plural (`we`, `our`, `us`, `let's`, `we're`, `we've`) and singular (`I`, `my`) in narrative `.md` prose are flagged (closing the gap that let `quantum-universe-axiom-motivation.md:5` and `axiom-independence.md:3` pass).
3. **Deterministic + Semantic LLM Gate (`scripts/claude-redteam-and-qa.ts qa-prose`) for Class L4 (Reading-Order Anachronisms):**
   - Add a deterministic Part-I reading-order checker for premature $q$ / $[n]_q$ / $\Phi_d(q)$ / Hecke / $\mathrm{SU}_q(2)$ / `"archimedean wall"` mentions in Chapter 1 (`quantum-universes/*.md`) and forward `](#label)` cross-references where `target_reading_index > source_reading_index`.
   - Extend `QA_PROSE_SYSTEM_RUBRIC` in `scripts/claude-redteam-and-qa.ts` with explicit Class L1–L4 criteria so `bun run scripts/claude-redteam-and-qa.ts qa-prose` (`ANTHROPIC_API_KEY` verified present in environment) provides semantic review for out-of-place passages such as `**On the substrate parameter.**` in `quantum-universes/quantum-universe.md:28-38`.

Cross-linked sibling bean: `qou-9iqh`.
