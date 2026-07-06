The substrate parameter $q$ is the variable of the nuclear Skein
polynomial.  The transfer matrix product computes this polynomial
in factored form without expansion.

**Proposition.**
*Let $\mathcal{N}(Z, N)$ be a nucleus with $A = Z + N$ nucleons.
The Markov trace
([factorization theorem](#thm:markov-trace-factorization))*

$$
  P_{\mathcal{N}}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  = 
  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

*is a polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$.  Each
factor*

$$
  \hat{V}_i(q) =  z(q) \cdot a_i(q) + b_i(q)
$$

*is a rational function in $q^{1/2}$, where $a_i(q), b_i(q) \in \mathbb{Z}[q^{\pm 1}]$ are the transfer matrix coefficients at
generator $\sigma_i$ and $z(q) = 1/(q^{1/2} + q^{-1/2})$ is the
Markov parameter.  The product $P_{\mathcal{N}}(q)$ is the
**Skein polynomial of the nuclear link** in factored form.
It is computed by exactly $\binom{A}{2}$ transfer matrix
multiplications — one per nucleon pair.*

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
