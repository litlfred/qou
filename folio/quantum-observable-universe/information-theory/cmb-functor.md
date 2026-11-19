Let $\partial$ be the horizon functor and let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the brane tower. The **CMB functor** is the composite

$$
  \mathrm{CMB}
   \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\partial}
  \mathcal{P}\!\bigl(\mathrm{Bun} \setminus \mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\varinjlim (A_1/A_0 \oplus A_2/A_0)}
  \mathbf{Mod}_R,
$$

so that on an aeon $\mathcal{A}$

$$
  \mathrm{CMB}(\mathcal{A})
  = 
  \varinjlim_{\mathcal{S} \in \partial(\mathcal{A})}
  \bigl(A_1/A_0 \oplus A_2/A_0\bigr)\big|_{\mathcal{S}},
$$

where the colimit is taken over the directed system of all diagrams in $\mathcal{A}$ converging to boundary objects, and $\mathbf{Mod}_R$ is the category of $R$-modules of sections of the jet quotient sheaves over the boundary.
