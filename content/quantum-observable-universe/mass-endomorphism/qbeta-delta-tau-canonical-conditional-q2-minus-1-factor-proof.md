**Proof.** By
[`chi_blocks_have_q2_minus_1_factor`](qbeta-per-block-chi-closed-forms.md),
each per-block character satisfies $\chi_\lambda(q) = (q^2 - 1) \cdot P_\lambda(q)$
for $q > 0$. Substituting and factoring out $(q^2 - 1)$ from the
weighted sum gives the claim. The Lean proof is a direct substitution
plus ring identity. $\square$
## Limitations of this block

- **A concrete instance of `CanonicalMarkovWeightsH3`.** The canonical
  $\sqrt q$-bearing Wenzl weights are still open at the formalisation
  level (require Markov-parameter $\sqrt q$ handling beyond `ring`).
  This block is rigorous *conditional* on such an instance existing.
- **The order-1+ Taylor coefficients of $\Delta\tau_M^{\text{can}}$.**
  Vanishing at $q = 1$ (order-0) is the immediate consequence; higher
  orders depend on the specific $y_\lambda(q)$ behaviour at $q = 1$,
  which the dimension-normalisation axiom alone does not pin down.
- **A bridge to the c_k precision ladder.** The f-map keystone (per
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md))
  is still open; this block contributes pre-archimedean structural
  input the f-map would consume, not a closure step.
