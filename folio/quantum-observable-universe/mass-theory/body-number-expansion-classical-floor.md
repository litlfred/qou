The [subset-cumulant recursion](#prop:subset-cumulant-recursion) reads the genuine $k$-body content of a nucleus off the Markov trace as the order-$k$ Möbius cumulant of $L(S) = \log(\mathrm{tr}_{\mathrm{free}}/\mathrm{tr}_S)$. A natural question is whether these cumulants are *ordered* in the deformation parameter $\varepsilon = q - 1$: whether the $k$-body term is smaller than the $(k-1)$-body term by a power of $\varepsilon$, so that the body-number expansion would carry a power counting of the kind an effective field theory organises its operators by. This remark records that it does not, and why.

**The bond factors at the classical point.** With the bonds placed by the canonical interface composition, the ratio $\mathrm{tr}_S/\mathrm{tr}_{\mathrm{free}}$ is a product of interface factors, one per bond, each of the form $z + d$: the Markov parameter $z$ of the [trace selection](#prop:markov-trace-frobenius-selection), $z_D = q^{3}/(q^{2} + 1)$ in convention D, plus a correction $d$ depending on the kind of the interface (proton–proton, proton–neutron, neutron–neutron). Expanded at $q = 1 + \varepsilon$ the three bond factors are

$$
  \tfrac12 + \varepsilon + \tfrac14 \varepsilon^{2}, \qquad
  \tfrac12 + 0\cdot\varepsilon + \tfrac34 \varepsilon^{2}, \qquad
  \tfrac12 - \varepsilon + \tfrac54 \varepsilon^{2}
$$

to second order, and the point is the common constant term: $z_D(1) = 1/2$, and every $d$ vanishes at $\varepsilon = 0$. At the classical point every bond factor is $1/2$, whatever its kind.

**The cumulant does not vanish.** Write $f_e$ for a bond factor and $g_e = f_e - 1$ for its Mayer variable; the connected three-body cumulant of the multiplicative assembly is minus the third Ursell function, $b_3 = -\varphi^{T}_{3}(g_{12}, g_{13}, g_{23})$ with $\varphi^{T}_{3} = g_{12}g_{13}g_{23} + g_{12}g_{13} + g_{12}g_{23} + g_{13}g_{23}$, the sum over the connected spanning graphs on three vertices. At the classical point $g_e = -1/2$ for every bond, so

$$
  b_3\bigl(\tfrac12, \tfrac12, \tfrac12\bigr) \;=\; -\Bigl(-\tfrac18 + \tfrac34\Bigr) \;=\; -\tfrac58 \;\neq\; 0 ,
$$

and the same computation for four bodies gives $b_4 = 79/64$. The three-body term therefore has $\varepsilon$-valuation zero: it is not suppressed relative to the two-body term by any power of $\varepsilon$, and the body-number expansion at fixed $q$ is a lattice-gas cluster expansion with weights of order one. Its convergence is a question about the size of the Mayer variables rather than about a small parameter. (For the mixed triple of one bond of each kind the $\varepsilon$-series of $b_3$ begins $-5/8 + 0\cdot\varepsilon + \tfrac{35}{16}\varepsilon^{2}$; the vanishing of the linear term is a property specific to that triple rather than a general one.)

**Classical floor of the trace difference.** The classical floor of the trace difference $\Delta = \mathrm{tr}_{\mathrm{free}} - \mathrm{tr}_{\mathrm{atom}}$, the coefficient $c_0 = 2^{-A} - 2^{1 - 2A}$ of $\varepsilon^{0}$, is nonzero for every $A \geq 2$; it is the same fact seen through the difference rather than through the cumulants.

**Jet-tower ordering in $\hbar_q^{2n}$.** The expansion of the framework that *is* geometric is the jet tower: the transfer operator is a series in $\hbar_q^{2n}$ over jet levels $n$ with remainder ratio $q^{-2}$, so that the local single-jet contribution leads and corrections form a geometric series. The framework's small parameter counts jet level rather than body number. An effective-field-theory reading of the corpus is therefore a statement about the jet tower (the truncation order of the ladder, the descended level-zero holonomy) rather than about the many-body assembly, whose expansion parameter is the bond weight itself.

**Scope.** This excludes an ordering *in $\varepsilon$*, on the strength of the identity $z_D(1) = 1/2$; it is a structural exclusion of that ordering and nothing more. It does not exclude an ordering of the body-number expansion in some other quantity, and it does not bear on the sign question for $b_3$, which is a question about the bond factors at the physical point.
