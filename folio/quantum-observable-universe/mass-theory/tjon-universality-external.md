The many-body magnitude leg of $\Delta_\lambda$ ([Per-partition $\Delta_\lambda$ value versus open super-pairwise many-body binding magnitude](#rem:delta-lambda-value-vs-magnitude)) is scored against an external observable—the empirical correlation between three-body and four-body binding energies, known in nuclear physics as the *Tjon line*. Separating what the effective-field-theory literature establishes from the inclusion--exclusion simplex expansion prevents an analogy from being misread as a derived premise.

## The external results

Two results are used.

**No four-body parameter at leading order.** Working in an effective theory of short-range interactions whose two-body scattering length $a$ is large compared with the natural low-energy length scale $\ell$ of the interaction ($|a| \gg \ell$), **Lucas Platter**, **Hans-Werner Hammer**, and **Ulf-G. Meißner** find that an $\mathrm{SU}(4)$-symmetric *one-parameter* three-nucleon interaction suffices to renormalise the four-nucleon system at leading order in $\ell/|a|$; the empirical triton--$\alpha$ correlation then follows by varying that single three-body parameter \cite{platter2005tjon}. With the binding energies $B({}^2\mathrm{H}) = 2.22\,\mathrm{MeV}$ and $B({}^3\mathrm{H}) = 8.48\,\mathrm{MeV}$ as inputs they obtain $B(\alpha) \approx 29.5\,\mathrm{MeV}$ for the $\alpha$-particle, against a Coulomb-corrected experimental $29.0 \pm 0.1\,\mathrm{MeV}$.

**A dimensionless four-to-three ratio.** Solving the four-boson Yakubovsky equations with no four-body parameter, **Hans-Werner Hammer** and **Lucas Platter** report that away from threshold the four-body ground state and the deepest three-body state are related by a factor of $5$ \cite{hammer2007fourbody}. The correlation is approximately linear away from threshold for either sign of $a$, with positive curvature for $a > 0$ and negative curvature for $a < 0$; the nonlinearity is confined to the threshold region.

## Limits of the external results

Each of the following is a separate statement that the results above do **not** license:

1. **"No four-body parameter is needed" is not "no four-body force exists."** The first is a statement about leading-order renormalisation; the second is a statement about physical interactions. The four-nucleon force is small, not absent: **Eric D. Jurgenson**, **Petr Navrátil**, and **Richard J. Furnstahl** evaluate the similarity-renormalisation-group-induced four-body contribution at ${}^4\mathrm{He}$ as a net effect of order tens of keV, with the long-range $\mathrm{N}^3\mathrm{LO}$ estimate of order a few hundred keV \cite{jurgenson2009srg}.

2. **The leading-order claim is contested in general.** Yamashita et al. find a strong sensitivity of the deepest four-body energy to a four-body subtraction constant, concluding that a four-body parameter should generally enter at leading order. As noted in \cite{hammer2007fourbody}, both analyses agree on the nuclear case because short-range repulsion suppresses four-particle contact configurations, while general universality rests on the inherited renormalisation-group power counting.

3. **The zero-range limit is not the nuclear regime.** The universal ratio $5$ is a zero-range result, whereas experimental nuclear binding from AME2020 \cite{ame2020} gives $B({}^4\mathrm{He})/B({}^3\mathrm{H}) \approx 3.42$ after Coulomb correction; \cite{platter2005tjon} attributes the shift of its leading-order Tjon line to neglected finite-range effects.

## Inequivalence with the simplex condition

Expanding the many-body binding moment in an inclusion--exclusion simplex basis,

$$
  M(A) \;=\; \sum_k \mu_k \binom{A}{k},
$$

translates the naive ansatz $\mu_4 = 0$ into $M(4) = 4M(3) - 6M(2)$. That algebraic condition is provably inequivalent to leading-order three-body renormalisability. On the $\mu_4 = 0$ baseline, $M(4) < 4\,M(3)$ holds strictly for every $\mu_2 > 0$ and arbitrary $\mu_3$ (with deficit $-6\mu_2$), placing the universal zero-range ratio $M(4)/M(3) = 5$ outside the reachable cone. Conversely, substituting $M(4) = 5\,M(3)$ forces

$$
  \mu_4 \;=\; 9\mu_2 + \mu_3,
$$

so $\mu_4$ is largest precisely in a four-boson calculation carrying zero four-body interaction input. Because three moments fitted to three anchors ($A = 2, 3, 4$) determine an exact algebraic identity

$$
  \mu_4 \;:=\; M(4) - 4M(3) + 6M(2),
$$

$\mu_4$ measures only the departure of $M(4)$ from the two-point binomial extrapolation, not an irreducible physical four-body potential. The external Tjon-line literature therefore motivates tracking departures from two-point extrapolation, without deriving the simplex baseline or licensing a four-body force interpretation of $\mu_4$.
