*Let $\mu = z + d$ with $d \in [-h,\,0]$ be an admissible interface scalar, so that
$\mu$ ranges over the band $[z-h,\,z]$. At $z = q^3/(q^2+1)$, whenever the two reduced
inequalities*

$$
  q - z \;<\; (z-h)\,(q+q^{-1}),
  \qquad
  z\,(q+q^{-1}) \;<\; z + q^{-1}
$$

*hold, every admissible $\mu$ satisfies*

$$
  \boxed{\;\; \mu_- \;<\; \mu \;<\; \mu_+ . \;\;}
$$

## Two separations, both conditional and both checked

The upper separation says the triplet weight lies above the band's ceiling,
$z < \mu_+$. Its reduced form $z(q+q^{-1}) < z+q^{-1}$ is, after substituting
$z = q^{3}/(q^{2}+1)$, equivalent to $q^{5} < q^{2}+1$ and therefore holds for
$q < 1.193859$.

The lower separation says the singlet weight lies below the band's floor,
$\mu_- < z-h$. Its reduced form is $q - z < (z-h)(q+q^{-1})$, which at $z = q^3/(q^2+1)$
holds for $q < 1.465571$.

The substrate parameter clears both, with $7.56\,\%$ of margin on the tighter of the
two. Neither is a knife-edge, and neither can be repaired by a better choice of $q$:
moving $q$ upward past $1.193859$ closes the upper separation only by moving $\mu_+$
into the band, which is not the same as reaching it from inside.

Both hypotheses are carried explicitly rather than folded into the statement, because
they depend on the loop parameter $z$: the band lies strictly between the two isospin
weights *given* the reduced inequalities, which must be verified for the chosen $z$.

## Dependence on the loop parameter $z$

At $z = q^3/(q^2+1)$ both reduced inequalities hold at $q_0$: the band $[z-h,\,z]$
contains the empirical deuteron point $B_{\mathrm{AME}}({}^2\mathrm{H})$ (attained at
$d = -0.11923\,h$), while $\mu_-$ lies strictly below the floor $z - h$ (by contrast,
at the smaller auxiliary parameter $z_{\mathrm{aux}} = 1/(q^{1/2}+q^{-1/2}) \approx 0.499320$,
$\mu_- \approx 0.303675$ sits inside $[0.290260,\, 0.499320]$ while the entire band sits
$30.69\,\%$ above $B_{\mathrm{AME}}({}^2\mathrm{H})$).

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. At
$q_0 = 1.10997858275138080759$ with $z = q^3/(q^2+1)$:

| quantity | value at $q_0$ | position |
|----------|---------------:|----------|
| $\mu_-$ ($T=0$) | $0.24729788674803459841$ | below the floor |
| $z-h$ (floor)   | $0.40362773835082593616$ | $63.22\,\%$ above $\mu_-$ |
| $z$ (ceiling)   | $0.61268803714646525160$ | --- |
| $\mu_+$ ($T=1$) | $0.75270211325196540159$ | $22.85\,\%$ above $z$ |

The two misses are $63.22\,\%$ and $22.85\,\%$ of the quantity each is measured
against. Neither is a margin a refinement absorbs.
