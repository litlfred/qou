Let $P \in \mathcal{S}(q)$ and let $\mathcal{C}_q$ be the Skein-Collatz map ([$q$-Collatz conjecture](#conj:q-collatz)). Restricting to the $N_{\mathrm{odd}}$ odd steps among the first $N$, set

$$
\langle v_{[2]} \rangle_N(P) := \frac{1}{N_{\mathrm{odd}}} \sum_{\substack{0 \leq k < N \\ \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}} v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr).
$$

The **orbit contact average** is $\langle v_{[2]} \rangle(P) := \lim_{N \to \infty} \langle v_{[2]} \rangle_N(P)$. With the **sharp contact threshold** $v^*(q) = \log [3]_q / \log [2]_q$, the **Collatz contact boundary** is

$$
\mathcal{H}_{Col}(q) = \bigl\{P \in \mathcal{S}(q) : \langle v_{[2]} \rangle(P) = v^*(q)\bigr\}.
$$
