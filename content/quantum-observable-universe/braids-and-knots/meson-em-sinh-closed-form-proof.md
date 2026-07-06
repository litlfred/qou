## Proof

We prove the equivalence as rational functions of $q$. Expanding $\hbar_q^2 = (1 - q^{-1})^2 = 1 - 2 q^{-1} + q^{-2}$ gives:

$$
  1 + \hbar_q - \tfrac{1}{2}\hbar_q^2
  = 1 + (1 - q^{-1}) - \tfrac{1}{2}(1 - 2 q^{-1} + q^{-2})
  = \tfrac{3}{2} - \tfrac{1}{2} q^{-2}
  = \frac{3 - q^{-2}}{2}.
$$

Multiplying numerator and denominator by $q^2$ yields $(3 q^2 - 1)/(2 q^2)$. In Lean, `field_simp; ring` closes the goal. $\square$
