The **$q$-energy** of a particle knot $K$ sums three terms derived from the categorical triple $(\mathbf{C}, A, \tau)$ and the aether parameter $q$.

**Definition.**
Let $K = \hat{\beta}$ be a particle knot with braid representative $\beta \in B_n$. The **$q$-energy** is:

$$
  \mathfrak{E}_q(K) \;=\; \underbrace{J_q^2(K) \cdot \hbar_q}_{\text{rotational}}
  \;+\;
  \underbrace{p_q(\beta)^2 \cdot \hbar_q / (2\,[n]_q)}_{\text{translational}}
  \;+\;
  \underbrace{\mathfrak{S}_q(K)}_{\text{action (rest mass)}}
$$

where:

- $J_q^2(K) = [j]_q [j+1]_q$ is the $q$-angular momentum ([q-angular momentum](#def:q-angular-momentum)),
- $p_q(\beta)$ is the $q$-momentum (writhe) ([q-momentum](#def:q-momentum)),
- $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\beta))$ is the categorical action — the Markov trace of the braid in the Hecke algebra $H_n(R, q)$,
- $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant,
- $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-number.

**At rest** ($p_q = 0$, $J_q = 0$):

$$
  \mathfrak{E}_q(K)\big|_{\text{rest}} \;=\; \mathfrak{S}_q(K) \;=\; \mathfrak{m}(K) c^2
$$

This recovers the topological mass formula.
