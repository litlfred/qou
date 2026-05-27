**Proposition (knot factor as chirality Gram pairing).**
*Let $\mathcal{K}$ be a knot with braid representative
$\beta_\mathcal{K} \in B_n$ and mirror $\beta_\mathcal{K}^*$, working
over $A = H_n(R, q)$.  The knot factor $a_\mathcal{K}$ in the unified
mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
is the normalised chirality Gram pairing*

$$
  a_\mathcal{K} \;=\;
  \frac{G_{\beta_\mathcal{K},\, \beta_\mathcal{K}^*}}
       {G_{\mathbf{1},\, \mathbf{1}}}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    w_\lambda \,
    \frac{\chi_\lambda(\beta_\mathcal{K})\, \chi_\lambda(\beta_\mathcal{K}^*)}
         {\chi_\lambda(\mathbf{1})^2},
$$

*with Plancherel weights $w_\lambda = \dim_q^2 V_\lambda / [n]_q!$
summing to $1$.  The identity is exact in $R$.*

*Proof.*
By
([Gram--spectral connection](#rem:gram-matrix-spectral-connection)),
the Gram matrix is block-diagonal in the central-idempotent basis
$\{e_\lambda\}$ with entries
$G_{\lambda \mu} = \delta_{\lambda \mu} \cdot \dim_q V_\lambda \cdot
\dim V_\lambda / [n]_q!$.  Expanding $\beta_\mathcal{K}, \beta_\mathcal{K}^*$
in $\{e_\lambda\}$ and substituting yields the displayed sum, which
is the depth-stratified specialisation of the unified mass functional
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
restricted to the chirality projection.  $\square$
