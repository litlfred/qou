> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md)).

**Proposition (algebraic stratification of the $\Phi_q$ tower).**
*Let $\beta \in B_n$ be a braid, and assume pentagon ascension: every stratum $S$ with $|S| \geq 3$ contributes zero at fixed jet level $n$ ([jet-tower remark](#rem:mass-endomorphism-jet-tower) §"Pentagon ascension"). Then the $\Phi_q$-tower admits a purely algebraic stratification by $|S|$:*

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

The statement is conditional on pentagon ascension, which is not proved. Its operator form is the `InterLevelLift` hypothesis of `QOU.LiftingDescent.JetProlongation`, which has no concrete instance. Not proved either: that the $|S|$-grading coincides with the $J^{|S|}/J^{|S|+1}$ grading of the GS confinement filtration.

The algebraic stratification operates strictly pre-$\tau$. It decomposes the mass endomorphism using only discrete categorical data, isolating the structural descent without invoking any hyperbolic or continuous geometry.
