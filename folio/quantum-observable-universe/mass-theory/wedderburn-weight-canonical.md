*The Bethe-Weizsäcker mass coefficient and the LP shadow-price scale the identical canonical $q$-deformed Wedderburn-block weight:*

$$
  \tilde w_\lambda(q)
  \;:=\;
  \frac{\dim_q(\lambda)^2}{[n]_q!}.
$$

*The quantum hook-length dimension $\dim_q(\lambda)$ is defined by the $q$-deformed Frame-Robinson-Thrall formula. This identity holds for all $\lambda$. No relation between the Markov coefficient $y_\lambda$ and $\tilde w_\lambda$ is asserted: the former "Wenzl-bridge reduction" $y_\lambda = \tilde w_\lambda(q)$ on the self-conjugate stratum is false there and was dropped (see below).*

This establishes the central canonicity of the weight $\tilde w_\lambda(q)$. The LP form multiplies this weight by $h/2$. The Markov coefficient $y_\lambda$, given by Wenzl's hook-content closed form, is a distinct family on every stratum.

> **Failure of the Wenzl-bridge premise on the $\kappa_\lambda = 0$ stratum.** The identity $y_\lambda = \tilde w_\lambda$ for $\kappa_\lambda = \sum_x c(x) = 0$ fails at **every** such partition with $n \leq 6$ except the trivial one-cell $\lambda = (1)$ — in the production convention D *and* in the excised convention C, so it is not a convention-scoping issue:
>
> | $\lambda$ | $\kappa$ | $y^{\mathrm D}(q_0)$ | $y^{\mathrm C}(q_0)$ | $\tilde w(q_0)$ |
> |---|---:|---:|---:|---:|
> | $(1)$ | 0 | 1.00000000 | 1.00000000 | 1.00000000 |
> | $(2,1)$ | 0 | 0.24729789 | 0.28092963 | 0.66067377 |
> | $(2,2)$ | 0 | 0.06115624 | 0.06947330 | 0.16604895 |
> | $(3,1,1)$ | 0 | **0** | 0.01676661 | 0.29466896 |
> | $(3,2,1)$ | 0 | **0** | 0.00731845 | 0.35863564 |
>
> $(2,2)$ and $(3,2,1)$ are precisely the two partitions this block's cited script is said to have verified.
>
> **The last two rows are a scope-(b) structural exclusion**, not a numerical near-miss. Convention D is the $\mathfrak{sl}_2$ point of the Ocneanu family ([markov-z-reconciliation remark](../mass-endomorphism/markov-z-reconciliation.md)), so $y_\lambda = 0$ identically once $\lambda$ has more than two rows — such a $\lambda$ has a cell of content $-2$, whose Ocneanu numerator factor vanishes. Meanwhile $\tilde w_\lambda$ is a ratio of products of positive quantum integers, hence strictly positive for $q > 0$. The identity there asserts $0 = \text{positive}$, and no choice of parameter reconciles it. The other two rows are scope (a): measured non-equality under six readings of $\dim_q(\lambda)^2/[n]_q!$ (symmetric vs unbalanced quantum integer, $q$-deformed vs ordinary dimension, squared vs unsquared), none of which matches.
>
> **What this does *not* invalidate, which is most of the block.** Equality of $y_\lambda$ and $\tilde w_\lambda$ on self-conjugate partitions was treated only as a hypothesis rather than a derived theorem, so no downstream result was deduced from a false theorem. While that hypothesis stood, no model carried the intended $y$ and $\tilde w$ together, rendering any result conditioned on that combined hypothesis vacuous at the intended specialization rather than false. **The core relation $\beta_\lambda \cdot h = -C_\lambda$ is untouched** — its proof uses only the definitional scalings of $\beta_\lambda$ and $C_\lambda$ and never invokes $y_\lambda$, so the BW and LP scalings $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ and $C_\lambda = \tilde w_\lambda \cdot h/2$ stand as definitional. The block's own off-stratum statement, that $y_\lambda$ and $\tilde w_\lambda$ are genuinely distinct families, is correct — and on this evidence correct on the stratum too.
>
> **Disposition: omitted from the canonical weight axioms.** The self-conjugate equality assumption is omitted from the canonical weight hypothesis structure; $y$ remains as data only, so the structure is inhabited at the honest values while the two definitional scalings and $\beta_\lambda \cdot h = -C_\lambda$ are unchanged.

**Notation.** This block's weight is $\tilde w_\lambda$, the third of the three registered partition-weight families (notation register §7aa: $y_\lambda$, $w_\lambda$ and $\tilde w_\lambda$ are distinct at $q \neq 1$, distinct from the Ocneanu/Markov family $w_\lambda(q)$).
