# Proof of the canonical $(q^2-1)$ factor

By the [per-block character closed forms](qbeta-per-block-chi-closed-forms.md), each per-block character satisfies $\chi_\lambda(q) = (q^2 - 1) P_\lambda(q)$ for $q > 0$. Substituting these into the weighted sum and factoring out $(q^2 - 1)$ yields the claim. $\square$

## Limitations

- **Concrete canonical weights.** The hypothesis is satisfied by the convention-D weights $y_{(3)} = (q^4+1)/(q^2+1)^2$, $y_{(2,1)} = q^2/(q^2+1)^2$, $y_{(1^3)} = 0$. These are rational in $q$ and satisfy the normalisation. The hypothesis of the theorem is therefore met by the canonical weights.
- **Higher-order Taylor coefficients of $\Delta\mathrm{tr}_M^{\text{can}}$.** Vanishing at $q = 1$ (order-0) is an immediate consequence. Higher orders depend on the specific behaviour of $y_\lambda(q)$ at $q = 1$, which the dimension-normalisation axiom does not uniquely determine.
- **Bridge to the $c_k$ precision ladder.** The $f$-map itself remains open. What follows provides pre-archimedean structural input for the $f$-map, rather than completing the derivation.
