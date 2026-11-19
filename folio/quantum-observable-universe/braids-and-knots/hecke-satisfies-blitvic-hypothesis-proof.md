*Proof.* The three claims follow directly from the Hecke quadratic relation $\sigma_i^2 = h\sigma_i + 1$ ($h = q - q^{-1}$), cyclicity of the Markov trace $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$, and the Markov stabilisation axiom $\mathrm{tr}_M(x \sigma_m) = z\,\mathrm{tr}_M(x)$ whenever $x \in H_m(q)$ involves only generators $\sigma_1, \ldots, \sigma_{m-1}$.

**Step 1: Centred quadratic relation, mean zero ($k = 1$), and exact Kronecker covariance ($k = 2$).** Let $\tilde\sigma_i := \sigma_i - z \cdot 1$ where $z = \mathrm{tr}_M(\sigma_i) = q^3/(q^2+1)$. By linearity and $\mathrm{tr}_M(1) = 1$,
$$
  \mathrm{tr}_M(\tilde\sigma_i) = \mathrm{tr}_M(\sigma_i) - z\,\mathrm{tr}_M(1) = z - z = 0.
$$
Expanding $\tilde\sigma_i^2 = (\sigma_i - z\cdot 1)^2$ and substituting $\sigma_i^2 = h\sigma_i + 1 = h(\tilde\sigma_i + z\cdot 1) + 1$ yields the centred Hecke quadratic relation:
$$
  \tilde\sigma_i^2
  = (h - 2z)\,\tilde\sigma_i + (h z + 1 - z^2)\cdot 1
  = (h - 2z)\,\tilde\sigma_i + v\cdot 1,
  \qquad
  v := h z + 1 - z^2.
$$
Applying $\mathrm{tr}_M$ gives the variance $\mathrm{tr}_M(\tilde\sigma_i^2) = (h - 2z)\cdot 0 + v = v > 0$ for all real $q > 0$ ([centred Hecke variance positivity](#prop:centered-hecke-variance-positive)). For $i \neq j$, assume without loss of generality that $i < j$ (the case $j < i$ follows by trace cyclicity $\mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j) = \mathrm{tr}_M(\tilde\sigma_j \tilde\sigma_i)$). Since $\tilde\sigma_i \in H_j(q)$ involves only index $i < j$, the Markov stabilisation property applies directly at index $j$ for every $i < j$, including the adjacent case $j = i + 1$:
$$
  \mathrm{tr}_M(\tilde\sigma_i \sigma_j) = z\,\mathrm{tr}_M(\tilde\sigma_i) = 0,
  \qquad
  \mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j)
  = \mathrm{tr}_M(\tilde\sigma_i \sigma_j) - z\,\mathrm{tr}_M(\tilde\sigma_i)
  = 0.
$$
Hence $\mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j) = v\,\delta_{i = j}$ for all $i, j \geq 1$.

**Step 2: Exact maximal-singleton vanishing and non-zero single-generator skewness.** Let $w = (i_1, \ldots, i_k)$ be a generator word whose maximum index $m = \max_r i_r$ occurs at a unique position $r_0$. By trace cyclicity, $\mathrm{tr}_M(\tilde\sigma_{i_1}\cdots\tilde\sigma_{i_k}) = \mathrm{tr}_M(X \tilde\sigma_m)$ where $X = \tilde\sigma_{i_{r_0+1}}\cdots\tilde\sigma_{i_k}\tilde\sigma_{i_1}\cdots\tilde\sigma_{i_{r_0-1}}$ is a product of centred generators with indices strictly less than $m$, so $X \in H_m(q)$. By the Markov stabilisation axiom at strand $m$,
$$
  \mathrm{tr}_M(X \tilde\sigma_m)
  = \mathrm{tr}_M(X \sigma_m) - z\,\mathrm{tr}_M(X)
  = z\,\mathrm{tr}_M(X) - z\,\mathrm{tr}_M(X)
  = 0.
$$
In particular, any multilinear word (where all indices are distinct) vanishes identically. By contrast, when the maximum index is repeated, applying the centred quadratic relation $\tilde\sigma_i^2 = (h - 2z)\tilde\sigma_i + v\cdot 1$ generates a non-zero drift term $(h - 2z)\tilde\sigma_i$. Specifically, for $k = 3$ and $i_1 = i_2 = i_3 = i$:
$$
  \mathrm{tr}_M(\tilde\sigma_i^3)
  = \mathrm{tr}_M\bigl(\tilde\sigma_i \cdot \tilde\sigma_i^2\bigr)
  = (h - 2z)\,\mathrm{tr}_M(\tilde\sigma_i^2) + v\,\mathrm{tr}_M(\tilde\sigma_i)
  = (h - 2z)\,v.
