<!-- FILE_START: varying-euler-intro.md -->
The Descartes universe fixes Bring's surface ($\chi = -6$) as the spacetime base. However, the categorical substrate accommodates a family of base surfaces of varying Euler characteristic. This section identifies the categorical features that survive a choice other than Bring. We survey the commutative-limit variants: the genus-2 quintic, the hyperelliptic family, and the $\mathbb{Z}/5\mathbb{Z}$-Bring descent.

The argument proceeds in two steps. First, we track the commutative-limit reductions (Track A). The genus-2 quintic fixes the formal setup, the hyperelliptic classification catalogues candidate base surfaces, and the $x_5$-automorphism, Bring-descent, and Prym-Jacobian blocks identify Bring as the natural fixed point. Second, we record the $\mathrm{U}(1)$-equivariant reduction. This ties the family back to the substrate-parametrised gauge group, bridging to the subsequent representation-theoretic analysis.
<!-- FILE_END: varying-euler-intro.md -->

<!-- FILE_START: genus-2-intro.md -->
Throughout this chapter the varying-Euler-characteristic framework has
kept the genus of the base manifold open, with the genus-$4$ base
surface fixing one concrete representative.  We now examine a
second natural representative --- the genus-$2$ hyperelliptic curve
$\mathcal{X}_5 \colon y^2 = x^5 - 1$
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) --- and its
relationship to the genus-$4$ base geometry.

**Content of the subsection.**  The remainder of this subsection
treats $\mathcal{X}_5$ structurally:

* the strictly commutative QOU at the classical limit $q = 1$
  ([def:commutative-qou](#def:commutative-qou));
* the hyperelliptic quintic itself
  ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic));
