**Remark (dressed-quark numerology at $q_0$).**

At the substrate parameter $q_0 \approx 1.10998$, combining
[`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
with the baryon-content sum rule $\bar\mu \approx M_N / 3$ pins the
individual dressed-quark masses to

$$
  \mu_{\mathfrak{u}} \;\approx\; 311.10\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} \;\approx\; 312.39\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \;\approx\; 1.288\,\text{MeV}.
$$

These are the values previously absorbed into the deprecated
`lem:nucleon-mass-splitting` as a four-input fit
($\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}, m_p, m_n$ each taken from
CODATA).  Under the substrate-pure derivation they reduce to a
**two-input** form: $M_N$ (anchored by CODATA) and $q_0$ (the
substrate parameter).  The CODATA value $m_n - m_p \approx 1.293\,
\text{MeV}$ is **no longer an input** — it is a prediction at
$-0.4\%$ residual.

## Why $\bar\mu \approx M_N / 3$

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

The Skein cross-terms cancel between the proton and neutron at
leading order (the Borromean braid topology has the same number
of $u u$ and $d d$ pairs across the doublet), so

$$
  M_N
  \;=\;
  \tfrac{1}{2}(m_p + m_n)
  \;\approx\;
  \tfrac{3}{2}\,(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
  \;=\;
  3 \,\bar\mu.
$$

Solving gives $\bar\mu \approx M_N / 3 \approx 312.7\,\text{MeV}$.

## Distance from the substrate bound

[`thm:flavor-mass-splitting-bound`](flavor-mass-splitting-bound.md)
gives the upper bound

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\;
  M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q
  \;\approx\;
  3.88\,\text{MeV},
$$

so the realised value $1.288\,\text{MeV}$ sits at about $33\%$ of
the bound.  The slack comes from the Skein-side adjustment factor
$(q^{1/2} + q^{-1/2})/(q + q^{-1}) \approx 0.997$ at $q_0$ combined
with the $O((\Delta m / M_N)^2)$ correction to the substrate
factor of [`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md).
Tightening the bound to capture the realised value remains open
(no canonical closed form is committed in this revision).

## Heavier flavors

The dressed-quark masses of $\mathfrak{s}, \mathfrak{c},
\mathfrak{b}, \mathfrak{t}$ are not pinned by the substrate
flavor-split derivation: that derivation is specific to the
nucleon doublet topology ($\mathfrak{u}\mathfrak{d}$).  An
extension to higher-flavor braids requires either:

- The strangelet topology
  ([`def:strangelet-intro`](../observations/strangelet-intro.md))
  for $\mathfrak{s}$.
- A flavor-dependent confinement-category extension for
  $\mathfrak{c}, \mathfrak{b}, \mathfrak{t}$ via the heavy-quark
  effective theory analog (open).

Until these extensions land, the entries
$\mu_{\mathfrak{s}}, \mu_{\mathfrak{c}}, \mu_{\mathfrak{b}}, \mu_{\mathfrak{t}}$
of the [`def:flavor-dressing-functor`](flavor-dressing-functor.md)
remain unconstrained.
