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

**The triple identity of $q$.**

The parameter $q$ plays three roles simultaneously:

| Role | Description |
|------|-------------|
| Algebraic | Deformation parameter of $H_A(q)$: $T^2 = (q - q^{-1})T + 1$ |
| Topological | Variable of the Skein polynomial $P_{\mathcal{N}}(q)$ |
| Physical | Substrate parameter $q$ from $\chi(A) = -6$ |

These are not three different objects — they are the **same $q$**.
The Hecke relation generates the polynomial; the Markov trace
makes it a link invariant; evaluating at $q$ projects the
topological invariant to the physical energy.

**Degree bounds for specific nuclei.**

| Nucleus | $A$ | $\binom{A}{2}$ steps | $\deg P_{\mathcal{N}} \leq$ |
|---------|-----|:---:|:---:|
| ${}^{2}\mathrm{H}$ | 2 | 1 | 3 |
| ${}^{3}\mathrm{H}$ | 3 | 3 | 8 |
| ${}^{4}\mathrm{He}$ | 4 | 6 | 15 |
| ${}^{14}\mathrm{C}$ | 14 | 91 | 195 |
| ${}^{56}\mathrm{Fe}$ | 56 | 1540 | 3135 |
| ${}^{210}\mathrm{Bi}$ | 210 | 21945 | 44099 |

All evaluated in milliseconds.

**Consequence for beta decay.**

The $Q$-value
([transition energy](#def:Q-value-transition)) is the ratio
of two Skein polynomials evaluated at the substrate parameter $q$:

$$
  Q
  = 
  P_{\mathcal{N}_{\mathrm{par}}}(q)
  - 
  P_{\mathcal{N}_{\mathrm{dau}}}(q)
  - 
  P_{e}(q)
$$

(in action units).  Since the parent and daughter polynomials
differ only at generators $\sigma_0, \ldots, \sigma_p$ (the
1-jet support of the beta decay
([jet expansion](#prop:generator-volume-decomposition))), the
difference is a polynomial of lower degree — concentrated in
the converting nucleon's generators.

**Consequence for double beta decay.**

The 2-jet cross-term $\Delta_{p_1 p_2}$
([generator volume decomposition](#prop:generator-volume-decomposition))
corresponds to the **interference** between two Skein
polynomial modifications.  In the polynomial language:

$$
  P_{\mathcal{N}}^{(2\beta)}(q)
  - 
  P_{\mathcal{N}}^{(\mathrm{par})}(q)
   \neq 
  \bigl[P_{\mathcal{N}}^{(\beta_1)}(q) - P_{\mathcal{N}}^{(\mathrm{par})}(q)\bigr]
  + 
  \bigl[P_{\mathcal{N}}^{(\beta_2)}(q) - P_{\mathcal{N}}^{(\mathrm{par})}(q)\bigr]
$$

The difference is the 2-jet cross-term: a polynomial in $q$
encoding the nuclear matrix element of double beta decay.
