<!-- FILE_START: transfer-matrix-mass-intro.md -->
The previous section identified the Feynman amplitude with the Markov trace through vertex factorisation. We now compile this data into a single operator on the categorical state space and extract mass from it. The construction is level-independent. The resulting mass formula forms the basis for all subsequent sections.

The section defines the Categorical mass operator, which assembles the vertex operators into a single morphism on the brane-tower state space. Two structural results follow: the Operator level independence proposition shows trace invariance under brane-tower level shifts. The Constituent and composite Markov-trace agreement lemma establishes the coincidence between the two factorisations of the trace. The Topological ansatz and field character remark records mass behaviour under change of knot ansatz.

The Mass formula (smooth case) provides the smooth-case form of the categorical mass identity. The Motivic mass measure $\mu$ packages the corresponding motivic substrate. The Hecke mass element and Hecke mass trace blocks define the element of $H_n(q)$ whose Markov trace returns the mass. The Charge–mass duality via the Frobenius pairing remark records the resulting Frobenius duality. Finally, the Skein Decomposition and Mass Ratios remark reads the Skein-relation content of the mass formula directly. The next section filters braid-group representations through the spectral algebra using this mass-trace evaluation.
<!-- FILE_END: transfer-matrix-mass-intro.md -->

<!-- FILE_START: categorical-transfer-matrix.md -->
Let $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a
[hadron](#def:hadron) at a brane point $p$
([localized hadron](#def:localized-hadron)), and let $\mathcal{S}_p$ be the
exceptional divisor at $p$
([exceptional divisor](#def:exceptional-divisor)).

A **categorical transfer matrix** for $\mathfrak{H}_p$ is the equivalence
class

$$
  \mathcal{T}(\mathfrak{H})
  = 
  \bigl[ T \bigr]_{\sim}
   \in 
  \mathrm{End}\bigl(H_n(R, q)\bigr) \big/ \sim
$$

where $T$ is any braiding operation on $\mathfrak{H}$ (at either level)
and the equivalence relation $\sim$ identifies two operations
$T_1 \sim T_2$ whenever they produce the same vertex volume:

$$
  T_1 \sim T_2
  \quad\Longleftrightarrow\quad
  \hat{V}(T_1, q) = \hat{V}(T_2, q)
  \quad\text{as polynomials in } q.
$$

This is well-defined because the vertex volume $\hat{V}_i(q)$
depends only on the Markov trace of the Hecke-reduced element.
It does not depend on the specific braid representative, the
decomposition of $\mathfrak{H}$ into constituents, or the path of
braiding operations within $\mathcal{S}_p$.
<!-- FILE_END: categorical-transfer-matrix.md -->

<!-- FILE_START: categorical-transfer-matrix-properties.md -->
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
$\iota_{j_i}$.  The index $i$ labels the **constituent slot**,
not the knot type: several slots may carry the same simple object
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
<!-- FILE_END: categorical-transfer-matrix-properties.md -->

<!-- FILE_START: transfer-matrix-level-independence.md -->
**Proposition (conditional on [`conj:crystal-graph-realization`](#conj:crystal-graph-realization) — transfer-matrix level independence).**
Let $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a hadron
with composite knot $K_{\mathfrak{H}} = \hat{\beta}_{\mathfrak{H}}$.  Let $\mathcal{T}(\mathfrak{H}_p)$
be the categorical transfer matrix
([categorical transfer matrix](#def:categorical-transfer-matrix)).
Then:

1. **Constituent-composite agreement.**  The Markov trace computed
   from the constituent insertion points $(z_1, \ldots, z_n)$
   and the Markov trace computed from the composite insertion
   point $z_H$ yield the same Jones polynomial:

   $$
     \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{const}}(q)
     = 
     \hat{V}^{\mathrm{comp}}(q)
     = 
     J_{K_{\mathfrak{H}}}(q).
   $$

2. **Path independence on $\mathcal{S}_p$.**  Two braiding operations
   $T_1, T_2$ on $\mathfrak{H}$ that produce isotopy-equivalent
   configurations
   ([isotopy equivalence](#def:bundle-isotopy-equivalence))
   have the same categorical transfer matrix:
   $\mathcal{T}(T_1) = \mathcal{T}(T_2)$.  In particular, the
   specific sequence of crossing changes within the exceptional
   divisor $\mathcal{S}_p$ does not affect the result --- only the
   equivalence class of the final configuration matters.

3. **Well-definedness.**  The categorical transfer matrix
   $\mathcal{T}(\mathfrak{H})$ depends only on the isotopy class of the
   hadron $\mathfrak{H}$ and the knot types $K_i$ of its constituents.
   It is independent of:
   - the braid representative $\beta_{\mathfrak{H}}$,
   - the PawLei embedding $\iota_{j_i}$ for each constituent,
   - the order of crossings evaluated within $\mathcal{S}_p$.
<!-- FILE_END: transfer-matrix-level-independence.md -->

<!-- FILE_START: tmli-constituent-composite-agreement.md -->
*For a hadron $\mathfrak{H} \hookrightarrow V^{\otimes N}$ with
$N = 2(j_1 + \cdots + j_n)$ and braid word
$\beta_{\mathfrak{H}} \in B_N$, the constituent product
$\prod \hat{V}_i^{\mathrm{const}}$ and the composite trace
$\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))$ evaluate the same element
of $H_N(q)$, so*

$$
  \prod_i \hat{V}_i^{\mathrm{const}}
  =
  \mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))
  =
  P_{K_{\mathfrak{H}}}(q).
$$
<!-- FILE_END: tmli-constituent-composite-agreement.md -->

<!-- FILE_START: topological-mass-formula.md -->
In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)),
the topological decomposition of mass
([topological mass](#thm:topological-mass)) specialises to a closed-form
relationship between the mass of a particle, the hyperbolic volume of its
associated knot, and the quantum Planck constant.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the $\mathbb{C}$-quantum observable universe
and let $K$ be a hyperbolic knot whose complement carries the vortex topology
of a stable particle, generated by $N$ blow-ups along the brane tower.  The
:refterm[descent]{#descent} involution $\hat{\tau}_n$
([:refterm[descent]{#descent} involution](#def:descent-involution)) induces the idempotent
splitting $\mathrm{End}_{\mathbf{C}}(A_{n+1}) = \mathcal{A}^{\mathrm{desc}} \oplus \mathcal{A}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).  Under the archimedean
fibre functor, the descended trace evaluates to the holonomy
$\mathrm{Hol}_{\nabla_A}$ and each transient trace to the quantum
dilogarithm $\Phi_q(z_i)$, giving the mass formula

$\mathfrak{m}(K) =  \frac{\mathrm{Vol}(K)}{\hbar_q^{2}},$

where $\mathrm{Vol}(K)$ is the hyperbolic volume of $S^3 \setminus K$
and $\hbar_q = 1 - 1/q$ is the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)) at the substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter)).

The derivation proceeds from the categorical decomposition
([topological mass](#thm:topological-mass)) via three identifications,
each following from the archimedean bridge.

**Step 1 — baseline holonomy $\mapsto$ hyperbolic volume.**
The descended trace of the universal vortex $\varrho_0$ is the
holonomy norm
$\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \rVert$.
Under the archimedean fibre functor
([categorical-archimedean-bridge](#prop:categorical-archimedean-bridge))
this is the imaginary part of the Chern--Simons functional on the
flat connection associated to $K$, which by the Chern–Simons /
hyperbolic-volume correspondence equals $\mathrm{Vol}(S^3 \setminus K)$
(Möbius energy;
[Kashaev volume density](#rem:kashaev-volume-density)).  Concretely,

$$
  \mathrm{Re}\,\mathrm{tr}\bigl(\hat{\tau}_n^{\mathrm{desc}}\,\mathrm{Hol}\bigr)
  \;=\; \mathrm{Vol}(K).
$$

**Step 2 — transient dilogarithm sum $\mapsto$ $(1/\hbar_q^{2} - 1)$ correction.**
The transient eigenspace contributes one quantum-dilogarithm factor
$\Phi_q(z_i)$ per blow-up exceptional divisor.  In the Briggs–Klein
spectral coordinates of the brane tower
([mass-endomorphism on the jet tower](#rem:mass-endomorphism-jet-tower)),
the $z_i$ are the eigenvalues of the per-crossing transfer operator
on the curvature-rank stratification.  Summing over the $N$ blow-ups
and using the dilogarithm identity
$\sum_{i=1}^N \Phi_q(z_i) = (1/\hbar_q^{2} - 1)\,\mathrm{Vol}(K)$
(Kashaev–Murakami volume conjecture restricted to the
$q$-deformation; this is `Hypothesis 2 (Dilogarithm evaluation)`
on the Lean structure
[`qou:QOU.ArchimedeanMassFormula`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ArchimedeanMassFormula.lean),
field `exceptional_sum_eq`):

$$
  \sum_{i=1}^{N} \Phi_q(z_i)
  \;=\; \mathrm{Vol}(K)\bigl(\hbar_q^{-2} - 1\bigr).
$$

The Lean formalisation isolates this identity as a hypothesis on
the archimedean structure rather than a derived theorem; the
evaluation in Briggs–Klein coordinates is the categorical content
the formula imports from the geometric side.

**Step 3 — combine.**
Adding the baseline and transient contributions and recognising
$1 + (\hbar_q^{-2} - 1) = \hbar_q^{-2}$:

$$
  \mathfrak{m}(K)
  \;=\; \mathrm{Vol}(K) + \mathrm{Vol}(K)\bigl(\hbar_q^{-2} - 1\bigr)
  \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}.
$$

Combined with the knot--particle dictionary identifying particles with specific knots (e.g. the figure-eight knot $4_1$ with the Higgs field), this formula determines the substrate parameter $q$ from experimental mass ratios (see §6.10).
<!-- FILE_END: topological-mass-formula.md -->

<!-- FILE_START: motivic-mass-measure.md -->
**Definition.**
*Let $K_0(\mathrm{Var}_k)$ be the **Grothendieck ring of varieties**
over the base field $k$ — the free abelian group on isomorphism
classes $[X]$ of $k$-varieties modulo the scissor relations
$[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with
product $[X] \cdot [Y] = [X \times Y]$. Let $\mathbb{L} = [\mathbb{A}^1_k]
\in K_0(\mathrm{Var}_k)$ denote the **Lefschetz motive**, and write
$\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ for its
localization. The **motivic mass measure** of the QOU brane is the
Kontsevich--Denef--Loeser motivic measure*

$$
  \mu \;:\; \mathcal{B}(\mathcal{L}(X))
  \;\longrightarrow\;
  \widehat{\mathcal{M}}
$$

*on cylindrical (Borel) subsets of the
[arc space](#def:arc-space) $\mathcal{L}(X)$ of a brane variety $X$,
valued in the dimension-completion $\widehat{\mathcal{M}}$ of
$\mathcal{M}$. Volumes of measurable subsets are computed by*

$$
  \mu(A)
  \;=\;
  [\pi_n(A)] \;\mathbb{L}^{-(n+1)\dim X}
  \qquad
  (\pi_n \colon \mathcal{L}(X) \to \mathcal{L}_n(X)),
$$

*independently of $n$ once $A$ is stable at level $n$.*

**Mass from blow-ups.** When the categorical
Gröbner--Shirshov reduction
([three-parameter Wedderburn formula](#thm:wedderburn-mass-formula))
processes a braid $\beta \in H_n(R, q)$, it performs a finite sequence
of algebraic blow-ups of the brane variety $X$ along the crossing
loci, producing exceptional divisors $E_1, \dots, E_r$ with
multiplicities (or codimension weights) $d_1, \dots, d_r$. The
**topological mass** of the reduced state is the motivic integral
of the trivial function over the arc space, computed by Kontsevich's
change-of-variables formula as

$$
  \mathfrak{m}_{\mathrm{mot}}(\beta)
  \;:=\;
  \int_{\mathcal{L}(X)} d\mu
  \;=\;
  \sum_{i=1}^{r}\, [E_i^{\circ}] \, \mathbb{L}^{-d_i}
  \;\in\;\widehat{\mathcal{M}},
$$

*where $[E_i^{\circ}]$ is the class of the smooth open part of the
$i$-th exceptional divisor.*

**Motivic rationale.** The mass endomorphism
([proton--electron mass ratio](#prop:mass-endomorphism-tower))
needs to assign a finite, $q$-discrete weight to a Gröbner-Shirshov
reduction whose intermediate states are singular: there is no smooth
volume form to integrate, no measure-theoretic Lebesgue construction
that survives the blow-up. The motivic measure $\mu$ assigns each
reduction step a value in the Grothendieck ring $\mathcal{M}$,
purely algebraically, by tracking which classes of varieties appear
as exceptional fibers. The categorical analogue of crossing the
$\chi(A) = -6$ topological horizon
([topological mass formula](#prop:topological-mass-formula)) is
exactly the contribution $[E_i^{\circ}] \mathbb{L}^{-d_i}$ of the
exceptional divisor of that blow-up.

The motivic mass $\mathfrak{m}_{\mathrm{mot}}(\beta)$ is a class in
$\widehat{\mathcal{M}}$ — a *motive*, not yet a real number. The
real-valued physical mass is recovered by applying the
[archimedean realization functor](#def:archimedean-realization-functor)
of the next subsection.
<!-- FILE_END: motivic-mass-measure.md -->

<!-- FILE_START: hecke-mass-element.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
Hecke algebra $H_n(R, q)$
([Hecke algebra](#rem:hecke-algebra-from-braiding)) and Markov trace
$\mathrm{tr}_M \colon H_n(R, q) \to k$
([Jones--Markov trace](#thm:jones-markov-trace)).

Let $\varrho \colon \mathbf{1} \to A$ be a vortex morphism with braid
representative $\beta \in B_n$.  The **mass integrand**
([mass identity](#def:mass-identity)) is the composition

$$
  \alpha_\varrho
  =
  (\textstyle\int_A \otimes \mathrm{id})
  \circ \Delta
  \circ \varrho
  \colon \mathbf{1} \to A,
$$

which, via left multiplication in the Frobenius--Hopf algebra $A$,
determines an endomorphism
$L_{\alpha_\varrho} \in \mathrm{End}_{\mathbf{C}}(A)$.
Since all constituent maps ($\Delta$, $\int_A$, $\varrho$) are morphisms
in $\mathbf{C}$, the fibre-functor image $\tau(L_{\alpha_\varrho})$ is
an $\mathrm{SU}_q(2)$-equivariant endomorphism of $V^{\otimes n}$.
By quantum Schur--Weyl duality, every such endomorphism is an element
of the Hecke algebra.

The **Hecke mass element** of the vortex $\varrho$ is

$$
  \Phi_{\mathrm{mass}}(\beta)
  \;:=\;
  \tau\bigl(L_{\alpha_\varrho}\bigr)
  \;\in\; H_n(R, q).
$$

The :refterm[descent]{#descent} involution $\hat{\tau}_n$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) induces an
idempotent decomposition within $H_n(R, q)$:

$$
  \Phi_{\mathrm{mass}}(\beta)
  =
  \Phi^{\mathrm{desc}}(\beta)
  +
  \Phi^{\mathrm{trans}}(\beta),
$$

where $\Phi^{\mathrm{desc}} = \tau(\hat{\tau}_n(L_{\alpha}))$ encodes
the base-level (descended) cycle and
$\Phi^{\mathrm{trans}} = \tau(L_{\alpha} - \hat{\tau}_n(L_{\alpha}))$
encodes the transient contributions at the blow-up centres.
<!-- FILE_END: hecke-mass-element.md -->

<!-- FILE_START: hecke-mass-trace.md -->
Let $(\mathbf{C}, A, \tau)$ be a QOU, let $\varrho \colon \mathbf{1} \to A$
be a vortex with braid representative $\beta \in B_n$, and let
$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$ be its Hecke mass element
([Hecke mass element](#def:hecke-mass-element)).

**Proposition.**  The categorical mass
([mass identity](#def:mass-identity)) equals the norm of the Markov
trace of the Hecke mass element:

$$
  \mathfrak{m}(\varrho_\beta)
  \;=\;
  \bigl\lvert
    \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \bigr\rvert.
$$

Moreover, the topological decomposition
([topological mass](#thm:topological-mass)) descends to $H_n(R, q)$:

$$
  \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{desc}}(\beta)\bigr)
  \;+\;
  \sum_{i=1}^{N}
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{trans}}_i(\beta)\bigr).
$$

**Archimedean specialisation (§7c).** The categorical mass-squared, the hyperbolic volume $\mathrm{vol} : \mathbb{R}$ and $\hbar : \mathbb{R}$, and the descended trace are the archimedean ($\mathbb{R}$-valued) readouts of the generic Markov-trace mass data; the $R\to\mathbb{R}$ realisation is acknowledged here.
<!-- FILE_END: hecke-mass-trace.md -->

<!-- FILE_START: hecke-generator-poly-reduction.md -->
*Let $\sigma_i$ be a Hecke generator, satisfying the quadratic relation
$\sigma_i^2 = (q - q^{-1})\,\sigma_i + 1$. For any finite list of scalars
$d_1, \dots, d_r \in R$, the product of single-generator factors collapses
to an $R$-linear combination of $\sigma_i$ and the identity,*

$$
  \prod_{j=1}^{r} \bigl(\sigma_i + d_j\,1\bigr) \;=\; \alpha\,\sigma_i + \beta\,1,
$$

*where $(\alpha, \beta)$ is given by the division-free recursion*

$$
  (\alpha,\beta)_{\varnothing} = (0,\,1),
  \qquad
  (\alpha,\beta)_{d\,::\,\mathrm{ds}}
    = \bigl(\alpha'\,(h + d) + \beta',\;\; \alpha' + \beta'\,d\bigr),
$$

*with $h = q - q^{-1}$ and $(\alpha',\beta')$ the coefficients for the
tail $\mathrm{ds}$.*
## Consequence for the Markov trace

In a seminormal (Gelfand–Zetlin) representation the diagonal entry of
$\alpha\,\sigma_i + \beta\,1$ on a two-box block depends only on the
content gap $\delta'$ of the two boxes added at that step, through the
eigenvalue $D(\delta')$ of $\sigma_i$. Hence whenever a braid word has a
**monotone** generator sequence — as the multi-nucleon atom word
$\beta_{\mathrm{atom}}$ does, each nucleon contributing
$\sigma_{3k}, \sigma_{3k+1}$ and one interface crossing $\sigma_{3k+2}$
without revisiting a generator — every per-generator operator $O_g$ is a
single-generator polynomial, and its seminormal diagonal is a single
$\alpha_g\,D(\delta'_g) + \beta_g$. The character then factorises as a sum
over Bratteli chains of a product of such local factors:
$$
  \chi^\lambda(\beta_{\mathrm{atom}})
   = \sum_{\varnothing = s_0 \subset s_1 \subset \cdots \subset s_n = \lambda}
       \ \prod_g \bigl(\alpha_g\,D(\delta'_g) + \beta_g\bigr),
$$
a transfer matrix over the Young lattice that never materialises the
$d_\lambda$-dimensional Hoefsmit representation. This is the mechanism by
which the canonical Markov trace
$\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ scales to large
atoms (Steps 3 and 9b of the mass–binding chain): the per-block work drops
to a few field operations, removing the $n!$ wall of the per-basis-vector
evaluation.

## Lean formalization

The division-free reduction is formalised in
`QOU.Braiding.hecke_gen_poly_reduction`, proved by induction over the
factor list from the Hecke quadratic alone (the coefficient recursion is
`QOU.Braiding.heckeAB`). The transfer-matrix character built on it is
implemented and validated to the 50-digit floor in
the formal derivation.
<!-- FILE_END: hecke-generator-poly-reduction.md -->

<!-- FILE_START: hecke-charge-mass-duality.md -->
The mass integrand
$\alpha_\varrho = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$
splits along two orthogonal directions in the Hecke algebra, corresponding
to the two Markov moves of the braid group.

| Restriction | Markov move | $H_n(R, q)$ element | Physical invariant |
|---|---|---|---|
| Horizontal | Conjugation (within a fibre) | $\rho(\beta)$ | Charge $Q$, crossing energy $\mathfrak{E}_{\mathrm{cross}}$ |
| Vertical | Stabilisation (along the tower) | $\Phi_{\mathrm{mass}}(\beta)$ | Mass $\mathfrak{m} = \mathrm{Vol}/\hbar_q^2$ |
| Mixed | Both simultaneously | $Y(a, z)$ (vertex operator) | Full particle data |

The Frobenius pairing $\langle a, b \rangle_F = \int_A \mu(a \otimes b)$
mediates the duality: it pairs $\mu$ (horizontal) with $\int_A$ (vertical).

**Horizontal restriction (conjugation, within a fibre).**
Restricting to a single level of the brane tower — crossings within
$V^{\otimes n}$ with no tower propagation — the Hecke element
$\rho(\beta) \in H_n(R, q)$ encodes the crossing structure directly.
The crossing energy
([crossing energy](#def:crossing-energy)) reads off the Skein
eigenvalue sum
$\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$,
and the Coulomb charge
([Coulomb charge](#def:coulomb-charge)) is the crossing asymmetry
$Q = \tfrac{1}{2}(n_+ - n_-)$.
These are **horizontal** invariants: they depend on the braiding
pattern, not on the depth of the tower.

**Vertical restriction (stabilisation, along the tower).**
The Hecke mass element
$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)) dresses
$\rho(\beta)$ with the Frobenius--comultiplication operator
$(\int_A \otimes \mathrm{id}) \circ \Delta$, which projects
through the Frobenius form (collapsing tower data) and
comultiplies (probing the tower depth).
Its Markov trace
([mass via Markov trace](#prop:hecke-mass-trace)) gives the
categorical mass $\mathfrak{m} = \mathrm{Vol}(K)/\hbar_q^2$
— a **vertical** invariant measuring resistance to
transport through the comultiplication.

**Mixed: the vertex operator as generating function.**
On the mixture — when horizontal crossings and vertical tower
steps act simultaneously — the result is the vertex operator
$Y(a, z)$ ([vertex operator](#def:vertex-operator)), whose modes

$$
  a_m
  =
  \mathrm{tr}_M\!\bigl(\check{R}_{(a)}\, z^m\bigr)
$$

combine horizontal braiding ($\check{R}$, the $R$-matrix) with
vertical insertion ($z^m$, the tower coordinate on
$\mathcal{S}_p$).  The vertex operator is the generating function
that encodes both charge and mass data simultaneously.

**The Frobenius pairing as mediator.**
The duality between horizontal and vertical is mediated by the
Frobenius pairing
([Frobenius pairing](#def:frobenius-pairing)):

$$
  \langle a, b \rangle_F
  =
  \textstyle\int_A \mu(a \otimes b),
$$

which pairs multiplication $\mu$ (horizontal: composing crossings)
with the Frobenius form $\int_A$ (vertical: integrating along the
tower).  This pairing identifies the particle element
$\rho(\beta)$ (charge carrier) with the mass element
$\Phi_{\mathrm{mass}}(\beta)$ (mass carrier) as dual aspects of a
single Hecke algebra element — connected by exactly the
Frobenius--comultiplication map that defines the categorical mass.
<!-- FILE_END: hecke-charge-mass-duality.md -->

<!-- FILE_START: skein-decomposition.md -->
This remark formalizes the refinement of the particle-topology mapping by shifting from torus knots to a framework grounded in hyperbolic volumes and Skein-deformed residues. By treating mass as the geometric resistance of the 1-jet bundle prolongation, the $q$-deformed Skein relation provides a rigorous Mass Sum Rule for composite hadronic states.
<!-- FILE_END: skein-decomposition.md -->

<!-- FILE_START: topological-field-ansatz.md -->
The following table summarizes the axiomatic assignments where particle identities map to specific knot types ($K$) and their associated masses $\mathcal{M}(K)$ depend on the local substrate field $q(p)$.

See [Table: Particle-to-knot axiomatic assignments](#tbl:topological-field-ansatz-table-data).
<!-- FILE_END: topological-field-ansatz.md -->

