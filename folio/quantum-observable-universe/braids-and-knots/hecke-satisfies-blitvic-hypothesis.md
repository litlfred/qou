Let $\tilde\sigma_i := \sigma_i - z \cdot 1 \in H_\infty(q)$ denote the centred Hecke generators under the Markov trace $\mathrm{tr}_M$, where $z = \mathrm{tr}_M(\sigma_i) = q^3/(q^2+1)$ and $h = q - q^{-1}$. The non-commutative random variables $\tilde\sigma_i$ satisfy the exact finite-$k$ orthogonality and singleton-vanishing identities together with the macroscopic pair-partition limit of Blitvić's non-commutative central limit theorem:

1. **Exact mean-zero and Kronecker covariance ($k = 1, 2$).** For all generator indices $i, j \geq 1$ (including adjacent indices $|i - j| = 1$):
   $$
     \mathrm{tr}_M(\tilde\sigma_i) = 0,
     \qquad
     \mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j) = v\,\delta_{i = j},
     \qquad
     v := h z + 1 - z^2 = \frac{q^4 + q^2 + 1}{(q^2 + 1)^2} > 0.
   $$
2. **Exact maximal-singleton vanishing vs. single-generator skewness.** Any centred word $\tilde\sigma_{i_1}\cdots\tilde\sigma_{i_k}$ in which the highest strand index $m = \max_r i_r$ appears with multiplicity one vanishes identically under $\mathrm{tr}_M$:
   $$
     \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr) = 0
     \qquad
     \bigl(\#\{r : i_r = \max_s i_s\} = 1\bigr).
   $$
   By contrast, unscaled finite-$k$ words with repeated indices need not vanish for odd $k \geq 3$: from $\tilde\sigma_i^2 = (h - 2z)\tilde\sigma_i + v\cdot 1$, the single-generator third central moment is
   $$
     \mathrm{tr}_M(\tilde\sigma_i^3) = (h - 2z)\,v = -\frac{(q^4 + 1)(q^4 + q^2 + 1)}{q(q^2 + 1)^3} \neq 0 \quad (q > 0).
   $$
3. **Macroscopic $N^{-1/2}$ pair-partition limit.** For the normalised sum $S_N := (N v)^{-1/2} \sum_{i=1}^N \tilde\sigma_i$, singleton vanishing eliminates every index partition containing a block of size $1$, while blocks of size $\geq 3$ carry at most $\lfloor (k-1)/2 \rfloor$ distinct indices and are suppressed by $O(N^{-1/2}) \to 0$. In the macroscopic limit $N \to \infty$, only pair-partitions $\pi \in P_2(k)$ survive:
   $$
     \lim_{N \to \infty} \mathrm{tr}_M(S_N^k)
     =
     \begin{cases}
       0 & \text{if } k \text{ is odd}, \\
       |P_2(k)| = (k - 1)!! & \text{if } k \text{ is even}.
     \end{cases}
   $$
