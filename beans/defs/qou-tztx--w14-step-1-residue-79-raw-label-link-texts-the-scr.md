---
# qou-tztx
title: 'W14 step-1 residue: 79 raw-label link texts the script skipped'
status: completed
type: task
priority: normal
tags:
    - voice-audit
    - fourth-wall-lean
created_at: 2026-11-20T17:30:00Z
updated_at: 2026-11-20T18:55:00Z
parent: qou-d4kh
---

scripts/voice-link-text-from-title.py (PR #8584) skipped: 28 titles over 110 characters with no cut point; 23 titles containing | [ ] or a backtick; 18 titles that themselves name Lean/Mathlib (using them would trade L2 for L1 -- consider retitling those blocks, which is itself a voice fix); 5 labels with no title. Re-run the script in dry mode to list them; fix by hand with a short descriptive text.

How (house style, set by PRs #8577, #8584, #8588): restate every "the Lean sibling proves X" as X with its mathematical reason; move declaration names, file names and class names to the block's `.ts` `lean` / `authorNotes`; a sentence carrying a real scope caveat ("Lean checks this only through ...", "the class has no instance", "by rfl against the inline value") is RESTATED in mathematical terms (hypothesis not proved / holds by definition / conditional on), never deleted; "we" becomes impersonal without changing meaning; repository paths in prose become link text naming what the file holds. One PR per chapter or small group; run `bun run folio/pipeline/voice-leak-ratchet.ts --shrink` (step 5, PR #8585) and commit the smaller baseline with the drain. Render-QA every math-bearing block. Owner ruling 2026-11-20, #8526 comment 7041693067 (W14 options 3+4).

Counts (W14b stack; re-measure on W14 #8566/#8569 once merged, which already cover part of this) are failing hits of `voice-leak-audit.ts` measured 2026-11-20 on branch `claude/voice-leak-wave-mass-theory-2026-11-20` (main 423c7a0a7 + step-1 link-text fix + mass-theory waves A/B); re-measure before starting.

Created by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws).

## 2026-11-20 — completed by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws)
PR #8640 merged (8313caeb3): the last 42 raw-label link texts on main got hand-written short titles (19 labels). Paper-wide L2 block-id 42 -> 0. Mechanical task, no open conjecture.
