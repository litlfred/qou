<!-- FILE_START: topological-mass-formula-transcendence-intro.md -->
This section develops topological mass and volume-tower transcendence. The construction begins with hyperbolic volumes.

Hyperbolic volumes record the substrate-level transcendence of the topological mass formula. The formula evaluated at $q_0$ yields the categorical hyperbolic volume of specific knot complements. Independent SnapPy computations for small-crossing knots provide a baseline to compare these substrate-level predictions. These small-crossing knots drive the mass predictions.
<!-- FILE_END: topological-mass-formula-transcendence-intro.md -->

<!-- FILE_START: hyperbolic-volumes-prose.md -->
**Hyperbolic volumes and the topological mass ansatz.**
Inertial mass originates in the topology of knot complements. The framework identifies every particle with a knot or link $K$ ([skein decomposition](#rem:skein-decomposition)). Each knot carries a **hyperbolic volume** $\mathrm{Vol}(K)$. This evaluates the volume of the complete hyperbolic metric on the complement $S^3 \setminus K$, computed via the Bloch--Wigner dilogarithm. Torus knots, such as the trefoil $3_1$, have zero hyperbolic volume. Hyperbolic knots have positive volume.

The framework identifies the Higgs boson with the figure-eight knot $4_1$ ([cohomological embedding](#prop:cohomological-embedding)). Its volume is

$$
  \mathrm{Vol}(4_1) = 3\mathrm{Cl}_2(\pi/3)
    \approx 2.02988321281931,
$$

where $\mathrm{Cl}_2$ denotes the Clausen function.

The [topological mass formula](#prop:topological-mass-formula) defines the mass $\mathfrak{m}(K)$ of a particle with knot type $K$ as

$$
  \mathfrak{m}(K) =  \frac{\mathrm{Vol}(K)}{\hbar_q^{2}},
  \qquad
  \hbar_q  :=  1 - q^{-1}.
$$

Here $q > 1$ represents the [substrate parameter](#def:substrate-parameter) and $\hbar_q$ represents the [quantum planck constant](#def:quantum-planck-constant). The mass functional $\mathcal{M}$ is not additive for composite states. It satisfies a $q$-deformed Skein recursion at every crossing in the color-exchange diagram.
<!-- FILE_END: hyperbolic-volumes-prose.md -->

<!-- FILE_START: predicted-spectra-intro.md -->
Bring's surface provides the geometric stage for the knot-to-particle correspondence ([Chapter 4](#chap:path-integrals-braiding)). The topological mass formula and its Skein-theoretic decomposition assemble here. The hyperbolic volume of a knot complement determines the mass of the associated particle. The Skein decomposition of the Jones polynomial separates the contributions of the Picard–Lefschetz thimbles attached to the exceptional color tubes. These results dictate the nuclear structure and yield the numerical predictions.
<!-- FILE_END: predicted-spectra-intro.md -->

<!-- FILE_START: cs-evaluation-faithfulness.md -->
Let $\Phi_n(K)$ denote the tower-level volume contribution from the [tower decomposition](#prop:volume-tower-decomposition). Let $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ denote the $n$-th [quantum characteristic class](#def:quantum-characteristic-classes).

**Proposition.**
The Chern--Simons evaluation map is *faithful* at each tower level. For every hyperbolic knot or link $K$ in the Descartes spectrum,

$$
  \kappa_n \neq 0 \quad \Longrightarrow \quad \Phi_n(K) \neq 0.
$$

If $\kappa_n$ defines a non-trivial obstruction in $H^2(\mathcal{S}, \mathcal{B})$, the Chern--Simons period integral over the $n$-th twisted sector yields a non-zero real contribution to $\mathrm{Vol}(K)$.

**Corollaries.**

1. **No accidental cancellation.** The Peiffer identity in the crossed groupoid conjugates $a^{(n)}$ by $g^{(n)}$ but preserves the period. The $\mathrm{SU}_{q_n}(2)$-adjoint action functions as an automorphism of the band $\mathcal{B} = \mathcal{O}_M^{\times}$, not as a projection to zero.
2. **Infinite non-trivial contributions.** The [Yekutieli lifting](#prop:yekutieli-lifting) theorem guarantees $\kappa_n \neq 0$ for all $n$. Faithfulness therefore implies the volume receives new data at every tower level.
3. **Path to algebraic independence.** If each $\Phi_n(K)$ carries arithmetically independent data, the series $\mathrm{Vol}(4_1) = \sum_n \Phi_n(4_1)$, $\mathrm{Vol}(5_2) = \sum_n \Phi_n(5_2)$, and $\mathrm{Vol}(\mathcal{B}_3) = \sum_n \Phi_n(\mathcal{B}_3)$ satisfy no polynomial relation. A finite polynomial cannot absorb infinitely many independent contributions.

**Relation to Mostow rigidity.**
Mostow rigidity guarantees the total volume $\mathrm{Vol}(K)$ defines a topological invariant. This proposition refines the invariant into a graded series $\{\Phi_n(K)\}_{n \geq 0}$, controlled by cohomological obstructions. Rigidity ensures convergence. Faithfulness ensures non-degeneracy at each grade.
<!-- FILE_END: cs-evaluation-faithfulness.md -->

<!-- FILE_START: hyperbolic-volume-transcendence.md -->
The [topological mass formula](#prop:topological-mass-formula) assigns mass
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$. Here $q$ denotes the
[substrate parameter](#def:substrate-parameter). Three non-zero
hyperbolic volumes drive the Descartes universe mass spectrum:

| Knot/Link | Volume | QOU identity |
|-----------|--------|-------------|
| Figure-eight $4_1$ | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$ | Higgs boson |
| Three-twist $5_2$ | $\mathrm{Vol}(5_2) \approx 2.82812$ | Down quark |
| Borromean rings $\mathcal{B}_3$ | $\mathrm{Vol}(\mathcal{B}_3) \approx 7.32772$ | Nucleon |

All torus knots (trefoil, cinquefoil, septafoil) possess zero hyperbolic
volume. They contribute no bare mass from this channel.

**Conjecture.**
The set $\{\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
\mathrm{Vol}(\mathcal{B}_3)\}$ is algebraically independent over
$\mathbb{Q}[q, q^{-1}]$. There exists no non-zero polynomial
$P \in \mathbb{Q}[q, q^{-1}][x, y, z]$ satisfying

$$
  P\bigl(\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
    \mathrm{Vol}(\mathcal{B}_3)\bigr) = 0.
$$

If the conjecture holds, the physical coefficient ring of the Descartes
universe forms $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)]$. This defines a polynomial ring in three
transcendentals over the ground ring. The specialisation map
$\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{R}$ sending
$q \mapsto q_0$ extends to an embedding of this ring into $\mathbb{R}$.
The three volumes remain algebraically independent over
$\mathbb{Q}(q_0)$.

*Remark.* The irrationality of a single hyperbolic 3-manifold volume remains an open problem. The Borel--Zagier conjecture concerns only
$\mathbb{Q}$-linear independence of volumes of non-commensurable
manifolds. This presents a strictly weaker, yet unresolved, claim.
Reid (1991) established $4_1$ as the unique arithmetic hyperbolic knot,
commensurable with $\mathrm{PSL}_2(\mathcal{O}_3)$. The three-twist
$5_2$ is non-arithmetic. The Borromean rings $\mathcal{B}_3$, as a
3-component link, fall outside Reid's classification. The
three complements are pairwise non-commensurable. The Borel--Zagier
conjecture would thus guarantee their $\mathbb{Q}$-linear independence.

**Scope: external open problem, partial categorical approach.**
This conjecture remains external to the framework. Its three forms

$$
  \text{irrationality}
  \;\Longleftarrow\;
  \mathbb{Q}\text{-linear independence}
  \;\Longleftarrow\;
  \text{algebraic independence}
$$

represent recognised open problems in transcendental
number theory. These include [single-volume irrationality](#conj:single-volume-irrationality)
(no hyperbolic 3-manifold volume is known to be irrational), [Borel--Zagier](#conj:borel-zagier-qou-volumes), and the Kontsevich--Zagier and Grothendieck period conjectures. The framework specifies only the choice of the three knots $4_1, 5_2, \mathcal{B}_3$. The mathematical hardness is entirely external.

The framework approaches the conjecture via two complementary, partial reductions. The deeper statement remains open. The sharper reduction is the
[jet-order reduction](#conj:three-knot-jet-order-independence). It
replaces Grothendieck-period machinery with a finite
per-order Gröbner--Shirshov independence computation. The skein engine
executes this computation natively. This pairs with a single QOU-native surreal bridge lemma. This reduction converts an external problem into an incremental
research target natively structured on the framework's jet-order filtration. The second reduction is the [transcendence shadow](#rem:yekutieli-transcendence-shadow). It
reduces algebraic independence to the non-collapse of the brane tower
and Nesterenko-type arithmetic control of the quantum dilogarithm.
Both paths relocate the difficulty. The Lean
formalisation proves the structural half: the tower
decomposition, Chern--Simons faithfulness, and the downstream
implications (algebraic independence $\Rightarrow$ Borel--Zagier
$\Rightarrow$ irrationality). The transcendence core is
axiomatised as the Lean class `HyperbolicVolumeIndependence`. Following
the conditional-class convention, the downstream results remain conditionally rigorous.

The conjecture serves as an ideal statement. It guarantees the predicted spectrum arises from no
algebraic coincidence. As the [formal-chain
remark](#rem:formal-chain-transcendence) records, the mass predictions
and the categorical derivation live entirely over $\mathbb{Z}[q, q^{-1}]$. They function independently of whether the volumes are transcendental, algebraic, or
rational. The framework operates strictly on the proved numerical
[distinctness](#prf:knot-volumes-verification) of the three volumes. This distinctness suffices for all mass predictions.
<!-- FILE_END: hyperbolic-volume-transcendence.md -->

<!-- FILE_START: single-volume-irrationality.md -->
**Conjecture.**
Each of the three non-zero QOU hyperbolic volumes is irrational:

$$
  \mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \notin \mathbb{Q},
  \qquad
  \mathrm{Vol}(5_2) \notin \mathbb{Q},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3) \notin \mathbb{Q}.
$$

*Remark.* This conjecture remains open. No hyperbolic 3-manifold volume has ever been proven irrational. The figure-eight volume $2\,\mathrm{Cl}_2(\pi/3)$ evaluates the Clausen function at a rational multiple of $\pi$. Its irrationality reduces to the irrationality of $\mathrm{Cl}_2(\pi/3) = \sum_{k=1}^{\infty} \sin(k\pi/3)/k^2$. This represents a Dirichlet $L$-value at $s = 2$ for the character $\chi_{-3}$. This evaluation remains unknown.

Ap\'ery (1978) proved $\zeta(3) \notin \mathbb{Q}$. The constant $\zeta(3)$ equals one-quarter the hyperbolic volume of the regular ideal tetrahedron. Knot complement volumes sum Bloch--Wigner dilogarithm values $D(z_i)$ at algebraic arguments. The arithmetic of these sums lies beyond current methods.

Irrationality forms the weakest link in the transcendence chain:

$$
  \text{irrationality}
  \;\Longleftarrow\;
  \mathbb{Q}\text{-linear independence (Borel--Zagier)}
  \;\Longleftarrow\;
  \text{algebraic independence.}
$$

Proving any of these statements for the QOU volumes demands a breakthrough in transcendental number theory.
<!-- FILE_END: single-volume-irrationality.md -->

<!-- FILE_START: borel-zagier-qou-volumes.md -->
**Conjecture (Borel--Zagier for QOU volumes).**

The three QOU hyperbolic volumes are $\mathbb{Q}$-linearly independent:

$$
  a_1 \,\mathrm{Vol}(4_1) + a_2 \,\mathrm{Vol}(5_2)
  + a_3 \,\mathrm{Vol}(\mathcal{B}_3) = 0,
  \quad a_i \in \mathbb{Q}
  \;\;\Longrightarrow\;\;
  a_1 = a_2 = a_3 = 0.
$$

This represents a special case of the Borel--Zagier conjecture. The Borel--Zagier conjecture asserts the $\mathbb{Q}$-linear independence of volumes of pairwise non-commensurable hyperbolic 3-manifolds.

#### Non-commensurability

Two manifolds are commensurable if they share a finite-sheeted cover. The three QOU complements occupy distinct commensurability classes:

- $S^3 \setminus 4_1$: The unique arithmetic hyperbolic knot complement. It is commensurable with $\mathrm{PSL}_2(\mathcal{O}_3)$.
- $S^3 \setminus 5_2$: A non-arithmetic complement with a cubic trace field. This field breaks commensurability with $4_1$.
- $S^3 \setminus \mathcal{B}_3$: A 3-component link complement. Its cusp geometry is incompatible with the knot complements. The ratios $\mathrm{Vol}(\mathcal{B}_3)/\mathrm{Vol}(4_1) \approx 3.610$ and $\mathrm{Vol}(\mathcal{B}_3)/\mathrm{Vol}(5_2) \approx 2.592$ confirm the link volume is not a simple rational multiple of either knot volume.

#### $K$-theoretic formulation

The Borel regulator maps $K_3(\overline{\mathbb{Q}}) \to \mathbb{R}$. Volumes of hyperbolic 3-manifolds lie in its image. The conjecture equates to the statement that the Borel regulator acts injectively (modulo torsion) on the $K_3$-elements corresponding to these three complements.

Linear independence is strictly weaker than [algebraic independence](#conj:hyperbolic-volume-transcendence) but strictly stronger than [irrationality](#conj:single-volume-irrationality).
<!-- FILE_END: borel-zagier-qou-volumes.md -->

<!-- FILE_START: three-knot-jet-order-independence.md -->
**Conjecture (jet-order independence — the QOU-attackable reduction).**
For every truncation order $N$, the Habiro-ring expansions of the coloured-Jones invariants for the three QOU knots/links,

$$
  J_{4_1}(q),\qquad J_{5_2}(q),\qquad J_{\mathcal{B}_3}(q)
  \;\in\; \widehat{\mathbb{Z}[q]},
$$

are *algebraically independent modulo $(q;q)_{N+1}$* over $\mathbb{Q}[q, q^{-1}]$. Equivalently, the Jacobian of their cyclotomic coefficient vectors $\bigl(c_0(K), \dots, c_N(K)\bigr)$ for $K \in \{4_1, 5_2, \mathcal{B}_3\}$ possesses full rank $3$ for all $N \ge N_0$.

This statement supplies a computationally viable target. It implies the [algebraic-independence conjecture](#conj:hyperbolic-volume-transcendence) provided the surreal-limit bridge holds. The ideal approach requires the full transcendence machinery (Grothendieck periods and the Borel regulator on $K_3(\overline{\mathbb{Q}})$), which remains out of reach. This reduction replaces that machinery with three framework-native tools and one remaining gap.

**Finiteness and decidability.**
Each $J_K(q)$ admits a canonical jet-order grading. The Habiro cyclotomic expansion $J_K(q) = \sum_{n \ge 0} c_n(K)\,(q;q)_n$ organizes the invariant such that the $n$-th term forms the vertical jet-degree $n$ component of the categorical generating function. This aligns with the body-order filtration grading the binding series $G(x;q) = \sum_n B_n x^n$. Algebraic independence to order $N$ imposes a finite-rank condition on the truncated coefficient matrix. The claim is strictly decidable.

**The three framework tools.**

1. **Jet-order filtration** supplies the grading. Independence is verified order-by-order. Reid (1991) anchors the base order. Because $4_1$ is the unique arithmetic hyperbolic knot, its trace field $\mathbb{Q}(\sqrt{-3})$ is rigidly distinct from the cubic trace field of $5_2$ and the link field of $\mathcal{B}_3$ at order $0$.
2. **Gröbner–Shirshov filtration** certifies each order. The reduction engine computes the elimination ideal $I_N = \bigl(\text{relations among } J_{4_1}, J_{5_2}, J_{\mathcal{B}_3} \bmod (q;q)_{N+1}\bigr) \subseteq \mathbb{Q}[q,q^{-1}][x,y,z]$. Full Jacobian rank holds if and only if $I_N$ carries no generator of total degree $\le N$. This translates "no polynomial relation" into a normal-form computation natively executed by the skein engine. The base-order certificate is formalized in Lean and directly witnessed by computation. The h-jet expansion about $q=1$ of the canonical Markov traces $\mathrm{tr}_M(K)$ for the three canonical braid words yields jet-Jacobian rows $(\tfrac14, -1, \tfrac{55}{16})$, $(\tfrac12, 0, -\tfrac1{16})$, and $(1, 0, 0)$. Their elimination determinant is $\tfrac1{16} \neq 0$ (LU pivots $(\tfrac14, 2, \tfrac18)$, `jetOrder3_certificate`). Full rank $3$ holds unconditionally at the base order. This constitutes a finite determinant test on real data. Higher orders require no further computation. The order-$N$ Jacobian contains this non-singular $3\times3$ minor as a column-submatrix. Its rank is therefore $\ge 3$. The three rows strictly bound the rank by $3$. The rank must be exactly $3$ at every $N$, as rank is monotonically non-decreasing in the column count. Lean formalizes the two endpoints of this argument. It proves the base minor is full-rank via explicit invertibility (`jetJacobianBase_rank`). It proves the abstract monotonicity principle (`jacobianRank_eq_three_of_base`): any monotone, row-bounded rank function equal to $3$ at the base order remains $3$ for all $N \ge 3$. The column-extension linkage discharging the principle's hypotheses for the order-$N$ Jacobian is supplied as a structural input. Per-order independence reduces to this structural linkage.
3. **Surreal error bounds** supply the bridge to the limit. The correct geometric picture is parallel transport on the projective state fibre. The coloured-Jones invariant $J_K(q)$ acts as the holonomy of the categorical connection, parallel-transported along the substrate $q$-deformation path on $\mathcal{S} = P \times_G \mathbb{CP}^1$. The volume is its singular-limit asymptotics $\mathrm{Vol}(K) = \lim_{n\to\infty} \tfrac{2\pi}{n}\log\lvert J_K(e^{2\pi i/n})\rvert$. The surreal error bound measures the transport error as $q$ deforms toward the root-of-unity point. This error is non-Archimedean because the target point is a singularity of the connection. The error is an infinitesimal in the surreal field. Three conditions must hold for the bridge:
   - **(I1) Uniformity in jet order.** The transport error must be bounded uniformly in $N$. The connection's curvature is uniformly controlled along the deformation path, independent of the truncation order. Any error growing with $N$ severs the transfer.
   - **(I2) Archimedean projection.** The error inhabits the surreal fibre level, carrying the $\operatorname{Im}(q)$ structure. The volume is archimedean ($\operatorname{Im}(q_0) = 0$). The surreal infinitesimal must project to exactly $0$ under $\tau$. A non-infinitesimal archimedean shadow would inject a spurious polynomial relation among the volumes.
   - **(I3) Monodromy separation.** Transport around the cusp is flat only at generic $q$. At the root-of-unity limit, the holonomy accumulates cusp/modular monodromy. The bound must isolate the physical holonomy, which yields $\mathrm{Vol}$, from this monodromy artifact.
   The framework's surreal-number error field provides the natural setting for this uniform bound. The Lean reduction splits the previously monolithic axiom. Uniformity (I1) and the (I2)∘(I3) composition are formally proved (`transport_uniform_bound`, `transport_shadow_vanishes`). The two physical inputs remain conjectural: the physical-holonomy shadow vanishes (I2), and the monodromy shadow vanishes (I3). These are now isolated as precisely stated hypotheses.

**The one remaining gap.**
This reduction does not prove the deep conjecture. It reduces the conjecture to a single native lemma:

> **Bridge lemma (open).** If $\{J_{4_1}, J_{5_2}, J_{\mathcal{B}_3}\}$ are jet-order independent for all $N$ with a surreal-bounded uniform error, then $\{\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)\}$ are algebraically independent over $\mathbb{Q}(q_0)$.

The reduction secures a strategic advantage. It shifts the [algebraic-independence conjecture](#conj:hyperbolic-volume-transcendence) from an intractable Grothendieck-period transcendence statement to a finite, per-order computation coupled with the surreal bridge. The base order is now Lean-certified. The (I1) uniformity and composition properties of the bridge are formally proved. Unconditional closure is sacrificed: the (I2) and (I3) physical inputs remain unproved. This converts an external dead end into an internal, incremental research target structured natively on the framework's filtration.
<!-- FILE_END: three-knot-jet-order-independence.md -->
