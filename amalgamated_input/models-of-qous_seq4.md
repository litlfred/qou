<!-- FILE_START: archimedean-models-intro.md -->
We specialise to archimedean fields. Over $\mathbb{R}$ and $\mathbb{C}$, the substrate parameter $q$ varies smoothly, and the categorical data becomes differential geometry on a contact 3-manifold. The commutative diagram of the preceding section implies every archimedean quantum observable universe is a $\mathbb{P}^1(\mathbb{C})$-bundle over a strictly pseudoconvex CR base with an $\mathrm{SU}(2)$ frame. We now construct explicit geometries that satisfy these conditions.

We present four models. First, a real hypersurface in a Calabi–Yau 2-fold extracts contact data from a K3 hypersurface to recover classical instanton moduli. Second, an ALE space yields an ADE orbifold quotient via the McKay correspondence. Third, the unit circle bundle over Bring's surface produces the genus-4 fibre ($\chi(S) = -6$) selected in the next chapter. Finally, the cosmological limits of $q$ define the deep-quantum and classical endpoints. These examples demonstrate that the archimedean axioms support diverse geometric realisations.

We extract invariants from two sources. The bundle provides gauge-theoretic data: the instanton connection, irreducibility, self-dual curvature, and the Seiberg–Witten differential. The Reeb fibre provides contact-geometric data: the Levi form of the $\mathbb{C}$-substrate, the Webster inner product, and the $q$-deformed Heisenberg commutator. Over $\mathbb{C}$, the categorical observation functor becomes a measurement of the Reeb flow.

We conclude with two bridge results. A spatial-realisation functor maps categorical data to differential data. A categorical–geometric correspondence confirms this functor preserves the axioms by comparing the categorical action against the classical Chern–Simons action. The subsequent section, **Non-Archimedean models**, transports this categorical formulation to $\mathbb{Q}_p$.
<!-- FILE_END: archimedean-models-intro.md -->

<!-- FILE_START: calabi-yau.md -->
Classical hyper-Kähler geometry provides a natural setting for quantum observable universes.

Let $X$ be a Calabi–Yau 2-fold (a K3 surface) with holonomy $\mathrm{SU}(2)$. Let $M \subset X$ be a smooth, strictly convex real hypersurface. The ambient Kähler geometry induces a 3-dimensional strictly pseudoconvex CR structure on $M$. The frame bundle of $X$ restricts to a principal $\mathrm{SU}(2)$-bundle $P \to M$ over the hypersurface. The associated state bundle $\mathcal{S} = P \times_{\mathrm{SU}(2)} \mathbb{P}^1(\mathbb{C})$ completes the data for an archimedean quantum observable universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$ ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)).

