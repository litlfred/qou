---
# qou-p8zx
title: Resolve PDF build warnings (cross-refs, macros, unicode)
status: todo
type: task
priority: normal
created_at: 2026-07-13T01:42:14Z
updated_at: 2026-07-13T01:42:47Z
---

Warnings to resolve:

1. Undefined cross-references (13 warnings):
   - def:simple-objects-V
   - eq:categorical-volume-constraint
   - eq:su2-emergence-diagram
   - eq:q-exp
   - lem:ccg-cosimplicial-identities
   - eq:z-from-SD
   - eq:topological-mass-decomp
   - conj:phi-q-tower-jsj-bridge
   - prop:archimedean-realization-functor
   - prop:six-term-mass-formula-complete
   - sec:mass-comparison-table
   - rem:hadron-half-life-verification
   - local-q-zeta-function

2. Undefined control sequences:
   - \@addpunct
   - \ignorespaces
   - \popQED
   - \endtrivlist
   - \@endpefalse
   - \colorlet
   - \tiny
   - \footnotesize
   - \coth
   - \lbrack
   - \rbrack
   - \coloneqq
   - \arctan

3. Unmapped unicode (failed PDF generation):
   - "𝔙" (U+1D519)
   - "’" (U+2019)
   - "É" (U+00C9)
   - "⥤" (U+2964)
