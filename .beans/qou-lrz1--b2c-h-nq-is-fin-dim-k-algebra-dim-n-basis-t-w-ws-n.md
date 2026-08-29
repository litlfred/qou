---
# qou-lrz1
title: 'B2c: H_n(q) is fin-dim K-algebra, dim = n! (basis {T_w : w∈S_n}). [track2]'
status: in-progress
type: task
priority: normal
created_at: 2026-07-24T16:34:39Z
updated_at: 2026-08-29T18:33:38Z
---

## 2026-08-29 — the surjective half of the Sn <-> type-A bridge is BUILT

New: content/quantum-observable-universe/lean/QOU/Hecke/SymmetricCoxeter.lean
(sorry-free, all general n, lean-direct exit 0, 7/7 #print axioms clean).

**The standing audits are stale on what Mathlib has.** The 2026-08-21 TL_n audit
lists build item 1 as 'S_n as a Coxeter group of type A -- absent', and AGENTS.md
says 'Equiv.Perm has no length/inversions'. Measured:
  PRESENT: CoxeterMatrix.Aₙ, the whole CoxeterSystem API (Basic/Length/Inversion/
  Matrix) including length, and Equiv.Perm.mclosure_swap_castSucc_succ.
  ABSENT: any link between Equiv.Perm and CoxeterMatrix.Aₙ (grep for Equiv.Perm
  across GroupTheory/Coxeter/ returns nothing).
So the gap is the BRIDGE, not the Coxeter theory.

Proved: swap_braid_pow_three, swap_disjoint_pow_two (general DecidableEq type);
s n i (adjacent transposition); **s_rel** -- all three type-Aₙ relation families
verified against the actual CoxeterMatrix.Aₙ entries; toPerm : (Aₙ n).Group →*
Perm (Fin (n+1)); toPerm_simple; **toPerm_surjective**.

## The remaining half, precisely

CoxeterSystem M W is a structure carrying a MulEquiv W ≃* M.Group
(Coxeter/Basic.lean:154). So it needs toPerm **injective** too, i.e. the
presentation imposes no relations beyond the three families, i.e.
|(Aₙ n).Group| <= (n+1)!. That is the classical hard half of the presentation
theorem for S_n (length/exchange or the geometric representation). Nothing in
this file bears on it.

Scope-(a): a statement about what this file does, NOT a claim that injectivity
is hard in principle or blocked. No invariant forbids it.
