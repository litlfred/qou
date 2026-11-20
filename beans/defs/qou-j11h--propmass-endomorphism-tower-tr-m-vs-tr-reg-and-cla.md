---
# qou-j11h
title: 'prop:mass-endomorphism-tower: tr_M vs tr_reg, and classical vs q weights (from #2481)'
status: completed
type: task
created_at: 2026-11-17T23:08:24Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-d8c7
---

PR #2481 left open which trace (Markov tr_M or regular tr_reg) and which weights (w_lambda(1) or w_lambda(q)) the proposition means. Left: state it, check the Lean matches.

Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Answered on PR #8534 (commit ed979e1440). The producer `computations/habiro/habiro_exact_mass_endomorphism.py` uses the regular-representation reading of the descended term, with q-deformed `dim_q(λ)²/[3]_q!` weights (symmetric q-dimension, `dim_q((2,1)) = [2]_q`) divided by their sum. Not the classical `d_λ²/|S_3|` named in item (1) of the block's 2026-06-22 note. Recorded as a new 2026-11-20 authorNote on `mass-endomorphism-tower.ts`; this records what the code does and is not a ruling. Lean check: the sibling is trace- and weight-agnostic (`V i` is data). It summed the pair term over adjacent pairs only, against the .md and the producer (all `i<j`); fixed to all pairs. lean-direct exit 0, both theorems `[propext, Classical.choice, Quot.sound]`. Not fixed, from the 2026-11-15 sidecar review (`docs/audits/2026-11-15-sidecar-review-mass-theory/findings-batch-2.md`): `li2q_nonpos_on_neg` is assumed for every x ≥ 0, while the .md's own series has finite radius. Complete this bean when #8534 merges.

## 2026-11-20 — merged

PR #8534 rebase-merged as `18e2fdd441` (owner: "Auto prepare merge"); all 3 commits replayed. The open residue named above (`li2q_nonpos_on_neg` on all of [0, ∞)) is decision D1 on #8526.
