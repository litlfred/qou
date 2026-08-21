---
# qou-kkja
title: 'GAP: two batch rows need a §3b-cond model class, not a revert (shell_filling_lp_strong_duality, mobius limit_to_classical)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:16:32Z
updated_at: 2026-08-21T21:17:05Z
---

Opened by the sorry-closure honesty audit (PR #5411,
docs/audits/2026-08-21-sorry-closure-honesty-audit.md).

The audit graded 12 declarations from the 2026-08-21 batch. All 12 were
reverted, but TWO of them are not pure self-assuming projections and
deserve a better disposition than the honest `sorry` they were returned
to. Recording them so the revert is not mistaken for the final answer.

1. `QOU/Molecular/shell_filling_rule.lean :: shell_filling_lp_strong_duality`
   Verdict `genuine-composition`. The batch proof chained two fields by
   transitivity (`rw [ctx.strong_duality, ctx.dual_obj_eq]`) rather than
   projecting the conclusion. What it assumes is LP strong duality
   itself — a real, citable theorem ([bertsimas1997], ISBN
   9781886529199), not a framework-specific claim.

2. `QOU/BraidsKnots/mobius_frobenius_kernel.lean :: limit_to_classical`
   The field asserts a real `Filter.Tendsto` claim, so the class is
   content-bearing rather than empty. But paired with `K_classical_eq`
   it recomposes to exactly the conclusion, which is why it was graded
   `self-assuming-projection (2-field split)` and reverted.

WHY NOT FIXED IN #5411: the honest §3b-cond fix is a SEPARATE `extends`
model class carrying the named upstream hypothesis, with the theorem
deriving the conclusion from it. For (1) that cannot be done
file-locally — the same `ShellFillingRuleContext` also carries the two
self-assuming pairs for claims (i) and (ii), so splitting duality out
means restructuring the class. The audit brief forbids inventing a new
class to tidy a gap away, so this is queued rather than improvised.

TO RESTART COLD:
- Exemplar to copy: `QOU/FluidDynamics/q_bkm_criterion.lean` (verified,
  §3b-cond item 5 non-degenerate).
- Better in-file precedent: the `QTurbulenceCascadeModel` pattern that
  this same batch deleted and #5411 restored — one named physical
  hypothesis (Kolmogorov cutoff `q^N <= Re^(3/4)`), conclusion DERIVED by
  log algebra in `finite_cascade_depth_of_cutoff`. Read that file first.
- For (1): add `class ShellFillingLPDuality extends ShellFillingRuleContext`
  with the LP primal/dual feasibility data as fields and strong duality
  either cited or derived; name it `_of_` per Mathlib conditional-lemma
  convention. Keep claims (i) and (ii) on honest `sorry`.
- Acceptance test: the class must NOT be dischargeable by choosing values
  that make the conclusion true. If it is, it is still self-assuming.
- Note: no instance exists for ANY of the twelve context classes, so
  every downstream `[ctx]`-conditional theorem is currently vacuously
  conditional. A trivial instance would be worse (the qou-6dzi / PUnit
  defect) — do not add one to make the class look inhabited.
