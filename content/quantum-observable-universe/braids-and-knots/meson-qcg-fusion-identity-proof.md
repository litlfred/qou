## Proof

Using $[n]_q = (q^n - q^{-n})/(q - q^{-1})$, we clear denominators by multiplying both sides by $(q - q^{-1})^2$. The identity becomes:

$$
  (q^3 - q^{-3})(q^4 - q^{-4})
  \;=\;
  (q - q^{-1}) \cdot
  \bigl((q^2 - q^{-2}) + (q^4 - q^{-4}) + (q^6 - q^{-6})\bigr).
$$

This ring identity holds over any field with $q \ne 0$. In Lean, `ring` closes the goal. $\square$
