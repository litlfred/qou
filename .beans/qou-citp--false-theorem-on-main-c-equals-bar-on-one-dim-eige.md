---
# qou-citp
title: 'FALSE THEOREM on main: c_equals_bar_on_one_dim_eigenvalue_neg_q_inv is false (-3q = q); Z toy encoding conflates the two Hecke eigenvalues'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:24:54Z
updated_at: 2026-08-21T21:25:39Z
---

Found while draining the small-category vacuity tranche (qou-h3ly) in PR #5408 — NOT one of the 22 ledger defects; a separate, worse problem in the same file.

**The file did not compile on main.** `git show origin/main:...c-equals-bar-iff-all-1dim.lean` + lean-direct gives **5 errors**, all pre-existing. Four were tactic failures (`omega` cannot see `Nat.factorial` or `^`) and were repaired in #5408:
- `h2_all_one_dim`, `h3_has_multidim` -> `decide`
- `two_only_unit_squares` -> bound `a,b <= 1` by `nlinarith`, then `omega`
- `factorial_exceeds_two_squares` -> `Nat.factorial_le hn` + `3! = 6`

**The fifth is a false statement.** `c_equals_bar_on_one_dim_eigenvalue_neg_q_inv (q h : ℤ) (hdef : h = q - (-q)) : (-q) - h = q`. From `hdef`, `h = 2q`; LHS `= -3q`; `-3q = q` iff `q = 0`. False for every non-zero q. Removed with the arithmetic recorded at the site (not weakened — Strict Lean Discipline §10).

**Root cause is the model.** The file encodes multiplicative Hecke eigenvalues additively over ℤ with `q⁻¹` as `-q`. Then `q` and `-q⁻¹` BOTH map to `q`, so the second eigenvalue case is not expressible as a claim distinct from the first. No sign fix works.

**Real fix:** restate both eigenvalue cases in the genuine multiplicative setting — `q : Rˣ` over `[CommRing R]`, as `mass-theory/meson-kaon-pion-hecke-seifert.lean` does with `chi_21` — and derive `C = bar` on the two eigenvalues `{q, -q⁻¹}` there. Then re-check whether the surviving `_eigenvalue_q` companion is saying what it appears to.

**Wider signal:** a content-block Lean sibling sat broken on main with 5 errors. Nothing caught it — library/sibling Lean has no `.qa.json` and CI is dispatch-only, so per AGENTS 'QA is agent-owned' this is exactly the class the agent-side gate exists to catch.
