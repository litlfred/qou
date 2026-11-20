---
# qou-rfp0
title: 'W14 wave 3: physics chapters (information-theory, observations, lifting-and-descent, knots-particles-confinement, nuclear-interactions, fluid-dynamics, brings-surface, braids-and-knots, eightfold-way)'
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

Chapters and counts (L1/L2/L3): information-theory 18/79/101; observations 11/57/96; lifting-and-descent 3/6/94; knots-particles-confinement 7/46/50; nuclear-interactions 7/34/59; fluid-dynamics 5/53/42; brings-surface 11/68/40; braids-and-knots 45/53/18; eightfold-way 32/110/2. observations is the empirical-comparison chapter: L3 there includes "our universe" / "our location" phrasing, restate as "the observed universe" / "the point of observation" as in Ch2 (PR #8577).

How (house style, set by PRs #8577, #8584, #8588): restate every "the Lean sibling proves X" as X with its mathematical reason; move declaration names, file names and class names to the block's `.ts` `lean` / `authorNotes`; a sentence carrying a real scope caveat ("Lean checks this only through ...", "the class has no instance", "by rfl against the inline value") is RESTATED in mathematical terms (hypothesis not proved / holds by definition / conditional on), never deleted; "we" becomes impersonal without changing meaning; repository paths in prose become link text naming what the file holds. One PR per chapter or small group; run `bun run folio/pipeline/voice-leak-ratchet.ts --shrink` (step 5, PR #8585) and commit the smaller baseline with the drain. Render-QA every math-bearing block. Owner ruling 2026-11-20, #8526 comment 7041693067 (W14 options 3+4).

Counts (W14b stack; re-measure on W14 #8566/#8569 once merged, which already cover part of this) are failing hits of `voice-leak-audit.ts` measured 2026-11-20 on branch `claude/voice-leak-wave-mass-theory-2026-11-20` (main 423c7a0a7 + step-1 link-text fix + mass-theory waves A/B); re-measure before starting.

Created by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws).
