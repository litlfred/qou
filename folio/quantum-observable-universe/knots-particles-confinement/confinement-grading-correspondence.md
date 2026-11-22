**Conjecture (confinement = KLR grading shift).**
*Under the Brundan–Kleshchev isomorphism \cite{brundankleshchev2009}, the confinement filtration $J^\bullet(q)$ on $H_n(R, q)$ coincides with the filtration induced by the natural $\mathbb{Z}$-grading on the KLR algebra \cite{khovanovlauda2009}. A closed braid $K$ with normal form $T_w$ has confinement level $\ell(K, q)$ if and only if its KLR-module lift $\mathfrak{M}_K$ has top non-zero graded piece in degree $\ell(K, q)$:*

$$
  T_w \in J^\ell(q) \setminus J^{\ell+1}(q)
  \;\iff\;
  (\mathfrak{M}_K)_d = 0 \;\;\text{for}\;\; d > \ell.
$$

**Computational role.**
*One enforces the KLR grading bound before any crystal step. Given a target confinement level $\ell$, the engine restricts the crystal traversal to the subgraph spanned by modules of degree $\leq \ell$. Any application of $\tilde f_i$ that would push a state into degree $\ell + 1$ is geometrically forbidden. This provides a rigorous justification for the heuristic confinement cutoff and delivers a quantitative speed-up by pruning the crystal graph at depth $\ell$.*

**Conjectural status.**
*The KLR grading is unique up to isomorphism, and the Brundan–Kleshchev isomorphism intertwines it with the centre of $H_n(R, q)$. It is conjectured that the filtration arising from the LP shadow-price ordering on knot-operator energies strictly agrees with the KLR grading filtration. This is supported by all witnessed atom knots up to $k_{\max} \leq 7$.*
