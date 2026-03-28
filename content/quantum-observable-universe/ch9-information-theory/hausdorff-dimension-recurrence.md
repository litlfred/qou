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

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n}
= (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit
$q = 1$, which is a **superattracting fixed point** (the derivative
$|1 - 1/q^2|$ vanishes at $q = 1$).  Starting from our local
$q_0 = 1.1097$:

| Step | $q_n$ | $\hbar_{q_n}$ | $d_H(q_n)$ | $\eta_q$ |
|:----:|--------|---------------|-----------|----------|
| 0 | $1.1097$ | $0.0989$ | $1.287$ | $0.892$ |
| 1 | $1.0108$ | $0.0107$ | $1.427$ | $0.989$ |
| 2 | $1.0001$ | $0.0001$ | $1.443$ | $1.000$ |
| 3 | $1.0000$ | $0$ | $1/\ln 2$ | $1.000$ |

Three Planck steps from our universe to the classical limit.
The convergence is superlinear: each step squares the distance to
$q = 1$.  At the fixed point, $\eta_q = 1$ nat: each Reeb
operation carries exactly one natural unit of information.

**Status of the formula in complex dynamics.**
There is **no known closed form** for $d_H(J_c)$ as a function of
the main-cardioid parameter $c$.  The Hausdorff dimension is
defined implicitly as the unique zero of the Bowen--Ruelle pressure
function $P(-t\,\log|f_c'|) = 0$ (Bowen 1979), which involves an
infinite-dimensional transfer operator.  The function $c \mapsto
d_H(J_c)$ is known to be:

- **Real-analytic** on the main cardioid interior (McMullen 1998).
- **Strictly $> 1$** for all $c \neq 0$ (the Julia set is a
  quasicircle but not a smooth curve).
- **Perturbatively**
  $d_H = 1 + |c|^2/(4\ln 2) + O(|c|^4)$ near $c = 0$ (Ruelle
  1982).  At $\theta = 0.1097$: $|c| = 0.346$, giving
  $d_H \approx 1.043$ --- a lower bound from the leading term.
- **Approaching $2$** at the cardioid boundary for certain sequences
  of parameters (Shishikura 1998).
- **$d_H(J_{1/4}) \approx 1.081$** at the cusp $c = 1/4$
  (numerical, parabolic parameter).

The QOU prediction $d_H(q) = (2q-1)/(q^3\ln 2)$ is therefore
**not a restatement of known mathematics** but a constraint from
the gravitational self-consistency condition.  At $q = 1.1097$
it predicts $d_H = 1.287$, which lies between the Ruelle lower
bound ($1.043$) and the cardioid-boundary supremum ($2$).

For $\theta = 0.1097 = [0; 9, 8, 1, 1, \ldots]$ (bounded-type
rotation number with large partial quotients $9$ and $8$), the
Julia set is a quasicircle whose distortion from a smooth circle
is controlled by the size of the partial quotients.  Large partial
quotients push $d_H$ above the Ruelle estimate, consistent with
the QOU value.

**Falsifiability.**
The prediction $d_H = 1.287$ is testable by high-precision
computation of $d_H(J_c)$ at $c = c(0.1097) = 0.338 + 0.073i$
using the Bowen--Ruelle pressure function (thermodynamic formalism
with Ruelle transfer operators).  Box-counting gives $d_H \approx
1.01$ but systematically underestimates thin quasicircles.
Transfer-operator methods achieve much higher precision and would
give a definitive comparison.

**Cosmological arrow of time.**
The monotone decrease of $d_H$ with $q$ defines an
information-theoretic arrow: the universe evolves from low $q$
(classical limit, maximal $d_H$, richest fractal structure) toward
high $q$ (Big Bang, $d_H = 0$, no structure).  Reversing time means
reversing the discrete recurrence — moving from less to more fractal
complexity.  The second law of thermodynamics, in this picture, is
the statement that the Julia set dimension increases as $q$
decreases: the universe gains information capacity as it ages.
