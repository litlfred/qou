---
# qou-lrz1
title: 'B2c: H_n(q) is fin-dim K-algebra, dim = n! (basis {T_w : w∈S_n}). [track2]'
status: completed
type: task
priority: normal
created_at: 2026-07-24T16:34:39Z
updated_at: 2026-08-30T07:56:21Z
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

## 2026-08-29 — THE BRIDGE IS COMPLETE

permCoxeterSystem n : CoxeterSystem (Aₙ n) (Equiv.Perm (Fin (n+1))), plus the
IsCoxeterGroup instance. **S_{n+1} IS the Coxeter group of type Aₙ, formalized**,
sorry-free at general n, all declarations #print axioms clean.

Route: s_rel (all three relation families) -> toPerm -> toPerm_surjective (via
Mathlib's mclosure_swap_castSucc_succ) -> the four coset-closure cases
(t_mul_gen_self / t_mul_gen_pred / t_comm / t_push) -> inCosets_all (every element
in one of n+2 parabolic cosets, by simple_induction_right) -> cover_surjective ->
finiteAn + card_An_le (|W(Aₙ n)| <= (n+1)!, induction from the trivial W(Aₙ 0))
-> toPerm_bijective by the cardinality squeeze against |S_{n+1}| = (n+1)!.

**Mathlib does not have this.** Measured before starting: the only CoxeterSystem
values in all of Mathlib are the tautological CoxeterMatrix.toCoxeterSystem and
CoxeterSystem.map (transport along an existing MulEquiv), and there are ZERO
IsCoxeterGroup instances -- the whole theory with no concrete group plugged in.

Consequence: cs.length and all of Coxeter/Length.lean and Coxeter/Inversion.lean
now apply to Equiv.Perm. That is exactly the length theory AGENTS.md records as
missing for Equiv.Perm, and it is what T_w well-definedness rests on. qou-twwf is
now unblocked.


## 2026-08-30 — CLOSED, merged to main as 9c7211676c (PR #6053)

`QOU.Hecke.TwBasis.basisTwOfField` is a genuine
`Module.Basis (Equiv.Perm (Fin (n+1))) K (IwahoriHecke K q n)` with
`coe = Tw`, and `finrank_eq_factorial : dim_K H_n(q) = (n+1)!`.  Sorry-free at
general `n`, over a field.  Matsumoto never used — see `qou-twwf` for why.
