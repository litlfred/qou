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

For each channel $c$, the per-nucleon Garside factor is:

- **Proton** ($\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$):
  $G_P(c)$ — computed from the typed crossing operator
  with quark content $(u, u, d)$

- **Neutron** ($\mathfrak{n} = \mathfrak{u}\mathfrak{d}\mathfrak{d}$):
  $G_N(c)$ — computed from the typed crossing operator
  with quark content $(u, d, d)$

The eight values $\{G_P(c), G_N(c)\}_{c \in \mathrm{channels}}$
are rational functions of $q$ and completely determine all nuclear
Q-values via the
[branching factorization](#prop:branching-qvalue-factorization).
