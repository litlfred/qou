---
# qou-0tiw
title: 'GAP: RankOneGaugeData fund_dim_two constrains nothing -- circular with SpinDecomposition'
status: todo
type: task
priority: normal
created_at: 2026-08-17T22:44:34Z
updated_at: 2026-08-17T22:46:18Z
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
