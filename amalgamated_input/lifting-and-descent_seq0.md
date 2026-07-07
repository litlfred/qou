<!-- FILE_START: jet-prolongation-intro.md -->
This chapter takes the quantum observable universe $(\mathbf{C}, A, \tau)$ and grows it: each level $A_n$ of a recursive tower is the jet prolongation of the previous one. The whole edifice of lifting, descent, and mass decomposition rests on this tower being well-defined. This section constructs the tower.

We begin with the Jet Prolongation proposition, which establishes that the jet object $J^1(A) = A \otimes \Omega^1(A)$ inherits a Frobenius–Hopf structure and a fibre functor, ensuring that $(\mathbf{C}, J^1(A), \tau', q)$ is again a QOU. A supporting lemma supplies the Hopf-side argument, and a remark on prolongation clarifies how the Kähler differential machinery feeds the construction. We then iterate this procedure to produce the recursive brane tower $\{A_n\}_{n \geq 0}$, examine the smooth geometric model $J^1\mathcal{S}_n$, and define the arc space $\mathcal{L}(X)$ that collects the levels into a single ind-scheme. The subsequent section, *Categorical Lifting*, uses the tower as the carrier for defining torsion and transport.
<!-- FILE_END: jet-prolongation-intro.md -->

<!-- FILE_START: jet-prolongation.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a ring $R$ ([quantum observable universe](#def:quantum-observable-universe)). Define the *jet object*:

$$
  J^1(A)  :=  A \otimes \Omega^1(A),
$$

where $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$ is the bimodule of Kähler differentials. Then $J^1(A)$ carries a canonical Frobenius–Hopf structure inherited from $A$, and the quadruple $(\mathbf{C}, J^1(A), \tau', q)$—where $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$ is the induced fibre functor—is again a quantum observable universe over $R$.
<!-- FILE_END: jet-prolongation.md -->

<!-- FILE_START: jet-prolongation-su2.md -->
We construct the [jet prolongation](#prop:jet-prolongation) of $A = \mathcal{O}(\mathrm{SU}(2))$.

**Kahler differentials.** The module of Kahler differentials is $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$, which for the left-invariant calculus on $\mathrm{SU}(2)$ yields:

$$
  \Omega^1(A) =  \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$

where $\omega_a$ are the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The jet object.** By [jet prolongation](#prop:jet-prolongation):

$$
  J^1(A)  :=  A \otimes \Omega^1(A)
   \cong  \mathcal{O}(\mathrm{SU}(2)) \otimes
  \mathrm{span}\{\omega_1, \omega_2, \omega_3\}.
$$

As a vector space, $J^1(A)$ consists of $\mathcal{O}(\mathrm{SU}(2))$-valued $1$-forms on $\mathrm{SU}(2)$, which are precisely the sections of the frame bundle $F(\mathrm{SU}(2))$.

**Inherited Frobenius–Hopf structure.** The comultiplication on $J^1(A)$ is defined by:

$$
  \Delta'(f \otimes \varTheta)(x, y)
  =  f(xy) \otimes \varTheta_y,
$$

where $\varTheta_y$ denotes the left-translate of $\varTheta$ to $T_y G$. The counit and antipode extend similarly: $\varepsilon'(f \otimes \varTheta) = f(e)\varTheta_e$ and $S'(f \otimes \varTheta)(x) = f(x^{-1}) \otimes (L_{x^{-1}})^*\varTheta$. The Frobenius form is $\int_{J^1 A}(f \otimes \varTheta) = \int_G f\varTheta$, integrating the $1$-form component over $G$ using the Haar measure.

**QOU structure.** The induced fibre functor is $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$, forgetting the $G$-action on sections while retaining the $1$-form structure. Since $\mathrm{SU}(2)$ is $3$-dimensional, $J^1(A)$ is a $3$-fold extension of $A$, yielding $\dim_{\tau'} J^1(A) = 3 \cdot \dim_\tau A$. The quadruple $(\mathrm{Rep}(\mathrm{SU}(2)), J^1(A), \tau', q)$ is again a quantum observable universe.
<!-- FILE_END: jet-prolongation-su2.md -->

<!-- FILE_START: jet-prolongation-categorical-jet.md -->
**Lemma.**
*The categorical jet object $J^1(A) := A \otimes \Omega^1(A)$, where $\Omega^1(A) = \ker(m\colon A\otimes A \to A)$ is the bimodule of Kähler differentials, is an object of the ambient rigid monoidal category, and inherits a Frobenius–Hopf structure $(\Delta', \varepsilon', S')$ from $A$.*
<!-- FILE_END: jet-prolongation-categorical-jet.md -->

<!-- FILE_START: prolongation-categorical.md -->
The proof above shows that jet prolongation is an *intrinsic*
consequence of the Frobenius--Hopf structure in a rigid :refterm[monoidal category]{#monoidal-category}:
no additional geometric input beyond the categorical data
$(\mathbf{C}, A, \tau)$ is required.  Concretely:

1. The Frobenius structure provides the Kähler differentials
   $\Omega^1(A)$ as a direct summand, from which the jet object
   $J^1(A)$ is built.
2. The Frobenius relation ensures that the comultiplication and
   multiplication are compatible, so the prolonged object inherits
   the full Hopf algebra structure.
3. The non-degeneracy and vanishing conditions propagate from $A$ to
   $J^1(A)$ by functoriality.

In this sense, the
([recursive brane tower](#def:recursive-brane-tower)) is generated entirely by
iterating the categorical jet construction.  The tower, together with its
associated :refterm[descent]{#descent} ([Subsection](#ssec:descent)), is a formal consequence
of the axioms of a quantum observable universe and does not require any
case-by-case verification.
<!-- FILE_END: prolongation-categorical.md -->

<!-- FILE_START: recursive-brane-tower.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a
ring $R$ ([quantum observable universe](#def:quantum-observable-universe)).  Set
$A_0 = A$.  *Inductively*, define
$A_{n+1} = J^1(A_n)$ as the
([jet prolongation](#prop:jet-prolongation)) of the Frobenius--Hopf
object $A_n$.

The *brane relation* is the following recursive structure:

1. Each jet object $A_n$ serves as the base object for the next level;
   $A_n$ is the *brane* of $A_{n+1}$.
2. At each level, the comultiplication $\Delta_n$ on $A_n$ encodes
   the $n$-th level connection, inherited from the Frobenius--Hopf
   structure by [jet prolongation](#prop:jet-prolongation).

The **recursive brane tower** is the sequence
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
in $\mathbf{C}$, where each embedding is the canonical inclusion
$A_n \hookrightarrow J^1(A_n) = A_{n+1}$ via the unit section.
<!-- FILE_END: recursive-brane-tower.md -->

<!-- FILE_START: brane-tower-terminology.md -->
The mathematical content of this construction is strictly the iterated jet prolongation $A_{n+1} = J^1(A_n)$. We use the term *brane* for each localized layer $A_n$, viewed physically as a geometric boundary enclosing level-$n$ internal degrees of freedom.

The qualifier *Yekutieli* is reserved for the lifting condition \cite{yekutieli2010} governing when level $n$ extends to $n+1$, and the nonabelian multiplicative integration \cite{yekutieli2015} over the tower. These results control assembly, not the Kähler-differential jet object itself. We therefore write simply *(recursive) brane tower* for the sequence.
<!-- FILE_END: brane-tower-terminology.md -->

<!-- FILE_START: recursive-brane-tower-su2.md -->
Continuing [jet prolongation for SU(2)](#ex:jet-prolongation-su2), we
construct the [recursive brane tower](#def:recursive-brane-tower) for
$G = \mathrm{SU}(2)$.

**Level 0.** $A_0 = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring
of polynomial functions on $\mathrm{SU}(2)$.  As a representation of
$\mathrm{SU}(2)$, it decomposes as $A_0 \cong \bigoplus_{j \geq 0} V_j \otimes V_j^*$ (Peter--Weyl), where $V_j$ is the spin-$j$
representation of dimension $2j + 1$.

**Level 1.** $A_1 = J^1(A_0) = A_0 \otimes \Omega^1(A_0)$.  Since
$\Omega^1(A_0) \cong A_0 \otimes \mathfrak{su}(2)^*$ as an
$A_0$-module and $\mathfrak{su}(2)^* \cong V_1$ (the spin-$1$
representation), we have

$$
  A_1  \cong  \Gamma\bigl(F(\mathrm{SU}(2))\bigr),
$$

the sections of the frame bundle.  As a representation, each
Peter--Weyl summand $V_j \otimes V_j^*$ in $A_0$ contributes
$(V_j \otimes V_1) \otimes V_j^*$ in $A_1$, giving a $3$-fold
multiplicity increase.

**Level 2.** $A_2 = J^1(A_1) \cong \Gamma(J^2(\mathrm{SU}(2)))$,
sections of the second jet bundle.  Each representation factor picks
up another tensor with $V_1$, so the summands have the form
$(V_j \otimes V_1 \otimes V_1) \otimes V_j^*$.  The Clebsch--Gordan
decomposition $V_1 \otimes V_1 \cong V_0 \oplus V_1 \oplus V_2$ shows
that the growth stabilizes: no irreducible of spin $> j + 2$ appears at
level $2$ that is not already forced by the tensor product.

**Stabilization.** Since $\dim \mathrm{SU}(2) = 3$, the jet bundle
$J^k(\mathrm{SU}(2))$ has fibre dimension $\binom{k + 3}{3}$, which
grows polynomially.  However, the *tower of gerbes*
$\mathfrak{G}_0 \to \mathfrak{G}_1 \to \mathfrak{G}_2 \to \cdots$
stabilizes at level $n = 3$: for $n \geq 3$, the obstruction classes
$\kappa_n$ repeat the pattern set by $\kappa_0, \kappa_1, \kappa_2$,
because $H^2(\mathbb{CP}^1, \mathcal{O}^{\times}) \cong \mathbb{Z}$
is generated by a single class.

**The tower.** The brane tower for $\mathrm{SU}(2)$ is

$$
  A_0  \hookrightarrow  A_1  \hookrightarrow  A_2
   \hookrightarrow  \cdots
$$

where each embedding $A_n \hookrightarrow A_{n+1}$ is the unit section
of the jet prolongation, and $A_n$ is a
$(3^n \cdot \dim A_0)$-dimensional object in $\mathrm{Rep}(\mathrm{SU}(2))$.
<!-- FILE_END: recursive-brane-tower-su2.md -->

<!-- FILE_START: brane-tower-levels.md -->
Starting from an archimedean [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe) $(\mathbf{C}, \varTheta, G, \mathcal{S}_1)$, the fibre functor $\tau$ converts the categorical brane tower into a geometric tower of bundles. Here, $\mathcal{S}_{n+1}$ is the bundle of orthonormal frames of $J^1 \mathcal{S}_n$, and the connection $A_n$ on $\mathcal{S}_n$ satisfies the Hermitian Yang--Mills equations at each level. The first jet prolongation yields $\mathcal{S}_2$ over the base manifold $M_1 = \mathcal{S}_1$, where the connection $A_2$ is uniquely determined by [jet prolongation ($\mathbb{C}$)](#cor:jet-prolongation-C).
<!-- FILE_END: brane-tower-levels.md -->

<!-- FILE_START: arc-space.md -->
**Definition.**
*Let $X$ be a variety in $\mathbf{C}$ — typically the exceptional divisor of a collision locus, the singular state of a tangled braid, or a fluid blow-up ([recursive brane tower](#def:recursive-brane-tower)). Its **$n$-th jet scheme** $\mathcal{L}_n(X)$ is the scheme representing the functor*

$$
  R \;\longmapsto\;
  \mathrm{Hom}_{\mathrm{Sch}}\!\bigl(
    \mathrm{Spec}\,R[t]/(t^{n+1}),\; X
  \bigr).
$$

*The **arc space** of $X$ is the inverse limit*

$$
  \mathcal{L}(X)
  \;=\;
  \varprojlim_{n}\; \mathcal{L}_n(X).
$$

**Identification with the brane tower.** The QOU framework's recursive brane tower $\mathcal{S}_0 \hookrightarrow \mathcal{S}_1 \hookrightarrow \mathcal{S}_2 \hookrightarrow \cdots$ ([recursive brane tower](#def:recursive-brane-tower)) is a tower of jet schemes. The $n$-th jet prolongation $j^n v$ of a section $v$ ([jet prolongation](#prop:jet-prolongation)) is an $R$-point of $\mathcal{L}_n(X)$, and the inverse limit coincides with $\mathcal{L}(X)$:

$$
  \mathcal{S}_n \;\equiv\; \mathcal{L}_n(X),
  \qquad
  \mathcal{S}_\infty
  \;:=\;\varprojlim_n \mathcal{S}_n
  \;\equiv\;
  \mathcal{L}(X).
$$

**Role of arc spaces.** When the base $X$ is singular — a vortex reconnection, an exceptional divisor, or a braid resolution — the arc space $\mathcal{L}(X)$ retains the formal data required to evaluate the variety algebraically without analytic charts. This algebraic evaluation grounds the [motivic mass measure](#def:motivic-mass-measure), assigning a finite "volume" to subsets of $\mathcal{L}(X)$ even when $X$ lacks a smooth volume form.

Through the arc-space identification, the brane tower inherits motivic integration. The next step ([algebraic quantum volume](#def:algebraic-quantum-volume)) makes this measure explicit.
<!-- FILE_END: arc-space.md -->

