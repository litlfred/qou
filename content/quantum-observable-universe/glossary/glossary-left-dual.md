**:defterm[Left dual]{#left-dual}.** An object $Y$ in a monoidal category has a *left dual*
if there exists an object $X$ and an exact pairing $(X, Y)$ — that is,
$X$ is the left dual of $Y$.

In practice, `HasLeftDual Y` asserts the existence of an `ExactPairing`
with $Y$ on the right. The paper writes $V^{\vee}$ for the
(right) dual of $V$; some sources swap the left/right convention.

**Mathlib reference.**
`CategoryTheory.HasLeftDual` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Accessor: `ᘁY` (Unicode left-dual notation) for the left dual object.
