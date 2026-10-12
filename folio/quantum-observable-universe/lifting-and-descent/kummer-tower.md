Stacking the Kummer sequences for all $n$ gives the **Kummer tower**. This filters $\mathbb{G}_m$ by its torsion subgroups:
$$
  \mu_1 \subset \mu_2 \subset \mu_3
  \subset \cdots \subset
  \mu_\infty \subset \mathbb{G}_m.
$$
The subgroup $\mu_\infty = \bigcup_{n \geq 1} \mu_n$ contains all roots of unity. This filtration induces a descending filtration on the obstruction:
$$
  \kappa  \in 
  F^1 H^2 \supset F^2 H^2 \supset F^3 H^2
  \supset \cdots,
  \qquad
  F^n H^2 = nH^2(\mathcal{S}, \mathbb{G}_m).
$$
The class $\kappa$ lies in $F^n$ if and only if it is $n$-divisible ($\kappa \bmod n = 0$).

**The trace and divisibility.** The [QU-to-QOU theorem](#thm:qu-to-qou) establishes that the first obstruction is the Euler class of the Reeb bundle: $\kappa_0 = e(\xi)$, with trace $\mathrm{tr}(\kappa_0) = \chi(A)$. The divisibility of this trace controls the Kummer reduction at level $n$:
$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(A).
$$
The obstruction $\kappa_0$ vanishes at precisely the Kummer levels $n$ that divide $|\chi(A)|$. It persists at all others. For any non-zero Euler characteristic, this gives a finite set of vanishing levels and a density-$1$ set of persisting levels.

**Complementary subgroup structure.** The obstruction at level $n$ in the brane tower ([QU-to-QOU](#thm:qu-to-qou), item 3) decomposes as:
$$
  \kappa_n = \kappa_0 + \delta_n,
$$
where $\delta_n$ is the jet correction at level $n$. The classes $\kappa_0$ and $\delta_n$ live in complementary subgroups of $H^2(\mathcal{S}, \mathbb{G}_m)$. The Euler class $\kappa_0$ is a topological invariant. The class $\delta_n$ is an analytic correction. They cannot cancel. Their sum $\kappa_n$ is nonzero whenever $\kappa_0$ is non-torsion.

This establishes the **perpetual obstruction** phenomenon. A non-torsion Euler class $\kappa_0$ produces a non-vanishing obstruction at every level of the brane tower. Jet refinement cannot remove it.

*Scope.* For the bands used in this corpus the complementary-subgroup step is not established on a closed surface such as Bring's. There $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$, so the jet corrections $\delta_n$ vanish. For the band $\mathbb{Z}$, the group $H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$ has no non-trivial complement. For $\mathcal{O}^{\times}$ and $\mathbb{G}_m$, the obstruction group itself is zero. See the scope note in the [proof of QU-to-QOU](#prf:qu-to-qou). On a smooth projective curve over an algebraically closed field, $H^2(\mathcal{S}, \mathbb{G}_m) = 0$ as well, so the divisibility statement above is properly a statement about the $\mu_n$-valued class, the degree modulo $n$.

**Summary.** For any quantum universe with non-zero Euler characteristic $\chi(A) \neq 0$:
1. The obstruction $\kappa_0$ is non-trivial.
2. The Kummer tower filters the obstruction space by divisibility.
3. The obstruction persists at all Kummer levels $n \nmid \chi(A)$.
4. The complementary subgroup structure prevents jet corrections from cancelling the topological obstruction.
5. Properties of $\mathbf{C}_q$ depending on the vanishing of $\kappa_0 \bmod n$ must contend with this arithmetic obstruction at each level.
