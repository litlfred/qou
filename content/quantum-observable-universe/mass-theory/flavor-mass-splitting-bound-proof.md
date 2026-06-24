Two ingredients:

1. **Positivity** (lower bound). By substrate construction,
 $q > 1$ implies $(q-1)^2 > 0$ and $1 - q^{-4} > 0$. Their
 product is positive; division by $3$ preserves the sign. By
 [`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
 the splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ is
 $M_N$ times this positive substrate factor (modulo
 $O((\Delta m / M_N)^2)$, which is below the leading term), so
 the difference is strictly positive.

2. **Upper bound.** The substrate factor satisfies
 $$
     \frac{(q - 1)^2 (1 - q^{-4})}{3}
     \;<\;
     \hbar_q^2 \cdot h_q \cdot [2]_q
     \;=\;
     \frac{(q-1)^2}{q^2} \cdot (q - q^{-1}) \cdot (q + q^{-1})
     \;=\;
     \frac{(q-1)^2 (q^4 - 1)}{q^4}.
   $$
 Both expressions share the numerator $(q-1)^2$; their ratio is
 $$
     \frac{(1 - q^{-4}) / 3}{(q^4 - 1)/q^4}
     \;=\;
     \frac{(q^4 - 1)/(3 q^4)}{(q^4 - 1)/q^4}
     \;=\;
     \frac{1}{3},
   $$
 The substrate factor of the proposition equals $1/3$ of the
 bound expression. Multiplication by $M_N$ preserves the
 inequality; the Skein-side adjustment factor
 $(q^{1/2} + q^{-1/2})/(q + q^{-1}) < 1$ at $q > 1$ tightens the
 bound further but is not required for the strict inequality.
 $\square$