Because $X$ is hyper-Kähler, the Kähler potential induces a contact form $\varTheta$ on $M$. The Reeb vector field $\xi$ ([Reeb decomposition](#ex:reeb-decomposition)) is the restriction of the Hamiltonian vector field of the Kähler potential. The hyper-Kähler triple $(\omega_I, \omega_J, \omega_K)$ restricts to forms on $M$, inducing the weight decomposition ([weight decomposition](#def:weight-decomposition)).

The categorical instanton condition ([categorical instanton](#def:categorical-instanton)) reduces to the anti-self-duality equation $F_A^+ = 0$ on $X$. The moduli space of solutions is the classical instanton moduli space on a K3 surface. The substrate parameter $q(p)$ ([substrate parameter](#def:substrate-parameter)) interpolates between this instanton connection and the Reeb component.

This construction casts standard instanton moduli problems as special cases of the categorical framework.
<!-- FILE_END: calabi-yau.md -->

<!-- FILE_START: ale.md -->
The links of ALE spaces provide a discrete, ADE-indexed family of archimedean quantum observable universes.

Let $\Gamma \subset \mathrm{SU}(2)$ be a finite subgroup. Let $X$ be the minimal resolution of $\mathbb{C}^2 / \Gamma$. The link $M = S^3 / \Gamma$ is a compact 3-dimensional strictly pseudoconvex CR manifold. We equip $M$ with the induced principal $\mathrm{SU}(2)$-bundle $P \to M$ and the state bundle $\mathcal{S} = P \times_{\mathrm{SU}(2)} \mathbb{P}^1(\mathbb{C})$. This data specifies an archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)).

The McKay correspondence classifies the subgroups $\Gamma$ by ADE Dynkin diagrams. The exceptional divisors of $X \to \mathbb{C}^2/\Gamma$ are copies of $\mathbb{CP}^1$ intersecting in the corresponding Dynkin pattern. Because $S^3/\Gamma$ is connected, the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) is constant. The weight decomposition ([weight decomposition](#def:weight-decomposition)) inherits the $\Gamma$-equivariant splitting of forms on $S^3$. The Reeb decomposition ([Reeb decomposition](#ex:reeb-decomposition)) reduces to the Hopf fibration $S^3/\Gamma \to S^2$, with the Reeb vector field $\xi$ generating the $\mathrm{U}(1)$ fibre rotation.

This classification yields one quantum observable universe for each Dynkin type ($A_n$, $D_n$, $E_6$, $E_7$, $E_8$). The connection data derives from the instanton moduli space on $X$.
<!-- FILE_END: ale.md -->

<!-- FILE_START: instanton.md -->
To verify that the categorical formalism recovers the classical gauge-theoretic object, we specialise to the archimedean setting. In the archimedean quantum universe ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)), a [categorical instanton](#def:categorical-instanton) specialises to an *instanton connection* on $P$. This is a connection $A$ whose curvature $F_A$, restricted to $H = \ker\varTheta$, is self-dual: $F_A|_H = {*_H}F_A|_H$. The $q$-Hodge star $\star_q$ specialises to the Webster Hodge star $*_H$ on $\Lambda^2 H^*$. Consequently, $\star_q$-self-duality recovers classical $*_H$-self-duality.
<!-- FILE_END: instanton.md -->

<!-- FILE_START: irreducible-connection.md -->
An instanton in the archimedean regime cannot reduce to an abelian $\mathrm{U}(1)$ sub-bundle. Its gauge orbit must remain free. [Categorical irreducible](#lem:categorical-irreducible) specialises to this geometric fact: every instanton connection $A$ on $P$ is irreducible. 

The vanishing cohomology $H^0(M, \mathrm{Ad}(P)) = 0$ ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) provides the archimedean instance of $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. Concretely, a non-zero section $s \in H^0(M, \mathrm{Ad}(P))$ furnishes an $\mathrm{Ad}$-invariant direction in $\mathfrak{su}(2)$ at every point. This reduces the connection to $\mathrm{U}(1)$. The QOU vanishing axiom forbids this, forcing the gauge orbit of $A$ to be free.
<!-- FILE_END: irreducible-connection.md -->

<!-- FILE_START: self-dual-curvature.md -->
On a four-dimensional space the Yang--Mills energy splits into a
topological floor, fixed by the bundle's second Chern number, and a
non-negative remainder that measures the anti-self-dual part of the
curvature; a connection attains the floor precisely when its curvature
is self-dual.  This example specialises
[categorical self duality](#prop:categorical-self-duality) to recover
that classical instanton picture.

In an archimedean quantum observable universe with
$\dim_{\mathbb{R}} H = 4$, categorical self-duality specialises:
every instanton connection $A$ on $P$ satisfies
$F_A|_H = {*_H}F_A|_H$, where $*_H$ denotes the Hodge star on the
four-dimensional space $H$.  Under the same specialisation the
categorical Yang--Mills functional
$\int_A(\star_q(F_\nabla) \cdot F_\nabla)$ — the integral over the
categorical universe of the $q$-Hodge pairing of the curvature with
itself — becomes the ordinary Yang--Mills energy
$\int_M \lVert F_A|_H \rVert^2\varTheta \wedge (d\varTheta)^2$ of the
restricted curvature $F_A|_H$ on the base $M$.

The Bogomolny trick decomposes
$\lVert F_A|_H \rVert^2 = \lVert F_A^+ \rVert^2 + \lVert F_A^- \rVert^2$
into its self-dual and anti-self-dual pieces.  The self-dual part
$\int \lVert F_A^+ \rVert^2$ is a topological invariant
(the second Chern number $c_2(P)$) and so cannot be lowered; the
anti-self-dual part carries energy with no such topological floor.
Minimising the Yang--Mills functional therefore forces
$F_A^-|_H = 0$.
<!-- FILE_END: self-dual-curvature.md -->

<!-- FILE_START: reeb-decomposition.md -->
In the archimedean realisation
([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)), the categorical weight
decomposition ([weight decomposition](#def:weight-decomposition)) specialises
to the *Reeb decomposition*: the contact form $\varTheta$ canonically
separates the $\mathrm{U}(1)$-fibre direction from the base, so the
weight grading becomes a split of forms into vertical and horizontal
parts.  Let $\xi$ denote the *Reeb
vector field*, characterised by $\iota_\xi d\varTheta = 0$ and
$\varTheta(\xi) = 1$.  Every differential $k$-form $\alpha$ ($k \geq 1$)
on $M$ decomposes uniquely as

$$
  \alpha = \alpha_H + \varTheta \wedge \iota_\xi\alpha,
$$

where $\alpha_H := \alpha - \varTheta \wedge \iota_\xi\alpha$ is the
*horizontal component* ($\iota_\xi\alpha_H = 0$) and
$\alpha_V := \varTheta \wedge \iota_\xi\alpha$ is the *vertical
component*.  The Reeb vector $\xi$ generates the
$\mathrm{U}(1)$-action (the maximal torus,
[maximal torus](#def:maximal-torus)), and the weight-$0$ subspace is the
horizontal distribution $H = \ker\varTheta$.
<!-- FILE_END: reeb-decomposition.md -->

<!-- FILE_START: cosmological-limits.md -->
**Conjectural interpretation.** The parameter range of the substrate field $q$ models a cosmological trajectory for a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)). The limits of $q$ represent a "big bang" and a "heat death".

Consider $M = S^3$ equipped with the standard contact form $\varTheta$ and the standard instanton on the Hopf bundle. As the instanton curvature concentrates near a point $p_0 \in S^3$, the substrate field $q$ partitions into two regimes:

- **Near $p_0$ ($q(p) \to \infty$, $\hbar_q \to 1$):**
  Uncertainty becomes maximal ($[\hat{X},\hat{P}]_q \to J$). Observables become maximally non-commutative. The quantum observable universe becomes fully quantum-mechanical, retaining no classical shadow. This is the "big bang" regime.

- **Away from $p_0$ ($q(p) \to 1$, $\hbar_q \to 0$):**
  The commutator $[\hat{X}, \hat{P}]_q$ vanishes. The Hopf algebra becomes cocommutative ($\sigma \circ \Delta = \Delta$, [Hopf non-cocommutativity](#rem:hopf-non-cocommutativity)). Observations commute, $q$-deformed operators reduce to their classical limits, and the transport equation reduces to classical parallel transport ($\nabla\psi = 0$). This is the "heat death" regime: a fully classical, frozen universe.

At both limits, the quantum observable universe structure degenerates:

- As $q \to \infty$, the Frobenius pairing $\langle f, g \rangle = \int_A(\mu(f \otimes g))$ ([Frobenius pairing](#def:frobenius-pairing)) loses non-degeneracy. Axiom (1) of the definition of a quantum observable universe fails; the universe ceases to be observable.

- As $q \to 1$, the $q$-Hodge star $\star_q$ reduces to the classical Hodge star $\star_1$. The quantum gauge group $\mathrm{SU}_q(2)$ collapses to the classical Lie group $\mathrm{SU}(2)$. The deformation vanishes, and the substrate parameter carries no information.

We conjecture the physically meaningful regime strictly satisfies $1 < q < \infty$, where quantum and classical features coexist. Rigorously analyzing these limits requires controlling the singular behavior of the Frobenius form as $q \to \infty$. This remains an open problem.
<!-- FILE_END: cosmological-limits.md -->

