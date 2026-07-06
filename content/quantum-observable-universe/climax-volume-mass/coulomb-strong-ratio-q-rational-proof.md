## Proof (Lean-formalised)

The formalisation in `coulomb-strong-ratio-q-rational.lean` requires two steps:

1. **Algebraic identity** (`qDiffOverSum_eq_qSqDiff_over_qSqSum`). For any real $q \ne 0$,

   $$
     \frac{q - q^{-1}}{q + q^{-1}} = \frac{q^2 - 1}{q^2 + 1}.
   $$

   The tactics `field_simp; ring` close the goal purely algebraically.

2. **Transcendental bridge** (`Real.tanh_log_eq_qDiffOverSum`). For any real $q > 0$,

   $$
     \tanh(\ln q) = \frac{q - q^{-1}}{q + q^{-1}}.
   $$

   This relies on `Real.exp_log` and the Mathlib definitions of `Real.sinh`, `Real.cosh`, and `Real.tanh`.

The composite proposition (`prop:coulomb-strong-ratio-q-rational`) follows immediately: $\tanh(\ln q) = (q^2-1)/(q^2+1)$ for $q > 0$.

## q-usage discipline

We state and prove the identity over $\mathbb{R}_{>0}$, the archimedean substrate-anchor regime. The fibre-level q-rational form $(q-q^{-1})/(q+q^{-1})$ exists as a Laurent-polynomial ratio over $\mathbb{Z}[q,q^{-1}]$. Evaluated at $q = q_0 \in \mathbb{R}_{>0}$, it equals the archimedean term $\tanh(\ln q_0)$. We avoid any $|q| = 1$ step. The identity uses $q^{-1}$ algebraically, not as conjugation, maintaining $q_0$ and $q_0^{-1}$ as real positive points. This satisfies the `lusztig_q_0_imaginary_part_zero` invariant (see [AGENTS.md §7c "Base ring convention"](../../../AGENTS.md)).
