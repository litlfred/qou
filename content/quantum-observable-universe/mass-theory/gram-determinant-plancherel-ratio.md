*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, let
$\beta_s = T_{2,9}$, $\beta_w = T_{3,5}$ be the unique pair of
genus-$4$ torus knots
([Bring uniqueness](#prop:force-carrier-bring-uniqueness)).  Each
admits a Wedderburn decomposition into central idempotents of the
ambient Hecke algebra $H_n(R, q)$:*

$$
  \beta_\bullet \;=\; \sum_{\lambda \,\vdash\, n}
    c_\lambda^{(\bullet)}\; e_\lambda,
  \qquad
  c_\lambda^{(\bullet)} \;=\; \chi_\lambda(\beta_\bullet) \in R.
$$

*Then the Gram-determinant ratio*

$$
  \kappa \;:=\; \frac{\det G^{\mathrm{cl}}_{\mathrm{CS}}}
                     {\det G^{q}_{\mathrm{CS}}}
$$

*appearing in the Chern-Simons :refterm[descent]{#descent}
(CS coupling) is given by the
Plancherel-weighted character product*

$$
  \boxed{\;
  \kappa \;=\;
  \prod_{\lambda \,\vdash\, n}
    \left[
      \frac{\dim V_\lambda}{\dim_q V_\lambda}
      \cdot
      \frac{[n]_q!}{n!}
    \right]^{c_\lambda^{(s)}\, c_\lambda^{(w)}}
  \,\in\, R.
  \;}
$$

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
