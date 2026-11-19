Let $L = \hat{\beta}$ be the braid closure of a computation $\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates, let $\mathcal{R}(L)$ be its Skein resolution tree, with $3^c$ leaves, and let $P_L(q)$ be the degree-$0$ observable to which the Markov trace collapses $\mathcal{R}(L)$. A **computational horizon** for $L$ is a jet horizon $\mathcal{H}_c \subset \mathcal{R}(L)$ with the following three properties.

1. **Degree-$0$ opacity.** The evaluation $P_L(q_0)$, which gives the yes/no answer of the decision problem, cannot be extracted from any polynomial-depth subtree of $\mathcal{R}(L)$.
2. **Degree $\geq 1$ leakage.** Each individual resolution path, as degree-$1$ linear transport data, admits verification in $O(\mathrm{poly}(c))$ Planck steps by checking crossing consistencies.
3. **Bandwidth saturation.** With information bandwidth $\mathfrak{B}(q)$ per Planck time, extracting the degree-$0$ answer by exploring all $3^c$ paths demands
$$
  t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)} \cdot  3^{c - c_0}
$$
Planck steps whenever interference fails to bound the effective tree size polynomially.
