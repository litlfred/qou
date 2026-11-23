Stacking the Kummer sequences for all $n$ gives the **Kummer tower**. This filters $\mathbb{G}_m$ by its torsion subgroups:
$$
  \mu_1 \subset \mu_2 \subset \mu_3
  \subset \cdots \subset
  \mu_\infty \subset \mathbb{G}_m.
$$
The subgroup $\mu_\infty = \bigcup_{n \geq 1} \mu_n$ contains all roots of unity. On a closed surface $\mathcal{S}$ the obstruction does not live in $H^2(\mathcal{S}, \mathbb{G}_m)$; on a curve that group is zero. It lives at each finite level. The Kummer sequence $1 \to \mu_n \to \mathrm{U}(1) \xrightarrow{(\cdot)^n} \mathrm{U}(1) \to 1$ assigns to a circle bundle $\xi$ the obstruction to an $n$-th root, a class in $H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n$.

**The Euler class and divisibility.** Item 2 of the [QU-to-QOU theorem](#thm:qu-to-qou) identifies the first obstruction of the Reeb bundle with its Euler class, $\kappa_0 = c_1(\xi) = e(\xi) = \chi(\mathcal{S})$. Item 3 identifies its image at Kummer level $n$:
$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(\mathcal{S}).
$$
The obstruction vanishes at precisely the Kummer levels $n$ that divide $|\chi(\mathcal{S})|$, and persists at all others. For non-zero Euler characteristic this gives a finite set of vanishing levels and a density-$1$ set of persisting levels. On Bring's surface, $\chi = -6$ and the vanishing levels are $n \in \{1, 2, 3, 6\}$; the case $n = 2$ is a spin structure.

**Not a jet-tower statement.** Earlier versions of this remark derived a *perpetual obstruction* at every level of the jet-prolongation tower from a complementary-subgroup decomposition $\kappa_n = \kappa_0 + \delta_n$. That decomposition is retracted. On a closed surface the jet corrections $\delta_n$ lie in the image of $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$, and $H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$ has no non-trivial complement. Persistence holds in the Kummer tower above, not in the jet tower. For the jet tower itself, see the [remark on jet-tower splitting](#rem:jet-tower-splitting-bring).

**Summary.** For a surface with non-zero Euler characteristic $\chi(\mathcal{S}) \neq 0$:
1. The obstruction $\kappa_0 = \chi(\mathcal{S})$ is non-trivial.
2. At Kummer level $n$ the obstruction is $\chi(\mathcal{S}) \bmod n \in H^2(\mathcal{S}, \mu_n)$.
3. The obstruction persists at all Kummer levels $n \nmid \chi(\mathcal{S})$.
4. Properties of $\mathbf{C}_q$ depending on the vanishing of $\kappa_0 \bmod n$ must contend with this arithmetic obstruction at each level.
