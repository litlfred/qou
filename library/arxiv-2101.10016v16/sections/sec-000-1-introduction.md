---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-11
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
1. Introduction
1.1. Historical context of the KLF equivalence. Let g be a f.d. complex simple Lie
algebra and k a positive integer, defined as the physical level. Let d denote the ratio of
the squared lengths of the long to the short roots (d = 1 for simply laced types, d = 2 for

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 3
types B, C, F, and d = 3 for G2). We define the shifted level as ℓ = d(k + hˇ), where hˇ is
the dual Coxeter number of g.
The current algebra of what is now known as the Wess–Zumino-Witten (WZW) model
was shown by Witten [187] to satisfy the commutation relations of affine Kac-Moody algebras at positive integer levels. Knizhnik and Zamolodchikov showed that the n-point
correlation functions of primary fields of the WZW model satisfy a system of partial differential equations, the Knizhnik–Zamolodchikov (KZ) equations [114].
Pioneering work by Kohno [116] established that the braid group representations with
respect to the vector representation of a non-exceptional Lie algebra, arising from the
monodromy of the KZ equations in his framework, are equivalent to those originating from
quantum groups. Kohno initially constructed these integrable connections on the full tensor
product of finite-dimensional representations of the Lie algebra g under a generic parameter
λ. In the particular case of sln, he found the associated Hecke algebra representations.
While he noted that the KZ equations appearing in conformal field theory were related
to his framework when the parameter specializes to λ = 1/ℓ, he restricted his explicit
implementation of the affine framework at a positive integer level strictly to the case of the
affine Kac–Moody algebra slb2, drawing upon the operator formalism of Tsuchiya and Kanie
[170]. By utilizing Wenzl’s classification of unitarizable Hecke algebra representations
at roots of unity, Kohno established the unitarizability of these geometric braid group
representations for both the vector and higher irreducible representations of sl2.
Crucially, this framework relied fundamentally on the multiplicity-free nature of the
sl2 fusion rules and the direct path-algebra descriptions of the corresponding Temperley–
Lieb algebra. For higher-rank Lie algebras, the emergence of non-trivial multiplicities and
higher-dimensional intertwining spaces introduces deep combinatorial obstructions.
Inspired by these results, Drinfeld [47, 48] introduced a deep braided tensor category
structure on the category of finite-dimensional g-modules by equipping it with an associator explicitly derived from the KZ equations. He proved the equivalence at a categorical
level between his category—known as the Drinfeld category—and the rigid braided tensor
category of modules over the formal quantum group Uh(g), marking a foundational breakthrough in representation theory. Drinfeld obtained rigidity of the Drinfeld category by
constructing an antipode on the associated quasi-bialgebra, following the Drinfeld–Kohno
theorem, via an operation that he called a twist of a quantum group [47].
Subsequently, inspired by Drindeld’s results, Kazhdan and Lusztig [109] extended Kohno’s
braid group equivalence to the affine setting at negative rational shifted levels, constructing a braided tensor category structure on certain non-semisimple module categories O−ℓ
over the corresponding affine Kac-Moody algebras (specifically for simply laced types).
They proved a categorical equivalence between O−ℓ and the representation categories of
corresponding quantum groups at the root of unity q = e
iπ
ℓ . A main result of their work
is a direct proof of rigidity of O−ℓ.
For the positive integer levels, Finkelberg followed the algebraic geometric approach developed by Beilinson, Feigin, and Mazur [11] for the semisimple braided tensor category O˜
ℓ
associated to an affine Lie algebra, and constructed a functor to a semisimple subquotient

