The $q$-deformed Hausdorff dimension $d_{H,q} = (2q-1)^2/q^3$
([discrete recurrence](#rem:hausdorff-dimension-recurrence)) is
distinct from the classical Hausdorff dimension $d_H$ of the Julia
set $J(f_q)$ over $\mathbb{C}$. This remark records the classical
quantity and the gap between the two.

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

See [Table 2](#tbl:hausdorff-dimension-recurrence-table2-data).

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
