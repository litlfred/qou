Let $\mathbf{C}_{\mathrm{any}}(N)$ define the exact observable modular tensor category detailed in [def:observable-mtc](#def:observable-mtc), functioning specifically at level $N \geq 3$. Let $\mathbf{V}$ specify any definitively non-trivial simple object. Evaluating across every $n \geq 2$, the embedded categorical braiding directly generates a functional representation

$$
  \rho_n \colon B_n  \longrightarrow
   \mathrm{Aut}_{\mathbf{C}_{\mathrm{any}}(N)}(\mathbf{V}^{\otimes n}),
  \qquad
  \sigma_i  \longmapsto
   \mathrm{id}_{\mathbf{V}^{\otimes (i-1)}}
   \otimes\, c_{\mathbf{V}, \mathbf{V}}
   \otimes\, \mathrm{id}_{\mathbf{V}^{\otimes (n - i - 1)}},
$$

governing the Artin braid group $B_n$ (see [def:braid-group](#def:braid-group)) mapped onto the tensor power of $\mathbf{V}$. This representation does not factor through the symmetric-group quotient $B_n \twoheadrightarrow S_n$.
