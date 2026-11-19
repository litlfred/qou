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

| Order $n$ | Coefficient $c_n$ | Derivation method |
|---|---|---|
| 0 | $0$ | classical-point vanishing at $q = 1$ |
| 1 | $-5/6$ | first derivative at $q = 1$ |
| 2 | $5/6$ | explicit quotient-rule derivative tower |
| 3 | $-23/9$ | explicit quotient-rule derivative tower |
| 4 | $77/18$ | iterated-Leibniz recurrence on $f \cdot D = N$ |
| 5 | $1349/108$ | iterated-Leibniz recurrence on $f \cdot D = N$ |
| 6 | $-191/4$ | iterated-Leibniz recurrence on $f \cdot D = N$ |
| 7 | $26285/162$ | iterated-Leibniz recurrence on $f \cdot D = N$ |

Every order is established analytically: orders 2 and 3 by explicit quotient-rule
derivative towers and orders 4 to 7 by an iterated-Leibniz recurrence on the
polynomial identity $f \cdot D = N$. The computational witness independently reproduces all
eight coefficients by direct series expansion.

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
  [per-block character closed forms](qbeta-per-block-chi-closed-forms.md)
  (surrogate definition and order-0/order-1 derivatives).
- Witness JSON:
  [`qbeta-c3-multiblock-recursion-attack.witness.json`](../../../computations/qbeta/qbeta-c3-multiblock-recursion-attack.witness.json).
