The [categorical transfer matrix](#def:categorical-transfer-matrix)
$\mathcal{T}(\mathfrak{H})$ arises from a configuration-space picture
of the constituent insertion points, a bi-filtration on the interaction
structure, and the two levels at which a braiding operation may act.
The well-definedness of the equivalence class, and its categorification
to a Lusztig canonical-basis vector, are spelled out below.

**Insertion points and the configuration space.**
The constituent knots $K_i$ are simple objects in $\mathbf{C}$,
each factoring through a tensor power of $V$
([knot factorization](#rem:knot-factorization)):
$K_i \hookrightarrow V^{\otimes 2j_i}$ via the PawLei embedding
$\iota_{j_i}$.  The index $i$ labels the **constituent slot**
rather than the knot type: several slots may carry the same simple object
(e.g.\ a proton has $K_1 = K_2 = T_{2,3}$ for two up quarks).
Each constituent has a
[vertex operator](#def:vertex-operator) $Y(K_i, z_i)$ inserted at
a point $z_i \in \mathcal{S}_p$.  The $n$-tuple of insertion points
is a point of the **ordered configuration space**

$$
  (z_1, \ldots, z_n)  \in 
  \mathrm{Conf}_n(\mathcal{S}_p)
  = 
  \bigl\{(z_1, \ldots, z_n) \in \mathcal{S}_p^{n}
  : z_i \neq z_j \text{ for } i \neq j\bigr\}.
$$

The ordering matches the constituent list of
$\mathfrak{H} = [K_1, \ldots, K_n]$; identical knot types occupy
distinct points on $\mathcal{S}_p$.  The constraint $z_i \neq z_j$
is the source of OPE singularities $(z_i - z_j)^{-k}$ — it is
what distinguishes two copies of the same knot within a single
fibre.

These insertion points are **not free** after the first crossing:
the link $\mathcal{L}$ encoding the internal entanglement
imposes algebraic relations among them.  Concretely, each
Hopf link between $K_i$ and $K_j$ constrains the pair
$(z_i, z_j)$ via the OPE singularity --- the Hecke relation
$(T - q)(T + q^{-1}) = 0$ evaluated at the collision
$z_i \to z_j$.

**Interaction filtration.**
The configuration space algebra carries a **bi-filtration** reflecting
the two sources of structure in the Reeb flow
([observation braid](#rem:observation-braid)):

1. **Ascending (jet prolongation).**  The brane tower
   $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
   ([jet prolongation](#prop:jet-prolongation)) grows with each
   Planck step.  At step $k$, the configuration space lifts to
   the $k$-th jet: insertion points acquire $k$-th order Taylor data,
   and knots with crossing number $\leq k$ become encodable
   ([jet-Planck steps](#rem:jet-planck-steps)).  A configuration
   $\mathcal{S}_0 = \sum_i (p_i, H_i)$
   ([bundle initial conditions](#def:bundle-initial-conditions))
   at any reference point in the affine chart may contain
   arbitrarily many constituents --- including hadrons and photons
   ($K = \varnothing$) --- each carrying only zeroth-order fibre data.
   The subsequent configurations $\mathcal{S}_1, \mathcal{S}_2, \ldots$
   represent the forward light cone of interactions from that
   reference point; $\mathcal{S}_{-1}, \mathcal{S}_{-2}, \ldots$
   represent the backward light cone (undoing computation).

2. **Descending (Hecke relations).**  Within a given jet level,
   each crossing between slots $i$ and $j$ adds a Hecke relation
   $(T - q)(T + q^{-1}) = 0$ to an **interaction ideal**
   $I_k \subset \mathcal{O}(\mathrm{Conf}_n(\mathcal{S}_p))$.  The
   ideals are nested: $I_1 \subset I_2 \subset \cdots \subset I_m$,
   so relations from earlier crossings are **never forgotten**.
   The quotient $\mathcal{O}_n / I_k$ shrinks monotonically --- the
   insertion points become more constrained with each interaction.

The two directions are complementary: jet prolongation **opens** new
degrees of freedom (higher-order Taylor coefficients, heavier knot
types), while Hecke relations **close** them (correlating the
insertion points that have interacted).  The information-theoretic
content of a hadron is the balance between these two: $\eta_q$
$q$-bits of information per step
([operational entropy](#def:operational-entropy)) measures the net
rate at which the ascending tower outruns the descending constraints.

**Two levels of braiding operation.**
A braiding operation on $\mathfrak{H}$ can be described at two levels:

1. **Constituent level.**  Operate on the insertion points
   $(z_1, \ldots, z_n)$ individually.  A crossing
   between $K_i$ and $K_j$ applies the vertex operator
   $Y(\sigma_k, z_k)$ at the relevant generator $\sigma_k$,
   producing a transfer matrix
   $T_{K_i, K_j}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
   that acts on the Hecke chain at $\sigma_k$.

2. **Composite level.**  Operate on the single insertion point
   $z_H$ of the composite knot
   $K_{\mathfrak{H}} = \hat{\beta}_{\mathfrak{H}}$ (the closure of the
   hadron braid word).  The Markov trace of the full braid
   word factors as a product of vertex volumes
   ([Markov trace product](#thm:markov-trace-product)):
   $\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}})) = \prod_i \hat{V}_i(q)$.

**Categorification.**
Under the Brundan–Kleshchev isomorphism
\cite{brundankleshchev2009}, the diagonalisation of $T$ via the
Gröbner–Shirshov filtration $J^\bullet(q)$ structurally categorifies
to the identification of a **Lusztig canonical-basis vector** in the
KLR module category $\mathcal{K}_n$
([crystal-graph realisation](#conj:crystal-graph-realization)): the
equivalence class $\mathcal{T}(\mathfrak{H})$ corresponds to an
indecomposable graded projective KLR module, and its eigenvalue
$\hat{V}(T, q)$ is the graded Euler characteristic of that module
under the Observation Frame $\tau$.