$$
For $z = q^3/(q^2+1)$ and $h = q - q^{-1}$, one has $h - 2z = -(q^4 + 1)/(q(q^2+1)) < 0$ for all real $q > 0$, so $\mathrm{tr}_M(\tilde\sigma_i^3) = (h - 2z)v \neq 0$. Thus pair-partition reduction holds in the $N^{-1/2}$-scaled macroscopic limit rather than for unscaled single-generator odd moments.

**Step 3: Macroscopic $N^{-1/2}$ pair-partition limit.** Expand the $k$-th moment of $S_N = (N v)^{-1/2} \sum_{i=1}^N \tilde\sigma_i$:
$$
  \mathrm{tr}_M(S_N^k)
  = (N v)^{-k/2} \sum_{1 \leq i_1, \ldots, i_k \leq N}
    \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr).
$$
For each index tuple $(i_1, \ldots, i_k) \in \{1, \ldots, N\}^k$, decompose its support $\{i_1, \ldots, i_k\} \subset \{1, \ldots, N\}$ into maximal connected components $R_1 < R_2 < \cdots < R_c$ under adjacency $|x - y| \leq 1$, so that $\max R_t \leq \min R_{t+1} - 2$ for every $1 \leq t < c$. Because generators in distinct runs satisfy $|x - y| \geq 2$, far-commutativity $\tilde\sigma_x \tilde\sigma_y = \tilde\sigma_y \tilde\sigma_x$ rearranges the word into a product of single-run subwords $\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k} = W_{R_1} W_{R_2} \cdots W_{R_c}$. Downward Hecke reduction and Markov stabilisation on $R_c$ act strictly above strand $\max R_{c-1} + 1$ and commute with $W_{R_1} \cdots W_{R_{c-1}}$, yielding exact multiplicative factorisation across gap-separated runs:
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  = \prod_{t=1}^c \mathrm{tr}_M(W_{R_t}).
$$
If any run $R_t$ contains only a single letter of the tuple ($|W_{R_t}| = 1$), Step 1 gives $\mathrm{tr}_M(W_{R_t}) = \mathrm{tr}_M(\tilde\sigma_j) = 0$. Every non-vanishing tuple therefore has $|W_{R_t}| \geq 2$ for each $t$, which forces $c \leq \lfloor k/2 \rfloor$. Moreover, each contiguous run $R_t$ has diameter at most $k - 1$, so for fixed word-shape and relative offsets $(i_r - \min R_{t(r)})$ there are at most $N^c$ choices of $(\min R_1, \ldots, \min R_c) \in \{1, \ldots, N\}^c$, and $|\mathrm{tr}_M(W_{R_t})|$ depends only on the translation-invariant relative offsets within $R_t$:
- If $k$ is odd, every non-vanishing tuple satisfies $c \leq (k-1)/2$, so the total number of non-vanishing tuples is $O(N^{(k-1)/2})$ with uniformly bounded trace weights. Multiplied by $(N v)^{-k/2}$, the sum is $O(N^{-1/2}) \to 0$ as $N \to \infty$.
- If $k = 2m$ is even, all non-vanishing tuples with $c \leq m - 1$ runs contribute $O(N^{m-1} \cdot N^{-m}) = O(N^{-1}) \to 0$. A tuple has $c = m$ runs if and only if $|W_{R_t}| = 2$ for every $1 \leq t \leq m$. Within a two-letter run $W_{R_t} = \tilde\sigma_a \tilde\sigma_b$, either $a \neq b$ ($|a - b| = 1$, for which Step 1 gives $\mathrm{tr}_M(\tilde\sigma_a \tilde\sigma_b) = 0$) or $a = b$ ($R_t = \{j_t\}$, for which $\mathrm{tr}_M(\tilde\sigma_{j_t}^2) = v$). Thus the surviving $c = m$ tuples correspond precisely to pair-partitions $\pi \in P_2(2m)$ assigned to pairwise gap-separated indices $|j_a - j_b| \geq 2$. Since $N(N-1)\cdots(N-m+1) - O(N^{m-1}) = N^m - O(N^{m-1})$ ordered $m$-tuples in $\{1, \ldots, N\}^m$ satisfy $|j_a - j_b| \geq 2$ for all $a \neq b$, summing over all $|P_2(2m)| = (2m - 1)!!$ pair-partitions yields
$$
  \lim_{N \to \infty} \mathrm{tr}_M(S_N^{2m})
  = \lim_{N \to \infty} (N v)^{-m} \cdot |P_2(2m)| \cdot \bigl(N^m - O(N^{m-1})\bigr) v^m
  = (2m - 1)!!. \qquad \square
$$
