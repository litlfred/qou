Let $f_q(z) = z^2 + c(q)$ be the quadratic iteration on the
exceptional divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$
([Julia set of Reeb flow](#rem:julia-set-reeb)), and let
$\mu_q$ be the measure of maximal entropy on the Julia set
$J(f_q)$.  The *operational entropy* of the Reeb dynamics at
substrate parameter $q$ is

$$
  \eta_q \;:=\; \frac{2q - 1}{q^3},
$$

measuring the information generated per $f_q$-iteration in
natural units (nats).

**Derivation from the Manning--McCluskey formula.**
The Hausdorff dimension of the Julia set and the operational
entropy are related by the Manning--McCluskey formula
$d_H = \eta_q / \chi_q$, where $\chi_q$ is the Lyapunov exponent.
In the $q$-deformed Reeb dynamics, the classical Lyapunov exponent
$\chi = \ln 2$ (valid at $c = 0$, where the Julia set is the unit
circle) is replaced by the $q$-deformed exponent

$$
  \chi_q \;=\; \frac{1}{2q - 1}.
$$

The replacement $\ln 2 \to 1/(2q-1)$ reflects that the QOU
operates in $q$-deformed information units, not classical nats:
the degree-$2$ map $f_q$ has effective multiplier
$1/(2q-1)$ in the $q$-connection frame, not $\ln 2$.  At $q = 1$:
$\chi_1 = 1$ (one nat per operation, matching the unit-circle
dynamics).

The Hausdorff dimension of the Julia set is then

$$
  d_H(q) \;=\; \frac{\eta_q}{\chi_q}
  \;=\; \eta_q \cdot (2q - 1)
  \;=\; \frac{(2q - 1)^2}{q^3}.
$$

**Self-consistency.**
This formula is not assumed — it is **forced** by the gravitational
self-consistency condition $G_{\mathrm{Planck}} = 1$
([gravitational constant](#def:gravitational-constant)).  With the
quadratic-suppression series for the in-progress braid entropy,
$S_{\mathrm{cell}} = \eta_q \cdot \hbar_q^2 / (1 - \hbar_q^2)$,
the condition $G_{\mathrm{Planck}} = 1$ reduces algebraically to
$\eta_q = (2q-1)/q^3$.  No numerical fitting is involved.

**Physical interpretation.**
Each iteration of $f_q$ is one application of the $q$-connection
$\nabla_q$ across a fibre
([Reeb operations per Planck unit](#prop:reeb-operations-per-planck)).
The operational entropy $\eta_q$ measures the **information
generated per iteration** — the number of distinguishable nats
produced by one $R$-matrix evaluation.  The total information
processed per Planck time is

$$
  I_P(q) \;=\; n_R(q) \cdot \eta_q
  \;=\; \frac{\eta_q}{\hbar_q}
  \;=\; \frac{(2q-1)}{q^2(q-1)},
$$

where $n_R(q) = 1/\hbar_q$ is the iteration count per Planck
circuit ([Planck time](#def:planck-time)).

**Regime behaviour.**

| Regime | $q$ | $\eta_q$ | $d_H(q)$ | Interpretation |
|--------|-----|----------|-----------|----------------|
| Classical limit | $q \to 1$ | $\to 1$ | $\to 1$ | One nat per step; Julia set = unit circle |
| Our universe | $1.1097$ | $0.892$ | $1.088$ | Moderate: each of ${\sim}\,10$ steps generates $0.89$ nats |
| Deep quantum | $\varphi^2$ | $0.327$ | $1.000$ | $d_H$ returns to $1$ at the golden threshold |
| Big Bang | $q \to \infty$ | $\to 0$ | $\to 0$ | Zero information per step; Julia set collapses |

**The golden crossover.**
The formula $d_H(q) = (2q-1)^2/q^3$ equals $1$ at exactly two
points: $q = 1$ and $q = (3 + \sqrt{5})/2 = \varphi^2 + 1
\approx 2.618$, where $\varphi = (1+\sqrt{5})/2$ is the golden
ratio.  For $1 < q < \varphi^2 + 1$, the Julia set is strictly
more fractal than a circle ($d_H > 1$).  Beyond $\varphi^2 + 1$,
the Julia set is less complex than a circle ($d_H < 1$, tending
toward a finite point set).

This golden crossover coincides with the golden threshold
([golden ratio degeneration](#rem:golden-ratio-degeneration)),
where the Siegel disk boundary has maximal fractal complexity.
