**Proposition (knot-operator LP/SDP selection via Gram-inverse dual basis).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic. Let $\{b_i\}$ be a Frobenius-non-degenerate basis for the Iwahori-Hecke algebra $H_n(q)$. For any confinement target $T \in H_n(q)$, the selection of a knot operator $\beta(T_{m,m'}) \in H_n(q)$ producing $T$ is determined by the Frobenius-Gram-inverse LP/SDP dual basis:*

$$
  \min_{\substack{x \geq 0 \\ G^{-1} S x \;\geq\; n_T}}
  \;\;\sum_{m'} t_{(m, m')} \, x_{(m, m')}
$$

*By strong duality and complementary slackness, the LP dual variables $(y_0^*, y^*)$ supply the shadow price of the net-multiplicity constraint, the Frobenius positivity shadow prices, and the active set identifying which knot operators contribute to the bound state.*

The LP is feasible if and only if the demand profile lies in the positive cone spanned by the supply profiles. The dual solution isolates the minimum-action generators.
