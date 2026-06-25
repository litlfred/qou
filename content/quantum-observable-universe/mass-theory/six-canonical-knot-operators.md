**Proposition (conditional on
[`def:q-reeb-flow-on-color-coords`](#def:q-reeb-flow-on-color-coords)).**
*Let $\mathcal{R}_p$ be the Reeb bundle over the exceptional
divisor at brane point $p$, equipped with the color-sector
coordinates $\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$
([color-sector coordinates](#def:color-sector-coords)) and the
$q$-Reeb flow $\phi^q_t$
([$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)).
For each of the six elements $w \in S_3 = \langle \sigma_1, \sigma_2 \mid
\sigma_i^2 = \mathbf{1},\; \sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2 \rangle$
the corresponding braid word $\beta_w \in B_3$ generates a unique
trajectory across $\mathcal{R}_p$ whose boundary footprint
realises $w$ as a Galois permutation of the colour tubes on the
ramified output disc.*

The six trajectories are tabulated below.  Each row specifies
(i) the braid word $\beta_w$, (ii) the per-sector flow rate
$\dot\psi^{(s)}$, (iii) the explicit trajectory in color-sector
coordinates, and (iv) the induced boundary permutation $\sigma_w$
on the colour-tube triple $(r,g,b)$.

See [Table](#tbl:six-canonical-knot-operators-table-data).

**Sketch of proof.**

1. **Identity.**  When no braid generator acts, the localisation
   rule of [`def:q-reeb-flow-on-color-coords`](#def:q-reeb-flow-on-color-coords)
   reduces all three sectors to spectators, so each strand traces
   the meridian $\psi^{(s)} = \mathrm{const}$ from the south
   foundry to the north foundry.  The boundary footprint is the
   identity permutation.

2. **Adjacent transpositions $\sigma_1, \sigma_2$.**  By the
   two-strand localisation rule, $\sigma_1$ activates the red and
   green sectors with equal and opposite angular rates (the
   centre of mass $\psi^{(r)} + \psi^{(g)}$ is conserved by the
   $\mathrm{SU}(2)$ structure of the Hecke action; the difference
   $\psi^{(r)} - \psi^{(g)}$ accumulates a phase of $\pi$, the
   half-rotation that distinguishes the two Hecke eigenvalues
   $\pm q^{\pm 1/2}$).  At the north foundry, the red and green
   sectors have swapped angular positions; the blue spectator is
   unchanged.  This realises the transposition $(rg)$ on the
   output ramified disc.

3. **Garside $\sigma_1\sigma_2\sigma_1$.**  Decompose the
   latitude interval $[0,\pi]$ into three equal sub-intervals,
   each carrying one adjacent-transposition flow.  The braid
   relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$
   guarantees that the two flow sequences produce the same
   boundary permutation $(rb)$ — the non-adjacent transposition —
   despite traversing different intermediate states of the green
   sector.  Geometrically, the green tube is displaced into the
   middle and returned; the red and blue tubes are exchanged via
   the compound flow through it.  This is the explicit ODE-level
   verification of the Garside-element identity in
   [Garside element as compound Reeb flow](#rem:garside-as-compound-flow).

4. **3-cycles $\sigma_1\sigma_2$ and $\sigma_2\sigma_1$.**  These
   braid words activate the *global* vortex sector of the Reeb
   flow: all three sectors rotate uniformly with rate $+q$
   (positive chirality) or $-q$ (negative chirality).  The
   trajectory traces a right-handed (resp. left-handed) helix
   along a Heegaard torus inside $\mathcal{R}_p \cong S^3$.  At
   the north foundry the entire colour triple has cyclically
   permuted, realising $(rgb)$ or $(rbg)$.

The six trajectories cover the six elements of $S_3$ exhaustively
because the braid relation forces $\sigma_1\sigma_2\sigma_1 =
\sigma_2\sigma_1\sigma_2$ and $\sigma_i^2 = \mathbf{1}$
(after passing to $S_3 = B_3/\langle\sigma_i^2\rangle$).  The
six boundary permutations are pairwise distinct, so the
correspondence $w \mapsto \beta_w$ is a bijection onto $S_3$.
This recovers the $S_3$ holonomy of $\rho: B_3 \to \mathrm{SU}(2)$
from [$\rho$ as $S_3$ holonomy on Lagrange resolvents](#rem:rho-s3-holonomy-exposition)
*explicitly as a trajectory computation* in the Reeb bundle. $\square$

**Why this is conditional.**  The proof above takes the
[$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)
class as given: it uses only the additive composition rule and
the two-strand localisation rule.  The underlying differential-
geometric existence of $\phi^q_t$ — the integrability of $\xi_q$,
its smoothness, and the convergence of the formal flow to a
continuous group of automorphisms of $\mathcal{R}_p$ — is the
content of the class hypothesis on the geometric side.  The
*combinatorial* content of the boundary-permutation table is
discharged by the Lean theorem
`QOU.CategoricalReeb.boundary_perm_realises_S3`
(which combines `boundaryPerm_injective`, `boundaryPerm_bijective`,
and the count `canonical_braid_count_six`: the six constructors
of `CanonicalBraid` form a nodup list of length six, so the
induced map to permutations of `ColorSector` is an injection
onto a set of size six $= |S_3|$).  This Lean theorem is
unconditional — it is a finite case check on six branches —
because the boundary-permutation table is itself purely
combinatorial; the geometric identification of those
permutations as the boundary footprints of the $q$-Reeb-flow
trajectories is the content of the manuscript prose above and
remains conditional on
[$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords).

**Volume corollaries.**  The two 3-cycle trajectories lie on a
Heegaard torus, so their knot complement contains a Seifert-fibered
piece with $V_{\mathrm{hyp}} = 0$
([torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)).
The Garside trajectory does not factor through any Heegaard
torus and contributes a non-trivial hyperbolic piece to the
JSJ decomposition
([hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb));
this is the geometric origin of the mass-versus-volume dichotomy
exploited by
[mass-volume factorization](#conj:mass-volume-factorization).
