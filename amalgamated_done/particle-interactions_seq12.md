<!-- FILE_START: hadron-algebra-intro.md -->
The previous section produced a relation algebra on Hecke generators. We now use those relations to single out configurations that bind into stable composites. We define a hadron as a knot composite whose Coulomb charge and crossing energy place it in the stability stratum of the relation algebra. An algebraic Gröbner reduction then factorizes any closed strand uniquely into hadron constituents.

This section defines the hadron and its stability condition. We establish well-definedness through existence and uniqueness: the stability stratum is non-empty, and any two minimal-energy representatives differ by a braid isotopy. We record the natural product, sum, and conjugation operations on hadrons. We connect knot factorization to the Pawlowski--Leitner basis. Finally, we define the localized hadron by adding a marked point at which the categorical mass concentrates. We package this localization as a fibre-compatible embedding for the upstream Möbius-energy machinery.

The subsequent section uses the hadron-factorization result to establish the dictionary between knot composites and physical particles.
<!-- FILE_END: hadron-algebra-intro.md -->

<!-- FILE_START: hadron.md -->
A *hadron* is a stable composite of fundamental knots. Its crossing energy is strictly negative, ensuring topological binding dominates repulsion.

Let $K_1, \ldots, K_n$ be prime knot types in the representation category $\mathbf{C}$. Let $\mathcal{L}$ be a link encoding their internal entanglement. A **hadron** is a composite

$$
  \mathfrak{H}_p = [K_1, \ldots, K_n]_p \oplus \mathcal{L}
$$

satisfying the **stability condition**:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}_p) < 0.
$$

The subscript $p$ specifies the localization point. The operator $\oplus$ denotes linking.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. Categorical identities hold over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hadron.md -->

<!-- FILE_START: hadron-exists.md -->
**Proposition.**
There exists a composite $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ satisfying the stability condition $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}_p) < 0$.

Uniqueness of the hadron at a given crossing partition is established subsequently.
<!-- FILE_END: hadron-exists.md -->

<!-- FILE_START: hadron-unique.md -->
**Theorem.**
Two hadrons sharing a crossing partition, localisation point $p$, and Hecke normal form coincide up to braid isotopy.

The Hecke normal form furnishes a canonical representative. Thus, uniqueness denotes uniqueness of the Hecke class in the algebra $H_n(R, q)$.
<!-- FILE_END: hadron-unique.md -->

<!-- FILE_START: hadron-interpretation.md -->
Arbitrary knot composites are not stable. Only composites whose $R$-matrix braiding yields net binding qualify as hadrons. The Coulomb charge $Q(\mathfrak{H})$ measures the electromagnetic character of this composite.

The integer $n$ counts the constituent knots and defines the *valence*. A valence of $3$ yields a **baryon**; a valence of $2$ yields a **meson**.

This definition remains abstract. The Euler characteristic $\chi(A)$ in the Descartes universe dictates the specific torus knots serving as generators.
<!-- FILE_END: hadron-interpretation.md -->

<!-- FILE_START: hadron-operations-closure.md -->
**Proposition.**
Let $\mathbf{C}$ be a rigid braided monoidal category and let $\mathfrak{H} \in \mathrm{Sym}^n(K)$ be a hadron with constituent knots $K_1, \ldots, K_n$.

1. **Braiding closure.** The braiding $\beta_{K_i, K_j}$ descends to an involution on $\mathrm{Sym}^n(K)$. For the antisymmetric product, exchanging identical constituents produces $-1$.
2. **Hopf linking closure.** The linking operation $\ell_{ij} \colon K_i \otimes K_j \to K_i \mathbin{\#_{\mathrm{Hopf}}} K_j$ is an endomorphism of $\mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ with a two-sided inverse when the linking number is trivial.
3. **Skein closure.** The $q$-deformed skein relation resolves any linked composite into a polynomial in $q$ times unlinked constituents, yielding the mass formula $\mathcal{M}(\mathfrak{H}) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}) + \sum_i \mathcal{M}(K_i)$.
4. **Fusion closure.** For hadrons $\mathfrak{H}_1 \in \mathrm{Sym}^{n_1}(K)$ and $\mathfrak{H}_2 \in \mathrm{Sym}^{n_2}(K)$, the fusion $\mathfrak{H}_1 \star \mathfrak{H}_2 \in \mathrm{Sym}^{n_1 + n_2}(K)$ is again a hadron.
<!-- FILE_END: hadron-operations-closure.md -->

