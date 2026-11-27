Let $\mathbf{C}$ be an $R$-linear rigid :refterm[monoidal category]{#monoidal-category}. Let
$$
  1  \longrightarrow  \mathcal{B}
   \longrightarrow  \mathfrak{G}'
   \longrightarrow  \mathfrak{G}
   \longrightarrow  1
$$
be a central extension of gerbes on a site $\mathcal{S}$, banded by an abelian sheaf $\mathcal{B}$. One says that $\mathbf{C}$ satisfies the **Quantum Lifting Condition** with respect to $(\mathfrak{G}', \mathfrak{G}, \mathcal{B})$ if, for every object $x \in \mathrm{Ob}(\mathfrak{G})$, the obstruction to lifting $x$ to an object $x' \in \mathrm{Ob}(\mathfrak{G}')$ is classified by a single cohomology class
$$
  \kappa(x)  \in  H^2(\mathcal{S}, \mathcal{B}),
$$
and $x$ admits a lift if and only if $\kappa(x) = 0$.

This is the categorical form of the gerbe central-extension obstruction of Yekutieli \cite{yekutieli2010}; one adopts the name *Quantum Lifting Condition* to emphasise its role in specialising the categorical aether.

**Proposition (Lean: `QOU.YekutieliLiftingCondition.ofCentralExtensions`, `QOU.CentralExtension.obstructionClass_eq_one_iff`).** Let $1 \to A_n \to E_n \to G_n \to 1$ ($n \in \mathbb{N}$) be central extensions of groups, $A_n$ commutative, and let $\varphi_n \colon H_n \to G_n$ be homomorphisms. Put $\kappa(\varphi_n) \in H^2(H_n, A_n)$ (trivial action) for the class of the obstruction cocycle of $\varphi_n$. Then $\varphi_n$ lifts to a homomorphism $H_n \to E_n$ if and only if $\kappa(\varphi_n) = 0$. Hence the data $\bigl(\prod_n H^2(H_n, A_n),\ n \mapsto \kappa(\varphi_n)\bigr)$ satisfy the Quantum Lifting Condition, with both directions proved rather than assumed.

*Proof.* Choose a set-theoretic section $\sigma_n$ of $E_n \to G_n$ and define $c(g,h) \in A_n$ by $\sigma_n(\varphi_n g)\,\sigma_n(\varphi_n h) = c(g,h)\,\sigma_n(\varphi_n(gh))$. Centrality of $A_n$ makes $c$ a 2-cocycle, and another section changes $c$ by the coboundary of $t\colon H_n \to A_n$ with $\sigma'_n = t\,\sigma_n$; so $\kappa(\varphi_n) = [c]$ in the commutative group $Z^2/B^2$ is independent of $\sigma_n$ (Lean: `obstructionClass_section_indep`). If $\psi$ is a lift, write $\sigma_n(\varphi_n g) = y(g)\,\psi(g)$; comparing the two expansions of $\sigma_n(\varphi_n g)\sigma_n(\varphi_n h)$ gives $c = \delta y$. Conversely, if $c = \delta x$ then $g \mapsto x(g)^{-1}\sigma_n(\varphi_n g)$ is multiplicative and lies over $\varphi_n$ (Lean: `exists_lift_iff_coboundary`). A class is trivial exactly when its representative is a coboundary, which gives the criterion. The obstruction of level $n$ is placed in the $n$-th factor of $\prod_n H^2(H_n, A_n)$, so it vanishes iff $\kappa(\varphi_n)$ does. $\square$

This is the group-level (one-object groupoid) case of Yekutieli's Thm 4.17 \cite{yekutieli2010}. The gerbe-level case over a site is open work.
