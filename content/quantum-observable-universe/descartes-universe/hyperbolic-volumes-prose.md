**Hyperbolic volumes and the topological mass ansatz.**
The key idea behind the following two propositions is that inertial mass
originates in the topology of knot complements. Every particle in the QOU
framework is identified with a knot or link $K$ (see the table in
[skein decomposition](#rem:skein-decomposition)). To each such knot one associates the
**hyperbolic volume** $\mathrm{Vol}(K)$: the volume of the complete
hyperbolic metric on the complement $S^3 \setminus K$, computed via the
Bloch--Wigner dilogarithm. For torus knots (e.g. the trefoil $3_1$) this
volume vanishes; for hyperbolic knots it is a positive topological invariant.
The figure-eight knot $4_1$, which the framework identifies with the Higgs
boson ([cohomological embedding](#prop:cohomological-embedding)),
has

$$
  \mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3)
    \approx 2.02988\,321\,281\,931,
$$

where $\mathrm{Cl}_2$ is the Clausen function (OEIS A091518; SnapPy-verified).

The **topological mass formula**
([topological mass formula](#prop:topological-mass-formula)) asserts that the
mass $\mathfrak{m}(K)$ of a particle with knot type $K$ is

$$
  \mathfrak{m}(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^{\,2}},
  \qquad
  \hbar_q \;:=\; 1 - q^{-1},
$$

where $q > 1$ is the
([substrate parameter](#def:substrate-parameter)) and $\hbar_q$ is the quantum
Planck constant ([quantum planck constant](#def:quantum-planck-constant)). For
*composite* states the mass functional $\mathcal{M}$ is *not*
additive; instead it satisfies a $q$-deformed Skein recursion at every
crossing in the color-exchange diagram, generalising the Jones-polynomial
Skein relation to a mass-valued setting.
