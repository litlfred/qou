## Proposition: magic numbers from torus knot shell sizes

**Withdrawn (owner ruling 2026-11-21).** The shell-size rule used here, that a closing shell of size $n_s$ is bound by the torus knot $T_{2,n_s}$, is withdrawn. Its basis was a mislabel: $(\sigma_0\sigma_1)^2\sigma_0$ closes to $T(2,4)$, not to the cinquefoil $T(2,5)$. The rule stays withdrawn until it is derived. This block is kept as a record of the proposal, because other blocks cite it, and it is not a result. Its Lean sibling checks a hard-coded table and does not derive the rule.

Let $q > 1$, and build the nucleus by inductive Gröbner--Shirshov reduction, each shell-boundary crossing mediated by the inter-shell torus-knot operator $\Phi_{\mathrm{shell}}^{(\ell)}$ (Chebyshev crossing coefficients of $T_{2, n_s}$). A shell closes exactly when the word-length histogram of $\bar{\mathcal{N}}(p, n)$ is palindromic, at nucleon count $A_{\mathrm{close}}$, and the closing shell of size $n_s = A_{\mathrm{close}} - A_{\mathrm{prev}}$ is bound by $T_{2, n_s}$. Each embeddable torus knot $T_{r,s}$ on the Bring surface assigns a shell capacity

$$
  \bigl|\mathrm{shell}(T_{r,s})\bigr| = r \times s
$$

(see [Table 2](#tbl:torus-knot-shell-binding-table2-data)). The construction is **proposed** to reproduce the experimental magic numbers

$$
  \{2,\, 8,\, 20,\, 28,\, 50,\, 82,\, 126\}
$$

as cumulative same-type shell occupancies (see [Table 3](#tbl:torus-knot-shell-binding-table3-data)). Closing the full sequence as a from-$q$ derivation — in particular reconciling the $r\times s$ shell capacities with the Table-3 occupancies — is the **key open problem**, not established here. The Hecke energy gap at a shell boundary scales as $|\lambda_+(T_{2,n_s})/\lambda_-(T_{2,n_s})| = q^{2 n_s}$; for the first shell closure (He-4 $\to$ Li-5),

$$
  \frac{\Delta E_5}{\Delta E_4} \approx \frac{1.409}{0.095} = 14.8 .
$$
