Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be a QOU with brane curve
$X$, quantum gauge group $G_q$, and $q$-Langlands dual $\check{G}_q$
(Definition \ref{def:q-langlands-dual}).  The **$q$-Geometric Langlands
correspondence** asserts the existence of an equivalence of
$\infty$-categories:

$$
  \mathbb{L}_q \colon
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q}(X))
  \;\xrightarrow{\;\sim\;}
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X)),
$$

satisfying:

1. **Hecke compatibility**: for every $q$-Hecke operator
   $\mathbf{T}_{x,\lambda}^{(q)}$ on the left-hand side, the functor
   $\mathbb{L}_q$ intertwines it with the action of
   $V_\lambda^{(q)}$ on $\mathrm{LocSys}_{\check{G}_q}(X)$:
   $$
     \mathbb{L}_q \circ \mathbf{T}_{x,\lambda}^{(q)}
     \;\simeq\;
     V_\lambda^{(q)}(-)_x \otimes \mathbb{L}_q.
   $$

2. **Fibre-functor factorisation**: the equivalence factors through
   the fibre functor $\tau$:
   $$
     \mathbb{L}_q = \tau^* \circ \mathbb{L}_q^{\mathrm{Tannakian}},
   $$
   where $\mathbb{L}_q^{\mathrm{Tannakian}}$ is determined by
   Tannaka--Krein reconstruction for $\check{G}_q$.

3. **$q$-Oper locus**: the equivalence $\mathbb{L}_q$ restricts to a
   bijection between $q$-opers (Definition \ref{def:q-oper}) and
   $q$-Hecke eigensheaves (Definition \ref{def:q-hecke-eigensheaf}):
   $$
     \mathrm{Op}_{\check{G}_q}(X) \;\hookrightarrow\;
     \mathrm{LocSys}_{\check{G}_q}(X)
     \quad\xrightarrow{\;\mathbb{L}_q^{-1}\;}\quad
     \{\text{$q$-Hecke eigensheaves}\}.
   $$

4. **Classical limit**: as $q \to 1$, $\mathbb{L}_q$ recovers the
   classical Geometric Langlands equivalence of Beilinson--Drinfeld
   (Proposition \ref{prop:q-gl-classical-limit}).
