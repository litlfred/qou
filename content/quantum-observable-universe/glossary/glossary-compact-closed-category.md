**:defterm[Compact closed category]{#compact-closed-category}.** A symmetric monoidal category that is
also rigid. Because the braiding identifies $X \otimes Y \cong Y \otimes X$, left duals and right duals coincide, so it suffices to
ask that every object has a dual.

The category $\mathrm{FinVect}_k$ of finite-dimensional vector spaces
is the prototypical example: the dual is the linear dual $V^* = \mathrm{Hom}_k(V, k)$.

**Mathlib reference.**
`CategoryTheory.CompactClosedCategory` (class).
Import: `Mathlib.CategoryTheory.Closed.Monoidal` (or
`Mathlib.CategoryTheory.Monoidal.Rigid.Basic`, depending on Mathlib
version).
Extends: `SymmetricCategory` + `RigidCategory`.
