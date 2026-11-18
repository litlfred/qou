---
# qou-ygyx
title: 'PROVE(lean): operator_selection_lp — theorem operator_selection_lp [ctx : OperatorSelectionLpContext] : OperatorSelectionLpCont [cited bertsimas1997,manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-bertsimas1997
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-11-18T07:49:45Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/operator_selection_lp.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean

### `operator_selection_lp`  —  line 99  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem operator_selection_lp [ctx : OperatorSelectionLpContext] : OperatorSelectionLpContext.IsFeasible ctx.x_star ∧ (∀ x : Fin ctx.d → ℝ, OperatorSelectionLpContext.IsFeasible x → OperatorSelectionLpContext.objective ctx.x_star ≤ OperatorSelectionLpContext.objective x) ∧ OperatorSelectionLpContext`
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
- **Tractability:** LP optimality of x_star (feasible + objective-minimising); LP optimality certificate, Mathlib lacks the duality library.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## RE-TRIAGED 2026-08-31 — NOT INFRA-BLOCKED — the class carries the conclusion

The `Next step` line above ("Infra-blocked: needs Mathlib theory that does not exist. Track
upstream") is one verdict that was stamped on fourteen beans in six seconds, and is wrong here.
Full audit: `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md`.

`operator_selection_lp` is `refine <ctx.x_star_feasible, ?_, ctx.zero_gap>` with the middle
conjunct discharged by `exact ctx.dual_bound_le_objective x hx`. All three conjuncts come from
class fields. The file docstring says the duality "is now **proved, sorry-free**"; that is true
of `#print axioms` and false of the mathematics.

Belongs to the qou-z9ws drain. Missed by BOTH scanners -- by the term-mode tool because the
proof is a tactic block (documented exclusion), and by
scripts/lean-self-assuming-tactic-mode-audit.py because `intro x hx` / `have hgap` introduce
locals, which that scanner's rule disqualifies.

The original text is kept above, not deleted: the Tractability line is per-item and is accurate;
only the Next-step verdict is being corrected.

## Round 83 Progress (PR #8392)
- Branch: `feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`
- Commit 1 (code + probe): `e226ba66ce53cea91430549ce1efc48cd1eeef24`
- Commit 2 (witness): `17c21a76b062fd76e16d4f84b23687e02fc0050c` (`scriptSha256 = 0635fcc96bfd3bd66e7452f9553ce1314e6829b0b1a6b7202ea86d48b4b232a6`)
