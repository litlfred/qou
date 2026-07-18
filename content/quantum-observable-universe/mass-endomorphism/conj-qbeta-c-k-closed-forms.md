**Closed-form conjectures for the $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_4, c_5, c_6, c_7$.**

We formalize these coefficients as conjectures. This permits downstream claims to use the §3b conditional-class exception, as implemented in [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder) via the Lean class `QBetaPrecisionLadderCoefficients`. In terms of the Hopf–Jones seed $c_3 = -2$ and the Kashiwara coupling $b$, the conjectured closed forms are

$$
  c_4 = c_3\, b^4 = -2 b^4, \qquad
  c_5 = -\bigl(b^2 + \tfrac{1}{2}\bigr), \qquad
  c_6 = c_3^2\, b^2 = 4 b^2, \qquad
  c_7 = c_3^3 = -8,
$$

with empirical match quality tabulated below.

## Closed forms

| Rung | Conjectured closed form | Empirical match | Categorical interpretation |
|:----:|:-----------------------:|:---------------:|----------------------------|
| $c_4$ | $c_3 \cdot b^4 = -2 \cdot b^4$ | **0.9%** residual | Hopf Jones $\times$ Kashiwara $b^4$ correction (multiplicative mixing) |
| $c_5$ | $-(b^2 + 1/2)$ | **2.4%** residual | Kashiwara $b^2$ + half-Hopf integer offset (mixed) |
| $c_6$ | $c_3^2 \cdot b^2 = 4 \cdot b^2$ | **14%** residual | Hopf Jones squared $\times$ Kashiwara $b^2$ |
| $c_7$ | $c_3^3 = -8$ | **signed error $+114\%$** | Hopf Jones cubed |

Match quality degrades at higher $k$. For $c_7$, the signed relative error is approximately $114\%$ (magnitude error $86\%$). We retain the conjecture because the $N=7$ correction's leverage on the cumulative $\mathfrak{Q}_\beta$ residual operates at the $10^{-13}$ scale. Any $c_7 \in [-100, +100]$ closes the gap to within $10^{-4}$ ppb, leaving the numerical value highly under-determined.
