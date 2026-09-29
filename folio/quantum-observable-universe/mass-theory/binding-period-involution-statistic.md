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
$I(n)$. The common value is a polynomial in $q$ of degree*

$$
\deg \;=\; n^{2} \;-\; H_{\min}(n),
\qquad
H_{\min}(n) \;=\; \min_{\lambda \vdash n} \sum_{c \in \lambda} h(c),
$$

*the minimum being over partitions of $n$ of the total hook length. Writing
$T_k = k(k+1)/2$, this minimum is itself closed-form,*

$$
H_{\min}(n) \;=\; 2n - 1 \;+\; \sum_{k \ge 2,\; T_k \le n-1} (n - T_k)
\;=\; \tfrac{2\sqrt{2}}{3}\, n^{3/2} + O(n),
$$

*attained at the staircase $(k, k-1, \dots, 1)$ when $n = T_k$ is triangular,
where it equals the square pyramidal number $k(k+1)(2k+1)/6$.*

> **Correction (2026-09-07).** This paragraph previously asserted that the
> left side "is a polynomial in $q$ of degree $n(n-1)$". That is false for
> every $n \ge 2$: it is the degree of the prefactor $q^{n(n-1)/2}$ times the
> naive bound, not of the product, and it exceeds the truth by
> $H_{\min}(n) - n = \Theta(n^{3/2})$. At $n = 3$ the polynomial is
> $q^{4} + 2q^{3} + q^{2}$, of degree $4$, against the claimed $6$; the
> degrees run $1, 4, 8, 14$ for $n = 2,3,4,5$ against $2, 6, 12, 20$.
> The identity displayed above is unaffected — only the degree remark was
> wrong. The block's own Lean sibling already carried the counterexample:
> `statExponents_three : statExponents 3 = {2, 3, 3, 4}` is kernel-decided
> and has maximum exponent $4$, so the `.lean` and the `.md` disagreed with
> each other. Derivation and verification:
> [`zn_hook_length_closed_form_probe.py`](../../../computations/deltalambda/zn_hook_length_closed_form_probe.py)
> (6/6, exact integer arithmetic) and
> [`hmin_closed_form_and_rev_sublinearity_probe.py`](../../../computations/deltalambda/hmin_closed_form_and_rev_sublinearity_probe.py)
> (5/5).
