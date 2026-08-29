Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realized as the $3$-strand braid word with traced volume matrix $M(q)$. Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis. Express the $q$-Toffoli in normal-form coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:

1. **(Stability region.)** The $q$-Toffoli element is LP-stable on the physical regime $q > 1$. All Hecke amplitudes carry the correct sign, rendering the confinement LP feasible. Three operator zeros in $(0, \infty)$ delimit sub-physical behavior:
$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
  \qquad
  q \,=\, 1,
$$
where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.

2. **(Three operator thresholds.)** Each zero corresponds to a vanishing Hecke amplitude:
See [Table 1](#tbl:toffoli-lp-stability-table1-data).
At $q_\star$, the diagonal amplitude $P_{7,7}$ vanishes **in the convention-$C$ frame**; under the canonical $z_D = q^3/(q^2+1)$ the diagonal is $q^3(q^4+1)/(q^2+1)^2$, strictly positive for every $q > 0$, so this threshold is a property of the excised frame rather than of the gate. At $q_\Phi$, the q-AND amplitude $\Phi$ reverses sign. At $q = 1$, the q-AND vanishes. The classical reversible Toffoli has trivial amplitude here.

3. **(Dual shadow prices.)** For $q > 1$, the LP dual admits bounded shadow prices $y_i^*(q)$ satisfying:
$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$
where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. **Open (2026-08-09).** The figure previously quoted here, $\kappa(G(q_0)) \approx 3.03$, is withdrawn. It came from a Gram matrix built with the naive length rule $\mathrm{tr}_M(T_w) = z^{\ell(w)}$ — the pre-2026-05-19 $\mathrm{tr}_M(e^-) = z^3$ bug — under the excised convention C, in float64, at a superseded 17-digit $q_0$; it corresponds to no convention in the registry. Under the production convention D the Markov–Gram form is **singular**, so $\lambda_{\max}/\lambda_{\min}$ in the ordinary sense is infinite and the bound above is not available on the full six-dimensional NF span. Whether the shadow-price bound is to be re-posed on the quotient by the radical is the same decision as for Term 4 of the six-term mass identity and is reserved for the owner. The replacement value must be read off a regenerated `toffoli-lp-stability.witness.json`; it is not to be hand-edited, and the producer needs three fixes (convention, trace rule, precision) before it can be re-run.

4. **(Physical-substrate stability.)** At $q_0 \approx 1.110$:
$$
  P_{7,7}(q_0) \,\approx\, 0.5514,
  \qquad
  \Phi(q_0) \,\approx\, 0.0495.
$$
Both are strictly positive. The $q$-Toffoli is LP-stable at the physical substrate value. The set $\{q\text{-Toffoli}, H\}$ generates universal reversible computation on the Reeb bundles.

**Substrate stability table:**
See [Table 2](#tbl:toffoli-lp-stability-table2-data).
