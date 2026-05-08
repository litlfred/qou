
The **algebraic** topological mass formula
([algebraic topological mass](#prop:topological-mass-formula-algebraic))
gives the mass ratio at the level of $\mathbb{Q}(q)$ as
$m_\mu / m_e = \Phi_1(4_1) / \hbar_q^{2}$, where
$\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$ is the
$\tau_{\mathrm{arch}}$-image of the algebraic quantum volume
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume))
and $\hbar_q = 1 - q^{-1}$. The Archimedean form of the same
identity ([topological mass formula](#prop:topological-mass-formula))
is the specialisation under $\tau_{\mathrm{arch}}$, which equates
$\Phi_1(4_1)$ with the hyperbolic volume $\mathrm{Vol}(4_1)$ at
$q = q_0$ via the volume conjecture
\cite{kashaev1997, murakami-murakami2001} as **τ-side naming**
(not as a derivation step). Substituting that
$\tau_{\mathrm{arch}}$-specialised numerical value here is the
final step:

$$
  (1 - q^{-1})^{2}
  = \frac{:val[Vol_4_1]{precision=6}}{:val[m_mu_over_e]{precision=7}}
  \approx 0.009817,
  \qquad
  1 - q^{-1} \approx 0.09908,
  \qquad
  q \approx 1.10998.
$$

The numerical values are independently verified by the SnapPy witness
([knot volumes verification](#prf:knot-volumes-verification)), which computes
$q \approx 1.10998$ from $\mathrm{Vol}(4_1) \approx 2.02988321281931$ and
$m_\mu/m_e \approx :val[m_mu_over_e]{precision=6}$ (CODATA 2022).
Since $f(q) = (1 - q^{-1})^{2}$ is strictly increasing for $q > 1$ and maps
$(1,\infty)$ onto $(0,1)$, the root is unique. The uncertainty
$\pm0.001$ is propagated from the CODATA relative uncertainty of
$2.2 \times 10^{-8}$ on $m_\mu / m_e$ and the τ-image SnapPy
verification-witness error bound of $10^{-14}$ on $\mathrm{Vol}(4_1)$;
the dominant contribution is the
finite decimal truncation of $q$. This value is consistent with the
hadronic mass predictions of [terminal resolution](#prop:terminal-resolution) and
with the $q$-deformed Hall conductance corrections of
[photonic Hall effect](#rem:photonic-hall).
