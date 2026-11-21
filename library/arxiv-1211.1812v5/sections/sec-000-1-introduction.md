---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 2-5
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.99
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#intro label="intro"}

In the ordinary approach to the theory of particle physics quantum fields are fundamental objects, but do not necessarily yield quantum observables because the property of gauge invariance with respect to a symmetry group must be imposed.

In algebraic quantum field theory this point of view is subverted: at a first stage only quantum observables are considered, in the spirit that these contain all the physical informations of the system under consideration.

Thus one could ask whether the observable quantities determine the quantum fields and the gauge group, and the answer to this question is a pivotal result: quantum fields and gauge group can be reconstructed, starting from the observable algebra and the set, called the superselection structure, of its physically relevant Hilbert space representations (*sectors*), that are interpreted as quantum charges ([@DR90]).

A celebrated mathematical byproduct is the Doplicher-Roberts duality for compact groups vs. *abstract* symmetric tensor categories, that generalizes Tannaka-Krein duality ([@DR89]).

The mathematical scenario of the above construction is the one defined by Haag, Kastler and then Araki in the middle sixties ([@Ara Chp.4],[@Haa Chp.III]): we have a base $\Delta_{dc}$ of the Minkowski spacetime, the one of double cones, and, for any $o \in \Delta_{dc}$, a *C\**-algebra $A_o$ that is interpreted as the one of quantum observables localized within $o$. Starting from this interpretation, it is natural to require that there are inclusion \*-morphisms

$$\label{eq.00}
\jmath_{o'o} : A_o \to A_{o'}
\ \ : \ \
\jmath_{o'' o'} \circ \jmath_{o'o} = \jmath_{o'' o}
\ \ , \ \
\forall o \subseteq o' \subseteq o'' \in \Delta_{dc}
\ .$$

The pair $\EuFrak{A}:= (A,\jmath)$ is known as the *observable net* and is usually -- but not always -- realized by means of quantum fields in the sense of Wightman ([@Ara §4.8]). An important point is that $\Delta_{dc}$ is a directed *poset* (partially ordered set) when ordered under inclusion, and this implies that we can construct the inductive limit *C\**-algebra $\vec{A} := \lim_j (A,\jmath)$ that can be represented as a \*-algebra of operators on a fixed Hilbert space. The superselection structure is then realized as a symmetric tensor *C\**-category $T$ of \*-endomorphisms of $\vec{A}$, and characterized as the dual of the compact gauge group $G$. This means, in particular, that any $\rho \in {\bf obj \ }T$ defines a finite-dimensional, unitary representation

$$\label{eq.rep}
u_\rho : G \to UH_\rho$$

such that $H_\rho$ appears in the field algebra as the $G$-vector space spanned by a multiplet of field operators

$\psi_1 , \ldots , \psi_{{\mathrm{dim}}(u_\rho)}$,

see ([@DR90]).

Now, for generic spacetimes $M$ in algebraic quantum field theory it is customary to select a convenient base $\Delta$, according to the causal properties and symmetries of $M$. In in this way one obtains, for example,

the base of intervals with proper closure for the circle in conformal theory, and the base of *diamonds* generating the topology of a globally hyperbolic spacetime, that is the setting of general relativity

[^1].

We note that when elements of $\Delta$ are arcwise and simply connected (as intervals, double cones and diamonds), we are able to recover base-independent invariants of $M$:

the fundamental group $\pi_1(M)$ ([@Ruz05]), the first singular and de Rham cohomology ([@RRV08]) and the category of flat bundles ([@RRV07; @RRV08]).

