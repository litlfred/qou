The [jet prolongation](#prop:jet-prolongation) is compatible with the braided monoidal structure. Suppose $\mathbf{C}$ is braided with braiding $c$, and each level $A_{n+1} = J^1(A_n)$ of the brane tower is an object of $\mathbf{C}$, with the section $\ell_n\colon A_n \to A_{n+1}$ and left inverse $r_n\colon A_{n+1} \to A_n$ morphisms of $\mathbf{C}$. Nothing has to be inherited: every pair of objects already carries the braiding $c$. What the tower needs is that the transition maps respect it, and this is naturality of $c$:
$$
  (\ell_n \otimes \ell_n) \circ c_{A_n, A_n} = c_{A_{n+1}, A_{n+1}} \circ (\ell_n \otimes \ell_n),
$$
and likewise for $r_n$. Applied factor by factor, $\ell_n^{\otimes k}$ and $r_n^{\otimes k}$ intertwine the braid-group representations $\rho_k$ on $A_n^{\otimes k}$ and $A_{n+1}^{\otimes k}$. The direct-limit algebra $\mathcal{A}_\infty = \varinjlim\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2))$ therefore carries a well-defined $B_k$-action for every $k$.
