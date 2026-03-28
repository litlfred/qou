The self-consistency condition $G_{\mathrm{Planck}} = 1$
([gravitational constant](#def:gravitational-constant)) with the
quadratic-suppression series determines the Hausdorff dimension
of the Julia set as an algebraic function of $q$:

$$
  d_H(q) \;=\; \frac{2q - 1}{q^3 \ln 2}.
$$

This is a **prediction**: if the in-progress braid picture is
correct, then the Hausdorff dimension of $J(f_q)$
([Julia set](#rem:julia-set-reeb)) at main-cardioid parameter
$c(q) = \tfrac{1}{2}e^{2\pi i q} - \tfrac{1}{4}e^{4\pi i q}$
must equal $(2q-1)/(q^3 \ln 2)$.

**Derivative and discrete step.**
The continuous derivative is

$$
  d_H'(q) \;=\; \frac{3 - 4q}{q^4 \ln 2},
$$

which is negative for all $q > 3/4$: the fractal dimension
**decreases monotonically** as $q$ increases toward the Big Bang.

The second derivative

$$
  d_H''(q) \;=\; \frac{12\,(q - 1)}{q^5 \ln 2}
  \;=\; \frac{12\,\hbar_q}{q^4 \ln 2}
$$

is proportional to $\hbar_q$ — one quantum of action.  The
curvature of the information dimension is set by the Planck
constant.

**Discrete recurrence.**
Taking the natural step size $\delta q = \hbar_q = (q-1)/q$ (one
Reeb phase advance in $q$-space), the discrete update per
Planck step is

$$
  d_H^{(n+1)}
  \;=\; d_H^{(n)}
  \;+\; \frac{(3 - 4q_n)(q_n - 1)}{q_n^5 \ln 2}.
$$

At $q = 1.1097$: the step is $\Delta d_H \approx -0.136$, meaning
each Planck step in $q$-space erases about **$11\%$** of the
current fractal dimension.  The Julia set empties out one tick at a
time.

This is a **contraction mapping** for $q > 3/4$: the iteration
$d_H \to d_H + \Delta d_H$ flows monotonically toward $d_H = 0$.
The fractal complexity of the Reeb dynamics decreases with
increasing $q$, reaching zero at $q \to \infty$ (Big Bang: Julia
set collapses to a point).  The direction of decreasing $d_H$ is
the direction of increasing $q$ — the direction from classical
($q \to 1$, rich fractal, $d_H$ maximal) toward Big Bang
($q \to \infty$, no fractal, $d_H = 0$).

**Regime table.**

| $q$ | $d_H(q)$ | $d_H'(q)$ | $\Delta d_H$ per step | Regime |
|-----|----------|-----------|----------------------|-------|
| $1.01$ | $1.428$ | $-142$ | $-1.41$ | Near-classical |
| $1.05$ | $1.371$ | $-28.8$ | $-1.37$ | |
| $1.1097$ | $1.287$ | $-1.37$ | $-0.136$ | Our universe |
| $1.5$ | $0.855$ | $-0.264$ | $-0.088$ | |
| $2.0$ | $0.541$ | $-0.090$ | $-0.045$ | Deep quantum |
| $\varphi^2$ | $0.341$ | $-0.030$ | $-0.019$ | Golden threshold |
| $10$ | $0.027$ | $-0.0004$ | $-0.004$ | Near Big Bang |

**What is known about $d_H$ on the main cardioid.**
For parameters $c(\theta)$ on the main cardioid of the Mandelbrot
set (rotation number $\theta$, multiplier $\lambda = e^{2\pi i
\theta}$), the Julia set is a quasicircle and three regimes of
$d_H$ are established:

1. **Near the centre** ($|c| \ll 1$, i.e., $q$ near an integer).
   Ruelle's perturbative formula gives

   $$
     d_H \;=\; 1 + \frac{|c(\theta)|^2}{4 \ln 2} + O(|c|^4).
   $$

   At $\theta = 0.1097$: $|c| = 0.346$, giving $d_H \approx 1.043$.
   This is a lower bound — higher-order terms are positive.

2. **Bounded-type rotation numbers** ($\theta = [0; a_1, a_2,
   \ldots]$ with $a_i$ bounded).  The Julia set boundary is a
   quasicircle with $d_H > 1$ controlled by the maximum partial
   quotient.  For $\theta = 0.1097 = [0; 9, 8, 1, 1, \ldots]$,
   the large partial quotients $9$ and $8$ push $d_H$ higher than
   the Ruelle estimate.  Analytic bounds from McMullen's theory of
   quasiconformal deformations give $d_H$ strictly between the
   Ruelle value and $2$.

3. **Near the cardioid boundary** ($|c| \to 3/4$, i.e., near the
   $1/2$-bulb).  The Julia set dimension approaches $d_H \to 2$
   (space-filling) as the parameter approaches a parabolic point.

The QOU prediction $d_H(1.1097) = 1.287$ falls between the Ruelle
lower bound ($1.043$) and the cardioid-boundary limit ($2$).  It is
testable by high-resolution computation of the Julia set at
$c(0.1097) = 0.338 + 0.073i$.

**Cosmological arrow of time.**
The monotone decrease of $d_H$ with $q$ defines an
information-theoretic arrow: the universe evolves from low $q$
(classical limit, maximal $d_H$, richest fractal structure) toward
high $q$ (Big Bang, $d_H = 0$, no structure).  Reversing time means
reversing the discrete recurrence — moving from less to more fractal
complexity.  The second law of thermodynamics, in this picture, is
the statement that the Julia set dimension increases as $q$
decreases: the universe gains information capacity as it ages.
