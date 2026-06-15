The classical Chern--Simons action \cite{witten1988}

$$
  S_{\mathrm{CS}}[A_{\mathrm{cl}}]
  =
  \frac{k}{4\pi}\!\int_M \mathrm{Tr}\!\left(
    A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}}
    + \tfrac{2}{3}\, A_{\mathrm{cl}} \wedge A_{\mathrm{cl}} \wedge A_{\mathrm{cl}}
  \right)
$$

(here $A_{\mathrm{cl}}$ is a $\mathfrak{g}$-valued connection
$1$-form on a $3$-manifold $M$, unrelated to the QOU observable
object $A \in \mathbf{C}$) and the
[categorical action](#def:categorical-action)
$\mathfrak{S} = \mathrm{tr}(\Phi)$ share a common skeleton: a scalar
functional built by tracing an internal morphism.  They differ in
how integration and trace are encoded:

| | Chern--Simons | Categorical |
|---|---|---|
| Domain | $3$-manifold $M$ | rigid monoidal $(\mathbf{C}, A, \tau)$ |
| Integration | $\int_M \{-\}$ | $\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \{-\}) \circ \mathrm{coev}_A$ |
| Trace | Lie-algebra $\mathrm{Tr}_{\mathfrak{g}}$ | categorical (rigid) trace on $A$ |
| Dynamics | explicit $A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}} + \tfrac{2}{3} A_{\mathrm{cl}}^{\wedge 3}$ | packaged inside $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ |

In the archimedean limit
([physicist translation](#rem:physicist-translation))
$\mathrm{tr} \to \int_M \{-\}\,\mathrm{dvol}$, so the rigid
"loop closure" $\mathrm{ev}_A \circ \{-\} \circ \mathrm{coev}_A$
*is* spacetime integration --- no volume form is postulated, the
rigid structure supplies it.  The perturbative saddle expansion
$A_{\mathrm{cl}} = A_{\mathrm{cl}}^{(0)} + \mathcal{A}$ around a
flat connection corresponds to fixing a background categorical
connection and expanding
$\Phi_q = \mathcal{D}_\nabla^2 + \cdots$ in fluctuations
([canonical action](#prop:qou-canonical-action)).

Classical Chern--Simons itself is **not** recovered as the bulk
categorical action: the archimedean image of
$\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ is
Einstein--Hilbert + Yang--Mills + Dirac, not CS
([physicist translation](#rem:physicist-translation)).  Classical
CS re-enters the framework elsewhere as a geometric *knot*
invariant for non-hyperbolic torus knots (see the corresponding
remark in the Descartes chapter).
