<!-- FILE_START: glossary-rigidity-intro.md -->
Glossary entries for rigidity, duality, and pivotal-category terminology.
<!-- FILE_END: glossary-rigidity-intro.md -->

<!-- FILE_START: glossary-exact-pairing.md -->
**:refterm[Exact pairing]{#exact-pairing}.** Given objects $X$ and $Y$ in a :refterm[monoidal category]{#monoidal-category},
an *:refterm[exact pairing]{#exact-pairing}* consists of morphisms
$\varepsilon \colon X \otimes Y \to \mathbf{1}$ (evaluation) and
$\eta \colon \mathbf{1} \to Y \otimes X$ (coevaluation) satisfying
the snake identities (also called *zig-zag identities* or
*triangle identities for adjunctions*):

$(\varepsilon \otimes \mathrm{id}_X) \circ (\mathrm{id}_X \otimes \eta) = \mathrm{id}_X, \qquad (\mathrm{id}_Y \otimes \varepsilon) \circ (\eta \otimes \mathrm{id}_Y) = \mathrm{id}_Y.$

When an :refterm[exact pairing]{#exact-pairing} exists, $Y$ is said to be a *:refterm[right dual]{#right-dual}* of $X$,
and $X$ a *:refterm[left dual]{#left-dual}* of $Y$.

**Mathlib reference.**
`CategoryTheory.ExactPairing` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Fields: `evaluation`, `coevaluation`, `evaluation_coevaluation'`,
`coevaluation_evaluation'`.
See also [def:snake-identity](#def:snake-identity) for the formal
statement used in this paper.
<!-- FILE_END: glossary-exact-pairing.md -->

<!-- FILE_START: glossary-left-dual.md -->
**:defterm[Left dual]{#left-dual}.** An object $Y$ in a :refterm[monoidal category]{#monoidal-category} has a *left dual*
if there exists an object $X$ and an :refterm[exact pairing]{#exact-pairing} $(X, Y)$ — that is,
$X$ is the left dual of $Y$.

In practice, `HasLeftDual Y` asserts the existence of an `ExactPairing`
with $Y$ on the right. The paper writes $V^{\vee}$ for the
(right) dual of $V$; some sources swap the left/right convention.

**Mathlib reference.**
`CategoryTheory.HasLeftDual` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Accessor: `ᘁY` (Unicode left-dual notation) for the left dual object.
<!-- FILE_END: glossary-left-dual.md -->

<!-- FILE_START: glossary-right-dual.md -->
**:defterm[Right dual]{#right-dual}.** An object $X$ in a :refterm[monoidal category]{#monoidal-category} has a *right dual*
if there exists an object $Y$ and an :refterm[exact pairing]{#exact-pairing} $(X, Y)$ — that is,
$Y$ is the right dual of $X$.

The paper's notation $V^{\vee}$ corresponds to a right dual. When the
category is rigid (every object has both left and right duals), the
distinction between left and right duals is often suppressed.

**Mathlib reference.**
`CategoryTheory.HasRightDual` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Accessor: `Xᘁ` (Unicode right-dual notation) for the right dual object.
<!-- FILE_END: glossary-right-dual.md -->

<!-- FILE_START: glossary-rigid-category.md -->
**:defterm[Rigid category]{#rigid-category}.** A :refterm[monoidal category]{#monoidal-category} in which every object has both
a :refterm[left dual]{#left-dual} and a :refterm[right dual]{#right-dual}. Equivalently, every object participates
in an :refterm[exact pairing]{#exact-pairing} on both sides.

The paper's
[Definition 1.1 (Rigid :refterm[monoidal category]{#monoidal-category})](#def:rigid-monoidal-category)
bundles a single object $V$ with its dual and the snake identities.
Mathlib's `RigidCategory` is the global statement that *all* objects
have duals.

**Mathlib reference.**
`CategoryTheory.RigidCategory` (class), extending `MonoidalCategory`.
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Provides: `HasLeftDual X` and `HasRightDual X` for every `X`.
<!-- FILE_END: glossary-rigid-category.md -->

<!-- FILE_START: glossary-pivotal-category.md -->
**:defterm[Pivotal category]{#pivotal-category}.** A rigid :refterm[monoidal category]{#monoidal-category} equipped with a
monoidal natural isomorphism $\delta_X \colon X \xrightarrow{\sim} X^{\vee\vee}$
between each object and its double dual. This makes left and right
traces (and hence quantum dimensions) coincide.

In the paper, the involutive structure
([Definition](#def:involutive-structure)) on a quantum universe plays
a role analogous to a pivotal structure.

**Mathlib reference.**
`CategoryTheory.PivotalCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic` (when available;
Mathlib coverage of pivotal categories is still in development).
<!-- FILE_END: glossary-pivotal-category.md -->

<!-- FILE_START: glossary-compact-closed-category.md -->
**:defterm[Compact closed category]{#compact-closed-category}.** A :refterm[symmetric monoidal category]{#symmetric-monoidal-category} that is
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
<!-- FILE_END: glossary-compact-closed-category.md -->

