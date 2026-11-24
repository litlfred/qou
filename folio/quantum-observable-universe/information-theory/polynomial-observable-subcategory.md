Let $\beta$ be a braid on $n$ strands with $c$ crossings, let $L = \hat{\beta}$ be its closure, let $\mathcal{R}(L)$ be the Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)), and fix a polynomial bound $p(c) = c^d$. For $x \in \mathcal{R}(L)$, let $\Gamma_{\mathrm{poly}}(x, A_0)$ be the set of degree-$0$ sections at $x$ that the Markov trace computes in at most $p(c)$ Planck steps. The **polynomial observable subcategory** of the resolution tree is the full sub-poset

$$
  \mathcal{R}^{\circ}(L, q)
  = 
  \bigl\{
    x \in \mathcal{R}(L)
     : 
    \Gamma_{\mathrm{poly}}\!(x, A_0) \neq 0
  \bigr\}.
$$
