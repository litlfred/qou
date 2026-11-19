For each channel $c$, the per-nucleon Garside factor $G(c)$ is the Frobenius matrix element of $\Delta_3$ in the $T_{2,3}$ eigenvector $v_c$.

**Proton** ($\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$), crossings:

$$
  \sigma_0(\mathfrak{u}\mathfrak{u}) \times [\sigma_1 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d}) \times [\sigma_0 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d})
$$

| Channel | $\lambda_c$ | $G_P(c)$ | Numeric at $q_0$ |
|:---:|:---:|:---:|:---:|
| Sym (Trivial) | $q^3$ | $q \cdot \tfrac{1}{2}[2]_q \cdot \tfrac{1}{2}[2]_q$ | $+1.122$ |
| Std $\lambda_1$ (Unconf.) | $-q$ | $\langle v_1, \Delta_3 v_1 \rangle_F$ | $-1.174$ |
| Std $\lambda_2$ (Conf.) | $q^{-1}$ | $\langle v_2, \Delta_3 v_2 \rangle_F$ | $+0.858$ |
| Alt (Sign) | $-q^{-3}$ | $(-q^{-1}) \cdot (-\tfrac{1}{2}[2]_q)^2$ | $-0.911$ |

**Channel sum:** $a = \sum_c G_P(c) = -h/2$.

**Neutron** ($\mathfrak{n} = \mathfrak{u}\mathfrak{d}\mathfrak{d}$), crossings:

$$
  [\sigma_0 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d}) \times [\sigma_1 - h](\mathfrak{d}\mathfrak{d}) \times [\sigma_0 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d})
$$

| Channel | $\lambda_c$ | $G_N(c)$ | Numeric at $q_0$ |
|:---:|:---:|:---:|:---:|
| Sym (Trivial) | $q^3$ | $\tfrac{1}{2}[2]_q \cdot q^{-1} \cdot \tfrac{1}{2}[2]_q$ | $+0.9108$ |
| Std $\lambda_1$ (Unconf.) | $-q$ | $\langle v_1, \Delta_3 v_1 \rangle_F$ | $-1.2222$ |
| Std $\lambda_2$ (Conf.) | $q^{-1}$ | $\langle v_2, \Delta_3 v_2 \rangle_F$ | $+0.7995$ |
| Alt (Sign) | $-q^{-3}$ | $(-\tfrac{1}{2}[2]_q) \cdot (-q) \cdot (-\tfrac{1}{2}[2]_q)$ | $-1.1221$ |

**Channel sum:** $b = \sum_c G_N(c) = -3(q^2-1)(q^2+1)^2/(4q^3)$.

The values $\{G_P(c), G_N(c)\}$ are algebraic functions of $q$ and determine all nuclear Q-values via the branching factorization.
