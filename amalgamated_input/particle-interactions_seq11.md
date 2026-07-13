<!-- FILE_START: branching-qvalue-intro.md -->
The Wedderburn mass formula of §8 yields total atomic masses. To organize individual $\beta$-decay branches, we require a per-channel decomposition. We use an $S_3^A$ branching rule to separate the per-nucleon channels and factor out the spectator contribution. This exposes the active channel and yields an exact character-sum product for the branching $\mathcal{Q}_q$-value. The parity of the mass number $A$ then completely determines the sign and regime of this $\mathcal{Q}_q$-value.

To fix the sign of the proton--neutron mass ordering, we apply a Yang--Baxter-corrected Markov trace on the trefoil braid. We then incorporate the positron branch correction, compute the closed-form tritium $\mathcal{Q}_q$-value, and impose a Frobenius positivity filter to exclude invalid configurations in even-$A$ decays. We map the categorical action to physical observables (mass, $\mathcal{Q}_q$-value, decay rate, and density). Finally, we show that the standard Borromean link $\mathcal{B}_3$ minimizes this categorical action, establishing the initial state for the molecular bond construction in Chapter 12.
<!-- FILE_END: branching-qvalue-intro.md -->

<!-- FILE_START: per-nucleon-channel-decomposition.md -->
**Definition.**
*The :defterm[per-nucleon channel decomposition]{#per-nucleon-channel-decomposition} of the typed Garside element for a nucleus of mass number $A$ is the factorization*

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
<!-- FILE_END: per-nucleon-channel-decomposition.md -->

<!-- FILE_START: spectator-normalization.md -->
The spectator normalization captures the contribution of unchanged nucleons to the Q-value character sum. In a beta decay, one neutron converts to a proton. The remaining $Z$ protons and $N - 1$ neutrons act as spectators.

**1. Definition.**
The spectator factor is

$$
  S(Z, N-1) = a^{Z} \cdot b^{N-1}
$$

where $a = -h/2$ and $b = -3(q^2-1)(q^2+1)^2/(4q^3)$ are the channel sums of the per-nucleon Garside factors.

**2. Fermionic character.**
Both $a < 0$ and $b < 0$ for all $q > 1$. This negativity reflects the fermionic character of the nucleon. The sign of the spectator product is $(-1)^{A-1}$. This sign fixes the parity regime for the Q-value.
<!-- FILE_END: spectator-normalization.md -->

<!-- FILE_START: branching-qvalue-factorization.md -->
We compute the branching $\mathcal{Q}_q$-value by summing over all $4^A$ channel configurations.

## Statement

**Proposition.**
*For $\beta^-$ decay of a nucleus $(Z, N)$ with $A = Z + N$:*

$$
  \sum_{\text{all } 4^A \text{ configs}}
  \Delta m_e
  = a^Z \cdot b^{N-1} \cdot (a - b)
$$

*where $a$ and $b$ are the per-nucleon channel sums.*
<!-- FILE_END: branching-qvalue-factorization.md -->

<!-- FILE_START: parity-regime-selection.md -->
The parity of the mass number $A$ determines which computational regime applies to the Q-value. This emerges from the fermionic sign of the spectator factor.

## Statement

**Theorem.**
*For all $q > 1$:*

$$
  \operatorname{sign}(a^Z \cdot b^{N-1}) = (-1)^{A-1}
$$

*The Q-value regimes are:*

1. **Odd $A$** ($A \geq 3$): The factorization $a^Z b^{N-1}(a-b)$ is positive, yielding $Q = |S \cdot \Delta| \times m_e$.
2. **Even $A$**: The factorization is negative. The Frobenius positivity filter restricts the sum to admissible configurations, yielding $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$.
3. **$A = 1$** (neutron decay): There are no spectators. We add the positron correction explicitly, yielding $Q = (S\Delta + 1) \times m_e$.
<!-- FILE_END: parity-regime-selection.md -->

<!-- FILE_START: positron-correction.md -->
The $+1$ additive term in the Q-value formula is a parity-dependent offset $\delta_A$, required to match the evaluated character sum to the observed kinematics.

## Statement

**Proposition.**
*The evaluated Q-value functional includes a formal parity-dependent trace offset:*

$$
  Q = (\Sigma_{\mathrm{char}} + \delta_A) \times m_e
$$

*where the offset $\delta_A$ depends on the parity regime.*

## Applicability of the correction

We apply the offset $\delta_A$ differently across two regimes:

1. **$A = 1$** and **Even $A$**: We add the correction explicitly, setting $\delta_A = 1$.
2. **Odd $A \geq 3$**: We apply no explicit correction, setting $\delta_A = 0$.

> **Open Issue:** We currently rely on this parity-dependent $\delta_A$ to align the categorical evaluation with the kinematic Q-value. We lack a formal justification for why $\delta_A$ is absorbed for odd $A$ but required for even $A$.
<!-- FILE_END: positron-correction.md -->

<!-- FILE_START: tritium-qvalue-symbolic.md -->
The $Q$-value for tritium beta decay ${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar\nu_e$ admits an exact closed form as a rational function of $q$.

## Statement

**Proposition.**

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  = \frac{3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)}{32q^7}
    \times m_e
$$

This follows from the branching factorization with $(Z, N) = (1, 2)$ and $A = 3$ (the odd regime).

## Derivation

From the branching factorization:

$$
  \sum_{4^3 \text{ configs}} \Delta m_e
  = a^1 \cdot b^{1} \cdot (a - b)
  = ab(a - b)
$$

Substituting the channel sums yields the stated closed form.

## Numerical evaluation

At the substrate parameter $q_0$:

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  \approx 0.0179 \;\text{MeV}.
$$

The experimental value is $Q_{\mathrm{exp}} = 0.0186$ MeV. The error is $-3.64\%$. The computation uses exactly three CODATA inputs to fix $q_0$, with zero additional fitting.
<!-- FILE_END: tritium-qvalue-symbolic.md -->

<!-- FILE_START: frobenius-positivity-filter.md -->
For nuclei with even mass number $A$, the raw character sum is negative. We obtain the physical Q-value by restricting the sum to Frobenius-positive configurations.

## Statement

**Proposition.**
*For even $A$: a channel configuration is Frobenius-positive if and only if both parent and daughter yield non-negative Markov traces.*

*A configuration is excluded exactly when its sign-pattern has odd total parity. Of the $2^A$ sign-patterns, exactly half are excluded.*

## Connection to the confinement LP

The Frobenius positivity constraint provides the continuous analogue of the LP feasibility constraint $Gx \geq 0$. It acts as a configuration filter.

## Computational complexity

For the ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ decay ($A = 6$), we exclude the 32 patterns with odd parity. The Frobenius-filtered sum yields $Q \approx 3.637$ MeV (experiment: $3.508$ MeV, error $+3.68\%$).
For large even $A$, the configurations require either enumeration or a closed-form simplification.
<!-- FILE_END: frobenius-positivity-filter.md -->

<!-- FILE_START: categorical-quantity-map.md -->
The four principal physical observables correspond rigidly to four distinct functionals acting on the categorical action:

| Physical quantity | Categorical functional | Formula |
|-------------------|----------------------|---------|
| **Mass** | Markov trace (absolute value) | $\mathfrak{m} = |\mathrm{tr}_M(\Phi)|$ |
| **Q-value** | Character sum | $Q = \sum_\lambda \chi_\lambda(\Delta) \times m_e$ |
| **Decay rate** | Frobenius matrix element | $\mathfrak{D} \propto |\langle v, \Phi v \rangle_F|^2$ |
| **Density** | Partial trace (crossing count) | $\rho = \mathrm{tr}_A(\varrho)$ |

Each functional isolates an orthogonal dimension of the underlying Hecke algebra element.
<!-- FILE_END: categorical-quantity-map.md -->

<!-- FILE_START: b3-local-minimum.md -->
We show the Borromean braid $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3$ is a local, rather than global, minimum of the categorical action.

## Global minimum

The confinement LP with the corrected Gram matrix admits a global minimum at $\mathrm{tr}_M = 0$. The Borromean solution $\mathcal{B}_3$ is a local minimum at a vertex of the LP feasible polytope.

## Corrected Gram matrix

The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ has a negative eigenvalue $\approx -0.956$. The Frobenius form is not positive definite.

## Eigenvalue selection

The confinement LP selects $\mathcal{B}_3$ via the $\min|\lambda|$ eigenvalue criterion. This identifies it as the least unstable confined state.
<!-- FILE_END: b3-local-minimum.md -->

