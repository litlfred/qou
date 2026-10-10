---
# qou-bq5e
title: 'Scope note in HeckeGS.lean: Bokut-Shiao is a Coxeter-GROUP theorem and there is no general-Coxeter GS theorem'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:28:44Z
updated_at: 2026-10-04T15:24:20Z
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
