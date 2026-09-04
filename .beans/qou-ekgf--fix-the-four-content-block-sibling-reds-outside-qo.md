---
# qou-ekgf
title: fix the four content-block sibling reds outside qou-e7xv's sweep (confinement-level-exists, euler-char-stability, localized-knot, qz-bicompletion)
status: in-progress
type: task
created_at: 2026-09-04T20:48:19Z
updated_at: 2026-09-04T20:48:19Z
---

Owner 'merge and go' after #6674 (qou-n9j7) landed; my stated judgement was this tranche next. The four files were last touched 2026-08-14 and are red on main because a library declaration each references has moved or vanished (confinement-level-exists → QOU.BraidKnot.ConfinementLevel.exists; localized-knot → QOU.KnotTheory.BraidWord.writhe; qz-bicompletion → zPochhammer) or Mathlib API drift (euler-char-stability: binder type inference at :25). Discipline: mechanical re-pointing only where the library carries the same object under a new name, verified lean-direct with the full cone; anything needing a new proof or a weakened statement is a bean, not a fix. Tracked also on qou-isps (which stays for qou-0xrn).
