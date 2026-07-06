**Numerical check at $q_0 = 1.109978595554181\ldots$ (50 dps).**

The Hoefsmit pipeline ([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) computes $\chi_\lambda(\beta_s)$ and $\chi_\lambda(\beta_w)$ in seminormal form. At strand count $n = 9$, the dominant blocks are the hook partitions $(8,1)$ and $(7,1,1)$, and the rectangular partition $(5,4)$. Substituting the Plancherel weights $w_\lambda = \dim_q^2(V_\lambda)/[n]_q!$ and character values yields

$$
  \kappa \;\approx\; 1.722.
$$

This matches the previous 2-jet hand computation, but now derives from the Wedderburn block structure without arbitrary truncation.

**Structural comparison.**

| Old derivation | Spectral derivation |
|---|---|
| Ratio of $2{\times}2$ Gram matrix determinants at $J^2$ jet | Plancherel-weighted character product over Wedderburn blocks |
| 2-jet truncation chosen by hand | Full $\lambda \vdash n$ sum, convergent by Plancherel ($\sum w_\lambda = 1$) |
| Tied to Bring-surface coordinate calculation | Categorical: depends only on $\chi_\lambda(\beta_\bullet)$ |
| Result $1.722$ stated as numerical fact | Result $1.722$ determined by which $\lambda$-blocks the genus-$4$ pair occupies |

**Lean handle.**

The formula evaluates symbolically over $R$ to a $q$-rational expression for $\kappa$, or specializes numerically via $\iota \colon R \to \mathbb{R}$ at $q \mapsto q_0$. Character values $\chi_\lambda(T_{m,n})$ for torus knots are polynomial in $q^{\pm 1}$ \cite{jones1987}. Thus, the formula reduces to a finite product of Laurent monomials.

**Sensitivity.**

The logarithmic derivative $\partial \ln \kappa / \partial \ln q$ at $q_0$ measures how Wedderburn block weights shift with the substrate parameter. Since $\sum_\lambda w_\lambda = 1$ at every $q$, the sensitivity is bounded by $\max_\lambda |c_\lambda^{(s)} c_\lambda^{(w)}| \cdot |\partial \ln(\dim_q V_\lambda)/\partial \ln q|$. This bound is finite and computable.
