The algebraic machinery of the Hecke algebra $H_n(R, q)$ and the
Jones--Markov trace
([Jones--Markov trace](#thm:jones-markov-trace)) has a direct
probabilistic interpretation: **each Hecke generator $\sigma_i$ is a
stochastic transition operator**, and the product factorization
$\prod_i \hat{V}_i$
([product factorization](#thm:markov-trace-product)) is the
product of independent one-step expectations along a Markov chain.

## Statement

**Proposition.**
*Let $H_n(R, q)$ be the Iwahori--Hecke algebra with generators
$\sigma_1, \ldots, \sigma_{n-1}$ satisfying $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
([Hecke relation](#rem:hecke-algebra-from-braiding)).*

**(i) Spectral idempotents.**
*The orthogonal idempotents*

$$
  e_+^{(i)} = \frac{\sigma_i + q^{-1}}{q + q^{-1}},
  \qquad
  e_-^{(i)} = \frac{q - \sigma_i}{q + q^{-1}}
$$

*satisfy $e_+^{(i)} + e_-^{(i)} = 1$,
$(e_\pm^{(i)})^2 = e_\pm^{(i)}$,
$e_+^{(i)} e_-^{(i)} = 0$, and reconstruct the generator as
$\sigma_i = q \cdot e_+^{(i)} - q^{-1} \cdot e_-^{(i)}$.*

**(ii) Transition probabilities.**
*Define the symmetric and antisymmetric transition probabilities:*

$$
  p_+ = \frac{q}{q + q^{-1}} = \frac{q^2}{q^2 + 1},
  \qquad
  p_- = \frac{q^{-1}}{q + q^{-1}} = \frac{1}{q^2 + 1}.
$$

*Then $p_+ + p_- = 1$ and $p_+/p_- = q^2$.  The stochastic
transition operator at generator $i$ is*

$$
  K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i,
$$

*where $s_i$ is the adjacent transposition.  In the defining
representation on $\mathbb{C}[S_n]$, $K_i$ is a row-stochastic
matrix: at each crossing, the system stays in its current
configuration with probability $p_+$ or transposes the adjacent
pair with probability $p_-$.*

**(iii) Markov property as memorylessness.**
*The Markov trace property
$\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
is equivalent to the statement that the transition at generator
$n$ depends only on the eigenvalue structure of $\sigma_n$, not on the
history $x \in H_{n-1}(q)$.  The expectation value of the $i$-th
crossing under $\mathrm{tr}_M$ is:*

$$
  \mathbb{E}[\hat{V}_i]
  = \mathrm{tr}_M(a_i \sigma_i + b_i)
  = z \cdot a_i + b_i
  = \hat{V}_i,
$$

*recovering the vertex volume
([product factorization](#thm:markov-trace-product)) as the
one-step conditional expectation.*

**(iv) Independence and factorization.**
*The product formula $\mathrm{tr}_M(\rho(\beta)) = \prod_i \hat{V}_i$
is the product of independent one-step expectations: each vertex
volume $\hat{V}_i$ is determined by the local crossing data
$(a_i, b_i)$ at generator $\sigma_i$, with no dependence on the
crossings at other generators.  This is a direct consequence of
memorylessness (iii).*

## Limiting behaviour

At $q = 1$ (classical limit), $p_+ = p_- = 1/2$ and the chain is
a fair random walk on $S_n$.  As $q \to \infty$ (deep-quantum
limit), $p_+ \to 1$ and the chain becomes deterministic: only
the symmetric channel survives, recovering the totally asymmetric
simple exclusion process (TASEP).  For the substrate value
$q = q_0$, the per-step Shannon entropy
$H = -p_+\ln p_+ - p_-\ln p_-$ is close to the maximum $\ln 2$;
the numerical evaluation is given in Chapter 7
([physical observations](#chap:observations)).
