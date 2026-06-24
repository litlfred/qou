The Iwahori--Hecke algebra $H_A(q)$ is defined over the ring
$\mathbb{Z}[q^{\pm 1}]$.  Each crossing factor
$C_{ij} = c_j \sigma_i + d_j$ has coefficients $(c_j, d_j)$
in $\mathbb{Z}[q^{\pm 1}]$:

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
   \in  \mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])
$$

has entries that are Laurent polynomials in $q$.  The
product of $k_i = A - i - 1$ such matrices at generator $\sigma_i$:

$$
  M_i(q) =  \prod_{j=i+1}^{A-1} T_j(q)
   \in  \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])
$$

has entries that are polynomials in $q^{1/2}$ of degree $\leq 2k_i$.
The traced volume:

$$
  \hat{V}_i(q) =  z(q) \cdot (M_i)_{11}(q) + (M_i)_{21}(q)
$$

is a rational function in $q^{1/2}$ (the $z$ denominator
$q^{1/2} + q^{-1/2}$ divides into the numerator for link
invariants by Jones's theorem).

The product $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$ is
a polynomial in $q^{1/2}$ because each factor is (after
cancellation with $z$), and its degree is bounded by:

$$
  \deg P_{\mathcal{N}}
   \leq 
  \sum_{i=0}^{A-2} (2k_i + 1)
  = 
  2 \cdot \frac{A(A-1)}{2} + (A-1)
  = 
  A^2 - 1.
$$

The computation requires exactly
$\sum_i k_i = \binom{A}{2}$ transfer matrix multiplications
(one per nucleon pair).  No polynomial expansion occurs — the
factored form is never unfolded.
$\qquad\blacksquare$
