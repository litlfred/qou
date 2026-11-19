The proof is by induction on the nucleon count $A$.

**Inductive claim.** For every $A \geq 2$, the reduction of $\Xi_A$ uses only the Hecke rule, and the result is the chain form

$$
\bar{\mathcal{N}}(A) \;=\; \prod_{i=0}^{A-2} \bigl(a_i\,\sigma_i + b_i\bigr),
$$

whose full expansion $\sum_{S} \bigl(\prod_{i \in S} a_i\bigr)\bigl(\prod_{i \notin S} b_i\bigr)\,\sigma_S$, over subsets $S \subseteq \{0, \ldots, A-2\}$ with $\sigma_S$ the product of the $\sigma_i$, $i \in S$, in increasing order, is already in normal form.

**Base case** $A = 2$. The word is the single factor $c\,\sigma_0 + d$: one linear block, no reducible subword, and the chain state is $(a_0, b_0) = (c, d)$.

**Normality of the expansion.** Every monomial $\sigma_S$ of the chain form contains each generator at most once, with indices strictly increasing left to right. Such a word contains no subword $\sigma_i^2$ (no repeated letter), no far-commutativity leading word $\sigma_j\sigma_i$ with $j \geq i+2$ (adjacent letters are strictly increasing), no Yang--Baxter leading word $\sigma_{i+1}\sigma_i\sigma_{i+1}$, and no Bokut--Shiao leading word $\sigma_i\sigma_{i-1}\cdots\sigma_j\sigma_i$ ($j \leq i - 1$, since that pattern repeats the outer letter $\sigma_i$). Hence every $\sigma_S$ is a normal word of the completed Gröbner--Shirshov basis, and distinct $S$ give distinct normal words, so the expansion is the unique normal-form expression.

**Inductive step** $A \to A+1$. Adding nucleon $\tau_A$ modifies the word in exactly two ways. At each existing block $i \leq A-2$, one new factor $c\,\sigma_i + d$ with $(c, d) = (c_{Ai}, d_{Ai})$ enters on the left of the block. Inside that block,

$$
\bigl(c\,\sigma_i + d\bigr)\bigl(a_i\,\sigma_i + b_i\bigr)
\;=\;
c\,a_i\,\sigma_i^2 + \bigl(c\,b_i + d\,a_i\bigr)\sigma_i + d\,b_i ,
$$

and the single occurrence of $\sigma_i^2$ is the only reducible subword created: the letters adjacent to the block across its boundaries carry strictly smaller (left) and strictly larger (right) generator indices, so no far-commutativity pattern arises, and a Yang--Baxter pattern would need the same letter twice separated by one position, which the block structure never produces. One application of the Hecke rule $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ gives

$$
a_i' \;=\; a_i c\,(q - q^{-1}) + a_i d + b_i c,
\qquad
b_i' \;=\; a_i c + b_i d,
$$

which is precisely the transfer-matrix recurrence $\bigl(\begin{smallmatrix} a_i' \\ b_i' \end{smallmatrix}\bigr) = T(c, d)\bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$. Second, one new block $c\,\sigma_{A-1} + d$ appears at the right end of the word, already linear, requiring no reduction. The result is again a block-ordered product of linear factors, so the inductive claim holds for $A+1$.

**Conclusion.** By induction, the reduction of $\Xi_A$ to $\bar{\mathcal{N}}(A)$ uses Hecke reductions only: one per crossing after the first at each generator (none when the running coefficient $a_i$ vanishes, as happens for purely scalar crossing types with $c = 0$), for a total of at most $\binom{A}{2} - (A-1) = \binom{A-1}{2}$ Hecke steps, and zero Yang--Baxter or far-commutativity steps. Since the rewriting system is confluent \cite{bergman1978} and the chain-form expansion consists of pairwise distinct normal words, the chain is the exact Gröbner--Shirshov normal form of the nucleus element. $\blacksquare$
