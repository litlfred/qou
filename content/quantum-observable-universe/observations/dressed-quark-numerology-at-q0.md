**Remark (dressed-quark numerology at $q_0$).**

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps), we combine [`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md) with the baryon-content sum rule $\bar\mu \approx M_N / 3$. This fixes the individual dressed-quark masses to:

$$
  \mu_{\mathfrak{u}} \;\approx\; 311.10\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} \;\approx\; 312.39\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \;\approx\; 1.286\,\text{MeV}.
$$

These values were previously absorbed into the deprecated `lem:nucleon-mass-splitting` as a four-input fit ($\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}, m_p, m_n$ taken from CODATA). Under the substrate-pure derivation, they reduce to a two-input form: $M_N$ (anchored by CODATA) and $q_0$ (the substrate parameter). The CODATA value $m_n - m_p \approx 1.293\,\text{MeV}$ is no longer an input. It is a prediction at $-0.53\%$ residual.

## Origin of $\bar\mu \approx M_N / 3$ and the Skein cross-term shift

The proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) braids each carry three quark vortices. The sum of nucleon masses contains three copies of the average quark dressing:

$$
  m_p + m_n
  \;=\;
  3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
  \;+\;
  \text{(Skein cross-terms)}.
$$

Setting the cross-terms to zero yields a naive closed-form upper estimate:

$$
  \bar\mu^{\mathrm{naive}}
  \;=\;
  \tfrac{1}{6}(m_p + m_n)
  \;=\;
  \tfrac{M_N}{3}
  \;\approx\;
  312.97\,\text{MeV}.
$$

The Borromean Skein cross-terms shift the per-quark contribution down by a uniform amount $\delta \approx 1.23\,\text{MeV}$ per quark ($6\delta \approx 7.4\,\text{MeV}$ total across the proton + neutron sum). This gives:

$$
  \bar\mu^{\mathrm{Skein-corrected}}
  \;=\;
  \bar\mu^{\mathrm{naive}} - \delta
  \;\approx\;
  311.75\,\text{MeV}.
$$

This is consistent with $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2 = (311.10 + 312.39)/2 = 311.745\,\text{MeV}$ from the per-quark values. The substrate split $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ (1.286 MeV) remains unaffected by the Skein cross-term adjustment, which acts uniformly on both flavors.

## Distance from the substrate bound

[`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md) gives the upper bound:

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\;
  M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q
  \;\approx\;
  3.88\,\text{MeV}.
$$

The realised value $1.286\,\text{MeV}$ sits at about $33\%$ of the bound. Per the slack-ratio identity in [`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md), the closed form for this ratio is:

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q}
  \;=\;
  \frac{1}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left((\Delta m / M_N)^2\right).
$$

The dominant contribution is the explicit $1/3$ in the substrate formula of [`prop:flavor-split-substrate`](flavor-split-substrate.md). The Skein-side factor $(q^{1/2} + q^{-1/2})/(q + q^{-1}) \approx 0.997$ at $q_0$ only adjusts the slack slightly. Tightening the bound to capture the realised value remains open.

## Heavier flavors

The dressed-quark masses of $\mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}$ are not pinned by the substrate flavor-split derivation. That derivation is specific to the nucleon doublet topology ($\mathfrak{u}\mathfrak{d}$). An extension to higher-flavor braids requires either:

- The strangelet topology ([`sec:strangelet-intro`](strangelet-intro.md)) for $\mathfrak{s}$.
- A flavor-dependent confinement-category extension for $\mathfrak{c}, \mathfrak{b}, \mathfrak{t}$ via the heavy-quark effective theory analog (open).

Until these extensions are formalized, the entries $\mu_{\mathfrak{s}}, \mu_{\mathfrak{c}}, \mu_{\mathfrak{b}}, \mu_{\mathfrak{t}}$ of the [`def:flavor-dressing-functor`](../braids-and-knots/flavor-dressing-functor.md) remain unconstrained.