4 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
fusion category O˜
−ℓ of a Kazhdan-Lusztig category at the opposite shifted level [55], and
thus, by the Kazhdan-Lusztig equivalence, to a semisimple subquotient fusion category
C(g, q, ℓ) of the corresponding quantum group at a root of unity.
Frenkel and Zhu established a vertex operator algebra structure on a certain representation Lk,0 of the affine Kac-Moody—and analogously for the Virasoro algebra—in such a
way that the representations of Lk,0 give rise to the WZW model [61]. We denote by Vgk
this vertex operator algebra.
Following an analytic approach based on differential equations, Huang and Lepowsky
constructed a braided tensor category structure on the module category of a vertex operator
algebra in a very general setting, including the affine cases, for which they relied on the KZ
equations [85]–[88]. Huang gave a rigorous proof of the Verlinde formula and the fusion
rules [178] and showed its relevance to prove rigidity and modularity [92], [93].
To complete the proof of the tensor equivalence of his functor O˜
ℓ → O˜−ℓ
, Finkelberg
needed the fusion rules and the Verlinde formula as well [56], established in his setting by
Teleman and Faltings [53], [171], guaranteeing that the K-rings of the positive and negative
shifted level categories are based-isomorphic. He also relied on rigidity of Kazhdan-Lusztig
category O−ℓ and of the category of finite-dimensional representations of the simple Lie
algebra g. He also derived rigidity of O˜
ℓ
from his tensor equivalence.
Summarizing, the existing proof of the tensor equivalence O˜
ℓ → C(g, q, ℓ) relies on results spanning distinct algebraic and geometric settings across both positive integer and
negative shifted levels. It requires separate quotient constructions to yield the semisimple
subquotients where rigidity defines the necessary tensor ideals, and uses rigidity to obtain
tensoriality of the equivalence. Furthermore, because the Kazhdan–Lusztig construction
does not apply to certain negative rational shifted levels, Finkelberg’s equivalence, and
consequently the proof of rigidity of O˜
ℓ
, do not cover some exceptional cases—namely, E6
and E7 at level k = 1, and E8 at levels k = 1, 2. Additionally, it is not easy to find literature explicitly extending the Kazhdan–Lusztig rigid braided tensor category construction
to non-simply laced Lie algebras, due to the greater complexities of the KZ equations.
Regarding the non-simply laced types, it is noted in Sect. 2.6 of [55] and Sect. 2, part (f)
of [56] that due to a uniform lower bound constraint of ℓ needed to guarantee rigidity of
O−ℓ, the rigidity of O˜
ℓ and the tensor equivalence property of the Finkelberg functor may
be unproved for low levels k ≤ 2, requiring further case-by-case study.
Taken together, the existing proof of the equivalence is distributed over [109], [55], [56],
[53] and [171]. Kazhdan and Lusztig carried out their construction for the simply-laced
types, while Finkelberg’s functor is stated for the other types as well.
Consequently, the need to describe a direct connection between affine Lie algebra module categories at positive integer levels and quantum groups emerged, see e.g. Gannon’s
observation in Sect. 6.2.3 of [68]. Notably, in [97], Huang explained in detail the history
of Finkelberg’s theorem and the need of finding a direct proof—one that bypasses the obstructions arising from the negative shifted levels and includes the exceptional cases (see
Problem 5). The interest of a direct construction extends beyond the case at hand. There
are conjectural equivalences between braided tensor categories of modules for other vertex

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 5
operator algebras and categories of modules for quantum groups for which no Kazhdan–
Lusztig category is available; in those cases the route through negative shifted levels is
unavailable. Huang has pointed out to us that this is his main reason of interest in the
problem. A direct construction of Finkelberg’s equivalence is therefore a natural starting
point for those cases.
In this spirit, we start with the quantum group fusion category. Wenzl showed in [185]
that this category can be constructed intrinsically for all Lie types and all positive integer
levels, treating the simply-laced and non-simply-laced cases uniformly, for the roots of
unity of the kind q = e
iπ/ℓ starting with a fundamental (generating) representation V of
Uq(g), see Theorem 5.4 in [25] for an explicit proof.
Starting from Wenzl’s realization of C(g, q, ℓ) and adopting a direct, operator-algebraic
framework, we give a direct proof of the equivalence with a category of modules of the
corresponding affine vertex operator algebra, in a single self-contained text. In this way
we circumvent the Verlinde formula dependency of the equivalence with the categories
of modules of affine vertex operator algebras (or affine Lie algebras), the passage to the
negative integer levels, and we derive rigidity of these categories from the equivalence,
thereby also rendering boundary cases uniformly accessible. We describe our approach in
the next subsection, state the problems solved in this paper in subsection 1.3, and describe
the main results in section 2. In section 3 we describe the organization of the rest of the
paper.
1.2. Overview of our approach. In the operator algebraic approach to quantum field
theory (AQFT) introduced by Haag and Kastler [80], the subsequent work of Doplicher,
Haag, and Roberts established the rigidity of the associated symmetric tensor C
∗
-categories
of superselection sectors from physically motivated principles, yielding Dirac’s particleantiparticle duality as a structural consequence [38], [39], [40], [81].
For high-dimensional theories, a deep result by Doplicher and Roberts established that
the category of localizable charges is equivalent to the representation category of a unique
compact group having the role of a global gauge group [41]. The Doplicher–Roberts compact group associated with the category describes rigidity via the passage to the conjugate
representation of the group. A closely related result was independently obtained by Deligne
for affine group schemes over a field [30].
In low-dimensional theories, one encounters unitary rigid braided tensor C
∗
-categories,
where the braided symmetry is given by unitary representations of the braid group acting
on tensor powers of an object [57, 58].
Parallel to this, as recalled in Subsect. 1.1,, Jones index theory led to the construction
of rigid tensor C
∗
-categories from inclusions of von Neumann algebras with trivial center
(subfactors) and yielded unitary representations of the braid group satisfying Temperley–
Lieb relations; conversely, inclusions of subfactors arise from such relations [100].
Shortly after Vaughan Jones’ discovery of subfactor theory and the Jones polynomial,
Wenzl connected the representation theory of Hecke algebras Hn(q) of type A at roots of
unity to inclusions of finite-index II1 subfactors. This breakthrough provided a foundational framework for the unitary structures linking subfactor theory, quantum groups, and

