The **neutron** is the baryon with $1 + 2$ crossing partition:
one up quark and two down quarks in the Borromean braid
$\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{n}
  \;=\;
  \mathcal{B}_3(\mathfrak{u},\, \mathfrak{d},\, \mathfrak{d})
$$

**Step 1: Borromean braid NF.**
Same as [proton](#def:categorical-proton) Step 1:
$\mathrm{net}(\mathcal{B}_3) = +1.000$, with intrinsic Hopf link
content (no separate $\mathcal{L}_H$ factor).

**Step 2: typed crossings.**
The two down quarks introduce stronger $-H_A$ shifts than
the proton's single down quark:

| Pair | Type | Crossing element |
|:---|:---|:---|
| $(0,1)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_0 - \tfrac{1}{2}H_A\cdot\mathbf{1}$ |
| $(0,2)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_0 - \tfrac{1}{2}H_A\cdot\mathbf{1}$ |
| $(1,2)$ | $\mathfrak{d}$-$\mathfrak{d}$ | $\sigma_1 - H_A\cdot\mathbf{1}$ |

The $\mathfrak{d}$-$\mathfrak{d}$ crossing on pair $(1,2)$
carries the full $-H_A$ shift (eigenvalue $-q^{-1}$), pulling
the net further below the proton's.

**Step 3: neutron NF.**
At $q_0 \approx 1.1100$:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\nu$ | $-0.2017$ |
| $\sigma_0$ | $H^0$ | $+0.0481$ |
| $\sigma_1$ | $H^1$ | $+1.0090$ |
| $\sigma_0\sigma_1$ | $L_+$ | $-0.0096$ |
| $\sigma_1\sigma_0$ | $L_-$ | $+0.0092$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $-0.0442$ |

$$
  \mathrm{net}(\mathfrak{n}) \;=\; +0.8108
$$

Compared to the proton ($\mathrm{net} = +0.9991$):
the extra down quark drives $\nu$ more negative
($-0.0997 \to -0.2017$) and flips $L_+$ from positive
($+0.0994$) to negative ($-0.0096$).  The $H^1$ term
stays near $+1$ in both, since both contain one up quark
on strand 1.

**Transition: proton $\to$ neutron.**
The NF difference (coefficient by coefficient) gives the
dimensionless beta decay transition
([energy scale](#rem:beta-decay-energy-scale)):

$$
  \Delta\mathrm{net}(\mathfrak{n} - \mathfrak{p})
  \;=\;
  0.8108 - 0.9991
  \;=\;
  -0.1883
$$

The energy scale $\mathbf{E}_0 = Q_\beta / |\Delta\mathrm{net}|
\approx 4.155$ MeV converts each coefficient difference to MeV
([formation chain](#rem:meson-to-proton-via-borromean)).

**Mass.**

$$
  m_{\mathfrak{n}}
  \;=\;
  2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$: $m_{\mathfrak{n}}(q_0) \approx 939.565$ MeV, derived from the substrate parameter ([local substrate](#prop:local-substrate-q)).  The
proton--neutron mass splitting is

$$
  m_{\mathfrak{n}} - m_{\mathfrak{p}}
  \;=\;
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  \;\approx\; 1.293 \text{ MeV}
$$

arising from the Skein resolution asymmetry between the
$\mathfrak{u}\text{-}\mathfrak{u}$ and $\mathfrak{d}\text{-}\mathfrak{d}$ crossing pairs within $\mathcal{B}_3$.

**Coulomb charge.**

$$
  Q(\mathfrak{n}) \;=\;
  1 \cdot (+\tfrac{2}{3}) + 2 \cdot (-\tfrac{1}{3}) \;=\; 0.
$$

The neutron is electrically neutral: its one positive-orientation
unknot ($\mathfrak{u}$) is exactly cancelled by two negative-orientation
unknots ($\mathfrak{d}$).  Inter-neutron Hopf crossings pick up the
coefficient $q^{-1}$ (negative crossings), producing an
attractive enhancement — the categorical expression of
electric neutrality.
