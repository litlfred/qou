**Proof.**
Because $\phi$ commutes with $\iota$, it descends along $\pi$ to an automorphism $\bar\phi$ of $\mathbb{P}^1$. Faithfulness of $\phi$ and commutativity with $\iota$ force $\bar\phi$ to be an element of order $5$ in $\mathrm{PGL}_2(\mathbb{C}) = \mathrm{Aut}(\mathbb{P}^1)$. Every order-5 element of $\mathrm{PGL}_2(\mathbb{C})$ is conjugate to $x \mapsto \zeta_5 x$. This map has exactly two fixed points on $\mathbb{P}^1$, namely $\{0, \infty\}$. Möbius normalisation fixes $\bar\phi \colon x \mapsto \zeta_5 x$.

The orbits of $\bar\phi$ on $\mathbb{P}^1$ have size 1 (fixed points: $0, \infty$) or 5 (generic orbits $\{a, \zeta_5 a, \zeta_5^2 a, \zeta_5^3 a, \zeta_5^4 a\}$ for $a \notin \{0, \infty\}$).

Since $\phi$ commutes with $\iota$, the branch divisor of $\pi$ is $\phi$-invariant. It descends to a $\bar\phi$-invariant subset of $\mathbb{P}^1$. Its cardinality is a non-negative combination of 1 and 5:

$$
  |\mathrm{Branch}(\pi)| \in \{0, 1, 2, 5, 6, 7, 10, 11, 12, \ldots\}.
$$

Riemann–Hurwitz gives:

$$
  |\mathrm{Branch}(\pi)| = 2g(X) + 2.
$$

The size is even. Condition (ii) forces $g \geq 2$. A sphere has $\mathrm{Aut}(\mathbb{P}^1) = \mathrm{PGL}_2$ which admits $\mathbb{Z}_5$, but a sphere is excluded from the hyperelliptic indexing $g \geq 2$. Thus, the size is at least 6. The smallest admissible $|\mathrm{Branch}(\pi)|$ in this list that is even and at least 6 is 6. This implies $g = 2$.

A $\bar\phi$-invariant set of size 6 decomposes uniquely into one size-5 orbit and one fixed point. (No other solution to $6 = 5a + b$ exists for $a, b \geq 0$ and $b \leq 2$.) The branch divisor is therefore:

$$
  \mathrm{Branch}(\pi) = \{\zeta_5^k a : 0 \leq k \leq 4\} \cup \{c\} \qquad \text{for some } a \neq 0, c \in \{0, \infty\}.
$$

Rescaling $x \mapsto a^{-1} x$ normalises $a = 1$. This yields the orbit $\{1, \zeta_5, \zeta_5^2, \zeta_5^3, \zeta_5^4\}$. The two choices $c = \infty$ and $c = 0$ yield the equations $y^2 = x^5 - 1$ and $y^2 = x(x^5 - 1) = x^6 - x$, respectively. The change of chart $x \mapsto 1/x$, $y \mapsto y/x^3$ maps one to the other up to a sign absorbed into $y$. Since the branch divisor determines a smooth hyperelliptic curve of genus $\geq 2$ up to isomorphism, both choices yield isomorphic curves.

Therefore, $X \cong \mathcal{X}_5$. $\square$
