The [q-NS system](#def:q-navier-stokes) at $q = 1$ recovers the classical incompressible Navier–Stokes equation on $\mathbb{R}^3$:

$$
  \partial_t v + (v \cdot \nabla)v = -\nabla p + \nu\Delta v,
  \qquad \nabla \cdot v = 0,
  \qquad v|_{t=0} = v_0.
$$

A central question in fluid dynamics is whether smooth initial data $v_0 \in C^\infty(\mathbb{R}^3)$ with $\nabla \cdot v_0 = 0$ and finite energy always produces a smooth global solution, or whether singularities can form in finite time.

The [NS obstruction](#def:ns-obstruction) $\mathrm{NS}(A)$ resolves this question using the categorical data of the quantum universe. If $\mathrm{NS}(A) = 0$, the flow is regular. If $\mathrm{NS}(A) \neq 0$, the flow blows up. This obstruction depends on the Euler characteristic $\chi(A)$. For $\chi(A) = 0$ ([torus example](#ex:torus-ns-regular)), the equation is globally regular. For $\chi(A) = -6$ ([Descartes universe](#thm:ns-singularity-descartes)), singularities form in finite time.