* its classification among minimal-genus hyperelliptic curves with
  $\mathbb{Z}_5$-symmetry
  ([thm:hyperelliptic-z5-classification](#thm:hyperelliptic-z5-classification));
* the $\mathbb{Z}_5$-automorphism $(x, y) \mapsto (\zeta_5 x, y)$
  ([prop:x5-z5-automorphism](#prop:x5-z5-automorphism));
* :refterm[descent]{#descent} of this $\mathbb{Z}_5$ from the base surface's Sylow-$5$ subgroup
  ([rem:bring-z5-descent](#rem:bring-z5-descent));
* categorical identification of $x$ on $\mathcal{X}_5$ with the first
  Lagrange resolvent $w_1$ on the genus-$4$ base
  ([prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification));
* a $\mathrm{U}(1)$-equivariant reduction of the exceptional divisor
  ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

**Shared geometric anchor: the five fifth roots of unity.**  Among
the branch points of $\mathcal{X}_5 \to \mathbb{P}^1$ are the five
fifth roots of unity
$\{1, \zeta_5, \zeta_5^{2}, \zeta_5^{3}, \zeta_5^{4}\}$.  The same
discrete set appears in the Lagrange-resolvent diagonalisation of
the cyclic subgroup $C_5 \subset S_5$ acting on the genus-$4$ base surface
([prop:lagrange-resolvent-transform](#prop:lagrange-resolvent-transform))
and, separately, as the truncation points of the root-of-unity
specialisation $q = \zeta_5$ treated in a later chapter
([def:observable-mtc](#def:observable-mtc)).  The weight
identification of
[prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification)
ties the first two occurrences together categorically: the coordinate
$x$ on $\mathcal{X}_5$ and the first Lagrange resolvent $w_1$ on the genus-$4$ base
are canonically identified at the level of $\mathbb{Z}_5$-weight-$(-1)$
isotypical components of their coordinate rings.
<!-- FILE_END: genus-2-intro.md -->

<!-- FILE_START: hyperelliptic-z5-classification.md -->
**Theorem.**
Let $X$ be a smooth projective Riemann surface of minimal genus satisfying two conditions:

*(i)* $X$ is hyperelliptic. There exists a degree-2 morphism $\pi \colon X \to \mathbb{P}^1$ with involution $\iota$.
*(ii)* $X$ admits a faithful $\mathbb{Z}_5$ automorphism $\phi$ commuting with $\iota$.

Then $g(X) = 2$. The surface $X$ is isomorphic to $\mathcal{X}_5 \colon y^2 = x^5 - 1$ ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)).
<!-- FILE_END: hyperelliptic-z5-classification.md -->

<!-- FILE_START: hyperelliptic-z5-classification-interpretation.md -->
1. **Fixed-point symmetry.** The two $\mathbb{Z}_5$-fixed points $0$ and $\infty$ of $\mathbb{P}^1$ play symmetric roles. Either can serve as the sixth branch point. The resulting curves are canonically isomorphic. Thus, we refer to $\mathcal{X}_5$ in the singular.

2. **The minimality is tight.** Dropping minimality permits $|\mathrm{Branch}(\pi)| \in \{10, 12, 14, \ldots\}$, yielding genera $g \in \{4, 5, 6, \ldots\}$. The $g = 4$ case with two size-5 orbits is the neighbourhood of Bring's curve. Higher cases constitute Galois covers of $\mathcal{X}_5$ or degenerations.

3. **No inheritance from Bring.** Condition (ii) requires only a faithful $\mathbb{Z}_5$. It does not require this $\mathbb{Z}_5$ to be a Sylow subgroup of a larger symmetry group. Identifying this abstract $\mathbb{Z}_5$ with the Sylow-5 residue of Bring's $S_5$ is a distinct structural assertion. The explicit computation in [rem:bring-z5-descent](#rem:bring-z5-descent) provides the justification.
<!-- FILE_END: hyperelliptic-z5-classification-interpretation.md -->

<!-- FILE_START: bring-z5-descent.md -->
**Remark.**
The $\mathbb{Z}_5$ automorphism of $\mathcal{X}_5$ established in
[prop:x5-z5-automorphism](#prop:x5-z5-automorphism) is the residue on
$\mathcal{X}_5$ of a Sylow 5-subgroup of the $S_5$ automorphism group
of [Bring's surface](#def:brings-surface).

**Classical fact** \cite{edge1978}.  Bring's curve $\mathcal{B}_{\mathrm{Br}}$
carries a faithful action of $S_5$ of order $120$.  The six Sylow
5-subgroups of $S_5$ each have order $5$, generated by a $5$-cycle.
Picking one such $5$-cycle $\tau \in S_5$, the quotient
$\mathcal{B}_{\mathrm{Br}} / \langle \tau \rangle$ is a hyperelliptic
curve of genus $2$ with residual automorphism
$\mathbb{Z}_5 \cong \langle \tau \rangle$ descending to the quotient.
Up to isomorphism this genus-$2$ quotient is the
$\mathcal{X}_5 \colon y^2 = x^5 - 1$ of Definition
[def:hyperelliptic-quintic](#def:hyperelliptic-quintic).

**Conclusion.**  Taking the $S_5$-invariant quotient of Bring's
genus-$4$ geometry and retaining the cyclic Sylow-5 residue gives
a natural genus-$2$ shadow of the full Descartes structure.  The
$A_5$-invariant complement --- the non-abelian structure that
accommodates three color tubes --- is discarded under this
restriction, consistent with the collapse to a single
$\mathrm{U}(1)$ phase tube recorded in
[prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction).

We do not reproduce the :refterm[descent]{#descent} calculation here; Edge \cite{edge1978}
gives the full treatment of genus-reduction quotients of Bring's
curve.
<!-- FILE_END: bring-z5-descent.md -->

<!-- FILE_START: x5-bring-prym-jacobian.md -->
**Remark (Jacobian-level parallel).**
The weight identification in [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification) has a Jacobian-level analogue. Let $H^{1}(\,\cdot\,, \mathbb{Q})$ denote rational first cohomology. Both $H^{1}(\mathcal{X}_5, \mathbb{Q})$ and $H^{1}(\mathcal{B}_{\mathrm{Br}}, \mathbb{Q})$ carry natural $\mathbb{Z}_5$-actions. The non-trivial $\mathbb{Z}_5$-isotypical decomposition is identical:

$$
  H^{1}(\mathcal{X}_5, \mathbb{Q})_{\neq 0}
    =  \chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4
    =  H^{1}(\mathcal{B}_{\mathrm{Br}}, \mathbb{Q})_{\neq 0}^{\mathrm{cyc}},
$$

where $\chi_k$ is the character $\sigma \mapsto \zeta_5^{\,-k}$. The right-hand side is the non-trivial $\mathbb{Z}_5$-isotypical part of Bring's rational $H^1$. The remaining weight-$0$ summand sits in the $S_5$-standard isotype and ignores the cyclic structure.

**Absence of a Prym embedding.** Bring's curve lacks a genus-$2$ Galois quotient. Consequently, the standard Prym construction provides no direct embedding $J(\mathcal{X}_5) \hookrightarrow J(\mathcal{B}_{\mathrm{Br}})$. The character equality instead records a compatibility of $\mathbb{Z}_5$-representations. Both Jacobians manifest the same non-trivial $\mathbb{Z}_5$-structure on abelian varieties of different dimensions via different curve geometries.

**Significance.** Combined with [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification), the coordinate and Jacobian compatibilities demonstrate that the cyclic $\mathbb{Z}_5$-observable structure of the genus-$2$ substrate $\mathcal{X}_5$ faithfully shadows the cyclic observable structure of the full $S_5$-substrate (Bring). Passing from Bring to $\mathcal{X}_5$ discards the $A_5$-factor but preserves the cyclic Sylow-$5$ residue exactly. Edge \cite{edge1978} documents the classical relation between Bring and its hyperelliptic quotients. We extract the categorical conclusion: both surfaces carry compatible $\mathbb{Z}_5$-graded coordinate rings.
<!-- FILE_END: x5-bring-prym-jacobian.md -->

<!-- FILE_START: weight-identification-consequences.md -->
**Remark.**
The categorical identification of [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification) unifies several threads in this paper. We record three consequences.

**1. Computability of the spectral coordinate $w_1$.** In the Descartes chapter, *evaluation in spectral coordinates* refers to the first Lagrange resolvent $w_1$ on Bring's surface, an abstract Fourier mode of a complete intersection in $\mathbb{P}^4$. The weight identification canonically equates every such evaluation with the evaluation of the affine coordinate $x$ on the hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$. The former is a five-term sum on a degree-$120$-symmetric surface; the latter is an elementary plane-curve coordinate. The $\mathcal{X}_5$ formulation is computationally and formally simpler.

**2. Alignment of $\mathbb{Z}_5$-isotype dimensions with $T_{2,3}$ and $T_{2,5}$.** Under the weight identification, the non-trivial $\mathbb{Z}_5$-isotypical part of $H^1(\mathcal{X}_5, \mathbb{Q})$ is the four-dimensional character sum $\chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4$. Equivalently, $J(\mathcal{X}_5)$ has complex dimension $2$. This four-dimensional rational isotype is precisely filled by the Seifert surface of the Solomon-seal torus knot $T_{2,5}$ (Seifert genus $2$, $\dim H^1 = 4$ over $\mathbb{Q}$). A two-dimensional sub-isotype is filled by the trefoil $T_{2,3}$ (Seifert genus $1$). The match between representation-theoretic dimensions and Seifert dimensions for these two knots follows directly from cyclic representation theory on $\mathcal{X}_5$.

**3. Equivalence of a $\mathrm{U}(1)$ phase tube and a single observed cyclic weight.** The collapse of three Descartes color tubes to a single $\mathrm{U}(1)$ phase tube ([rem:u1-phase-tube](#rem:u1-phase-tube)) has a precise weight-graded interpretation. The full non-commutative theory keeps all five Lagrange weights $\zeta_5^{\,0}, \zeta_5^{\,-1}, \zeta_5^{\,-2}, \zeta_5^{\,-3}, \zeta_5^{\,-4}$ distinguishable as separate observable channels (the trivial weight, three colour tubes, and a chiral conjugate, organised by $\mathrm{SU}(3)$-triality from $S_5$). The commutative-limit theory keeps only the weight-$(-1)$ channel visible, canonically identified with $x$ on $\mathcal{X}_5$. "One tube" therefore means exactly one observed non-trivial $\mathbb{Z}_5$-weight.

**Application in prior blocks.** Two existing blocks incorporate this identification where the $w_1$ / $\mathbb{Z}_5$ structure plays a direct role. [rem:t211-ideal-annihilation](#rem:t211-ideal-annihilation) gains a representation-theoretic origin for the $T_{2,3}$ / $T_{2,5}$ row of its embeddability table. [rem:color-tube-constraints](#rem:color-tube-constraints) gains a commutative-limit specialisation that maps the full $S_5$-symmetric color system to the single $\mathrm{U}(1)$ tube on $\mathcal{X}_5$. We defer rewriting the Descartes chapter to express "evaluation in spectral coordinates" via $\mathcal{X}_5$ coordinates to a subsequent pass.
<!-- FILE_END: weight-identification-consequences.md -->

<!-- FILE_START: u1-phase-tube.md -->
**Remark (physical interpretation).**
The $\mathrm{U}(1)$-equivariant reduction of [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction) admits a compact physical reading. The three color tubes of the Descartes chapter (the non-abelian observable channels $\mathfrak{u}$, $\mathfrak{d}$, $\mathfrak{s}$ and their cyclic images) originate from the $S_5$-symmetric action on the genus-$4$ Bring geometry. This geometry lifts to a normal bundle structure on the exceptional divisor supporting three distinct $\mathrm{SU}(3)$-triality-compatible fibres.

In the commutative-limit specialisation ([def:commutative-qou](#def:commutative-qou)), the representation theory truncates to the maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$. By [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction), $\mathrm{U}(1)$-equivariant observables on $\mathcal{S}_p$ reduce to a single phase coordinate $\varphi \in S^1$. All three non-abelian tubes of the Descartes universe are consequently indistinguishable at the level of observables. They collapse to **one $\mathrm{U}(1)$ phase tube**.

**Weight-graded reading.**
Under the weight identification of [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification), this collapse acquires a sharp $\mathbb{Z}_5$-representation-theoretic content. The full non-commutative theory keeps the five Lagrange weights $\zeta_5^{\,0}, \zeta_5^{\,-1}, \ldots, \zeta_5^{\,-4}$ distinguishable as separate observable channels (the trivial weight, three colour tubes, and a chiral conjugate). The commutative-limit theory keeps only the weight-$(-1)$ channel visible and identifies it canonically with the single coordinate $x \in \mathcal{O}(\mathcal{X}_5)$. The "single phase tube" is *precisely* the weight-$(-1)$ isotypical component of the $\mathbb{Z}_5$-graded coordinate ring, not a vague geometric collapse.

**Branch-point localisation.**
On the genus-$2$ curve $\mathcal{X}_5$ ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)), the five branch points $\zeta_5^{k}$ of the double cover lie symmetrically along the unit circle of the $x$-plane. Via the identification of $x$ with the Lagrange resolvent $w_1$ (Remark [rem:lagrange-resolvents](#rem:lagrange-resolvents)), these five roots of unity pick out five preferred phase values $\varphi_k = 2\pi k / 5$ on the single $\mathrm{U}(1)$ tube. These are the positions on the phase circle where the double-cover monodromy is non-trivial and where the local variation of $q$ on the base manifold sees topological defects. The smooth $\mathrm{U}(1)$ flow between them is the commutative-limit analogue of the color-sector braid currents of the Descartes chapter.

**No anyons here.**
Because the braiding is symmetric in the commutative limit, these defects are not anyonic. They carry $S_n$-statistics. The anyonic counterpart belongs to the root-of-unity specialisation ([def:observable-mtc](#def:observable-mtc)) treated in the fluid dynamics chapter.
<!-- FILE_END: u1-phase-tube.md -->

<!-- FILE_START: descent-mirror-intro.md -->

<!-- FILE_END: descent-mirror-intro.md -->

<!-- FILE_START: e-minus-one.md -->
In the :refterm[descent]{#descent} from $\mathcal{S}_1$ (full torsion bundle) to $\mathcal{S}_0$ (trivial
bundle), the self-duality of spacetime and color admits a flip: the
orientation of the color fibre can reverse relative to the spacetime
base.  This produces a bundle $\mathcal{S}_{-1}$ that acts as a skew or mirror
image of $\mathcal{S}_1$.  From the perspective of ascending the bundle hierarchy,
$\mathcal{S}_{-1}$ appears to be matter; from the perspective of descending, it
appears to be antimatter.  The distinction is purely one of orientation
in the :refterm[descent]{#descent} tower.
<!-- FILE_END: e-minus-one.md -->

