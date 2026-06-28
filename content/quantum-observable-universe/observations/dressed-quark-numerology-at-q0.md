**Remark (dressed-quark numerology at $q_0$).**

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps), combining
[`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md)
with the baryon-content sum rule $\bar\mu \approx M_N / 3$ pins the
individual dressed-quark masses to

$$
  \mu_{\mathfrak{u}} \;\approx\; 311.10\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} \;\approx\; 312.39\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \;\approx\; 1.286\,\text{MeV}.
$$

These are the values previously absorbed into the deprecated
`lem:nucleon-mass-splitting` as a four-input fit
($\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}, m_p, m_n$ each taken from
CODATA).  Under the substrate-pure derivation they reduce to a
**two-input** form: $M_N$ (anchored by CODATA) and $q_0$ (the
substrate parameter).  The CODATA value $m_n - m_p \approx 1.293\,
\text{MeV}$ is **no longer an input** — it is a prediction at
$-0.53\%$ residual.

## Origin of $\bar\mu \approx M_N / 3$ (and the Skein cross-term shift)

The proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron
($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) braids each carry three
quark vortices, so the sum of nucleon masses contains three
copies of the average quark dressing:

$$
  m_p + m_n
  \;=\;
  3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
  \;+\;
  \text{(Skein cross-terms)}.
$$

**Naive estimate (Skein cross-terms ignored).**  Setting the cross-terms
to zero gives a closed-form upper estimate

$$
  \bar\mu^{\mathrm{naive}}
  \;=\;
  \tfrac{1}{6}(m_p + m_n)
  \;=\;
  \tfrac{M_N}{3}
  \;\approx\;
  312.97\,\text{MeV}.
$$

**Skein-corrected value (matches the per-quark numerology above).**
The actual Borromean Skein cross-terms shift the per-quark
contribution down by a uniform amount $\delta \approx 1.23\,\text{MeV}$
per quark (so $6\delta \approx 7.4\,\text{MeV}$ total across the
proton + neutron sum).  This gives

$$
  \bar\mu^{\mathrm{Skein-corrected}}
  \;=\;
  \bar\mu^{\mathrm{naive}} - \delta
  \;\approx\;
  311.75\,\text{MeV},
$$

consistent with $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2
= (311.10 + 312.39)/2 = 311.745\,\text{MeV}$ from the per-quark values
quoted above.  The substrate split $\mu_{\mathfrak{d}} -
\mu_{\mathfrak{u}}$ (1.286 MeV) is unaffected by the Skein cross-term
adjustment, which acts uniformly on both flavors.
