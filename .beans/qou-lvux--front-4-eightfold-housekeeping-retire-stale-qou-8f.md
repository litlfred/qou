---
# qou-lvux
title: 'Front 4: eightfold housekeeping — retire stale qou-8fl1 items, fix cheat-sheet 4-C title, Sym2Gate vacuity'
status: todo
type: task
created_at: 2026-09-03T04:37:54Z
updated_at: 2026-09-03T04:37:54Z
parent: qou-icj2
---


## DONE 2026-09-03 (PR #6458) — all three housekeeping targets closed

- qou-8fl1 items 1, 2, 5 retired by re-measurement (commit ab3decad); items 6, 7
  remain research-gated.
- Cheat-sheet 4-C heading retitled to match its own banner (ab3decad).
- Sym2Gate.lean RETIRED (this commit): its three theorems were arithmetic
  tautologies (3*4/2 = 6; 1+5 = 6 ∧ 1 ≥ 1; 6 = 6 ∧ 0 < 1) carrying content only
  in their names (Strict Lean Discipline item 5). prop:color-su3-from-g2 lean.ref
  now → Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three; the three prose
  sites (schur-weyl-eightfold ×2, open-problems ledger rows 19/30 + item 1) and
  the definition index repointed; nothing imported the file. Both blocks
  render-checked (markdownToLatex + validateLatexAst) and qa-swept.
