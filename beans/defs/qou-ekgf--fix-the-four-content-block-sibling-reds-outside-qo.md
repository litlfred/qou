---
# qou-ekgf
title: fix the four content-block sibling reds outside qou-e7xv's sweep (confinement-level-exists, euler-char-stability, localized-knot, qz-bicompletion)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T20:48:19Z
updated_at: 2026-10-04T15:12:36Z
parent: qou-5vkl
---

Owner 'merge and go' after #6674 (qou-n9j7) landed; my stated judgement was this tranche next. The four files were last touched 2026-08-14 and are red on main because a library declaration each references has moved or vanished (confinement-level-exists → QOU.BraidKnot.ConfinementLevel.exists; localized-knot → QOU.KnotTheory.BraidWord.writhe; qz-bicompletion → zPochhammer) or Mathlib API drift (euler-char-stability: binder type inference at :25). Discipline: mechanical re-pointing only where the library carries the same object under a new name, verified lean-direct with the full cone; anything needing a new proof or a weakened statement is a bean, not a fix. Tracked also on qou-isps (which stays for qou-0xrn).



## 2026-09-04 21:0xZ — three of four resolved; the fourth is a real gap; and a recipe defect found
- confinement-level-exists: library theorem renamed exists → nonempty; sibling + lean.ref re-pointed (green).
- euler-char-stability: two untyped ∀ n binders (green).
- localized-knot: NO source change needed — BraidWord.writhe IS in the library (KnotTheory.lean:86); the cached QOU.KnotTheory olean was stale with a fresh mtime, so the mtime-based dirty closure skipped it. Rebuilt → green. Harness red, misfiled as real on qou-isps; corrected there.
- qz-bicompletion: REAL — zPochhammer (the P_n(q,z) generator of I_{m,n}) is defined nowhere in tracked history and the .md only names it. Not invented here; stays open (qou-isps).
Recipe correction recorded in the lean-verifier memory; seed-commit closure (1,494 modules) re-running in the background to re-establish the library claim honestly.



## 2026-09-05 00:5xZ — the seed-closure rebuild finished: 1,495/1,497, one real red (qou-4a7a), one harness (UGB path, script fixed). Nothing further to fix on this branch; the two remaining sibling reds are qz-bicompletion (never-defined generator) and qou-0xrn.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
