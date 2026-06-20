*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $L = \hat{\beta}$ be the braid closure of a computation
$\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates
([Skein Turing machine](#rem:skein-turing-machine)).  The Skein
resolution tree $\mathcal{R}(L)$ has $3^c$ leaves — one per
discrete history — and the Markov trace collapses this tree to
the degree-$0$ observable $P_L(q)$.

A **computational horizon** for $L$ is a jet horizon
$\mathcal{H}_c \subset \mathcal{R}(L)$ such that:

1. **Degree-$0$ opacity.**  The evaluation $P_L(q_0)$ — the
   yes/no answer of the decision problem — is a degree-$0$
   section of the brane tower.  It cannot be extracted from
   any polynomial-depth subtree of $\mathcal{R}(L)$.

2. **Degree $\geq 1$ leakage.**  Individual resolution paths
   (witnesses) are degree-$1$ data: they are linear transport
   through the tree.  A single path can be **verified** in
   $O(\mathrm{poly}(c))$ Planck steps — one traverses the
   witness and checks consistency at each crossing.

3. **Bandwidth saturation.**  The information bandwidth
   $\mathfrak{B}(q)$ per Planck time
   ([information bandwidth](#def:information-speed-of-light))
   bounds the rate at which resolution paths can be sampled.
   If $3^c$ paths must be explored to extract the degree-$0$
   answer, and $\mathfrak{B}(q) \cdot t$ bounds the total
   information accessible in $t$ Planck steps, then the
   computation requires

   $$
     t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)}
      \cdot  3^{c - c_0}
   $$

   Planck steps whenever the surviving tree below depth $c_0$
   carries non-cancelling weight — i.e., whenever interference
   does not reduce the effective tree size to polynomial.

The computational horizon is an instance of the jet horizon
([jet horizon](#def:jet-horizon)) applied to the resolution
tree: degree-$0$ data (the answer) is separated from
degree $\geq 1$ data (the witnesses) by a codimension-$1$
barrier.  The barrier is **opaque** when the Markov trace
cannot factor the Skein polynomial into $O(\mathrm{poly}(c))$
terms — when the interference pattern of the $3^c$ histories
does not simplify.

**Structural parallel with the jet horizon.**

| Jet horizon | Computational horizon |
|-------------|----------------------|
| Degree-$0$ sections vanish on $\mathcal{H}$ | The answer $P_L(q_0)$ is inaccessible in poly time |
| Degree $\geq 1$ data leaks through | Witnesses (resolution paths) are poly-time verifiable |
| Hawking radiation: thermal, no particle identity | Partial computation: statistical correlations, no answer |
| Aeon boundary: separates observable epochs | Complexity class boundary: separates P from NP |
