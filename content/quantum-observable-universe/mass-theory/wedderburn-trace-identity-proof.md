*Proof.*
The Markov trace $\operatorname{tr}_M$ on $H_n(R, q)$ decomposes over
the Wedderburn blocks as
$\operatorname{tr}_M = \sum_{\lambda \vdash n} y_\lambda(q)\, \chi^\lambda$,
where $\chi^\lambda$ is the irreducible character of the block indexed
by $\lambda$ and $y_\lambda(q)$ is its Markov weight. Evaluating at the
identity and using $\chi^\lambda(\mathbf{1}) = d_\lambda = f^\lambda$
(the ordinary block dimension, the number of standard Young tableaux of
shape $\lambda$) gives
$$
  \operatorname{tr}_M(\mathbf{1})
    = \sum_{\lambda \vdash n} y_\lambda(q)\, d_\lambda .
$$
The Markov trace is normalized so that $\operatorname{tr}_M(\mathbf{1}) = 1$
(the defining trace condition), whence
$\sum_{\lambda \vdash n} d_\lambda\, y_\lambda(q) = 1$. The unit sum is
the Plancherel completeness of the $y_\lambda$ weights, established for
every $n$ from the closed-form recipe for $y_\lambda$
(`plancherel_via_recipe`).

At $q = 1$ the Markov weights reduce to $y_\lambda = d_\lambda / n!$, and
the identity becomes the Wedderburn–Artin dimension count
$\sum_\lambda d_\lambda^2 = n! = \dim H_n$ for $\mathbb{C}[S_n]$.
$\square$
