**Proposition (brane-tower convergence via q-Laplacian decay).**
*Dropping the locality assumption for composite physical observables
requires summing over the brane tower — an infinite jet
prolongation*
$$
  T(\rho) \;=\; \sum_{n \geq 1} \hbar_q^{2n} \, \Delta^{(n)}(\rho),
$$
*where $\Delta^{(n)}$ is the $n$-th iterated q-Laplacian on the
Reeb bundle. The tower sum converges absolutely for all $q$ in the
Wenzl positivity regime, and is dominated by the lowest-level local
contribution.*

**Bound.** For $q$ in the Wenzl regime
$q^{1/2} + q^{-1/2} > 2$, and for $\rho$ with bounded $L^2$ norm
on the Reeb bundle,
$$
  \boxed{\;
  \bigl|\,T(\rho) - \hbar_q^2 \,\Delta^{(1)}(\rho)\,\bigr|
  \;\leq\;
  \hbar_q^4 \, \|\rho\|_{L^2} \cdot
    \frac{q^{-2}}{1 - q^{-2}}
  \;.}
$$

The leading correction $\hbar_q^2 \, \Delta^{(1)}(\rho)$ is the
single-jet (local) Laplacian contribution; the remainder decays
geometrically with ratio $q^{-2} < 1$ (in the regime $q > 1$,
including the QOU substrate $q_0 \approx 1.110$).

**Mechanism — exponential damping of high modes.** The q-Laplacian
on a vortex filament of length $L_q$ has spectrum
$$
  \lambda_k^{(q)} \;=\; [k]_q^{\,2} \cdot \hbar_q / L_q^2,
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}}.
$$
For $q > 1$, the q-integer $[k]_q$ grows exponentially in $k$:
$[k]_q \sim q^k / (q - q^{-1})$ as $k \to \infty$. Therefore
high-wavenumber Reeb modes are damped at the exponential rate
$\exp\!\bigl(-\nu_q [k]_q^2 \, t\bigr)$. The $n$-th iterated
Laplacian acting on mode $k$ contributes a factor $\lambda_k^{(q),n}
\sim q^{2nk} / (q - q^{-1})^{2n}$, which is dominated by the
$\hbar_q^{2n} \sim (q - q^{-1})^{-2n}$ prefactor for any fixed
mode $k$.

**Geometric-series tail.** Iteration of the bound gives
$$
  T(\rho) \;=\;
  \sum_{n = 1}^{\infty}
    \hbar_q^{2n}\,\Delta^{(n)}(\rho)
  \;\leq\;
  \|\rho\|_{L^2} \,
  \sum_{n = 1}^{\infty}
    \hbar_q^{2n} \cdot q^{-2(n-1)}
  \;=\;
  \frac{\hbar_q^2 \, \|\rho\|_{L^2}}{1 - q^{-2}\hbar_q^2}
$$
which is a convergent geometric series in $q^{-2}\hbar_q^2 < 1$
for the substrate range $q > 1.05$ (covering the QOU calibration
window).

**Physical reading.** Dropping locality requires summing over all
causally connected knots, which is infinite. The q-Laplacian
exponential mode-damping ensures only the lowest few jet levels
contribute appreciably; the rest are suppressed geometrically. The
non-local integration is therefore finite, *dominated by local
contributions*, and computable to arbitrary precision by truncating
the tower at any fixed level.

This is the convergence statement underlying the QOU treatment of
composite operators: in the Gröbner–Shirshov tower expansion of a
hadron's mass, the leading term is the local single-jet contribution,
and the corrections form a geometric series in $\hbar_q^2 \cdot q^{-2}$.
