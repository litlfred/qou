The substrate parameter $q_0$ is not a fundamental constant: it
characterises the quantum-deformation strength of *this* universe's
brane substrate, and its numerical value is determined by
experimental mass ratios measured in our local cosmological context.
Multiple independent mass ratios provide experimental handles on the
same underlying $q_0$, each with different measurement precision.

The muon-anchor identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
currently fixes $q_0$ from the CODATA muon-to-electron mass ratio
(relative uncertainty $22\,\mathrm{ppb}$).  The proton substrate
identity
([`prop:proton-mass-substrate-identity`](../braids-and-knots/proton-mass-substrate-identity.md))
provides an alternative route through a different observable:

$$
  \frac{m_p}{m_e}
  \;=\;
  \dim V_{(2,1)} \cdot
  \biggl(
    \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
    \cdot
    \frac{|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|}{y_{(3)}(q)}
    \;-\;
    |S_3|
  \biggr).
$$

Inverting this algebraically for $q$ (Newton iteration on the
rational function $F_{\mathrm{Bor}}(q)$) determines $q_0$ from
$m_p/m_e$ instead of $m_\mu/m_e$.  The CODATA proton-to-electron
mass ratio has relative uncertainty $0.06\,\mathrm{ppb}$ — a
factor of $371$ tighter than the muon ratio.

| Anchor | CODATA ratio | Relative uncertainty | $q_0$ precision |
|--------|-------------|---------------------|-----------------|
| $m_\mu/m_e$ (muon, current) | $206.7682830$ | $22\,\mathrm{ppb}$ | $22\,\mathrm{ppb}$ |
| $m_p/m_e$ (proton) | $1836.15267343$ | $0.06\,\mathrm{ppb}$ | $0.06\,\mathrm{ppb}$ |
| $m_n/m_e$ (neutron) | $1838.68366173$ | $0.48\,\mathrm{ppb}$ | $0.48\,\mathrm{ppb}$ |

Each row is an independent experimental determination of the same
$q_0$.  The framework does not privilege one over another on
theoretical grounds — the choice is a matter of which laboratory
measurement carries the smallest uncertainty.  For precision work,
the proton ratio is currently optimal; for conceptual clarity, the
muon-anchor identity (a single Bloch–Wigner period divided by the
substrate Planck constant) remains the most transparent.

When the proton anchor is used, the muon-to-electron mass ratio
becomes a **prediction** of the framework rather than an input.
At the current formula precision ($0.24\,\mathrm{ppm}$), the
predicted $m_\mu/m_e$ agrees with CODATA to $0.21\,\mathrm{ppm}$
— within the formula's empirical residual but well outside
CODATA's own $22\,\mathrm{ppb}$ uncertainty.

The anchors are not independent: all satisfy the same
overdetermined system (multiple equations, one unknown $q$).
Closing the $0.24\,\mathrm{ppm}$ residual — via the Habiro-exact
evaluation at higher brane-tower order — would make all routes
agree, and the choice of anchor would become purely a matter of
experimental convenience.

As more mass ratios are measured to higher precision (including
the $\tau$-lepton via the torus-knot tower at $T(2,7)$, and meson
ratios via the $H_3$ Frobenius bridge), each provides an
independent cross-check of the substrate parameter.  Consistency
across these independent determinations is itself a test of the
framework: if the QOU substrate is correct, all mass ratios must
yield the same $q_0$ to within their respective experimental
uncertainties.
