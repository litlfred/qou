The [q-NS system](#def:q-navier-stokes) at $q = 1$ recovers the
classical incompressible Navier--Stokes equation on
$\mathbb{R}^3$:

$$
  \partial_t v + (v \cdot \nabla)v = -\nabla p + \nu\Delta v,
  \qquad \nabla \cdot v = 0,
  \qquad v|_{t=0} = v_0.
$$

A standard question in the analysis of this equation is whether
smooth initial data $v_0 \in C^\infty(\mathbb{R}^3)$ with
$\nabla \cdot v_0 = 0$ and finite energy always gives rise to a
smooth global solution, or whether singularities can form in
finite time.

The [NS obstruction](#def:ns-obstruction) $\mathrm{NS}(A)$
computes the answer from the categorical data of the quantum
universe: $\mathrm{NS}(A) = 0$ implies regularity;
$\mathrm{NS}(A) \neq 0$ implies blowup.  The obstruction
depends on $\chi(A)$.  For $\chi(A) = 0$
([torus example](#ex:torus-ns-regular)), the equation is
globally regular.  For $\chi(A) = -6$
([Descartes universe](#thm:ns-singularity-descartes)),
singularities form.
