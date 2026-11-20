*Let $\mathcal{N}(Z, N)$ be a nucleus with $A \geq 2$ nucleons, with each crossing between nucleons of types $\tau_i$ and $\tau_j$ at generator $\sigma_i$ the linear element $c\,\sigma_i + d \in H_A(q)$, and let*

$$
\Xi_A \;=\; \prod_{i=0}^{A-2} \; \prod_{j=A-1}^{i+1} \bigl(c_{ji}\,\sigma_i + d_{ji}\bigr)
$$

*be the block-ordered nucleus element (blocks ordered by increasing generator index; the inner product taken in decreasing $j$, matching the transfer-matrix order). Then the Gröbner--Shirshov reduction of $\Xi_A$:*

1. *uses only the Hecke rule $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ — zero Yang--Baxter and zero far-commutativity steps, with at most $\binom{A-1}{2}$ Hecke steps in total;*
2. *terminates in the chain form*
   $$
   \bar{\mathcal{N}}(A) \;=\; \prod_{i=0}^{A-2} \bigl(a_i\,\sigma_i + b_i\bigr),
   $$
   *whose coefficients $(a_i, b_i)$ are produced by the transfer-matrix recurrence $\bigl(\begin{smallmatrix} a_i' \\ b_i' \end{smallmatrix}\bigr) = T(c, d)\bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$;*
3. *and the full expansion $\sum_{S} \bigl(\prod_{i \in S} a_i\bigr)\bigl(\prod_{i \notin S} b_i\bigr)\,\sigma_S$, over subsets $S \subseteq \{0, \ldots, A-2\}$ with $\sigma_S$ the product of the $\sigma_i$, $i \in S$, in increasing order, is the exact Gröbner--Shirshov normal form of $\Xi_A$.*

Here the Gröbner--Shirshov rewriting system for $H_A(q)$ has three families of rules — the Hecke rule, far-commutativity $\sigma_j\sigma_i \to \sigma_i\sigma_j$ for $j \geq i + 2$, and the Bokut--Shiao family $\sigma_j\sigma_{j-1}\cdots\sigma_k\sigma_j \to \sigma_{j-1}\sigma_j\sigma_{j-1}\cdots\sigma_k$ for $k \leq j - 1$, whose case $k = j - 1$ is Yang--Baxter $\sigma_j\sigma_i\sigma_j \to \sigma_i\sigma_j\sigma_i$ with $j = i + 1$. With Yang--Baxter in place of the whole Bokut--Shiao family the system is not confluent once $A \geq 4$. The completed system is a Gröbner--Shirshov basis and is confluent by the Diamond Lemma \cite{bergman1978}, so the normal form is unique and independent of the reduction order ([Hecke normal form](#def:hecke-normal-form)).
