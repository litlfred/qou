<!-- FILE_START: quantum-observable-universes-intro.md -->
The remaining sections of this chapter elaborate the categorical,
algebraic, and analytic context of the QOU axioms without adding new
structure.  They place the construction in its TQFT setting, record
the $q$-jacobiator identity behind the non-vanishing of $d_q^2$, give
the physical reading of the categorical action, and assemble the
categorical lifting that prepares the Yekutieli brane tower of
[*Lifting and Descent*](#chap:torsion).  The elaborations are mutually
independent, sharing only the axioms established above.
<!-- FILE_END: quantum-observable-universes-intro.md -->

<!-- FILE_START: tqft-context.md -->
The axioms of
[quantum universe](#def:quantum-universe)
and [quantum observable universe](#def:quantum-observable-universe) are grounded in the algebraic
framework of topological quantum field theory (TQFT).

*Frobenius--Hopf objects and 2d TQFT.*
A commutative Frobenius algebra over $R$ is equivalent to a
$2$-dimensional TQFT
$Z \colon \mathbf{2Cob} \to R\text{-}\mathrm{Mod}$
\cite{kock2004, atiyah1988}. The Frobenius--Hopf object $A$ in
[quantum universe](#def:quantum-universe) carries both the Frobenius structure
(encoding the $2$d cobordism data: the product $\mu$ corresponds to a
pair-of-pants cobordism, the Frobenius form $\int_A$ to a cap) and a
Hopf structure (encoding the quantum-group symmetry that extends the theory
to three dimensions). Concretely, a $2$d TQFT assigns to
the circle $S^1$ a Frobenius algebra $A$ and to each cobordism
$\Sigma \colon S^1 \sqcup \cdots \to S^1 \sqcup \cdots$ a linear map
built from $\mu$, $\Delta_\mu$, $\eta$, and $\int_A$. The Hopf
structure $(\Delta, \varepsilon, S)$ equips $A$ with the additional data
needed for three-dimensional and extended TQFTs
\cite{turaev2010, witten1988}.

*The observability condition as a categorical contact condition.*
In the TQFT setting, the condition
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def:quantum-observable-universe)) is the categorical
analogue of the *contact condition* (maximal non-integrability).
A non-zero morphism $\mathbf{1} \to \mathrm{Ad}(A)$ would give a
global invariant section of the adjoint object --- the categorical
counterpart of a nowhere-vanishing section of the adjoint bundle --- and
would force the TQFT to decompose into a direct sum of
lower-dimensional theories. Requiring
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ therefore ensures:

1. *irreducibility*: the associated $3$-dimensional TQFT
   (Chern--Simons type, with gauge datum $A$ and quantum
   parameter $q$) does not split as a direct sum;
2. *non-degeneracy across cobordisms*: the TQFT pairing on
   state spaces assigned to surfaces is non-degenerate
   \cite{freed2010};
3. *full dualisability*: in the sense of the cobordism
   hypothesis \cite{baez1995, lurie2009}, the object $A$ is
   fully dualisable in the relevant Morita higher category, so the
   TQFT extends to a fully local (extended) field theory.

In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), this categorical
condition reduces to
$H^0(M, \mathrm{Ad}(P)) = 0$ --- the classical requirement that the
instanton connection admits no infinitesimal automorphisms, which is the
gauge-theoretic manifestation of the contact (maximally non-integrable)
geometry of $(M, \varTheta)$.
<!-- FILE_END: tqft-context.md -->

<!-- FILE_START: vanishing-explication.md -->
In [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe), the condition
$H^0(M, \mathrm{Ad}(P)) = 0$ eliminates all infinitesimal gauge
symmetries, while $\Gamma_c(M,\mathcal{S}) = 0$ ensures the jet-bundle
map $\Gamma(J^1 \mathcal{S}) \hookrightarrow \mathcal{A}(P)$ is injective.
<!-- FILE_END: vanishing-explication.md -->

<!-- FILE_START: levi-generalisation.md -->
[$\mathbb{C}$-quantum universe](#ex:c-quantum-universe) requires only Levi non-degeneracy
(not strict pseudoconvexity). This generality is deliberate: the QOU
framework applies whenever the following three cohomological/obstruction
conditions hold.

1. *Kohn--Rossi finite-dimensionality.*
 The tangential CR complex
 $(\Omega^{0,\bullet}_b(M), \bar\partial_b)$ has
 finite-dimensional cohomology
 $H^{0,k}_{\bar\partial_b}(M)$ for all $k$. This replaces
 strict pseudoconvexity in ensuring analytic control over
 $q$-harmonic forms ([$q$-harmonic form](#def:q-harmonic-form)).
 In the strictly pseudoconvex case, Kohn's sub-elliptic
 estimates guarantee this automatically; for indefinite
 Levi signature, one imposes it as a hypothesis.
2. *Non-degeneracy of the substrate.*
 The Levi form $L_\varTheta$ is non-degenerate (but not necessarily
 positive definite), so the substrate parameter
 $q(p) = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert$
 ([$\mathbb{C}$-substrate via Levi form](#rem:c-substrate-via-levi)) is well-defined and
 the regime $q > 1$ is attainable. When the Levi form has
 indefinite signature $(r,s)$ with $r,s \geq 1$, the Webster
 metric $g_\varTheta$ is pseudo-Riemannian; the contraction
 $\langle L_\varTheta, F_A^+\rangle$ remains well-defined (using
 the pseudo-Riemannian inner product on $\Lambda^+ H^*$), and
 one takes the absolute value to ensure $q \geq 1$.
3. *QOU vanishing ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)).*
 The conditions $H^0(M, \mathrm{Ad}(P)) = 0$ and
 $\Gamma_c(M,\mathcal{S}) = 0$ serve as the gauge-theoretic obstructions.
 These are purely topological/cohomological and independent of the
 Levi signature.

Together, conditions (1)--(3) ensure that all results of this chapter
(irreducibility of the connection, self-duality of the curvature,
substrate dynamics, $q$-deformed operators) extend to CR manifolds of
arbitrary Levi signature. The strictly pseudoconvex case (signature
$(n,0)$) is the simplest and motivates all examples in this chapter;
the indefinite case arises accordingly for real hypersurfaces in
indefinite Kähler manifolds and for boundaries of
Grauert tubes over pseudo-Riemannian manifolds.
<!-- FILE_END: levi-generalisation.md -->

<!-- FILE_START: quantum-gauge-group-category.md -->
The
([quantum gauge group](#def:quantum-gauge-group)) is realised pointwise by
the Hopf algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ of regular
functions on $\mathrm{SU}_{q(p)}(2)$. The categorical view replaces
each fibre with its representation category
$\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$, a :refterm[braided monoidal category]{#braided-monoidal-category}.
Tannaka--Krein duality reconstructs $\mathcal{O}_{q(p)}$ from
$\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ via
$\mathrm{End}^{\otimes}(\tau)$, where $\tau$ is the forgetful
fibre functor. For any two points $p, p' \in M$ connected by a
path $\gamma$, the passage between fibres is captured by the
commutative square

```tex
\begin{equation}\label{eq:tannaka-krein-functoriality}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_{q(p)}(\mathrm{SU}(2))
    \ar[r, "\mathrm{Rep}"]
    \ar[d, "\text{transition along } \gamma"']
  & \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))
    \ar[d, "\text{monoidal functor}"]
  \\
  \mathcal{O}_{q(p')}(\mathrm{SU}(2))
    \ar[r, "\mathrm{Rep}"']
  & \mathrm{Rep}(\mathrm{SU}_{q(p')}(2))
\end{tikzcd}
\end{equation}
```

Tannaka--Krein reconstruction inverts the horizontal arrows, so the
Hopf-algebra and representation-category viewpoints are equivalent
fibrewise.
<!-- FILE_END: quantum-gauge-group-category.md -->

<!-- FILE_START: hopf-structure-diagrams.md -->
Write $\mathcal{O}_q = \mathcal{O}_q(\mathrm{SU}(2))$.
The Hopf comultiplication satisfies *coassociativity*:

```tex
\begin{equation}\label{eq:coassociativity}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_q
    \ar[r, "\Delta_q"]
    \ar[d, "\Delta_q"']
  & \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[d, "\mathrm{id} \otimes \Delta_q"]
  \\
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\Delta_q \otimes \mathrm{id}"']
  & \mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
\end{tikzcd}
\end{equation}
```

Non-cocommutativity and the self-duality short exact sequence are
developed categorically in
[Remarks](#rem:hopf-non-cocommutativity)
and [Remark](#rem:self-dual-ses).
<!-- FILE_END: hopf-structure-diagrams.md -->

<!-- FILE_START: quantum-flatness.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with quantum
gauge group $G_q = \mathrm{Aut}^{\otimes}(\tau)$
([quantum gauge group](#def:quantum-gauge-group)) and connection $\nabla$
on $A$ ([categorical connection](#def:categorical-connection)), and let
$B \in \Omega^2(A) \otimes \mathrm{Ad}(A)$ be the $2$-form datum of the
inner-automorphism $2$-group $\mathrm{INN}(G_q)$.  The connection $\nabla$
is :defterm[quantum flat]{#quantum-flatness} when its curvature equals the
$2$-form datum:

$$
  F_\nabla = B.
$$
<!-- FILE_END: quantum-flatness.md -->

<!-- FILE_START: self-dual-2group.md -->
A strict $2$-group is equivalently a *crossed module*: a
group homomorphism $\partial \colon H \to G$ together with an
action of $G$ on $H$ satisfying the Peiffer identity. The
associated exact sequence

```tex
\begin{equation}\label{eq:crossed-module-ses}
\begin{tikzcd}[column sep=2em]
  1 \ar[r]
  & \ker\partial \ar[r]
  & H \ar[r, "\partial"]
  & G \ar[r]
  & \mathrm{coker}\partial \ar[r]
  & 1
\end{tikzcd}
\end{equation}
```

encodes the $2$-group as a homotopy type with
$\pi_0 = \mathrm{coker}\partial$ and
$\pi_1 = \ker\partial$.

The *inner-automorphism $2$-group*
$\mathrm{INN}(G) = (G \xrightarrow{\mathrm{id}} G)$
has $\ker\partial = 1$ and $\mathrm{coker}\partial = 1$, so it is
connected and connected as a $2$-group. A $2$-connection for
$\mathrm{INN}(G)$ on a principal $2$-bundle over $M$ consists of a
$\mathfrak{g}$-valued $1$-form $A$ and a $\mathfrak{g}$-valued
$2$-form $B$, subject to the *:refterm[quantum flatness]{#quantum-flatness}* condition

$F_A =  B.$

In the QOU setting, $G = \mathrm{SU}(2)$ and the Levi distribution
$H = \ker\varTheta$ has $\dim_{\mathbb{R}} H = 4$, so the Hodge
decomposition $\Lambda^2 H^* = \Lambda^+\!H^* \oplus \Lambda^-\!H^*$
is available. Imposing the *simplicity constraint*

$B  \in  \Gamma\!\bigl(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)\bigr)$

\--- that is, requiring the $2$-form datum to be self-dual ---
and combining with :refterm[quantum flatness]{#quantum-flatness} gives
the commutative diagram

```tex
\begin{equation}\label{eq:2group-instanton}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^1(M,\mathfrak{g})
    \ar[r, "d_A"]
  & \Omega^2(M,\mathfrak{g})
    \ar[r, "\pi^+"]
  & \Omega^{2,+}(M,\mathfrak{g})
  \\
  & F_A \ar[u, "=B"]
    \ar[r, equal]
  & F_A^+ \ar[u, "\text{simplicity}"']
\end{tikzcd}
\end{equation}
```

The :refterm[quantum flatness]{#quantum-flatness} condition $F_A = B$ combined with the simplicity
constraint $B = F_A^+$ forces $F_A = F_A^+$, hence $F_A^- = 0$.
This is precisely the instanton equation
$F_A|_H = {*_H}F_A|_H$
of instanton. Thus, the self-dual formulation
used throughout this paper is a special case of $2$-group gauge theory
for $\mathrm{INN}(\mathrm{SU}(2))$ subject to a simplicity constraint
on the $2$-form datum.

This perspective clarifies the relationship between the instanton
condition in Chapter 1 and the higher-categorical structures of later
chapters: the parallel-transport $2$-functor of the
$\mathrm{INN}(\mathrm{SU}(2))$ $2$-bundle assigns to paths in $M$
not only group elements in $\mathrm{SU}(2)$ but $2$-morphisms
encoding the self-dual curvature, with the simplicity constraint
selecting the physical (instanton) sector.
<!-- FILE_END: self-dual-2group.md -->

<!-- FILE_START: emergence-to-quantum-flat.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe satisfying
the
([categorical volume constraint](#eq:categorical-volume-constraint)), so that
$G_q = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}_q(2)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)). Then the inner-automorphism
$2$-group $\mathrm{INN}(G_q)$ is the unique strict $2$-group whose
quantum flatness condition $F_A = B$ reproduces the
instanton equation $F_A^{-} = 0$ under the simplicity constraint.

```tex
\begin{equation}\label{eq:emergence-to-quantum-flat-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  F_A \ar[r, equal, "\text{instanton}"]
    \ar[d, "F_A = B"']
  & F_A^+ \ar[d, equal, "\text{simplicity}"] \\
  B \ar[r, equal]
  & F_A^+
\end{tikzcd}
\qquad\text{(derived quantum flatness)}
\end{equation}
```

:refterm[Quantum flatness]{#quantum-flatness}
([quantum flatness](#def:quantum-flatness)) is not an independent
assumption: it is a *derived consequence* of the instanton axiom. The instanton condition
$F_A = F_A^+$ (self-dual curvature) combined with the simplicity
constraint $B = F_A^+$ gives $F_A = B$ automatically. The $2$-group
language is a descriptive overlay that makes the higher-categorical
structure manifest, not an additional physical constraint.
<!-- FILE_END: emergence-to-quantum-flat.md -->

<!-- FILE_START: simplicity-from-category.md -->
The $*$-involution on $\mathbf{C}$---required by the QOU
observability axiom---induces via the fibre functor an involution on
$\Omega^2(M, \mathfrak{g}_q)$ whose $+1$-eigenspace is exactly the
self-dual forms $\Omega^{2,+}(M, \mathfrak{g}_q)$. Thus the full
chain

$$
  \text{volume constraint}
  \xRightarrow{\text{Tannaka}}
  G_q = \mathrm{SU}_q(2)
  \xRightarrow{\mathrm{INN}}
  F_A = B
  \xRightarrow{*\text{-structure}}
  B = F_A^+
  \Longrightarrow
  F_A^- = 0
$$

is forced by the axioms of the quantum observable universe, with no
additional geometric input beyond the CR structure of $M$.
<!-- FILE_END: simplicity-from-category.md -->

<!-- FILE_START: frobenius-simplification.md -->
The Hopf algebra $\mathcal{O}_q(\mathrm{SU}(2))$ carries a natural
*Frobenius structure*: the Haar state
$h_q \colon \mathcal{O}_q \to \mathbb{C}$ induces a non-degenerate
pairing $\langle a, b \rangle = h_q(ab)$, making $\mathcal{O}_q$ into
a Frobenius algebra with comultiplication $\Delta_\mu$ dual to the
multiplication. This Frobenius comultiplication is compatible with the
Hopf comultiplication $\Delta_q$ of the coassociativity diagram and
satisfies the *Frobenius relation*:

```tex
\begin{equation}\label{eq:frobenius-relation-elab}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu"]
    \ar[d, "\mathrm{id} \otimes \Delta_\mu"']
  & \mathcal{O}_q
    \ar[d, "\Delta_\mu"]
  \\
  \mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu \otimes \mathrm{id}"']
  & \mathcal{O}_q \otimes \mathcal{O}_q
\end{tikzcd}
\end{equation}
```

where $\mu$ is the algebra multiplication and $\Delta_\mu$ the
Frobenius comultiplication (dual to $\mu$ under the Haar pairing).
The non-degeneracy of $h_q$ is expressed by requiring the composite

```tex
\begin{equation}\label{eq:frobenius-nondegen}
\begin{tikzcd}[column sep=3em]
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu"]
  & \mathcal{O}_q
    \ar[r, "h_q"]
  & \mathbb{C}
\end{tikzcd}
\end{equation}
```

to be a perfect pairing, i.e. the induced map
$\mathcal{O}_q \to \mathcal{O}_q^*$ is an isomorphism.

This Frobenius--Hopf structure on $\mathcal{O}_q(\mathrm{SU}(2))$ is
precisely the datum required by the general
[quantum universe](#def:quantum-universe): the Haar state $h_q$ realises
the Frobenius form $\int_A \colon A \to \mathbf{1}$, and the
non-degeneracy is the $\mathbb{C}$
instance of condition (1) in
[quantum observable universe](#def:quantum-observable-universe).
In the archimedean realisation ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)),
the $4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$ and the two analytic vanishing
conditions of [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)
reduce to a triple:

1. a CR manifold $(M, \varTheta)$ of hypersurface type with
 non-degenerate Levi form;
2. a non-degenerate Frobenius--Hopf object $A$ in the monoidal
 category of vector bundles over $M$, playing the role of
 $(G, \mathcal{S})$; and
3. an instanton connection on the underlying $A$-bundle
 ([instanton](#def:categorical-instanton)).

The vanishing condition $H^0(M, \mathrm{Ad}(P)) = 0$ then follows from
the non-degeneracy of the Frobenius form $\int_A$ via the diagram

```tex
\begin{equation}\label{eq:frobenius-vanishing}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \mathrm{Ad}(A) \otimes \mathrm{Ad}(A)
    \ar[r, "\mu_{\mathrm{Ad}}"]
    \ar[d, "\text{global sections}"']
  & \mathrm{Ad}(A)
    \ar[r, "\int_{A,\mathrm{Ad}}"]
  & \mathcal{O}_M
    \ar[d, "\textstyle\int_M"]
  \\
  H^0(M,\mathrm{Ad}(A)) \otimes H^0(M,\mathrm{Ad}(A))
    \ar[rr, "\text{pairing}"']
  & & \mathbb{C}
\end{tikzcd}
\end{equation}
```

The adjoint representation $\mathrm{Ad}(A)$ inherits a non-degenerate
[Frobenius pairing](#def:frobenius-pairing) from $\int_A$; any global parallel section would
pair non-by definition with itself, contradicting the irreducibility of
the instanton connection
([irreducible connection](#ex:irreducible-connection)). Hence the Frobenius
non-degeneracy, combined with irreducibility, forces
$H^0(M, \mathrm{Ad}(A)) = 0$. The section-vanishing condition
$\Gamma_c(M, \mathcal{S}) = 0$ follows similarly from the non-existence of
$A$-equivariant sections of the associated $\mathbb{P}^1(\mathbb{C})$-bundle.

Note that the horizontal distribution $H = \ker\varTheta$ itself
*fails* to carry a Frobenius structure (as discussed in
[$q$-torsion existence](#rem:q-torsion-existence)); it is the gauge algebra, not the
distribution, that is Frobenius.
<!-- FILE_END: frobenius-simplification.md -->

<!-- FILE_START: j1e-local-states.md -->
The jet bundle $J^1 \mathcal{S}$ serves as the space of local states of the
$\mathbb{C}$ quantum observable universe. The classical gauge dynamics,
encoded by the *instanton connection* $A$
([irreducible connection](#ex:irreducible-connection)), are weighted by the substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter)) to define the
quantum field algebra $\mathrm{SU}_q(2)$
([quantum gauge group](#def:quantum-gauge-group)).
<!-- FILE_END: j1e-local-states.md -->

