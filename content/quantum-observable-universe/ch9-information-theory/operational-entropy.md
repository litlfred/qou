Let $f_q(z) = z^2 + c(q)$ be the quadratic iteration on the
exceptional divisor $E_c \cong \mathbb{P}^1(\mathbb{C})$
([Julia set of Reeb flow](#rem:julia-set-reeb)), and let
$\mu_q$ be the measure of maximal entropy on the Julia set
$J(f_q)$.  The *operational entropy* of the Reeb dynamics at
substrate parameter $q$ is the metric entropy

$$
  \eta_q \;:=\; h_{\mu_q}(f_q),
$$

where $h_{\mu_q}$ denotes the Kolmogorov--Sinai entropy of $f_q$
with respect to $\mu_q$.

**Bounds.**
For the degree-$2$ map $f_q$, the topological entropy is
$h_{\mathrm{top}}(f_q) = \log 2$ (independent of $q$), and the
variational principle gives $\eta_q \leq \log 2$ with equality
when $\mu_q$ is the measure of maximal entropy.  Over
$\mathbb{C}$, the Hausdorff dimension $d_H(q)$ of $J(f_q)$
provides a geometric bound via the Manning--McCluskey formula:

$$
  \eta_q \;=\; d_H(q) \cdot \chi_q,
$$

where $\chi_q = \int \log |f_q'| \, d\mu_q$ is the Lyapunov
exponent.  For parameters on the main cardioid,
$\chi_q = \log 2$ and hence $\eta_q = d_H(q) \cdot \log 2$.

**Physical interpretation.**
Each iteration of $f_q$ is one application of the $q$-connection
$\nabla_q$ across a fiber
([Reeb operations per Planck unit](#prop:reeb-operations-per-planck)).
The operational entropy $\eta_q$ measures the **information
generated per iteration** --- the number of distinguishable bits
produced by one $R$-matrix evaluation.  The total information
processed per Planck time is

$$
  I_P(q) \;=\; n_R(q) \cdot \eta_q
  \;=\; \frac{\eta_q}{\hbar_q},
$$

where $n_R(q) = 1/\hbar_q$ is the iteration count per Planck
circuit ([Planck time](#def:planck-time)).

**Regime behaviour.**

| Regime | $q$ | $\eta_q$ | Interpretation |
|--------|-----|----------|----------------|
| Big Bang | $q \to \infty$ | $\to 0$ | Julia set shrinks to a point; minimal information per step |
| Our universe | $1.1097$ | $d_H(1.1097) \cdot \log 2$ | Moderate: each of ${\sim}\,10$ steps generates $\eta_q$ bits |
| Golden threshold | $1/\varphi^2$ | $d_H(1/\varphi^2) \cdot \log 2$ | Peak $d_H$, maximal information density |
| Classical limit | $q \to 1$ | $\to \log 2$ | Full topological entropy; $d_H \to 1$ |

The notation $\eta_q$ (eta) is chosen to avoid collision with
Planck's constant $h$ and the reduced Planck constant $\hbar_q$.
