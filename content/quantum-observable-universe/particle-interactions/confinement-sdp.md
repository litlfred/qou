The scalar [confinement LP](#prop:confinement-lp) is the diagonal
projection of a richer **semidefinite program** over matrix-valued
operators.  The SDP is the actual selection principle computed by
the multi-level pipeline
(`folio-assistant/computations/multi_level_sdp.py`,
`sdp_cross_channel.py`, `misdp_cross_channel.py`); the LP obtains
only when every Wedderburn block decouples.

### Spectral-gap feasibility (algebraic form)

From the categorical origin of the crossing energy
([crossing energy](#def:crossing-energy)), the SDP's feasibility is
equivalent to a **Hecke spectral-gap condition**: the feasible cone is
non-empty if and only if

$$
  \Delta_{\sigma}(q) \;:=\; \lvert q + q^{-1} \rvert \;>\; 0,
$$

i.e.\ the Hecke generator $\sigma$ on $V \otimes V$ has non-degenerate
eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$.  The dual
certificate at optimum is the pair of Jones--Wenzl projectors
onto the two isotypic components; the SDP's complementary slackness
matrix is their orthogonal decomposition.  **Deconfinement $=$
spectral-gap closure:** $\Delta_{\sigma}(q) \to 0$ at $q = \pm i$ (Kauffman
bracket degeneracy) and the feasible cone collapses.

The SDP retains its role as a numerical certificate at given $q$, but
its existence is guaranteed by the categorical volume constraint and
can be produced from the eigenvalue structure alone without invoking
continuous optimisation.

## Primal SDP (matrix operator selection)

**Proposition.**
*Let $n$ be the Hecke strand count at confinement level $\ell$ and
let $(\pi_\lambda)_{\lambda \vdash k, k \le n}$ be the central
idempotents projecting onto the Wedderburn blocks of $H_n(q)$.
Let $T \in \mathrm{End}_R(H_n(R, q))$ be the cost operator
(Markov-trace weighting, or the $q$-Laplacian resolvent).  The
confined operator at $q$ is the solution $\Phi^* \succeq 0$ of:*

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
  \qquad (\text{2×2 pair PSD})
$$

$$
  \mathrm{tr}(\Phi) \;=\; n_{\mathrm{target}}
  \qquad (\text{normalisation})
$$

*where the 2×2 blocks range over adjacent pairs $(\sigma_i, \sigma_{i+1})$
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
Strong duality holds under Slater's condition (a strictly feasible
$\Phi \succ 0$ exists at generic $q$).*

## Complementary slackness is a matrix equation

*At optimum:*

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

*This is a **matrix** equality, not a sum of scalar complementary
slackness relations.  Its rank counts the **active dual support**
— the number of Wedderburn blocks simultaneously coupled at the
optimum.  When the rank exceeds one, the confined state is a sum
of operators from distinct blocks, which is what the
`electron-shell-ilp` witness observes when it reports "electrons
alternate between $\sigma_1^{-1}$ and $\sigma_0^{-1}$": those are
two tight dual blocks at the same $\Phi^*$.*

## Multi-operator binding

*For any two confined particles
$P_1, P_2$ ([confined particle](#def:confined-particle))
whose composite satisfies the SDP, the **binding subword** is:*

$$
  W_{\mathrm{bind}}
  \;=\;
  \sum_{\lambda \in \mathcal{S}^*} y_\lambda^* \cdot \pi_\lambda \cdot \Phi^*
$$

*where $\mathcal{S}^* = \{\lambda : y_\lambda^* > 0\}$ is the
**active support** at optimum.  The cardinality
$|\mathcal{S}^*| \ge 1$ is the **binding multiplicity**:
$|\mathcal{S}^*| = 1$ recovers the scalar LP regime
(single-channel binding); $|\mathcal{S}^*| \ge 2$ is the generic
multi-operator regime and includes all shell-closure and
magic-number configurations.*

## Relation to the scalar LP

*The scalar [confinement LP](#prop:confinement-lp) is obtained by
restricting $\Phi$ to the diagonal span of the NF basis
$\{b_i\}$ and dropping the 2×2 pair blocks.  Equivalently: the LP
is the SDP with the rank-1 restriction $\Phi = \mathrm{diag}(x)$
and the simplification $\pi_\lambda \mapsto \mathbf{1}_\lambda$
(indicator vector).  The LP is exact when every Wedderburn block is
one-dimensional (no cross-channel coupling); in general it is a
**lower bound** on the SDP and misses the multi-operator binding
structure.*

## MISDP (mixed-integer SDP)

*When operator counts are constrained to integers — as in the
confinement hierarchy at levels $\ell \le 3$ where crossing
multiplicities must be integral — the feasible region becomes
$\Phi \succeq 0 \wedge \mathrm{rank}\text{-content}(\Phi)
\in \mathbb{Z}_{\ge 0}^{|\mathcal{S}|}$.  The MISDP is solved
by continuous SDP relaxation plus branch-and-cut (see
`misdp_cross_channel.py`), matching the confinement framework
at every level of the hierarchy.*
