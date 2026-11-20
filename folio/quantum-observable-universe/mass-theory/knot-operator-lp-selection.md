*Let $R$ be the categorical coefficient ring with $q \in R$ generic. Let $\{b_i\}$ be a basis for the Iwahori-Hecke algebra $H_n(q)$. For any confinement target $T \in H_n(q)$, the selection of a knot operator $\beta(T_{m,m'}) \in H_n(q)$ producing $T$ is determined by the LP/SDP dual basis of the Frobenius Gram pseudo-inverse:*

$$
  \min_{\substack{x \geq 0 \\ G^{+} S x \;\geq\; n_T}}
  \;\;\sum_{m'} t_{(m, m')} \, x_{(m, m')}
$$

*Here $G$ is the Frobenius Gram matrix of $\{b_i\}$ and $G^{+}$ is its Moore–Penrose pseudo-inverse, the inverse of the trace form on the quotient $H_n(q)/\mathrm{rad}$ by its radical; when $G$ is non-degenerate, $G^{+} = G^{-1}$. By strong duality and complementary slackness, the LP dual variables $(y_0^*, y^*)$ supply the shadow price of the net-multiplicity constraint, the Frobenius positivity shadow prices, and the active set identifying which knot operators contribute to the bound state.*

The LP is feasible if and only if the demand profile lies in the positive cone spanned by the supply profiles. The dual solution isolates the minimum-action generators.
