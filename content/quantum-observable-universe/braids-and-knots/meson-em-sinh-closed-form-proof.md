## Proof

The four expressions are equal as rational functions of $q$ over any
field with $q \ne 0$. Starting from the leftmost, expand
$\hbar_q^2 = (1 - q^{-1})^2 = 1 - 2 q^{-1} + q^{-2}$, so

$$
  1 + \hbar_q - \tfrac{1}{2}\hbar_q^2
  = 1 + (1 - q^{-1}) - \tfrac{1}{2}(1 - 2 q^{-1} + q^{-2})
  = \tfrac{3}{2} - \tfrac{1}{2} q^{-2}
  = \frac{3 - q^{-2}}{2}.
$$

Multiplying numerator and denominator by $q^2$ gives
$(3 q^2 - 1)/(2 q^2)$. The Lean formalisation closes each step with
`field_simp; ring`. $\square$
