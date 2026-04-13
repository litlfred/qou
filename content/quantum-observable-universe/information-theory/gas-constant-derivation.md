The gas constant $R_q = N_A(q) \cdot k_B$ is derived from $q$
and the Borromean volume.  A **categorical mole** is
$N_A(q) = 12 / \mathfrak{m}_{C\text{-}12}(q)$ particles,
where the Carbon-12 mass in QOU natural units is

$$
  \mathfrak{m}_{C\text{-}12}(q)
  \;=\;
  \frac{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }{\hbar_q^2},
$$

with $\mathrm{Vol}(\mathcal{B}_3) = 7.32772\ldots$ the
Borromean volume, $\delta_{\mathfrak{n}}$ the neutron--proton
Skein mass difference, and $B_{12}(q)$ the nuclear binding
energy from the 66-crossing transfer matrix
([terminal resolution](#prop:terminal-resolution)).

The gas constant is

$$
  R_q
  \;=\;
  \frac{12\,\hbar_q^3}{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }.
$$

At leading order (neglecting binding and neutron mass
corrections):

$$
  R_q
  \;\approx\;
  \frac{(q-1)^3}{q^3 \cdot \mathrm{Vol}(\mathcal{B}_3)}.
$$

$R$ depends on exactly two inputs: $q$ (algebraic) and
$\mathrm{Vol}(\mathcal{B}_3)$ (topological).  The mass
predictions already match CODATA to sub-keV precision, so
$R$ is automatically correct — it is downstream of the
mass spectrum.

**Fundamental constants dictionary.**

| Constant | QOU expression | Depends on |
|----------|----------------|------------|
| $c$ | $1/(q-1)$ | $q$ only |
| $\hbar$ | $(q-1)/q$ | $q$ only |
| $G$ | $c_q^3 \hbar_q / S_{\mathrm{cell}}$ | $q$ only |
| $k_B$ | $1$ (natural units) | — |
| $R$ | $12\hbar_q^3 / (12\,\mathrm{Vol}(\mathcal{B}_3) + \cdots)$ | $q$, $\mathrm{Vol}(\mathcal{B}_3)$ |

The first four constants depend on $q$ alone.  $R$
additionally requires the Borromean topological invariant
because it connects substrate geometry to the baryonic
mass scale.