6 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
two-dimensional conformal field theory [182, 183]. Wenzl explicitly constructed and classified finite-dimensional, irreducible representations of the non-semisimple algebras Hn(q)
that are unitarizable, thereby constructing new hyperfinite II1 subfactors that generalize
the Temperley-Lieb-Jones constructions. As observed in [183], via quantum Schur-Weyl
duality, these representations of Hecke algebras can naturally be viewed as arising from
the endomorphism algebras of tensor powers of the fundamental representation of Uq(slN )
[99].
Drinfeld introduced quantum groups at the ICM in Berkeley in 1986 [45]. Quantum
groups provide rigidity via the antipode. The representation theory of quantum groups at
roots of unity was developed by Lusztig [119, 122], Reshetikhin, Turaev [155].
We are naturally led to ask whether rigidity of categories on the conformal field theory side, and in particular for Vgk
, can be explained by an equivalence with a category
of representations of a semisimple quantum gauge group in the sense of the DoplicherRoberts program. We therefore look for a natural construction of a quantum version of
the Doplicher–Roberts compact group for braided categories. A major difference with
Drinfeld setting is that, in our setting, the involved braided tensor categories, and especially the quantum group fusion category, are not given from the start with a fibre functor
to the category of vector spaces.
Mack and Schomerus pioneered the question of bridging the Doplicher–Roberts program on global quantum gauge groups and field algebras in conformal field theory with
Drinfeld’s work on the Drinfeld-Kohno theorem mentioned in Subsect. 1.1. Specifically,
they introduced the weak quasi-Hopf algebras that extend Drinfeld’s original structures,
implementing them for the sl2-case as a quantum analogue of Doplicher–Roberts compact
groups [124, 165].
Their early construction of both the weak quasi-Hopf algebras and the analogue of
the Doplicher–Roberts field algebra encountered complications, arising primarily from the
non-triviality of the associator and a lack of uniqueness or naturality beyond the sl2 case.
Wenzl extended the construction of subfactors from quantum groups at roots of unity
and constructed unitary braided tensor structures on the quantum group fusion category
uniformly for all Lie types, in [184], [185].
Mack and Schomerus program was not developed further until recently, when two of us
found a natural construction of Mack-Schomerus weak quasi-Hopf algebras associated to
the quantum group fusion category of Uq(slN ) for all positive integer levels [25].
Our first aim in this paper is to put the examples of [25] into a new theory of weak Hopf
algebras, and then extend the construction to all other Lie types.
Specifically, we adopt an operator-algebraic approach where unitarity and C
∗
-structures
with unitary representations of the braid group play a primary role.
Our approach heavily relies on the foundational C
∗
-algebraic techniques for quantum
group fusion categories developed by Wenzl. We consider Wenzl linear functor
W : C(g, q, ℓ) → Hilb
and construct on it a weak tensor structure in the sense of Definition 4.8.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 7
We achieve new examples AW (g, q, ℓ) in this paper for all Lie types and levels, with
different methods as compared to the type A case treated in [25], without using the fusion
rules, see Theorem 2.5. For g = slN we recover our earlier examples. We prove that these
algebras satisfy properties of compatible unitary coboundary weak Hopf algebras in a sense
that we introduce in Definition 30.1.
The class of unitary coboundary weak (quasi-)Hopf algebras (Definition 28.1) admits a
categorical characterization that significantly simplifies their axiomatic description; see
Theorem 29.1. In the specific case of a symmetric tensor C
∗
-category endowed with a unitary fibre functor to the category of Hilbert spaces, this characterization reduces precisely
to the requirement that the functor is symmetric. This constraint is required and, in fact,
plays a fundamental role in the Doplicher–Roberts duality theory for compact groups, in
determining the fibre functor uniquely.
In the braided setting, the categorical characterization of a unitary coboundary weak
quasi-Hopf algebra requires finding a weak quasi-tensor structure on the given functor
implemented by coisometric fibre maps Fρ,σ associated with the tensor product bifunctor of the underlying braided category. It is required that the structure maps respect
the coboundary symmetries of both the source and target categories. Indeed, the unique
coboundary symmetry on the category of Hilbert spaces is the standard permutation symmetry. Since the coboundary symmetry of a braided tensor category is obtained by multiplying the braiding by a 2-coboundary derived from a square root of the ribbon element,
this characterization forces a rigid constraint: via the fibre functor, the braided symmetry of the category is uniquely determined as the permutation symmetry modified by this
square root 2-coboundary.
Formulas of this nature indeed govern the explicit structure of the braided symmetry in
categories arising from conformal field theory, such as loop group conformal nets or affine
vertex operator algebras (see Remarks 29.2, 38.16, and references therein). This operator
algebraically realizes the categorical balancing relation where the double braiding equals
the 2-coboundary defined by the twist. On an irreducible component of the minimum
energy subspace of the tensor product, the braiding evaluates precisely to the square root
of the Virasoro phases multiplied by the permutation symmetry, see Theorem 4.1 in [93].
While the braided symmetry in these settings is traditionally derived from the monodromy of the Knizhnik–Zamolodchikov equations, our framework provides an independent
method for constructing this symmetry entirely via unitary coboundary weak quasi-Hopf
algebras with coisometric structure maps. In our view, this construction beautifully realizes an insightful perspective of Vaughan Jones on the profound relevance of manifest
unitarity in conformal field theory (cf. [150]).
In the quantum group setting, the action of the R-matrix on tensor product spaces does
not take an analogous simple diagonal form. Consequently, the associated coboundary
matrix does not act trivially. Since this matrix induces the unitary structure on the fusion
spaces [185], this unitary structure effectively measures the deviation of the R-matrix
from acting strictly via the square roots of the ribbon phases–a purely quantum effect.
We explicitly quantify this phenomenon. Specifically, we show that the unitary modular
quantum group fusion category C(g, q, ℓ), which is described by the unitary representations

