We derive the gas constant $R_q = N_A(q) \cdot k_B$ from $q$ and the Borromean volume. A **categorical mole** consists of $N_A(q) = 12 / \mathfrak{m}_{C\text{-}12}(q)$ particles. The mass of Carbon-12 in QOU natural units is:

$$
  \mathfrak{m}_{C\text{-}12}(q)
  \;=\;
  \frac{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }{\hbar_q^2}.
$$

Here $\mathrm{Vol}(\mathcal{B}_3) = 7.32772\ldots$ is the Borromean volume, $\delta_{\mathfrak{n}}$ is the neutron--proton Skein mass difference, and $B_{12}(q)$ is the nuclear binding energy computed from the 66-crossing transfer matrix ([terminal resolution](#prop:terminal-resolution)).

The gas constant evaluates to:

$$
  R_q
  \;=\;
  \frac{12\,\hbar_q^3}{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }.
$$

At leading order, neglecting binding energy and neutron mass corrections, this simplifies to:

$$
  R_q
  \;\approx\;
  \frac{(q-1)^3}{q^3 \cdot \mathrm{Vol}(\mathcal{B}_3)}.
$$

The gas constant $R$ requires precisely two inputs: the algebraic parameter $q$ and the topological invariant $\mathrm{Vol}(\mathcal{B}_3)$. Because the mass predictions already match CODATA to sub-keV precision, $R$ is automatically correct. It is strictly downstream of the mass spectrum.

**Fundamental constants dictionary.**

| Constant | QOU expression | Depends on |
|----------|----------------|------------|
| $c$ | $1/(q-1)$ | $q$ only |
| $\hbar$ | $(q-1)/q$ | $q$ only |
| $G$ | $c_q^3 \hbar_q / S_{\mathrm{cell}}$ | $q$ only |
| $k_B$ | $1$ (natural units) | — |
| $R$ | $12\hbar_q^3 / (12\,\mathrm{Vol}(\mathcal{B}_3) + \cdots)$ | $q$, $\mathrm{Vol}(\mathcal{B}_3)$ |

The first four constants depend on $q$ alone. The gas constant $R$ additionally requires the Borromean topological invariant because it maps the substrate geometry to the baryonic mass scale.
