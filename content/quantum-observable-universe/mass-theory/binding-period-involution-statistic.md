**Proposition (the balanced dimension sum as an involution statistic).**

*For $n \geq 1$ let $[k] = (q^k - q^{-k})/(q - q^{-1})$ denote the balanced
quantum integer, and for a partition $\lambda \vdash n$ with hook lengths
$h(c)$, $c \in \lambda$, set*

$$
\dim_q^{\mathrm{bal}}(\lambda) \;=\; \frac{\prod_{k=1}^{n} [k]}{\prod_{c \in \lambda} [h(c)]},
\qquad
S^{\mathrm{bal}}(n; q) \;=\; \sum_{\lambda \vdash n} \dim_q^{\mathrm{bal}}(\lambda).
$$

*For an involution $w \in \mathrm{Inv}(S_n)$ let $\lambda(w)$ be its RSK
shape, let $\mathrm{maj}(w) = \sum_{i \in \mathrm{Des}(w)} i$ be its major
index, where $\mathrm{Des}(w) = \{\, i : w(i) > w(i+1) \,\}$ is the descent
set, and let $\mathrm{content}(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$
be the content sum of a shape. Then*

$$
S^{\mathrm{bal}}(n; q)\, q^{n(n-1)/2}
\;=\;
\sum_{w \in \mathrm{Inv}(S_n)} q^{\,2\,\mathrm{maj}(w) + \mathrm{content}(\lambda(w))} .
$$

*In particular both sides specialise at $q = 1$ to the involution count
$I(n)$, and the left side is a polynomial in $q$ of degree $n(n-1)$.*
