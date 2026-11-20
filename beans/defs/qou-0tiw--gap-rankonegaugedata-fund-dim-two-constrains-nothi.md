---
# qou-0tiw
title: 'GAP: RankOneGaugeData fund_dim_two constrains nothing -- circular with SpinDecomposition'
status: todo
pr: 8209
type: task
priority: normal
tags:
    - 8f-lean
    - reorg-2026-10-04
    - 8f-open
created_at: 2026-08-17T22:44:34Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Found by the ch1+ch2 audit (qou-n4jv), 2026-08-17.
Audit: docs/audits/2026-08-17-ch1-ch2-lean-sibling-elaboration-sweep.md (P1).

File: quantum-observable-universes/su2-emergence.lean
Struct: QOU.RankOneGaugeData

Documented as 'the three constraints that together force SU(2)'. Measured, ONE
constrains the QOU:
  * fund_dim_two : ({twice_j := 1 : SpinLabels}).cat_dim = 2
      -- an arithmetic fact about a LITERAL. Discharged by the `decide` tactic (verified
      -- exit 0). It never mentions qou, so it does NOT say that THIS QOU's
      -- fundamental object has dimension 2.
  * volume_nondeg -- genuine constraint on qou.volumeForm  [OK]
  * adjoint_trivial := qou.adjoint_vanishing
      -- has a DEFAULT VALUE, so every QOU satisfies it automatically.

So su2_emergence reads as 'volume non-degeneracy (plus the QOU axioms) yields a
spin decomposition', not a three-legged derivation. A scope warning saying this
was added to the docstring in 1bc67fbe; the structure was NOT changed.

THE HARD PART (why it was not fixed inline): tying fund_dim_two to
qou.fundamentalObj needs the spin indexing that SpinDecomposition supplies --
and SpinDecomposition is the CONCLUSION su2_emergence produces. The hypothesis
cannot reference it without circularity. Breaking that needs either
  (a) a spin-indexing structure independent of su2_emergence, taken as a
      hypothesis, with su2_emergence upgrading it; or
  (b) stating fund_dim_two via a categorical dimension of qou.fundamentalObj
      computed from the QOU data directly (no spin labels).
This declaration is the most depended-upon on the critical path -- do not
restructure it casually.

SEPARATE ISSUE, same file: su2_emergence is an `axiom`, not sorry+Ref and not a
conjecture class. Its docstring is honest that Tannaka duality is absent from
Mathlib, but per AGENTS.md 'Axiomatization is NOT a Proof' an axiom is the one
disposition that hides from #print axioms' sorryAx and from the vacuity audits.
Worth converting to a conjecture class; not done here.


## Triaged 2026-10-10 — OPEN, not mechanical; tagged `8f-open`

Read while working the `8f-lean` front. **This bean already explains why it
cannot be fixed inline**, under its own heading THE HARD PART: tying
`fund_dim_two` to `qou.fundamentalObj` needs the spin indexing that
`SpinDecomposition` supplies, and `SpinDecomposition` is the **conclusion**
`su2_emergence` produces. The hypothesis would need the conclusion.

So it is open formalisation work with a circularity to break, not a repair.
The 1bc67fbe docstring scope-warning remains the honest interim state.

## Progress (2026-11-16, PR #8209)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/RankOneSpinSingletThreeGenerationsLadderChargeAndNearlyKahlerCosets.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`9c4fe9d8065c7167caac7a61ef4becd45df1573f`, `scriptHash: e6bdb7c63ac7`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8209`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8209, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
