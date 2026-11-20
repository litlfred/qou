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
> **The last two rows are a scope-(b) structural exclusion**, not a numerical near-miss. Convention D is the $\mathfrak{sl}_2$ point of the Ocneanu family ([Reconciliation of the Markov parameter $z$](../mass-endomorphism/markov-z-reconciliation.md)), so $y_\lambda = 0$ identically once $\lambda$ has more than two rows — such a $\lambda$ has a cell of content $-2$, whose Ocneanu numerator factor vanishes. Meanwhile $\tilde w_\lambda$ is a ratio of products of positive quantum integers, hence strictly positive for $q > 0$. The identity there asserts $0 = \text{positive}$, and no choice of parameter reconciles it. The other two rows are scope (a): measured non-equality under six readings of $\dim_q(\lambda)^2/[n]_q!$ (symmetric vs unbalanced quantum integer, $q$-deformed vs ordinary dimension, squared vs unsquared), none of which matches.
>
> **What this does *not* invalidate, which is most of the block.** `y_eq_self_conjugate` was previously a Lean **class field** — assumed, not proved — so nothing in the corpus was ever *proved* wrong by its falsity. What followed, while it stood, was that the class had no inhabitant carrying the intended $y$ and $\tilde w$ together, so any `[WedderburnWeightCanonical R]`-conditional result was vacuous at the intended instance rather than false. **`WedderburnWeightCanonical.beta_mul_h_eq_neg_C`, the file's one real theorem, is untouched** — its proof uses `beta_eq` and `C_eq` only and never reads the `y` field, so the BW and LP scalings $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ and $C_\lambda = \tilde w_\lambda \cdot h/2$ stand as definitional. The block's own off-stratum statement, that $y_\lambda$ and $\tilde w_\lambda$ are genuinely distinct families, is correct — and on this evidence correct on the stratum too.
>
> **Disposition: dropped from the class signature.** Of the three options — restrict the field to $\lambda = (1)$, drop it, or demote the block to a conjecture — the author chose to drop. The field `y_eq_self_conjugate` and its projection theorem `y_self_conjugate` are removed from the Lean; `y` remains in the class as data only, and the class is inhabitable at the honest values. The two definitional scalings and `beta_mul_h_eq_neg_C` are unchanged. Weakening the field to make the class inhabitable would have been laundering, which is why the choice waited for the author. Measurement: [`wenzl_bridge_self_conjugate_premise_is_false.py`](https://github.com/litlfred/qou/blob/main/computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py), whose first check now guards the drop.

**Notation.** This block's weight is $\tilde w_\lambda$, the third of the three registered partition-weight families (notation register §7aa: $y_\lambda$, $w_\lambda$ and $\tilde w_\lambda$ are distinct at $q \neq 1$). The body previously wrote it as $w_\lambda(q)$, conflating it with the Ocneanu/Markov family; the manifest title and the Lean both say $\tilde w_\lambda$, and they are correct.
