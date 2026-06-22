---
# 8ehe
title: Resolve 5 placeholders/TODOs in qou/lean/MathlibExt
status: in-progress
type: task
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-22T13:55:39Z
---

## Progress (2026-06-22, branch claude/epic-wright-b147hr)

- **Scratch.lean — `quadratic_form_two_index_proof` sorry RESOLVED** (sorry-free,
  lean-direct EXIT=0). The pre-existing proof did not even compile (`hH j i` applied
  `IsHermitian` as a function); rewrote it: Hermitian symmetry via
  `congrFun (congrFun hH i) j` + `conjTranspose_apply`, then the quadratic form by
  unfolding `dotProduct`/`mulVec` to Finset sums and collapsing the `Pi.single`
  supports with `Finset.sum_ite_eq'` + `ring`. (The identity in fact holds for `i=j`
  too, so the `i ≠ j` hypothesis is now `_hij`.)
  NOTE: `Scratch.lean` is **unwired** (not imported in `QOU.lean`, no `.ts`/`.md`
  siblings) and its target lemma `pos_semidef_diag_zero` is already proven in
  `PosSemidefDiagZero.lean` — flagged for owner: rehome the now-proven lemma or delete
  the scratch file.

- **Remaining MathlibExt sorries** (not touched — correctly deferred): the 9 in
  `SDPRealUniqueness.lean` are Goldman–Tucker / strict-complementarity content with
  `[manuscript]` + Boyd–Vandenberghe refs (genuine multi-week categorical work, not a
  mechanical close). `SDPRankEquality.lean` is already sorry-free (its grep "2 sorry"
  were the words "sub-sorries" in a docstring).

