The proposition separates two facts: the Markov trace is local in a single newly added crossing, and the Gröbner–Shirshov normal form depends on the whole word. A third statement is often attached to them, that the Markov trace of the normal form factorises over its letters,
$$
  \mathrm{tr}_M(\rho_{\mathrm{NF}}(\beta)) = \prod_{i=1}^{M} \widehat{V}_i(q),
$$
with each factor depending only on its own normal-form generator and the Bratteli path it traces through $H_1 \subset H_2 \subset \cdots$. This is not a theorem of the paper. The factors $\widehat{V}_i$ have no definition yet, and the Markov trace is not multiplicative, so no argument from the trace alone gives a product.

What has been checked is the input such a factorisation would rest on. Over $\mathbb{Q}(q)$ at generic $q$, the Wedderburn decomposition
$$
  H_n(R, q) \otimes_R \mathbb{Q}(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}_{\mathbb{Q}(q)}(S^\lambda_q)
$$
holds, and the Markov trace restricted to each block is a multiple $w_\lambda(q)$ of the standard trace \cite{wenzl1988}. The closed form
$$
  w_\lambda(q) = \prod_{x \in \lambda} \frac{z\,q^{c(x)} - z_{-}\,q^{-c(x)}}{q^{h(x)} - q^{-h(x)}}, \qquad z_{-} = z - (q - q^{-1}),
$$
where $c(x)$ and $h(x)$ are the content and hook length of the cell $x$, has been checked exactly for every $\lambda \vdash n \le 5$. Turning this into the product above needs a definition of $\widehat{V}_i$ in terms of the Bratteli path and a proof that the block weights compose along it. Both remain to be done.
