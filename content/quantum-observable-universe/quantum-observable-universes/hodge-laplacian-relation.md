The relationship between the Hodge star and the Laplacian carries over
to the $q$-deformed setting. Classically, the codifferential is
$\delta = (-1)^{nk+n+1}\star d\star$, so the Hodge star mediates
between differentiation and its adjoint. In the $q$-deformed theory,
the $q$-Hodge star $\star_q$ ([q-Hodge star](#def:q-hodge-star))
rescales the inner product by the substrate parameter $q$, and the
$q$-codifferential $\delta_q$ inherits this deformation.

The $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_qd_q$ is
formally self-adjoint with respect to the Webster inner product.
By the defining property $\langle d_q \alpha, \beta \rangle_\varTheta = \langle \alpha, \delta_q \beta \rangle_\varTheta$
([codifferential formula](#rem:q-codifferential-formula)):

$$
  \langle \Delta_q\alpha, \beta \rangle_\varTheta
  = \langle \delta_q\alpha, \delta_q\beta \rangle_\varTheta
  + \langle d_q\alpha, d_q\beta \rangle_\varTheta
  = \langle \alpha, \Delta_q\beta \rangle_\varTheta.
$$

Self-adjointness guarantees real eigenvalues and orthogonal
eigenspaces. In particular, $\ker \Delta_q$ (the space of particles)
is a well-defined subspace with a canonical complement.
