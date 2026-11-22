**Conjecture (open).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, let
$\beta_s = T_{2,9}$, $\beta_w = T_{3,5}$.  Each
admits a Wedderburn decomposition into central idempotents of the
ambient Hecke algebra $H_n(R, q)$:*

$$
  \beta_\bullet \;=\; \sum_{\lambda \,\vdash\, n}
    c_\lambda^{(\bullet)}\; e_\lambda,
  \qquad
  c_\lambda^{(\bullet)} \;=\; \chi_\lambda(\beta_\bullet) \in R.
$$

*Then the [Gram-determinant ratio](#def:cs-gram-determinant-ratio)
$\kappa = \det G^{\mathrm{cl}}_{\mathrm{CS}} / \det G^{q}_{\mathrm{CS}}$
appearing in the Chern-Simons :refterm[descent]{#descent}
(CS coupling) is given by a Plancherel-weighted character product of the
form*

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

The displayed product is not yet a well-defined element of $R$, and
making it one is part of the conjecture. Two points are open: $T_{2,9}$
is the closure of a braid on $2$ strands and $T_{3,5}$ of a braid on
$3$, so the two character families live on different Hecke algebras and
the product over $\lambda \vdash n$ needs a common $n$; and the exponents
$c_\lambda^{(s)} c_\lambda^{(w)}$ lie in $R$, not in $\mathbb{Z}$, so the
powers are not defined in $R$. Nothing downstream uses this formula: the
value $\kappa \approx 1.7216$ used in the $\alpha_{\mathrm{EM}}$ form is
computed directly from the two Gram determinants.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
