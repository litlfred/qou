Two-step in `coulomb-strong-ratio-q-rational.lean`:

1. **Algebraic identity** (`qDiffOverSum_eq_qSqDiff_over_qSqSum`): for any real
   $q \ne 0$,

   $$
     \frac{q - q^{-1}}{q + q^{-1}} = \frac{q^2 - 1}{q^2 + 1}.
   $$

   Closed by `field_simp; ring` — pure-algebraic, generic-ring style.

2. **Transcendental bridge** (`Real.tanh_log_eq_qDiffOverSum`): for any real
   $q > 0$,

   $$
     \tanh(\ln q) = \frac{q - q^{-1}}{q + q^{-1}}.
   $$

   Uses `Real.exp_log` and the definitions of `Real.sinh`, `Real.cosh`,
   `Real.tanh` in Mathlib.

The composite (`prop:coulomb-strong-ratio-q-rational`) is the immediate
corollary: $\tanh(\ln q) = (q^2-1)/(q^2+1)$ for $q > 0$.
