**Proposition.**
*The mass of a neutral atom $(Z, N)$ is*

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha \sum_i \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
$$

*where the **full traced volume** per generator is the
Wedderburn-weighted sum:*

$$
  \hat{V}_i^{\mathrm{full}}
  =
  w_{\mathrm{sym}} \cdot \lambda_i^{\mathrm{sym}}
  + w_{\mathrm{std}} \cdot \hat{V}_i^{\mathrm{std}}
  + w_{\mathrm{alt}} \cdot \lambda_i^{\mathrm{alt}}
$$

*with Wedderburn--Markov weights
$w_\lambda = \dim_q(\lambda)^2 / [3]_q!$ evaluated at the
baryon level $n = 3$:*

$$
  w_{\mathrm{sym}} = w_{\mathrm{alt}}
  = \frac{1}{[3]_q!} \approx 0.165, \qquad
  w_{\mathrm{std}} = \frac{[2]_q^2}{[3]_q!} \approx 0.669
$$

*and:*
- *$\alpha = m_e \times 8G$ where $G \approx 0.9160$ is Catalan's
  constant and $\mathrm{Vol}(\mathcal{B}_3) = 8G$ (theorem, not
  numerical).*
- *$\hat{V}_i^{\mathrm{std}} = z \cdot a_i + b_i$ is the traced
  volume of generator $i$ (standard representation trace).*
- *$\lambda_i^{\mathrm{sym}} = \prod_j (c_j q + d_j)$ and
  $\lambda_i^{\mathrm{alt}} = \prod_j (-c_j q^{-1} + d_j)$ are
  the symmetric and alternating eigenvalue products.*

*All weights are derived from $q_0$.  The formula has
**zero fitted parameters**.*

*The additive formula regularises the near-zero generator
($\hat{V}^{\mathrm{std}} \approx 0.002$ for $A \geq 4$): the
symmetric and alternating channels contribute $O(1)$ terms that
pull $\hat{V}^{\mathrm{full}}$ away from zero, replacing the
logarithmic singularity $\ln|0.002| \approx -6.1$ with
$\ln|0.14| \approx -1.9$.*

**Brane tower correction.**
*The single-level formula above computes the traced volume at
brane level $n = 0$.  The full tower
([topological decomposition](#thm:topological-mass)) multiplies
the product $\prod_i \hat{V}_i^{\mathrm{full}}$ by the
constant factor $\mathrm{Li}_2(q^{-2}) \approx 1.098$, adding
$\ln\mathrm{Li}_2(q^{-2}) \approx +0.094$ to
$\sum_i \ln|\hat{V}_i^{\mathrm{full}}|$.  This correction is
uniform across generators because each brane level $n$
contributes $q^{-2n}/n^2$ to the dilogarithm series, independent
of the crossing pattern.  Level~1 captures $73.9\%$ of the
tower; levels $1$--$3$ capture $94.3\%$; levels $1$--$10$
capture $99.75\%$.  The tower correction is $< 1\%$ of $\Phi$
and does not materially change the accuracy.*

**Log-separated approximation.**
*The additive formula can be approximated by separating the
logarithms:*

$$
  \sum_i \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
  \approx
  \Phi_1 + \beta_2 \Phi_2 + \beta_3 \Phi_3
$$

*where $\Phi_1 = \sum \ln|\hat{V}^{\mathrm{std}}|$,
$\Phi_2 = \sum \ln|\det M_i|$,
$\Phi_3 = \sum \ln|\lambda^{\mathrm{sym}}/\lambda^{\mathrm{alt}}|$,
with $\beta_2 = -2[3]_q$ (motivated) and
$\beta_3 \approx 0.050$ (fitted).  This effective formula
achieves $0.074\%$ mean error with one fitted parameter,
compared to $0.146\%$ for the exact additive formula with
zero fitted parameters.  The fitted $\beta_3$ compensates
for $\mathcal{B}_3$ dressing of hydrogen and ordering effects
in heavy nuclei.*
