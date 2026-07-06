Let $\beta$ be a braid on $n$ strands with $c$ crossings,
$L = \hat{\beta}$ its closure, and
$\mathcal{R}(L)$ the Skein resolution tree
([Skein Turing machine](#rem:skein-turing-machine)).  Fix a
polynomial bound $p(c) = c^d$.

**Definition.**
The **polynomial observable subcategory** of the resolution
tree is the full sub-poset

$$
  \mathcal{R}^{\circ}(L, q)
  = 
  \bigl\{
    x \in \mathcal{R}(L)
     : 
    \Gamma_{\mathrm{poly}}\!(x, A_0) \neq 0
  \bigr\},
$$

where $\Gamma_{\mathrm{poly}}(x, A_0)$ consists of those
degree-$0$ sections at $x$ that are computable — via the
Markov trace restricted to $\mathcal{R}_{p(c)}$ — in at most
$p(c)$ Planck steps.  This is the computational analog of the
observable subcategory
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$
([observable subcategory](#def:observable-subcategory)): the
nodes of the resolution tree from which the degree-$0$ answer
$P_L(q)$ is polynomial-time accessible.
