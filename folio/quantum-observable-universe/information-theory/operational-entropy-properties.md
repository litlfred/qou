The operational entropy $\eta_q = (2q-1)/q^3$ ([operational entropy](#def:operational-entropy)) connects to the Hausdorff dimension, exhibits a forced self-consistency, and organizes the physical regimes.

**Derivation from the Manning--McCluskey formula.**
The Manning--McCluskey formula $d_H = \eta_q / \chi_q$ relates the Hausdorff dimension of the Julia set to the operational entropy, where $\chi_q$ is the Lyapunov exponent. In the $q$-deformed Reeb dynamics, the classical Lyapunov exponent $\chi = \ln 2$ (valid at $c = 0$, where the Julia set is the unit circle) is replaced by the $q$-deformed exponent:

$$
  \chi_q =  \frac{1}{2q - 1}.
$$

The substitution $\ln 2 \to 1/(2q-1)$ reflects that the framework operates in $q$-deformed information units rather than classical nats. The degree-$2$ map $f_q$ has an effective multiplier of $1/(2q-1)$ in the $q$-connection frame. At $q = 1$, this recovers $\chi_1 = 1$, meaning one nat per operation, which matches the unit-circle dynamics.

The $q$-deformed Hausdorff dimension of the Julia set is:

$$
  d_{H,q} := \frac{\eta_q}{\chi_q} = \eta_q (2q - 1) = \frac{(2q - 1)^2}{q^3}.
$$

**$d_{H,q}$ versus $d_H$.**
The formula $d_{H,q} = (2q-1)^2/q^3$ is exact within the $q$-deformed framework. It is not an approximation of the classical Hausdorff dimension $d_H$ over $\mathbb{C}$. The two quantities use different Manning--McCluskey inputs:

| | Classical $d_H$ | $q$-deformed $d_{H,q}$ |
|---|---|---|
| **Topological entropy** | $h_{\mathrm{top}} = \ln 2$ (degree-2 map) | $\eta_q = (2q-1)/q^3$ (operational entropy) |
| **Lyapunov exponent** | $\chi(c)$ (computed numerically) | $\chi_q = 1/(2q-1)$ (rational in $q$) |
| **Formula** | $d_H = \ln 2 / \chi(c)$ | $d_{H,q} = \eta_q / \chi_q$ |
| **At $q = 1$** | $d_H = \ln 2 / \ln 2 = 1$ | $d_{H,q} = 1/1 = 1$ |
| **At $q = q_0$** | $d_H \approx 1.047$ (transfer operator) | $d_{H,q} \approx 1.088$ (exact) |
| **Field dependence** | $\mathbb{C}$ only | Any field $k$ with $q \in k^\times$ |

The classical $d_H$ depends on the transcendental quantity $\ln 2$ and requires the analytic structure of $\mathbb{C}$. The $q$-deformed $d_{H,q}$ is a rational function of $q$. It applies over any field, including $\mathbb{F}_p$ or $\mathbb{Q}_p$. The two dimensions agree at $q = 1$ and at $q = \varphi^2$, but diverge elsewhere. The $3.9\%$ difference at $q = q_0$ is structural: classical conformal dynamics uses $\ln 2$ for the topological entropy, whereas the $q$-deformed dynamics uses $\eta_q$. In the QOU framework, $d_{H,q}$ rather than $d_H$ governs the physics.

Gravitational self-consistency forces this formula, without fitting ([operational entropy is forced by self-consistency](#rem:operational-entropy-self-consistency)).

**Physical interpretation.**
Each iteration of $f_q$ corresponds to one application of the $q$-connection $\nabla_q$ across a fibre ([Reeb operations per Planck unit](#prop:reeb-operations-per-planck)). The operational entropy $\eta_q$ measures the information generated per iteration, representing the number of distinguishable $q$-bits produced by one $R$-matrix evaluation. The total information processed per Planck time is:

$$
  I_P(q) = n_R(q) \eta_q = \frac{\eta_q}{\hbar_q} = \frac{2q-1}{q^2(q-1)},
$$

where $n_R(q) = 1/\hbar_q$ is the iteration count per Planck circuit ([Planck time](#def:planck-time)).

**Regime behaviour.**

| Regime | $q$ | $\eta_q$ | $d_{H,q}$ | Interpretation |
|--------|-----|----------|-----------|----------------|
| Classical limit | $q \to 1$ | $\to 1$ | $\to 1$ | One nat per step; Julia set = unit circle |
| Observable universe | $q_0$ | $0.892$ | $1.088$ | Moderate: each of ${\sim}10$ steps generates $0.89$ $q$-bits |
| Deep quantum | $\varphi^2$ | $0.327$ | $1.000$ | $d_{H,q}$ returns to $1$ at the golden threshold |
| Deep-quantum | $q \to \infty$ | $\to 0$ | $\to 0$ | Zero information per step; Julia set collapses |

**The golden crossover.**
The formula $d_{H,q} = (2q-1)^2/q^3$ equals $1$ at exactly two points: $q = 1$ and $q = (3 + \sqrt{5})/2 = \varphi^2 \approx 2.618$, where $\varphi = (1+\sqrt{5})/2$ is the golden ratio. For $1 < q < \varphi^2$, the Julia set is strictly more fractal than a circle ($d_{H,q} > 1$). Beyond $\varphi^2$, the Julia set is less complex than a circle ($d_{H,q} < 1$, tending toward a finite point set). This golden crossover coincides with the golden threshold ([golden ratio degeneration](#rem:golden-ratio-degeneration)), where the Siegel disk boundary has maximal fractal complexity.
