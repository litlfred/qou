*Let $R$ be a commutative ring in which $q$ and $[2]_q = q + q^{-1}$ are invertible, and let $\sigma_1, \sigma_3, \sigma_5$ be three pairwise-commuting elements of a commutative $R$-algebra, each satisfying the Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$. Write $e^{s}(\sigma) = (\sigma + q^{-1})/[2]_q$ (the symmetric idempotent, eigenvalue $q$) and $e^{a}(\sigma) = (q - \sigma)/[2]_q$ (the antisymmetric idempotent, eigenvalue $-q^{-1}$), and for $\epsilon_1, \epsilon_2, \epsilon_3 \in \{s, a\}$ set*

$$
  E(\epsilon_1, \epsilon_2, \epsilon_3) \;:=\; e^{\epsilon_1}(\sigma_1)\, e^{\epsilon_2}(\sigma_3)\, e^{\epsilon_3}(\sigma_5).
$$

*Then:*

1. *(Disjoint strand pairs.) The strand pairs $\{1,2\}, \{3,4\}, \{5,6\}$ on which $\sigma_1, \sigma_3, \sigma_5$ act are pairwise disjoint and their union is $\{1, \dots, 6\}$.*
2. *(Pure-pattern idempotents.) The eight elements $E(\epsilon_1, \epsilon_2, \epsilon_3)$ are idempotent and pairwise orthogonal, and their sum is $1$.*
3. *(Six-pattern decomposition.) The six patterns other than $(s,s,s)$ and $(a,a,a)$ satisfy*
   $$
     \sum_{(\epsilon_1, \epsilon_2, \epsilon_3) \neq (s,s,s),\,(a,a,a)} E(\epsilon_1, \epsilon_2, \epsilon_3) \;=\; 1 - E(s,s,s) - E(a,a,a).
   $$
4. *(Closure invariants of the carrier powers.) For $k = 2, 3, 4$, the word $\sigma^{2k}$ in the braid group $B_2$ of a single strand pair induces the identity permutation of the strand endpoints, so its closure has two components, and its writhe is $2k$.*

### Computed tableau multiplicities

Enumerating the $76$ standard Young tableaux of size $6$ and classifying each of $\sigma_1, \sigma_3, \sigma_5$ on the Hoefsmit seminormal basis vector as sym, alt or mixed gives exactly $20$ tableaux on which all three act diagonally. Their sym/alt patterns occur with multiplicities

| $(s,s,s)$ | $(a,s,s)$ | $(s,a,s)$ | $(s,s,a)$ | $(a,a,s)$ | $(a,s,a)$ | $(s,a,a)$ | $(a,a,a)$ |
|---|---|---|---|---|---|---|---|
| $4$ | $2$ | $1$ | $3$ | $3$ | $1$ | $2$ | $4$ |

These counts are computed (by enumerating standard tableaux and eigenvalue classes); they are not derived in closed form.

The naming of the six patterns and of the carrier powers $\sigma_1^4, \sigma_3^6, \sigma_5^8$ as the electroweak carriers $W, Z, H$, together with the minimality of $n = 6$, the interface-knot refinement, the dimension-collapse resolution, the Plancherel-weight special case and the $N_v$ implication, is collected in
[the Hoefsmit cell-content context](#rem:hoefsmit-ew-cell-content-context).
