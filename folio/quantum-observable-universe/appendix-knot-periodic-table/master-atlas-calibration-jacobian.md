**Archimedean specialisation.** Whereas the operator tables of the preceding section hold over an arbitrary commutative ground ring $R$ with invertible parameter $q \in R^\times$ and canonical Markov trace weight $z = q^3/(q^2+1)$, every empirical lookup table in the remainder of this annex crosses the Archimedean wall $R \mapsto \mathbb{R}$ and evaluates model invariants against CODATA-2022 ([codata2022](#cite:codata2022)), PDG-2024 ([pdg2024](#cite:pdg2024)), AME2020 ([ame2020](#cite:ame2020), [ame2020tables](#cite:ame2020tables)), and NUBASE2020 ([nubase2020](#cite:nubase2020)).

**Physical calibration vector.** Every post-wall observable $O(m_e, q_0, m_{\pi^\pm})$ is a smooth algebraic, Clausen, or Thomae--Jackson function of at most the three physical calibration measurements spanning the three real degrees of freedom of the Bring rank-two Hodge plane $2W$ ([calibration discipline](#rem:epistemic-status-of-calibrations)):

1. **Leptonic mass unit ($m_e$).** Electron rest-mass energy $m_e = 0.51099895069 \pm 0.00000000016\;\mathrm{MeV}$ ([codata2022](#cite:codata2022); relative uncertainty $0.3131\;\mathrm{ppb}$), setting the overall energy scale on $2W$.
2. **Weak decay-width modulus ($\mathfrak{D}_\beta \mapsto q_0$).** Dimensionless substrate deformation parameter $q_0 > 1$, anchored numerically on the most precise measured dimensionless baryon-to-lepton ratio (**Arm P**, $R_p = m_{\mathfrak{p}}/m_e = 1836.152673426 \pm 0.000000032$, [codata2022](#cite:codata2022)) via $2(\mathrm{Vol}(4_1)/\hbar_{q_0}^2)F_{\mathrm{Bor}}(q_0) - 12 = R_p$, yielding $q_0^{(p)} =$ :val[q_0_proton]{format=measured}. Evaluated instead on the muon-to-electron ratio (**Arm M**, $R_\mu = m_\mu/m_e = 206.7682827 \pm 0.0000046$, [codata2022](#cite:codata2022)) via $\mathrm{Vol}(4_1)/\hbar_{q_0}^2 = R_\mu$, the comparison pin is $q_0^{(\mu)} =$ :val[q_0_muon]{format=measured}, shifted by $q_0^{(\mu)} - q_0^{(p)} = +1.289 \times 10^{-8}$ ($+11.61\;\mathrm{ppb}$).
3. **Orthogonal meson scale ($m_{\pi^\pm}$).** Charged pion rest-mass energy $m_{\pi^\pm} = 139.57039 \pm 0.00018\;\mathrm{MeV}$ ([pdg2024](#cite:pdg2024); relative uncertainty $1.290\;\mathrm{ppm}$), fixing the zero-volume Hopf meson sector.

**Exact Fréchet--Jacobian propagation ($80$-digit precision).** For each observable $O(m_e, q_0(R_p), m_{\pi^\pm})$, partial derivatives with respect to $(m_e, q_0, m_{\pi^\pm})$ and the implicit anchor derivative $\mathrm{d}q_0^{(p)}/\mathrm{d}R_p = [\Phi_p'(q_0^{(p)})]^{-1}$ are evaluated in arbitrary-precision arithmetic at $95$ working decimal digits and serialized at $80$ decimal digits with truncation floor $\varepsilon_{\mathrm{trunc}} \le 10^{-60}$:

$$
  \sigma_{\mathrm{pred}}(O)
  \;=\;
  \sqrt{
    \left(\frac{\partial O}{\partial m_e}\right)^{\!2} \sigma_{m_e}^2
    \;+\;
    \left(\frac{\partial O}{\partial q_0}\frac{\mathrm{d}q_0^{(p)}}{\mathrm{d}R_p}\right)^{\!2} \sigma_{R_p}^2
    \;+\;
    \left(\frac{\partial O}{\partial m_{\pi^\pm}}\right)^{\!2} \sigma_{m_{\pi^\pm}}^2
    \;+\;
    \varepsilon_{\mathrm{trunc}}^2
  }.
$$

**Uniform six-column master-table contract.** Each of the five Master Reference Tables below (Tables A.1 through A.5) reports: (1) species or observable and confinement layer $\mathcal{L}_0\text{--}\mathcal{L}_4$; (2) canonical braid or motif normal form; (3) symbolic formula and explicit epistemic tier (*Calibration Pin*, *Proved*, *Derived*, *Conditional*, or *Open*); (4) predicted value $O_{\mathrm{pred}} \pm \sigma_{\mathrm{pred}}$ together with the cross-anchor shift diagnostic $[\Delta_{\mu\text{-pin}} = O(q_0^{(\mu)}) - O(q_0^{(p)})]$; (5) experimental value $O_{\mathrm{exp}} \pm \sigma_{\mathrm{exp}}$ with pinpoint bibliographic source; and (6) signed residual $\Delta = O_{\mathrm{pred}} - O_{\mathrm{exp}}$, fractional miss, experimental pull $\Delta/\sigma_{\mathrm{exp}}$, and combined calibration-aware pull $z_{\mathrm{comb}} = \Delta / \sqrt{\sigma_{\mathrm{pred}}^2 + \sigma_{\mathrm{exp}}^2}$. Calibration-pin rows satisfy $\Delta \equiv 0$ by construction and are excluded from accuracy counts (as summarized in the per-observable accuracy status remark immediately below).
