*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Garside matrix element for a nucleus of mass number $A$
factors as a product of **per-nucleon contributions**, each
decomposed into four channels by the $T_{2,3}$ eigenstructure
of $H_3(q)$.

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
is the expectation value of the typed Garside element $\Delta_3$
in the $T_{2,3}$ eigenvector $v_c$:

$$
  G(c) = \langle v_c | \Delta_3(\text{quarks}) | v_c \rangle
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
| Std $\lambda_1$ (Unconf.) | $-q$ | $\langle v_1 \mid \Delta_3 \mid v_1 \rangle$ | $-1.174$ |
| Std $\lambda_2$ (Conf.) | $q^{-1}$ | $\langle v_2 \mid \Delta_3 \mid v_2 \rangle$ | $+0.858$ |
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
| Std $\lambda_1$ (Unconf.) | $-q$ | $\langle v_1 \mid \Delta_3 \mid v_1 \rangle$ | $-1.2222$ |
| Std $\lambda_2$ (Conf.) | $q^{-1}$ | $\langle v_2 \mid \Delta_3 \mid v_2 \rangle$ | $+0.7995$ |
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
