*Proof.*  Decompose $\Delta_q$ into its three components:

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

**Existence at arbitrary $q > 0$.**  The formula for $G_q$ is a
*classical* Gaussian with variance $\sigma^2 = t/q^2$.  It is
convergent and strictly positive for every $q > 0$ and every $t > 0$.
In particular, at the physical substrate value
$q_0 \approx 1.11$ ([local substrate $q$](#prop:local-substrate-q)),
the $q$-Gaussian

$$
  G_{q_0}(t, x) \;=\; \bigl(4\pi t / q_0^2\bigr)^{-n/2}
  \exp\!\left(-\frac{q_0^2  |x|^2}{4t}\right)
$$

is a legitimate density with variance $\sigma^2 \approx 0.81\,t$ —
narrower than the classical Gaussian by a factor of
$q_0^{-2} \approx 0.81$.  No convergence obstruction appears in the
archimedean realisation of the $q$-heat kernel at $q_0 > 1$.

**Non-Reeb-invariant extensions.**  For a general initial datum with
non-trivial Reeb-fibre dependence, the fundamental solution is not
the Reeb-invariant Gaussian alone — it picks up additional modes
from $\Delta_\xi$, given by the Peter--Weyl decomposition
([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)).  The
Reeb-invariant sector is the *zeroth* Peter--Weyl component $j = 0$,
for which $\lambda_0(q) = 0$.
