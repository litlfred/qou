Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = 1/(q^{1/2} + q^{-1/2})$ ([Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).

## Why adjacency does not matter

The naive worry is that for **adjacent** generators
$\sigma_i, \sigma_{i+1}$, the braid relation
$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$
might introduce dependencies that spoil the factorization. The
proof above sidesteps that concern because the peel operates on
a **length-2** word, not a length-3 word: no braid relation is
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

## Operator interpretation

The value $z^2$ is the **Jones polynomial of the Hopf link**
(unknotted two-component linking) evaluated at the substrate
parameter:
$J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
= -(q + q^{-1})/(q^{1/2} + q^{-1/2})$. Multiplying by the
Markov normalization recovers the pair contribution to the
categorical mass — the pair blow-up centre at coordinate
$\hat V_i\hat V_j$ carries the same weight $z^2$ regardless
of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$
(cf. `adjacent-vs-full-probe.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)).
