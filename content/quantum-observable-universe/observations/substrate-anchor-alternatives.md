The substrate parameter $q_0$ is not a fundamental constant: it
characterises the quantum-deformation strength of *this* universe's
brane substrate, and its numerical value is determined by
experimental mass ratios measured in our local cosmological context.
Multiple independent mass ratios provide experimental handles on the
same underlying $q_0$, each with different measurement precision.

$q_0$ is pinned from the **proton** ratio $m_p/m_e$ — the most
precisely measured ($0.06\,\mathrm{ppb}$) — via the proton substrate
identity below; $m_\mu/m_e$ is then a prediction. The muon-anchor
identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ is the most
transparent cross-check (CODATA muon ratio, $22\,\mathrm{ppb}$).  The
proton substrate identity
([`prop:proton-mass-substrate-identity`](../appendix-qvalues/proton-mass-substrate-identity.md))
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
At the current formula precision, the predicted $m_\mu/m_e$ agrees
with CODATA to $\approx 0.21\,\mathrm{ppm}$ — outside CODATA's
$22\,\mathrm{ppb}$ uncertainty by a factor $\approx 9.5$.

This factor is the decisive reason to prefer the proton anchor.
At present the framework cannot satisfy both ratios with a single
$q_0$: the two anchor formulas demand values of $q_0$ that differ by
$\approx 11.5\,\mathrm{ppb}$. This gap reflects the **current
formulas' theory imprecision** (each carries a residual relative to
the true substrate value); a fully-derived pair of formulas would
close it. Until then it is the floor below which fitting any single
observable is meaningless — see
[`docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`]. The
residual must surface in *whichever* ratio is left as a prediction.
Anchoring on the **less** precise ratio (muon, $22\,\mathrm{ppb}$)
forces the residual onto the **more** precise one (proton,
$0.06\,\mathrm{ppb}$), where it reads as a $\approx 4000\,\sigma$
discrepancy with experiment. Anchoring on the **more** precise
ratio (proton) instead pushes the residual onto the muon, where the
same absolute discrepancy is only $\approx 9.5\,\sigma$ — over two
orders of magnitude less significant. The general principle: pin
$q_0$ on the most precisely measured ratio, so the unavoidable
theory residual lands where it is least statistically significant.

**Remark (formal vs. numerical calibration).** A subtlety separates
the *formal* calibration input from the *numerical* anchor. The
principled CAL-2 input is the neutron $\beta$-decay observable
$\mathfrak{D}_\beta$ (equivalently $\mathfrak{Q}_\beta$): it fixes the substrate
scale through the weak sector that the substrate identity governs, and
is in that sense the *better*, more fundamental calibration. It is,
however, a poor *numerical* pin for $q_0$. The $\mathfrak{Q}_\beta$ value is known
only to $\approx 780\,\mathrm{ppb}$ — four orders of magnitude coarser
than $m_p/m_e$ — and, being a small neutron–proton mass difference, it
carries only modest sensitivity to $q$
($\mathrm{d}\ln \mathfrak{Q}_\beta/\mathrm{d}\ln q \approx 11$), so its propagated
uncertainty is $\sigma(q_0) \approx 68\,\mathrm{ppb}$, against
$\lesssim 1\,\mathrm{ppb}$ from a lepton or baryon mass ratio. The
substrate identity for $\mathfrak{Q}_\beta$ moreover carries a $\approx 0.2\%$
residual, which would displace $q_0$ by $\approx 185\,\mathrm{ppm}$ were
$\mathfrak{Q}_\beta$ forced to its measured value. The framework therefore retains
$\mathfrak{D}_\beta$ as the *conceptual* CAL-2 and a consistency
cross-check, while fixing the *numerical* value of $q_0$ from the most
experimentally accurate ratio available — and reports $\mathfrak{Q}_\beta$ as a
prediction tested against its measured value, not as the pin. The
principled calibration and the precise calibration are different
observables; the anchor is chosen for accuracy.

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
