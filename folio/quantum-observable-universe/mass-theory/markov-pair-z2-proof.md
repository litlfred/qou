## Proof

The argument is a **direct two-step peel**, one Markov move per
factor. Embed $\sigma_i\sigma_j$ in $H_{j+1}(q)$, the minimal
Hecke algebra containing both generators; higher embeddings
follow by Markov closure $\mathrm{tr}_M^{H_n} = \mathrm{tr}_M^{H_{n-1}}$
on any element of $H_{n-1}(q)$ embedded in $H_n(R, q)$.

*Peel 1 (outer generator).* In $H_{j+1}(q)$ the rightmost
generator is $\sigma_j$. Since $\sigma_i \in H_j(q)$ (it involves
only indices $\le j-1$), $\sigma_i$ commutes by definition with the
coefficient ring and is not affected by the Markov move on
$\sigma_j$:

$$
  \mathrm{tr}_M^{H_{j+1}}\!(\sigma_i\sigma_j)
  \;=\; z \cdot \mathrm{tr}_M^{H_j}\!(\sigma_i).
$$

*Peel 2 (inner generator).* The remaining element $\sigma_i$
lives in $H_j(q)$. Repeatedly apply Markov closure to reduce
to the minimal embedding $\sigma_i \in H_{i+2}(q)$:

$$
  \mathrm{tr}_M^{H_j}\!(\sigma_i)
  \;=\; \mathrm{tr}_M^{H_{j-1}}\!(\sigma_i)
  \;=\; \cdots \;=\;
  \mathrm{tr}_M^{H_{i+2}}\!(\sigma_i).
$$

In $H_{i+2}(q)$, $\sigma_i$ itself is the rightmost generator.
Apply the Markov axiom once more:

$$
  \mathrm{tr}_M^{H_{i+2}}\!(\sigma_i)
  \;=\; z \cdot \mathrm{tr}_M^{H_{i+1}}\!(1)
  \;=\; z.
$$

Combining the two peels:
$\mathrm{tr}_M(\sigma_i\sigma_j) = z \cdot z = z^2$.
$\square$

## Independence of adjacency

The naive worry is that for **adjacent** generators
$\sigma_i, \sigma_{i+1}$, the braid relation
$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$
might introduce dependencies that spoil the factorization. The
proof above sidesteps that concern because the peel operates on
a **length-2** word rather than a length-3 word: no braid relation is
invoked. The only algebra used is:

1. $\sigma_j$ is the rightmost generator (index-maximal) in
 $\sigma_i\sigma_j$ for $i < j$, so the Markov axiom applies
 directly.
2. $\sigma_i \in H_j(q)$ has all its support at indices $\le j-1$,
 so it is invariant under the embedding
 $H_j(q) \hookrightarrow H_{j+1}(q)$.

Both conditions hold irrespective of $|i-j|$. Braid relations
become relevant only for length-$\ge 3$ words with repeated
generators.

## Relation to the nuclear product factorization

This proposition is the **pair specialization** of the nuclear
Markov-trace product formula
([Markov trace factorization](#thm:markov-trace-factorization)),
obtained by setting $a_i = a_j = 1$ and $b_i = b_j = 0$. The
general product formula $\prod_i (z\,a_i + b_i)$ instantiates at
each pair generator to $z\cdot 1 + 0 = z$, and the product over
the two pair indices gives $z^2$.

The present proposition isolates the pair identity as a
standalone algebraic fact that does **not** require the
full nuclear Gröbner--Shirshov reduction machinery. It
underwrites the all-pairs set $\mathcal{P}_n = \{(i,j) : i < j\}$
in the jet-tower mass decomposition
([jet-tower remark](#rem:mass-endomorphism-jet-tower)) without
adjacency restriction.
