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
