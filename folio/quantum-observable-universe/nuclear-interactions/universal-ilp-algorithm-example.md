The [universal ILP algorithm](#def:universal-ilp-algorithm) at the four levels of the construction:

| Level | Input | Frobenius | ILP selects | Crossings |
|:------|:------|:----------|:-----------|:----------|
| Quarks $\to$ confinement | uud | **FAIL** | $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | 6 |
| Proton $\to$ gluon | $\mathcal{B}_3 \times$ quarks | **FAIL** | $\sigma_0 \sigma_0$ | 2 |
| Proton $\to$ H atom | proton + gluon | **PASS** | $\sigma_1^{-1}$ | 1 |
| H $\to$ H$_{2}$ molecule | H atom | **PASS** | $T_{2,3}^{-1}$ | 3 |

At every level, the algorithm uses the same Gram matrix $G$ and the same Frobenius positivity constraint. The only difference between levels is the **topological constraint**:

- Step 2a (unstable): the operator must be a **braid group element**.
- Step 2b (stable): the operator must be a **knot**.
