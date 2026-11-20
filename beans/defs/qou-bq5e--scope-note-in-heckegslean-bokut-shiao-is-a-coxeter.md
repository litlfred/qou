---
# qou-bq5e
title: 'Scope note in HeckeGS.lean: Bokut-Shiao is a Coxeter-GROUP theorem and there is no general-Coxeter GS theorem'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:28:44Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1o8n
---

`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean` now
correctly says the axiom `hecke_is_gs_basis` was false and deleted, and its
References block names Bokut & Shiao (now registered as [bokut2001], entry
created 2026-08-09 -- the refid was previously dangling, cited at
QOU/Archimedean/MassGapGm.lean:46 with no entry in references.ts).

Two scope facts belong in that module header and in `qou-auq3`, both now
citable:

1. THERE IS NO GENERAL-COXETER THEOREM TO APPEAL TO. [chenliu2009] Example 3.2
   (pp. 4-5) refutes by explicit counterexample the Bokut-Shiao conjecture that
   a GS basis of an arbitrary Coxeter group is obtainable from
   S = {(1),(2),(3')} using only the commuting relations: the rank-4 matrix
   m12 = m23 = m24 = infinity, m13 = 3, m14 = 2, m34 = 5 fails, and the
   corrected basis is exhibited. Its introduction restricts the known positive
   results to FINITE Coxeter groups. Type A_{n-1} is finite, so the folio's own
   case is untouched -- recording that is the point, so nobody later invokes
   "GS bases for Coxeter groups" generically.

2. THE DEFORMATION IS NOT COVERED. [chenliu2009], like [bokut2001], works with
   the Coxeter group and never mentions H_n(q) or a deformation parameter.
   `qou-auq3` must not assume the transfer from C[W] to H_n(q); the paper that
   does treat the deformed type-A case is Kang-Lee-Lee-Oh 2002 (sibling bean).

Also worth one line while there: `heckeRewritingSystem` contains only the
defining relations, so even at q = 1 the cited theorem never applied to it --
the module already says this at section 4e; the citation now exists to back it.

Target: the module docstring / References block of HeckeGS.lean, and the
`qou-auq3` analysis. NOT an aid-proof: neither document discharges anything.

- Round 78 (`lane-e667`): Formalized `qou-pan0`, `qou-tgci`, `qou-ykt7`, `qou-bq5e`, `qou-ch3j` in `QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence` with 80-dps `mpmath` 2-commit witness stamp (`0869f3f0f137dac72b436e92a747c174449acb33` -> `8147a3388c97af1335cf6c164bd3eb4c9b4bd78a`, `scriptHash=f8a29b2aeceb36b8f640091b101ca03046313573b1d604a9e680784ae71f9af4`) in PR `litlfred/qou#8422` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8422, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
