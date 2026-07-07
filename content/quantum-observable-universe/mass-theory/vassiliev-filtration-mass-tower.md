The Markov trace $\operatorname{tr}_M(\beta)(q)$ expands about $q = 1$ in the Hecke deformation parameter $h = q - q^{-1}$:

$$
  \operatorname{tr}_M(\beta)(q)
  \;=\;
  c_0(\beta)
  \;+\;
  c_1(\beta) \cdot h
  \;+\;
  c_2(\beta) \cdot h^2
  \;+\;
  \cdots
$$

Each coefficient $c_k(\beta)$ is a Vassiliev invariant of type $k$. The graded decomposition by type establishes a canonical filtration by complexity. The leading term $c_0$ is the classical Markov trace. The type-2 term $c_2 \cdot h^2$ introduces the first mass-discriminating framing correction. Higher-order terms supply precision refinements, converging rapidly due to the suppression factor $|h|^k \approx (0.209)^k$ at $q_0 \approx 1.110$.

For the LP/SDP operator-selection framework, the Vassiliev filtration provides a canonical cost-vector basis at each type: $t_k^{(\mathrm{type}\,m)} = c_m(b_k)$. This decomposes the mass-formula optimisation into a graded hierarchy of independent linear programs.
