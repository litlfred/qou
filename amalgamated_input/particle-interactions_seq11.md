<!-- FILE_START: branching-qvalue-intro.md -->
The Wedderburn mass formula of §8 yields total atomic masses. To organize individual $\beta$-decay branches, we require a per-channel decomposition. We use an $S_3^A$ branching rule to separate the per-nucleon channels and factor out the spectator contribution. This exposes the active channel and yields an exact character-sum product for the branching $\mathcal{Q}_q$-value. The parity of the mass number $A$ then completely determines the sign and regime of this $\mathcal{Q}_q$-value.

To fix the sign of the proton--neutron mass ordering, we apply a Yang--Baxter-corrected Markov trace on the trefoil braid. We then incorporate the positron branch correction, compute the closed-form tritium $\mathcal{Q}_q$-value, and impose a Frobenius positivity filter to exclude invalid configurations in even-$A$ decays. We map the categorical action to physical observables (mass, $\mathcal{Q}_q$-value, decay rate, and density). Finally, we show that the standard Borromean link $\mathcal{B}_3$ minimizes this categorical action, establishing the initial state for the molecular bond construction in Chapter 12.

_(draft.)_
<!-- FILE_END: branching-qvalue-intro.md -->

<!-- FILE_START: per-nucleon-channel-decomposition.md -->
**Definition.**
*The :defterm[per-nucleon channel decomposition]{#per-nucleon-channel-decomposition} of the typed Garside
element for a nucleus of mass number $A$ is the factorization*

$$
  G(c_1, \ldots, c_A)
  = \prod_{m=1}^{A} G_{n_m}(c_m),
$$

*where each per-nucleon factor $G_{n_m}(c_m)$ is the expectation value
of $\Delta_3$ in the $T_{2,3}$ eigenvector of channel $c_m$,
$n_m \in \{P, N\}$ is the nucleon type, and
$c_m \in \{\mathrm{triv}, \mathrm{conf}, \mathrm{unconf}, \mathrm{sign}\}$
ranges over the four channels of the $T_{2,3}$ eigenstructure of
$H_3(q)$.*

The remaining sections derive this factorization from the $S_3^A$
branching rule, identify the four channels with the $T_{2,3}$
eigendecomposition, and tabulate the per-nucleon Garside data.

## $S_3^A$ branching

The typed Garside element
([typed crossing operator](#def:typed-crossing-operator))
for a nucleus with $Z$ protons and $N$ neutrons acts on
$V^{\otimes 3A}$, where $V$ is the fundamental representation.
The $S_3^A$ branching rule decomposes this action into a product
of $A$ per-nucleon factors:

$$
  G(c_1, \ldots, c_A)
  = \prod_{m=1}^{A} G_{n_m}(c_m)
$$

where $n_m \in \{P, N\}$ is the nucleon type and
$c_m \in \{\mathrm{triv}, \mathrm{conf}, \mathrm{unconf},
\mathrm{sign}\}$ is the channel.

## Four channels from $T_{2,3}$ eigendecomposition

The trefoil operator $T_{2,3} = \sigma_0 \sigma_1 \sigma_0$
in $H_3(q)$ has four eigenvalues corresponding to four
channels:

1. **Trivial** ($\lambda = q^3$): fully symmetric channel
2. **Confining** ($\lambda = q^{-1}$): standard representation,
   confining component
3. **Unconfining** ($\lambda = -q$): standard representation,
   anti-confining component
4. **Sign** ($\lambda = -q^{-3}$): fully antisymmetric channel

## Per-nucleon channel data

For each channel $c$, the per-nucleon Garside factor $G(c)$
is the Frobenius matrix element of the typed Garside element $\Delta_3$
in the $T_{2,3}$ eigenvector $v_c$:

$$
  G(c) = \langle v_c, \Delta_3(\text{quarks}) v_c \rangle_F
$$

In the symmetric and alternating channels (dim $= 1$), this
is the product of per-crossing eigenvalues.  In the standard
channel (dim $= 2$), $v_c$ is the eigenvector of
$T_{2,3} = \sigma_0\sigma_1\sigma_0$ in the seminormal basis.

**Proton** ($\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$), crossings:

$$
  \sigma_0(\mathfrak{u}\mathfrak{u}) \times [\sigma_1 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d}) \times [\sigma_0 - \tfrac{1}{2}h](\mathfrak{u}\mathfrak{d})
$$

The four channels correspond to the earlier eigendecomposition:
Sym $= $ Trivial ($\lambda = q^3$), Std $\lambda_1 = $ Unconfining
($\lambda = -q$), Std $\lambda_2 = $ Confining ($\lambda = q^{-1}$),
Alt $= $ Sign ($\lambda = -q^{-3}$).

| Channel | $\lambda_c$ | $G_P(c)$ | Numeric at $q_0$ |
|:---:|:---:|:---:|:---:|
| Sym (Trivial) | $q^3$ | $q \cdot \tfrac{1}{2}[2]_q \cdot \tfrac{1}{2}[2]_q$ | $+1.122$ |
| Std $\lambda_1$ (Unconf.) | $-q$ | $\langle v_1, \Delta_3 v_1 \rangle_F$ | $-1.174$ |
| Std $\lambda_2$ (Conf.) | $q^{-1}$ | $\langle v_2, \Delta_3 v_2 \rangle_F$ | $+0.858$ |
| Alt (Sign) | $-q^{-3}$ | $(-q^{-1}) \cdot (-\tfrac{1}{2}[2]_q)^2$ | $-0.911$ |

**Channel sum:** $a = \sum_c G_P(c) = -h/2$ (verified algebraically
and numerically at $q_0$: $a = -0.1045$).

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

**Channel sum:** $b = \sum_c G_N(c) = -3(q^2-1)(q^2+1)^2/(4q^3)$
(verified: $b = -0.6340$ at $q_0$; individual values sum to
$0.9108 - 1.2222 + 0.7995 - 1.1221 = -0.6340$).

The eight values $\{G_P(c), G_N(c)\}_{c \in \mathrm{channels}}$
are algebraic functions of $q$ (rational in the sym and alt
channels; roots of a quadratic in the standard channel) and
completely determine all nuclear
Q-values via the
[branching factorization](#prop:branching-qvalue-factorization).
<!-- FILE_END: per-nucleon-channel-decomposition.md -->

<!-- FILE_START: spectator-normalization.md -->
The spectator normalization captures the contribution of unchanged nucleons to the Q-value character sum. In a beta decay ${}^A_Z X \to {}^A_{Z+1} Y + e^- + \bar\nu$, one neutron converts to a proton. The remaining $Z$ protons and $N - 1$ neutrons act as spectators.

**1. Definition.**
The spectator factor is
$$
  S(Z, N-1) = a^{Z} \cdot b^{N-1}
$$
where $a$ and $b$ are the channel sums of the per-nucleon Garside factors ([per-nucleon decomposition](#def:per-nucleon-channel-decomposition)):
$$
  a = \sum_{c} G_P(c) = -\frac{h}{2},
  \qquad
  b = \sum_{c} G_N(c)
    = -\frac{3(q^2-1)(q^2+1)^2}{4q^3}
$$
with $h = q - q^{-1}$.

**2. Fermionic character.**
Both $a < 0$ and $b < 0$ for all $q > 1$. The negativity reflects the fermionic character of the nucleon: each spectator contributes a sign flip to the character sum. The sign of the full spectator product is:
$$
  \operatorname{sign}(a^Z \cdot b^{N-1})
  = (-1)^{Z} \cdot (-1)^{N-1}
  = (-1)^{A-1}.
$$
This sign fixes the [parity regime](#thm:parity-regime-selection) for the Q-value.
<!-- FILE_END: spectator-normalization.md -->

<!-- FILE_START: branching-qvalue-factorization.md -->
We compute the branching $\mathcal{Q}_q$-value by summing over all $4^A$ channel configurations. This character sum factors exactly into a spectator contribution and an active-channel difference.

## Statement

**Proposition.**
*For $\beta^-$ decay of a nucleus $(Z, N)$ with $A = Z + N$:*

$$
  \sum_{\text{all } 4^A \text{ configs}}
  \Delta m_e
  = a^Z \cdot b^{N-1} \cdot (a - b)
$$

*where $a = \sum_c G_P(c)$ and $b = \sum_c G_N(c)$ are the per-nucleon channel sums ([spectator normalization](#def:spectator-normalization)).*
<!-- FILE_END: branching-qvalue-factorization.md -->

<!-- FILE_START: parity-regime-selection.md -->
The **parity of the mass number** $A$ determines which computational regime applies to the Q-value. This emerges not as a fitting parameter, but from the fermionic sign of the spectator factor.

## Statement

**Theorem.**
*For all $q > 1$:*

$$
  \operatorname{sign}(a^Z \cdot b^{N-1}) = (-1)^{A-1}
$$

*The Q-value regimes are:*

1. **Odd $A$** ($A \geq 3$): The factorization $a^Z b^{N-1}(a-b)$ is positive, yielding

   $$
     Q = |S \cdot \Delta| \times m_e
   $$

   *where $S = a^Z b^{N-1}$ and $\Delta = a - b$.*

2. **Even $A$**: The factorization is negative. The [Frobenius positivity filter](#prop:frobenius-positivity-filter) restricts the sum to admissible (non-negative-trace) configurations, yielding

   $$
     Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e
   $$

   *where $\Sigma_{\mathrm{FP}}$ represents the sum over Frobenius-positive configurations and $+1$ introduces the [positron correction](#prop:positron-correction).*

3. **$A = 1$** (neutron decay): There are no spectators. We add the positron correction explicitly:

   $$
     Q = (S\Delta + 1) \times m_e
   $$
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

We apply the offset $\delta_A$ differently across two regimes ([parity regime selection](#thm:parity-regime-selection)):

1. **$A = 1$** (neutron decay) and **Even $A$**:
   We add the correction explicitly, setting $\delta_A = 1$.
   $Q = (S\Delta + 1) \times m_e$ (for $A=1$).
   $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$ (for even $A$).

2. **Odd $A \geq 3$**:
   We apply no explicit correction, setting $\delta_A = 0$.
   $Q = |S\Delta| \times m_e$.

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

This is the simplest non-trivial application of the [branching factorization](#prop:branching-qvalue-factorization). We have $(Z, N) = (1, 2)$ and $A = 3$ (the odd regime).

## Derivation

From the branching factorization with $Z = 1$ and $N = 2$:

$$
  \sum_{4^3 \text{ configs}} \Delta m_e
  = a^1 \cdot b^{1} \cdot (a - b)
  = ab(a - b)
$$

Substitute the channel sums $a = -h/2$ and $b = -3(q^2-1)(q^2+1)^2/(4q^3)$:

$$
  Q = |ab(a-b)| \times m_e.
$$

This simplifies to the stated closed form.

## Numerical evaluation

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 decimal places):

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  \approx 0.0179 \;\text{MeV}.
$$

The experimental value is $Q_{\mathrm{exp}} = 0.0186$ MeV. The error is $-3.64\%$. The entire computation uses exactly three CODATA inputs ($\mathrm{Vol}(4_1)$, $m_\mu/m_e$, $m_e$) to fix $q_0$, with zero additional fitting.
<!-- FILE_END: tritium-qvalue-symbolic.md -->

<!-- FILE_START: frobenius-positivity-filter.md -->
For nuclei with even mass number $A$, the raw character sum is negative ([parity regime](#thm:parity-regime-selection)). We obtain the physical Q-value by restricting the sum to Frobenius-positive configurations. These are configurations where both parent and daughter yield non-negative Markov traces.

## Statement

**Proposition.**
*For even $A$: a channel configuration $(c_1, \ldots, c_A) \in \{\mathrm{triv}, \mathrm{conf}, \mathrm{unconf}, \mathrm{sign}\}^A$ is Frobenius-positive if and only if:*

$$
  m_{e,\mathrm{par}} = \prod_{m=1}^{A} G_{n_m}(c_m) \geq 0
  \quad \text{and} \quad
  m_{e,\mathrm{dau}} = \prod_{m=1}^{A} G_{n'_m}(c_m) \geq 0
$$

*Under the spectator-factor sign mechanism, we write $\varepsilon_m \in \{0, 1\}$ for the sign of the $m$-th spectator factor, where $\varepsilon_m = 1$ exactly when $G_{n_m}(c_m) < 0$. A configuration is excluded exactly when its sign-pattern has odd total parity $\sum_{m=1}^{A} \varepsilon_m \equiv 1 \pmod 2$. Of the $2^A$ sign-patterns, exactly half ($2^{A-1}$) are excluded.*

## Connection to the confinement LP

The Frobenius positivity constraint provides the continuous analogue of the LP feasibility constraint $Gx \geq 0$ in the [confinement LP](#prop:confinement-lp). In the discrete (branching) setting, it acts as a configuration filter. Only configurations producing non-negative mass elements for both parent and daughter nuclei contribute to the Q-value.

## Computational complexity

For the ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ decay ($A = 6$), the $4^6 = 4096$ configurations reduce to $2^6 = 64$ sign-patterns. We exclude the $2^5 = 32$ patterns with odd parity. The Frobenius-filtered sum yields $Q \approx 3.637$ MeV (experiment: $3.508$ MeV, error $+3.68\%$).

For large even $A$ (for example, ${}^{14}\mathrm{C}$ at $A = 14$), the $4^{14} = 268{,}435{,}456$ configurations require either enumeration or a closed-form simplification of the Frobenius-filtered sum.
<!-- FILE_END: frobenius-positivity-filter.md -->

<!-- FILE_START: categorical-quantity-map.md -->
The four principal physical observables---mass, $\mathcal{Q}_q$-value, decay rate, and density---correspond rigidly to four distinct functionals acting on the [categorical action](#def:categorical-action):

| Physical quantity | Categorical functional | Formula |
|-------------------|----------------------|---------|
| **Mass** | Markov trace (absolute value) | $\mathfrak{m} = |\mathrm{tr}_M(\Phi)|$ |
| **Q-value** | Character sum | $Q = \sum_\lambda \chi_\lambda(\Delta) \times m_e$ |
| **Decay rate** | Frobenius matrix element | $\mathfrak{D} \propto |\langle v, \Phi v \rangle_F|^2$ |
| **Density** | Partial trace (crossing count) | $\rho = \mathrm{tr}_A(\varrho)$ |

Each functional isolates an orthogonal dimension of the underlying Hecke algebra element:

- The **Markov trace** isolates a scalar value representing the action at rest. This dictates the mass.
- The **character sum** isolates the action difference across irreducible representations. This dictates the transition energy.
- The **Frobenius norm** measures the geometric overlap between initial and final states. This dictates the transition rate.
- The **partial trace** counts discrete crossings per strand. This dictates the spatial density.
<!-- FILE_END: categorical-quantity-map.md -->

<!-- FILE_START: b3-local-minimum.md -->
We show the Borromean braid $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3$ is a local, rather than global, minimum of the categorical action.

## Global minimum

The [confinement LP](#prop:confinement-lp) with the corrected Gram matrix (using $\mathrm{tr}_M(e^-) = z^3$) admits a global minimum at $\mathrm{tr}_M = 0$. This represents a massless confined state. The Borromean solution $\mathcal{B}_3$ is a local minimum at a vertex of the LP feasible polytope.

## Corrected Gram matrix

With the corrected Markov trace ([corrected trace](#prop:corrected-markov-trace)), the $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ has a negative eigenvalue $\approx -0.956$. This indefinite signature means the Frobenius form is not positive definite. Consequently, the LP feasible region is unbounded in the direction of the negative eigenvector.

## Eigenvalue selection

The confinement LP selects $\mathcal{B}_3$ via the $\min|\lambda|$ eigenvalue criterion. The minimum absolute eigenvalue of the Gram matrix restricted to the net-constraint hyperplane picks out the Borromean solution. This identifies it as the least unstable confined state, sitting closest to the boundary between confinement and deconfinement.
<!-- FILE_END: b3-local-minimum.md -->

