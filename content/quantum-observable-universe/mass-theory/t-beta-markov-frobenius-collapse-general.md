**Proposition (Min-Frobenius-norm collapse — general unital R-algebra).**
*Let $R$ be a strict-ordered field. Let $A$ be a unital $R$-algebra. Let $\tau : A \to R$ be an $R$-linear normalised trace ($\tau(1) = 1$, $\tau(xy) = \tau(yx)$). Assume $\tau$ is positive-semi-definite on squares: $0 \le \tau(X \cdot X)$ for all $X \in A$. For any $S \in R$ and $X \in A$ satisfying $\tau(X) = S$, we have:*
$$
S^2 \;\le\; \tau(X \cdot X).
$$
*If $\tau$ is non-degenerate on squares ($\tau(Y \cdot Y) = 0 \implies Y = 0$), the lower bound is attained if and only if $X = S \cdot 1_A$.*

## Relation to the substrate-model version

This proposition lifts [`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md) from the substrate model ($A = R$, $\tau = \mathrm{id}$) to the general unital $R$-algebra setting, where $A$ may be non-commutative and infinite-dimensional.

## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ at generic $q > 0$ with $\tau = \tau_M$, this proposition identifies the canonical SDP-min-Frobenius-norm operator for the constraint $\tau_M(T_\beta) = S$:
$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H.
$$
The $L^2$-Euclidean coordinate-norm operator and the Markov-Frobenius operator both reproduce the SDP constraint. The observable $c_k$ Taylor coefficients remain invariant.
