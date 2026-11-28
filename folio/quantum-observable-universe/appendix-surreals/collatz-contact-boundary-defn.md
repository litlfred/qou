The orbit contact average of $P \in \mathcal{S}(q)$ measures the average $[2]_q$-adic valuation of the results of the odd steps over the first $N$ steps of the Skein-Collatz map ([conj:q-collatz](#conj:q-collatz)). Restricting to the $N_{\mathrm{odd}}$ odd steps:

$$
\langle v_{[2]} \rangle_N(P) := \frac{1}{N_{\mathrm{odd}}} \sum_{\substack{0 \leq k < N \\ \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}} v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr).
$$

Define the orbit contact average as $\langle v_{[2]} \rangle(P) := \lim_{N \to \infty} \langle v_{[2]} \rangle_N(P)$.

The Collatz contact boundary is the codimension-$1$ locus where the orbit's contact with $D_{[2]}$ is exactly critical:

$$
\mathcal{H}_{Col}(q) = \bigl\{P \in \mathcal{S}(q) : \langle v_{[2]} \rangle(P) = v^*(q)\bigr\},
$$

where $v^*(q) = \log [3]_q / \log [2]_q$ is the heuristic contact threshold at a real value $q > 0$. The limit $\langle v_{[2]} \rangle(P)$ does not separate convergent from divergent orbits. On the fundamental cycle $q^{-1} \mapsto 1 + q^{-1} = q^{-1}[2]_q \mapsto q^{-1}$, each odd step is followed by exactly one halving, so $\langle v_{[2]} \rangle = 1$, and every orbit that reaches this cycle has limit $1$. A degree count gives $\langle v_{[2]} \rangle \leq 1$ for every domain-stable orbit with infinitely many odd steps ([section introduction](#sec:collatz-intro), item 7). The convention matters: $\mathcal{C}_q$ already divides by $[2]_q$ in its odd step, so $v_{[2]}$ counts the halvings *after* that built-in one.
