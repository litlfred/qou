We define a computational horizon as a barrier where evaluation outpaces verification. 

Let $L = \hat{\beta}$ be the braid closure of a computation $\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates ([Skein Turing machine](#rem:skein-turing-machine)). The Skein resolution tree $\mathcal{R}(L)$ has $3^c$ leaves corresponding to discrete histories. The Markov trace collapses this tree to the degree-$0$ observable $P_L(q)$.

A **computational horizon** for $L$ is a jet horizon $\mathcal{H}_c \subset \mathcal{R}(L)$ exhibiting three properties:

1. **Degree-$0$ opacity.** The evaluation $P_L(q_0)$ provides the yes/no answer of the decision problem. As a degree-$0$ section of the brane tower, it cannot be extracted from any polynomial-depth subtree of $\mathcal{R}(L)$.
2. **Degree $\geq 1$ leakage.** Individual resolution paths act as witnesses. As degree-$1$ linear transport data, a single path can be verified in $O(\mathrm{poly}(c))$ Planck steps by checking consistency at each crossing.
3. **Bandwidth saturation.** The information bandwidth $\mathfrak{B}(q)$ per Planck time ([information bandwidth](#def:information-bandwidth)) restricts the sampling rate of resolution paths. If $3^c$ paths must be explored to extract the degree-$0$ answer, extracting the answer requires

   $$
     t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)}
      \cdot  3^{c - c_0}
   $$

   Planck steps whenever interference fails to reduce the effective tree size to polynomial.

The computational horizon is a concrete instance of the jet horizon ([jet horizon](#def:jet-horizon)) applied to the resolution tree. It separates degree-$0$ data (the answer) from degree $\geq 1$ data (the witnesses) by a codimension-$1$ barrier. This barrier becomes opaque when the Markov trace fails to factor the Skein polynomial into $O(\mathrm{poly}(c))$ terms.

**Structural parallel with the jet horizon.**

| Jet horizon | Computational horizon |
|-------------|----------------------|
| Degree-$0$ sections vanish on $\mathcal{H}$ | The answer $P_L(q_0)$ is inaccessible in poly time |
| Degree $\geq 1$ data leaks through | Witnesses (resolution paths) are poly-time verifiable |
| Hawking radiation: thermal, no particle identity | Partial computation: statistical correlations, no answer |
| Aeon boundary: separates observable epochs | Complexity class boundary: separates P from NP |
