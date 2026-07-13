## Construction

Build the nucleus one nucleon at a time by alternating
proton–neutron Hopf linking:

1. Start with $\mathcal{N}(1, 0) = \mathbf{1}$ (identity
 in $H_1(q)$).
2. **Hopf-link** the next nucleon: append crossings
 $\sigma_j^{\epsilon(j,k)}$ for all existing nucleons $j < k$.
3. **Reduce** via the Gröbner--Shirshov basis $G = \{\sigma_i^2 - (q - q^{-1})\sigma_i - 1, \text{YB}, \text{far-comm}\}$.
4. Record the **Hecke reduction energy** $\Delta E_k$
 ([Gröbner–Shirshov energy](#thm:groebner-shirshov-energy))
 and the **word-length histogram** $h_k(\ell) = \#\{w \in
   \mathrm{supp}(\mathcal{N}) : |w| = \ell\}$.

Repeat until $A = p + n$ nucleons are linked.

## Proposition

**Let $q > 1$ and let $\mathcal{N}(p, n)$ be the Gröbner--Shirshov
normal form of the nuclear braid in $H_A(q)$ constructed by
sequential Hopf linking with alternating $\mathfrak{p}$-$\mathfrak{n}$
filling.**

**(i) Normal form (inductive, for all $A$).**
$\mathcal{N}(p, n)$ is in Gröbner--Shirshov normal form for **every**
$A \geq 1$, by induction on $A$:

- **Base case.** $\mathcal{N}(1, 0) = \mathbf{1}$ is by definition
 in normal form (the empty word has no squares, no YB triples, no
 far-comm pairs).

- **Inductive step.** Given $\mathcal{N}$ at step $A$ in normal
 form in $H_A(q)$, the Hopf-link step produces:

 $$
    \xi_{A+1}
    = 
    \mathcal{N}(A)
     \cdot 
    \prod_{j=0}^{A-1}(c_j \sigma_j + d_j)
  $$

 where each factor $(c_j \sigma_j + d_j)$ is the crossing element
 for the new nucleon with nucleon $j$ (already in normal form:
 linear in $\sigma_j$, no squares). The product $\xi_{A+1}$ may
 contain $\sigma_j^2$ terms from multiplying $\sigma_j$ factors.
 Apply the Gröbner--Shirshov division algorithm
 ([division algorithm](#unital-groebner-bases:def:division-algorithm))
 with the Hecke basis $G$:

 $$
    \mathcal{N}(A+1)
     := 
    r(\xi_{A+1}, G)
  $$

 By the **main theorem** of Gröbner--Shirshov basis theory
 ([main theorem](#unital-groebner-bases:thm:ugb-main-theorem)):

 1. The algorithm **terminates** (the length-lex ordering on positive
 braid monomials is well-founded).
 2. The remainder $r(\xi_{A+1}, G)$ is **unique** (independent of
 reduction path).
 3. The remainder is in **normal form** (no word in its support
 contains a leading monomial of any $g \in G$).

 Therefore $\mathcal{N}(A+1)$ is in normal form. $\square$

The normal form has at most $A!$ terms (the dimension of $H_A(q)$
over $\mathbb{Z}[q^{± 1}]$, equal to $|S_A|$). This is a
**finite** representation for any nucleus.

**(ii) Symmetric histogram at shell closures.**
When $p = n$ (doubly-even nuclei), the word-length histogram
$h(\ell)$ is a **palindrome**:

$$
  h(\ell) =  h(L - \ell)
  \qquad \text{for all } 0 \leq \ell \leq L
$$

where $L$ is the maximum word length in the support.

Verified for:

See [Table 1](#tbl:shell-closure-normal-form-table1-data).

These are the **Poincaré polynomials** of the symmetric groups
$S_4$ and $S_6$: the rank-generating functions of the Bruhat
order on reduced words.

For $p \neq n$ (e.g., $(2,1)$, $(3,2)$, $(4,3)$), the histogram
is **not** a palindrome.

**(iii) Dominant term at shell closure.**
The coefficient of the dominant term (largest $|c_w|$) **jumps
discontinuously** at shell closures:

See [Table 2](#tbl:shell-closure-normal-form-table2-data).

The ratio to the previous step is **larger at shell closures**
($\times 1.56, \times 2.10, \times 2.95$) than at non-closures
($\times 1.25, \times 1.41, \times 1.55$).

**(iv) Shell energy gap.**
The Hecke reduction energy $\Delta E_k$ at step $k$ (adding
the $k$-th nucleon) exhibits a **gap** at shell breaks:

See [Table 3](#tbl:shell-closure-normal-form-table3-data).

The energy drops at the closure ($0.274 \to 0.095$: the last
nucleon fits into the existing shell) and then **jumps** at the
next step ($0.095 \to 1.409$: the new nucleon must start a fresh
shell). The ratio $1.409 / 0.095 = 14.8$ is the **shell gap**
in Hecke energy units.

The optimal $A$-term refinement of this raw normal form — obtained
by quotienting by the adjacency / chain-collapse ideals
([quotient ideals $I_8$, $I_9$](#def:gs-quotient-ideals-I8-I9)) — is
stated separately
([optimal normal form](#thm:optimal-normal-form-valley)).
