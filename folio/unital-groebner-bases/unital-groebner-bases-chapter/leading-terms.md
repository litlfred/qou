Assume that $B$ is well-ordered by $<$. Let $f \in A$, then we may write $f$
uniquely as the finite sum:

$$f = c_1 b_1 + c_2 b_2 + \cdots + c_n b_n \quad \text{for } c_i \in R^* := R \setminus \{0\},\; b_i \in B$$

such that $b_1 > b_2 > \cdots > b_n$. Then:

- The **leading monomial** of $f$: $\LM(f) := b_1$
- The **leading coefficient** of $f$: $\LC(f) := c_1$
- The **leading term** of $f$: $\LT(f) := \LC(f) \cdot \LM(f)$

We say that $\beta \in B$ **divides** $f$ (written $\beta \mid f$) if there are
$u, v \in B$ and $\lambda \in R^*$ such that
$\lambda \LT(u \cdot \beta \cdot v) = \LT(f)$.
