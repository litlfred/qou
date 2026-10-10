**Archimedean realisation.**
Following the [categorical--archimedean bridge](#prop:categorical-archimedean-bridge), the fibre functor $\tau$ maps the categorical [$q$-Navier--Stokes system](#def:q-navier-stokes) to coordinates on the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \partial_t v + (v \cdot \nabla_A)v
  = 
  -\frac{1}{\rho}\nabla_A p
  -  \nabla_A Q_q
  +  \nu_q\Delta_q v
  +  \frac{1}{\rho}
  \nabla_A \cdot \boldsymbol{\sigma}_q,
$$

where $\nabla_A$ is the $\mathrm{SU}(2)$ covariant derivative, and the coordinates of the $q$-deformed viscous stress tensor are

$$
  (\boldsymbol{\sigma}_q)_{ij}
  = 
  \nu_q\rho
  \bigl(
    \nabla_{A,i}v_j + \nabla_{A,j}v_i
    - \tfrac{2}{3}(\nabla_A \cdot v)\delta_{ij}
  \bigr),
$$

joined by the continuity equation $\partial_t\rho + \nabla_A \cdot (\rho v) = 0$.
