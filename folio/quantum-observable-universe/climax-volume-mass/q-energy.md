The **$q$-energy** of a particle knot $K$ evaluates the [categorical Hamiltonian](#def:categorical-hamiltonian) in the dimensionless substrate action/mass chart ($\ell_P = \hbar_q\,t_P = 1$), summing the rotational, translational, and rest-action projections derived from $(\mathbf{C}, A, \tau)$ and the substrate parameter $q$.

Let $K = \hat{\beta}$ be a particle knot with braid representative $\beta \in B_n$. The **$q$-energy** is

$$
  \mathfrak{E}_q(K) \;=\; \underbrace{J_q^2(K) \cdot \hbar_q}_{\text{rotational}}
  \;+\;
  \underbrace{p_q(\beta)^2 \cdot \hbar_q / (2\,[n]_q)}_{\text{translational}}
  \;+\;
  \underbrace{\mathfrak{S}_q(K)}_{\text{rest action / mass}},
$$

where:

- $J_q^2(K) = [j]_q [j+1]_q$ is the $q$-angular momentum ([q-angular momentum](#def:q-angular-momentum)),
- $p_q(\beta)$ is the $q$-momentum (writhe) ([q-momentum](#def:q-momentum)),
- $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\beta))$ is the categorical action — the Markov trace of the braid in the Hecke algebra $H_n(R, q)$,
- $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant,
- $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-number.

**At rest** ($p_q = 0$, $J_q = 0$):

$$
  \mathfrak{E}_q(K)\big|_{\text{rest}} \;=\; \mathfrak{S}_q(K) \;=\; \mathfrak{m}(K)
$$

in the substrate mass chart, whereas converting to the causal-cone chart ($c_q = 1/(q - 1)$) rescales the rest value by $c_q^2$ to $\mathfrak{E}(K) = \mathfrak{m}(K)\,c_q^2 = \mathfrak{m}(K)/(q - 1)^2$ ([categorical Hamiltonian](#def:categorical-hamiltonian)).