8 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
of our unitary coboundary weak Hopf algebra AW (g, q, ℓ) by Theorem 2.5, is fundamentally
incompatible with the existence of coisometric fusion projections due to the weakly trivial
associator of AW (g, q, ℓ) and the non-integrality of the quantum dimensions of C(g, q, ℓ) (see
Theorem 16.8). Thus, extracting coisometric fusion projections via polar decomposition
inevitably twists the weak Hopf algebra into a genuine weak quasi-Hopf algebra, necessarily
equipped with a 3-coboundary associator.
By applying an analytic Drinfeld twist method and Wenzl’s de-quantization curve to the
weak Hopf algebras AW (g, q, ℓ), we obtain a self-contained construction of a unitary rigid
braided tensor structure on the module category of the affine vertex operator algebra Vgk
(see Corollary 2.9).
A pivotal feature of our unitary structure on Rep(Vgk
) and analytic twist is that it equips
Zhu’s minimum energy functor with a canonical weak quasi-tensor structure (F0, G0), in
a way that F0 coincides with the restriction of Huang-Lepowsky tensor product structure
map, and moreover the twist forces F0 to be coisometric and G0 to be the isometric Hilbert
space adjoint of F0, a property we establish in Theorem 21.3. Comparing with HuangLepowsky ribbon braided tensor structure, at this stage we have established an equivalence
of the two categories, the ribbon structures and the tensor product bifunctors for the affine
vertex operator alegbras at positive integer levels.
In searching the Drinfeld twist we have been inspired by the categorical framework of
Drinfeld-Kohno theorem established by Neshveyev and Tuset for compact quantum groups
[139]. However, our twist seems different from their twist. Our twist may be regarded as a
specialization at the root of unity to the fusion algebra AW (g, q, ℓ) of the original Drinfeld
twist in the formal setting, arising from a square root of Drinfeld coboundary matrix [47],
that we consider in an operator algebraic sense.
We prove all the properties of the affine vertex operator algebra fusion category at a
positive integer level using the methods of quantum symmetry and the Drinfeld twist.
Specifically, the ribbon-braided tensor structure, fusion rules, and rigidity of the unitary
quantum group fusion category C(g, q, ℓ) induce a corresponding structure on the weak Hopf
C
∗
-algebra AW (g, q, ℓ). From this position, we transfer the structure to the Zhu algebra
via our Drinfeld twist and the de-quantization curve used in [185] to prove unitarity of the
fusion category.
Wenzl’s curve gives an algebra isomorphism between AW (g, q, ℓ) and the Zhu algebra
A(Vgk). The twist transports the rest of the structure: coproduct, (weak trivial) associator,
antipode, R-matrix, unitary structure, making the Zhu algebra into a unitary coboundary
weak quasi-Hopf C
∗
-algebra with 3-coboundary associator. From this position, we lift the
structure to the module category Rep(Vgk) of the vertex operator algebra via Zhu’s linear
equivalence and its inverse. In this way, we obtain the structure of a unitary rigid ribbonbraided tensor category on Rep(Vgk
) braided tensor equivalent to the quantum group fusion
category.
We deduce the rigidity of our VOA fusion category Rep(Vgk) directly from our tensor
equivalence, driven by the antipode of AW (g, q, ℓ) and our specialized Drinfeld twist.
This approach allows us to bypass the need to dualize through negative levels, provide an explicit, self-contained proof of the Kazhdan-Luszting-Finkelberg theorem that

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 9
includes the exceptional boundary cases, and simultaneously settle the problem of Galindo
on uniqueness of the unitary structure in a tensor category, as well as those of Frenkel-Zhu
and Doplicher-Roberts for the WZW model within the framework of vertex operator algebras. Along our path, we solve Kirillov’s conjecture in the algebraic-geometric framework
of Beilinson, Feigin, and Mazur utilized by Finkelberg, using general Tannakian methods
for weak quasi-Hopf algebras, Finkelberg’s equivalence theorem, and Wenzl’s unitarity of
C(g, q, ℓ).
We complete the comparison between our unitary ribbon braided structure with the
Huang–Lepowsky structure. We find a complete identification of the full categorical data
(ribbon structure, tensor product bifunctor, braiding, and associativity morphisms) for the
classical Lie types and G2. For all Lie types, we obtain identifications between the two
structures for the braiding and associativity morphisms on many objects involving tensor
products with the fundamental representations, see Theorem 2.11. To keep the focus on the
core ideas developed in this paper, the detailed proofs of Theorems 8.13 and 8.21, as well
as their applicability to the stated Lie types, are deferred to our companion paper [149].
In this way we obtain an independent construction of the Huang-Lepowsky braided tensor
structure on Rep(Vgk
) which does not depend on the Knizhnik-Zamolodchikov equations,
and a proof of rigidity of this category that does not depend on the Verlinde formula or
fusion rules.
Finally, in [150], we provide a conceptual and expository historical overview of the
main ideas of our proof of the KLF theorem and its applications to the unitarizability of
categories arising from conformal field theory, and we outline directions for future research.
The remainder of the paper is organized as follows. In the subsequent Subsect. 1.3, we
we state the open Problems 1, 2, 3, 4, 5, and 6 which are of primary interest in our paper
(with Problem 1 serving as our original motivation). In Sect. 2, we state our main results.
In Sect. 3, we provide an outline of the rest of the paper. In doing so, we discuss the
utility of the KLF theorem (or other instances of equivalences coming, e.g., from pointed
fusion categories) to transport unitary structures from the quantum group fusion category
to the affine vertex operator algebra fusion category.
1.3. Statements of the problems under consideration in this paper. As outlined
in the previous subsections, our uniform operator-algebraic framework is connected to
several long-standing problems across algebraic quantum field theory (AQFT), conformal
field theory, and tensor category theory. For clarity, we state these problems here.
As recalled in Subsect. 1.2, the Doplicher–Roberts theorem characterizes the category
of high-dimensional localizable charges by the representation category of a unique compact
group. However, in low dimensions, the statistics dimension may be non-integer, meaning
the category cannot correspond to a standard compact group. Because the braid group
naturally appears in low-dimensional quantum field theories, Doplicher and Roberts posed
the following problem, which served as the original motivation for this paper:
Problem 1. (Sect. 7 in [43]) Can we extend the duality theory for compact groups [41]
Theorem 6.1 to more general objects, by replacing strict symmetric monoidal C*-categories

