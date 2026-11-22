The substrate parameter $q$ acts as the variable of the nuclear Skein polynomial. The transfer matrix product computes this polynomial in factored form without expansion.

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

*is a rational function of $q$ whose denominator divides
$(q^2+1)^{A-1}$, and whose numerator is a Laurent polynomial in $q$ of
span (highest minus lowest exponent) $\leq (A-1)(A+3)$.  Each
factor*

$$
  \hat{V}_i(q) =  z(q) \cdot a_i(q) + b_i(q)
$$

*is a rational function in $q$, where $a_i(q), b_i(q) \in \mathbb{Z}[\tfrac12][q^{\pm 1}]$ are the transfer matrix coefficients at
generator $\sigma_i$ and $z(q) = q^3/(q^2+1)$ is the canonical
Markov parameter.  The product $P_{\mathcal{N}}(q)$ is the **Skein polynomial of the nuclear link** in factored form.
It is computed by exactly $\binom{A}{2}$ transfer matrix
multiplications — one per nucleon pair.*

Under the alternative Convention-C parameter $z_C = 1/(q^{1/2} + q^{-1/2})$, each factor is a Laurent polynomial in $q^{1/2}$ and $P_{\mathcal{N}}$ is a polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$. At the canonical parameter the $z$ denominator does not cancel in general: for a single $\mathfrak{p}$-$\mathfrak{p}$ crossing, $\hat{V}_0 = zh + 1 = (q^4+1)/(q^2+1)$.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
