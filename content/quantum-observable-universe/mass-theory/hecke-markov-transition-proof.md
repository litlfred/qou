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

This is precisely the Diaconis--Ram construction \cite{diaconis-ram2000}:
the systematic-scan Metropolis algorithm on $S_n$ targeting the
Mallows measure $\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$
has transition operator $K = K_1 K_2 \cdots K_{n-1}$, a product
of Hecke algebra elements.

**(iii)** The Markov property
$\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ says that the
contribution of the rightmost generator $\sigma_n$ separates as the
scalar factor $z$, regardless of the element $x \in H_{n-1}(q)$.
This is the **memorylessness** of a Markov chain: the transition
at step $n$ depends only on the crossing type at $\sigma_n$,
not on the history of previous crossings.

**(iv)** Follows from (iii) by induction: peeling generators
from right to left, each factor $\hat{V}_i = z a_i + b_i$ is
independent of the remaining product, giving
$\mathrm{tr}_M(\rho(\beta)) = \prod_i \hat{V}_i$.  $\square$

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
