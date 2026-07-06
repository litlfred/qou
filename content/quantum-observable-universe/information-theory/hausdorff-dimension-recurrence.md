The self-consistency condition $G_{\mathrm{Planck}} = 1$
([gravitational constant](#def:gravitational-constant)) with the
quadratic-suppression series and the $q$-deformed Lyapunov exponent
$\chi_q = 1/(2q-1)$
([operational entropy](#def:operational-entropy)) determines the
**$q$-deformed Hausdorff dimension** as an algebraic function of
$q$:

$$
  d_{H,q} =  \frac{(2q - 1)^2}{q^3}.
$$

This is **exact** within the $q$-deformed framework — a rational
function of $q$ that works over any field $k$ with $q \in k^\times$.
It is distinct from the classical Hausdorff dimension $d_H$ of the
Julia set $J(f_q)$ over $\mathbb{C}$, which depends on the
transcendental topological entropy $\ln 2$.  See
[operational entropy](#def:operational-entropy) for the full
comparison.

The formula satisfies $d_{H,q}(1) = 1$ (unit circle), $d_{H,q} > 1$
for $1 < q < (3+\sqrt{5})/2$, and $d_{H,q} = 1$ again at the golden
threshold $q = (3+\sqrt{5})/2 = \varphi^2 \approx 2.618$.

**Derivative and discrete step.**
The continuous derivative is

$$
  d_{H,q}'(q) =  \frac{(2q-1)(3 - 4q)}{q^4},
$$

which is negative for $q > 3/4$: the $q$-deformed fractal dimension
**decreases** as $q$ increases toward the Big Bang (for $q$ in the
physical range $q > 1$).

**Discrete recurrence.**
Taking the natural step size $\delta q = \hbar_q = (q-1)/q$ (one
Reeb phase advance in $q$-space), the discrete update per
Planck step is

$$
  d_{H,q}^{(n+1)}
  =  d_{H,q}^{(n)}
  +  \frac{(2q_n - 1)(3 - 4q_n)(q_n - 1)}{q_n^5}.
$$

This is a **contraction mapping** for $q > 3/4$: the iteration
$d_{H,q} \to d_{H,q} + \Delta d_{H,q}$ flows monotonically toward
$d_{H,q} = 0$.  The fractal complexity of the Reeb dynamics
decreases with increasing $q$, reaching zero at $q \to \infty$ (Big
Bang: Julia set collapses to a point).  The direction of decreasing
$d_{H,q}$ is the direction of increasing $q$ — the direction from
classical ($q \to 1$, rich fractal, $d_{H,q}$ maximal) toward Big
Bang ($q \to \infty$, no fractal, $d_{H,q} = 0$).

**Regime table.**

See [Table 1](#tbl:hausdorff-dimension-recurrence-table1-data).

The $q$-deformed $d_{H,q}$ should not be confused with the classical
Hausdorff dimension $d_H$ of the Julia set over $\mathbb{C}$; the two
quantities and their comparison are treated separately
([classical Hausdorff dimension comparison](#rem:hausdorff-dimension-classical-comparison)).

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n} = (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit
$q = 1$, which is a **superattracting fixed point** (the derivative
$|1 - 1/q^2|$ vanishes at $q = 1$).  Starting from our local
$q_0$:

See [Table 3](#tbl:hausdorff-dimension-recurrence-table3-data).

Three Planck steps from our universe to the classical limit.
The convergence is superlinear: each step squares the distance to
$q = 1$.  At the fixed point, $\eta_q = 1$ nat: each Reeb
operation carries exactly one natural unit of information.

**Cosmological arrow of time.**
The monotone decrease of $d_{H,q}$ with $q$ defines an
information-theoretic arrow: the universe evolves from low $q$
(classical limit, maximal $d_{H,q}$, richest fractal structure)
toward high $q$ (Big Bang, $d_{H,q} = 0$, no structure).  Reversing
time means reversing the discrete recurrence — moving from less to
more fractal complexity.  The second law of thermodynamics, in this
picture, is the statement that the $q$-deformed dimension increases
as $q$ decreases: the universe gains information capacity as it ages.
