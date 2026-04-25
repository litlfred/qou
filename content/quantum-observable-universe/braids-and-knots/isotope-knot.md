**Definition.**
*Two atom-knots ([atom](#def:atom-knot)) $K_1, K_2$ of types
$(Z, N_1)$ and $(Z, N_2)$ with $N_1 \neq N_2$ are
**isotopes** iff their NF block decompositions agree on the
proton-quark block:*

$$
  T_{w_1} \;=\; T_{w_{q^Z}} \cdot T_{w_{\bar q^{N_1}}^{(1)}}
                \cdot T_{w_{\mathrm{inter}}^{(1)}},
  \qquad
  T_{w_2} \;=\; T_{w_{q^Z}} \cdot T_{w_{\bar q^{N_2}}^{(2)}}
                \cdot T_{w_{\mathrm{inter}}^{(2)}},
$$

*with **identical $w_{q^Z}$**.*

*The isotope relation is an equivalence on $\{$atom-knots with
fixed $Z\}$ (reflexive: $K \sim K$; symmetric: trivial; transitive:
both share $w_{q^Z}$).  The isotope class of $K$ at fixed $Z$ is
parametrised by the neutron-quark block $w_{\bar q^N}$ and the
inter-nucleon connector $w_{\mathrm{inter}}$.*

**Two isotopes are knot-distinct.**
*Markov closures of $T_{w_1}$ and $T_{w_2}$ generally have
different Jones polynomials whenever $N_1 \neq N_2$, since the
neutron-quark blocks contribute distinct Hecke generators.  So
isotopes are different knots, not the same knot at different
substrate parameters.*

**Stability per isotope is independent.**
*The LP-dual ILP-feasibility ([stable atom](#def:stable-atom))
is computed on the full NF $T_w$ — including the $w_{\bar q^N}$
and $w_{\mathrm{inter}}$ blocks — so different isotopes can have
different stability at the same $q$ ([unstable
atom](#def:unstable-atom)).  This is the categorical analogue of
the classical observation that ${}^{12}\mathrm{C}$ is stable while
${}^{14}\mathrm{C}$ is not.*
