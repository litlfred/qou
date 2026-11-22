Let $\beta$ be a braid on $n$ strands with $c$ crossings. Let $L = \hat{\beta}$ be its closure. Let $\mathcal{R}(L)$ be the Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)). Fix a polynomial bound $p(c) = c^d$.

**Definition.**
The **polynomial observable subcategory** of the resolution tree is the full sub-poset

$$
  \mathcal{R}^{\circ}(L, q)
  = 
  \bigl\{
    x \in \mathcal{R}(L)
     : 
    \Gamma_{\mathrm{poly}}\!(x, A_0) \neq 0
  \bigr\}.
$$

The set $\Gamma_{\mathrm{poly}}(x, A_0)$ consists of degree-$0$ sections at $x$ that the Markov trace computes in at most $p(c)$ Planck steps. This trace restricts to $\mathcal{R}_{p(c)}$. It collects the nodes of the resolution tree from which the degree-$0$ answer $P_L(q)$ is polynomial-time accessible.
