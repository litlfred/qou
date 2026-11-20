For the deuteron interface $I \in H_6(q)$, the operator-valued branching identity ([Hecke branching trace decomposition](#prop:hecke-branching-trace-decomposition)) expands $\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)$ as a sum over $(\mu, \nu)$ blocks of traces of $A^\lambda_{\mu,\nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c}$.

A scalar-substrate ansatz approximates each $A^\lambda_{\mu,\nu}(I)$ by its best scalar multiple of the identity:
$$
A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \;:=\; \frac{\mathrm{tr} A^\lambda_{\mu,\nu}(I)}{d_\mu \cdot d_\nu} \cdot \mathbf{1}_{V_\mu \otimes V_\nu}.
$$

By the orthogonality of the scalar and traceless components under the Hilbert–Schmidt inner product, the operator-valued residual holds Frobenius norm:
$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \bigr\|_F^2 \;=\; \bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2 \;-\; \frac{\bigl| \mathrm{tr} A^\lambda_{\mu,\nu}(I) \bigr|^2}{d_\mu \cdot d_\nu}.
$$

Summing across all $35$ $(\lambda, \mu, \nu)$ blocks of the $H_6$ deuteron-interface decomposition yields:

| Quantity | Frobenius |
|---|---|
| Scalar-approximation total | $3.517$ |
| Operator-valued residual total | $3.603$ |
| Non-scalar blocks | $19 / 35$ |

The operator-valued residual magnitude **exceeds** the scalar approximation magnitude. Symmetric scalar substrate ansätze recover less than half of the structural Frobenius content of the $A^\lambda_{\mu,\nu}(I)$ family.

This quantitative magnitude budget forces the structural conclusion. The symmetric scalar substrate cannot account for the empirical Z$\leftrightarrow$N-asymmetric mass-formula residuals ($\Delta_{\text{coupling}}$ +0.796 MeV; T5 −0.325 MeV). We construct these residuals to be operator-valued at the per-Wedderburn-block level.
