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

| $q$ | $d_{H,q}$ | Regime |
|-----|----------|-------|
| $1$ | $1.000$ | Classical limit (unit circle) |
| $1.01$ | $1.010$ | Near-classical |
| $q_0$ | $1.088$ | Our universe |
| $1.5$ | $1.185$ | Basilica ($c = -3/4$) |
| $2.0$ | $1.125$ | Deep quantum |
| $\varphi^2$ | $1.000$ | Golden crossover |
| $3.0$ | $0.926$ | Beyond golden |
| $10$ | $0.361$ | Near Big Bang |

**$d_{H,q}$ vs. $d_H$: comparison with classical Hausdorff dimension.**

For parameters $c(\varTheta)$ on the main cardioid of the Mandelbrot
set (rotation number $\varTheta$, multiplier $\lambda = e^{2\pi i \varTheta}$), the Julia set is a quasicircle and the classical
Hausdorff dimension $d_H$ satisfies:

1. **Ruelle perturbative** [ruelle1982] (valid near $|c| \ll 1$):

   $$
     d_H =  1 + \frac{|c(\varTheta)|^2}{4 \ln 2} + O(|c|^4).
   $$

   At $\varTheta = 0.1097$: $|c| = 0.346$, giving $d_H \approx 1.043$.

2. **Transfer operator** (numerical, Bowen–Ruelle): $d_H \approx 1.047$ at $N = 800$ grid points.

3. **QOU $q$-deformed**: $d_{H,q} = 1.088$.

The gap $d_{H,q} - d_H \approx 0.041$ is explained by the
different Manning–McCluskey inputs:

| | Classical $d_H$ | $q$-deformed $d_{H,q}$ |
|---|---|---|
| Topological entropy | $\ln 2 = 0.693$ | $\eta_q = 0.892$ |
| Lyapunov exponent | $\chi(c) \approx 0.662$ | $\chi_q = 0.820$ |
| Dimension | $0.693/0.662 = 1.047$ | $0.892/0.820 = 1.088$ |

The classical $d_H$ is a property of conformal dynamics over
$\mathbb{C}$.  The $q$-deformed $d_{H,q}$ replaces the
transcendental $\ln 2$ with the rational $\eta_q$ and the
numerical $\chi(c)$ with the algebraic $\chi_q$.  The QOU claim
is that $d_{H,q}$ governs the physics (it determines the
$q$-critical line, information bandwidth, and gravitational
self-consistency).

**There is no known closed form** for the classical $d_H(J_c)$ as
a function of the main-cardioid parameter $c$.  The Hausdorff
dimension is defined implicitly as the unique zero of the
Bowen--Ruelle pressure function $P(-t\log|f_c'|) = 0$
[bowen1979], which involves an infinite-dimensional transfer
operator.  The function $c \mapsto d_H(J_c)$ is:

- **Real-analytic** on the main cardioid interior [mcmullen1998].
- **Strictly $> 1$** for all $c \neq 0$ (the Julia set is a
  quasicircle but not a smooth curve).
- **Approaching $2$** at the cardioid boundary for certain sequences
  of parameters [shishikura1998].

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n} = (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit
$q = 1$, which is a **superattracting fixed point** (the derivative
$|1 - 1/q^2|$ vanishes at $q = 1$).  Starting from our local
$q_0$:

| Step | $q_n$ | $\hbar_{q_n}$ | $d_{H,q}$ | $\eta_q$ |
|:----:|--------|---------------|-----------|----------|
| 0 | $q_0$ | $0.0989$ | $1.088$ | $0.892$ |
| 1 | $1.0108$ | $0.0107$ | $1.010$ | $0.991$ |
| 2 | $1.0001$ | $0.0001$ | $1.000$ | $1.000$ |
| 3 | $1.0000$ | $0$ | $1.000$ | $1.000$ |

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
