---
# qou-a1k9
title: 'W14 wave 2: mass chapters (predicted-spectra, mass-endomorphism, stochastic-mechanics, climax-volume-mass, appendix-mass-binding-algorithms)'
status: todo
type: task
priority: normal
tags:
    - voice-audit
    - fourth-wall-lean
created_at: 2026-11-20T17:30:00Z
updated_at: 2026-11-20T17:30:00Z
parent: qou-d4kh
---

Chapters and counts (L1/L2/L3): predicted-spectra 78/249/123; mass-endomorphism 51/263/86; stochastic-mechanics 79/138/11; climax-volume-mass 5/24/22; appendix-mass-binding-algorithms 6/139/4 (its alg: blocks are a maintenance contract with the Python API, AGENTS.md "Mass-and-Binding-Algorithms appendix sync" -- keep the API pointers in authorNotes or the .ts `computation` field, do not drop them). predicted-spectra holds data tables that are Lean maps (e.g. upstream-mathlib-additions-table1-data): move to authorNotes or ask before dropping.

How (house style, set by PRs #8577, #8584, #8588): restate every "the Lean sibling proves X" as X with its mathematical reason; move declaration names, file names and class names to the block's `.ts` `lean` / `authorNotes`; a sentence carrying a real scope caveat ("Lean checks this only through ...", "the class has no instance", "by rfl against the inline value") is RESTATED in mathematical terms (hypothesis not proved / holds by definition / conditional on), never deleted; "we" becomes impersonal without changing meaning; repository paths in prose become link text naming what the file holds. One PR per chapter or small group; run `bun run folio/pipeline/voice-leak-ratchet.ts --shrink` (step 5, PR #8585) and commit the smaller baseline with the drain. Render-QA every math-bearing block. Owner ruling 2026-11-20, #8526 comment 7041693067 (W14 options 3+4).

Counts (W14b stack; re-measure on W14 #8566/#8569 once merged, which already cover part of this) are failing hits of `voice-leak-audit.ts` measured 2026-11-20 on branch `claude/voice-leak-wave-mass-theory-2026-11-20` (main 423c7a0a7 + step-1 link-text fix + mass-theory waves A/B); re-measure before starting.

Created by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws).
