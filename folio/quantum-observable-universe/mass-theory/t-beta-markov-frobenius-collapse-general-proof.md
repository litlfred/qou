## Proof

Let $R$, $A$, $\tau$, $S$, and $X$ be as in the statement: $R$ an ordered field, $A$ a unital $R$-algebra with unit $1_A$, $\tau : A \to R$ an $R$-linear map with $\tau(1_A) = 1$ and $\tau(xy) = \tau(yx)$, $X \mapsto X^\dagger$ an $R$-linear anti-multiplicative map with $1_A^\dagger = 1_A$ and $\tau(X^\dagger) = \tau(X)$, the twisted form $\tau(Y \cdot Y^\dagger)$ positive-semi-definite, and $X \in A$ an element satisfying the constraint $\tau(X) = S$.

**Step 1 — centrality of scalars.** For any $S \in R$ the element $S \cdot 1_A$ is central in $A$: the compatibility of the $R$-action with the multiplication gives $(S \cdot 1_A)\,Y = S \cdot Y = Y\,(S \cdot 1_A)$ for every $Y \in A$. In particular $S \cdot 1_A$ commutes with $X$ even when $A$ is non-commutative, and $(S \cdot 1_A)(S \cdot 1_A) = S^2 \cdot 1_A$.

**Step 2 — completing the square.** By linearity and $1_A^\dagger = 1_A$, $(X - S \cdot 1_A)^\dagger = X^\dagger - S \cdot 1_A$. Expanding with Step 1,

$$
(X - S \cdot 1_A)(X - S \cdot 1_A)^\dagger \;=\; X \cdot X^\dagger - S \cdot X - S \cdot X^\dagger + S^2 \cdot 1_A .
$$

Applying $\tau$, its $R$-linearity, $\tau(X^\dagger) = \tau(X)$, and the normalisation $\tau(1_A) = 1$,

$$
\tau(X \cdot X^\dagger) \;=\; \tau\bigl((X - S \cdot 1_A)(X - S \cdot 1_A)^\dagger\bigr) + 2 S\, \tau(X) - S^2 .
$$

This identity holds for every $X \in A$ and $S \in R$; neither the constraint nor positivity has been used yet.

**Step 3 — imposing the constraint.** Substituting $\tau(X) = S$ into the identity of Step 2,

$$
\tau(X \cdot X^\dagger) \;=\; \tau\bigl((X - S \cdot 1_A)(X - S \cdot 1_A)^\dagger\bigr) + S^2 .
$$

**Step 4 — the lower bound.** By positivity of the twisted form, $\tau\bigl((X - S \cdot 1_A)(X - S \cdot 1_A)^\dagger\bigr) \ge 0$, so Step 3 gives

$$
S^2 \;\le\; \tau(X \cdot X^\dagger) ,
$$

which is the asserted bound.

**Step 5 — the equality case.** Assume in addition that the twisted form is non-degenerate, i.e. $\tau(Y \cdot Y^\dagger) = 0$ implies $Y = 0$.

If $\tau(X \cdot X^\dagger) = S^2$, then Step 3 forces $\tau\bigl((X - S \cdot 1_A)(X - S \cdot 1_A)^\dagger\bigr) = 0$, so non-degeneracy applied to $Y = X - S \cdot 1_A$ gives $X - S \cdot 1_A = 0$, i.e. $X = S \cdot 1_A$.

Conversely, if $X = S \cdot 1_A$, then $X^\dagger = S \cdot 1_A$ and $X \cdot X^\dagger = S^2 \cdot 1_A$ by Step 1, hence $\tau(X \cdot X^\dagger) = S^2\, \tau(1_A) = S^2$ (and the constraint $\tau(X) = S \, \tau(1_A) = S$ holds automatically).

Therefore the lower bound $S^2$ is attained exactly at $X = S \cdot 1_A$. $\blacksquare$

The cyclicity hypothesis $\tau(xy) = \tau(yx)$ is part of what makes $\tau$ a trace and the Frobenius pairing $\langle X, Y \rangle_\tau = \tau(X \cdot Y)$ symmetric; the argument above uses only the $R$-linearity of $\tau$ and $\dagger$ (anti-multiplicativity of $\dagger$ is not used; it is assumed so that the positivity hypothesis is not automatic, since the degenerate map $X \mapsto \tau(X) \cdot 1_A$ would otherwise make $\tau(Y \cdot Y^\dagger) = \tau(Y)^2 \ge 0$ on every algebra), the normalisation, $1_A^\dagger = 1_A$, $\tau(X^\dagger) = \tau(X)$, positivity of the twisted form, and (for uniqueness) its non-degeneracy.

## Specialisations

With $X^\dagger = X$ this is the untwisted statement, and for $A = R$, $\tau = \mathrm{id}$ it reduces to the scalar identity $x^2 = (x - S)^2 + 2 S x - S^2$. For $A = H_n(R, q)$ with $\tau = \mathrm{tr}_M$, the untwisted choice fails for $n \ge 3$ ($\mathrm{tr}_M(X \cdot X) < 0$ at $X = \sigma_1\sigma_2 - \sigma_2\sigma_1$); the anti-involution fixing each $\sigma_i$ gives a positive twisted form, degenerate under convention D, so $T_\beta = S \cdot 1_H$ holds up to its radical.
