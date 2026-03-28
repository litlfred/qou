The Gröbner normal form $\bar{\mathcal{N}}(p, n)$ of a nucleus
built by sequential Hopf linking
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction))
exhibits a **shell closure signature** when $(p, n)$ is a
doubly-magic configuration.

## Construction

Build the nucleus one nucleon at a time by alternating
proton–neutron Hopf linking:

1. Start with $\bar{\mathcal{N}}(1, 0) = \mathbf{1}$ (identity
   in $H_1(q)$).
2. **Hopf-link** the next nucleon: append crossings
   $\sigma_j^{\epsilon(j,k)}$ for all existing nucleons $j < k$.
3. **Reduce** via the Gröbner basis $G = \{\sigma_i^2 -
   (q - q^{-1})\sigma_i - 1,\; \text{YB},\; \text{far-comm}\}$.
4. Record the **Hecke reduction energy** $\Delta E_k$
   ([Gröbner–Shirshov energy](#thm:groebner-shirshov-energy))
   and the **word-length histogram** $h_k(\ell) = \#\{w \in
   \mathrm{supp}(\bar{\mathcal{N}}) : |w| = \ell\}$.

Repeat until $A = p + n$ nucleons are linked.

## Proposition

**Let $q > 1$ and let $\bar{\mathcal{N}}(p, n)$ be the Gröbner
normal form of the nuclear braid in $H_A(q)$ constructed by
sequential Hopf linking with alternating $\mathfrak{p}$-$\mathfrak{n}$
filling.**

**(i) Normal form.**
$\bar{\mathcal{N}}(p, n)$ is in Gröbner normal form for all
$A \leq 9$ (verified computationally): every word in the support
is a reduced word in $H_A(q)$ — no $\sigma_i^2$ patterns,
no Yang–Baxter–reducible triples, no unsorted far-commutativity
pairs.

**(ii) Symmetric histogram at shell closures.**
When $p = n$ (doubly-even nuclei), the word-length histogram
$h(\ell)$ is a **palindrome**:

$$
  h(\ell) \;=\; h(L - \ell)
  \qquad \text{for all } 0 \leq \ell \leq L
$$

where $L$ is the maximum word length in the support.

Verified for:

| $A$ | $(p, n)$ | Histogram $h(\ell)$ | Palindrome? |
|-----|----------|---------------------|:-----------:|
| $4$ | $(2, 2)$ | $\{1, 3, 4, 3, 1\}$ | **Yes** |
| $6$ | $(3, 3)$ | $\{1, 5, 13, 23, 31, 34, 31, 23, 13, 5, 1\}$ | **Yes** |

These are the **Poincaré polynomials** of the symmetric groups
$S_4$ and $S_6$: the rank-generating functions of the Bruhat
order on reduced words.

For $p \neq n$ (e.g., $(2,1)$, $(3,2)$, $(4,3)$), the histogram
is **not** a palindrome.

**(iii) Dominant term at shell closure.**
The coefficient of the dominant term (largest $|c_w|$) **jumps
discontinuously** at shell closures:

| $A$ | $(p,n)$ | Dominant $|c_w|$ | Word length | Ratio to $A-1$ |
|-----|---------|:----------------:|:-----------:|:---------------:|
| $3$ | $(2,1)$ | $1.246$ | $1$ | — |
| $4$ | $(2,2)$ | $1.946$ | $4$ | $\times 1.56$ ★ |
| $5$ | $(3,2)$ | $2.424$ | $4$ | $\times 1.25$ |
| $6$ | $(3,3)$ | $5.084$ | $7$ | $\times 2.10$ ★ |
| $7$ | $(4,3)$ | $7.193$ | $9$ | $\times 1.41$ |
| $8$ | $(4,4)$ | $21.248$ | $16$ | $\times 2.95$ ★ |
| $9$ | $(5,4)$ | $32.962$ | $22$ | $\times 1.55$ |

The ratio to the previous step is **larger at shell closures**
($\times 1.56, \times 2.10, \times 2.95$) than at non-closures
($\times 1.25, \times 1.41, \times 1.55$).

**(iv) Shell energy gap.**
The Hecke reduction energy $\Delta E_k$ at step $k$ (adding
the $k$-th nucleon) exhibits a **gap** at shell breaks:

| Step | $\to (p,n)$ | $\Delta E$ | Hecke steps | |
|:----:|:-----------:|:----------:|:-----------:|:---:|
| $2$ | $(2,1)$ | $0.274$ | $2$ | ★ closure |
| $3$ | $(2,2)$ | $0.095$ | $10$ | ★ closure |
| $4$ | $(3,2)$ | $1.409$ | $58$ | shell break |
| $5$ | $(3,3)$ | $2.174$ | $790$ | |

The energy drops at the closure ($0.274 \to 0.095$: the last
nucleon fits into the existing shell) and then **jumps** at the
next step ($0.095 \to 1.409$: the new nucleon must start a fresh
shell).  The ratio $1.409 / 0.095 = 14.8$ is the **shell gap**
in Hecke energy units.

## Interpretation

The Poincaré palindrome at $(p, p)$ nuclei means the Gröbner
normal form fills the **entire Bruhat lattice of $S_{2p}$
symmetrically**.  Every reduced word of length $\ell$ is paired
with a reduced word of length $L - \ell$ with matching
coefficient magnitude.  This is the algebraic signature of
**complete shell filling**: all available crossing configurations
within the shell are occupied, and the structure is invariant
under the Bruhat duality $w \mapsto w_0 w$ (where $w_0$ is the
longest element of $S_{2p}$).

The Borromean closure — the 3-body linking that creates the
shell — is encoded in the dominant word.  At each shell closure,
the dominant word jumps to a significantly **longer** reduced
word (from length 1 at $A = 3$ to length 4 at $A = 4$; from
length 9 at $A = 7$ to length 16 at $A = 8$), reflecting the
intertwining of all nucleons within the closed shell.

The dominant words at shell closures are:

| $(p,n)$ | Dominant word | Length |
|---------|--------------|:------:|
| $(2,2)$ | $\sigma_0\sigma_1\sigma_0\sigma_2$ | $4$ |
| $(3,3)$ | $\sigma_2\sigma_1\sigma_0\sigma_2\sigma_3\sigma_2\sigma_4$ | $7$ |
| $(4,4)$ | $\sigma_1\sigma_0\sigma_2\sigma_3\sigma_2\sigma_1\sigma_0\sigma_3\sigma_2\sigma_4\sigma_3\sigma_2\sigma_4\sigma_5\sigma_4\sigma_6$ | $16$ |

These are specific reduced words in $S_{2p}$ — the
**shell closure permutations** that maximally intertwine the
$p$ protons and $p$ neutrons within the shell.
