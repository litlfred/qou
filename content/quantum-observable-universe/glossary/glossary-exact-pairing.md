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
