The :refterm[descent]{#descent} involution $\hat{\tau}_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution)) decomposes the level-$(n{+}1)$ endomorphism algebra into a direct sum:

$$
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
  = 
  \mathcal{A}_{n+1}^{\mathrm{desc}}  \oplus  \mathcal{A}_{n+1}^{\mathrm{trans}},
$$

where $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}_n$ is the descended subalgebra (endomorphisms that factor through level $n$) and $\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat{\tau}_n$ is the transient complement (genuinely new endomorphisms at level $n{+}1$). The algebraic filter ([algebraic filter](#rem:algebraic-filter)) refines this decomposition:

1. **Bosonic modes.** Longitudinal modes lifted from level $n$ lie entirely in $\mathcal{A}_{n+1}^{\mathrm{desc}}$. They commute with the curvature and survive every round-trip through the tower.
2. **Fermionic modes.** Ladder modes at level $n{+}1$ split between the two summands. Those in $\mathcal{A}_{n+1}^{\mathrm{trans}}$ are the modes created by the jet prolongation that lack a pre-image at level $n$.
