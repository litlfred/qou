**Proposition (conditional).** If the relabellings of $n$ strands are in bijection with the
symmetry group $S_5$ of Bring's surface, then $n = 5$. If moreover three strands are
colour, the other two are isospin. The count $5$ is odd, as
[`prop:odd-strands-force-chirality`](odd-strands-force-chirality.md) requires.

Bring's surface is cut out by $p_1 = p_2 = p_3 = 0$ in the five homogeneous coordinates of
$\mathbb{P}^4$, permuted by $S_5$. The traceless condition $\sum_i y_i = 0$ on strand charges
is the hyperplane $p_1 = 0$. The three colour strands are the colour tube coordinates of
[`def:color-tube-coordinates`](../brings-surface/color-tube-coordinates.md).

A second route gives the same count. If the $n-1$ traceless charge directions are Bring's $g$
holomorphic differentials, then $n = g + 1$, and Bring's map has $\chi = 2 - 2g = -6$, so
$g = 4$ and $n = 5$. The two hypotheses are compatible: the holomorphic differentials carry
the four-dimensional traceless part of the permutation representation of $S_5$, twisted by
the sign.

**Proof.** A bijection gives $n! = 5! = 120$, and $n! = 1$ for $n \le 1$, so $n = 5$ by
injectivity of the factorial on $n \ge 2$. Then $5 - 3 = 2$. For the genus route, $2 - 2g = -6$ gives $g = 4$.

**What stays open.** Why strand relabellings are Bring's symmetries (or the charges its
differentials), and why three strands are colour; these are inputs here.

## Lean structure

`QOU.StandardModel.StrandCount`: `strandCount_eq_five`, `isospin_count`, `five_odd`,
`bring_genus_eq_four`, `strandCount_of_genus`.
Sorry-free.
