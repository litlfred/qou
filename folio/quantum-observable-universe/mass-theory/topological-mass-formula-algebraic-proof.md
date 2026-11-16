## Proof

The pre-$\tau$ identity follows directly from the unified knot
mass formula
([`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified))
with three observations:

1. **Descended piece.** The level-$0$ Markov trace
   $|\mathrm{tr}_M(\rho(\beta))|$ is the Jones polynomial
   $J_K(q)$
   ([`thm:jones-markov-trace`](#thm:jones-markov-trace)). Before the
   absolute value is taken, $\mathrm{tr}_M(\rho(\beta))$ is an element of
   $\mathbb{Z}[q^{\pm 1}][(q^{2}+1)^{-1}] \subset \mathbb{Q}(q)$; the absolute
   value itself is archimedean and is applied after $\tau_{\mathrm{arch}}$.
2. **Singleton tower.** Each $\Phi_q(|\hat V_i|)$ is a quantum
   dilogarithm of an element of $\mathbb{Z}[q^{1/2}, q^{-1/2}]$;
   formally well-defined in the Habiro completion
   $\widehat{\mathbb{Z}[q]}$
   ([`def:habiro-ring`](#def:habiro-ring)) without analytic
   continuation.
3. **Pair tower.** Each pair contribution
   $\Phi_q(|\hat V_i \hat V_j|)$ is similarly in
   $\widehat{\mathbb{Z}[q]}$, with the $z^2$ prefactor
   established by
   [`lem:tower-pair-equality-fixed-level`](#lem:tower-pair-equality-fixed-level)
   as an exact equality.

The tower terms are therefore formal elements of the Habiro
completion $\widehat{\mathbb{Z}[q]}$, while the descended piece lies in
$\mathbb{Q}(q)$. Neither ring contains the other: $\widehat{\mathbb{Z}[q]}$
contains $\sum_{n} (q;q)_n$, which is not a rational function, and
$\mathbb{Q}(q)$ contains $1/(q^{2}+1)$, which is not in
$\widehat{\mathbb{Z}[q]}$. So the sum is not claimed to lie in a single one
of them before $\tau_{\mathrm{arch}}$. The
$\tau_{\mathrm{arch}}$ specialisation at $q = q_0$ then produces
the canonical mass; multiplication by $\hbar_q^{-2}$ and
identification with $\mathrm{Vol}(K) / \hbar_{q_0}^{2}$ via the
volume conjecture is the τ-image step recorded by
[`prop:topological-mass-formula`](#prop:topological-mass-formula).
$\square$
