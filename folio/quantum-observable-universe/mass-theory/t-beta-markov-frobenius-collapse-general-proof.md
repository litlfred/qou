## Proof

Let $R$, $A$, $\tau$, $S$, and $X$ be as in the statement: $R$ an ordered field, $A$ a unital $R$-algebra with unit $1_A$, $\tau : A \to R$ an $R$-linear map with $\tau(1_A) = 1$ and $\tau(xy) = \tau(yx)$, positive-semi-definite on squares, and $X \in A$ an element satisfying the constraint $\tau(X) = S$. For $Y \in A$ we abbreviate $Y^2 = Y \cdot Y$.

**Step 1 — centrality of scalars.** For any $S \in R$ the element $S \cdot 1_A$ is central in $A$: the compatibility of the $R$-action with the multiplication gives $(S \cdot 1_A)\,Y = S \cdot Y = Y\,(S \cdot 1_A)$ for every $Y \in A$. In particular $S \cdot 1_A$ commutes with $X$ even when $A$ is non-commutative, and $(S \cdot 1_A)(S \cdot 1_A) = S^2 \cdot 1_A$.

**Step 2 — completing the square.** Expanding the square of $X - S \cdot 1_A$ and collecting the two cross terms via Step 1,

$$
(X - S \cdot 1_A)^2 \;=\; X \cdot X - 2 S \cdot X + S^2 \cdot 1_A .
$$

Applying $\tau$, its $R$-linearity, and the normalisation $\tau(1_A) = 1$,

$$
\tau\bigl((X - S \cdot 1_A)^2\bigr) \;=\; \tau(X \cdot X) - 2 S\, \tau(X) + S^2 ,
$$

equivalently

$$
\tau(X \cdot X) \;=\; \tau\bigl((X - S \cdot 1_A)^2\bigr) + 2 S\, \tau(X) - S^2 .
$$

This identity holds for every $X \in A$ and $S \in R$; neither the constraint nor positivity has been used yet.

**Step 3 — imposing the constraint.** Substituting $\tau(X) = S$ into the identity of Step 2,

$$
\tau(X \cdot X) \;=\; \tau\bigl((X - S \cdot 1_A)^2\bigr) + S^2 .
$$

**Step 4 — the lower bound.** By positive-semi-definiteness on squares, $\tau\bigl((X - S \cdot 1_A)^2\bigr) \ge 0$, so Step 3 gives

$$
S^2 \;\le\; \tau(X \cdot X) ,
$$

which is the asserted bound.

**Step 5 — the equality case.** Assume in addition that $\tau$ is non-degenerate on squares, i.e. $\tau(Y^2) = 0$ implies $Y = 0$.

If $\tau(X \cdot X) = S^2$, then Step 3 forces $\tau\bigl((X - S \cdot 1_A)^2\bigr) = 0$, so non-degeneracy applied to $Y = X - S \cdot 1_A$ gives $X - S \cdot 1_A = 0$, i.e. $X = S \cdot 1_A$.

Conversely, if $X = S \cdot 1_A$, then $X \cdot X = S^2 \cdot 1_A$ by Step 1, hence $\tau(X \cdot X) = S^2\, \tau(1_A) = S^2$ (and the constraint $\tau(X) = S \, \tau(1_A) = S$ holds automatically).

Therefore the lower bound $S^2$ is attained exactly at $X = S \cdot 1_A$. $\blacksquare$

The cyclicity hypothesis $\tau(xy) = \tau(yx)$ is part of what makes $\tau$ a trace and the Frobenius pairing $\langle X, Y \rangle_\tau = \tau(X \cdot Y)$ symmetric; the argument above uses only the $R$-linearity, the normalisation, positivity on squares, and (for uniqueness) non-degeneracy.

## Specialisations

For $A = R$ and $\tau = \mathrm{id}$ this recovers the substrate-model statement, where completing the square reduces to the scalar identity $x^2 = (x - S)^2 + 2 S x - S^2$. The proposition does not apply directly to $A = H_n(R, q)$ with $\tau = \mathrm{tr}_M$ for $n \ge 3$: there $\mathrm{tr}_M(X \cdot X)$ takes negative values (at $X = \sigma_1\sigma_2 - \sigma_2\sigma_1$), and under convention D it is degenerate. The Hecke statement $T_\beta = S \cdot 1_H$, up to the radical, is proved with the twisted form $\mathrm{tr}_M(X \cdot X^\dagger)$ in [Min-Frobenius-norm collapse](t-beta-markov-frobenius-collapse.md).
