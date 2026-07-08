<!-- FILE_START: jet-prolongation-intro.md -->
This chapter extends the quantum observable universe $(\mathbf{C}, A, \tau)$ into a recursive hierarchy. Each level $A_n$ of this tower forms the jet prolongation of the previous one. The subsequent mechanisms of lifting, descent, and mass decomposition rely strictly on this tower. This section formally constructs it.

We first establish that the jet object $J^1(A) = A \otimes \Omega^1(A)$ strictly inherits the Frobenius–Hopf structure and fibre functor, making $(\mathbf{C}, J^1(A), \tau', q)$ a valid QOU. Iterating this procedure algebraically generates the recursive brane tower $\{A_n\}_{n \geq 0}$. We then examine the smooth geometric model $J^1\mathcal{S}_n$ and define the arc space $\mathcal{L}(X)$, which rigorously assembles the levels into a single ind-scheme. This tower provides the formal carrier for defining torsion and transport.
<!-- FILE_END: jet-prolongation-intro.md -->

<!-- FILE_START: jet-prolongation.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a ring $R$ ([quantum observable universe](#def:quantum-observable-universe)). We define the *jet object*:
$$
  J^1(A) := A \otimes \Omega^1(A),
$$
where $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$ is the bimodule of Kähler differentials. The space $J^1(A)$ inherits a canonical Frobenius–Hopf structure directly from $A$. The quadruple $(\mathbf{C}, J^1(A), \tau', q)$—with the induced fibre functor $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$—forms a quantum observable universe over $R$.
<!-- FILE_END: jet-prolongation.md -->

<!-- FILE_START: jet-prolongation-su2.md -->
We explicitly construct the [jet prolongation](#prop:jet-prolongation) of $A = \mathcal{O}(\mathrm{SU}(2))$.

**Kähler differentials.** The module of Kähler differentials is $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$. For the left-invariant calculus on $\mathrm{SU}(2)$, this yields:
$$
  \Omega^1(A) = \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$
where $\omega_a$ are the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The jet object.** By definition:
$$
  J^1(A) := A \otimes \Omega^1(A) \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}.
$$
As a vector space, $J^1(A)$ consists of $\mathcal{O}(\mathrm{SU}(2))$-valued $1$-forms on $\mathrm{SU}(2)$. These exactly match the sections of the frame bundle $F(\mathrm{SU}(2))$.

**Inherited Frobenius–Hopf structure.** The comultiplication on $J^1(A)$ reads:
$$
  \Delta'(f \otimes \varTheta)(x, y) = f(xy) \otimes \varTheta_y,
$$
where $\varTheta_y$ denotes the left-translate of $\varTheta$ to $T_y G$. The counit $\varepsilon'(f \otimes \varTheta) = f(e)\varTheta_e$ and antipode $S'(f \otimes \varTheta)(x) = f(x^{-1}) \otimes (L_{x^{-1}})^*\varTheta$ extend similarly. The Frobenius form identically integrates the $1$-form component over $G$ via the Haar measure: $\int_{J^1 A}(f \otimes \varTheta) = \int_G f\varTheta$.

**QOU structure.** The induced fibre functor $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$ retains the $1$-form structure while forgetting the $G$-action on sections. Because $\mathrm{SU}(2)$ is $3$-dimensional, $J^1(A)$ acts as a $3$-fold extension of $A$, forcing $\dim_{\tau'} J^1(A) = 3 \cdot \dim_\tau A$. The quadruple $(\mathrm{Rep}(\mathrm{SU}(2)), J^1(A), \tau', q)$ formally constitutes a quantum observable universe.
<!-- FILE_END: jet-prolongation-su2.md -->

<!-- FILE_START: jet-prolongation-categorical-jet.md -->
*The categorical jet object $J^1(A) := A \otimes \Omega^1(A)$—where $\Omega^1(A) = \ker(m\colon A\otimes A \to A)$ is the bimodule of Kähler differentials—acts as an object of the ambient rigid monoidal category and strictly inherits a Frobenius–Hopf structure $(\Delta', \varepsilon', S')$ from $A$.*
<!-- FILE_END: jet-prolongation-categorical-jet.md -->

<!-- FILE_START: prolongation-categorical.md -->
Jet prolongation emerges strictly as an intrinsic consequence of the Frobenius–Hopf structure within a rigid monoidal category. It requires no geometric input beyond the categorical data $(\mathbf{C}, A, \tau)$. Concretely:
1. The Frobenius structure supplies the Kähler differentials $\Omega^1(A)$ as a direct summand, completely defining the jet object $J^1(A)$.
2. The Frobenius relation enforces compatibility between comultiplication and multiplication, ensuring the prolonged object inherits the complete Hopf algebra structure.
3. Non-degeneracy and vanishing conditions naturally propagate from $A$ to $J^1(A)$ through functoriality.

Iterating this categorical jet construction entirely generates the recursive brane tower. The tower and its associated descent ([Subsection](#ssec:descent)) structurally follow from the QOU axioms without case-by-case verification.
<!-- FILE_END: prolongation-categorical.md -->

<!-- FILE_START: recursive-brane-tower.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a ring $R$. We set $A_0 = A$. *Inductively*, we define $A_{n+1} = J^1(A_n)$ as the jet prolongation of the Frobenius–Hopf object $A_n$.

The *brane relation* enforces a recursive structure:
1. Each jet object $A_n$ acts as the base object for the next level; $A_n$ geometrically forms the *brane* of $A_{n+1}$.
2. The comultiplication $\Delta_n$ on $A_n$ explicitly encodes the $n$-th level connection, strictly inherited via jet prolongation.

The **recursive brane tower** defines the sequence
$$
  A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots
$$
in $\mathbf{C}$, where each embedding acts as the canonical inclusion $A_n \hookrightarrow J^1(A_n) = A_{n+1}$ through the unit section.
<!-- FILE_END: recursive-brane-tower.md -->

<!-- FILE_START: brane-tower-terminology.md -->
The mathematics here strictly traces the iterated jet prolongation $A_{n+1} = J^1(A_n)$. We assign the term *brane* to each localized layer $A_n$, representing a geometric boundary enclosing level-$n$ internal degrees of freedom.

We reserve the qualifier *Yekutieli* for the lifting condition \cite{yekutieli2010} that governs extensions from $n$ to $n+1$, and for the nonabelian multiplicative integration \cite{yekutieli2015} over the tower. These results control structural assembly rather than the Kähler-differential jet object itself. We therefore write simply *(recursive) brane tower* for the sequence.
<!-- FILE_END: brane-tower-terminology.md -->

<!-- FILE_START: recursive-brane-tower-su2.md -->
Continuing the [jet prolongation for SU(2)](#ex:jet-prolongation-su2), we construct the explicit brane tower for $G = \mathrm{SU}(2)$.

**Level 0.** $A_0 = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring of polynomial functions on $\mathrm{SU}(2)$. As an $\mathrm{SU}(2)$ representation, it decomposes via Peter–Weyl as $A_0 \cong \bigoplus_{j \geq 0} V_j \otimes V_j^*$, where $V_j$ denotes the spin-$j$ representation of dimension $2j + 1$.

**Level 1.** $A_1 = J^1(A_0) = A_0 \otimes \Omega^1(A_0)$. Because $\Omega^1(A_0) \cong A_0 \otimes \mathfrak{su}(2)^*$ and $\mathfrak{su}(2)^* \cong V_1$, we strictly obtain:
$$
  A_1 \cong \Gamma\bigl(F(\mathrm{SU}(2))\bigr),
$$
the sections of the frame bundle. Each Peter–Weyl summand $V_j \otimes V_j^*$ in $A_0$ explicitly contributes $(V_j \otimes V_1) \otimes V_j^*$ in $A_1$, dictating a $3$-fold multiplicity increase.

**Level 2.** $A_2 = J^1(A_1) \cong \Gamma(J^2(\mathrm{SU}(2)))$, the sections of the second jet bundle. Each representation factor gains another tensor with $V_1$, yielding summands of the form $(V_j \otimes V_1 \otimes V_1) \otimes V_j^*$. The Clebsch–Gordan decomposition $V_1 \otimes V_1 \cong V_0 \oplus V_1 \oplus V_2$ explicitly caps the growth: no irreducible representation of spin $> j + 2$ appears at level $2$ unless the tensor product strictly forces it.

**Stabilization.** Because $\dim \mathrm{SU}(2) = 3$, the jet bundle $J^k(\mathrm{SU}(2))$ has a polynomially growing fibre dimension $\binom{k + 3}{3}$. However, the *tower of gerbes* $\mathfrak{G}_0 \to \mathfrak{G}_1 \to \mathfrak{G}_2 \to \cdots$ physically stabilizes at level $n = 3$. For $n \geq 3$, the obstruction classes $\kappa_n$ strictly repeat the pattern set by $\kappa_0, \kappa_1, \kappa_2$ because a single class identically generates $H^2(\mathbb{CP}^1, \mathcal{O}^{\times}) \cong \mathbb{Z}$.

**The tower.** The complete brane tower for $\mathrm{SU}(2)$ is:
$$
  A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots
$$
where each embedding acts as the unit section of the jet prolongation. Each $A_n$ forms a $(3^n \cdot \dim A_0)$-dimensional object in $\mathrm{Rep}(\mathrm{SU}(2))$.
<!-- FILE_END: recursive-brane-tower-su2.md -->

<!-- FILE_START: brane-tower-levels.md -->
Starting from an archimedean [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe) $(\mathbf{C}, \varTheta, G, \mathcal{S}_1)$, the fibre functor $\tau$ geometrically converts the categorical brane tower into a bundle tower. Here, $\mathcal{S}_{n+1}$ defines the orthonormal frame bundle of $J^1 \mathcal{S}_n$. The connection $A_n$ on $\mathcal{S}_n$ strictly satisfies the Hermitian Yang–Mills equations at each level. The first jet prolongation uniquely constructs $\mathcal{S}_2$ over the base manifold $M_1 = \mathcal{S}_1$, fully determining the connection $A_2$ via [jet prolongation ($\mathbb{C}$)](#cor:jet-prolongation-C).
<!-- FILE_END: brane-tower-levels.md -->

<!-- FILE_START: arc-space.md -->
**Definition.**
*Let $X$ be a variety in $\mathbf{C}$—typically the exceptional divisor of a collision locus, the singular state of a tangled braid, or a fluid blow-up. Its **$n$-th jet scheme** $\mathcal{L}_n(X)$ rigorously represents the functor:*
$$
  R \longmapsto \mathrm{Hom}_{\mathrm{Sch}}\!\bigl(\mathrm{Spec}\,R[t]/(t^{n+1}),\; X\bigr).
$$
*The **arc space** of $X$ is the formal inverse limit:*
$$
  \mathcal{L}(X) = \varprojlim_{n} \mathcal{L}_n(X).
$$

**Identification with the brane tower.** The QOU framework's recursive brane tower $\mathcal{S}_0 \hookrightarrow \mathcal{S}_1 \hookrightarrow \cdots$ mathematically forms a tower of jet schemes. The $n$-th jet prolongation $j^n v$ of a section $v$ acts as an $R$-point of $\mathcal{L}_n(X)$. The inverse limit physically coincides with $\mathcal{L}(X)$:
$$
  \mathcal{S}_n \equiv \mathcal{L}_n(X), \qquad \mathcal{S}_\infty := \varprojlim_n \mathcal{S}_n \equiv \mathcal{L}(X).
$$

**Role of arc spaces.** When the base $X$ is singular—a vortex reconnection, an exceptional divisor, or a braid resolution—the arc space $\mathcal{L}(X)$ safely retains the formal data necessary to evaluate the variety algebraically without analytic charts. This algebraic evaluation grounds the [motivic mass measure](#def:motivic-mass-measure), predictably assigning a finite volume to subsets of $\mathcal{L}(X)$ even when $X$ inherently lacks a smooth volume form.

Through this arc-space identification, the brane tower natively inherits motivic integration. The [algebraic quantum volume](#def:algebraic-quantum-volume) formally makes this measure explicit.
<!-- FILE_END: arc-space.md -->

