<!-- FILE_START: glossary-rigidity-intro.md -->
We define rigidity, duality, and pivotal-category terminology used throughout this paper.
<!-- FILE_END: glossary-rigidity-intro.md -->

<!-- FILE_START: glossary-exact-pairing.md -->
**:refterm[Exact pairing]{#exact-pairing}.** Given objects $X$ and $Y$ in a monoidal category, an exact pairing consists of morphisms $\varepsilon \colon X \otimes Y \to \mathbf{1}$ (evaluation) and $\eta \colon \mathbf{1} \to Y \otimes X$ (coevaluation) satisfying the snake identities:

$(\varepsilon \otimes \mathrm{id}_X) \circ (\mathrm{id}_X \otimes \eta) = \mathrm{id}_X, \qquad (\mathrm{id}_Y \otimes \varepsilon) \circ (\eta \otimes \mathrm{id}_Y) = \mathrm{id}_Y.$

When an exact pairing exists, $Y$ is a right dual of $X$, and $X$ a left dual of $Y$.

**Mathlib reference.**
`CategoryTheory.ExactPairing` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
<!-- FILE_END: glossary-exact-pairing.md -->

<!-- FILE_START: glossary-left-dual.md -->
**:defterm[Left dual]{#left-dual}.** An object $Y$ in a monoidal category has a left dual if there exists an object $X$ and an exact pairing $(X, Y)$.

**Mathlib reference.**
`CategoryTheory.HasLeftDual` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
<!-- FILE_END: glossary-left-dual.md -->

<!-- FILE_START: glossary-right-dual.md -->
**:defterm[Right dual]{#right-dual}.** An object $X$ in a monoidal category has a right dual if there exists an object $Y$ and an exact pairing $(X, Y)$.

**Mathlib reference.**
`CategoryTheory.HasRightDual` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
<!-- FILE_END: glossary-right-dual.md -->

<!-- FILE_START: glossary-rigid-category.md -->
**:defterm[Rigid category]{#rigid-category}.** A monoidal category in which every object has both a left dual and a right dual.

**Mathlib reference.**
`CategoryTheory.RigidCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
<!-- FILE_END: glossary-rigid-category.md -->

<!-- FILE_START: glossary-pivotal-category.md -->
**:defterm[Pivotal category]{#pivotal-category}.** A rigid monoidal category equipped with a monoidal natural isomorphism $\delta_X \colon X \xrightarrow{\sim} X^{\vee\vee}$ between each object and its double dual. This makes left and right traces coincide.

**Mathlib reference.**
`CategoryTheory.PivotalCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
<!-- FILE_END: glossary-pivotal-category.md -->

<!-- FILE_START: glossary-compact-closed-category.md -->
**:defterm[Compact closed category]{#compact-closed-category}.** A symmetric monoidal category that is also rigid. Since the braiding identifies $X \otimes Y \cong Y \otimes X$, left duals and right duals coincide.

**Mathlib reference.**
`CategoryTheory.CompactClosedCategory` (class).
Import: `Mathlib.CategoryTheory.Closed.Monoidal`.
<!-- FILE_END: glossary-compact-closed-category.md -->
