*Proof.*
The Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ decomposes over
the Wedderburn blocks as
$\mathrm{tr}_M = \sum_{\lambda \vdash n} y_\lambda(q)\, \chi^\lambda$,
where $\chi^\lambda$ is the irreducible character of the block indexed
by $\lambda$ and $y_\lambda(q)$ is its Markov weight. Evaluating at the
identity and using $\chi^\lambda(\mathbf{1}) = d_\lambda = f^\lambda$
(the ordinary block dimension, the number of standard Young tableaux of
shape $\lambda$) gives
$$
  \mathrm{tr}_M(\mathbf{1})
    = \sum_{\lambda \vdash n} y_\lambda(q)\, d_\lambda .
$$
The Markov trace is normalized so that $\mathrm{tr}_M(\mathbf{1}) = 1$
(the defining trace condition), whence
$\sum_{\lambda \vdash n} d_\lambda\, y_\lambda(q) = 1$. The
decomposition exists because $H_n(R, q)$ is semisimple under the
hypothesis $[k]_q \neq 0$ for $2 \le k \le n$.

The weights $y_\lambda$ are *not* the Plancherel weights
$d_\lambda / n!$ at $q = 1$. Under convention D, $q = 1$ gives
$z = 1/2$; at $n = 2$ the conditions
$y_{(2)} + y_{(1,1)} = 1$ and $y_{(2)} - y_{(1,1)} = \mathrm{tr}_M(\sigma) = 1/2$
give $y_{(2)} = 3/4$, $y_{(1,1)} = 1/4$. The Plancherel weights belong to
the normalised regular trace of $\mathbb{C}[S_n]$, which is the Markov
trace at $z = 0$; for it the identity is the Wedderburn–Artin count
$\sum_\lambda d_\lambda^2 = n!$.
$\square$
