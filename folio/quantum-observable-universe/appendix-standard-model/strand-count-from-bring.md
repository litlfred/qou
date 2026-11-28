**Proposition (conditional).** If the relabellings of $n$ strands are in bijection with the
symmetry group $S_5$ of Bring's surface, then $n = 5$. If moreover three strands are
colour, the other two are isospin. The count $5$ is odd, as
[`prop:odd-strands-force-chirality`](odd-strands-force-chirality.md) requires.

Bring's surface is cut out by $p_1 = p_2 = p_3 = 0$ in the five homogeneous coordinates of
$\mathbb{P}^4$, permuted by $S_5$. The traceless condition $\sum_i y_i = 0$ on strand charges
is the hyperplane $p_1 = 0$. The three colour strands are the colour tube coordinates of
[`def:color-tube-coordinates`](../brings-surface/color-tube-coordinates.md).

**Proof.** A bijection gives $n! = 5! = 120$, and $n! = 1$ for $n \le 1$, so $n = 5$ by
injectivity of the factorial on $n \ge 2$. Then $5 - 3 = 2$.

**What stays open.** Why strand relabellings are Bring's symmetries, and why three strands
are colour; both are inputs here.

## Lean structure

`QOU.StandardModel.StrandCount`: `strandCount_eq_five`, `isospin_count`, `five_odd`.
Sorry-free.
