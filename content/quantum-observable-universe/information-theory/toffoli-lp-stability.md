**Proposition.**
*Let $T_q \in H_3(q)$ be the $q$-Toffoli element. It is realised as the $3$-strand braid word whose traced volume matrix is $M(q)$ ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis ([Gram matrix](#prop:frobenius-gram-matrix)). Write the $q$-Toffoli in NF coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:*

1. **(Stability region.)** *The $q$-Toffoli element is LP-stable ([LP-dual stability](#prop:lp-dual-stability)) on the **physical regime** $q > 1$. All Hecke amplitudes have the correct sign. The confinement LP ([confinement as LP](#prop:confinement-lp)) is feasible. Three operator zeros in $(0, \infty)$ delimit sub-physical behaviour:*

$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
  \qquad
  q \,=\, 1,
$$

   *where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.*

2. **(Three operator thresholds.)** *Each zero corresponds to a vanishing Hecke amplitude:*

See [Table 1](#tbl:toffoli-lp-stability-table1-data).

   *At $q_\star$, the diagonal amplitude $P_{7,7}$ vanishes. At $q_\Phi$, the q-AND amplitude $\Phi$ reverses sign. At $q = 1$, the q-AND vanishes. The classical reversible Toffoli has trivial amplitude here.*

3. **(Dual shadow prices.)** *For $q > 1$, the LP dual has bounded shadow prices $y_i^*(q)$ satisfying:*

$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$

   *where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$ is the Gram condition number. At the physical substrate value $q_0 \approx 1.110$, $\kappa(G(q_0)) \approx 3.03$ (verified in the witness file). All shadow prices remain bounded in Skein units.*

4. **(Physical-substrate stability.)** *At $q_0 \approx 1.110$:*

$$
  P_{7,7}(q_0) \,\approx\, 0.5514,
  \qquad
  \Phi(q_0) \,\approx\, 0.0495.
$$

   *Both are strictly positive. The $q$-Toffoli is LP-stable at the physical substrate value. The set $\{q$-Toffoli$, H\}$ generates universal reversible computation on the Reeb bundles ([q-GoL](#prop:q-game-of-life)).*

**Substrate stability table** (verified numerically by `toffoli-lp-stability.witness.json`):

See [Table 2](#tbl:toffoli-lp-stability-table2-data).
