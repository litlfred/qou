*Proof.* Write $X$ for a polynomial variable and $p(X) = X^{2} - hX - 1$. The quadratic relation $\sigma^{2} = h\sigma + 1$ says $p(\sigma) = 0$, so any polynomial in $\sigma$ can be reduced modulo $p$ before the trace is taken. By linearity, $\mathrm{tr}(aX + b)|_{X=\sigma} = a z + b$.

**Variance.** In $K[X]$,
$$
  (X - z)^{2} = p(X) + (h - 2z)\,X + (1 + z^{2}),
$$
so $\mathrm{tr}(\tilde\sigma^{2}) = (h - 2z)z + 1 + z^{2} = hz + 1 - z^{2}$.

**Third moment.** In $K[X]$,
$$
  (X - z)^{3} = (X + h - 3z)\,p(X) + \bigl(h^{2} + 1 - 3hz + 3z^{2}\bigr)X + \bigl(h - 3z - z^{3}\bigr),
$$
so
$$
  \mathrm{tr}(\tilde\sigma^{3}) = (h^{2} + 1 - 3hz + 3z^{2})\,z + h - 3z - z^{3}
  = (h^{2}+1)z + h - 3hz^{2} - 3z + 2z^{3}.
$$

**A Markov trace restricts to such a trace.** For a Markov trace family on the Hecke tower, $\mathrm{tr}_1$ is $K$-linear with $\mathrm{tr}_1(1) = 1$, and the Markov property at $x = 1$ gives $\mathrm{tr}_1(\sigma_0) = z$.

**The value at $q = 2$.** Here $h = 3/2$ and $z = 8/5$, so
$$
  \mathrm{tr}(\tilde\sigma^{3}) = \tfrac{13}{4}\cdot\tfrac{8}{5} + \tfrac{3}{2} - 3\cdot\tfrac{3}{2}\cdot\tfrac{64}{25} - \tfrac{24}{5} + 2\cdot\tfrac{512}{125} = -\tfrac{357}{250}.
$$

Blitvić's hypothesis requires every odd centred moment to vanish, so it fails. $\square$

**Where the earlier argument went wrong.** It applied the Markov property to a factor $\tilde\sigma_i$ inside a word in which the same index $i$ occurs again. The Markov property $\mathrm{tr}(x\sigma_n) = z\,\mathrm{tr}(x)$ holds only for $x \in H_n(q)$, that is, when $\sigma_n$ does not occur in $x$. It does not apply when the index is repeated.
