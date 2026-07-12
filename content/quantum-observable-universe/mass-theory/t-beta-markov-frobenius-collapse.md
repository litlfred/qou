*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$, equipped with the unique Jones–Markov trace $\mathrm{tr}_M : H \to R$ ([Wenzl–Jones uniqueness theorem](#prop:markov-trace-frobenius-selection)). Equip $H$ with the Frobenius inner product $\langle X, Y \rangle_\tau := \mathrm{tr}_M(X \cdot Y)$. The element of minimum Frobenius norm satisfying the linear constraint $\mathrm{tr}_M(T_\beta) = S$ for a scalar $S \in R$ is:*
$$
\boxed{\; T_\beta = S \cdot 1_H \;}
$$
*with $\| T_\beta \|^2_\tau = S^2$.*

## Corollary — observable c_k invariance

The $\mathfrak{Q}_\beta$ production rule extracts the Taylor coefficients $c_k$ from $\mathrm{tr}_M(T_\beta)(q)$. The constraint $\mathrm{tr}_M(T_\beta) = S = \mathfrak{Q}_\beta / E_0$ is satisfied identically under both the Euclidean $L^2$ coordinate norm and the canonical Markov–Frobenius norm. We have $\mathrm{tr}_M(T_\beta)(q) \equiv S(q)$. The coefficients $c_k$ are invariant:
$$
c_k^{\,L2} = c_k^{\,Markov} = c_k\!\!\left(S(q)\right)
\quad\text{for all } k.
$$
The observables are extracted from the constraint, not from the operator expansion. The norms only differ in selecting the primal-feasible operator $T_\beta \in H_n(R, q)$.

## Categorical reading

Under the Markov–Frobenius norm, $T_\beta = S \cdot 1_H$ is a scalar multiple of the identity. The $q$-dependence flows entirely through $S(q)$. There is no multi-channel SHAPE distributed across the normal-form basis. The Euclidean norm's six-channel spread is an artifact of the coordinate basis. The Markov–Frobenius minimum-norm solution is the canonical choice.
