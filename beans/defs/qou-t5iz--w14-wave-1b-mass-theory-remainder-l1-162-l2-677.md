---
# qou-t5iz
title: 'W14 wave 1b: mass-theory remainder (L1 162, L2 677)'
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

Remaining `mass-theory` hits after waves A/B (PR #8588): L1 162 (mostly "the Lean sibling proves ..." sentences), L2 677 (declaration names 377-ish, FQNs, repository paths, block-ids whose link text step 1 skipped). Heaviest blocks: algebraic-geometric-dilog-equivalence, hecke-monodromy-step-two (prose outside the restated section), h3-frobenius-casimir-markov-trace-proof, order-of-magnitude-screen-proof, typed-b3-sub-braid-extraction, isospin-mass-split-em-localisation, hecke-radical-is-temperley-lieb, cellular-depth-filtration-proof, plancherel-term-7-formulation, canonical-trace-factorises-over-chain.

How (house style, set by PRs #8577, #8584, #8588): restate every "the Lean sibling proves X" as X with its mathematical reason; move declaration names, file names and class names to the block's `.ts` `lean` / `authorNotes`; a sentence carrying a real scope caveat ("Lean checks this only through ...", "the class has no instance", "by rfl against the inline value") is RESTATED in mathematical terms (hypothesis not proved / holds by definition / conditional on), never deleted; "we" becomes impersonal without changing meaning; repository paths in prose become link text naming what the file holds. One PR per chapter or small group; run `bun run folio/pipeline/voice-leak-ratchet.ts --shrink` (step 5, PR #8585) and commit the smaller baseline with the drain. Render-QA every math-bearing block. Owner ruling 2026-11-20, #8526 comment 7041693067 (W14 options 3+4).

Counts (W14b stack; re-measure on W14 #8566/#8569 once merged, which already cover part of this) are failing hits of `voice-leak-audit.ts` measured 2026-11-20 on branch `claude/voice-leak-wave-mass-theory-2026-11-20` (main 423c7a0a7 + step-1 link-text fix + mass-theory waves A/B); re-measure before starting.

Created by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws).
