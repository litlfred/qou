---
# qou-kzo1
title: 10 more context-class sorries unswept — same shape as the 8 already refuted
status: todo
type: task
created_at: 2026-08-09T10:50:57Z
updated_at: 2026-08-09T10:50:57Z
---


Eight context-class `sorry`s in the newly-visible set were swept in qou-octr and
**all eight were refutable** — none was an open gap. These ten are the same
shape and have not been attempted:

| theorem | class |
|---|---|
| `mobius_frobenius_kernel` | `MobiusFrobeniusKernelContext` |
| `nsi_q_kernel_identification` | `NsiQDeformedKernelContext` |
| `states` | `QNsWellposednessContext` |
| `scalar_channel_ordering_independent` | `NucleonOrderingFactorizationContext` |
| `shell_filling_inner_shells` | `ShellFillingRuleContext` |
| `shell_filling_hund_rule` | `ShellFillingRuleContext` |
| `shell_filling_lp_strong_duality` | `ShellFillingRuleContext` |
| `four_term_pair_nucleon_counts` | `FourTermPairNucleonContext` |
| `operator_selection_lp` | `OperatorSelectionLpContext` |
| `confinement_categorical` | `ConfinementCategoricalContext` |

Spot-checked two while classifying and both look identical to the refuted set —
`shell_filling_inner_shells` asserts `occupancy n = capacity n` over two free
class fields, `shell_filling_hund_rule` asserts `singly c ≤ singly ground` over
another two.

## Method (about two minutes each)

Construct an instance filling every field, choosing values that disagree, and
prove the negation:

```lean
theorem <name>_unconstrained_false :
    ¬ ∀ ctx : <Context>, <the conclusion> := by
  intro h
  have := h { …every field, numbers picked to disagree… }
  norm_num at this
```

Worked examples for all eight: `docs/audits/2026-08-09-unclosable-context-sorries.lean.txt`,
and each now sits next to the theorem it refutes.

**Do not grep for this.** Two syntactic proxies were tried in qou-octr and both
failed — the property is "do the class's hypotheses constrain the fields the
conclusion names", which is not a pattern. Build the instance.

Whatever the outcome, record it: a statement that survives the attempt is
evidence *for* it, which is how `covariance_kernel_conjecture` was cleared.
