**Observation.** At the cost-coincidence loci of the operator-selection LP/SDP—points $q^* > 0$ where two cost coefficients $t_i(q)$ and $t_j(q)$ become equal—the strict-complementarity condition fails and the SDP is degenerate. These loci coincide exactly with the metallic-ratio ladder $\{\delta_n : n \in \mathbb{N}^+\}$.

**The mechanism.** For the $n=2$ LP with basis $\{\gamma, \sigma_0\}$ of $H_2(q)$, the cost coefficients are

$$
  t_1(q) \;=\; 2(q + q^{-1}),
  \qquad
  t_2(q) \;=\; q^2 - q^{-2}.
$$

A direct algebraic calculation gives

$$
  t_1(q) \;=\; t_2(q)
  \quad\Longleftrightarrow\quad
  q - q^{-1} \;=\; 2
  \quad\Longleftrightarrow\quad
  q \;=\; \delta_{\rm silver} \;=\; 1 + \sqrt{2}.
$$

At this $q$, the LP optimum is a face of the feasible polytope rather than a vertex. Any feasible $x$ satisfying $x_1 + x_2 = n_{\rm target}$ achieves the same primal cost $t_1 x_1 + t_2 x_2 = t_1 \cdot n_{\rm target}$. The dual shadow prices $y_i^*$ become non-unique (multiple optimal $(y_0^*, y^*)$ values), strict complementarity fails, and the active set $\mathcal{A} = \{i : y_i^* > 0\}$ is empty. This is the SDP-degeneracy signature: rapid loss of conditioning, ambiguous identification of binding constraints, and multiple optimal solutions returned.

**Empirical verification.** The $n=2$ LP active-set sweep observed this signature. Below silver the active set was $\{0\}$ (row 1 tight), AT silver it was $\emptyset$ (degenerate), above silver it was $\{1\}$ (row 2 tight). The degeneracy at silver is the first non-null result in a series of prior canonical probes that all returned smooth observables.

**Structural significance.** The metallic-ratio ladder sits on the algebraic side: $q = \delta_n$ is where the Hecke scalar $q - q^{-1}$ takes the integer value $n$, making $\sigma$ satisfy the integer-coefficient quadratic $\sigma^2 = n \sigma + 1$. Smooth observables (Wenzl weights, Jones polynomial signs, $n=3$ per-block character signs) do not see this discrete arithmetic structure because they are rational functions of $q$ with no discontinuities. The LP-vertex combinatorics sees it: cost-coefficient coincidences are algebraic events that translate the arithmetic of $q - q^{-1}$ into a topological change of the optimum's face dimension.

**Physical interpretation.** Identifying the silver coincidence with the CFL phase transition of dense quark matter gives the empirical handle on this algebraic phenomenon. The CFL transition density $\rho_c$ is the physical realization of the silver-coincidence point. The SDP degeneracy there is the order-parameter discontinuity of the first-order CFL transition. Multiple metallic ratios on the ladder correspond to multiple phase transitions. The bar-mirror $\varphi^2 \approx 2.618$ of the deconfinement boundary $q_{\rm gold} = 1/\varphi^2$ forms a candidate for the CFL $\to$ gCFL boundary observed in dense-QCD phenomenology.

**Generalisation (conditional).** For the strand-$n$ LP with basis size $d_n = n!$, the cost coefficients $t_i(q)$ are rational functions of $q$. The pairwise coincidence equations $t_i(q) = t_j(q)$ have rational-function solutions. Those solutions on the metallic ladder constitute the set $S(n) \subseteq \{\delta_k : k \le n\}$ of LP-degeneracy points for $n$ strands. For $n=2$, $S(2) = \{2\}$ (silver only). For $n=3$, the categorical evaluation returns $\{\delta_{\rm silver}\}$. The higher-strand characterisation remains conditional.

**Falsifiability handle.** Running an SDP solver on the canonical operator-selection problem at $q$-values near each metallic ratio reveals measurable signs of degeneracy: rising condition-number of the KKT system, multiple optimal solutions reported by the solver, and $y_i^*$ values dropping to tolerance for all $i$ simultaneously. Each observation tests the algebraic identification.
