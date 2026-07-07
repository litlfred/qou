**Definition.**
*The per-nucleon channel decomposition of the typed Garside element for a nucleus of mass number $A$ is the factorization*

$$
  G(c_1, \ldots, c_A)
  = \prod_{m=1}^{A} G_{n_m}(c_m),
$$

*where each per-nucleon factor $G_{n_m}(c_m)$ is the expectation value of $\Delta_3$ in the $T_{2,3}$ eigenvector of channel $c_m$, $n_m \in \{P, N\}$ is the nucleon type, and $c_m \in \{\mathrm{triv}, \mathrm{conf}, \mathrm{unconf}, \mathrm{sign}\}$ ranges over the four channels of the $T_{2,3}$ eigenstructure of $H_3(q)$.*

## $S_3^A$ branching

The typed Garside element acts on $V^{\otimes 3A}$. The $S_3^A$ branching rule decomposes this action into a product of $A$ per-nucleon factors.

## Four channels from $T_{2,3}$ eigendecomposition

The trefoil operator $T_{2,3} = \sigma_0 \sigma_1 \sigma_0$ in $H_3(q)$ has four eigenvalues corresponding to four channels:

1. **Trivial** ($\lambda = q^3$): fully symmetric channel
2. **Confining** ($\lambda = q^{-1}$): standard representation, confining component
3. **Unconfining** ($\lambda = -q$): standard representation, anti-confining component
4. **Sign** ($\lambda = -q^{-3}$): fully antisymmetric channel

## Per-nucleon channel data

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


**Terms defined:** :defterm[per-nucleon-channel-decomposition]
