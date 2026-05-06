The total atomic mass of a neutral atom $(Z, N)$ with $n_{\mathrm{gen}}$
Hecke–NF generators decomposes as nucleon and electron rest masses plus
a Wedderburn-weighted binding term:

$$
  M(Z, N) \;=\; Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e
  \;+\; \alpha \sum_{i=1}^{n_{\mathrm{gen}}} \ln \bigl|\hat{V}_i^{\mathrm{full}}\bigr|,
$$

where $\hat{V}_i^{\mathrm{full}} = w_{\mathrm{sym}}\,\lambda_i^{\mathrm{sym}}
+ w_{\mathrm{std}}\,\hat{V}_i^{\mathrm{std}} + w_{\mathrm{alt}}\,\lambda_i^{\mathrm{alt}}$
are the Wedderburn–Markov weighted generator volumes at baryon level $n = 3$
($w_{\mathrm{sym}} = w_{\mathrm{alt}} = 1/[3]_q!$, $w_{\mathrm{std}} = [2]_q^2/[3]_q!$),
and the binding scale is $\alpha = m_e \cdot 8G$ with $G$ Catalan's constant.
See `QOU.Interactions.WedderburnMassFormula` for the Lean verification.
