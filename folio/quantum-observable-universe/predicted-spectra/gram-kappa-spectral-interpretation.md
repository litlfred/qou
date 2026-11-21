**Numerical check at $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps).**

The Hoefsmit pipeline ([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) computes $\chi_\lambda(\beta_s)$ and $\chi_\lambda(\beta_w)$ in seminormal form. At strand count $n = 9$, the hook partitions $(8,1)$ and $(7,1,1)$ and the rectangular partition $(5,4)$ are the dominant blocks. Substituting the Plancherel weights $w_\lambda = \dim_q^2(V_\lambda)/[n]_q!$ and character values yields

$$
  \kappa \;\approx\; 1.722.
$$

No committed producer reproduces this evaluation, and the product it evaluates is not yet well defined ([open conjecture](#conj:gram-determinant-plancherel-ratio)), so its agreement with the value computed from the [Gram determinants](#def:cs-gram-determinant-ratio) is unverified.

**Structural comparison.**

| Old derivation | Spectral derivation |
|---|---|
| Ratio of $2{\times}2$ Gram matrix determinants at $J^2$ jet | Plancherel-weighted character product over Wedderburn blocks |
| 2-jet truncation chosen by hand | Full $\lambda \vdash n$ sum over the finitely many $\lambda \vdash n$ |
| Tied to Bring-surface coordinate calculation | Categorical: depends only on $\chi_\lambda(\beta_\bullet)$ |
| Result $1.722$ computed from the two determinants | Result would be determined by the $\lambda$-blocks of the genus-$4$ pair, if the conjecture holds |

**Symbolic form.**

The formula evaluates symbolically over $R$ to a $q$-rational expression for $\kappa$. It specializes numerically via $\iota \colon R \to \mathbb{R}$ at $q \mapsto q_0$. Character values $\chi_\lambda(T_{m,n})$ for torus knots are polynomial in $q^{\pm 1}$ \cite{jones1987}. The formula reduces to a finite product of Laurent monomials.

**Sensitivity.**

The logarithmic derivative $\partial \ln \kappa / \partial \ln q$ at $q_0$ measures the shift of Wedderburn block weights with the substrate parameter. The $q$-deformed weights do **not** sum to $1$ away from $q = 1$ ($\sum_\lambda w_\lambda(q) = 0.987$ at $n = 3$, $1.051$ at $n = 8$); the sum is finite because $\lambda$ ranges over the partitions of $n$, not because it is normalised. The sensitivity is bounded by $\max_\lambda |c_\lambda^{(s)} c_\lambda^{(w)}| \cdot |\partial \ln(\dim_q V_\lambda)/\partial \ln q|$. This bound is finite and computable.
