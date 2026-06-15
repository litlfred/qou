**Generators.** A knot type $K$ is *fundamental* if its hyperbolic
volume vanishes: $\mathrm{Vol}(K) = 0$.  By the geometrization of knot
complements, these are precisely the torus knots (and the unknot).  In
the particle dictionary, the fundamental knots are the fermions:
the unknot (neutrino), trefoil $3_1$ (electron), cinquefoil $5_1$
(tau), and the torus$(p,2)$ family.

**Generation.** The Skein module $\mathrm{Sk}_q$ is generated as an
algebra by the fundamental knot types $\{K_i\}_{i \in \mathcal{F}}$
and the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$.  Every hadron
$H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$
admits a **terminal Skein resolution**: iterating the Skein relation

$$
  q \cdot L_+ -  q^{-1} \cdot L_-
  =  (q - q^{-1}) \cdot L_0
$$

at every crossing terminates in a finite polynomial

$$
  [H] =  \sum_{\alpha} c_\alpha(q) \cdot
  [K_{i_1}] \cdots [K_{i_k}]
$$

where each $[K_{i_j}]$ is the class of a fundamental knot and
$c_\alpha(q) \in \mathbb{Z}[q^{\pm 1}]$.

**Mass from linking.**  By
([Skein-resolution mass formula](#lem:skein-mass-from-linking)),
$\mathcal{M}(H) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
+ \sum_i \mathrm{Vol}(K_i)/\hbar_q^2$.  For hadrons composed entirely
of fundamental (torus-knot) constituents, $\mathrm{Vol}(K_i) = 0$
for all $i$, so the entire inertial mass arises from the linking
topology, $\mathcal{M}(H) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})$.
$\square$
