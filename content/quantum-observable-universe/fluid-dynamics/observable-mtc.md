Fix a positive integer $N \geq 3$ and set
$q = \zeta_N = e^{2\pi i / N}$ --- a primitive $N$-th root of unity.
At this value of the substrate parameter the representation category
$\mathrm{Rep}(U_q(\mathfrak{su}_2))$ is not semisimple; quotienting
by the ideal of negligible morphisms produces the *truncated*
category
$\mathbf{C}_{\mathrm{any}}(N)$ with only finitely many simple
objects $\mathbf{V}_0, \mathbf{V}_1, \ldots, \mathbf{V}_{N-2}$
\cite{moore-seiberg1989}.

**Definition.**  The **observable modular tensor category** at level
$N$ is the ribbon fusion category $\mathbf{C}_{\mathrm{any}}(N)$
together with the braiding $c$ and ribbon twist $\varTheta$ inherited
from the quasi-triangular structure of $U_q(\mathfrak{su}_2)$ at
$q = \zeta_N$.  Equivalently, $\mathbf{C}_{\mathrm{any}}(N)$ is a
*modular* tensor category: the $S$-matrix
$S_{ij} = \mathrm{tr}(c_{\mathbf{V}_i, \mathbf{V}_j} \circ
c_{\mathbf{V}_j, \mathbf{V}_i})$ is non-degenerate.

**Braiding non-symmetry.**  For $N \geq 3$ and any non-trivial
simple $\mathbf{V} \in \mathbf{C}_{\mathrm{any}}(N)$,

$$
  c_{\mathbf{V}, \mathbf{V}} \circ c_{\mathbf{V}, \mathbf{V}}
    \neq  \mathrm{id}_{\mathbf{V} \otimes \mathbf{V}},
$$

The braiding does not square to the identity on simples.  This
is the hallmark of a genuinely modular (non-symmetric) tensor
category and is the prerequisite for anyonic statistics.

**Relation to the commutative limit.**  The commutative limit
$q \to 1$ of Chapter 3 corresponds to $N \to \infty$, where the
truncation opens up, negligible morphisms vanish, and the braiding
degenerates to a symmetric structure.  The two specialisations are
therefore distinct:

| Specialisation | $q$ | Braiding | Anyons |
|---|---|---|---|
| Commutative limit | $q = 1$ | symmetric | no |
| Root-of-unity $\mathrm{MTC}$ | $q = \zeta_N$ ($N \geq 3$) | non-symmetric | yes |

The geometric shadow on the genus-$2$ curve $\mathcal{X}_5$ of
[def:hyperelliptic-quintic](#def:hyperelliptic-quintic) picks up
either regime via its fifth-roots-of-unity branch set: in the
commutative limit the $\zeta_5^{k}$ mark classical phase defects
on a single $\mathrm{U}(1)$ tube, while at $q = \zeta_5$ the same
discrete data labels anyonic fusion channels in
$\mathbf{C}_{\mathrm{any}}(5)$.
