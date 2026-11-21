## Proof

**(i)** Direct computation from $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$.
Since $\sigma_i$ satisfies a quadratic with distinct roots $q$ and
$-q^{-1}$, the spectral projectors are
$e_\pm = (\sigma_i - \lambda_\mp)/(\lambda_\pm - \lambda_\mp)$.
Substituting $\lambda_+ = q$, $\lambda_- = -q^{-1}$ gives the
stated formulas.

**(ii)** The element $e_+^{(i)} = (\sigma_i + q^{-1})/(q + q^{-1})$
acts on the $q$-eigenspace as the identity and on the
$(-q^{-1})$-eigenspace as zero.  In the permutation
representation, the $q$-eigenspace is the in-order subspace
(adjacent elements not transposed) and the $(-q^{-1})$-eigenspace
is the transposed subspace.  The convex combination
$K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i$ is manifestly
stochastic (non-negative entries, rows summing to $1$).

Since $s_i$ acts by a permutation matrix, $K_i$ is symmetric, so its
columns also sum to $1$: $K_i$ is doubly stochastic, and its stationary
law is the uniform measure on $S_n$, not the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$. The Diaconis--Ram
systematic-scan Metropolis chain \cite{diaconis-ram2000}, which does
target the Mallows measure, accepts the transposition with a
probability that depends on whether it creates an inversion; it is a
different operator from $K_i$.

**(iii)** The Markov property
$\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ says that the
contribution of the rightmost generator $\sigma_n$ separates as the
scalar factor $z$, regardless of the element $x \in H_{n-1}(q)$.
This is the **memorylessness** of a Markov chain: the transition
at step $n$ depends only on the crossing type at $\sigma_n$,
not on the history of previous crossings.

**(iv)** Induction on $\ell$ when each generator occurs at most once.
Let $\sigma_m$ be the letter of highest index, so the word is
$u\,\sigma_m\,v$ with $u, v$ words in $\sigma_1, \ldots, \sigma_{m-1}$.
By cyclicity of the trace, $\mathrm{tr}_M(u\,\sigma_m\,v) =
\mathrm{tr}_M(v u\,\sigma_m)$, and $vu \in H_{m}(q)$ does not involve
$\sigma_m$, so the Markov property gives
$\mathrm{tr}_M(vu\,\sigma_m) = z\,\mathrm{tr}_M(vu)$. The word $vu$ has
$\ell - 1$ letters, each generator still at most once, so by induction
$\mathrm{tr}_M(\sigma_{i_1}\cdots\sigma_{i_\ell}) = z^{\ell}$, the base
case being $\mathrm{tr}_M(1) = 1$.
If a generator repeats, the remaining word is no longer in
$H_{m-1}(q)$ and the Markov property does not apply; the step fails
(for $\sigma_1\sigma_2\sigma_1$ one gets $h z^2 + z \neq z^3$).  $\square$

## Limiting behaviour

At $q = 1$ (classical limit), $p_+ = p_- = 1/2$ and the chain is
a fair random walk on $S_n$.  As $q \to \infty$ (deep-quantum
limit), $p_+ \to 1$ and the chain becomes deterministic: only
the symmetric channel survives, recovering the totally asymmetric
simple exclusion process (TASEP).  For the substrate value
$q = q_0$, the per-step Shannon entropy
$H = -p_+\ln p_+ - p_-\ln p_-$ is close to the maximum $\ln 2$;
the canonical evaluation is given in Chapter 7
([physical observations](#chap:observations)).
