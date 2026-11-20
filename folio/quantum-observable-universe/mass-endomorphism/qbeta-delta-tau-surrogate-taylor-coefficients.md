**Catalogue (Taylor coefficients of the surrogate $\Delta\mathrm{tr}_M$).**
*The Taylor coefficients $c_n$ of*
[the surrogate trace difference $\Delta\mathrm{tr}_M^{\text{surr}}$](qbeta-per-block-chi-closed-forms.md)
*expanded around the classical point $q = 1$ in the variable
$w = q - 1$, to order 7, are read off the closed form*

$$
  \Delta\mathrm{tr}_M^{\text{surr}}(q) = \frac{
    2q^{17} - 2q^{16} - 5q^{15} + 4q^{14} + 8q^{13} - 9q^{12} - 8q^{11}
    + 9q^{10} + 11q^{9} - 11q^{8} - 9q^{7} + 8q^{6} + 9q^{5} - 8q^{4}
    - 4q^{3} + 5q^{2} + 2q - 2
  }{4 q^{8} (q^2 + q + 1)}
$$

*by substituting $q = 1 + w$ and extracting the coefficient of $w^n$:*

| Order $n$ | Coefficient $c_n$ | Status |
|---|---|---|
| 0 | $0$ | proved |
| 1 | $-5/6$ | proved |
| 2 | $5/6$ | proved |
| 3 | $-23/9$ | proved |
| 4 | $77/18$ | proved |
| 5 | $1349/108$ | proved |
| 6 | $-191/4$ | proved |
| 7 | $26285/162$ | proved |

Every order is now proved, orders 2 and 3 by explicit quotient-rule
derivative towers and orders 4 to 7 by an iterated-Leibniz recurrence on the
polynomial identity $f \cdot D = N$. An independent direct series expansion, which shares no
machinery with the proof, reproduces all eight coefficients.

**Dependence on the intra-nucleon ordering.** The closed form above is the one
induced by the canonical borromean $\chi_{(2,1)}$; the grouped ordering gives
$(-q^{11} + q^{10} - 2q^9 + q^8 + q^6 - q^5 - q^3 + 2q^2 - q + 1)/(4q^5(q^2+q+1))$
and hence $c_3 = -41/9$, $c_4 = 149/18$, $c_5 = -1729/108$, $c_6 = 111/4$,
$c_7 = -3665/81$. **Orders 0, 1 and 2 are the same in both frames**, which is
the load-bearing fact: the classical-point vanishing, the $(q^2-1)$ factor and
the first two Taylor data all survive the reordering, and only orders 3 and
above move.

## Cross-references

- Parent block:
  [Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, antipode pairing, and vanishing at $q = 1$](qbeta-per-block-chi-closed-forms.md)
  (definition of the surrogate and the order-0/order-1 proofs).
