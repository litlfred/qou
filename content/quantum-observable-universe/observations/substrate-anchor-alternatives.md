The substrate parameter $q_0$ enters the framework through
the muon-anchor identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$,
which fixes $q_0$ from the CODATA muon-to-electron mass ratio
(relative uncertainty $22\,\mathrm{ppb}$).  The proton substrate
identity
([`prop:proton-mass-substrate-identity`](../braids-and-knots/proton-mass-substrate-identity.md))
opens a second, experimentally sharper route:

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

When the proton anchor is used, the muon-to-electron mass ratio
becomes a **prediction** of the framework rather than an input.
At the current formula precision ($0.24\,\mathrm{ppm}$), the
predicted $m_\mu/m_e$ agrees with CODATA to $0.21\,\mathrm{ppm}$
— within the formula's empirical residual but well outside
CODATA's own $22\,\mathrm{ppb}$ uncertainty.

The two anchors are not independent: both satisfy the same
overdetermined system (two equations, one unknown $q$).  Closing
the $0.24\,\mathrm{ppm}$ residual — via the Habiro-exact
evaluation at higher brane-tower order — would make the two
routes agree, and the choice of anchor would become a matter of
experimental convenience rather than theoretical necessity.

For future experimental tests, the framework predicts that any
CODATA-precision measurement of a mass ratio involving $q_0$
(such as $m_\tau/m_e$ via the torus-knot tower at $T(2,7)$)
should be derivable from the same $q_0$, providing an independent
cross-check of the substrate parameter.