<!-- FILE_START: hadron-operations.md -->
The braiding and Hopf link structure of $\mathbf{C}$ induce natural operations on the symmetric product $\mathrm{Sym}^n(K)$.

**Braiding.** The braiding $\beta_{K_i, K_j}$ permutes constituent knots within a hadron. Because $\mathrm{Sym}^n$ quotients by the symmetric group action, this descends to an involution.

**Hopf linking.** Two knots link via the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$. The linking operation replaces two constituents with a linked pair. The inverse decomposes a linked pair when the linking number is trivial.

**Skein action.** The $q$-deformed Skein relations act on $\mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ by resolving link crossings. Iterating across all crossings resolves the composite into unlinked constituents scaled by a polynomial in $q$.

**Fusion.** We fuse two hadrons by constructing the Hopf link between their binding structures. This provides a categorical model for hadron scattering.
<!-- FILE_END: hadron-operations.md -->

<!-- FILE_START: knot-factorization.md -->
The tensor generation property of the fundamental object $V$ implies every constituent knot type $K_i$ factors through a tensor power of $V$.

If $K_i$ has associated simple object $V_{j_i}$, then $V_{j_i}$ appears as a direct summand of $V^{\otimes 2j_i}$. The Pawlowski--Leitner basis provides a canonical embedding, so a hadron $\mathfrak{H}$ can be written in a universal tensor form:

$$
  \mathfrak{H}  \hookrightarrow 
  V_{1/2}^{\otimes 2(j_1 + \cdots + j_n)}.
$$

This embedding corresponds to a choice of partial-wave channel. The physical hadron is obtained by summing over all channels weighted by the Skein polynomial.

In the QOU framework, this factorization explains why all composite particles are built from $V$. The categorical dimension $2$ of $V$ is the minimal non-trivial dimension compatible with the volume constraint.
<!-- FILE_END: knot-factorization.md -->

<!-- FILE_START: localized-hadron.md -->
A localized hadron is a hadron placed at a categorical point $p$ of the projective line $\mathbb{P}(V)$.

Formally, a **localized hadron** at $p$ is a morphism in $\mathbf{C}$:

$$
  H_p  \colon  \mathbf{1}
   \longrightarrow 
  \mathrm{Sym}^n\!\bigl(\mathcal{K}_p\bigr)
  \otimes
  \mathcal{L}_{p}^{\mathrm{bind}}
$$

where $\mathcal{K}_p$ denotes the fibre of knot types at $p$ and $\mathcal{L}_{p}^{\mathrm{bind}}$ is the binding Hopf link at $p$. The morphism distinguishes a localized hadron from an abstract one.
<!-- FILE_END: localized-hadron.md -->

<!-- FILE_START: hadron-fibre-embedding.md -->
Abstract hadrons encode topological data algebraically. To represent a physical particle, this data must embed into the geometric fibre of the knot bundle over spacetime. 

Let $\mathfrak{H} \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ be a hadron. Let $\mathcal{S}_p$ denote the fibre over a point $p \in \mathbb{P}(V)$. A **fibre-compatible hadron embedding** is a morphism

$$
  \iota_p \colon \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}} \longrightarrow \mathcal{S}_p
$$

satisfying four conditions.

1. **Integrability.** The abstract Skein action intertwines with the geometric operations on knots in $\mathcal{S}_p$.
2. **Fibre confinement.** The image $\iota_p(\mathfrak{H})$ lies entirely in $\mathcal{S}_p$. A finite Möbius energy bound enforces this, preventing the knot complement from developing cusps that reach the fibre boundary.
3. **Hopf compatibility.** The embedding respects the Hopf structure.
4. **Volume compatibility.** The embedding preserves hyperbolic volumes: $\mathrm{vol}(\iota_p(K_i)) = \mathrm{vol}(K_i)$.

A localized hadron with a fibre-compatible embedding is a **physically realized hadron**. The integrability condition ensures the algebraic structure admits a strict geometric realization.
<!-- FILE_END: hadron-fibre-embedding.md -->
