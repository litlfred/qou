The orbit contact average of $P \in \mathcal{S}(q)$ measures the average $[2]_q$-adic valuation of the results of the odd steps over the first $N$ steps of the Skein-Collatz map ([conj:q-collatz](#conj:q-collatz)). Restricting to the $N_{\mathrm{odd}}$ odd steps:

$$
\langle v_{[2]} \rangle_N(P) := \frac{1}{N_{\mathrm{odd}}} \sum_{\substack{0 \leq k < N \\ \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}} v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr).
$$

The orbit contact average is defined by $\langle v_{[2]} \rangle(P) := \lim_{N \to \infty} \langle v_{[2]} \rangle_N(P)$.

The Collatz contact boundary is the codimension-$1$ locus where the orbit's contact with $D_{[2]}$ is exactly critical:

$$
\mathcal{H}_{Col}(q) = \bigl\{P \in \mathcal{S}(q) : \langle v_{[2]} \rangle(P) = v^*(q)\bigr\},
$$

where $v^*(q) = \log [3]_q / \log [2]_q$ is the sharp contact threshold. Elements above the boundary (high contact) converge; elements below (insufficient contact) diverge.
