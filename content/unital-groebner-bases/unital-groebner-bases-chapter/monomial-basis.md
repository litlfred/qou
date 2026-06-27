Throughout, $R$ is a commutative ring with unity and $A$ is an
$R$-algebra without quasi-zeros (i.e.\ elements $a \in A$ such that
$bac = 0$ for all $b, c \in A$ not both $1$).

Choose a set of algebra generators
$A = R\langle x_i \mid i \in \Lambda\rangle$ for some index set
$\Lambda$.

**Monomials.** Let $\alpha = \alpha_1 \alpha_2 \cdots \alpha_n$ be a
finite-length word in $\Lambda$. A *monomial* in $A$ is the ordered
product

$$
  x_\alpha := x_{\alpha_1} \cdot x_{\alpha_2} \cdots x_{\alpha_n}.
$$

**Monomial basis.** Suppose $A$ is free as an $R$-module. We say $A$
has a **monomial basis** $B$ subordinate to $\Lambda$ if $B$ is a subset
of all finite-length words in $\Lambda$ such that

$$
  A = R\{x_\beta \mid \beta \in B\}.
$$

We identify $\beta$ with $x_\beta$ to simplify notation.

**Leading terms.** Assume $B$ is well-ordered by $<$. For
$f \in A$, write $f$ uniquely as

$$
  f = c_1 b_1 + c_2 b_2 + \cdots + c_n b_n,
  \qquad c_i \in R^* := R \setminus \{0\},\;
  b_i \in B,\;
  b_1 > b_2 > \cdots > b_n.
$$

Then define:
- $\mathrm{LM}(f) := b_1$ (the *leading monomial*),
- $\mathrm{LC}(f) := c_1$ (the *leading coefficient*),
- $\mathrm{LT}(f) := \mathrm{LC}(f)\,\mathrm{LM}(f)$
  (the *leading term*).
