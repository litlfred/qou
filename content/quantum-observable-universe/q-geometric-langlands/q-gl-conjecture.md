Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $X$ be its brane curve, $G_q$ its quantum gauge group, and $\check{G}_q$ its $q$-Langlands dual ([q-Langlands dual](#def:q-langlands-dual)). The **$q$-Geometric Langlands correspondence** asserts an equivalence of $\infty$-categories:

$$
  \mathbb{L}_q \colon
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q}(X))
  \xrightarrow{ \sim }
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X)).
$$

This equivalence is parametrised by the non-torsion locus $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ and satisfies five properties.

1. **Hecke compatibility**: For every $q$-Hecke operator $\mathbf{T}_{x,\lambda}^{(q)}$ ([q-Hecke operator](#def:q-hecke-operator)), the functor $\mathbb{L}_q$ intertwines the action on the left with the action of $V_\lambda^{(q)}$ on $\mathrm{LocSys}_{\check{G}_q}(X)$:
   $$
     \mathbb{L}_q \circ \mathbf{T}_{x,\lambda}^{(q)}
     \simeq
     V_\lambda^{(q)}(-)_x \otimes \mathbb{L}_q.
   $$

2. **Fibre-functor factorisation**: The equivalence factors through the fibre functor $\tau$:
   $$
     \mathbb{L}_q = \tau^* \circ \mathbb{L}_q^{\mathrm{Tannakian}}.
   $$
   Tannaka--Krein reconstruction for $\check{G}_q$ determines $\mathbb{L}_q^{\mathrm{Tannakian}}$.

3. **$q$-Oper locus**: The equivalence $\mathbb{L}_q$ restricts to a bijection between $q$-opers ([q-oper](#def:q-oper)) and $q$-Hecke eigensheaves ([q-Hecke eigensheaf](#def:q-hecke-eigensheaf)):
   $$
     \mathrm{Op}_{\check{G}_q}(X)  \hookrightarrow 
     \mathrm{LocSys}_{\check{G}_q}(X)
     \quad\xrightarrow{\mathbb{L}_q^{-1}}\quad
     \{\text{$q$-Hecke eigensheaves}\}.
   $$

4. **Kummer constraint**: The equivalence $\mathbb{L}_q$ forms a well-defined $\mathbb{G}_m$-family on the non-torsion locus $\mathbb{G}_m^{\mathrm{nt}}$. At roots of unity $q \in \mu_n$, the quantum dimension $[n]_q = 0$ vanishes, the Frobenius pairing degenerates, and $\mathbb{L}_q$ breaks down. The obstruction ([Kummer filtration](#rem:kummer-filtration-obstruction)) persists at all Kummer levels $n \nmid \chi(A)$.

5. **Classical limit**: As $q \to 1$, $\mathbb{L}_q$ recovers the classical Geometric Langlands equivalence ([classical limit](#conj:q-gl-classical-limit)).
