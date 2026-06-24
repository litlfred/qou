The pre-$\tau$ identity follows directly from the unified knot mass formula
([`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)) with
three observations, each placing one term in $\mathbb{Q}(q)$:

1. **Descended piece.** The level-$0$ Markov trace
   $|\mathrm{tr}_M(\rho(\beta))|$ is the Jones polynomial
   $J_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$
   ([`thm:jones-markov-trace`](#thm:jones-markov-trace)), an element of
   $\mathbb{Q}(q)$.
2. **Singleton tower.** Each $\Phi_q(|\hat V_i|)$ is a quantum dilogarithm
   of an element of $\mathbb{Z}[q^{1/2}, q^{-1/2}]$, formally well-defined
   in the Habiro completion $\widehat{\mathbb{Z}[q]}$
   ([`def:habiro-ring`](#def:habiro-ring)) without analytic continuation.
3. **Pair tower.** Each pair contribution $\Phi_q(|\hat V_i \hat V_j|)$ is
   likewise in $\widehat{\mathbb{Z}[q]}$, with the $z^2$ prefactor
   established as an exact equality by
   [`lem:tower-pair-equality-fixed-level`](#lem:tower-pair-equality-fixed-level).

The full sum is therefore an element of
$\widehat{\mathbb{Z}[q]} \subset \mathbb{Q}(q)$ at every step, so
$\mathfrak{m}_{\mathrm{alg}}(\beta) = \Phi_1(\beta)/\hbar_q^2$ holds in
$\mathbb{Q}(q)$ before any specialisation. Applying $\tau_{\mathrm{arch}}$
at $q = q_0$ produces the numerical mass; multiplication by $\hbar_q^{-2}$
and identification with $\mathrm{Vol}(K)/\hbar_{q_0}^2$ via the volume
conjecture is the $\tau$-image step recorded by the archimedean companion
[`prop:topological-mass-formula`](#prop:topological-mass-formula) — used
there as a $\tau$-side identification, not as a derivation step. $\qquad\blacksquare$
