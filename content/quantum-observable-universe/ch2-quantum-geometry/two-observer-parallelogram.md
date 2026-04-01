Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$, and let
$\alpha \colon \mathbf{1} \to A$ be a
([fermion](#def:fermion-boson-decomposition)) regarded as a
([categorical point](#def:categorical-point)).
Consider two independent observations at $\alpha$,
$O_1, O_2 \colon A \to A$
([observation](#def:observation)).  These data
assemble into a *parallelogram of observations*:

```tex
\begin{equation}\label{eq:observation-parallelogram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  & O_1(\alpha) \arrow[dr, "\text{compare}"] & \\
  \alpha \arrow[ur, "O_1"]
         \arrow[dr, "O_2"']
  & & \delta\alpha \\
  & O_2(\alpha) \arrow[ur, "\text{compare}"'] &
\end{tikzcd}
\end{equation}
```

where $O_i(\alpha)$ denotes the composite $O_i \circ \alpha \colon
\mathbf{1} \to A$.  The discrepancy is the *commutator of observations*:

$$
  [O_1,\, O_2](\alpha)
  \;=\;
  (O_1 \circ O_2 - O_2 \circ O_1) \circ \alpha
  \;\in\; \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A).
$$

Each observation perturbs the substrate parameter by
$\delta q_i$ ([observation](#def:observation), condition (2)),
inducing shifted parameters $q_i' = q + \delta q_i$.  The commutator
$[q_1', q_2']$ measures the obstruction:

$$
  [O_1,\, O_2](\alpha)
  \;=\;
  [q_1',\, q_2'] \cdot \alpha_V,
$$

where $\alpha_V$ is the vertical (fermionic) component of $\alpha$
([fermion](#def:fermion-boson-decomposition)).

This vanishes if and only if $[q_1', q_2'] = 0$ (the shifted
parameters commute) or $\alpha_V = 0$ (the particle is a boson).
Generically, the non-cocommutativity of the Hopf structure ensures
$[q_1', q_2'] \neq 0$: independent observations of a fermion
necessarily disagree.
