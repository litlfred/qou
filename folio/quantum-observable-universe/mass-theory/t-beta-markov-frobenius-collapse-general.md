*Let $R$ be a strict-ordered field. Let $A$ be a unital $R$-algebra. Let $\tau : A \to R$ be an $R$-linear normalised trace ($\tau(1) = 1$, $\tau(xy) = \tau(yx)$). Assume $\tau$ is positive-semi-definite on squares: $0 \le \tau(X \cdot X)$ for all $X \in A$. For any $S \in R$ and $X \in A$ satisfying $\tau(X) = S$, the following properties hold:*
$$
S^2 \;\le\; \tau(X \cdot X).
$$
*If $\tau$ is non-degenerate on squares ($\tau(Y \cdot Y) = 0 \implies Y = 0$), the lower bound is attained if and only if $X = S \cdot 1_A$.*

## Relation to the aether-model version

This proposition lifts [minimum-Frobenius-norm $T_\beta$ collapse](t-beta-markov-frobenius-collapse.md) from the aether model ($A = R$, $\tau = \mathrm{id}$) to the general unital $R$-algebra setting, where $A$ may be non-commutative and infinite-dimensional.

## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ with $\tau = \mathrm{tr}_M$ the hypothesis fails for $n \ge 3$: $\mathrm{tr}_M(X \cdot X) < 0$ at $X = \sigma_1\sigma_2 - \sigma_2\sigma_1 \in H_3$, and under convention D the trace is degenerate as well. The Hecke case is instead proved with the twisted form $\mathrm{tr}_M(X \cdot X^\dagger)$ in [minimum-Frobenius-norm $T_\beta$ collapse](t-beta-markov-frobenius-collapse.md), which gives, up to the radical,
$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H.
$$
The $L^2$-Euclidean coordinate-norm operator and the Markov-Frobenius operator both reproduce the SDP constraint. The observable $c_k$ Taylor coefficients remain invariant.
