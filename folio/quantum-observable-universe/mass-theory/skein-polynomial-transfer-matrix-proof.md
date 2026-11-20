*Proof.*
The Iwahori--Hecke algebra $H_A(q)$ is defined over the ring
$\mathbb{Z}[q^{\pm 1}]$.  Each crossing factor
$C_{ij} = c_j \sigma_i + d_j$ has coefficients $(c_j, d_j)$
in $\mathbb{Z}[\tfrac12][q^{\pm 1}]$ (the factor $\tfrac12$ enters only
through the mixed crossing):

| Pair type | $c_j$ | $d_j$ | Hecke element |
|-----------|-------|-------|---------------|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | $\sigma$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | $\sigma^{-1} = \sigma - (q - q^{-1})$ |
| mixed | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $\frac{1}{2}(\sigma + \sigma^{-1})$ |

The $(1, -(q - q^{-1}))$ convention for nn crossings is the unique
convention consistent with the Hecke inverse relation
$\sigma^{-1} = \sigma - (q - q^{-1})$.  This is not a normalization
choice — any other coefficients break $\sigma \cdot \sigma^{-1} = 1$
in the standard $(2,1)$ representation.  The unimodularity
$\det T = -1$ is a theorem (consequence of the Hecke relation
$\sigma^2 = (q - q^{-1})\sigma + 1$, which forces eigenvalues
$q, -q^{-1}$ with product $-1$), not an assumption.

The transfer matrix at each crossing:

$$
  T_j(q) = 
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
   \in  \mathrm{M}_2(\mathbb{Z}[\tfrac12][q^{\pm 1}])
$$

has entries that are Laurent polynomials in $q$ with exponents in
$[-1, 1]$.  The
product of $k_i = A - i - 1$ such matrices at generator $\sigma_i$:

$$
  M_i(q) =  \prod_{j=i+1}^{A-1} T_j(q)
   \in  \mathrm{M}_2(\mathbb{Z}[\tfrac12][q^{\pm 1}])
$$

has entries that are Laurent polynomials in $q$ with exponents in
$[-k_i, k_i]$.
The traced volume:

$$
  \hat{V}_i(q) =  z(q) \cdot (M_i)_{11}(q) + (M_i)_{21}(q)
$$

is, with $z = q^3/(q^2+1)$,

$$
  \hat{V}_i(q) = \frac{q^3 (M_i)_{11}(q) + (q^2+1)(M_i)_{21}(q)}{q^2+1},
$$

a quotient of a Laurent polynomial with exponents in
$[-k_i, k_i + 3]$ by $q^2 + 1$.  The denominator does not cancel in
general (for one $\mathfrak{p}$-$\mathfrak{p}$ crossing,
$\hat{V}_0 = (q^4+1)/(q^2+1)$).

The product $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$ is
therefore a rational function whose denominator divides
$(q^2+1)^{A-1}$, and the span of its numerator is bounded by:

$$
  \operatorname{span} N_{\mathcal{N}}
   \leq 
  \sum_{i=0}^{A-2} (2k_i + 3)
  = 
  2 \cdot \frac{A(A-1)}{2} + 3(A-1)
  = 
  (A-1)(A+3).
$$

The bound is attained: a symbolic check over random crossing
sequences for $A \le 5$ reaches it and never exceeds it.

The computation requires exactly
$\sum_i k_i = \binom{A}{2}$ transfer matrix multiplications
(one per nucleon pair).  No polynomial expansion occurs — the
factored form is never unfolded.  $\square$

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

| Nucleus | $A$ | $\binom{A}{2}$ steps | $\operatorname{span} N_{\mathcal{N}} \leq$ |
|---------|-----|:---:|:---:|
| ${}^{2}\mathrm{H}$ | 2 | 1 | 5 |
| ${}^{3}\mathrm{H}$ | 3 | 3 | 12 |
| ${}^{4}\mathrm{He}$ | 4 | 6 | 21 |
| ${}^{14}\mathrm{C}$ | 14 | 91 | 221 |
| ${}^{56}\mathrm{Fe}$ | 56 | 1540 | 3245 |
| ${}^{210}\mathrm{Bi}$ | 210 | 21945 | 44517 |

Under the alternative Convention-C parameter
$z = 1/(q^{1/2} + q^{-1/2})$, which cancels against the numerator and
gives a polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$ (table values
$3, 8, 15, 195, 3135, 44099$).

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
