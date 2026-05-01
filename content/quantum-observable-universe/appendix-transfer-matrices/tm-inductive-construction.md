Given a nucleus with $A$ nucleons and its transfer matrix
chains $\{M_i\}_{i=0}^{A-2}$, we describe precisely how
adding one nucleon produces the $A+1$ nucleus.  This
inductive step is the engine behind every nuclear Skein
polynomial computation.

## The inductive step: $A \to A+1$

**Given:** Nucleus $\mathcal{N}(Z, N)$ with $A = Z + N$ nucleons
in ordering $[\tau_0, \ldots, \tau_{A-1}]$ where
$\tau_k \in \{\mathfrak{p}, \mathfrak{n}\}$.  The braid has
generators $\sigma_0, \ldots, \sigma_{A-2}$ with transfer
matrix products $M_i$ and Markov-traced volumes $\hat{V}_i$.

**Add nucleon** $\tau_A$ at position $A$.

**Result:** Nucleus $\mathcal{N}'$ with $A+1$ nucleons,
generators $\sigma_0, \ldots, \sigma_{A-1}$, and updated
transfer matrix products $M_i'$.

### Rule 1: Existing generators gain one crossing

Every existing generator $\sigma_i$ ($i = 0, \ldots, A-2$)
acquires one new crossing — between nucleon $i$ and the
new nucleon $A$.  The transfer matrix product **appends**
one new factor:

$$
  M_i'(q)
  = 
  T_{\tau_i, \tau_A}(q)  \cdot  M_i(q)
$$

where $T_{\tau_i, \tau_A}$ is determined by the pair type:

| Pair $(\tau_i, \tau_A)$ | Transfer matrix |
|:-----------------------:|:---------------:|
| $(\mathfrak{p}, \mathfrak{p})$ | $T_{pp}$ |
| $(\mathfrak{n}, \mathfrak{n})$ | $T_{nn}$ |
| $(\mathfrak{p}, \mathfrak{n})$ or $(\mathfrak{n}, \mathfrak{p})$ | $T_{\mathrm{mix}}$ |

The new factor enters on the **left** (outermost position
in the braid word), since nucleon $A$ has the highest index
and the product is taken in decreasing order of $j$.

### Rule 2: One new generator is created

A new generator $\sigma_{A-1}$ appears, with a **single**
crossing between nucleon $A-1$ and nucleon $A$:

$$
  M_{A-1}'(q)
  = 
  T_{\tau_{A-1}, \tau_A}(q)
$$

This generator has chiral degree $k_{A-1} = 1$ — it sees
only one crossing and contributes a single transfer matrix
factor to the Skein polynomial.

### Rule 3: Skein polynomial update

The nuclear Skein polynomial of the $(A+1)$-nucleus factors as:

$$
  P_{\mathcal{N}'}(q)
  = 
  \underbrace{
    \prod_{i=0}^{A-2} \hat{V}_i'(q)
  }_{\text{updated existing generators}}
   \cdot 
  \underbrace{
    \hat{V}_{A-1}'(q)
  }_{\text{new generator}}
$$

where each updated volume is:

$$
  \hat{V}_i'(q)
  = 
  z \cdot (M_i')_{11} + (M_i')_{21}
$$

### Rule 4: Crossing count grows by $A$

Adding the $(A+1)$-th nucleon creates $A$ new crossings
(one with each existing nucleon).  The total crossing count
goes from $\binom{A}{2}$ to $\binom{A+1}{2} = \binom{A}{2} + A$.

| Quantity | Before ($A$ nucleons) | After ($A+1$ nucleons) | Change |
|----------|:---------------------:|:----------------------:|:------:|
| Generators | $A - 1$ | $A$ | $+1$ |
| Total crossings | $\binom{A}{2}$ | $\binom{A+1}{2}$ | $+A$ |
| Crossings at $\sigma_i$ ($i < A-1$) | $A - i - 1$ | $A - i$ | $+1$ each |
| Crossings at $\sigma_{A-1}$ | — | $1$ | new |
| Transfer matrix multiplications | $\binom{A}{2}$ | $\binom{A+1}{2}$ | $+A$ |

## The recurrence at each generator

At generator $\sigma_i$, the coefficients $(a_i, b_i)$ in
$M_i = \bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$
satisfy the **transfer matrix recurrence**.  Starting from
$(a, b) = (0, 1)$ (identity), each new crossing with nucleon
$j$ updates:

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix}
  = 
  T(c_j, d_j)
   \cdot 
  \begin{pmatrix} a \\ b \end{pmatrix}
