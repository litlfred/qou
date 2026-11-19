## Proof (sketch)

The program is a semidefinite program over the symmetric cone
$\mathbb{S}_+^N$, $N = \dim_R H_n(R, q)$, and existence/attainment of
the optimum is standard convex duality.

1. **The feasible set is a compact spectrahedron and the objective
   is bounded below.** The normalisation $\mathrm{tr}(\Phi) = n_{\mathrm{target}}$
   together with $\Phi \succeq 0$ confines $\Phi$ to a bounded slice of
   the PSD cone, on which the linear objective $\langle T, \Phi\rangle$
   attains its minimum $\Phi^\star \succeq 0$.

2. **Slater $\Rightarrow$ strong duality.** Under the strict-feasibility
   hypothesis (`ctx.slaterStrictFeasible`: a $\Phi_0 \succ 0$ strictly
   satisfying every per-block and $2\times2$ pair constraint, available
   at generic $q$ where $|q + q^{-1}| > 0$), the conic-duality theorem
   gives strong duality — the dual SDP is solvable, $\mathrm{primal} =
   \mathrm{dual}$, and the complementary-slackness identity
   $\Phi^\star(y_0^\star I + \sum_\lambda y_\lambda^\star \pi_\lambda - T) = 0$
   certifies optimality (\cite{boyd-vandenberghe-2004}, §5.9). The shadow prices
   $y_\lambda^\star \ge 0$ are exactly the per-block Frobenius-positivity
   duals of the LP/SDP witness contract.

3. **The scalar LP is the diagonal restriction.** When every Wedderburn
   block decouples (no off-diagonal pair constraint binds), the matrix
   SDP collapses block-by-block to the
   [confinement LP](#prop:confinement-lp), with equal primal/dual values. $\square$
