*The QOU framework takes exactly three external calibration inputs:*

| Calibration | Canonical observable | What it fixes | Numerical proxy (source) |
| ------------------------------- | -------------- | ------------- | ------ |
| CAL-1 | $m_e$ (leptonic mass scale) | the dimensional unit (scale) | $m_e$, CODATA (electron mass) |
| CAL-2 | $P_{\mathrm{skew}}^{\beta}$ (neutron $\beta$-sector bar-skew channel) | $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | $\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta}$; modulus pinned most precisely by $m_\mu/m_e$ (CODATA muon mass) |
| CAL-3 | $P_{\mathrm{avg}}^{\pi}$ (pion-sector bar-even channel) | the meson scale, independent of $m_e$ and $q_0$ ([meson scale independence](#prop:meson-scale-independence)) | $m_\pi$, PDG (charged-pion mass) |

**Definition (calibrated substrate parameter).** Let $r = \mathrm{Vol}(4_1)/(m_\mu/m_e)$, where $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ is the hyperbolic volume of the figure-eight knot. Since $0 < r < 1$, the equation

$$
  \bigl(1 - q^{-1}\bigr)^{2} = r
$$

has exactly one root $q > 1$, namely $q = 1/(1 - \sqrt{r})$. The **calibrated substrate parameter** $q_0$ is this root. In terms of the [quantum Planck constant](#def:quantum-planck-constant) $\hbar_q = 1 - q^{-1}$, the defining equation reads $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_{q_0}^{2}$.

This is the definition of $q_0$ in the ideal layer. In the Physical-Observations layer, $q_0$ may instead be pinned to the proton ratio $m_p/m_e$, which is measured more precisely. That is a substitution of the anchor, not a fourth calibration.

The definition makes no claim about how masses depend on the three inputs. The claim that every hadronic mass factors as $m_e^{a}\,m_\pi^{c}\,Q_X(q_0)$ with $Q_X \in \mathbb{Q}(q)$ is the conjecture [Exactly three calibration inputs](#conj:three-calibration-inputs). The claim that the three inputs are the three real moduli of the polarised Hodge structure on $H^1(\text{Bring}) = 2W$ is the conjecture [The three calibrations are the three cohomological data of H¹(Bring)](#conj:calibration-cohomology-alignment).
