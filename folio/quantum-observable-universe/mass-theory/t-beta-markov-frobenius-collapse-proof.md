## Proof — completing the square

Let $X \in H$ satisfy the constraint $\mathrm{tr}_M(X) = S$.  Write the
decomposition $X = (X - S \cdot 1) + S \cdot 1$ and expand the
Frobenius norm-squared:

$$
\| X \|^2_\tau = \mathrm{tr}_M(X X^\dagger)
              = \mathrm{tr}_M\big((X - S \cdot 1)(X - S \cdot 1)^\dagger\big)
                + S \, \mathrm{tr}_M(X + X^\dagger) - S^2 \, \mathrm{tr}_M(1).
$$

(The scalar $S \cdot 1$ is central and fixed by $\dagger$, so
$(X - S \cdot 1)(X - S \cdot 1)^\dagger = X X^\dagger - S(X + X^\dagger) + S^2 \cdot 1$.
Since $\mathrm{tr}_M(T_w) = \mathrm{tr}_M(T_{w^{-1}})$, the trace is
$\dagger$-invariant, so $\mathrm{tr}_M(X^\dagger) = \mathrm{tr}_M(X) = S$;
applying linearity term by term gives the identity above.)

Substituting the Markov normalisation $\mathrm{tr}_M(1) = 1$ and the
constraint $\mathrm{tr}_M(X) = S$:

$$
\| X \|^2_\tau = \| X - S \cdot 1 \|^2_\tau + 2 S^2 - S^2
             = \| X - S \cdot 1 \|^2_\tau + S^2.
$$

The twisted form is **positive-semi-definite**: in the orthogonal
seminormal form each $\sigma_i$ is real symmetric, so $\dagger$ is the
blockwise transpose and
$\| Y \|^2_\tau = \sum_\lambda y_\lambda \, \| Y_\lambda \|_F^2 \ge 0$,
since every Markov weight $y_\lambda \ge 0$. Therefore

$$
\| X \|^2_\tau \;\ge\; S^2,
$$

with equality iff $\| X - S \cdot 1 \|^2_\tau = 0$, i.e. iff
$X - S \cdot 1$ vanishes on every block with $y_\lambda > 0$. Under
convention D the blocks with $y_\lambda = 0$ are exactly the shapes with
three or more rows, so the minimiser is $S \cdot 1$ up to that radical.
(The untwisted form $\mathrm{tr}_M(X \cdot X)$ cannot be used: it is
negative on $\sigma_1\sigma_2 - \sigma_2\sigma_1 \in H_3$.)

Therefore $T_\beta = S \cdot 1$ is a minimum-Frobenius-norm primal-feasible element, with $\| T_\beta \|^2_\tau = S^2$. $\quad\blacksquare$