10 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
by strict braided monoidal C*-categories? What is the full class of compact group-like
objects which arise in this way?
Parallel to this, in the study of conformal field theory (CFT), Moore and Seiberg conjectured analytic properties of quantum fields and discovered polynomial equations that
later evolved into the notion of modular tensor categories [129, 130, 154, 155, 173]. Noting
that in various examples of CFT, the braid matrix is closely related to the R-matrix of
specific quantum groups, they posed the following:
Problem 2. (Sect. 9 in [130]) Understand chiral algebras of conformal field theory as
generalization of quantum groups.
Regarding construction of unitary structures on modular fusion categories, Kirillov defined hermitian forms on the quantum group fusion category C(g, q, ℓ) in [111] and on the
Beilinson-Feigin-Mazur category O˜
ℓ at positive integer levels in [113], and conjectured that
they are unitary. The quantum group case was settled by Wenzl in [185], while the affine
Lie algebra case, to the authors’ knowledge, remained open.
Problem 3. (Remark 10.7 in [113]) The natural conjecture, parallel to the quantum group
case, is that so defined inner product on the spaces of morphisms is positive definite. So
far, we have no proof of it except for sl2 case where it can be checked by direct calculation.
Observing the deep connections between the categorical data of CFTs and Drinfeld’s
quasi-Hopf algebras [47], Frenkel and Zhu asked for a rigorous algebraic bridge in the
framework of vertex operator algebras:
Problem 4. ([61]) A complete conceptual explanation of this phenomenon is needed. In
the setting of vertex operator algebras, associate a general construction of quasi-triangular
quasi-Hopf algebra with a vertex operator algebra with the same tensor category of representations.
Further related conjectures may be found in [65], [128].
Addressing the tensor category structure directly, Huang and Lepowsky constructed a
general tensor product theory for module categories of VOAs [85, 86, 87, 88], establishing,
in particular, the modular tensor structure for affine VOAs at positive integer levels [90,
92, 93]. To reconcile this intrinsic VOA approach with the historical algebraic-geometric
proof of the Kazhdan–Lusztig–Finkelberg equivalence, Huang formulated the following
challenge:
Problem 5. (Problem 4.4 in [97]) Find a direct construction of this equivalence without
using the equivalence given by Kazhdan-Lusztig so that this equivalence covers all the cases,
including the important g = E8 and k = 2 case.
Finally, our operator-algebraic methods based on weak quasi-bialgebras require establishing unique C
∗
-structures on tensor categories. This directly addresses a fundamental
question raised by Galindo [66]:

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 11
Problem 6. May a fusion category admit more than a unitary structure making it into a
unitary tensor category?
In the following Section 2, we state our main results, demonstrating how the construction
of weak quasi-Hopf C
∗
-algebras and the transport of unitary coboundary structures via
Drinfeld twists provides a direct, unified solution to these five problems.
