> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md)).

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

If every stratum with $|S| \geq 3$ is zero, one can take $\delta = 0$ and $J_{n+1} = 0$, and the identity holds exactly. The statement is conditional on pentagon ascension, which is not proved. Stated without $\delta$ and $J_{n+1}$, the hypothesis is empty: every sum satisfies it with $\delta = 0$ and $J_{n+1}$ the whole ring. Its content is the pentagon identity that produces $\delta$, and the jet-level tower that defines $J_{n+1}$. Its operator form is the `InterLevelLift` hypothesis of `QOU.LiftingDescent.JetProlongation`, which has no concrete instance. Not proved either: that the $|S|$-grading coincides with the $J^{|S|}/J^{|S|+1}$ grading of the GS confinement filtration.

The algebraic stratification operates strictly pre-$\tau$. It decomposes the mass endomorphism using only discrete categorical data, isolating the structural descent without invoking any hyperbolic or continuous geometry.
