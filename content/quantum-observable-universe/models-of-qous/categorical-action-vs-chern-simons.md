The classical Chern–Simons action \cite{witten1988}

$$
  S_{\mathrm{CS}}[A_{\mathrm{cl}}]
  =
  \frac{k}{4\pi}\!\int_M \mathrm{Tr}\!\left(
    A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}}
    + \tfrac{2}{3}\, A_{\mathrm{cl}} \wedge A_{\mathrm{cl}} \wedge A_{\mathrm{cl}}
  \right)
$$

and the categorical action $\mathfrak{S} = \mathrm{tr}(\Phi)$ ([categorical action](#def:categorical-action)) share a common skeleton. Both are scalar functionals built by tracing an internal morphism. (Here $A_{\mathrm{cl}}$ is a $\mathfrak{g}$-valued connection $1$-form on a $3$-manifold $M$, distinct from the QOU observable object $A \in \mathbf{C}$.) They diverge in their encoding of integration and trace:

| | Chern--Simons | Categorical |
|---|---|---|
| Domain | $3$-manifold $M$ | rigid monoidal $(\mathbf{C}, A, \tau)$ |
| Integration | $\int_M \{-\}$ | $\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \{-\}) \circ \mathrm{coev}_A$ |
| Trace | Lie-algebra $\mathrm{Tr}_{\mathfrak{g}}$ | categorical (rigid) trace on $A$ |
| Dynamics | explicit $A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}} + \tfrac{2}{3} A_{\mathrm{cl}}^{\wedge 3}$ | packaged inside $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ |

In the archimedean limit ([physicist translation](#rem:physicist-translation)), the trace becomes $\int_M \{-\}\,\mathrm{dvol}$. The rigid loop closure $\mathrm{ev}_A \circ \{-\} \circ \mathrm{coev}_A$ yields spacetime integration without an independently postulated volume form; the rigid structure supplies it. The perturbative expansion $A_{\mathrm{cl}} = A_{\mathrm{cl}}^{(0)} + \mathcal{A}$ around a flat connection corresponds to fixing a background categorical connection and expanding $\Phi_q = \mathcal{D}_\nabla^2 + \cdots$ in fluctuations ([canonical action](#prop:qou-canonical-action)).

The bulk categorical action does not recover classical Chern–Simons. The archimedean image of $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ is the sum of the Einstein–Hilbert, Yang–Mills, and Dirac actions ([physicist translation](#rem:physicist-translation)). Classical Chern–Simons enters the framework separately as a geometric knot invariant for non-hyperbolic torus knots ([classical Chern--Simons as a non-hyperbolic knot invariant](#rem:chern-simons-as-knot-invariant)).
