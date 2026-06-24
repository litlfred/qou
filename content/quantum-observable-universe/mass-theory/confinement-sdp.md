The scalar [confinement LP](#prop:confinement-lp) is the
diagonal projection of a richer **semidefinite program** over
matrix-valued operators.  The SDP is the actual selection
principle computed by the multi-level pipeline
(`computations/multi_level_sdp.py`,
`sdp_cross_channel.py`, `misdp_cross_channel.py`); the LP
obtains only when every Wedderburn block decouples.

## Primal SDP (matrix operator selection)

**Proposition.**
*Let $n$ be the Hecke strand count at confinement level $\ell$
and let $(\pi_\lambda)_{\lambda \vdash k, k \le n}$ be the
central idempotents projecting onto the Wedderburn blocks of
$H_n(q)$.  Let $T \in \mathrm{End}_R(H_n(R, q))$ be the cost
operator (Markov-trace weighting, or the $q$-Laplacian
resolvent).  The confined operator at $q$ is the solution
$\Phi^* \succeq 0$ of:*

$$
  \min_{\Phi} \quad \langle T, \Phi \rangle
  \qquad (\text{matrix action})
$$

*subject to:*

$$
  \Phi \;\succeq\; 0
  \qquad (\text{global PSD cone})
$$

$$
  \langle \pi_\lambda, \Phi \rangle \;\ge\; 0
  \quad \forall\, \lambda \vdash k,\ k \le n
  \qquad (\text{per-block Frobenius positivity})
$$

$$
  \begin{pmatrix}
    \Phi_{ii} & \Phi_{ij} \\
    \Phi_{ji} & \Phi_{jj}
  \end{pmatrix}
  \;\succeq\; 0
  \quad \forall\, \text{adjacent generator pairs } (i, j)
  \qquad (\text{$2 \times 2$ pair PSD})
$$

$$
  \mathrm{tr}(\Phi) \;=\; n_{\mathrm{target}}
  \qquad (\text{normalisation})
$$

*where the 2$\times$2 blocks range over adjacent pairs $(\sigma_i, \sigma_{i+1})$
in the Hecke generator chain — one block per confinement level from
$\ell = 3$ (baryonic) up to $\ell = 7$ (molecular), as tabulated in
the multi-level SDP infrastructure.*

## Dual SDP (matrix shadow prices)

*The dual program is:*

$$
  \max_{y_0, (y_\lambda)} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to the **matrix inequality**:*

$$
  y_0 \cdot I \;+\; \sum_\lambda y_\lambda \cdot \pi_\lambda \;-\; T
  \;\preceq\; 0
$$

$$
  y_\lambda \ge 0 \quad \forall\, \lambda
$$

*The dual variable $y_0$ is the shadow price of the normalisation
constraint; $(y_\lambda)$ are the per-block shadow prices.
Strong duality holds under Slater's condition (a strictly
feasible $\Phi \succ 0$ exists at generic $q$), and at optimum:*

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

*as a matrix equation.*

## Companion interpretive remarks

The exposition of *why* this SDP is the right object — feasibility
as a Hecke spectral-gap, the active-support reading of the dual,
the relation to the scalar LP, and the integer-restricted MISDP
variant — has been split into four companion remarks so that the
proposition statement above stays minimal:

* [Spectral-gap feasibility](#rem:confinement-sdp-spectral-gap):
  feasibility iff $|q + q^{-1}| > 0$; deconfinement = gap closure.
* [Multi-operator binding](#rem:confinement-sdp-multi-operator):
  active support $\mathcal{S}^*$, binding multiplicity, and why
  complementary slackness is a *matrix* equation.
* [Relation to the scalar LP](#rem:confinement-sdp-vs-lp):
  the LP as the diagonal restriction of the SDP; when each is
  exact.
* [MISDP variant](#rem:confinement-misdp): integer-constrained
  confinement levels.

The geometric face of this proposition — SDP optimality as
Picard--Lefschetz steepest descent, dual variables as thimble
depths — is developed in
the SDP-as-thimble-flow remark below.

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
   [confinement LP](#prop:confinement-lp), with equal primal/dual values.

The Lean sibling encodes the data as `ConfinementSDPData` and states
`confinement_sdp` conditional on `slaterStrictFeasible`; the conic-duality
step is deferred there via `sorry` (`-- Ref: [manuscript]`), pending a
Mathlib SDP strong-duality API. $\square$
