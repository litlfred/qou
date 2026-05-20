**Question.** Does the universal-residue prefactor
$\alpha = m_e \cdot 8 G$
([gravity spectral prefactor](#prop:gravity-spectral-prefactor))
fix $G$ as a numerical constant, or does $G$ inherit a closed
$q$-rational form from the substrate parameter $q$?  Both faces
admit a sharp answer.

**Closed $q$-rational form (information face).**
The $q$-Yang--Mills--Levi variation
([gravitational constant](#def:gravitational-constant)) gives
$G$ as the ratio of $c_q^3 \hbar_q$ to the cumulative jet-tower
entropy $S_{\mathrm{cell}}(q) = (q-1)^2/q^3$.  Substituting
$c_q = 1/(q-1)$ and $\hbar_q = (q-1)/q$ and reducing:

$$
  G_q
  \;=\;
  \frac{c_q^3 \cdot \hbar_q}{S_{\mathrm{cell}}(q)}
  \;=\;
  \frac{1/(q-1)^3 \cdot (q-1)/q}{(q-1)^2/q^3}
  \;=\;
  \frac{q^2}{(q-1)^4}.
$$

This is a strictly $q$-rational expression in $\mathbb{Q}(q)$ — no
transcendental input, no fitted coefficient.  It is the $q$-natural
form of $G$, before any unit conversion to Planck or SI.

**Planck-unit identity.**
Newton's constant in Planck units is the dimensionless ratio
$G_{\mathrm{Planck}} = G_q \cdot (\hbar_q / c_q)^2$.  With
$\hbar_q / c_q = (q-1)^2/q$,

$$
  G_{\mathrm{Planck}}
  \;=\;
  \frac{q^2}{(q-1)^4}
  \cdot
  \left(\frac{(q-1)^2}{q}\right)^2
  \;=\;
  \frac{q^2}{(q-1)^4}
  \cdot
  \frac{(q-1)^4}{q^2}
  \;=\;
  1
$$

identically in $\mathbb{Q}(q)$, for every $q \neq 0, 1$.  The
algebraic identity is verified in Lean as
`gravitational_planck_eq_one` (file
[gravitational-constant.lean](#def:gravitational-constant)).

**Consequence for the spectral prefactor.**
Substituting $G_{\mathrm{Planck}} = 1$ into
$\alpha = m_e \cdot 8 G$
([gravity spectral prefactor](#prop:gravity-spectral-prefactor))
gives, in Planck units,

$$
  \alpha_{\mathrm{Planck}}(q)
  \;=\;
  8\, m_e(q),
$$

so the only $q$-dependence of the universal-residue prefactor in
Planck units is carried by the electron mass $m_e(q)$ and by the
Plancherel-weighted residue $\sum_{k \geq 4}\Phi_k$.  $G$ itself
contributes no further $q$-dependence — its $q$-rational content
is exactly cancelled by the Planck normalisation.

**Reconciling the two faces.**
The two derivations of $G$ in this folio are dual, not competing.

| Face | Source | Closed form | Planck value |
|------|--------|-------------|--------------|
| Categorical (spectral) | Plancherel residue $\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}$ at depth $\geq 4$ | $\alpha/(8 m_e)$ | $1$ |
| Information (variational) | $q$-YM--Levi action, jet-tower entropy | $q^2/(q-1)^4$ | $1$ |

The categorical face fixes $G$ as the universal-residue prefactor
of the deep-tower stratum; the information face fixes $G$ as the
information-geometric coupling of the substrate.  Both reduce to
$G_{\mathrm{Planck}} = 1$ identically in $q$, so the two faces are
algebraically consistent — no fitting, no calibration condition at
$q_0$ beyond the closed-form identities.

**Empirical anchor.**
Newton's constant in SI units,
$G_{\mathrm{Newton}} \approx 6.674 \times 10^{-11}\,
\mathrm{m^3\, kg^{-1}\, s^{-2}}$, sets the Planck length, mass, and
time triple via
$\ell_P = \sqrt{\hbar G / c^3}$,
$m_P = \sqrt{\hbar c / G}$,
$t_P = \sqrt{\hbar G / c^5}$.
In QOU units these are absorbed into the conversion
$(\hbar_q / c_q)^2 = (q-1)^4/q^2$, and the SI value of $G$ becomes
the human-scale rescaling that maps $\ell_P, m_P, t_P$ onto metres,
kilograms, and seconds.  The empirical $G_{\mathrm{Newton}}$
therefore enters as a unit-system datum, not as a fit parameter on
$q$.  The substrate value $q_0 = 1.109978595554181\ldots$ (50 dps) is fixed by the
lepton-mass cross-check
([substrate consistency window](#prop:substrate-consistency-window)),
not by gravity.

**Summary (one line).**
$G_q = q^2/(q-1)^4$ in $q$-natural units; in Planck units
$G_{\mathrm{Planck}} = 1$ identically for all $q \neq 0, 1$;
the universal-residue prefactor reduces to
$\alpha_{\mathrm{Planck}}(q) = 8 m_e(q)$ with no residual
$q$-dependence in $G$ itself.
