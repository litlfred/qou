## Proof — Lagrangian / completing-the-square argument

Let $X \in H$ satisfy the constraint $\mathrm{tr}_M(X) = S$.  Write the
decomposition $X = (X - S \cdot 1) + S \cdot 1$ and expand the
Frobenius norm-squared:

$$
\| X \|^2_\tau = \mathrm{tr}_M(X \cdot X)
              = \mathrm{tr}_M\big((X - S \cdot 1)(X - S \cdot 1)\big)
                + 2 S \, \mathrm{tr}_M(X) - S^2 \, \mathrm{tr}_M(1).
$$

(This is the algebraic identity $X X = (X - S)(X - S) + 2 S X - S^2$
inside any commutative ring, lifted to $H$ via the linearity of
$\mathrm{tr}_M$.  See [`completing_the_square_substrate`](markov-trace-frobenius-selection.lean#L139)
for the substrate-model statement.)

Substituting the Markov normalisation $\mathrm{tr}_M(1) = 1$ and the
constraint $\mathrm{tr}_M(X) = S$:

$$
\| X \|^2_\tau = \| X - S \cdot 1 \|^2_\tau + 2 S^2 - S^2
             = \| X - S \cdot 1 \|^2_\tau + S^2.
$$

The Jones–Markov trace $\mathrm{tr}_M$ is **positive-semi-definite on
squares** (a standard property of the unique normalised trace on
the symmetric semisimple Iwahori–Hecke algebra at generic $q$),
so $\| X - S \cdot 1 \|^2_\tau \ge 0$.  Therefore

$$
\| X \|^2_\tau \;\ge\; S^2,
$$

with equality iff $\| X - S \cdot 1 \|^2_\tau = 0$.  By the
[non-degeneracy](#prop:markov-trace-frobenius-selection) of
$\mathrm{tr}_M$ (Wenzl 1988, Jones 1987), the only $Y \in H$ with
$\mathrm{tr}_M(Y \cdot Y) = 0$ is $Y = 0$; hence $X - S \cdot 1 = 0$, i.e.
$X = S \cdot 1$.

Therefore the minimum-Frobenius-norm primal-feasible element is
$T_\beta = S \cdot 1$, with $\| T_\beta \|^2_\tau = S^2$. $\quad\blacksquare$
