The correspondence between the Feynman path integral formalism and the QOU categorical trace is strict.

See [Table](#tbl:feynman-qou-dictionary-table-data).

**Three finite computations of the path integral.**
The categorical trace admits three independent evaluation methods, each producing the same finite answer without regularisation:

1. **Multiplicative integral** (analytic):
   $\mathfrak{m} = \lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$.
   The surface $\Sigma$ is the disc swept by the photon threading the hadron braid. The multiplicative integral accumulates the connection along this surface.

2. **Ribbon trace** (algebraic):
   $\mathfrak{m} = \lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))\rVert \cdot (q-1)^2$.
   The Reshetikhin--Turaev invariant evaluated in the ribbon category gives the crossing energy. The factor $(q-1)^2 = c_q^{-2}$ converts to mass.

3. **Gröbner--Shirshov reduction** (computational):
   $\mathfrak{m} = (q-1)^2 \sum |c_w| \cdot |q - q^{-1}|$.
   Each Hecke step $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ contributes a discrete term. Yang--Baxter moves are free. Confluence ensures path independence (gauge invariance).

**Photon threading as insertion of a complete set of states.**
The Feynman propagator inserts a complete set of intermediate states. The QOU analogue is photon threading. The photon strand $\gamma$ passes through the hadron braid $\beta_{\mathfrak{H}}$, encountering each crossing sequentially. Each crossing contributes a Hecke step (eigenvalue insertion). The braid crossings act as intermediate states. The Hecke relation provides the eigenvalue decomposition at each insertion.
