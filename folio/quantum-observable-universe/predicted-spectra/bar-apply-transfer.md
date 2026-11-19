Let $P \colon \mathbb{R}_{>0} \to \mathrm{Prop}$ be a bar-invariant property of the aether parameter:

$$
  \forall\,q > 0,\quad P(q) \iff P(q^{-1}).
$$

For every $a > 0$:

1. **Lower bound transfer.**
   $\bigl(\forall q > a,\; P(q)\bigr) \iff
    \bigl(\forall q < a^{-1},\, q > 0 \Rightarrow P(q)\bigr).$

2. **Two-sided extension.**
   If $a < 1$ and $\bigl(\forall q \in (a, a^{-1}),\, P(q)\bigr)$, then
   $\bigl(\forall q \in \mathbb{R}_{>0} \setminus \{a, a^{-1}\},\, P(q)\bigr)$
   does not follow in general. If $P$ is continuous on
   $\mathbb{R}_{>0}$, bar-invariance forces $P$ to extend symmetrically
   across both endpoints.

3. **Negation transfer.**
   $\bigl(\exists q < a,\, q > 0 \land \neg P(q)\bigr) \iff
    \bigl(\exists q > a^{-1},\, \neg P(q)\bigr)$.
