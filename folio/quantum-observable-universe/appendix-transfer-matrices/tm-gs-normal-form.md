*Let $\mathcal{N}(Z, N)$ be a nucleus with $A \geq 2$ nucleons, with each crossing between nucleons of types $\tau_i$ and $\tau_j$ at generator $\sigma_i$ the linear element $c\,\sigma_i + d \in H_A(q)$, and let*

$$
\Xi_A \;=\; \prod_{i=0}^{A-2} \; \prod_{j=A-1}^{i+1} \bigl(c_{ji}\,\sigma_i + d_{ji}\bigr)
$$

*be the block-ordered nucleus element (blocks ordered by increasing generator index; the inner product taken in decreasing $j$, matching the transfer-matrix order). Then the Gröbner--Shirshov reduction of $\Xi_A$:*

1. *uses only the Hecke rule $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ — zero Yang--Baxter, zero Bokut--Shiao, and zero far-commutativity steps, with at most $\binom{A-1}{2}$ Hecke steps in total;*
2. *terminates in the chain form*
   $$
   \bar{\mathcal{N}}(A) \;=\; \prod_{i=0}^{A-2} \bigl(a_i\,\sigma_i + b_i\bigr),
   $$
   *whose coefficients $(a_i, b_i)$ are produced by the transfer-matrix recurrence $\bigl(\begin{smallmatrix} a_i' \\ b_i' \end{smallmatrix}\bigr) = T(c, d)\bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$;*
3. *and the full expansion $\sum_{S} \bigl(\prod_{i \in S} a_i\bigr)\bigl(\prod_{i \notin S} b_i\bigr)\,\sigma_S$, over subsets $S \subseteq \{0, \ldots, A-2\}$ with $\sigma_S$ the product of the $\sigma_i$, $i \in S$, in increasing order, is the exact Gröbner--Shirshov normal form of $\Xi_A$.*

For general words in $H_A(q)$ ($A \geq 4$), confluence requires completing the three defining rule families — the Hecke rule, far-commutativity $\sigma_i\sigma_j \to \sigma_j\sigma_i$ ($i \geq j + 2$), and Yang--Baxter $\sigma_{i+1}\sigma_i\sigma_{i+1} \to \sigma_i\sigma_{i+1}\sigma_i$ — with the $q$-free Bokut--Shiao braid family $\sigma_i\sigma_{i-1}\cdots\sigma_j\sigma_i \to \sigma_{i-1}\sigma_i\sigma_{i-1}\cdots\sigma_j$ ($j \leq i - 1$, which subsumes Yang--Baxter at $j = i - 1$; [Hecke normal form](#def:hecke-normal-form)), after which the completed rewriting system is confluent by the Diamond Lemma \cite{bergman1978}. On the block-ordered nuclear word $\Xi_A$, intra-block Hecke reduction produces strictly increasing generator chains $\sigma_S$ in which no generator index appears more than once; every such chain is already irreducible under the entire Bokut--Shiao completed basis with zero braid or far-commutativity steps.
