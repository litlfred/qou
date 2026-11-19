# Proof of the canonical $(q^2-1)$ factor

By [the per-block character closed forms](qbeta-per-block-chi-closed-forms.md), each per-block character satisfies $\chi_\lambda(q) = (q^2 - 1) P_\lambda(q)$ for $q > 0$. Substituting these into the weighted sum and factoring out $(q^2 - 1)$ yields the claim by direct substitution and a ring identity. $\square$

## Limitations

- **Concrete inhabitant of the canonical $H_3$ Markov weights.** The dimension-normalisation hypothesis is satisfied by the convention-D weights $y_{(3)} = (q^4+1)/(q^2+1)^2$, $y_{(2,1)} = q^2/(q^2+1)^2$, $y_{(1^3)} = 0$. These are rational in $q$, and their normalisation holds identically as $(q^4+1) + 2q^2 = (q^2+1)^2$. The hypothesis of the proposition is therefore met by the canonical convention-D weights.
- **Higher-order Taylor coefficients of $\Delta\mathrm{tr}_M^{\text{can}}$.** Vanishing at $q = 1$ (order-0) is an immediate consequence. Higher orders depend on the specific behaviour of $y_\lambda(q)$ at $q = 1$, which the dimension-normalisation axiom does not uniquely determine.
- **Bridge to the $c_k$ precision ladder.** While the all-order Convention-D generating function $\mathcal{G}_D(u; q)$ and cumulants $c_2^{(D)}, c_3^{(D)}, c_4^{(D)}$ are established on the canonical trace, constructing the explicit $f$-map to the empirical ladder is unproved; what follows supplies its pre-archimedean $(q^2 - 1)$ divisibility input.
