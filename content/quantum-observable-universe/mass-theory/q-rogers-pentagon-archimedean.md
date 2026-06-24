**Proposition (Post-$\tau$ pentagon = pre-$\tau$ pentagon + $q$-$\log^2$ Rogers correction).**

*The pentagon identity for the q-dilogarithm
([`def:q-dilogarithm`](#def:q-dilogarithm)) takes two structurally
distinct forms depending on whether the pre-$\tau$ (categorical R-side)
or post-$\tau$ (archimedean $\mathbb{R}$-side) register is operative
([`rem:pre-tau-vs-post-tau`](#rem:pre-tau-vs-post-tau)).*

### Pre-$\tau$ (bare) pentagon

*In the q-shuffle Hopf algebra $\mathcal{H}_q$ over
$R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$, the
q-dilogarithm satisfies the bare five-term identity*

$$
  \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) =
  \mathrm{Li}_2^q(uv) +
  \mathrm{Li}_2^q\!\!\left(\frac{u(1-v)}{1-uv}\right) +
  \mathrm{Li}_2^q\!\!\left(\frac{v(1-u)}{1-uv}\right) \tag{P}
$$

*as a Hopf-algebraic identity in $\mathcal{H}_q^{\otimes 2}$
([`prop:q-dilogarithm-unique`](#prop:q-dilogarithm-unique)): it is the
defining pentagon for the level-2 primitive, holding in $R$ without
any analytic considerations.*

### Post-$\tau$ (archimedean) pentagon

*Under the archimedean realization functor
([`def:archimedean-realization-functor`](#def:archimedean-realization-functor)),
$\mathrm{Li}_2^q$ realises as the convergent series
$\sum_n z^n / (n \cdot [n]_q)$ on $|z| < q$. The post-$\tau$ pentagon
**picks up a $\log_q^2$ correction term** with respect to the bare
identity:*

$$
  \boxed{\;
    \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) - \mathrm{Li}_2^q(uv) -
    \mathrm{Li}_2^q(\alpha) - \mathrm{Li}_2^q(\beta) \;=\;
    \log_q\!\!\left(\frac{1-u}{1-uv}\right) \cdot
    \log_q\!\!\left(\frac{1-v}{1-uv}\right) + O\bigl((q-1)^2\bigr)
  \;}
  \tag{R}
$$

*where $\alpha = u(1-v)/(1-uv)$, $\beta = v(1-u)/(1-uv)$, and
$\log_q$ is the q-logarithm ([`def:q-logarithm`](#def:q-logarithm)).*