$$

Explicitly:

$$
  a' = a  c_j (q - q^{-1}) + a  d_j + b  c_j,
  \qquad
  b' = a  c_j + b  d_j
$$

When adding nucleon $A$, this recurrence is applied **once
more** at each existing generator, appending the new factor
$T_{\tau_i, \tau_A}$ to the chain.

## Jet expansion interpretation

The transfer matrix product at generator $\sigma_i$ admits
a jet expansion in the crossing count:

| Jet order $r$ | Physical content | Multiplicity at chiral degree $k_i$ |
|:---:|---|:---:|
| $0$ | Free nucleon (identity) | $1$ |
| $1$ | Pair interactions | $k_i$ |
| $2$ | Triple correlations | $\binom{k_i}{2}$ |
| $r$ | $(r+1)$-body correlations | $\binom{k_i}{r}$ |
| $k_i$ | Full product (exact) | $1$ |

Adding nucleon $A$ **increases the chiral degree at every
existing generator by 1**: $k_i \to k_i + 1$.  Each generator
gains access to one higher jet order — one more layer of
many-body correlation.

**Beta decay as the 1-jet variation.**  Single beta decay
changes one nucleon type.  The $\mathcal{Q}_q$-value is:

$$
  \delta E =  \sum_{i=0}^{p} (\hat{V}_i^{\mathrm{dau}} - \hat{V}_i^{\mathrm{par}})
$$

