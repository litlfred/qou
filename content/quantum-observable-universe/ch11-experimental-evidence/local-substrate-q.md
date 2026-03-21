In any sufficiently small neighbourhood $U \subset M$ of the observable
universe, the substrate parameter $q$
([Definition](#def:substrate-parameter)) satisfies
$$
  q\big|_U \;=\; 1.1097 \;\pm\; 0.001.
$$
More precisely, $q|_U$ is the unique real root $q > 1$ of the equation
$$
  (1 - q^{-1})^{2}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e},
$$
where $\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$ is the
hyperbolic volume of the figure-eight knot and $m_\mu / m_e = 206.768\,2827$
is the CODATA muon--electron mass ratio.

---

The topological mass conjecture (Conjecture 4.25) gives
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^{\,2}$ with
$\hbar_q = 1 - q^{-1}$ (see the proof of
[Proposition](#prop:skein-mass-relation)). Rearranging yields
the equation above. Substituting the numerical values,
$$
  (1 - q^{-1})^{2}
  = \frac{2.02988}{206.768}
  \approx 0.009\,817,
  \qquad
  1 - q^{-1} \approx 0.09908,
  \qquad
  q \approx 1.1097.
$$
Since $f(q) = (1 - q^{-1})^{2}$ is strictly increasing for $q > 1$ and maps
$(1,\infty)$ onto $(0,1)$, the root is unique. The uncertainty
$\pm\,0.001$ is propagated from the CODATA relative uncertainty of
$2.2 \times 10^{-8}$ on $m_\mu / m_e$ and the SnapPy error bound of
$10^{-14}$ on $\mathrm{Vol}(4_1)$; the dominant contribution is the
finite decimal truncation of $q$. This value is consistent with the
hadronic mass predictions of [Proposition](#prop:terminal-resolution) and
with the $q$-deformed Hall conductance corrections of
[Remark](#rem:photonic-hall).
