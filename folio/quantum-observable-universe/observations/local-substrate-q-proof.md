
The algebraic topological mass formula ([algebraic topological mass](#prop:topological-mass-formula-algebraic)) gives the mass ratio in $\mathbb{Q}(q)$ as $m_\mu / m_e = \Phi_1(4_1) / \hbar_q^{2}$. Here $\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$ is the $\tau_{\mathrm{arch}}$-image of the algebraic quantum volume ([Algebraic quantum volume $\mathrm{Vol}_q(K)$](#def:algebraic-quantum-volume)) and $\hbar_q = 1 - q^{-1}$. The calibration CAL-2 ([three-calibration discipline](#def:three-calibration-discipline)) fixes $q_0$ by the equation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^{2}$, with $\mathrm{Vol}(4_1)$ the hyperbolic volume. This is a definition of $q_0$, not a consequence of a conjecture. That the equation is the archimedean form of the mass identity, with $\Phi_1(4_1) = \mathrm{Vol}(4_1)$ via the volume conjecture \cite{kashaev1997, murakami-murakami2001}, is the separate [topological mass formula](#conj:topological-mass-formula), and nothing below uses it. Substituting the $\tau_{\mathrm{arch}}$-specialised numerical value yields:

$$
  (1 - q^{-1})^{2}
  = \frac{{{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}}{{{ qou.computations.q-pinning-50-digit.calibration_inputs.m_mu_over_e_str | precision: 7 }}}
  \approx 0.009817,
  \qquad
  1 - q^{-1} \approx 0.09908,
  \qquad
  q \approx 1.10998.
$$

The SnapPy witness ([knot volumes verification](#prf:knot-volumes-verification)) independently verifies the numerical values. It computes $q \approx 1.10998$ from $\mathrm{Vol}(4_1) \approx 2.02988321281931$ and $m_\mu/m_e \approx {{ qou.computations.q-pinning-50-digit.calibration_inputs.m_mu_over_e_str | precision: 6 }}$ (CODATA 2022). The function $f(q) = (1 - q^{-1})^{2}$ is strictly increasing for $q > 1$ and maps $(1,\infty)$ onto $(0,1)$. Thus the root is unique. The $\pm0.001$ uncertainty propagates from the CODATA relative uncertainty ($2.2 \times 10^{-8}$ on $m_\mu / m_e$) and the $\tau$-image SnapPy error bound ($10^{-14}$ on $\mathrm{Vol}(4_1)$). Finite decimal truncation of $q$ provides the dominant contribution. This value aligns with the hadronic mass predictions of [terminal resolution](#prop:terminal-resolution) and the $q$-deformed Hall conductance corrections of [photonic Hall effect](#rem:photonic-hall).

