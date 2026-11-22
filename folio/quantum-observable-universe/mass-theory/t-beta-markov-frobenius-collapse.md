*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$, equipped with the unique Jones–Markov trace $\mathrm{tr}_M : H \to R$ ([Wenzl–Jones uniqueness theorem](#prop:markov-trace-frobenius-selection)). Let $R$ be ordered, $q > 0$, and let $X \mapsto X^\dagger$ be the $R$-linear anti-involution fixing each $\sigma_i$. Equip $H$ with the Frobenius form $\langle X, Y \rangle_\tau := \mathrm{tr}_M(X \cdot Y^\dagger)$. An element of minimum Frobenius norm satisfying the linear constraint $\mathrm{tr}_M(T_\beta) = S$ for a scalar $S \in R$ is:*
$$
\boxed{\; T_\beta = S \cdot 1_H \;}
$$
*with $\| T_\beta \|^2_\tau = S^2$. The minimiser is unique up to the radical of $\langle\,\cdot\,,\cdot\,\rangle_\tau$, which under convention D is the sum of the Wedderburn blocks of shapes with three or more rows.*

## Why the twist $Y^\dagger$ is needed

The untwisted form $\mathrm{tr}_M(X \cdot Y)$ is not positive on $H_n$ for $n \ge 3$. In $H_3$ take $X = \sigma_1\sigma_2 - \sigma_2\sigma_1$. Then $\mathrm{tr}_M(X) = 0$ and
$$
\mathrm{tr}_M(X \cdot X) \;=\; -\,\frac{2\,(q^4 + q^2 + 1)}{(q^2+1)^2} \;<\; 0
\qquad (q > 0),
$$
so $\mathrm{tr}_M\bigl((S\cdot 1 + tX)^2\bigr) = S^2 + t^2\,\mathrm{tr}_M(X^2)$ is unbounded below in $t$ and has no minimum. In the orthogonal seminormal form every $\sigma_i$ is a real symmetric matrix, so $\dagger$ is the blockwise transpose and $\mathrm{tr}_M(X X^\dagger) = \sum_\lambda y_\lambda \,\| X_\lambda \|_F^2 \ge 0$ because every Markov weight $y_\lambda$ is non-negative.

## Corollary — observable c_k invariance

The $\mathfrak{Q}_\beta$ production rule extracts the Taylor coefficients $c_k$ from $\mathrm{tr}_M(T_\beta)(q)$. The constraint $\mathrm{tr}_M(T_\beta) = S = \mathfrak{Q}_\beta / E_0$ is satisfied identically under both the Euclidean $L^2$ coordinate norm and the canonical Markov–Frobenius norm. Then $\mathrm{tr}_M(T_\beta)(q) \equiv S(q)$. The coefficients $c_k$ are invariant:
$$
c_k^{\,L^2} = c_k^{\,\mathrm{Markov}} = c_k\!\!\left(S(q)\right)
\quad\text{for all } k.
$$
The observables are extracted from the constraint, not from the operator expansion. The norms only differ in selecting the primal-feasible operator $T_\beta \in H_n(R, q)$.

## Categorical reading

Under the Markov–Frobenius norm, $T_\beta = S \cdot 1_H$ is a scalar multiple of the identity. The $q$-dependence flows entirely through $S(q)$. There is no multi-channel SHAPE distributed across the normal-form basis. The Euclidean norm's six-channel spread is an artifact of the coordinate basis. The Markov–Frobenius minimum-norm solution is the canonical choice.
