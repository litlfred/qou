**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**

*Let $n \geq 2$. Let $\beta \in B_n$ be a typed braid encoded as a sequence of crossings in $\{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\cdot\mathbf{1}\}$, with $h = q - q^{-1}$. The $q$-character on each 1-dimensional irreducible representation of $H_n(q)$ obeys the universal closed form:*

$$
\boxed{
  \chi^{(n)}_q(\beta) \;=\; q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}
  \qquad\text{and}\qquad
  \chi^{(1^n)}_q(\beta) \;=\; \bigl(-q^{-1}\bigr)^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)},
}
$$

*where:*
* $w(\beta) = \#(\sigma_i) - \#(\sigma_i^{-1})$ is the **writhe**.
* $m(\beta)$ is the number of **averaged** (operator-valued $\sigma_i - h/2$) crossings.
* $[2]_q = q + q^{-1}$ is the quantum integer.

This form is independent of $n$. The choice of 1-d irrep ($V_{(n)}$ trivial or $V_{(1^n)}$ sign) dictates the eigenvalue $\lambda_\sigma \in \{+q,\, -q^{-1}\}$.

This block operates on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at the substrate parameter $q_0$.
