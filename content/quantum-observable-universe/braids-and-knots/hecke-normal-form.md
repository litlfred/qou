The **Hecke normal form** of an element $h \in H_n(R, q)$ is a representative obtained by iterated application of three rewriting rules, each oriented so that the shortlex-larger word reduces to the shortlex-smaller one:

1. Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
2. Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $i > j + 1$.
3. Yang--Baxter: $\sigma_{i+1} \sigma_i \sigma_{i+1} \to \sigma_i \sigma_{i+1} \sigma_i$.

These three rules **do not form a Gröbner--Shirshov basis**, and the reduction they generate is therefore not confluent: the normal form they produce depends on the order in which rules are applied. The obstruction appears first at $n = 4$, where the overlap of rule 3 for $(\sigma_2, \sigma_3)$ with rule 2 for $(\sigma_3, \sigma_1)$ over the word $\sigma_3\sigma_2\sigma_3\sigma_1$ has $S$-polynomial $\sigma_2\sigma_3\sigma_2\sigma_1 - \sigma_3\sigma_2\sigma_1\sigma_3$, in which both words are already irreducible.

Confluence is recovered by **completing** the system with the Bokut--Shiao family

$$
\sigma_i \sigma_{i-1} \cdots \sigma_j \sigma_i \;\to\; \sigma_{i-1} \sigma_i \sigma_{i-1} \cdots \sigma_j
\qquad (j \leq i - 1),
$$

which subsumes rule 3 at $j = i - 1$ and which carries no $q$: it is a braid-group identity, obtained by commuting $\sigma_i$ past $\sigma_{i-2} \cdots \sigma_j$ and then applying the braid relation, with the quadratic relation never used. The refuting $S$-polynomial above is, up to sign, exactly this rule at $(i, j) = (3, 1)$; for the completed system it is therefore no longer a normal form, and the $n = 4$ obstruction is gone.

The completed system **is** a Gröbner--Shirshov basis for every $n \geq 1$ and every admissible $q$-datum, and its normal forms are consequently unique. Standard monomials for the completed system index a basis of $H_n(R, q)$, which is free of rank $n!$ over $R$, in bijection with the symmetric group $S_n$. Computationally, the reduction may be evaluated by directed Kashiwara crystal traversal rather than by $S$-polynomial overlap analysis.
