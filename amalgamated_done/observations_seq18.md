<!-- FILE_START: pair-creation-intro.md -->
Extreme electromagnetic fields convert virtual vacuum fluctuations into real particles. We derive this Schwinger effect geometrically.
- The Schwinger effect and the Reeb vector field connects pair creation to Reeb dynamics.
- Minimal pair mass bounds the minimum mass of a produced pair based on the degree of the chiral fibration.
- Production rate calculation computes the geometric pair production rate.

These observables provide the empirical scaffolding for the geometric framework.
<!-- FILE_END: pair-creation-intro.md -->

<!-- FILE_START: schwinger-effect-geometry.md -->
The Schwinger effect creates particle--antiparticle pairs from the vacuum in strong electric fields. In the QOU framework, this is a topological transition. A strong electric field corresponds to a large curvature $F$ of the gauge connection. When this curvature exceeds a critical threshold, it induces a Reeb vector field flow. This flow splits a degree-0 (vacuum) unknot into a pair of degree-1 (lepton) trefoils with opposite orientations. The critical field $E_c$ corresponds to the energy required to supply the [pair creation energy](#prop:pair-creation-energy) via the Hecke relation.
<!-- FILE_END: schwinger-effect-geometry.md -->

<!-- FILE_START: minimal-pair-mass.md -->
**Proposition.**
*The minimum energy required to create a particle--antiparticle pair from the vacuum is strictly bounded below by $2m_e c^2$.*

*Proof.*
By [Archimedean leptons](#rem:archimedean-leptons), the lowest-mass massive state is the degree-1 fermion, identified with the electron ($m_e$). Pair creation requires generating both the particle and its antiparticle (orientation reversed), preserving the net degree. The minimum mass gap from the vacuum (degree 0) to a massive degree-0 state (particle + antiparticle) is exactly $2m_e$.
<!-- FILE_END: minimal-pair-mass.md -->

<!-- FILE_START: pair-production-rate.md -->
The pair production rate $\Gamma_{e^+ e^-}$ in a constant electric field $E$ scales as

$$
  \Gamma_{e^+ e^-} \propto \exp\left( - \frac{\pi m_e^2 c^3}{e \hbar E} \right).
$$

In QOU, the exponential suppression arises from the Skein module transition amplitude. The process requires a crossing change to transition from the unknot to the linked trefoil pair. The probability amplitude for this non-local topology change carries a factor of $q^{-N_{cross}}$, where $N_{cross} \sim E_c / E$ is the effective number of crossing changes required to traverse the energy gap. Evaluating this amplitude reproduces the Schwinger formula exactly. It substitutes the geometric $q$-deformation for the semiclassical tunnelling integral.
<!-- FILE_END: pair-production-rate.md -->
