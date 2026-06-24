By induction on the list. The empty product is $1 = 0\cdot\sigma_i + 1\cdot 1$.
For the step, suppose $\prod_{\mathrm{ds}} = \alpha'\,\sigma_i + \beta'\,1$.
Then
$$
\begin{aligned}
(\sigma_i + d\,1)\,(\alpha'\,\sigma_i + \beta'\,1)
  &= \alpha'\,\sigma_i^2 + (\beta' + d\,\alpha')\,\sigma_i + d\,\beta'\,1 \\
  &= \alpha'\,\bigl((q-q^{-1})\sigma_i + 1\bigr) + (\beta' + d\,\alpha')\,\sigma_i + d\,\beta'\,1 \\
  &= \bigl(\alpha'(h + d) + \beta'\bigr)\,\sigma_i + \bigl(\alpha' + \beta'\,d\bigr)\,1,
\end{aligned}
$$
using the quadratic relation in the second line. This is exactly
$(\alpha,\beta)_{d\,::\,\mathrm{ds}}$. $\qquad\blacksquare$

This is the Cayley–Hamilton reduction for the rank-one quadratic that
every Hecke generator satisfies: since $\sigma_i$ annihilates
$(x - q)(x + q^{-1})$, any polynomial in $\sigma_i$ alone is congruent to a
linear remainder $\alpha\,\sigma_i + \beta\,1$ modulo that quadratic. The
recursion is purely ring-theoretic, holding over any commutative base ring
$R$ with no archimedean or invertibility hypothesis. (The closed eigenvalue
form $\alpha = (E_1 - E_2)/(q + q^{-1})$, $E_1 = \prod_j (q + d_j)$,
$E_2 = \prod_j (-q^{-1} + d_j)$ used for numerical speed is a corollary that
does require $q + q^{-1}$ to be invertible.)