In several cases of physical interest, in particular when $\pi_1(M)$ is not trivial (anti-de Sitter spacetimes, the circle, Aharonov-Bohm solenoids), $\Delta$ cannot be directed, see ([\[eq.back1\]](#eq.back1){reference-type="ref" reference="eq.back1"}), and $\EuFrak{A}$ is more generally a *C\**-precosheaf.

At the mathematical level, at the present time the most general superselection structure available on spacetimes with at least two spatial dimensions is the one defined by Brunetti and Ruzzi ([@BR08]): it is expressed in terms of cocycles $z$ with values in the unitary precosheaf of $\EuFrak{A}$, that play the role of *charge transporters* in the terminology of [@Rob0; @Rob]. This generalizes previous works by Guido, Longo, Roberts, Verch and Ruzzi ([@Rob0; @Rob; @GLRV01; @Ruz05]), with the motivation of clarifying the relations between spacetime topology and structural properties of quantum field theory.

The difference between the approach of ([@BR08]) and the one of [@GLRV01; @Ruz05] is that in the first case we have that observable unitary phases (that we call *holonomies*) appear when one performs a charge transport around a closed loop (see [@BR08 §7]).

This feature is typical in situations like the Aharonov-Bohm effect ([@Fey §15.5],[@ES49; @AB59]), where the electromagnetic field gives rise to observable effects induced by the holonomy of the vector potential. The sectors studied in [@GLRV01; @Ruz05], instead, have trivial holonomy in the above sense and for this reason, following [@BR08], we call them *topologically trivial sectors*.

The Brunetti-Ruzzi superselection structure yields a symmetric tensor *C\**-category $Z^{1,\bullet}(\EuFrak{A})$ describing charge composition, statistics and the particle-antiparticle correspondence (*conjugate sectors*), contains the set $Z^{1,\bullet}_t(\EuFrak{A})$ of topologically trivial sectors as a full subcategory, and coincides with it when $\pi_1(M)$ is trivial.

Nevertheless at the present time it is not clear how to perform a field reconstruction as in the cases of Minkowski spacetime ([@DR90]) and topologically trivial sectors in spacetimes where $\Delta$ is directed ([@GLRV01]), so we do not know whether it is possible to interpret the dual group of $Z^{1,\bullet}(\EuFrak{A})$ as the gauge group. We stress that this problem is open also for topologically trivial sectors in spacetimes with nontrivial fundamental group.

 

In the present paper we focus on globally hyperbolic spacetimes $M$ with at least two spatial dimensions. This last condition is motivated by the fact that we are interested in sectors having ordinary Fermi-Bose (para)statistics that, as well-known, in low-dimensional spacetimes are not ensured (braided statistics may appear, see [@GLRV01 §3]). Following the standard approach ([@GLRV01; @Ruz05; @BR08]) we take $\Delta$ as the base of diamonds whose basic properties, related to the features of Cauchy surfaces in $M$, are discussed in [@GLRV01 §2.1] and [@Ruz05 §3.2].

In one of our main results we prove that $Z^{1,\bullet}(\EuFrak{A})$ is the category of sections of a presheaf $\EuFrak{S}^\bullet$ of symmetric tensor *C\**-categories with simple units (Theorem [\[thm.br\]](#thm.br){reference-type="ref" reference="thm.br"}).

Our intention is to use $\EuFrak{S}^\bullet$ as a tool to perform the field reconstruction (see the following paragraphs and §[\[sec.concl\]](#sec.concl){reference-type="ref" reference="sec.concl"}), anyway our result also gives new light on the structure of $Z^{1,\bullet}(\EuFrak{A})$: first, it allows us to assign to sectors new invariants of geometric nature, and, secondly, it suggests that the dual object describing the superselection structure may not to be merely a group.

In fact, as a consequence of abstract results for generic presheaves ([@Vas12]), we have that $Z^{1,\bullet}(\EuFrak{A})$ can be characterized as a Tannaka-type dual $\widehat\mathcal G$ of a locally constant -- or, equivalently, flat -- group bundle

$$\mathcal G\to M \ .$$

Thus we have $\mathcal G$-equivariant flat vector bundles in place of the unitary representations ([\[eq.rep\]](#eq.rep){reference-type="ref" reference="eq.rep"}), and, keeping in mind the above-mentioned interpretation of $G$-Hilbert spaces in terms of multiplets of fields, this suggests that the charged field operators that are expected to give rise to sectors in $Z^{1,\bullet}(\EuFrak{A})$ should be visualized in terms of local sections of flat bundles. This idea is not new and has been formulated in the setting of quantum fields ([@Ish; @AI79]), and is currently object of research ([@FL]).

An essential ingredient of the duality result is given by an embedding morphism

$I : \EuFrak{S}^\bullet \to \EuFrak{C}$,

where $\EuFrak{C}$ is a presheaf of full subcategories of the one of Hilbert spaces. This is a crucial point: $I$ may not exist or not to be unique, so the same holds for $\mathcal G$ which, when existing, will depend on the choice of $I$. This does not exclude that there is a criterion to select a unique \"physical\" gauge group bundle $\mathcal G_{phys}$, nevertheless our results show that the isomorphism

$$\label{eq.01}
Z^{1,\bullet}(\EuFrak{A}) \ \simeq \ \widehat\mathcal G_{phys}$$

does not suffice to characterize $\mathcal G_{phys}$, differently from what happens in the Minkowski spacetime.

From the point of view of invariants, we prove that any sector $z$ defines a compact Lie group

$G_z \subseteq {{\mathbb U}(d)}$, $d \in {\mathbb N}$,

and a projective representation

$$\chi_z : \pi_1(M) \to NG_z / G_z \ ,$$

where $NG_z$ is the normalizer of $G_z$ in ${{\mathbb U}(d)}$. The importance of $\chi_z$ relies in the fact that an embedding of $\EuFrak{S}^\bullet$ defines, for any sector $z$, a lift

$$\widehat\chi_z : \pi_1(M) \to NG_z
\ \ , \ \
\chi_z = \widehat\chi_z \, {\mathrm{mod}} G_z \ .$$

Lifts of $\chi_z$ are classified in cohomological terms by a $NG_z$-valued 1--cochain $u_z$ defined on the simplicial set of $\Delta$ (see Theorem [\[thm.gerbe\]](#thm.gerbe){reference-type="ref" reference="thm.gerbe"}).

We interpret $\chi_z$ as a flat principal $NG_z / G_z$-bundle and assign to it Cheeger-Chern-Simons characteristic classes living in the odd cohomology of $M$ (see ([\[eq.ccs\]](#eq.ccs){reference-type="ref" reference="eq.ccs"})) that vanish when $z \in Z^{1,\bullet}_t(\EuFrak{A})$.

To illustrate how group bundles yield gauge symmetries we construct field *C\**-precosheaves obtained by twisting a given \"topologically trivial\" field net with gauge group $G$ (Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"}). The resulting *C\**-precosheaf is acted upon by a locally constant $G$-bundle and has representations with nontrivial holonomy in the sense of [@BR08], with the feature that non-triviality of the holonomy is explicitly related with non-triviality of the gauge group bundle. In accordance with the above-mentioned duality breaking, we have examples of inequivalent field precosheaves -- acted upon by inequivalent group bundles -- having the same observable net, this last represented on a fixed Hilbert space (Cor.[\[cor.gauge1\]](#cor.gauge1){reference-type="ref" reference="cor.gauge1"}).

In §[\[rem.qed\]](#rem.qed){reference-type="ref" reference="rem.qed"} we discuss twists given by background classical potentials interacting with Dirac fields, obtaining relative phases analogous to those appearing in the Aharonov-Bohm effect.

In §[\[sec.free\]](#sec.free){reference-type="ref" reference="sec.free"}, by using generalized free fields we show that for every locally constant $G$-bundle (with suitable structure group) there is a field *C\**-precosheaf having it as a \"group\" of global gauge symmetries.

The choice of considering free fields is dictated by the current lack (at least at the author knowledge) of nonperturbative, local quantum fields in spacetimes with nontrivial $\pi_1(M)$ and spacetime dimension $\geq 3$; but since our twisting procedure works independently of the spacetime dimension, in §[\[sec.BMT\]](#sec.BMT){reference-type="ref" reference="sec.BMT"} we apply our result to conformal current algebras, where the cases $G = {\mathbb Z}_{2n}$, $n \in {\mathbb N}$, occur ([@BMT1; @BMT2]).

The loss of uniqueness and -- in theory -- of existence of the dual group bundle can be avoided already at the mathematical level, moving ourselves in the more convenient setting of gerbes over $\Delta$. This notion is illustrated in §[\[sec.concl\]](#sec.concl){reference-type="ref" reference="sec.concl"}. We shall show in a forthcoming paper ([@VasX]) that $\EuFrak{S}^\bullet$ defines a *unique* dual group gerbe $\check \EuFrak{G}$, which *may* collapse to several, possibly inequivalent, group bundles having the same dual.

In this spirit, we prove in ([\[eq.CON1a\]](#eq.CON1a){reference-type="ref" reference="eq.CON1a"}) that the above-mentioned cochains $u_z$ define Lie group gerbes, that will turn out to be finite-dimensional representations of $\check \EuFrak{G}$.

On these grounds we expect that, at least *a priori*, existence and uniqueness of a field *C\**-precosheaf having $\EuFrak{A}$ as fixed-point precosheaf are not ensured.

Thus we give the notion of *$\check \EuFrak{G}$-*C\**-gerbe* over a poset, defined as a pair $\EuFrak{F}= (F,i)$ where

$F := \{ F_o \}_{o \in \Delta}$

is a family of *C\**-algebras with \*-monomorphisms

$i_{o'o} : F_o \to F_{o'}$, $o \subseteq o'$,

whose possible precosheaf structures are encoded by $\check \EuFrak{G}$ (see ([\[eq.CON2\]](#eq.CON2){reference-type="ref" reference="eq.CON2"}): an interesting point is that fixed-point algebras of a $\check \EuFrak{G}$-*C\**-gerbe always have a unique precosheaf structure).

The fact that a unique \"field gerbe\" $\EuFrak{F}$ may be reconstructed starting from $\EuFrak{A}$ and $Z^{1,\bullet}(\EuFrak{A})$ is object of a work in progress, in which the presheaf $\EuFrak{S}^\bullet$ plays a crucial role (see §[\[sec.concl\]](#sec.concl){reference-type="ref" reference="sec.concl"}).

In this setting, we expect that some invariant of $Z^{1,\bullet}(\EuFrak{A})$, beside ([\[eq.01\]](#eq.01){reference-type="ref" reference="eq.01"}), should allow us to pick a unique \"physical\" field *C\**-precosheaf in which $\EuFrak{F}$ would collapse, carrying a $\mathcal G_{phys}$-action.

Constructions of $\check \EuFrak{G}$-*C\**-gerbes, defined by Wightman fields and labelled by projective representations of the fundamental group, are made in Theorem [\[thm.gauge3\]](#thm.gauge3){reference-type="ref" reference="thm.gauge3"}.

[^1]: In principle we may find more that a suitable base for the purposes of algebraic quantum field theory; but the superselection structure turns out to be independent of the base up to isomorphism, see [@Ruz05 Theorem 2.23].
