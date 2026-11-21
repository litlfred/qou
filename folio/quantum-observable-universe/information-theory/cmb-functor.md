To aggregate the cosmic microwave background across an entire boundary, one promotes the pointwise boundary datum to a functor. 

Let $\partial$ be the horizon functor  and let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the brane tower . The **CMB functor** maps each aeon $\mathcal{A}$ to the colimit of the degree $\geq 1$ jet quotients over its boundary. One defines this as the composition:

$$
  \mathrm{CMB}
   \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\partial}
  \mathcal{P}\!\bigl(\mathrm{Bun} \setminus \mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\varinjlim (A_1/A_0 \oplus A_2/A_0)}
  \mathbf{Mod}_R.
$$

Evaluated on an aeon $\mathcal{A}$, the functor yields:

$$
  \mathrm{CMB}(\mathcal{A})
  = 
  \varinjlim_{\mathcal{S} \in \partial(\mathcal{A})}
  \bigl(A_1/A_0 \oplus A_2/A_0\bigr)\big|_{\mathcal{S}}.
$$

The target category $\mathbf{Mod}_R$ consists of $R$-modules corresponding to sections of the jet quotient sheaves over the boundary.

| Factor | Jet degree | Content |
|:---|:---:|:---|
| $\varinjlim (A_1/A_0)\vert_{\partial\mathcal{A}}$ | $1$ | Linear transport: winding modes, first-order correlations |
| $\varinjlim (A_2/A_0)\vert_{\partial\mathcal{A}}$ | $2$ | Curvature: linking modes, power spectrum |

One takes the colimit over the directed system of all diagrams in $\mathcal{A}$ converging to boundary objects. This aggregates the degree $\geq 1$ data from every light cone reaching the boundary, not just a single computation sequence.

For a single boundary object $\mathcal{S}_0 \in \partial(\mathcal{A})$, the pointwise CMB  $\mathrm{CMB}(\mathcal{S}_0) = (A_1/A_0, A_2/A_0)|_{\mathcal{S}_0}$ is the stalk of the CMB functor at $\mathcal{S}_0$. The full CMB functor is the sheafification over the entire boundary.

By conformal invariance , the CMB functor does not depend on the choice of generator for the horizon ideal $\mathfrak{h} \subset A_0$. It depends solely on the vanishing locus—the conformal class of $A_0$.
