The **orbit contact average** of $P \in \mathcal{S}(q)$ measures the average $[2]_q$-adic valuation ([$[2]_q$-adic valuation](#def:two-q-adic-valuation)) following the odd steps of the Skein-Collatz map ([conj:q-collatz](#conj:q-collatz)). Over the first $N$ steps, restricting to the $N_{\mathrm{odd}}$ odd steps:

$$
  \langle v_{[2]} \rangle_N(P)
   := 
  \frac{1}{N_{\mathrm{odd}}}
  \sum_{\substack{0 \leq k < N \\
    \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}}
  v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr).
$$

The infinite-horizon limit $\langle v_{[2]} \rangle(P) := \lim_{N \to \infty} \langle v_{[2]} \rangle_N(P)$ is the **orbit contact average**.

The **Collatz contact boundary** is the codimension-$1$ locus where the orbit's contact with the halving divisor $D_{[2]}$ is exactly critical:

$$
  \mathcal{H}_{Col}(q)
  = 
  \bigl\{P \in \mathcal{S}(q) :
  \langle v_{[2]} \rangle(P) = v^*(q)\bigr\}.
$$

The sharp contact threshold is $v^*(q) = \log [3]_q / \log [2]_q$. Elements above this boundary achieve high contact and many halvings, ensuring convergence. Elements below this boundary achieve insufficient contact and diverge.
