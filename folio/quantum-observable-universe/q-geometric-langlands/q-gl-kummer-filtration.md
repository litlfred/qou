The Kummer tower $\mu_1 \subset \mu_2 \subset \cdots \subset \mu_\infty \subset \mathbb{G}_m$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) induces a descending filtration on the moduli of $q$-local systems. For each $n \geq 1$, define the **level-$n$ sublocus**:

$$
  \mathrm{LocSys}_{\check{G}_q}^{(n)}(X)
  \subset
  \mathrm{LocSys}_{\check{G}_q}(X).
$$

This sublocus consists of $q$-local systems $\mathcal{L}_q$ whose $q$-monodromy $\Omega_q(\varrho)$ ([q-local system](#def:q-local-system)) is $n$-divisible in $\mathrm{End}(\tau(\mathcal{L}_q))$ for every contractible $\varrho$.

1. $\mathrm{LocSys}_{\check{G}_q}^{(1)}(X) = \mathrm{LocSys}_{\check{G}_q}(X)$ (all $q$-local systems).
2. The $q$-GL equivalence $\mathbb{L}_q$ ([$q$-GL conjecture](#conj:q-geometric-langlands)) restricts to each filtered piece:
   $$
     \mathbb{L}_q^{(n)} \colon
     \mathcal{D}_q^{(n)}\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q})
     \xrightarrow{ \sim }
     \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}^{(n)}(X)).
   $$
   Here, $\mathcal{D}_q^{(n)}$ consists of $q$-$\mathcal{D}$-modules whose Hecke eigenvalues have $n$-divisible monodromy.
3. The sublocus $\mathrm{LocSys}_{\check{G}_q}^{(n)}$ admits lifts through the brane tower only when $n \mid \chi(A)$ ([obstruction calculation](#prop:q-gl-obstruction-calc)). At levels $n \nmid \chi(A)$, the perpetual obstruction prevents full lifting.
4. The $q$-GL equivalence $\mathbb{L}_q$ is well-defined as a $\mathbb{G}_m$-family on $\mathbb{G}_m^{\mathrm{nt}} = \mathbb{G}_m \setminus \mu_\infty$.
