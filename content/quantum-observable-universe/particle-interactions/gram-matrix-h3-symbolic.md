**Proposition (symbolic Hoefsmit Gram on $H_3(q)$).** *Let $u = \sqrt{q}$ with $u > 0$ (equivalently $q > 0$). On the 6-element NF basis*

$$\{1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$$

*the Hoefsmit-seminormal Gram matrix $G(q)$ has the following 21 distinct (by symmetry) entries as Laurent polynomials in $u$:*

| Cell | Value |
|---|---|
| $G[0,0]$ | $1$ |
| $G[0,1] = G[0,2]$ | $u/(u^2+1) = \sqrt{q}/(q+1)$ |
| $G[0,3] = G[0,4] = G[1,2]$ | $u^2/(u^2+1)^2 = q/(q+1)^2$ |
| $G[0,5]$ | $(u^2 + u - 1)/(u^2+1)$ |
| $G[1,1] = G[2,2]$ | $(u^2 + u - 1)/u$ |
| $G[1,3] = G[1,4] = G[2,3] = G[2,4]$ | $(u^2 + u - 1)/(u^2+1)$ |
| $G[1,5] = G[2,5] = G[3,3] = G[4,4]$ | $(u^4 + u - 1)(u^4 + u^3 - 1)/[u^2(u^2+1)^2]$ |
| $G[3,4]$ | $((u^2 + u - 1)/u)^2$ |
| $G[3,5] = G[4,5]$ | $(u^{10} + u^9 - u^8 - u^5 + u^2 + u - 1)/[u^4(u^2+1)]$ |
| $G[5,5]$ | $(u^{12} + u^{11} - 2u^{10} - u^9 + 2u^8 + u^7 - u^6 - u^5 + 2u^4 + u^3 - 2u^2 - u + 1)/u^6$ |

*Then:*
1. *$G(q)$ is symmetric: $G[i,j] = G[j,i]$ for all $i, j$.*
2. *$G[0,0] = 1$.*
3. *$\det G(q) \neq 0$ for $q > 0,\ q \neq 1$.*
## Numerical evaluation at the substrate

Sympy-computed symbolic entries match `folio-assistant/computations/gram-matrix-dual.witness.json` at $q_0 \approx 1.110$ to max absolute difference $\approx 2.1 \times 10^{-16}$ across all 36 entries (see `gram-h3-symbolic-regression.witness.json` for the live value). The determinant at $u_0 = \sqrt{q_0}$ is $\det G(u_0) \approx -0.189205253071$ (one negative eigenvalue $\approx -0.855$ — Frobenius positivity is a genuine constraint, not an automatic property).

## Role in the framework

This proposition delivers the **Phase 1b** instance of [`def:universal-ilp-algorithm`](universal-ilp-algorithm.md)'s [`HasH3GramMatrix`](universal-ilp-algorithm.lean) typeclass — replacing the Phase 1a stub (`gram_matrix ≡ 0`) with categorical closed-form entries. Downstream consumers (operator-selection LP, Frobenius-positivity ILP, crystal-weight $\Delta_\lambda(K)$ derivation) can now consume the typeclass axioms with the structural properties **proved**, not just empirically observed at $q_0$.

The remaining $\det \neq 0$ proof (Phase 1b-2) reduces the entire Option E **Phase 1** workstream to a single, routine symbolic-determinant computation.

## Cross-references

- [`def:universal-ilp-algorithm`](universal-ilp-algorithm.md) — consumer of this proposition
- [`docs/audits/-option-e-crystal-weight-delta-lambda.md`](../../../docs/audits/-option-e-crystal-weight-delta-lambda.md) — full Phase 0/1/2/3/4 Option E workplan
- [`folio-assistant/computations/gram-matrix-dual.py`](../../../folio-assistant/computations/gram-matrix-dual.py) — pyhecke numerical Gram (regression guard)
- [`tools/pyhecke/python/pyhecke/gram.py`](../../../tools/pyhecke/python/pyhecke/gram.py) — canonical NF basis + TR_M definition
