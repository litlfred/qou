The self-consistency condition $G_{\mathrm{Planck}} = 1$ ([gravitational constant](#def:gravitational-constant)), combined with the quadratic-suppression series and the $q$-deformed Lyapunov exponent $\chi_q = 1/(2q-1)$ ([operational entropy](#def:operational-entropy)), determines the **$q$-deformed Hausdorff dimension** as an algebraic function of $q$:

$$
  d_{H,q} = \frac{(2q - 1)^2}{q^3}.
$$

This is exact within the $q$-deformed framework. It is a rational function of $q$ defined over any field $k$ with $q \in k^\times$. It differs from the classical Hausdorff dimension $d_H$ of the Julia set $J(f_q)$ over $\mathbb{C}$, which relies on the transcendental topological entropy $\ln 2$. See [operational entropy](#def:operational-entropy) for the detailed comparison.

The formula gives $d_{H,q}(1) = 1$ (unit circle), $d_{H,q} > 1$ for $1 < q < (3+\sqrt{5})/2$, and $d_{H,q} = 1$ again at the golden threshold $q = (3+\sqrt{5})/2 = \varphi^2 \approx 2.618$.

**Derivative and discrete step.**
The continuous derivative is

$$
  d_{H,q}'(q) = \frac{(2q-1)(3 - 4q)}{q^4},
$$

which is negative for $q > 3/4$. Thus, the $q$-deformed fractal dimension decreases as $q$ increases toward the Big Bang (for $q$ in the physical range $q > 1$).

**Discrete recurrence.**
Taking the natural step size $\delta q = \hbar_q = (q-1)/q$ (one Reeb phase advance in $q$-space), the discrete update per Planck step is

$$
  d_{H,q}^{(n+1)} = d_{H,q}^{(n)} + \frac{(2q_n - 1)(3 - 4q_n)(q_n - 1)}{q_n^5}.
$$

This defines a contraction mapping for $q > 3/4$. The iteration $d_{H,q} \to d_{H,q} + \Delta d_{H,q}$ flows monotonically toward $d_{H,q} = 0$. The fractal complexity of the Reeb dynamics decreases with increasing $q$, vanishing at $q \to \infty$ (the Big Bang, where the Julia set collapses to a point). The direction of decreasing $d_{H,q}$ coincides with increasing $q$ — pointing from the classical regime ($q \to 1$, maximal $d_{H,q}$) toward the Big Bang ($q \to \infty$, $d_{H,q} = 0$).

**Regime table.**

See [Table 1](#tbl:hausdorff-dimension-recurrence-table1-data).

The $q$-deformed $d_{H,q}$ and the classical Hausdorff dimension $d_H$ of the Julia set over $\mathbb{C}$ are distinct quantities ([classical Hausdorff dimension comparison](#rem:hausdorff-dimension-classical-comparison)).

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n} = (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit $q = 1$. This is a superattracting fixed point (the derivative $|1 - 1/q^2|$ vanishes at $q = 1$). Starting from our local $q_0$:

See [Table 3](#tbl:hausdorff-dimension-recurrence-table3-data).

It takes three Planck steps from our universe to reach the classical limit. The convergence is superlinear: each step squares the distance to $q = 1$. At the fixed point, $\eta_q = 1$ nat, meaning each Reeb operation carries exactly one natural unit of information.

**Cosmological arrow of time.**
The monotone decrease of $d_{H,q}$ with $q$ defines an information-theoretic arrow. The parameter $q$ flows from the classical limit (low $q$, maximal $d_{H,q}$, maximal fractal structure) toward the Big Bang (high $q$, $d_{H,q} = 0$, no structure). Reversing time reverses the discrete recurrence, flowing from lesser to greater fractal complexity. The second law of thermodynamics asserts that the $q$-deformed dimension increases as $q$ decreases. The universe gains information capacity as it ages.
