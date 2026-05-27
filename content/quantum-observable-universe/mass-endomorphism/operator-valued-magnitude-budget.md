For the deuteron interface $I \in H_6(q)$, the operator-valued
branching identity
[`prop:hecke-branching-trace-decomposition`](#prop:hecke-branching-trace-decomposition)
expands $\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)$ as a sum over
$(\mu, \nu)$ blocks of traces of $A^\lambda_{\mu,\nu}(I) \in \operatorname{End}(V_\mu \otimes V_\nu)^{\oplus c}$.

A *scalar-substrate ansatz* approximates each $A^\lambda_{\mu,\nu}(I)$
by its best scalar multiple of the identity:

$$
A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \;:=\; \frac{\operatorname{tr} A^\lambda_{\mu,\nu}(I)}{d_\mu \cdot d_\nu} \cdot \mathbf{1}_{V_\mu \otimes V_\nu}.
$$

By orthogonality of the scalar and traceless components under the
Hilbert–Schmidt inner product (Pythagoras), the operator-valued
residual has Frobenius norm

$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \bigr\|_F^2 \;=\; \bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2 \;-\; \frac{\bigl| \operatorname{tr} A^\lambda_{\mu,\nu}(I) \bigr|^2}{d_\mu \cdot d_\nu}.
$$

Summing across all $35$ $(\lambda, \mu, \nu)$ blocks of the H_6
deuteron-interface decomposition:

| Quantity | Frobenius |
|---|---|
| Scalar-approximation total | $3.517$ |
| Operator-valued residual total | $3.603$ |
| Non-scalar blocks | $19 / 35$ |

The operator-valued residual magnitude **exceeds** the scalar
approximation magnitude. Symmetric scalar substrate ansatze recover
less than half of the structural Frobenius content of the
$A^\lambda_{\mu,\nu}(I)$ family.

This is the quantitative magnitude budget that drives the
[`structural-diagnosis-operator-valued`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-17-structural-diagnosis-operator-valued.md)
audit's conclusion: the symmetric scalar substrate cannot, in
principle, account for the empirical Z$\leftrightarrow$N-asymmetric mass-formula
residuals (Δ_coupling +0.796 MeV; T5 −0.325 MeV) — those are
operator-valued at the per-Wedderburn-block level by construction.
