Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Skein module
$\mathcal{S}_q = \mathcal{S}_q(\mathcal{C})$.

**Generators.** Call a knot type $K$ *fundamental* if its hyperbolic
volume vanishes: $\mathrm{Vol}(K) = 0$.  By the geometrization of knot
complements, these are precisely the torus knots (and the unknot).  In
the particle dictionary, the fundamental knots are the fermions:
the unknot (neutrino), trefoil $3_1$ (electron), cinquefoil $5_1$
(tau), and the torus$(p,2)$ family.

**Statement.** The Skein module $\mathcal{S}_q$ is generated as an
algebra by:

1. The fundamental (mass-zero) knot types $\{K_i\}_{i \in \mathcal{F}}$
   (torus knots), and
2. The Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ (the binding operation).

Every hadron $H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$
admits a **terminal Skein resolution**: iterating the Skein relation

$$
  q \cdot L_+ \;-\; q^{-1} \cdot L_-
  \;=\; (q - q^{-1}) \cdot L_0
$$

at every crossing in the linked configuration terminates in a finite
polynomial

$$
  [H] \;=\; \sum_{\alpha} c_\alpha(q) \cdot
  [K_{i_1}] \cdots [K_{i_k}]
$$

where each $[K_{i_j}]$ is the class of a fundamental knot and
$c_\alpha(q) \in \mathbb{Z}[q^{\pm 1}]$.

**Mass from linking.** Evaluating the mass functional
$\mathcal{M}$ on the Skein resolution gives:

$$
  \mathcal{M}(H)
  \;=\;
  \underbrace{Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})}_{\text{binding energy (from linking)}}
  \;+\;
  \underbrace{\sum_{i=1}^{n}
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{\,2}}}_{\text{constituent mass (zero for torus knots)}}
$$

where $Q(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial of
the linking configuration and
$\hbar_q = 1 - q^{-1}$.

**Consequence.** For hadrons composed entirely of fundamental
(torus-knot) constituents, $\mathrm{Vol}(K_i) = 0$ for all $i$, so
the entire inertial mass arises from the linking topology:

$$
  \mathcal{M}(H)
  \;=\; Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}).
$$

Mass is purely a property of *how* the constituents are linked, not
*what* they are.  The Skein polynomial $Q(q)$ encodes the crossing
structure of the binding Hopf link, and the substrate parameter $q$
converts this combinatorial data into a physical mass.  This explains
the sub-keV agreement with CODATA values
([terminal resolution](#prop:terminal-resolution)): the proton and
neutron masses are determined entirely by the Skein polynomial of the
Borromean/Hopf binding structure on three torus-knot constituents.
