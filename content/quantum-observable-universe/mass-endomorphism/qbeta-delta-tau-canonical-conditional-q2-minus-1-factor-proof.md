# Proof of the canonical $(q^2-1)$ factor

By [`chi_blocks_have_q2_minus_1_factor`](qbeta-per-block-chi-closed-forms.md), each per-block character satisfies $\chi_\lambda(q) = (q^2 - 1) P_\lambda(q)$ for $q > 0$. Substituting these into the weighted sum and factoring out $(q^2 - 1)$ yields the claim. The Lean proof uses direct substitution and a ring identity. $\square$

## Limitations

- **Concrete instance of `CanonicalMarkovWeightsH3`.** The formalisation of canonical $\sqrt q$-bearing Wenzl weights requires Markov-parameter $\sqrt q$ handling beyond the `ring` tactic. This theorem is rigorous conditionally on such an instance existing.
- **Higher-order Taylor coefficients of $\Delta\tau_M^{\text{can}}$.** Vanishing at $q = 1$ (order-0) is an immediate consequence. Higher orders depend on the specific behaviour of $y_\lambda(q)$ at $q = 1$, which the dimension-normalisation axiom does not uniquely determine.
- **Bridge to the $c_k$ precision ladder.** The $f$-map keystone remains open (see [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)). This block provides pre-archimedean structural input for the $f$-map, rather than completing the derivation.