summing only over generators $\sigma_i$ with $i \leq p$
(the converting nucleon's position).  Generators $\sigma_i$
with $i > p$ are unaffected and cancel exactly.

## Gröbner--Shirshov normal form (inductive proof)

The inductive construction produces a well-defined normal
form at every step:

- **Base case.** $\bar{\mathcal{N}}(1, 0) = \mathbf{1}$
  (identity in $H_1(q)$).

- **Inductive step.** Given $\bar{\mathcal{N}}(A)$ in normal
  form, Hopf-link the next nucleon:

$$
  \xi_{A+1}
  = 
  \bar{\mathcal{N}}(A)
   \cdot 
  \prod_{j=0}^{A-1}(c_j \sigma_j + d_j)
$$

  Apply the Gröbner--Shirshov division algorithm with basis
  $G = \{T^2 - (q-q^{-1})T - 1, \text{YB}, \text{far-comm}\}$:

$$
  \bar{\mathcal{N}}(A+1)
   := 
  r(\xi_{A+1}, G)
$$

  By the main theorem of Gröbner--Shirshov basis theory: the algorithm
  **terminates** (length-lex ordering is well-founded), the
  remainder is **unique** (independent of reduction path), and
  the remainder is in **normal form**.

**Key fact (verified $A \leq 6$, inductive proof for all $A$):**
The Gröbner--Shirshov reduction has **zero Yang--Baxter steps** and
**zero far-commutativity steps**.  Only Hecke reductions
($T^2 \to (q-q^{-1})T + 1$) are needed.  Therefore the
per-generator transfer matrix chain is the exact Gröbner--Shirshov
normal form — no reordering of generators occurs.

## Shell closure signatures

At doubly-magic configurations $(p, p)$, the Gröbner--Shirshov normal
form exhibits special structure:

**(i) Palindromic histogram.**  The word-length histogram
$h(\ell) = \#\{w \in \mathrm{supp}(\bar{\mathcal{N}}) : |w| = \ell\}$
is a palindrome $h(\ell) = h(L - \ell)$, matching the
**Poincar\'e polynomial of $S_{2p}$**.

| $A$ | $(p, n)$ | Histogram | Palindrome? |
|:---:|:--------:|-----------|:-----------:|
| $4$ | $(2, 2)$ | $\{1, 3, 4, 3, 1\}$ | **Yes** |
| $6$ | $(3, 3)$ | $\{1, 5, 13, 23, 31, 34, 31, 23, 13, 5, 1\}$ | **Yes** |

For $p \neq n$, the histogram is **not** palindromic.

**(ii) Dominant term jump.**  The dominant coefficient
$|c_w|$ jumps discontinuously at shell closures:

| $A$ | $(p,n)$ | Dominant $\lvert c_w\rvert$ | Ratio to $A-1$ |
|:---:|:-------:|:----------------:|:--------------:|
| $3$ | $(2,1)$ | $1.246$ | — |
| $4$ | $(2,2)$ | $1.946$ | $\times 1.56$ $\star$ |
| $5$ | $(3,2)$ | $2.424$ | $\times 1.25$ |
| $6$ | $(3,3)$ | $5.084$ | $\times 2.10$ $\star$ |

The ratio is **larger at shell closures** ($\star$) than at
non-closures.

**(iii) Shell energy gap.**  The Hecke reduction energy
$\Delta E_k$ **drops** at shell closures (the last nucleon
fits into the existing shell) and **jumps** at the next step
(a new shell must be opened):

| Step | $\to (p,n)$ | $\Delta E$ | Gap ratio |
|:----:|:-----------:|:----------:|:---------:|
| $3$ | $(2,2)$ | $0.095$ | closure |
| $4$ | $(3,2)$ | $1.409$ | $\times 14.8$ (shell break) |

## Complexity bound and magic-shell folding

The pairwise inductive step is the engine of the heavy-atom
algorithm; its cost determines whether the framework scales to
nuclei of physical interest ($A \leq 250$).

**Worst-case bound.** Without shell-folding optimizations, the
total number of $2 \times 2$ transfer-matrix multiplications to
build $\bar{\mathcal{N}}(A)$ from $\mathbf{1}$ is exactly

$$
  C_{\mathrm{bare}}(A)  =  \binom{A}{2}  =  \tfrac{1}{2} A (A-1).
$$

Each step appends one factor over $\mathbb{Z}[q^{\pm 1/2}]$ to a
$2 \times 2$ matrix product, so the algorithm is quadratic in $A$
and polynomial in the bit-size of intermediate Laurent coefficients.

**Shell-folding optimization.** At a magic configuration $A = m \in
\mathcal{M} = \{2, 8, 20, 28, 50, 82, 126\}$ (cf.
[heavy-atom examples](#tm-heavy-atom-examples) §B.7), the
shell-closure signatures (i)--(iii) above identify the closed
shell as a single Markov-equivalence class.  When the next nucleon
is added, it is sufficient to interact it with the
**collective torus-knot operator** $T_{2, 2k}$ (where $k$ is the
shell size) rather than with each of the $k$ internal nucleons
separately.  The folded step costs

$$
  C_{\mathrm{fold}}(\text{add nucleon to closed shell of size } k)
  =  O(1)
$$

matrix multiplications, replacing $k$ pairwise crossings with one
torus-knot factor.  Across an atom that closes shells at
$m_1 < m_2 < \cdots < m_r \leq A$, the savings compound: adding
the $(m_j + 1)$-th nucleon costs $1$ instead of $m_j$ steps.

**Correctness.** Folding preserves Reidemeister equivalence
because the palindromic-histogram criterion (i) certifies that the
closed shell is in the totally-antisymmetric (alternating)
Wedderburn block, and the alternating block is rank-one over the
relevant irreducible representation; the torus-knot generator
$T_{2, 2k}$ is the unique non-trivial Hecke element in that block.
The Skein polynomial of the $A+1$-nucleus computed with folding
agrees identically with the unfolded $\binom{A+1}{2}$-step product,
provided the fold is taken only at certified shell closures.

**Empirical status.**  The histogram-palindrome criterion is
verified for $A \leq 6$ ([heavy-atom examples](#tm-heavy-atom-examples)
§B.7).  For $A > 6$ the fold is taken under the
[shell-closure-stability conjecture](#prop:shell-closure-stability).
The complete folded $\mathcal{Q}_q$-value algorithm appears in
[heavy-atom examples](#tm-heavy-atom-examples) §B.7.
