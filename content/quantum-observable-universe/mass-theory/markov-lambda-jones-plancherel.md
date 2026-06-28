Given the [Wedderburn $\lambda$-block decomposition of the Markov
chain](#rem:markov-lambda-knot-operations), the Jones polynomial
factorises through the irreps as a Plancherel sum over $\lambda$.

The factorisation of the Jones polynomial through irreps is

```tex
\begin{equation}\label{eq:jones-plancherel}
  J_L(q)
  \;=\;
  \mathrm{tr}_M\bigl(\rho_q(\beta_L)\bigr)
  \;=\;
  \sum_{\lambda \vdash n}
    w_\lambda(q) \,\chi^\lambda_q\bigl(\rho(\beta_L)\bigr),
\end{equation}
```

where $w_\lambda(q)$ is the Ocneanu weight
([Jones--Markov trace](#thm:jones-markov-trace)) and
$\chi^\lambda_q(\rho(\beta_L)) = \mathrm{tr}\,\rho^\lambda_q(\beta_L)$
is the irreducible $q$-character of the closed braid in the
$\lambda$-block.

In the Markov-chain language this is an explicit
**classical/quantum factorisation**:

- **Classical layer.**  The normalised weights
  $\pi_\lambda(q) = w_\lambda(q) / \sum_\mu w_\mu(q)$ form a
  probability measure on partitions $\lambda \vdash n$.  Markov
  II moves a sample along the Young graph according to this
  measure.
- **Quantum layer.**  Inside each sector, the character
  $\chi^\lambda_q(\rho(\beta_L))$ is a closed-path amplitude
  sum over $\mathrm{SYT}(\lambda)$ with matrix elements given
  by Hoefsmit seminormal form
  ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
  The chain here is an amplitude walk in $V_\lambda$, with
  entries that are rational functions of $q$ and can be
  negative.

The Jones polynomial is therefore the expectation of a
quantum-amplitude observable under a classical probability on
$\lambda$.  This is the precise sense in which
$\lambda$ is the **classical label** of the knot-theoretic
process and SYT paths are its **quantum trajectories**.
