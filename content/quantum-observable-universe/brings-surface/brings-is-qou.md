*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Bring's surface $\Sigma_4$ ([Bring's surface](#def\:brings-surface)) gives rise
to a quantum observable universe over $R$ (with $30 \in R^{\times}$):

1. *Quantum universe.*  Set $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_{q}(2))$ over $R$,
   $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the
   Haar state, and $\tau$ the forgetful functor to $R$-$\mathrm{Mod}$.
   The differential calculus $\Omega^1(A)$ is the Woronowicz
   $3$-dimensional calculus.
2. *Observability.*
   $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by the quantum
   Schur lemma: $\mathrm{SU}_q(2)$ has no non-trivial invariants in the
   adjoint representation.
3. *Yekutieli lifting.*  The brane tower satisfies the Yekutieli
   lifting condition ([Yekutieli lifting](#prop\:yekutieli-lifting));
   the obstruction classes $\kappa_n \neq 0$ persist at every level
   by [motivic perpetual obstruction](#conj\:motivic-perpetual-obstruction)
   applied with $\chi(A) = -6$.
4. *Euler characteristic.*  By [QU-to-QOU lifting](#thm\:qu-to-qou),
   $\chi(A) = \mathrm{tr}(\mathrm{id}_A) = 2 - 2g = -6$.
5. *Geometric :refterm[descent]{#descent}* (for $n = 1$, $\dim M_S = 3$):

   $$
     M_S \xrightarrow{ \mathrm{Reeb}} \Sigma_4
     \xrightarrow{\pi} \mathbb{P}(V)
     \xrightarrow{ \mathrm{branch}} \{6 \text{points}\}.
   $$

   The degree-$4$ covering $\pi$ has $6$ branch points with total
   ramification $R_{\mathrm{tot}} = 14$ (Riemann--Hurwitz), and the
   ramification profile is determined by the $S_5$-symmetry.
