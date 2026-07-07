<!-- FILE_START: descent-intro.md -->
The :refterm[descent]{#descent} machinery connects the infinite brane tower to finite-dimensional
geometry.  Given a quantum observable universe $(\mathbf{C}, A, \tau)$ with
brane tower $\{A_n\}_{n \geq 0}$
([recursive brane tower](#def:recursive-brane-tower)), the :refterm[descent]{#descent} lemma
([:refterm[descent]{#descent} lemma](#lem:descent)) shows that each level $A_n$ inherits the
full QOU structure from $A$.  The :refterm[descent]{#descent} involution
([:refterm[descent]{#descent} involution](#def:descent-involution)) then splits each $A_n$ into
eigenspaces whose direct limit recovers the physical algebra.  This section
develops the :refterm[descent]{#descent} involution, its eigenspace decomposition, and the
mass-decomposition formula that results.

The arc proceeds in three movements.  We first record the existence
and uniqueness of the descent involution at each tower level — the
involutive splitting is forced by the fixed point of the brane
recursion.  We then exhibit the eigenspace decomposition
$A_n = A_n^+ \oplus A_n^-$ and identify the $+$-eigenspace as the
*physical* part of the algebra: the part that survives the
classical limit and feeds the mass observables.  The closing blocks
of the section assemble these per-level decompositions into the
mass-decomposition formula, which the next section's cosimplicial
machinery promotes into a genuine higher-categorical structure.
<!-- FILE_END: descent-intro.md -->

<!-- FILE_START: descent-eigenspaces.md -->
The :refterm[descent]{#descent} involution $\hat{\tau}_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution))
decomposes the level-$(n{+}1)$ endomorphism algebra into a direct sum

$$
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
  = 
  \mathcal{A}_{n+1}^{\mathrm{desc}}  \oplus  \mathcal{A}_{n+1}^{\mathrm{trans}},
$$

where $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}_n$ is the
descended subalgebra (endomorphisms that factor through level $n$) and
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat{\tau}_n$ is the *transient
complement* (genuinely new endomorphisms at level $n{+}1$).  The
([algebraic filter](#rem:algebraic-filter)) refines this decomposition:

1. The bosonic (longitudinal) modes lifted from level $n$ lie entirely in
   $\mathcal{A}_{n+1}^{\mathrm{desc}}$: they commute with the curvature
   and survive every round-trip through the tower.
2. The fermionic (ladder) modes at level $n{+}1$ split between the two
   summands; those in $\mathcal{A}_{n+1}^{\mathrm{trans}}$ are the modes
   created by the jet prolongation that have no pre-image at level $n$.
<!-- FILE_END: descent-eigenspaces.md -->

<!-- FILE_START: descent-eigenspaces-su2.md -->
Continuing the [:refterm[descent]{#descent} involution for SU(2)](#ex:descent-involution-su2), we compute the [:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces) of $\hat{\tau}$ on $\mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))$.

**The splitting.** The idempotent $\hat{\tau}$ splits the $6$-dimensional endomorphism algebra into two complementary subspaces:

$$
  \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))
  =  \mathfrak{A}^{\mathrm{desc}}  \oplus  \mathfrak{A}^{\mathrm{trans}},
$$

where $\mathfrak{A}^{\mathrm{desc}} = \mathrm{im}(\hat{\tau})$ is the descended (persistent) eigenspace and $\mathfrak{A}^{\mathrm{trans}} = \ker(\hat{\tau})$ is the transient eigenspace.

**Descended eigenspace.** $\mathfrak{A}^{\mathrm{desc}}$ is $3$-dimensional, isomorphic to $\mathrm{End}(\mathcal{O}(\mathrm{SU}(2))) \cong \mathfrak{su}(2)$ via the adjoint representation. These endomorphisms commute with $\mathrm{U}(1)$-averaging: they act exclusively on the base algebra, remaining insensitive to cotangent fluctuations.

**Transient eigenspace.** $\mathfrak{A}^{\mathrm{trans}}$ is $3$-dimensional, isomorphic to the cotangent complement $\Omega^1(\mathrm{SU}(2)/\mathrm{U}(1)) \cong \Omega^1(\mathbb{CP}^1) \oplus \mathbb{C}$. Explicitly, $\mathfrak{A}^{\mathrm{trans}}$ is spanned by endomorphisms that act non-trivially on the fibre directions $\omega_1, \omega_2, \omega_3$ but vanish under $\mathrm{U}(1)$-averaging.

**Representation-theoretic identification.** Under the adjoint action of $\mathrm{SU}(2)$, the descended eigenspace transforms as $V_1$ (the spin-$1$ representation), matching the transient eigenspace which also transforms as $V_1$. These two copies of $V_1$ are separated by their $\mathrm{U}(1)$-weights: $\mathfrak{A}^{\mathrm{desc}}$ carries weight $0$ while $\mathfrak{A}^{\mathrm{trans}}$ carries weights $\pm 1$.
<!-- FILE_END: descent-eigenspaces-su2.md -->

<!-- FILE_START: brane-boundary.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe equipped with the [recursive brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$. Let $\mathfrak{d}_{n+1}$ be the :refterm[descent]{#descent} homomorphism ([:refterm[descent]{#descent}](#lem:descent)). The **defining boundary** of the $n$-th brane is the full subcategory of $\mathbf{C}$ comprising subobjects of $A_n$ where the restriction morphism $r_n \colon A_n \to A_{n-1}$ has a non-trivial kernel:

$$
  \partial A_n
  = 
  \bigl\{ S \hookrightarrow A_n \bigm|
    \ker(r_n|_S) \neq 0 \bigr\}.
$$

In the archimedean realisation, $\partial A_n$ corresponds to the geometric locus $\partial \mathcal{S}_n = \{p \in \mathcal{S}_n \mid \ker(\mathfrak{d}_{n+1}|_p) \neq 0\} \subseteq \mathcal{S}_n$, which is exactly the degeneracy locus of the fibrewise :refterm[descent]{#descent} map.
<!-- FILE_END: brane-boundary.md -->

<!-- FILE_START: brane-boundary-su2.md -->
Continuing the [brane tower for SU(2)](#ex:recursive-brane-tower-su2), we evaluate the [brane boundary](#def:brane-boundary) at level $0$.

**The singular set.** For $G = \mathrm{SU}(2)$ acting on $\mathbb{CP}^1$ via the Hopf fibration, the singular set $S$ comprises the fixed points of the $\mathrm{U}(1)$-action: the north and south poles $\{0, \infty\} \subset \mathbb{CP}^1$. These dictate the vortex loci where the fibre degenerates.

**Categorical boundary.** The brane boundary $\partial A_0$ is the kernel of the restriction $r_0|_S \colon A_0 \to A_0|_S$:

$$
  \partial A_0
  =  \ker\bigl(\mathcal{O}(\mathrm{SU}(2))
  \xrightarrow{r_0|_S} \mathcal{O}(\mathrm{U}(1)_N)
  \oplus \mathcal{O}(\mathrm{U}(1)_S)\bigr),
$$

where $\mathrm{U}(1)_N$ and $\mathrm{U}(1)_S$ are the stabiliser fibres over the poles. In Peter--Weyl terms, $\partial A_0$ is the ideal of functions $f \in \mathcal{O}(\mathrm{SU}(2))$ vanishing on both stabiliser circles.

**Archimedean picture.** In the archimedean setting, $\partial \mathcal{S}_0$ is the boundary of the $\mathrm{SU}(2)$-frame bundle restricted to the vortex locus. The frame bundle $F(\mathrm{SU}(2)) \to \mathrm{SU}(2)$ restricts over $S$ to two copies of $\mathrm{U}(1) \times \mathbb{R}^3$, making $\partial \mathcal{S}_0 \cong (\mathrm{U}(1) \times S^2) \sqcup (\mathrm{U}(1) \times S^2)$, a disjoint union of two solid tori boundaries.

**Dimension.** As $\mathrm{SU}(2)$ is $3$-dimensional and $S$ is $1$-dimensional, $\partial A_0$ has codimension $2$ in $A_0$, properly matching the vortex as a codimension-$2$ defect.
<!-- FILE_END: brane-boundary-su2.md -->

<!-- FILE_START: brane-boundary-structure.md -->
The defining boundary $\partial A_n$ ([brane boundary](#def:brane-boundary)) possesses the following properties:

1. *Codimension.* In the archimedean realisation, $\partial A_n$ corresponds to a closed subset in $\mathcal{S}_n$ of real codimension at least 2.
2. *Exceptional object.* At each degeneration locus of the restriction $r_n$, the kernel $\ker(r_n|_S)$ is isomorphic to a simple object of $\mathbf{C}$. Archimedianly, this is $\mathbb{P}^1(\mathbb{C}) \cong S^2$, the exceptional divisor of the topological blow-up.
3. *Involution symmetry.* The :refterm[descent]{#descent} involution $\hat{\tau}_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution)) restricts to an endomorphism of $\partial A_n$. Its fixed subobjects coincide with the monodromy fixed points of the [quantum characteristic classes](#def:quantum-characteristic-classes).
4. *Chirality interface (archimedean).* When $n = 1$, $\partial \mathcal{S}_1$ isolates macroscopic spacetime from internal chiral modes. It forms the geometric boundary separating the base $M$ from the gauge fibre, across which the Reeb involution $\xi \mapsto -\xi$ ([Descartes chirality](#rem:archimedean-chirality)) reverses orientation.
<!-- FILE_END: brane-boundary-structure.md -->

<!-- FILE_START: descent-reduction-zero.md -->
When $\dim M_k = 0$ the base manifold is a discrete set of points and
the geometric data of the archimedean quantum observable universe
reduce to purely algebraic invariants at each point $p\in M_k$.

1. *Connection.*  The $\mathrm{SU}(2)$ connection $A_k$ has no
   directions along which to parallel-transport; its curvature
   $F_A$ vanishes identically and the holonomy is trivial.
2. *Bundle.*  The principal $\mathrm{SU}(2)$ bundle $\mathcal{S}$
   restricts to its fibre $\mathcal{S}_p$ over the point $p$; the bundle
   is determined entirely by this single fibre together with
   the group action.
3. *Substrate parameter.*  The substrate parameter
   $q(p) = 1 + \lVert L\wedge F_A^{+}\rVert(p)$
   ([$\mathbb{C}$-substrate via Levi form](#rem:c-substrate-via-levi)) assigns to each point a
   definite quantum constant $q\in[1,\infty)$, encoding the full
   content of the quantum observable universe at that point.
4. *Reeb direction.*  There is no tangent space, so the Reeb
   vector field ([$q$-Reeb vector field](#ex:q-reeb-vector-field)) and the
   horizontal distribution are absent; only the internal
   $\mathrm{SU}(2)$ fibre data persist.

In this terminal stage every observable is determined by the fibre
$\mathcal{S}_p$ and the value $q(p)$.  When $M_k$ consists of several points the
:refterm[descent]{#descent} data decompose into independent summands, one per point; when
$M_k$ is connected---i.e. a single point---the entire quantum
observable universe is captured by the pair $(\mathcal{S}_p, q(p))$.
<!-- FILE_END: descent-reduction-zero.md -->

<!-- FILE_START: descent-physical-zero.md -->
At dimension 0, all spatial extent vanishes and the physical content becomes purely algebraic.

1. *Primordial state.* The vortex filaments, flows, and spatial modes of higher-dimensional strata are absent; what remains is the initial datum of the fermionic content encoded in the fibre $\mathcal{S}_p$.
2. *Mass.* Lacking a base manifold for integration, the nonabelian multiplicative integral of the [mass identity](#def:mass-identity) degenerates. The surface $\Sigma$ collapses to a point, and the holonomy around $\gamma$ reduces to a single fibre evaluation $m = \lVert L \wedge F^+\rVert(p)$. Dimension-0 mass is an instantaneous, pointwise quantity rather than a distributed one.
3. *Lepton generations.* All vertical harmonic forms ([Betti numbers on branes](#rem:betti-numbers-brane)) concentrate at the point; the Euler characteristic $\chi(\mathcal{S}_p)$ retains the count of fermionic degrees of freedom without spatial multiplicity.
<!-- FILE_END: descent-physical-zero.md -->

<!-- FILE_START: descent-reduction.md -->
When $\dim M_k = 1$ the geometric data of the archimedean quantum observable
universe collapse as follows.

1. *Connection.*  The $\mathrm{SU}(2)$ connection $A_k$ restricts to
   a single dimension; its holonomy reduces to a $\mathrm{U}(1)$ phase
   around $S^1$.
2. *Bundle.*  The principal $\mathrm{SU}(2)$ bundle $\mathcal{S}$ descends to a
   bundle over the $1$-dimensional base whose fibre dynamics are locked
   into a single periodic flow.
3. *Reeb direction.*  The inverse of the Reeb vector field
   ([$q$-Reeb vector field](#ex:q-reeb-vector-field)) becomes the only direction
   of motion; the horizontal distribution is trivial and no bosonic modes
   ([algebraic filter](#rem:algebraic-filter)) survive.

The :refterm[descent]{#descent} need not terminate here; a further step carries $M_k$ to a
zero-dimensional base ([:refterm[descent]{#descent} reduction to zero](#rem:descent-reduction-zero)).
<!-- FILE_END: descent-reduction.md -->

<!-- FILE_START: descent-physical.md -->
At dimension 1, the physical content simplifies drastically.

1. *Primordial vortex.* The vortex filaments of the [mass identity](#def:mass-identity) are no longer embedded in a larger space; the entire manifold *is* the filament.
2. *Mass as pure drag.* When $\dim M_k = 1$, the surface $\Sigma$ in the [mass identity](#def:mass-identity) degenerates to the $1$-manifold $M_k$ itself. The $2$-dimensional nonabelian multiplicative integral reduces, via the nonabelian Stokes theorem \cite{yekutieli2015}, to the holonomy of the connection $\nabla_A$ around $M_k$:

   $$
     m = 
     \bigl\lVert
     \mathrm{Hol}_{\nabla_A}\!\bigl(M_k; \mathfrak{G}\bigr)
     \bigr\rVert,
   $$

   so mass represents the fundamental holonomy resistance of the $1$-dimensional flow against the $\mathrm{SU}(2)$ rotation.
3. *Lepton generations.* Because the number of lepton generations is bounded by the Euler characteristic and vertical degree ([Betti numbers on branes](#rem:betti-numbers-brane)), a $1$-dimensional base supports only the most fundamental fermionic state; there is no room for higher-degree vertical harmonic forms.
<!-- FILE_END: descent-physical.md -->

<!-- FILE_START: descent-fixed-point.md -->
Each step down the brane tower removes a space-like dimension through the
$\mathrm{SU}(2)$ rotation and its associated fixed-point set.

1. *Ascent (generation).*  Moving from $M_k$ ($\dim = 0$) upward
   lifts the connection $A$ to higher categorical structures via the jet
   prolongation ([jet prolongation](#prop:jet-prolongation)).
2. *:refterm[Descent]{#descent} (projection).*  Moving back down via the :refterm[descent]{#descent}
   homomorphism $\mathfrak{d}_n$ ([:refterm[descent]{#descent}](#lem:descent)) acts as an
   ([algebraic filter](#rem:algebraic-filter)) on the
   level-$(n{+}1)$ algebra.  The transient complement
   $\mathcal{A}_{n+1}^{\mathrm{trans}}$
   ([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces))---the genuinely new
   modes at level $n{+}1$ with no pre-image at level $n$---is
   annihilated by the :refterm[descent]{#descent} involution $\hat{\tau}_n$.
   At dimension 1 only the longitudinal
   $\mathrm{U}(1)$ backbone remains
   ([:refterm[descent]{#descent} reduction](#rem:descent-reduction)), and at dimension 0 even
   that is collapsed to a single fibre datum
   ([:refterm[descent]{#descent} reduction to zero](#rem:descent-reduction-zero)).
3. *Round-trip involution.*  The composition of ascent and :refterm[descent]{#descent}
   is the :refterm[descent]{#descent} involution $\hat{\tau}_n$
   ([:refterm[descent]{#descent} involution](#def:descent-involution)), acting on
   $\Gamma(J^1 \mathcal{S}_{n+1})$, whose image
   $\mathcal{A}_{n+1}^{\mathrm{desc}}$ is the stable core of the brane
   algebra at level $n{+}1$.  The defining boundary $\partial \mathcal{S}_n$
   ([brane boundary](#def:brane-boundary)) marks the geometric locus
   where the fibrewise :refterm[descent]{#descent} map has a non-trivial kernel.
<!-- FILE_END: descent-fixed-point.md -->

