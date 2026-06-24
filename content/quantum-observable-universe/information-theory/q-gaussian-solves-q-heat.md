Over $\mathbb{R}^n$ with the archimedean realisation of the
$q$-Laplacian ([three-term expansion](#rem:q-laplacian-expansion)),
the **Reeb-invariant $q$-Gaussian**

$$
  G_q(t, x) \;=\; \bigl(4\pi q^{-2} t\bigr)^{-n/2}
  \exp\!\left(-\frac{q^2  |x|^2}{4t}\right)
$$

is a fundamental solution of the $q$-heat equation
([$q$-heat equation](#def:q-heat-equation)):

$$
  \partial_t G_q \;=\; -\Delta_q G_q,
  \qquad
  \lim_{t \downarrow 0} G_q(t, \cdot) \;=\; \delta_0.
$$

**Time rescaling interpretation.**  Since $-\Delta_q = q^{-2}\nabla^2$
on Reeb-invariant forms, writing $\tau = q^{-2} t$ gives

$$
  G_q(t, x) \;=\; \bigl(4\pi \tau\bigr)^{-n/2}
  \exp\!\bigl(-|x|^2 / (4 \tau)\bigr),
$$

the *classical* Gaussian heat kernel in rescaled time.  Physically:
Reeb-invariant diffusion on a QOU with substrate parameter $q$ is
isomorphic to ordinary diffusion, with the clock running at rate
$q^{-2}$.  At the Big Bang ($q \to \infty$) the clock freezes: heat
cannot spread on the base, because all the "diffusive budget" is
absorbed by the Reeb-fibre direction (which $G_q$ ignores).  At heat
death ($q \to 1$) the clock runs at unit rate and $G_q$ recovers the
classical Gaussian.

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
