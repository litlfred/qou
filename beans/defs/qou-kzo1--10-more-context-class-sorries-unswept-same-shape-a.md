---
# qou-kzo1
title: 10 more context-class sorries unswept — same shape as the 8 already refuted
status: completed
type: task
priority: normal
created_at: 2026-08-09T10:50:57Z
updated_at: 2026-09-26T11:03:18Z
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

---

## Swept 2026-08-09 — 5 more refuted, running total 13 of 13

| theorem | verdict | refuted by |
|---|---|---|
| `shell_filling_inner_shells` | REFUTED | `n_val := 2`, empty shells; class gives `≤`, theorem asserts `=` |
| `shell_filling_hund_rule` | REFUTED | `ValenceConfig := Bool`, ground the *less* singly-occupied one |
| `shell_filling_lp_strong_duality` | REFUTED | `Z := 0, y_0 := 0, primal_obj := 1` |
| `mobius_frobenius_kernel` | REFUTED | `K_FH ≡ 0`; limit `0` vs claimed `1/‖γs−γt‖² = 1` |
| `operator_selection_lp` | REFUTED | `d := 0`: empty-sum objective vs `n_target * y_0_star` |
| `scalar_channel_ordering_independent` | **not a gap** | already proved: `(hperm.map f).prod_eq` |

### Two things this round changed about the finding

**1. Carrying hypotheses is not enough.** `ShellFillingRuleContext` is *not* a
bare-data class — it carries `capacity_def : ∀ n, capacity n = 2*n²` and
`occupancy_le_capacity : ∀ n, occupancy n ≤ capacity n`. It is still refutable,
because the theorem asserts `occupancy n = capacity n` and the class only
bounds it. The criterion is not "does the class have hypotheses" but "are they
strong enough for the conclusion" — which kills the last syntactic proxy I had
for detecting this cheaply.

**2. It is not confined to arithmetic.** `mobius_frobenius_kernel` asserts a
*limit* (`Tendsto … (nhds (1/‖γs−γt‖²))`) over a free kernel field, and falls
the same way — set `K_FH ≡ 0` and use uniqueness of limits in a `NeBot` filter.
Analysis statements are not safer.

### One correction

`scalar_channel_ordering_independent` was on this list in error — my extractor
matched a neighbouring declaration. It is proved, sorry-free, and always was.

### Not attempted (3)

- `nsi_q_kernel_identification` — same shape, needs `qDeformedKernel`'s value.
- `four_term_pair_nucleon_counts`
- `confinement_categorical` — extends `QOU.Shared.MarkovTraceContext`, so the
  instance needs the parent's fields too; more construction work, no reason to
  expect a different answer.

`operator_selection_lp`'s refutation is in
`docs/audits/2026-08-09-unclosable-context-sorries.lean.txt` but **not** in the
source file: that module imports only `Algebra.Order.Ring.Defs` and
`Fintype.Fin`, so neither `ℝ` nor `ℤ`'s ordered-ring instances are in scope, and
widening a substrate-side module's imports for an audit artefact risks the
`wall-side-correct` criterion. Left out deliberately.
