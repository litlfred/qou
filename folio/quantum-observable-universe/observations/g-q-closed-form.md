**Question.** Does the universal-residue prefactor $\alpha = m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor)) fix $G$ as a numerical constant, or does $G$ inherit a closed $q$-rational form from the substrate parameter $q$? Both faces admit a sharp answer.

**Closed $q$-rational form (information face).**

The $q$-Yang–Mills–Levi variation ([gravitational constant](#def:gravitational-constant)) yields $G$ as the ratio of $c_q^3 \hbar_q$ to the cumulative jet-tower entropy $S_{\mathrm{cell}}(q) = (q-1)^2/q^3$. Substituting $c_q = 1/(q-1)$ and $\hbar_q = (q-1)/q$ gives:

$$
  G_q
  \;=\;
  \frac{c_q^3 \cdot \hbar_q}{S_{\mathrm{cell}}(q)}
  \;=\;
  \frac{1/(q-1)^3 \cdot (q-1)/q}{(q-1)^2/q^3}
  \;=\;
  \frac{q^2}{(q-1)^4}.
$$

This strictly $q$-rational expression in $\mathbb{Q}(q)$ requires no transcendental input and zero fitted coefficients. It is the $q$-natural form of $G$, prior to any unit conversion (Planck or SI).

**Planck-unit identity.**

Newton's constant in Planck units is the dimensionless ratio $G_{\mathrm{Planck}} = G_q \cdot (\hbar_q / c_q)^2$. With $\hbar_q / c_q = (q-1)^2/q$, compute:

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

This holds identically in $\mathbb{Q}(q)$ for every $q \neq 0, 1$.

**Consequence for the spectral prefactor.**

Substituting $G_{\mathrm{Planck}} = 1$ into $\alpha = m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor)) yields the Planck-unit relation:

$$
  \alpha_{\mathrm{Planck}}(q)
  \;=\;
  8\, m_e(q).
$$

The electron mass $m_e(q)$ and the Plancherel-weighted residue $\sum_{k \geq 4}\Phi_k$ carry the entire $q$-dependence of the universal-residue prefactor in Planck units. $G$ itself contributes no further $q$-dependence; the Planck normalisation exactly cancels its $q$-rational content.

**Reconciling the two faces.**

The two derivations of $G$ in this folio are dual, not competing.

| Face | Source | Closed form | Planck value |
| --- | --- | --- | --- |
| Categorical (spectral) | Plancherel residue $\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}$ at depth $\geq 4$ | $\alpha/(8 m_e)$ | $1$ |
| Information (variational) | $q$-YM–Levi action, jet-tower entropy | $q^2/(q-1)^4$ | $1$ |

The categorical face sets $G$ as the universal-residue prefactor of the deep-tower stratum. The information face sets $G$ as the information-geometric coupling of the substrate. Both derivations reduce to $G_{\mathrm{Planck}} = 1$ identically in $q$. The two faces are algebraically consistent without any calibration condition at $q_0$.

**Empirical anchor.**

Newton's constant in SI units ($G_{\mathrm{Newton}} \approx 6.674 \times 10^{-11}\, \mathrm{m^3\, kg^{-1}\, s^{-2}}$) establishes the Planck length, mass, and time triple via $\ell_P = \sqrt{\hbar G / c^3}$, $m_P = \sqrt{\hbar c / G}$, and $t_P = \sqrt{\hbar G / c^5}$. In QOU units, the conversion $(\hbar_q / c_q)^2 = (q-1)^4/q^2$ absorbs these quantities. The SI value of $G$ functions strictly as the human-scale rescaling that maps $\ell_P, m_P, t_P$ onto metres, kilograms, and seconds. The empirical $G_{\mathrm{Newton}}$ therefore enters as a unit-system datum, not as a fit parameter on $q$. The lepton-mass cross-check ([substrate consistency window](#prop:substrate-consistency-window)) fixes the substrate value $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps), independent of gravity.

**Summary.**

In $q$-natural units, $G_q = q^2/(q-1)^4$. In Planck units, $G_{\mathrm{Planck}} = 1$ identically for all $q \neq 0, 1$. The universal-residue prefactor reduces to $\alpha_{\mathrm{Planck}}(q) = 8 m_e(q)$ with no residual $q$-dependence in $G$.
