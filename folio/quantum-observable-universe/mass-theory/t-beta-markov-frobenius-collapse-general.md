*Let $R$ be a strict-ordered field. Let $A$ be a unital $R$-algebra. Let $\tau : A \to R$ be an $R$-linear normalised trace ($\tau(1) = 1$, $\tau(xy) = \tau(yx)$). Let $X \mapsto X^\dagger$ be an $R$-linear map on $A$ with $1^\dagger = 1$ and $\tau(X^\dagger) = \tau(X)$. Assume the twisted form is positive-semi-definite: $0 \le \tau(Y \cdot Y^\dagger)$ for all $Y \in A$. For any $S \in R$ and $X \in A$ satisfying $\tau(X) = S$:*
$$
S^2 \;\le\; \tau(X \cdot X^\dagger).
$$
*If the twisted form is non-degenerate ($\tau(Y \cdot Y^\dagger) = 0 \implies Y = 0$), the lower bound is attained if and only if $X = S \cdot 1_A$.*

Taking $X^\dagger = X$ recovers the untwisted statement $S^2 \le \tau(X \cdot X)$ under positivity of $\tau$ on squares.

## Relation to the substrate-model version

This proposition lifts [Min-Frobenius-norm collapse: T_β = S · 1 under the canonical Markov-trace inner product on H_n(R, q)](t-beta-markov-frobenius-collapse.md) from the substrate model ($A = R$, $\tau = \mathrm{id}$) to the general unital $R$-algebra setting, where $A$ may be non-commutative and infinite-dimensional.

## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ with $\tau = \mathrm{tr}_M$, take $\dagger$ to be the $R$-linear anti-involution fixing each $\sigma_i$. In the orthogonal seminormal form $\mathrm{tr}_M(Y \cdot Y^\dagger) = \sum_\lambda y_\lambda \,\|Y_\lambda\|_F^2 \ge 0$, so the positivity hypothesis holds. The untwisted choice $\dagger = \mathrm{id}$ does not work for $n \ge 3$: $\mathrm{tr}_M(X \cdot X) < 0$ at $X = \sigma_1\sigma_2 - \sigma_2\sigma_1 \in H_3$. Under convention D the twisted form is degenerate, with radical the sum of the Wedderburn blocks of shapes with three or more rows, so the minimiser
$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H
$$
is unique only up to that radical. The $L^2$-Euclidean coordinate-norm operator and the Markov-Frobenius operator both reproduce the SDP constraint. The observable $c_k$ Taylor coefficients remain invariant.
