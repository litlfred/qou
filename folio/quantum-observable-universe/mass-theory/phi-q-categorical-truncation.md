*Let $\mathfrak{H}$ be a confined particle with Hecke NF $T_w$. The categorical brane-tower contribution truncates to the finite sum:*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w) = \sum_{k=0}^{k_\star(T_w)} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(T_w) = \sum_i \Phi_q^{[\leq k_\star(T_w)]}(z_i).
$$

*The depth $k_\star(T_w)$ is exactly the maximum GB-depth among the support partitions. Truncation at any deeper level $k \geq k_\star$ yields the identical categorical value.*

*Scope.* With GB-depth defined as Lusztig's $a$-function ([cellular-depth-filtration proposition](#prop:cellular-depth-filtration)); the three earlier readings (ideal power, Coxeter length, rewrite depth) are each degenerate or not compatible with the blocks. With that choice the statement splits in two:

- The **centre-projection** part (vanishing above $k_\star$, independence of the cut-off for $k\ge k_\star$, and recovery of the trace) is [cell-depth-truncation proposition](#prop:cell-depth-truncation), items 1–3. On $T_w$ it removes nothing: $k_\star(T_w)=\binom n2$, the largest value of $a$ (item 4).
- The **second equality**, which identifies the level-$K$ partial sum with $\sum_i\Phi_q^{[\le K]}(z_i)$ at every level, is false together with stabilisation: $\Phi_q^{[\le K+1]}(z)\ne\Phi_q^{[\le K]}(z)$ for every $z\ne0$ (item 5 of the same proposition). At a single level that equality is a definition of a residual, not a theorem.
