A computational horizon is a barrier where evaluation outpaces verification. 

Let $L = \hat{\beta}$ be the braid closure of a computation $\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates. The Skein resolution tree $\mathcal{R}(L)$ contains $3^c$ leaves representing discrete histories. The Markov trace collapses this tree to the degree-$0$ observable $P_L(q)$.

A **computational horizon** for $L$ is a jet horizon $\mathcal{H}_c \subset \mathcal{R}(L)$ exhibiting three properties:

1. **Degree-$0$ opacity.** The evaluation $P_L(q_0)$ provides the yes/no answer of the decision problem. As a degree-$0$ section of the brane tower, it resists extraction from any polynomial-depth subtree of $\mathcal{R}(L)$.
2. **Degree $\geq 1$ leakage.** Individual resolution paths furnish witnesses. As degree-$1$ linear transport data, a single path admits verification in $O(\mathrm{poly}(c))$ Planck steps by checking crossing consistencies.
3. **Bandwidth saturation.** The information bandwidth $\mathfrak{B}(q)$ per Planck time restricts the sampling rate. If extracting the degree-$0$ answer requires exploring all $3^c$ paths, the extraction demands
$$
  t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)} \cdot  3^{c - c_0}
$$
Planck steps whenever interference fails to bound the effective tree size polynomially.

The computational horizon applies the jet horizon directly to the resolution tree. It separates the degree-$0$ answer from the degree $\geq 1$ witnesses via a codimension-$1$ barrier. This barrier turns opaque when the Markov trace fails to factor the Skein polynomial into $O(\mathrm{poly}(c))$ terms.

**Structural parallel with the jet horizon.**

| Jet horizon | Computational horizon |
|-------------|----------------------|
| Degree-$0$ sections vanish on $\mathcal{H}$ | The answer $P_L(q_0)$ is inaccessible in poly time |
| Degree $\geq 1$ data leaks through | Witnesses (resolution paths) are poly-time verifiable |
| Hawking radiation: thermal, no particle identity | Partial computation: statistical correlations, no answer |
| Aeon boundary: separates observable epochs | Complexity class boundary: separates P from NP |
