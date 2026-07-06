**Proposition (Bar-transfer principle).**
Let $P \colon \mathbb{R}_{>0} \to \mathrm{Prop}$ be a property of the
substrate parameter that is **bar-invariant**:

$$
  \forall\,q > 0,\quad P(q) \iff P(q^{-1}).
$$

Then for every $a > 0$:

1. **Lower bound transfer.**
   $\bigl(\forall q > a,\; P(q)\bigr) \iff
    \bigl(\forall q < a^{-1},\, q > 0 \Rightarrow P(q)\bigr).$

2. **Two-sided extension.**
   If $a < 1$ and $\bigl(\forall q \in (a, a^{-1}),\, P(q)\bigr)$, then
   $\bigl(\forall q \in \mathbb{R}_{>0} \setminus \{a, a^{-1}\},\,
    P(q)\bigr)$
   does **not** follow in general — but if $P$ is also continuous on
   $\mathbb{R}_{>0}$, the bar-invariance forces $P$ to extend symmetrically
   across both endpoints.

3. **Negation transfer.**
   $\bigl(\exists q < a,\, q > 0 \land \neg P(q)\bigr) \iff
    \bigl(\exists q > a^{-1},\, \neg P(q)\bigr)$.

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
