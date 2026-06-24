*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Markov trace of the nuclear braid word factors exactly as
a product of **Markov-traced generator volumes** — one per braid
generator $\sigma_i$.  This factorization is an exact algebraic
identity in $H_A(q)$, and the result is a **polynomial in $q$**:
the Skein polynomial of the nuclear link.

**Theorem.**
Let $\mathcal{N}(Z, N)$ be the Gröbner--Shirshov-reduced
nuclear braid word in $H_A(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).
At each generator $\sigma_i$, let $(a_i, b_i)$ be the
transfer-matrix-reduced chain coefficients
([generator volume decomposition](#prop:generator-volume-decomposition)).
Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov trace parameter.
Then the Markov trace factors exactly:

$$
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  = 
  \prod_{i=0}^{A-2}
  \bigl(z \cdot a_i + b_i\bigr).
$$

Each $\hat{V}_i = z \cdot a_i + b_i$ is a **polynomial in
$q$** (since $a_i, b_i$ are polynomials in $q$ from the
transfer matrix product, and $z$ is rational in $q^{1/2}$).
The full trace is therefore a **product of polynomials** — the
factored form of the nuclear Skein polynomial.

## The transfer matrix IS the polynomial

At each crossing between nucleons $i$ and $j$, the transfer
matrix

$$
  T_j = 
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
$$

has entries that are polynomials in $q$.  The crossing types
determine the coefficients:

| Pair type | $c_j$ | $d_j$ | $\det(T_j)$ |
|-----------|-------|-------|:-----------:|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | $-1$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | $-1$ |
| mixed | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $-1 + \frac{1}{4}(q - q^{-1})^2$ |

The product of $k_i$ transfer matrices at generator $\sigma_i$
gives $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are
polynomials in $q$ of degree $\leq 2k_i$.  Then:

$$
  \hat{V}_i(q) =  z \cdot (M_i)_{11} + (M_i)_{21}
$$

is a polynomial in $q^{1/2}$.  The nuclear Skein polynomial is:

$$
  P_{\mathcal{N}}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

**This product IS the Skein polynomial of the nuclear link
$\mathcal{N}(Z, N)$**, written in factored form.  Evaluating at
the substrate $q$ gives the physical categorical action.

## $q$ as the polynomial variable

The substrate parameter $q$ is simultaneously:

1. **The deformation parameter** of the Iwahori--Hecke algebra $H_A(q)$,
   controlling the deviation from the symmetric group.
2. **The variable** of the Skein polynomial, in which each
   transfer matrix entry is polynomial.
3. **The physical parameter** the substrate $q$, determined by the
   Descartes condition $\chi(A) = -6$.

The entire nuclear physics is encoded in the polynomial
$P_{\mathcal{N}}(q)$.  Computing the polynomial requires
exactly $\binom{A}{2}$ transfer matrix multiplications.
Evaluating the polynomial at the substrate parameter $q$ gives the energy.
Taking the ratio $P_{\mathrm{par}}(q) / P_{\mathrm{dau}}(q)$
gives the matrix element for beta decay.

## Consequence: the chain of invariant-preserving maps

$$
  \mathbb{Z}[B_A]
  \xrightarrow{\text{Hecke quotient}}
  H_A(q)
  \xrightarrow{\text{transfer matrices}}
  \prod_{i} (a_i(q) \sigma_i + b_i(q))
  \xrightarrow{\text{Markov trace}}
  \prod_{i} \hat{V}_i(q)
  = 
  P_{\mathcal{N}}(q)
$$

Each step preserves the link invariant.  The polynomial
$P_{\mathcal{N}}(q)$ is a well-defined invariant of the nuclear
link $\mathcal{N}(Z, N)$ — it does not depend on the braid
representative or the reduction path.  Evaluating at
the substrate $q$ projects the polynomial invariant to the physical
energy.

## The polynomial degree

The degree of $P_{\mathcal{N}}(q)$ as a polynomial in $q^{1/2}$
is bounded by:

$$
  \deg P_{\mathcal{N}}  \leq 
  \sum_{i=0}^{A-2} (2k_i + 1)
  = 
  A(A-1) + (A-1)
  = 
  (A-1)(A+1)
  = 
  A^2 - 1
$$

For ${}^{14}\mathrm{C}$: $\deg \leq 195$.  For
${}^{210}\mathrm{Bi}$: $\deg \leq 44{,}099$.  The transfer
matrix product evaluates this polynomial at the substrate parameter $q$
without ever expanding it.

## Asymptotic behaviour

For heavy nuclei ($A \gg 1$), the ratio of $L_0^{-}$ and parent
traces converges:

$$
  \frac{\mathrm{tr}(L_0^{-})}{\mathrm{tr}(\mathcal{N})}
   \longrightarrow 
  \frac{1}{\hbar_q}
  = 
  \frac{1}{1 - q^{-1}}
   \approx  10.09
  \quad\text{as } A \to \infty.
$$

The sub-leading correction is $O(1/A)$ and carries the
nucleus-specific information (shell structure, pairing).
