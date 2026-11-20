*Proof.* One decomposes $\Delta_q$ into its three components:

$$
  \Delta_q \;=\; q^{-2} \Delta
  + q^{-1}(1 - q^{-1})\,\mathfrak{C}
  + (1 - q^{-1})^2\,\Delta_\xi.
$$

The operator $\mathfrak{C}$ is the Coriolis cross-coupling and $\Delta_\xi$ is the pure Reeb-spin Laplacian. Both $\mathfrak{C}$ and $\Delta_\xi$ contain at least one factor of $\mathcal{L}_\xi$ or $\iota_\xi$.

The Gaussian $G_q$ depends only on the base coordinates $x \in M$, not on the Reeb-fibre direction. Therefore,

$$
  \mathcal{L}_\xi G_q = 0,
  \qquad
  \iota_\xi G_q = 0.
$$

Both the Coriolis and spin contributions vanish on $G_q$:

$$
  -\Delta_q G_q \;=\; -q^{-2} \Delta G_q \;=\; q^{-2} \nabla^2 G_q.
$$

Here $\nabla^2 = \sum \partial_i^2$ is the non-positive analyst's Laplacian and $\Delta = -\nabla^2$ is the non-negative Hodge Laplacian. Direct differentiation yields

$$
  \partial_t G_q \;=\; G_q \left(
    -\frac{n}{2t} + \frac{q^2 |x|^2}{4t^2}
  \right),
  \quad
  \nabla^2 G_q \;=\; G_q \left(
    -\frac{n q^2}{2 t} + \frac{q^4 |x|^2}{4 t^2}
  \right).
$$

Multiplying the second equation by $q^{-2}$ yields the first. Hence $\partial_t G_q = -\Delta_q G_q$. The initial-data condition $G_q(t,\cdot) \to \delta_0$ as $t \downarrow 0$ follows from standard properties of the Gaussian heat kernel. $\square$

**Existence at arbitrary $q > 0$.** The formula for $G_q$ defines a classical Gaussian with variance $\sigma^2 = t/q^2$. It is convergent and strictly positive for every $q > 0$ and $t > 0$. At the physical substrate value $q_0 \approx 1.11$ ([local substrate $q$](#prop:local-substrate-q)), the $q$-Gaussian

$$
  G_{q_0}(t, x) \;=\; \bigl(4\pi t / q_0^2\bigr)^{-n/2}
  \exp\!\left(-\frac{q_0^2  |x|^2}{4t}\right)
$$

is a strict density with variance $\sigma^2 \approx 0.81\,t$. This is narrower than the classical Gaussian by a factor of $q_0^{-2} \approx 0.81$. No convergence obstruction appears in the archimedean realisation of the $q$-heat kernel at $q_0 > 1$.

**Non-Reeb-invariant extensions.** For a general initial datum with non-trivial Reeb-fibre dependence, the fundamental solution includes additional modes from $\Delta_\xi$. These modes form the Peter--Weyl decomposition ([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)). The Reeb-invariant sector corresponds to the zeroth Peter--Weyl component $j = 0$, where $\lambda_0(q) = 0$.
