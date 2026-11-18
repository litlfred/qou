Let $K$ be a field, $q \in K^\times$, $h = q - q^{-1}$, and let $\mathrm{tr}$ be a $K$-linear trace on $H_1(q)$ with $\mathrm{tr}(1) = 1$ and $\mathrm{tr}(\sigma) = z$. Put $\tilde\sigma := \sigma - z \cdot 1$. Then

$$
  \mathrm{tr}\bigl(\tilde\sigma^{2}\bigr) = h z + 1 - z^{2},
  \qquad
  \mathrm{tr}\bigl(\tilde\sigma^{3}\bigr) = (h^{2}+1)\,z + h - 3 h z^{2} - 3 z + 2 z^{3}.
$$

Every Markov trace on the Hecke tower restricts to such a trace on $H_1(q)$. Under convention D, $z = q^{3}/(q^{2}+1)$; at $q = 2$ this gives $\mathrm{tr}(\tilde\sigma^{3}) = -357/250 \neq 0$.

So the odd centred moments of the Hecke generators under the Jones–Markov trace do **not** all vanish, and the generators do **not** satisfy the pair-partition hypothesis of Blitvić's non-commutative central limit theorem [`blitvic2012`], which requires every odd moment to vanish.
