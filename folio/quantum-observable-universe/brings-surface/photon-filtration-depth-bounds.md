*Let $n \ge 2$, $N = n(n-1)/2$, and let $F_1 \subset H_n(q)$ be spanned by $1$ and the sliding [photons](#def:photon)' terms $\sigma_i$ $(0 \le i \le n-2)$ and $\sigma_i\sigma_{i+1}^{-1}$ $(0 \le i \le n-3)$. Let $F_k$ be the span of products of at most $k$ elements of $F_1$, and $L(n)$ the least $k$ with $F_k = H_n(q)$. Then*

$$
  \left\lceil \tfrac{N}{2} \right\rceil \;\le\; L(n) \;\le\; \left\lfloor \tfrac{n^2}{4} \right\rfloor .
$$

**Proof.** Let $C_m$ be the span of the Iwahori–Matsumoto basis elements $T_w$ with $\ell(w) \le m$. Then $C_aC_b \subseteq C_{a+b}$, and $T_{w_0} \notin C_{N-1}$ \cite{iwahori1964}. Since $\sigma_i = T_{s_i}$ and $\sigma_i\sigma_{i+1}^{-1} = T_{s_is_{i+1}} - (q - q^{-1})\,T_{s_i}$, we have $F_1 \subseteq C_2$. Hence $F_k \subseteq C_{2k}$, and $T_{w_0} \in F_k$ forces $N \le 2k$.

For the upper bound, write every $w$ as a reduced product of increasing runs $s_a s_{a+1} \cdots s_b$ of lengths $r_j \le j$, $j = 1, \dots, n-1$. This is the inverse of the decreasing-run normal form of $w^{-1}$. A run of length $r$ equals a product of $\lfloor r/2 \rfloor$ elements $\sigma_i\sigma_{i+1}^{-1}$ and at most one $\sigma_i$, up to terms of smaller length. So $F_K$ contains $T_w + (\text{shorter terms})$ for every $w$, with $K = \sum_{j=1}^{n-1}\lceil j/2\rceil = \lfloor n^2/4 \rfloor$. These $n!$ elements are unitriangular in the basis $\{T_w\}$, so they span $H_n(q)$. $\square$
