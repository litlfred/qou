The Hoefsmit seminormal form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)) diagonalises $H_n(q)$ on $V^{\otimes n}$ along a Young--Jucys--Murphy tower indexed by standard tableaux, each generator $\sigma_i$ splitting a tableau-vector into a symmetric ($q$-eigen) and an antisymmetric ($-q^{-1}$-eigen) component. Writing $\mathrm{Tab}(\lambda)$ for the standard tableaux of shape $\lambda$ and $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ for the dyadic surreals of birthday $\leq n$, there is a canonical injective embedding

$$
  \Phi : \bigsqcup_{\lambda \vdash n,\, \ell(\lambda) \leq 2} \mathrm{Tab}(\lambda) \hookrightarrow \mathbf{No}_{\leq n}^{\mathrm{dy}}
$$

such that:
1. The empty tableau at $n = 0$ and the singleton tableau at $n = 1$ both map to $0$. For $n \geq 2$, the one-row tableau $(n)$ maps to a non-zero value determined by its sign sequence.
2. Each YJM-edge $t \to t'$ in the tableau forest corresponds to a unique sign-sequence extension $s \to s\!\cdot\! +$ (symmetric channel) or $s \to s\!\cdot\! -$ (antisymmetric channel). The sign sequence of a size-$n$ tableau has length $n - 1$.
3. The birthday $b(\Phi(t))$ is bounded by the length of the sign sequence (i.e., by $n - 1$). Surreals in the image are of birthday $\leq n - 1$. The complement of the image in $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ consists of non-tableau dyadic rationals.

The eigencomponent recursion, the tableau-forest counting, and the consequences of this identification (birthday-refined crossing number, the Conway-recipe form of $\rho_\lambda(\sigma_i)$, and the surreal sign-sequence expansion of $J_K(q)$) are recorded in the [context note](#rem:hoefsmit-is-surreal-construction-context).
