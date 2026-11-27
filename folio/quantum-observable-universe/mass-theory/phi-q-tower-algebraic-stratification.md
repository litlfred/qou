**Proposition (algebraic stratification of the $\Phi_q$ tower).**
*Let $\beta \in B_n$ be a braid, and assume pentagon ascension in the following form ([jet-tower remark](#rem:mass-endomorphism-jet-tower) §"Pentagon ascension"). The sum of the strata with $|S| \geq 3$ equals a correction $\delta_S$ on the strata with $|S| \leq 2$, plus a residual lying in the submodule $J_{n+1}$ of contributions at jet level $n+1$. Then, modulo $J_{n+1}$, the $\Phi_q$-tower admits a purely algebraic stratification by $|S|$, with each summand below read as corrected by $\delta_S$:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl\| \mathrm{tr}_M(\rho(\beta_\emptyset))\bigr\|_F
  \;+\;
  \sum_{|S| = 1} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
  \;+\;
  \sum_{|S| = 2} z^{2} \Phi_q\bigl(\|\hat V_S\|_F\bigr).
$$

*The Frobenius norm $\|\cdot\|_F$ evaluates entirely within the ground ring $\mathbb{Z}[q^{\pm 1/2}]$.*

If every stratum with $|S| \geq 3$ is zero, one can take $\delta = 0$ and $J_{n+1} = 0$, and the identity holds exactly. The statement is conditional on pentagon ascension, which is not proved. Stated without $\delta$ and $J_{n+1}$, the hypothesis is empty: every sum satisfies it with $\delta = 0$ and $J_{n+1}$ the whole ring. Its content is the pentagon identity that produces $\delta$, and the jet-level tower that defines $J_{n+1}$. One candidate for the residual submodule comes from the jet module of order $k$, $(S \otimes S)/I^{k+1}$, where $I = \ker(m : S \otimes S \to S)$. There the residual submodule is $I^{k+1}$. At first order it is $I^2$, and the conclusion is an equality in $J^1(S) = (S \otimes S)/I^2$. The jet order $k$ is not the tower level $n$. The tower iterates first jets, and $J^1(J^1(S))$ is not $(S \otimes S)/I^3$, so $I^{k+1}$ is not $J_{n+1}$. Which submodule is $J_{n+1}$ at tower level $n+1$ is open. The candidate does not show that the $|S| \geq 3$ residual lies in $I^2$, and it does not show that a stratum value lies in $S \otimes S$. Each stratum $\Phi_q(\|\hat V_S\|_F)$ is a scalar in the ground ring. Placed in $S \otimes S$ as a scalar, it lies in $I$ only if it is zero, whenever the ground ring embeds in $S$. So for scalar strata the condition "residual in $I^{k+1}$" is the same as "residual zero". A residual that is nonzero but lies in $I^2$ needs strata that are not scalars, such as jets built from $\hat V_S$ itself rather than from its norm. Such non-scalar jet strata have not yet been constructed, nor has an explicit inter-level jet-prolongation lift been exhibited on concrete algebras. Not proved either: that the $|S|$-grading coincides with the $J^{|S|}/J^{|S|+1}$ grading of the GS confinement filtration.

The algebraic stratification operates strictly pre-$\tau$. It decomposes the mass endomorphism using only discrete categorical data, isolating the structural descent without invoking any hyperbolic or continuous geometry.
