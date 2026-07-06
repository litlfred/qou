The Skein resolution obstruction provides a fourth evaluation of the universal obstruction class $\chi(A) \in HH^2 \cong k$ ([QOU obstruction reduction](#thm:qou-obstruction-reduction)). It measures whether the degree-$0$ answer $P_L(q)$ can be extracted from the resolution tree in polynomial depth.

**Definition.** Let $L = \hat{\beta}$ be a link with $c$ crossings and $\mathcal{R}(L)$ its Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)). The **Skein resolution obstruction** is the image of the universal class under the resolution-tree restriction map:

$$
  \kappa_c^{\mathrm{comp}}(L, q)
  = 
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)
   \in 
  H^2(\mathcal{R}, \mathbb{G}_m),
$$

where $\mathrm{res}_{\mathcal{R}} \colon HH^2(\mathrm{Ad}) \to H^2(\mathcal{R}, \mathbb{G}_m)$ evaluates the unique obstruction scalar $\chi(A)$ on the resolution tree of $L$.

This joins the spectral (RH), collision (NS), and elliptic (BSD) restrictions ([QOU obstruction reduction](#thm:qou-obstruction-reduction)). All four map the same class in $HH^2 \cong k$. Since $HH^2$ is one-dimensional, they are proportional: the single integer $\chi(A) = -6$ controls whether each problem persists through the classical limit.

**Kummer reduction.** The Kummer filtration ([Kummer filtration](#rem:kummer-filtration-obstruction)) applies directly:

$$
  \kappa_c^{\mathrm{comp}} \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

The obstruction vanishes at the divisors of $|\chi(A)| = 6$ (levels $\{1, 2, 3, 6\}$) and persists otherwise. Computationally, the Kummer level $n$ corresponds to the root-of-unity $q_n = e^{2\pi i/n}$:

- At $n \mid 6$ (vanishing torsion): the Iwahori--Hecke algebra at $q_n$ contains a radical that prunes the resolution tree — the BQP mechanism.
- At $n \nmid 6$ (persisting torsion): quantum interference at this root of unity cannot collapse the tree.

**Field dependence.** Over a finite field $\mathbb{F}_p$, the substrate parameter $q \in \mathbb{F}_p^\times$ is always $\mathbb{G}_m$-torsion (order dividing $p - 1$). The Kummer reduction at level $p - 1$ controls the obstruction:

$$
  \kappa_c^{\mathrm{comp}} \bmod (p-1) = 0
  \quad\Longleftrightarrow\quad
  (p - 1) \mid \chi(A).
$$

For $p > 7$, we have $p - 1 > 6 = |\chi(A)|$. Thus, $(p-1) \nmid 6$ and the obstruction persists modulo $p - 1$. However, the resolution tree over $\mathbb{F}_p$ possesses at most $p$ distinct weights — the computation terminates in bounded time. P = NP over finite fields is trivially true (finite lookup), not because the obstruction vanishes, but because the field is finite.

Over $\mathbb{R}$ at non-torsion $q_0 = 1.109978595554181\ldots$ (50 dps), no Kummer level applies. The Iwahori--Hecke algebra $H_n(q_0)$ is semisimple ($\mathrm{Rad} = 0$). The full $3^c$ tree survives, and the obstruction does not vanish.
