The electron is the trefoil $3_1$. This torus knot has $\mathrm{Vol}_q(\beta_{3_1}) = 0$ in $\mathbb{Z}[q^{\pm 1/2}]$ ([algebraic quantum volume](#def:algebraic-quantum-volume)). It sits at the base of the topological tower, providing the unit against which all other masses are measured. The Higgs field is the figure-eight knot $4_1$ ([cohomological embedding](#prop:cohomological-embedding)). Its algebraic quantum volume $\mathrm{Vol}_q(\beta_{4_1})$ τ-realises to the hyperbolic-volume constant $\mathrm{Vol}(4_1) \approx {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}$.

Applying the algebraic topological mass formula ([algebraic topological mass](#prop:topological-mass-formula-algebraic)) to the muon–electron ratio eliminates the overall mass scale. This gives $m_\mu / m_e = \Phi_1(4_1) / \hbar_q^{2}$ at the $\mathbb{Q}(q)$ level. Here, $\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$ is the $\tau_{\mathrm{arch}}$-image of the algebraic quantum volume ([algebraic quantum volume](#def:algebraic-quantum-volume)). Under $\tau_{\mathrm{arch}}$, the value $\Phi_1(4_1)$ specialises to the numerical hyperbolic volume $\mathrm{Vol}(4_1)$ via the volume conjecture \cite{kashaev1997, murakami-murakami2001}. This constitutes τ-side naming of the algebraic value rather than a derivation input. Substituting $\hbar_q = 1 - q^{-1}$ and the CODATA value $m_\mu / m_e \approx 206.7682827(46)$ yields

$$
  \hbar_q^{2}
  = \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  = \frac{{{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}}{{{ qou.computations.q-pinning-50-digit.calibration_inputs.m_mu_over_e_str | precision: 7 }}}
  \approx {{ qou.computations.q-pinning-50-digit.derived_50_digit.hbar_q_sq | precision: 4 }},
  \qquad
  \hbar_q \approx {{ qou.computations.q-pinning-50-digit.derived_50_digit.hbar_q | precision: 4 }},
$$

so $1/q = 1 - {{ qou.computations.q-pinning-50-digit.derived_50_digit.hbar_q | precision: 4 }} = {{ qou.computations.q-pinning-50-digit.derived_50_digit.q_inv | precision: 4 }}$ and $q \approx {{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 6 }}$.

The Skein relation acts as the mass-functional analogue of the Kauffman bracket recursion. At each crossing in the color-exchange diagram of a hadron, the three resolutions $L_+$, $L_-$, and $L_0$ satisfy $q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2}-q^{-1/2})\mathcal{M}(L_0)$. This relation descends from the $q$-deformed $\mathrm{SU}(2)$ Chern--Simons functional on the $1$-jet bundle prolongation of the CR manifold ([the braids and knots chapter](#chap:path-integrals-braiding)). $\square$
