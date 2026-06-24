Decompose $\Delta_q$ into its three components:

$$
  \Delta_q \;=\; q^{-2} \Delta
  + q^{-1}(1 - q^{-1})\,\mathfrak{C}
  + (1 - q^{-1})^2\,\Delta_\xi,
$$

where $\mathfrak{C}$ is the Coriolis cross-coupling and $\Delta_\xi$ is
the pure Reeb-spin Laplacian.  Each of $\mathfrak{C}$ and $\Delta_\xi$
contains at least one factor of $\mathcal{L}_\xi$ or $\iota_\xi$.

The Gaussian $G_q$ depends only on the base coordinates $x \in M$,
not on the Reeb-fibre direction, hence

$$
  \mathcal{L}_\xi G_q = 0,
  \qquad
  \iota_\xi G_q = 0,
$$

so both the Coriolis and spin contributions vanish on $G_q$:

$$
  -\Delta_q G_q \;=\; -q^{-2} \Delta G_q \;=\; q^{-2} \nabla^2 G_q,
$$

where $\nabla^2 = \sum \partial_i^2$ is the analyst's Laplacian
(non-positive) and $\Delta = -\nabla^2$ is the Hodge Laplacian
(non-negative).  It remains to verify the classical calculation
$\partial_t G_q = q^{-2} \nabla^2 G_q$.  Direct differentiation gives

$$
  \partial_t G_q \;=\; G_q \left(
    -\frac{n}{2t} + \frac{q^2 |x|^2}{4t^2}
  \right),
  \quad
  \nabla^2 G_q \;=\; G_q \left(
    -\frac{n q^2}{2 t} + \frac{q^4 |x|^2}{4 t^2}
  \right),
$$

and multiplying the second by $q^{-2}$ yields exactly the first.
Hence $\partial_t G_q = -\Delta_q G_q$.  The initial-data condition
$G_q(t,\cdot) \to \delta_0$ as $t \downarrow 0$ is the standard
property of the Gaussian heat kernel.  $\qed$
$\qquad\blacksquare$
