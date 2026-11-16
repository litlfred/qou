---
# qou-vs2i
title: 'PROVE(lean): shell_filling_rule.lean — 3 cited sorries [cited bertsimas1997,manuscript]'
status: in-progress
pr: 8216
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - repo-infra
    - cite-bertsimas1997
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-10-04T15:22:45Z
parent: qou-wp6m
---

**File:** `QOU/Molecular/shell_filling_rule.lean` (QOU)  ·  3 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean

### `shell_filling_inner_shells`  —  line 93  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext] : ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
- **Tractability:** Inner shells fully occupied (occupancy = capacity below valence); combinatorial over context class.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `shell_filling_hund_rule`  —  line 104  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext] : ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
- **Tractability:** Hund's rule maximises singly-occupied orbitals; combinatorial optimisation over context.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `shell_filling_lp_strong_duality`  —  line 115  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext] : ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 `
- **Cited:** `[bertsimas1997]`, `[manuscript]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
- **Tractability:** LP strong duality primal_obj = Z·y_0 for the shell-filling LP; needs LP strong-duality library Mathlib lacks.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

## Progress (2026-11-16, PR #8216)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/HyperchargeWritheRotationJordanGlobalGroupOctonionAndShellFilling.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`4e815f9543024d961ef648f5d19347ad79739059`, `scriptHash: 34801c11045c`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8216`
