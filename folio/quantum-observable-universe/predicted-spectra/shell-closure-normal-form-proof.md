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

## Raw normal form (part (i))

$\mathcal{N}(p, n)$ is in Gröbner--Shirshov normal form for **every**
$A \geq 1$, by induction on $A$:

- **Base case.** $\mathcal{N}(1, 0) = \mathbf{1}$ is by definition
 in normal form (the empty word has no squares, no YB triples, no
 far-comm pairs).

- **Inductive step.** Given $\mathcal{N}$ at step $A$ in normal
 form in $H_A(q)$, the Hopf-link step produces

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
    r(\xi_{A+1}, G).
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
over $\mathbb{Z}[q^{\pm 1}]$, equal to $|S_A|$), a finite
representation for any nucleus.

## Optimal normal form

**Proof sketch.**
The proof is by induction on $A$. Adding strand $A$ creates cross-terms $\sigma_i \cdot \sigma_{A-1}$ for all $i < A - 1$. Absorb these terms as follows:

- If $|i - (A-1)| \geq 2$: Far-commutativity gives $\sigma_{A-1} \cdot \sigma_i$. Then I$_{9}$ absorbs this term since the prefix $\sigma_i$ is present.
- If $|i - (A-1)| = 1$: This forms an adjacency pair. I$_{8}$ absorbs this term since the prefix $\sigma_{A-1}$ is present.
- If $i = A - 1$: The Hecke relation yields $\sigma_{A-1}^2 = (q - q^{-1})\sigma_{A-1} + \mathbf{1}$. Both terms are already in the basis.

The identity term $\mathbf{1}$ survives because $d \neq 0$ for nn and pn crossings. The condition $N \geq Z - 1$ ensures at least one nn or pn crossing exists at every generator. $\square$

This is verified computationally for all $A \leq 8$ (reducing 14,256 terms to 8 for ${}^8\mathrm{Be}$).

**Valley of stability boundary.**
The optimality fails for $N < Z - 1$ (proton-heavy nuclei). When all crossings are pp type ($d = 0$), the identity term vanishes. Multiplying by $(c \cdot \sigma_k + 0)$ does not preserve the identity. Without $\mathbf{1}$ in the support, I$_{9}$ chain-stripping lacks a root.

See [Table 4](#tbl:shell-closure-normal-form-table4-data).

The boundary $N \geq Z - 1$ matches the nuclear valley of stability.
