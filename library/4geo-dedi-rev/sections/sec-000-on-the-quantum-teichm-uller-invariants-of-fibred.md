---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-000-on-the-quantum-teichm-uller-invariants-of-fibred
section_title: "ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS"
section_number: null
pages: 2-26
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
toc_source: inferred
---
3-MANIFOLDS
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
1 Institut Montpelli´erain Alexander Grothendieck, CNRS, Universit´e de Montpellier
(sbaseilh@univ-montp2.fr)
2 Dipartimento di Matematica, Universit`a di Pisa, Largo Bruno Pontecorvo 5, 56127 Pisa, Italy
(benedett@dm.unipi.it)
Abstract. We show that the reduced quantum hyperbolic invariants of pseudo-Anosov diﬀeomor-
phisms of punctured surfaces are intertwiners of local representations of the quantum Teichm¨uller
spaces. We characterize them as the only intertwiners that satisfy certain natural cut-and-paste op-
erations of topological quantum ﬁeld theories and such that their traces deﬁne invariants of mapping
tori.
Contents
1.
Introduction
1
2.
Topological-combinatorial support
6
3.
Background results
7
3.1.
Classical hyperbolic geometry
7
3.2.
Quantum hyperbolic geometry
9
3.3.
Representations of the quantum Teichm¨uller spaces
13
3.4.
Intertwiners of local representations
16
4.
Proofs
17
References
25
1. Introduction
Let M be a ﬁbred cusped 3-manifold, that is, an oriented non compact ﬁnite volume complete
hyperbolic 3-manifold which ﬁbres over the circle S1. In this paper we describe the relationships
between the quantum hyperbolic invariants of M (QHI) ([4, 5, 6]), and the intertwiners of ﬁnite
dimensional representations of the quantum Teichm¨uller space of S ([7, 8], [11]), where S is a ﬁbre of
some ﬁbration of M over S1. Recall that M is the interior of a compact manifold ¯
M with boundary
made by tori, and that S is the interior of a compact surface with boundary ¯S, properly embedded in
¯
M, so that ¯S ∩¯
M is a family of ‘meridian’ curves on ∂¯
M.
The existence of such relationships has been expected for a long time, and their precise formulation
often thought as depending only on the solution of a handful of technical problems. Let us recall the
main arguments underlying this opinion. Let q be a primitive N-th root of unity, where N is odd.
Then:
• The quantum Teichm¨uller space Tq
S of S consists of the set of Chekhov-Fock algebras Tq
λ,
considered up to a suitable equivalence relation (see Section 3.3), where λ varies among the
ideal triangulations of S. A representation ρ of Tq
S is a suitable family of ‘compatible’ repre-
sentations ρ = {ρλ : Tq
λ →End(Vλ)}λ. The irreducible representations of Tq
S were classiﬁed
up to isomorphism in [7], and so-called local representations were introduced and classiﬁed in
[8].
1
2
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
• The local representations are reducible, but more suited to perform the usual cut-and-paste
operations of topological quantum ﬁeld theories. In this framework, it is natural to restrict
to a distinguished family of intertwiners, satisfying some functorial properties with respect
to the inclusion of triangulated subsurfaces. Theorem 20 of [8] proposed such a family, and
argued that for every couple (ρ, ρ′) of isomorphic local representations of Tq
S and every couple
(λ, λ′) of ideal triangulations of S, there is a unique projective class of intertwiners in the
family which are deﬁned from the representation space Vλ of ρλ to the representation space
Vλ′ of ρ′
λ′.
Let us call the elements of these classes QT intertwiners.
• The diﬀeomorphisms of S act on the local representations of Tq
S. Denote by φ the monodromy
of some ﬁbration of M over S1. If a local representation ρ is isomorphic to its pull-back φ∗ρ
under φ (an instance is canonically associated to the hyperbolic holonomy of M [7, 8]), then
the trace of a suitably normalized QT intertwiner which relates ρλ to φ∗ρλ′, λ′ := φ(λ), should
be an invariant of M (possibly depending on φ) and the isomorphism class of ρ.
• The QT intertwiners can be constructed by composing elementary intertwiners, associated to
the diagonal exchanges in a sequence relating two ideal triangulations of S, and these were
identiﬁed with the Kashaev 6j-symbols in [2].
• The QHI of M can be deﬁned by QH state sums over “layered” triangulations of M, that
is, roughly, 3-dimensional ideal triangulations that realize sequences of diagonal exchanges
relating the surface ideal triangulations λ and φ(λ), in such a way that every diagonal exchange
is associated to a tetrahedron of the triangulation. The main building blocks of the QH state
sums are tensors called matrix dilogarithms, carried by the (suitably decorated) tetrahedra,
which were derived in [3] from the Kashaev 6j-symbols.
In conclusion, the QHI of M would coincide with the traces of QT intertwiners of local represen-
tations of Tq
S (at least when M is equipped with the hyperbolic holonomy). Only a suitable choice
of normalization of the QT intertwiners and an explicit correspondence between formulas would be
missing.
Another fact pointing in the same direction is that both the isomorphism classes of local repre-
sentations of the quantum Teichm¨uller spaces and the QHI depend on similar geometric structures.
Every local representation ρ of Tq
S deﬁnes an augmented character of π1(S) in PSL(2, C) [8], called its
holonomy, given by a system of (exponential) shear-bend coordinates on every ideal triangulation λ of
S. Moreover ρ has a load hρ, deﬁned as a N-th root of the product of the share-bend coordinates on
any ideal triangulation λ of S, and which does not depend on the choice of λ. The holonomy and the
load classify ρ up to isomorphism. On another hand, the QHI of any cusped 3-manifold M depend
on a choice of augmented character r of π1(M) in PSL(2, C), lying in the irreducible component of
the variety of augmented characters containing the hyperbolic holonomy. If S is a ﬁbre of a ﬁbration
of M over S1, r can be recoved from its restriction to π1(S).
However, other facts suggested that the relations between the QT intertwiners and the QHI would
be subtler than expected:
• The matrix dilogarithms are obtained from the Kashaev 6j-symbols by rewriting them in a
non trivial way as tensors depending on geometrically meaningful parameters (which are N-th
roots of hyperbolic shape parameters), but also by applying a symmetrization procedure. This
procedure is necessary to get the invariance of the QH state sums over any cusped 3-manifold.
It involves several additional choices, and eventually forces to multiply the QH state sums
by a normalization factor. It implies furthermore that the QHI must actually depend not
only on the choice of an augmented character r of π1(M) in PSL(2, C), but also on some
cohomological classes, called weights, which cannot be recovered from the holonomy of local
representations of the quantum Teichm¨uller spaces. The weights gauge out the additional
choices. Surprisingly, both the normalization factor of the QH state sums and the weights did
not appear in quantum Teichm¨uller theory.
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
3
• An issue about the uniqueness of the projective classes of QT intertwiners has been ﬁxed
recently. By a careful analysis of the deﬁnition of local representations, and adapting the con-
struction of the QT intertwiners from [8], for every couple (ρλ, ρ′
λ′) as above, it is constructed
in [11] a unique, minimal set Lρρ′
λλ′ of projective classes of QT intertwiners which relate ρλ to
ρ′
λ′, and a free transitive action
(1)
ψρρ′
λλ′ : H1(S; Z/NZ) × Lρρ′
λλ′ →Lρρ′
λλ′.
In particular, the set Lρρ′
λλ′ is far from being reduced to one point.
The meaning of the normalization factor of the QH state sums has been better understood in [6].
In that paper we showed that for every cusped 3-manifold M, the QH state sums of M without the
normalization factor deﬁne ﬁner invariants Hred
N (M, r, κ; s), called reduced QH invariants, well-deﬁned
up to multiplication by 4N-th roots of unity. They depend on an augmented PSL(2, C)-character
r of π1(M), a class κ ∈H1(∂¯
M; C∗), C∗= C \ {0} being the multiplicative group, such that κN
coincides up to sign with the restriction of r to π1(∂¯
M), and an additional structure s on M, called a
non ambiguous structure.
When M ﬁbres over S1, a natural choice of s is a ﬁbration of M, say with monodromy φ. Let us
denote by Mφ the realization of M as the mapping torus of φ, equipped with the corresponding ﬁbra-
tion, and the reduced QH invariant by Hred
N (Mφ, r, κ). The latter depends directly on the monodromy
φ, and hence is apparently more suited to investigate the relationships with the QT intertwiners.
Note, however, that the class κ is residual of the cohomological weights involved in the deﬁnition of
the unreduced QHI, and so the above considerations about the weights still apply.
Denote by S a ﬁbre of Mφ. Rather than considering Mφ one can consider as well the mapping
cylinder Cφ of φ. In this case, instead of a scalar invariant there is a (reduced) QH-operator
Hred
N (TCφ,˜b, w) ∈End
 (CN)⊗2m
,
m := −χ(S),
which is such that
(2)
Hred
N (Mφ, r, κ) = Trace

Hred
N (TCφ,˜b, w)

.
More precisely, in the spirit of topological quantum ﬁeld theories, for every odd N ≥3 the QHI
deﬁne a contravariant functor from the category of (decorated) (2 + 1)-cobordisms to the category
of vector spaces. In particular, it associates vector spaces Uλ and Uλ′ to the triangulated surfaces
(S, λ) and (S, λ′) respectively, where λ′ := φ(λ), and a QH-operator Hred
N (TCφ,˜b, w): Uλ′ →Uλ to the
cylinder Cφ. The diﬀeomorphism φ gives an identiﬁcation between Uλ and Uλ′, so one can consider
Hred
N (TCφ,˜b, w) as an element of End (Uλ).
Moreover, the construction of the functor provides a
natural identiﬁcation of Uλ with (CN)⊗2m.
The operator Hred
N (TCφ,˜b, w) is deﬁned by means of QH state sums over layered QH-triangulations
(TCφ,˜b, w) of Cφ. Here, by ‘layered QH-triangulation’ we mean that: TCφ is a triangulation of Cφ
that produces a layered triangulation of Mφ under the quotient map Cφ →Mφ; w is a suitable
system of N-th roots of shape parameters, solving the Thurston edge equations associated to the
triangulation of Mφ induced by TCφ, and which actually encodes both r and κ; ﬁnally ˜b is a way of
ordering the elements of w in each tetrahedron of TCφ, called weak-branching. The complete deﬁnition
of (TCφ,˜b, w) is given in Section 3.2.
Our results describe the relationships between the QH-operators Hred
N (TCφ,˜b, w) and the set Lρρ′
λλ′
of QT intertwiners. First note that these are assigned to (λ, λ′) in a covariant way, as they go from the
representation space Vλ of ρλ to the representation space Vλ′ of ρ′
λ′. For every ﬁnite dimensional vector
space V , denote by V ′ its dual space. The natural way to convert a QH operator Hred
N (TCφ,˜b, w) into
a covariant one (preserving the value of its trace) is to consider its dual, or transposed operator
Hred
N (TCφ,˜b, w)T ∈End (U ′
λ) .
4
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Using the deﬁnitions of U ′
λ in the QHI and of Vλ in the theory of local representation of Tq
λ one gets
natural identiﬁcations U ′
λ ∼=
 (CN)′⊗2m ∼= Vλ. Under all these identiﬁcations
Hred
N (TCφ,˜b, w)T ∈End
 (CN)′⊗2m
is a QT intertwiner. Clearly, the matrix elements of these tensors in the respective canonical bases of
 (CN)′⊗2m and (CN)⊗2m are related by
(3)
(Hred
N (TCφ,˜b, w)T )i1...i2m
j1...j2m = Hred
N (TCφ,˜b, w)j1...j2m
i1...i2m .
We can now state our results precisely. Let S be a punctured surface of negative Euler characteristic,
φ a pseudo-Anosov diﬀeomorphism of S, Mφ the mapping torus of φ equipped with its ﬁbration over
S1 with monodromy φ, and consider triples (Mφ, r, κ) and (TCφ,˜b, w) as above. Denote by λ, λ′ the
ideal triangulations of S given by the restriction to S×{0} and φ(S)×{1} of the (layered) triangulation
TCφ.
Theorem 1.1. (1) The QH-triangulation (TCφ,˜b, w) determines representations ρλ and ρλ′ of Tq
λ and
Tq
λ′ respectively, belonging to a local representation ρ of Tq
S, such that ρλ is isomorphic to φ∗ρλ′, and
acting on Vλ = Vλ′ = (
 (CN)′⊗2m. Moreover the transposed operator Hred
N (TCφ,˜b, w)T , considered
as an element of Hom(Vλ, Vλ′), is a QT intertwiner which intertwins the representations ρλ and ρλ′.
(2) For any other choice of weak branching ˜b′, the operator Hred
N (TCφ,˜b′, w)T intertwins local rep-
resentations canonically isomorphic to ρλ, ρλ′ respectively.
We call Hρ
λ,λ′ := Hred
N (TCφ,˜b, w)T a QHI intertwiner.
Denote by X0(M) the (unique) irreducible component of the variety of augmented PSL(2, C)-
characters of M that contains the discrete faithful holonomy rh.
Denote by X(S) the variety of
augmented characters of S, and by i∗: X0(M) →X(S) the restriction map.
Recall the residual
weight κ ∈H1(∂¯
Mφ; C∗) involved in the deﬁnition of the reduced QHI.
Theorem 1.2. (1) There is a neighborhood of i∗(rh) in i∗(X0(M)) ⊂X(S) such that, for any
isomorphism class of local representations of Tq
S whose holonomy lies in this neighborhood, there
is a representative ρ of the class, representations ρλ, ρλ′ belonging to ρ, and a QHI intertwiner
Hred
N (TCφ,˜b, w)T intertwining ρλ and ρλ′ as above. The load of ρ is determined by the values of the
weight κ at the meridian curves that form ¯S ∩¯
M.
(2) The set of QHI intertwiners Hρ
λ,λ′ is the subset of QT intertwiners which intertwin the repre-
sentation ρλ to ρλ′, and whose traces are well deﬁned invariants of the triples (Mφ, r, κ) such that the
restriction of r to π1(S) is the holonomy of ρ.
Let us make a few comments on Theorem 1.1 and 1.2.
• A key point of Theorem 1.1 (1) is to realize the transposed of the matrix dilogarithms as inter-
twiners between local representations of the two Chekhov-Fock algebras that one can associate to an
ideal square. To this aim we consider an operator theoretic formulation of the matrix dilogarithms.
As these are related to the Kashaev 6j-symbols (in a non trivial way), one could alternatively de-
velop a proof based on the result of Bai [2] relating the Kashaev 6j-symbols with intertwiners as
above. However, it is not immediate. Bai’s result deals with local representations up to isomorphism,
and does not provide explicit relations between actual representatives. Also the relation between the
Kashaev 6j-symbols and the intertwiners of local representations is expressed in abstract terms, using
the cyclic representations of the Weyl algebra, and not in terms of the eventual geometrically relevant
parameters, the q-shape parameters (see Section 3.2).
• Theorem 1.2 (1) holds true more generally for any isomorphism class of local representations whose
holonomy lies in i∗(B), where B is a determined Zariski open subset of the eigenvalue subvariety E(M)
of X0(M), introduced in [12]. Let us note here that E(M) = X0(M) if M has a single cusp, and in
general, rh ∈E(M), and dimCE(M) equals the number of cusps of M. For simplicity, in this paper
we restrict to characters in a neighborhood of i∗(rh) in i∗(X0(M)). The general case is easily deduced
from the results of [5].
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
5
• We can say that the invariance property of the QHI selects preferred elements in the set of all
traces of QT intertwiners (which has no a priori basepoints). Note that, the action (1) being transitive,
it does not stabilizes the set of QHI intertwiners. As well as the reduced QHI of Mφ give rise to the QT
intertwiners Hred
N (TCφ,˜b, w)T , with the mild ambiguity by 4N-th roots of unity factors, the unreduced
QHI of M give rise to the QT intertwiners HN(TCφ,˜b, w)T , in the same projective classes as the
“reduced” ones. The unreduced QHI of M, hence the associated QT intertwiners, do not depend on
the choice of a ﬁbration of M. However they depend on the full set of cohomological weights, which
dominates the classes κ. The ratio unreduced/reduced QHI is a simpler invariant called symmetry
defect, which can be used to study the dependence of the reduced QHI with respect to the ﬁbration
of Mφ ([6]). Finally, the ambiguity of the invariants up to multiplication by 4N-th roots of unity may
not be sharp (see [5] for some improvements in the case of the unreduced QHI).
The theorems above have the following consequences.
Recall that the reduced QH invariants satisfy the identity Hred
N (Mφ, r, κ) = Trace
 Hred
N (TCφ,˜b, w)

,
and that Mφ is the interior of a compact manifold ¯
Mφ with boundary made by tori. Let us call longitude
any simple closed curve in ∂¯
Mφ intersecting a ﬁbre of ¯
Mφ in exactly one point. We have:
Corollary 1.3. The reduced QH invariants Hred
N (Mφ, r, κ) do not depend on the values of the weight
κ on longitudes.
We can also use the QH-operators Hred
N (TCφ,˜b, w) to build ﬁner invariants, associated to any ir-
reducible representation of Tq
S. Namely, recall that every reducible representation is canonically the
direct sum of its isotypical components (the maximal direct sums of isomorphic irreducible sum-
mands). Every intertwiner ﬁxes globally each isotypical component. Then, we consider the isotypical
intertwiners
Lφ
ρλ(µ) := Hred
N (TCφ,˜b, w)T
|ρλ(µ)
obtained by restriction to the isotypical components ρλ(µ) of ρλ, associated to irreducible represen-
tations µ of Tq
λ. Any irreducible representation of Tq
λ can be embedded as a summand of some local
representation ([13]), and so has a corresponding isotypical component.
We have:
Corollary 1.4. (1) The trace of Lφ
ρλ(µ) is an invariant of (Mφ, r, κ) and µ, well-deﬁned up to multi-
plication by 4N-th roots of unity. It depends on the isotopy class of φ and satisﬁes
Hred
N (Mφ, r, κ) =
X
ρλ(µ)⊂ρλ
Trace

Lφ
ρλ(µ)

.
(2) The invariants Trace(Lφ
ρλ(µ)) do not depend on the values of the weight κ on longitudes.
In perspective, another application of Theorem 1.1 would be to study the representations of the
Kauﬀman bracket skein algebras deﬁned by means of the QHI intertwiners, by using the results of
[13].
The background material is recalled in Section 2 and 3. The proofs are in Section 4.
Remark about the parameter q. In this paper we denote by q an arbitrary primitive N-th root
of unity, where N ≥3 is odd. Our orientation conventions used to deﬁne the quantum Teichm¨uller
space, in the relations (14) and (16), imply that q corresponds to q−1 in some papers about quantum
Teichm¨uller theory, eg. in [7] or [11]. Our choice of q is motivated by Thurston’s relations between
shape parameters in hyperbolic geometry; in the quantum case, this choice gives the most natural
form to the tetrahedral and edge relations between q-shape parameters (see Section 3.2).
Acknowledgement. We thank the referee for the several suggestions that have helped us to really
improve the text.
6
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
2. Topological-combinatorial support
We ﬁx a compact closed oriented smooth surface S0 of genus g, and a subset P = {p1, . . . , pr} ⊂S0
of r ≥1 marked points. We denote by S the punctured surface S0 \ P. We assume that
m := −χ(S) = (2g −2) + r > 0.
A diﬀeomorphism φ0 : S0 →S0 such that φ0(pj) = pj for every j induces a diﬀeomorphism
φ : S →S. Consider the cylinder C0 := S0 × [0, 1] with the product orientation. Denote by M0 the
mapping torus of φ0 with the induced orientation. That is, M0 := C0/∼φ0, where (x, 0) ∼φ0 (y, 1) if
y = φ0(x), x, y ∈S0. Let ˆ
M0 be the space obtained by collapsing to one point xj the image in M0 of
each line pj × [0, 1] in C0. Then ˆ
M0 is a pseudo-manifold; X = {x1, . . . , xr} is the set of singular (ie.
non manifold) points of ˆ
M0. Every singular point xj has a conical neighbourhood homeomorphic to
the quotient of T 2
j × [0, 1] by the equivalence relation identifying T 2
j × {0} to a point, where T 2
j is a
2-torus. The point xj corresponds to the coset of T 2
j × {0}, and T 2
j × {1} is called the link of xj in
ˆ
M0. So M = ˆ
M0 \ X is the interior of a compact manifold ¯
M with boundary formed by r tori. In
fact M is the mapping torus Mφ = C/∼φ, where C = S × [0, 1]. From now on, we denote by Mφ the
manifold M endowed with this ﬁbration over the circle S1, and by Cφ the mapping cylinder of φ.
Layered triangulations of Mφ can be constructed as follows (see for instance [10], where one can
ﬁnd also a proof of the well known fact that two ideal triangulations of S are connected by a ﬁnite
chain of diagonal exchanges). Consider the set of triangulations λ of S0 whose sets of vertices coincide
with P. By removing P, such a triangulation λ is also said an ideal triangulation of S; it has 3m
edges and 2m triangles. Denote by λ′ = φ0(λ) the image ideal triangulation of S. Let us ﬁx a chain
of diagonal exchanges connecting λ to λ′:
λ = λ0 →λ1 →· · · →λk = λ′.
Possibly by performing some additional diagonal exchanges followed by their inverses, we can assume
that this chain is “full”, in the sense that every edge of λ supports some diagonal exchange in the
chain. Then the chain induces a 3-dimensional triangulation T of ˆ
M0, whose tetrahedra are obtained
by “superposing”, for every j, the two squares of λj, λj+1 involved in the diagonal exchange λj →λj+1
(see Figure 1). The set of vertices of T coincides with X. The ideal triangulation T \ X is called a
layered triangulation of Mφ. It lifts to a layered triangulation TCφ of the cylinder Cφ.
For each tetrahedron of T, we call abstract tetrahedron its underlying simplicial set considered
independently of the face pairings in T. Similarly we call abstract edge or face of T any edge or face
of an abstract tetrahedra of T. Given any edge e of T, we write E →e to mean that an abstract edge
E is identiﬁed to e in the triangulation T.
From now on we assume that the diﬀeomorphism φ of S is pseudo-Anosov, so that Mφ is a hyperbolic
manifold with r cusps.
By construction every (ideally triangulated) surface (S, λj) is embedded in T and TCφ. The union
of the surfaces (S, λj) forms the 2-skeletons of T and TCφ. Every surface (S, λj) divides Mφ locally,
and the given orientations of S and Mφ determines the (local) positive side of S in M. In terms
of TCφ, the positive side of (S, λ) = (S, λ0) lifts to a collar of S × {0}, while the negative side of
(S, λ′) = (S, λk) lifts to a collar of S × {1}.
The triangulation T is naturally endowed with a taut pre-branching ω. Let us recall brieﬂy this
notion (see [6], [10]). A taut pre-branching is a choice of transverse co-orientation for each 2-face
of T, so that for every tetrahedron, exactly two of its 2-face co-orientations point inward/outward;
moreover, it is required that there are exactly two abstract diagonal edges E →e for every edge e
of T. Here, we call diagonal edges the two edges of an abstract tetrahedron whose adjacent 2-face
co-orientations point both inward or both outward. The taut pre-branching ω of T is deﬁned by the
system of transverse 2-face co-orientations dual to the orientation of the embedded surfaces (S, λj).
We ﬁx also a weak branching ˜b compatible with ω (see [5]). Recall that ˜b is a choice of vertex ordering
b for each abstract tetrahedron of T, called (local) branching, satisfying the following constraint. The
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
7
abstract 2-faces of the tetrahedron have an orientation induced by b, given by their vertex orderings up
to even permutations. Then, it is required that these orientations match, under the 2-face pairings,
with the orientations dual to ω (note that we do not require that the abstract vertex orderings
match: this deﬁnes the stronger notion of global branching). Similarly, ˜b gives an orientation to every
tetrahedron; without loss of generality, we can assume that it agrees with the orientation of M. A
weak branching ˜bj is also deﬁned on every surface triangulation λj, by giving every triangle τ in λj
the branching induced by the tetrahedron lying on the positive side of τ.
In Figure 1 we show a typical local conﬁguration occurring in T or TCφ, that is, a tetrahedron ∆,
represented under an orientation preserving embedding in R3, built by gluing squares Q, Q′ along the
boundary, carrying triangulations λ, λ′ related by a diagonal exchange. The orientation of ∆agrees
with the standard orientation of R3, and the 2-face co-orientations that deﬁne the pre-branching ω
are dual to the counter-clockwise orientation of the four faces of ∆. We have chosen one branching
b of ∆(any edge being oriented from the lowest to the biggest endpoint) among the two which are
compatible with ω and induce the given orientation of ∆. The 2-faces are ordered as the opposite
vertices are, accordingly with b.
We advertize that Figure 1 will be used to support all computations. In such a situation we will
denote by e0 the edge [v0, v1], by e1 the edge [v1, v2], and by e2 the edge [v0, v2].
Q
Q’
∆
0
3
2
1
3
1
2
0
Figure 1.
3. Background results
3.1. Classical hyperbolic geometry. Let M be any cusped hyperbolic 3-manifold with r cusps,
r ≥1.
We denote by X(M) the variety of augmented PSL(2, C)-characters of M. Let us recall the deﬁni-
tion. Consider the set of pairs (r, {ξΓ}Γ∈Π), where r: π1(M) →PSL(2, C) is a group homomorphism,
Π is the set of peripheral subgroups of π1(M) (associated to the boundary tori T 2
i of ¯
M, for all choices
of base points of π1(T 2
i ) and π1(M) and paths between them), and for every Γ ∈Π, ξΓ ∈CP 1 is a ﬁxed
point of r(Γ) such that the assignment Γ →ξΓ is equivariant with respect to the action of π1(M) on
Π by conjugation and on CP 1 via r by Moebius transformations. The set {(r, {ξΓ}Γ∈Π)} is a complex
aﬃne algebraic set R(M), with an action of PSL(2, C) deﬁned on a pair (r, {ξΓ}Γ) by conjugation on
r and Moebius transformation on {ξΓ}Γ. Then, X(M) is the algebro-geometric quotient of R(M) by
PSL(2, C), that is, the set of closed points of the ring of invariant functions C[R(M)]P SL(2,C).
Similarly we denote by X(S) the variety of augmented characters of a surface S.
In the setting of Section 2, if M = Mφ and S is a ﬁbre of the ﬁbration, then the inclusion map
i: S = S × {0} ,→Mφ induces a regular (restriction) map
i∗: X(Mφ) →X(S).
8
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Recall that π1(Mφ) is a HNN-extension of π1(S). That is, given a generating set γ1, . . . , γu of π1(S)
satisfying the relations r1, . . . , rv, there is an isomorphism between π1(Mφ) and the group generated
by γ1, . . . , γu and an element t satisfying the relations r1, . . . , rv and tαt−1 = φ∗(α) for all α ∈
π1(S), where φ∗: π1(S) →π1(S) is the isomorphism induced by φ. Therefore, every representation
r: π1(S) →PSL(2, C) that may be extended to Mφ is such that r(π1(S)) and r ◦φ∗(π1(S)) are
conjugate subgroups of PSL(2, C). Any augmented character of S that may be extended to Mφ is
thus a ﬁxed point of the map Φ∗: X(S) →X(S) induced by the map r 7→r ◦φ∗on representations,
and i∗(X(Mφ)) is a subvariety of Fix(Φ∗).
Again in the setting of Section 2, let (T,˜b) be a weakly branched layered triangulation of the
ﬁbred cusped manifold Mφ. Let us recall a few facts about the gluing variety G(T,˜b), that is, the
set of solutions of the Thurston gluing equations supported by (T,˜b). It is a complex aﬃne algebraic
set of dimension greater than or equal to r. The points of G(T,˜b) are classically called systems of
shape parameters. Their coordinates, the shape parameters, are scalars in C \ {0, 1} associated to
the abstract edges of T. The shape parameters of opposite edges of a tetrahedron are equal, and the
cyclically ordered triple of shape parameters of a tetrahedron encodes an isometry class of hyperbolic
ideal tetrahedra.
The set G(T,˜b) is deﬁned by the following two sets of equations. For every branched tetrahedron,
set wj := w(Ej), j = 0, 1, 2 (see before Figure 1 for the ordering of the edge Ej). For every edge e of
T, deﬁne the total shape parameter W(e) as the product of the shape parameters w(E), where E →e.
Then we have:
• (Tetrahedral equation) For every tetrahedron and j ∈{0, 1, 2}, wj+1 = (1 −wj)−1 cyclically;
hence w0w1w2 = −1.
• (Edge equation) For every edge e of T, W(e) = 1.
A point w ∈G(T,˜b) determines a pseudo-developing map Fw :
˜
Mφ →H3, where
˜
Mφ is the
universal cover of Mφ, and Fw is well-deﬁned up to post-composition with an orientation-preserving
isometry of H3. The map Fw sends homeomorphically the edges of ˜T to complete geodesics, and
it satisﬁes Fw(g˜x) = rw(g)Fw(˜x) for all ˜x ∈˜
Mφ, g ∈π1(Mφ), where rw : π1(Mφ) →PSL(2, C) is
a homomorphism. So w encodes the conjugacy class of rw. In fact, Fw determines also some rw-
equivariant set {ξΓ}Γ∈Π as above, so that eventually the map w 7→rw can be lifted to a regular
“holonomy” map
hol: G(T,˜b) →X(Mφ).
We have (see Proposition 4.6 of [5] when Mφ has a single cusp, and Remark 1.4 of [6] for the general
case):
Proposition 3.1. There is a subvariety A of G(T,˜b) of dimension equal to the number of cusps
of M, and a point wh ∈A, such that hol(wh) is the hyperbolic holonomy of Mφ, and hol|A is a
homeomorphism from a Zariski open subset of A containing wh onto its image.
In particular, every point w ∈A encodes an augmented character of Mφ; the algebraic closure of
hol(A) is the eigenvalue subvariety E(Mφ) of X0(Mφ), the irreducible component of X(Mφ) containing
the discrete faithful holonomy rh (see [12]). If Mφ has a single cusp, then E(Mφ) = X0(Mφ); in general
E(Mφ) contains rh and has complex dimension equal to the number of cusps of Mφ.
It follows from Proposition 3.1 that a point of i∗(X0(Mφ)) ⊂X(S) close enough to i∗(rh) is encoded
by a point w ∈A.
From now on, we consider only systems of shape parameters w lying in the subvariety A of G(T,˜b).
Denote by (T,˜b, w) the layered triangulation T of Mφ endowed with the weak branching ˜b and the
labelling of the abstract edges of T by a system of shape parameters w.
For every j = 0, . . . , k,
consider the ideally triangulated surfaces (S, λj) embedded into (T,˜b, w) as in Section 2. For every
edge e of λj, deﬁne the lateral shape parameter W +
j (e) as the product of the shape parameters of the
abstract edges E →e carried by the tetrahedra lying on the positive side of (S, λj).
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
9
Lemma 3.2. For any edge e of λj, the (exponential) shear-bend coordinate of e deﬁned by any pleated
surface Fw| ˜S (ie. any lift ( ˜S, ˜λj) of (S, λj) to ˜
Mφ, and any pseudo-developing map Fw| ˜S : ˜S →H3),
coincides with the parameter xj(e) := −W +
j (e).
The proof follows from the deﬁnitions (see eg. [7]). Note that x0(e) = xk(φ0(e)) for every edge
e of λ = λ0. Also, the shear-bend coordinate of any edge ˜e of ˜λj is eventually ‘attached’ to the
corresponding edge e of λj, because for diﬀerent choices of ˜S or Fw the images of Fw| ˜S diﬀer only by
an hyperbolic isometry.
Remarks 3.3. The parameter xj(e) is the opposite of W +
j (e) because the (oriented) bending angle
along an edge of λj is traditionally measured by the external dihedral angle π −θ (see eg. [7, 8]),
whereas the shape parameters use the internal dihedral angle θ. So θ = 0 when two adjacent ideal
triangles F(τ) and F(τ ′) coincide, for triangles τ, τ ′ of ( ˜S, ˜λj).
3.2. Quantum hyperbolic geometry. We keep the setting of the previous section.
Recall that N ≥3 is an odd integer, and q a primitive N-th root of unity.
We begin with a few qualitative, structural features of the reduced quantum hyperbolic state sum
Hred
N (T,˜b, w) deﬁned in [5, 6]. It is a regular rational function deﬁned on a covering of the gluing
variety G(T,˜b). The points of this covering over a point w ∈G(T,˜b) are certain systems of N-th roots
w(E) of the shape parameters w(E), which label the abstract edges E of T and are called quantum
shape parameters. Alike the “classical” ones, opposite edges of an abstract tetrahedron are given
the same quantum shape parameter. Moreover, the quantum shape parameters verify the following
relations, which are “quantum” counterparts of the deﬁning equations of the gluing variety. For every
branched tetrahedron of (T,˜b) put wj := w(Ej) (with the usual edge ordering ﬁxed before Figure 1).
For every edge e of (T,˜b, w), deﬁne the total quantum shape parameter W(e) as the product of the
quantum shape parameters of the abstract edges E →e. Then we have:
• (Tetrahedral relation) For every tetrahedron, w0w1w2 = −q.
• (Edge relation) For every edge e of T, W(e) = q2.
For simplicity we will work with systems of quantum shape parameters w such that the corresponding
systems of “classical” shape parameters w belong to a simply connected open neighborhood A0 ⊂
A ⊂G(T,˜b) of wh (the general case of systems w with arbitrary w ∈A is described in [5]). Note that
A0 is chosen so that w(E) varies continuously with w ∈A0.
Remarks 3.4. (1) For every z ∈C \ {0}, denote by log(z) the determination of the logarithm which
has the imaginary part in ] −π, π]. There is a Z-labelling d of the abstract edges of T such that, for
every system w of quantum shape parameters over a point w ∈A0, and every abstract edge E, we
have
(4)
w(E) = exp
 1
N (log(w(E)) + πi(N + 1)d(E))

.
The above relations veriﬁed by the quantum shape parameters can be equivalently rephrased in terms
of the Z-labelling d. For any point w ∈A0, a Z-labelling d satisfying these relations deﬁnes a system
of quantum shape parameters over w by the formula (4).
(2) In [4, 5, 6] we solved (mainly in terms of the Z-labellings d) the existence problem of triples
(T,˜b, w) for any cusped hyperbolic 3-manifold in the special case q = −exp(−iπ/N).
The same
method works for an arbitrary q, up to minor changes.
The following result summarizes in a qualitative way the invariance properties of Hred
N (T,˜b, w).
Denote by A0,N the set of systems of quantum shape parameters over A0. Recall from Section 2
that Mφ can be considered as the interior of a compact manifold ¯
Mφ bounded by tori. Fix a basis
(l1, m1), . . . , (lr, mr) of π1(∂¯
Mφ), and use it to identify H1(∂¯
Mφ; C∗) with (C∗)2r. Any augmented
character [(r, {ξΓ}Γ)] ∈X(Mφ) determines the square of one of the two (reciprocally inverse) eigen-
values of r(γ), for any non trivial simple closed curve γ on ∂¯
Mφ and representative r of the character.
Namely, by taking r in its conjugacy class so that r(π1(∂¯
Mφ)) ﬁxes the point ∞on CP 1, r([γ]) acts
10
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
on C as w 7→γrw + b, where γr ∈C∗and b ∈C. The coeﬃcient γr is that squared eigenvalue selected
by [(r, {ξΓ}Γ)].
We have (see [5] and [6]):
Theorem 3.5. (1) There exists a determined regular rational map κN : A0,N →(C∗)2r such that the
image κN(A0,N) is the open subset of (C∗)2r made of all the classes κ ∈H1(∂¯
Mφ; C∗) such that κ(lj)N
and κ(mj)N are equal up to a sign respectively to the squared eigenvalues selected by [(r, {ξΓ}Γ)] at
the curves lj and mj, where r := [(r, {ξΓ}Γ)] = hol(w) for some w ∈A0.
(2) Given r ∈hol(A0) and κ ∈H1(∂¯
Mφ; C∗) as above, the value of Hred
N (T,˜b, w) is independent, up
to multiplication by 4N-th roots of unity, of the choice of (T,˜b, w) among all weakly branched layered
triangulations of Mφ endowed with a system of quantum shape parameters w such that hol(w) = r
and κN(w) = κ.
We denote the resulting invariant by Hred
N (Mφ, r, κ) := Hred
N (T,˜b, w).
By the results of [6], it
actually depends on the ﬁbration of Mφ.
The map κN in Theorem 3.5 is a lift to A0,N of j∗◦hol|A0, where j∗is the restriction map
X(Mφ) →X(∂Mφ). Here is a concrete way to compute κN(w)(α), for α ∈H1(∂¯
Mφ; Z). It is well
known that the truncated tetrahedra of an ideal triangulation T of Mφ provide a cell decomposition
of ¯
Mφ which restricts to a triangulation ∂T of ∂¯
Mφ. Every abstract vertex of T corresponds to an
abstract triangle of ∂T (at which a tetrahedron has been “truncated”); every vertex of such a triangle
is contained in one abstract edge of T. Represent the class α by an oriented simple closed curve a
on ∂¯
Mφ, transverse to ∂T. The intersection of a with a triangle F of ∂T is a collection of oriented
arcs. We can assume that none of these arcs enters and exits F by a same edge. Then, each one turns
around a vertex of F. If ∆is a tetrahedron of T and F corresponds to a vertex of ∆, for every vertex
v of F we denote by Ev the edge of ∆containing v, and write a →Ev to mean that some subarcs of a
turn around v. We count them algebraically, by using the orientation of a: if there are s+ (resp. s−)
such subarcs whose orientation is compatible with (respectively, opposite to) the orientation of ∂¯
Mφ
as viewed from v, then we set ind(a, v) := s+ −s−. Then
(5)
κN(w)(α) =
Y
a→Ev
w(Ev)ind(a,v).
In the case where α is the class of a positively oriented meridian curve mi of ∂¯
Mφ, this gives
(6)
κN(w)(α) =
Y
mi→Ev
w(Ev).
Let us give now more details about the deﬁnition of the reduced QH state sum Hred
N (T,˜b, w). We
are going to do it in terms of the QH-operator associated to the cylinder Cφ, already mentioned in
the Introduction.
By cutting (T,˜b, w) along one of the surfaces (S, λj) (that is, a triangulated ﬁbre of Mφ), we get a
QH-triangulation (TCφ,˜b, w) of the cylinder Cφ having as “source” boundary component (S, λ), and
as “target” boundary component (S, λ′), where λ = λj and λ′ = φ(λj). It carries in a contravariant
way the QH-operator Hred
N (TCφ,˜b, w) ∈End
 (CN)⊗2m
, which is such that
Trace

Hred
N (TCφ,˜b, w)

= Hred
N (T,˜b, w).
We deﬁne the QH-operator Hred
N (TCφ,˜b, w) by means of elementary tetrahedral and 2-face operators,
as follows.
We can regard the QH triangulation (T,˜b, w) of Mφ as a network of abstract QH-tetrahedra (∆, b, w),
with gluing data along the 2-faces. To each QH-tetrahedron (∆, b, w) we associate a linear isomorphism
called basic matrix dilogarithm (“basic” refers to the fact that we have dropped a symmetrization factor
from the matrix dilogarithms that enter the deﬁnition of the unreduced QHI),
LN(∆, b, w): V2 ⊗V0 →V3 ⊗V1
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
11
where Vj is a copy of CN associated to the 2-face of (∆, b) opposite to the vertex vj. The basic
matrix dilogarithms will be deﬁned explicitly below. For the moment, note that V1, V3 correspond
to the 2-faces with pre-branching co-orientation pointing inside ∆. Concerning the gluing data, every
2-face F of T is obtained by gluing a pair of abstract 2-faces. Denote by Fs and Ft the “source” and
“target” 2-face of the pair, with respect to the transverse co-orientation deﬁned by the pre-branching
ω˜b. Denote by VFs and VFt the copies of CN associated to Fs and Ft. The identiﬁcation Fs →Ft is
given by an even permutation on three elements, which encodes the image of the vertices of Fs in Ft.
So it can be encoded by an element r(F) ∈Z/3Z. The triangulation TCφ of the cylinder Cφ has 2m
free 2-faces at both the source and target boundary components, (S, λ) and (S, λ′). Note that at every
2-face of (S, λ) the pre-branching orientation points inside Cφ, while it points outside at the 2-faces
of (S, λ′). For every gluing Fs →Ft occuring at an internal 2-face F of TCφ, as well as to every 2-face
F of (S, λ′), we associate an endomorphism (again in contravariant way)
(7)
Qr(F )
N
: VFt →VFs.
By deﬁnition, the QH-operator Hred
N (TCφ,˜b, w) is the total contraction of the network of tensors
{LN(∆, b, w)}∆and {Qr(F )
N
}F . In formulas:
(8)
Hred
N (TCφ,˜b, w) =
X
s
Y
∆
LN(∆, b, w)s
Y
F
Qr(F )
N,s
where the sum ranges over all maps s: {abstract 2-faces of T} ∪{2-faces of (S, λ′)} →{0, . . . , N −1}
(the states of (TCφ,˜b, w)), and LN(∆, b, w)s and QN,s denote the entries of the tensors LN(∆, b, w)
and QN selected by s, when the tensors are written in the canonical basis {ej} of CN. Note that
the domain of s contains two copies of each 2-face F in the target boundary component of Cφ. They
correspond to the source and target spaces VFs, VFt of Qr(F )
N
.
Finally, we provide an operator theoretic deﬁnition of the basic matrix dilogarithms (it is a straight-
forward rewriting of formula (32) in [4]), as well as their entries and those of the endomorphisms QN.
Since it is the transposed tensor Hred
N (TCφ,˜b, w)T mentioned in the Introduction (see formula (3)) that
occurs in Theorem 1.1, we consider the transposed endomorphisms of QN and of the basic matrix
dilogarithm instead:
QT
N : V ′
Fs →V ′
Ft , LT
N(∆, b, w) : V ′
3 ⊗V ′
1 →V ′
2 ⊗V ′
0
where V ′
Fs = V ′
Ft = V ′
j = (CN)′, the dual space of CN, for every j. The matrix elements will be given
with respect to the canonical basis of
 (CN)′⊗2.
Remark 3.6. If {ej} is the canonical basis of CN, and {ej} the dual basis of (CN)′, the identiﬁcation
map ι : CN →(CN)′, ι(ej) = ej, extends to a canonical identiﬁcation, also denoted by ι, between
(CN)⊗2 and
 (CN)′⊗2. Below we will rather deal with the endomorphisms
ι−1 ◦QT
N ◦ι ∈End
 CN
, ι−1 ◦LT
N(∆, b, w) ◦ι ∈End
 (CN)⊗2
.
Obviously, they have the same matrix elements as QT
N and LT
N(∆, b, w) with respect to the canonical
basis of CN and (CN)′, and (CN)⊗2 and
 (CN)′⊗2, respectively. Similarly we will consider
ι−1 ◦Hred
N (TCφ,˜b, w)T ◦ι ∈End
 (CN)⊗2m
.
For simplicity we will systematically omit the maps ι from the notations.
The endomorphism QT
N : VFs →VFt is deﬁned in the standard basis {ej} of (the copies VFs, VFt
of) CN by
(9)
QT
N(ek) =
1
√
N
N−1
X
j=0
q2kj+j2ej.
Deﬁne the endomorphisms A0, A1, A2 ∈End(CN) by
(10)
A0ek = q2kek, A1ek = ek+1, A2ek = q1−2kek−1.
12
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Note that A0A1A2 = qIdCN . We stress that these operators arise in the representation of the triangle
algebra (see Section 3.3.2 below); their occurrence in the deﬁnition of the basic matrix dilogarithm is a
key point to perform the computations at the end of the paper that will establish the bridge between
the QHI and the QT intertwiners.
Put
g(x) =
N−1
Y
j=1
(1 −xq2j)j/N, h(x) = g(x)
g(1)
Υ = 1
N
N−1
X
i,j=0
q−2ij−jAi
0 ⊗(A1A0)−j.
For any triple of quantum shape parameters w = (w0, w1, w2) and any endomorphism U such that
U N = −Id, set
Ψw(U) = h(w0)
N−1
X
i=0
U i
iY
j=1
−q−1w2
1 −w−1
0 q2j
where by convention we set the product equal to 1 when i = 0. Then
(11)
LT
N(∆, b, w) = Ψw(−A0A1 ⊗A−1
1 ) ◦Υ.
Later we will need the following elementary but crucial fact, which belongs (in a diﬀerent form) to
Faddeev-Kashaev [9].
Lemma 3.7. Let w0, w2 be complex numbers such that wN
2 = 1−w−N
0
, and U an endomorphism such
that U N = −Id. Then Ψw(U) deﬁned as above is the unique endomorphism up to scalar multiplication
which is a solution of the functional relation
(12)
Ψw(q2U) = (w0 + q−1w0w2U)Ψw(U).
Proof. The hypothesis on w0, w2 implies that the summands of Ψw(U) are periodic in i, with
period N. Hence we get the same sum if i ranges from 1 to N. With this observation, we have
q−1w0w2UΨw(U) = h(w0)
N−1
X
i=0
U i+1q−1w0w2
iY
j=1
−q−1w2
1 −w−1
0 q2j
= h(w0)
N−1
X
i=0
U i+1q−1w0w2
1 −w−1
0 q2i+2
−q−1w2
 i+1
Y
j=1
−q−1w2
1 −w−1
0 q2j
= h(w0)

−w0
N−1
X
i=0
U i+1
i+1
Y
j=1
−q−1w2
1 −w−1
0 q2j +
N−1
X
i=0
(q2U)i+1
i+1
Y
j=1
−q−1w2
1 −w−1
0 q2j


= −w0Ψw(U) + Ψw(q2U).
Hence Ψw(U) solves the equation (12).
Conversely, U N = −Id implies that U is diagonalizable
with eigenvalues in the set {−q2i, i = 0, . . . , N −1}. Hence Ψw(U) is a polynomial in U completely
determined by its eigenvalues, which are of the form Ψw(−q2i). By (12) they are given for i ≥1
by Ψw(−q2i) = Qi
j=1(w0 −q2j−3w0w2)Ψw(−1), and hence uniquely determined up to the choice of
Ψw(−1). Therefore (12) has a unique solution Ψw(U) up to scalar multiplication.
2
Remark 3.8. The normalization factor h(w0) is chosen so that det
 Ψw(−A0A1 ⊗A−1
1 )

= 1.
In particular, when (w0, w1, w2) is a triple of quantum shape parameters we have
(13)
Ψw(q2U) = (w0 −w−1
1 U)Ψw(U).
Finally the entries of LT
N(∆, b, w) in the basis {ek ⊗el}k,l of
 CN⊗2 are as follows. Identify Z/NZ
with {0, 1, . . . , N −1}. For every a ∈Z set δ(a) = 1 if a ≡0 mod(N), and δ(a) = 0 otherwise. For
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
13
every n ∈Z/NZ, consider the function ω(x, y|n) deﬁned on the curve {(x, y ∈C2| xN + yN = 1} by
ω(x, y|0) = 1, ω(x, y|n) =
n
Y
j=1
y
1 −xq−2j , n ≥1.
Then, for every i, j, k, l ∈Z/NZ we have
LT
N(∆, b, w)k,l
i,j = h(w0)q−2kj−k2ω(w0, w−1
1 |i −k)δ(i + j −l).
3.3. Representations of the quantum Teichm¨uller spaces. Unless stated diﬀerently, the results
recalled in this section are proved in [7, 8] or [11].
Let λ be an ideal triangulation of S, and q as above. Recall that m = −χ(S). Put n := 3m and
ﬁx an ordering e1, . . . , en of the edges λ. For all distinct i, j set σij := aij −aji ∈{0, ±1, ±2}, where
aij is the number of times ei is on the right of ej in a triangle of λ, using the orientation of S. The
Chekhov-Fock algebra Tq
λ is the algebra over C with generators X±1
i
associated to the edges ei, and
relations
(14)
XiXj = q2σijXjXi.
When q = 1, T1
λ is just the algebra of Laurent polynomials C[X±1
1 , . . . , X±1
n ], which is the ring
of functions on the classical (enhanced) Teichm¨uller space generated by the exponential shear-bend
coordinates on λ.
The algebra Tq
λ has a well-deﬁned fraction algebra ˆTq
λ, and any diagonal exchange λ →λ′ induces
an isomorphism of algebras
ϕq
λλ′ : ˆTq
λ′ →ˆTq
λ.
The above deﬁnition of Tq
λ works as well for any ideally triangulated punctured compact oriented
surface S, possibly with boundary, where each boundary component is a union of edges. In particular,
take S the ideal triangulated squares Q, Q′ in Figure 1. Number the edges of their triangulations λ,
λ′ as in Figure 2. In such a situation ϕq
λλ′ has the form
(15)
ϕq
λλ′(X′
5) = X−1
5
ϕq
λλ′(X′
1) = (1 + qX5)X1
, ϕq
λλ′(X′
3) = (1 + qX5)X3
ϕq
λλ′(X′
2) = (1 + qX−1
5 )−1X2
, ϕq
λλ′(X′
4) = (1 + qX−1
5 )−1X4.
It is proved in [1] (see also Theorem 1.22 in [11]) that this case of the ideal square determines,
for any punctured compact oriented surface S, a unique family {ϕq
λλ′}λλ′ of algebra isomorphisms
ϕq
λλ′ : ˆTq
λ′ →ˆTq
λ deﬁned for all ideal triangulations λ and λ′ of S, if the family satisﬁes certain
natural properties with respect to composition, diﬀeomorphisms of S, and decomposition into ideally
triangulated subsurfaces.
Q
Q’
∆
1
2
4
3
5
5
4
1
2
3
Figure 2.
Given any ideal triangulations λ, λ′ of S and ﬁnite dimensional representation ρλ : Tq
λ →End(Vλ),
one says that ρλ ◦ϕq
λλ′ makes sense if for every generator X′
i ∈Tq
λ′ the element ϕq
λλ′(X′
i) can be
14
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
written as PiQ−1
i
∈ˆTq
λ, where Pi, Qi ∈Tq
λ and ρλ(Pi), ρλ(Qi) are invertible endomorphisms of Vλ.
In such a case, ρλ ◦ϕq
λλ′(X′
i) = ρλ(Pi)ρλ(Qi)−1 is well-deﬁned (ie. independent of the choice of the
pair (Pi, Qi)).
By deﬁnition, the quantum Teichm¨uller space of S is the quotient set Tq
S := (`
λ ˆTq
λ)/ ∼, where ∼
identiﬁes the algebras ˆTq
λ and ˆTq
λ′ by ϕq
λλ′, for all ideal triangulations λ, λ′ of S. A representation of
Tq
S is a family of representations
ρ := {ρλ : Tq
λ →End(Vλ)}λ
indexed by the set of ideal triangulations of S, such that ρλ ◦ϕq
λλ′ makes sense for every λ, λ′ and is
isomorphic to ρλ′. In fact, it is enough to check the isomorphisms ρλ′ ∼= ρλ ◦ϕq
λλ′ whenever λ and λ′
diﬀer by a ﬂip.
3.3.1. Local representations. The irreducible representations of Tq
S were classiﬁed up to isomorphism
in [7]. The local representations of Tq
S are special reducible representations deﬁned as follows (see
[8, 11]). Deﬁne the triangle algebra T as the algebra over C with generators Y ±1
0
, Y ±1
1
, Y ±1
2
and
relations
(16)
Y0Y1 = q2Y1Y0, Y1Y2 = q2Y2Y1, Y2Y0 = q2Y0Y2.
Fix an ordering τ1, . . . , τ2m of the triangles of λ. Order the abstract edges ej
0, ej
1, ej
2 of τj so that the
induced cyclic ordering is counter-clockwise with respect to the orientation of S. Associate to τj a
copy Tj of the algebra T , with generators denoted by Y j
0 ,Y j
1 ,Y j
2 , so that Y j
i is associated to the edge
ej
i. There is an algebra embedding
(17)
iλ : Tq
λ →T1 ⊗. . . ⊗T2m
deﬁned on generators by (we denote a monomial ⊗jAj in ⊗jTj by omitting the terms Aj = 1):
• If ei is an edge of two distinct triangles τli and τri, and eli
ai, eri
bi are the edges of τli, τri
respectively identiﬁed to ei, then iλ(Xi) := Y li
ai ⊗Y ri
bi .
• If ei is an edge of a single triangle τki, and eki
ai, eki
bi are the edges of τki identiﬁed to ei, with
eki
ai on the right of eki
bi , then iλ(Xi) := q−1Y ki
ai Y ki
bi = qY ki
bi Y ki
ai .
A representation ρλ of Tq
λ is local if
ρλ = (ρ1 ⊗. . . ⊗ρ2m) ◦iλ : Tq
λ →End(V1 ⊗. . . ⊗V2m)
for some irreducible representations ρj : T →End(Vj) of T , j ∈{1, . . . , 2m}. So, a local representation
is an equivalence class of tuples (ρ1, . . . , ρ2m), where two tuples are equivalent if their restrictions to
the subalgebra iλ(Tq
λ) of T1 ⊗. . . ⊗T2m deﬁne the same representation. Two local representations
ρλ = (ρ1 ⊗. . . ⊗ρ2m) ◦iλ and ρ′
λ = (ρ′
1 ⊗. . . ⊗ρ′
2m) ◦iλ of Tq
λ are isomorphic if there are linear
isomorphisms Lj : Vj →V ′
j such that for every j = 1, . . . , 2m and Y ∈Tj we have
Lj ◦ρj(Y ) ◦(Lj)−1 = ρ′
j(Y ).
It is straightforward to check that this deﬁnition is independent of the choice of tuples (ρ1, . . . , ρ2m),
(ρ′
1, . . . , ρ′
2m). By deﬁnition a local representation ρ of Tq
S is a representation formed by local repre-
sentations ρλ.
3.3.2. Isomorphism classes and standard local representations. The isomorphism classes of irreducible
representations of the triangle algebra T are parametrized by tuples of non zero scalars (y0, y1, y2, h) ∈
(C•)4 such that hN = y0y1y2. The parameter h is called the load of the class. The isomorphism class
with parameters (y0, y1, y2, h) can be represented by standard representations ρ : T →End(CN),
which have the form
(18)
ρ(Yi) = yiAi, i ∈{0, 1, 2}
where y0, y1, y2 ∈C∗satisfy
yN
i = yi, i ∈{0, 1, 2}, h = y0y1y2
and A0, A1, A2 are the endomorphisms of CN deﬁned in (10).
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
15
Any local representation of Tq
λ has dimension N 2m. The isomorphism class of a local representation
ρλ of Tq
λ is determined by:
• a non zero complex weight xi associated to each edge of λ;
• a N-th root h of x1 . . . xn, called the load.
The weights xi and the load h are such that
(19)
ρλ(XN
i ) = xiIdV1⊗...⊗V2m, ρλ(H) = hIdV1⊗...⊗V2m
where H is a central element of Tq
λ, called the principal central element, given by
(20)
H = q−P
l<l′ σll′X1 . . . Xn.
Note that hN = x1 . . . xn. It is straightforward to check that two local representations are iso-
morphic if and only if they are isomorphic as local representations.
We call ({x1, . . . , xn}, h) the
parameters of ρλ. We say that a local representation ρλ = (ρ1 ⊗. . . ⊗ρ2m) ◦iλ is standard if every ρi
is. This notion naturally extends to representations of Tq
S. Every point of (C∗)n can be realized as the
n-tuple of parameters xi, i = 1, . . . , n, of a standard local representation of Tq
λ. There is a one-to-one
correspondence between isomorphism classes of local representations {ρλ : Tq
λ →End(V1⊗. . .⊗V2m)}λ
of Tq
S and families of parameters {({x1, . . . , xn}λ, hλ)}λ such that
(21)
hλ = hλ′ and xi = ϕ1
λλ′(x′
i)
for every i = 1, . . . , n and any two ideal triangulations λ, λ′ of S with edge weights {x1, . . . , xn},
{x′
1, . . . , x′
n} and loads hλ, hλ′ respectively. The edge weights xi of a local representation ρλ : Tq
λ →
End(Vλ) deﬁne its “classical shadow”
sh(ρλ) : T1
λ →End(C)
by taking the restriction of ρλ to the subalgebra C[X±N
1
, . . . , X±N
n
] ∼= T1
λ of the center of Tq
λ. This
notion extends immediately to local representations ρ = {ρλ : Tq
λ →End(Vλ)}λ of Tq
S; the classical
shadow
sh(ρ) = {sh(ρλ) : T1
λ →End(C)}λ
is a representation of the coordinate ring T1
S of the Teichm¨uller space (considered as a rational manifold
with transition functions the maps ϕ1
λλ′).
Every representation of T1
S is the shadow of N local
representations of Tq
S. The shadows of local representations encode the Zariski open subset of X(S)
made of the so-called peripherically generic characters. These include all the augmented characters of
injective representations.
The load h has the following geometric interpretation. Let [(r, {ξΓ}Γ∈Π)] be the augmented char-
acter of S determined by sh(ρ). Each Γ ∈Π is a group generated by the class in π1(S) of a small
loop mj in S going once and counter-clockwise around the j-th puncture, for some j ∈{1, . . . , r}
and some choice of basepoints. Since π1(S) is a free group, r: π1(S) →PSL(2, C) can be lifted to a
homomorphism ˆr: π1(S) →SL(2, C); the ﬁxed point ξΓ ∈P1 is then contained in an eigenspace of
ˆr(mj), corresponding to an eigenvalue aj ∈C. Then
(22)
hN = (−1)ra−1
1
. . . a−1
r .
Finally, the decomposition into irreducible summands of a local representation ρλ of Tq
λ is ([13])
(23)
ρλ = ⊕ρλ(µ)⊂ρλ ρλ(µ)
where the sum ranges over the set of all spaces ρλ(µ) formed by intersecting one eigenspace for each
of the so-called (central) puncture elements of Tq
λ. Each space ρλ(µ) is also the isotypical component
of an irreducible representation µ of Tq
λ, that is, the direct sum of all irreducible summands of ρλ
isomorphic to µ. Every irreducible representation of Tq
λ has an isotypical summand appearing in some
local representation, and has multiplicity N g in it.
16
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
3.4. Intertwiners of local representations. Let (S, λ) and q be as before. Any surface R obtained
by splitting S along some (maybe all) edges of λ inherits an orientation from S, and an ideal trian-
gulation µ from λ. By gluing along edges backwards, one says that (S, λ) is obtained by fusion from
(R, µ). In such a case, every local representation ηµ = (η1 ⊗. . . ⊗η2m) ◦iµ of Tq
µ determines a local
representation ρλ of Tq
λ by setting ρλ = (η1 ⊗. . . ⊗η2m) ◦iλ. One says that ηµ represents ρλ.
Given local representations η = {ηµ : Tq
µ →End(Wµ)}µ, ρ = {ρλ : Tq
λ →End(Vλ)}λ of Tq
R and Tq
S
respectively, one says that ρ is obtained by fusion from η if ηµ represents ρλ for all ideal triangulations
µ of R, where λ is the ideal triangulation of S obtained by fusion from µ.
In [11], the following result is proved. The intertwiners Lρρ′
λλ′ ∈Lρρ′
λλ′ in the statement are called QT
intertwiners.
Theorem 3.9. There exists a collection {(Lρρ′
λλ′, ψρρ′
λλ′)}, indexed by the couples of isomorphic local
representations ρ = {ρλ : Tq
λ →End(Vλ)}λ, ρ′ = {ρ′
λ : Tq
λ →End(V ′
λ)}λ of Tq
S and by the couples of
ideal triangulations λ, λ′ of S, such that:
(1) Lρρ′
λλ′ is a set of projective classes of linear isomorphisms Lρρ′
λλ′ : Vλ →Vλ′ such that for every
X′ ∈Tq
λ′ we have
Lρρ′
λλ′ ◦(ρλ ◦ϕq
λλ′)(X′) ◦(Lρρ′
λλ′)−1 = ρ′
λ′(X′).
(2) ψρρ′
λλ′ : H1(S; Z/NZ) × Lρρ′
λλ′ →Lρρ′
λλ′ is a free transitive action.
(3) Let R be a surface such that S is obtained by fusion from R. Let η = {ηµ : Tq
µ →End(Wµ)}µ,
η′ = {η′
µ : Tq
µ →End(W ′
µ)}µ be two local representations of Tq
R such that ρ, ρ′ are obtained respectively
by fusion from η, η′. Then, for every ideal triangulations µ, µ′ of R, if λ, λ′ are the corresponding
ideal triangulations of S, there exists an inclusion map j : Lηη′
µµ′ →Lρρ′
λλ′ such that for every L ∈Lηη′
µµ′
and every c ∈H1(R; Z/NZ) the following holds:
(j ◦ψηη′
µµ′)(c, L) = ψρρ′
λλ′(π∗(c), j(L))
where π: R →S is the projection map.
(4) For every isomorphic local representations ρ, ρ′, ρ′′ of Tq
S and for every ideal triangulations λ, λ′,
λ′′ of S the composition map
Lρρ′
λλ′ × Lρ′ρ′′
λ′λ′′
−→
Lρρ′′
λλ′′
(L1, L2)
7−→
L2 ◦L1
is well-deﬁned, and for all c, d ∈H1(S; Z/NZ) it satisﬁes
ψρ′ρ′′
λ′λ′′(d, L2) ◦ψρρ′
λλ′(c, L1) = ψρρ′′
λλ′′(c + d, L2 ◦L1).
It is also proved in [11] that any collection of intertwiners satisfying a weak form of conditions (3)
and (4) (not involving the actions ψρρ′
λλ′) contains the collection {Lρρ′
λλ′}. So the latter is minimal with
respect to these conditions.
Note that property (3) describes the behaviour of the intertwiners in Lρρ′
λλ′ under cut-and-paste
of subsurfaces along edges of λ, λ′.
In particular, it implies that they can be decomposed into
elementary intertwiners as follows.
Any two ideal triangulations λ, λ′ of S can be connected by
a sequence λ = λ0 →. . . →λk+1 = λ′ consisting of k diagonal exchanges followed by an edge
reindexing λk →λk+1 (with same underlying triangulation). Then, any projective class of intertwiners
[Lρρ′
λλ′] ∈Lρρ′
λλ′ can be decomposed as
(24)
Lρρ′
λλ′ = Lρρ′
λ′λ′ ◦Lρρ
λkλk+1 ◦· · · ◦Lρρ
λ0λ1
where Lρρ
λiλi+1 ∈Lρρ
λiλi+1 intertwins ρλi and ρλi+1 ◦(ϕq
λiλi+1)−1, related by the i-th diagonal exchange,
for every i ∈{0, . . . , k −1}, and Lρρ′
λ′λ′ intertwins ρλ′ and ρ′
λ′ on the triangulation λ′. In general the
intertwiner Lρρ′
λλ′ depends on the choice of sequence λ = λ0 →. . . →λk+1 = λ′, but the set Lρρ′
λλ′ and
the action ψρρ′
λλ′ do not.
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
17
4. Proofs
We are ready to prove our main Theorems 1.1, 1.2, and Corollary 1.4. Let us reformulate them by
using the background material recalled in the previous sections.
Let Mφ be a ﬁbred cusped hyperbolic 3-manifold realized as the mapping torus of a pseudo Anosov
diﬀeomorphism φ of a punctured surface S. Put m = −χ(S) > 0. Let Cφ be the associated cylinder.
Let T be a layered triangulation of Mφ, and TCφ the induced layered triangulation of Cφ, with source
boundary component the ideally triangulated surface (S, λ), and target boundary component (S, λ′),
where λ′ = φ(λ) (as in Section 2).
For every odd N ≥3 and every primitive N-th root of unity q, let (T,˜b, w) be a QH layered
triangulation of Mφ, where w is a system of quantum shape parameters over w ∈A, where A
is the subvariety of the gluing variety G(T,˜b) as in Proposition 3.1.
Let (TCφ,˜b, w) be the in-
duced QH triangulation of Cφ, and Hred
N (TCφ,˜b, w) ∈End
 (CN)⊗2m
the QH operator deﬁned by
means of the QH state sum carried by (TCφ,˜b, w). Associated to it we have the transposed operator
Hred
N (TCφ,˜b, w)T ∈End
 ((CN)′)⊗2m
and ι−1 ◦Hred
N (TCφ,˜b, w)T ◦ι ∈End
 (CN)⊗2m
as in Section
3.2, still denoted by Hred
N (TCφ,˜b, w)T (see Remark 3.6).
Now we re-state and prove our ﬁrst main theorem, Theorem 1.1.
First Main Theorem. (1) Every layered QH-triangulation (TCφ,˜b, w) determines representations
ρλ and ρλ′ of Tq
λ and Tq
λ′ respectively, belonging to a local representation ρ of Tq
S and such that
Vλ = Vλ′ = (CN)⊗2m, and ρλ is isomorphic to φ∗ρλ′.
Moreover, the operator Hred
N (TCφ,˜b, w)T ,
considered as an element of Hom(Vλ, Vλ′), is a QT intertwiner which intertwins the representations
ρλ and ρλ′.
(2) For any other choice of weak branching ˜b′, Hred
N (TCφ,˜b′, w)T intertwins local representations
canonically isomorphic to ρλ, ρλ′ respectively.
Proof. We organize the proof in several steps:
Step 1. Every transposed basic matrix dilogarithm LT
N(∆, b, w) ∈End
 (CN)⊗2
(see Section 3.2)
intertwins standard local representations of Tq
λ, Tq
λ′ (see Section 3.3.2), where λ, λ′ are the ideal
triangulations of the squares Q, Q′ in Figure 3.
Q
Q’
∆
1
2
4
3
5
5
4
1
2
3
Figure 3.
Step 2. Every transposed 2-face operator (QT
N)r(F ) : Vs →Vt (see (9)) intertwins representations of
the triangle algebra ρs : T →End
 CN
, ρt : T →End
 CN
, associated to the abstract 2-faces Fs, Ft
so that for each one the generator Y0 labels the edge joining the lowest vertex to the middle one (with
respect to the vertex ordering induced by the branching), and Y1 labels the edge joining the lowest
vertex to the biggest one.
Step 3.
Every layered QH-triangulation (TCφ,˜b, w) of the cylinder Cφ, associated to a sequence
of diagonal exchanges λ = λ0 →λ1 →· · · →λk = λ′, determines standard local representations
18
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
ρj : Tq
λj →End
 (CN)⊗2m
associated to the surfaces (S, λj), for every j ∈{0, . . . , k}. These repre-
sentations belong to a local representation ρ of the quantum Teichm¨uller space Tq
S.
By Step 1, Step 2, and its actual deﬁnition by means of a QH state sum, Hred
N (TCφ,˜b, w)T intertwins
the local representations ρ0 and ρk.
Step (2) proves the claim (2) in the First Main Theorem; the three steps together prove (1). The
details follow.
4.0.1. Proof of Step 1. Consider the squares Q, Q′ and the branched tetrahedron (∆, b) in Figure 3.
Use the branching to order as e0, e1, e2 the edges of any triangle of the squares Q, Q′, so that e0 goes
from the lowest vertex to the middle one, and e1 goes from the lowest vertex to the biggest one. In
such a situation there are two embeddings (17), of the form iλ : Tq
λ →T3 ⊗T1, iλ′ : Tq
λ′ →T2 ⊗T0,
where Ti is the copy of the triangle algebra associated to the i-th 2-face (ie. opposite to the i-th
vertex) of (∆, b), and
iλ(X1) = Y 3
0 ⊗1, iλ(X2) = 1 ⊗Y 1
1 , iλ(X3) = 1 ⊗Y 1
2 , iλ(X4) = Y 3
2 ⊗1, iλ(X5) = Y 3
1 ⊗Y 1
0 .
iλ′(X′
1) = Y 2
0 ⊗1, iλ′(X′
2) = Y 2
1 ⊗1, iλ′(X′
3) = 1 ⊗Y 0
2 , iλ′(X′
4) = 1 ⊗Y 0
0 , iλ′(X′
5) = Y 2
2 ⊗Y 0
1 .
Note that Y i
j is associated to the edge ej of the i-th 2-face of (∆, b), that we have speciﬁed above.
Recall the notion of standard local representation in Section 3.3.2.
Proposition 4.1. Let ρλ = (ρ3 ⊗ρ1) ◦iλ : Tq
λ →End(V3 ⊗V1) be a standard local representation,
and yi
j be such that ρi(Y i
j ) = yi
jAj, for i ∈{1, 3}, j ∈{0, 1, 2}. Let w be a triple of quantum shape
parameters of the branched tetrahedron (∆, b) such that w2 = −qy3
1y1
0. Then, for all X ∈Tq
λ we have
(25)
LT
N(∆, b, w) ◦ρλ(X) = ρλ′((ϕq
λλ′)−1(X)) ◦LT
N(∆, b, w)
where ρλ′ = (ρ2 ⊗ρ0) ◦iλ : Tq
λ′ →End(V2 ⊗V0) is the standard representation given by
(26)
y2
0 = w−1
0 y3
0
,
y2
1 = w−1
1 y1
1
,
y0
0 = w−1
1 y3
2
,
y0
2 = w−1
0 y1
2
,
y2
2y0
1 = −qw−1
2 .
Remark 4.2. Note that w2 and w1 = wN
1
= (1 −wN
2 )−1 and w0 = 1 −w−1
1
are determined
by ρλ, but the choice of N-th root w1 (or w0) is free; this choice determines w, and hence ρλ′,
completely by the relation w0w1w2 = −q. Also, we have ρλ(X5) = y3
1y1
0A1 ⊗A0 = −q−1w2A1 ⊗A0,
ρλ′(X′
5) = −qw−1
2 A2 ⊗A1, so that
ρλ(XN
5 ) = −w2IN ⊗IN, ρλ′((X′
5)N) = −w−1
2 IN ⊗IN.
Proof. It is enough to check (25) for X ∈{X1, . . . , X5}, using the relations (15). Let us do the
cases X = X5 and X4, the other cases being respectively similar to this last. For X = X5 recall that
ϕq
λλ′(X′
5) = X−1
5 ; in this case the identity (25) reads
LT
N(∆, b, w) ◦(y1
0y3
1A1 ⊗A0) = (y0
1y2
2A2 ⊗A1)−1 ◦LT
N(∆, b, w).
Consider the factorization formula (11). We have (A2 ⊗A1)−1 = qA1A0 ⊗A−1
1 , so it commutes with
Ψw(−A0A1 ⊗A−1
1 ) and we get
(y0
1y2
2A2 ⊗A1)−1 ◦LT
N(∆, b, w) =
= Ψw(−A0A1 ⊗A−1
1 ) ◦(q(y0
1y2
2)−1A1A0 ⊗A−1
1 ) ◦

1
N
N−1
X
i,j=0
q−2ij−jAi
0 ⊗(A1A0)−j


= Ψw(−A0A1 ⊗A−1
1 ) ◦

1
N
N−1
X
i,j=0
q−2(i+1)(j+1)−(j+1)+3Ai
0 ⊗(A1A0)−j

◦
◦(q(y0
1y2
2)−1A1A0 ⊗A−1
1 )
= LT
N(∆, b, w) ◦(q3A−1
0
⊗A1A0) ◦(q(y0
1y2
2)−1A1A0 ⊗A−1
1 )
= LT
N(∆, b, w) ◦((y0
1y2
2)−1A1 ⊗A0).
Hence the identity (25) holds true for X = X5 whenever
(27)
(y0
1y2
2)−1 = y1
0y3
1 = −q−1w2.
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
19
For X = X4 recall that ϕq
λλ′(X′
4) = (1 + qX−1
5 )−1X4; in this case the identity (25) reads
(28)
LT
N(∆, b, w) ◦(y3
2A2 ⊗IN) = (1 + qy2
2y0
1A2 ⊗A1) ◦(IN ⊗y0
0A0) ◦LT
N(∆, b, w).
Now we have:
LT
N(∆, b, w)◦(y3
2A2 ⊗IN)
= Ψw(−A0A1 ⊗A−1
1 ) ◦(y3
2A2 ⊗IN) ◦

1
N
N−1
X
i,j=0
q−2i(j+1)−jAi
0 ⊗(A1A0)−j


= Ψw(−A0A1 ⊗A−1
1 ) ◦(qy3
2A2 ⊗A1A0) ◦Υ
= (qy3
2A2 ⊗A1A0) ◦Ψw(q2(−A0A1 ⊗A−1
1 )) ◦Υ
= (qy3
2A2 ⊗A1A0) ◦(w0 + q2w−1
1 A1A0 ⊗A−1
1 ) ◦Ψw(−A0A1 ⊗A−1
1 ) ◦Υ
= (1 + w0w1(A1A0)−1 ⊗A1) ◦(w−1
1 A1A0 ⊗A−1
1 )◦
◦(qy3
2A2 ⊗A1A0) ◦LT
N(∆, b, w)
= (1 −q2w−1
2 A2 ⊗A1) ◦(IN ⊗w−1
1 y3
2A0) ◦LT
N(∆, b, w).
Note that we used the relation (13) in the fourth equality. Hence, using (27) we see that (25) holds
true for X = X4 whenever y0
0 = w−1
1 y3
2. The other cases X = X1, X2 or X3 are similar.
2
4.0.2. Proof of Step 2. Consider QH-tetrahedra (∆, b, w), (∆′, b′, w′) glued along a 2-face F. Denote
as usual by Fs, Ft the abstract 2-faces of ∆, ∆′ corresponding to F. Recall that the vertices v0, v1,
v2 of Fs and Ft are ordered by the branchings b and b′ respectively; the gluing Fs →Ft is encoded by
an even permutation p := σr(F ) of the vertices, where σ is the 2-cycle (v0v1v2) and r(F) ∈Z/3Z.
Assume that a standard representation of the triangle algebra ρs : T →End(CN) is given on Fs,
where the generators Y0 labels the edge [v0, v1], and Y1 labels the edge [v0, v2]. Using the gluing, ρs
is the pull-back of a standard representation ρt : T →End(CN) on Ft, where now Y0 labels the edge
[vp(0), vp(1)], and Y1 labels the edge [vp(0), vp(2)]. So Yi on Fs corresponds to Yp−1(i) on Ft.
We have:
Lemma 4.3. The endomorphism (QT
N)r(F ) intertwins ρs and ρt. Namely, for all X in T we have
(QT
N)r(F ) ◦ρs(X) = ρt(X) ◦(QT
N)r(F ).
Proof. It is enough to check this on generators, where it follows from QT
NAi(QT
N)−1 = Ai−1 (indices
mod(3)). This is straightforward to check.
2
Note that QN has order 3 up to multiplication by 4-th roots of 1 (see [5], Lemma 7.3: if N = 2n+1,
we have Q3
N = φ−1
N IN, where φN =
  n+1
N

if N ≡1 mod(4), and φN =
  n+1
N

i if N ≡3 mod(4)).
4.0.3. Proof of Step 3. Let (TCφ,˜b, w) be a layered QH-triangulation of the cylinder Cφ as usual.
Recall that for every j ∈{0, . . . , k}, the triangulated surface (S, λj) inherits a weak branching ˜bj from
its positive side in (T,˜b, w). Order as τ j
1, . . . , τ j
2m the branched abstract triangles of (λj,˜bj). For every
i ∈{1, . . . , 2m}, order as ei
0, ei
1, ei
2 the edges of the triangle τ j
i , as described before Proposition 4.1
and Lemma 4.3. Label ei
k with the generator Y i
k of a copy of the triangle algebra T .
Assume that for some j ∈{0, . . . , k} we are given a standard local representation
ρj = (ρj
1 ⊗. . . ⊗ρj
2m) ◦iλj : Tq
λj →End((CN)⊗2m)
where the standard representations ρj
i : T →End(CN) are associated to the triangles τ j
i . As in
(18), put ρj
i(Yk) := yj
i,kAk. By the very deﬁnition of iλj (see (17)), for any edge es of λj, with edge
generator Xs ∈Tq
λj, we have (as usual we denote a monomial ⊗jAj in T ⊗2m by omitting the terms
Aj = 1):
(a) ρj(Xs) = yj
li,aiyj
ri,biAli
ai ⊗Ari
bi, if es is an edge of two distinct triangles τ j
li and τ j
ri, and eli
ai,
eri
bi are the edges of τ j
li, τ j
ri respectively identiﬁed to es.
20
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
(b) ρj(Xs) = q−1yj
ki,aiyj
ki,biAki
aiAki
bi , if es is an edge of a single triangle τ j
ki, and eki
ai, eki
bi are the
edges of τ j
ki identiﬁed to es, with eki
ai on the right of eki
bi .
Consider the diagonal exchange λj →λj+1, and the corresponding triangulated (abstract) squares Q
and Q′, as in Figure 3. The standard representations ρj
i : T →End(CN) associated to the triangles of
Q deﬁne a standard local representation ρQ of Tq
λj|Q. Denote by ρQ′ the standard local representation
of Tq
λj+1|Q′ deﬁned from ρQ by the relations (26), where (∆, b, w) is the QH-tetrahedron of (TCφ,˜b, w)
bounded by Q and Q′; we describe below the relations between w and ρj (and hence ρQ).
The
representation ρQ′ extends (by fusion) to a standard local representation
ρj+1 = (ρj+1
1
⊗. . . ⊗ρj+1
2m ) ◦iλj : Tq
λj+1 →End((CN)⊗2m)
by stipulating that ρj+1
i
= ρj
i on the common triangles of (S, λj) and (S, λj+1). Since (S, λj+1) is
given the weak-branching ˜bj+1 induced by its positive side in (TCφ,˜b, w), for every triangle τ j+1
i
of
(S, λj+1) where ˜bj+1 diﬀers from the weak-branching given by (S, λj) or Q′, replace the corresponding
representation ρj+1
i
by (QT
N)r(F ) ◦ρj+1
i
(X) ◦(QT
N)−r(F ), as in Lemma 4.3. For simplicity, we keep
however the same notation for ρj+1. Deﬁne
Lρjρj+1
λjλj+1 : End((CN)⊗2m) →End((CN)⊗2m)
as the operator acting as the identity on all factors except on the representation space CN ⊗CN ,→
(CN)⊗2m of ρQ, where it acts by

(QT
N)r(F2) ⊗(QT
N)r(F0)
◦LT
N(∆, b, w). Here, as usual we denote
by F2 and F0 the 2-faces supporting the target space of LT
N(∆, b, w).
By construction, for every
X ∈Tq
λj+1 we have
(29)
Lρjρj+1
λjλj+1 ◦ρj ◦ϕq
λjλj+1(X′) ◦(Lρjρj+1
λjλj+1)−1 = ρj+1(X).
Finally, assuming that a standard local representation ρj is given for j = 0, by working as above we
can deﬁne inductively a sequence of standard local representation ρj, j = 0, . . . , k, and set
Lρ0,ρk
λ0,λk := Lρk−1ρk
λk−1λk ◦· · · ◦Lρ0ρ1
λ0λ1.
Comparing with (8) we see that
Lρ0,ρk
λ0,λk = Hred
N (TCφ,˜b, w)T .
Now we have to specialize the choice of ρ0, structurally related to the triangulation (TCφ,˜b, w).
Similarly to the “classical” lateral shape parameters W +
j (e) (Section 3.1), put:
Deﬁnition 4.4. For every edge e of (S, λj), the lateral quantum shape parameter W+
j (e) is the product
of the quantum shape parameters w(E) of the abstract edges E →e carried by tetrahedra lying on
the positive side of (S, λj). The quantum shear-bend coordinates of (S, λj) are the scalars
xj(e) := −q−1W+
j (e).
Denote by λ(1)
j
the set of edges of the ideal triangulation λj.
By Proposition 3.2, the quantum shear-bend coordinates xj(e), e ∈λ(1)
j , form a system of N-th
roots of the shear-bend coordinates xj(e) of λj.
By ﬁxing w and varying w over w in the tuple
(TCφ,˜b, w), one obtains a family of systems {xj(e)}e∈λ(1)
j
such that x0(e) = xk(φ(e)) for every edge e
of λ = λ0.
The QH-triangulation (TCφ,˜b, w) determines xj(es) for all j ∈{0, . . . , k} and every edge es of λj.
Consider the case j = 0, and the regular map
π0 : {y0 = (y0
i,k)i,k} →{x0 = (x0(es))es∈λ(1)
0 }
deﬁned by
(30)
x0(es) = y0
li,aiy0
ri,bi
or
y0
ki,aiy0
ki,bi
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
21
according to the cases (a) or (b) described at the beginning of Step 3. A simple dimensional count
shows that π0 is surjective, with generic ﬁbre isomorphic to (C∗)3m. Then, take a point y0 ∈π−1
0 (x0).
We get
(31)
ρ0(Xs) = x0(es)Ali
ai ⊗Ari
bi
or
ρ0(Xs) = q−1x0(es)Aki
aiAki
bi
again according to the cases (a) or (b) above. We have to check that the sequence of local representa-
tions ρj constructed by starting from ρ0 is consistent, that is, compatible with w under the diagonal
exchanges. Using the notations of Figure 3, by the tetrahedral and edge relations satisﬁed by the
quantum shape parameters, for all j ∈{0, . . . , k} we have
(32)
xj(e5) = −q−1w2, xj+1(e5) = −qw−1
2
and
(33)
xj+1(e1) = xj(e1)w−1
0
,
xj+1(e2) = xj(e2)w−1
1
xj+1(e3) = xj(e3)w−1
0
,
xj+1(e4) = xj(e4)w−1
1 .
In particular, (32) for j = 0 is consistent with the relation w2 = −qy3
1y1
0 required by Proposition
4.1 (where y3
1 = y0
ri,bi and y1
0 = y0
li,ai).
Then, comparing (33) and (26) we see that for every
j ∈{0, . . . , k}, ρj is indeed deﬁned by identities like (31), with x0 replaced by xj.
By (29), the representations ρ0, . . . , ρk belong to a local representation ρ = {ρλ : Tq
λ →End(Vλ)}λ
of Tq
S. By (19), (31) and the similar identities for ρj, we see that the parameters of ρj are
({xj(e)}e∈λ(1)
j , h)
where xj(e) = (xj(e))N and
(34)
h =
Y
e∈λ(1)
j
xj(e).
For this identity, ﬁrst note that the right hand side, say hj, does not depend on j. Indeed, by (32),
(33) and the tetrahedral and edge relations for w0, w1 and w2, we see that
Q5
i=1 xj(ei) = Q5
i=1 xj+1(ei)
under a diagonal exchange. Since the quantum shear-bend coordinates of edges not touched by a
diagonal exchange are not altered, we deduce that hj = hj+1 for every j = 0, . . . , k −1. Now we
can check (34) as follows. Consider a triangle τ j
s of λj, with edges Xi, Xj, Xk, where i < j < k.
The weak branching ˜b provides a bijection p: {i, j, k} 7→{0, 1, 2}. Then iλj(H) is a tensor product of
monomials associated to the triangles of λj, and the monomial for τ j
s is q
−σ|τj
s Y s
p(i)Y s
p(j)Y s
p(k) where
−σ|τ j
s is the contribution to the summand −σij −σik −σjk of −P
l<l′ σll′ coming from the triangle
τ j
s . Noting that the product Y s
0 Y s
1 Y s
2 is invariant under cyclic permutations, one checks immediately
that q
−σ|τl
j Y s
p(i)Y s
p(j)Y s
p(k) = q−1Y s
0 Y s
1 Y s
2 . So
iλj(H) = ⊗2m
s=1(q−1Y s
0 Y s
1 Y s
2 )
and hence
ρj(H) = ⊗2m
s=1(ys
0ys
1ys
2q−1As
0As
1As
2) = xj(e1) . . . xj(en)Id(CN)⊗2m.
Summarizing our discussion, we have proved the following result. It concludes the proof of Step 3
of our First Main Theorem, and hence of Theorem 1.1 in the introduction.
Proposition 4.5. The QH triangulation (TCφ,˜b, w) determines a sequence of standard local repre-
sentations ρj : Tq
λj →End((CN)⊗2m) associated to the triangulated surfaces (S, λj), with parameters
({xj(e)}e∈λ(1)
j , h), h = Q
e∈λ(1)
j
xj(e),
and belonging to a local representation ρ of Tq
S. Moreover, Hred
N (TCφ,˜b, w)T intertwins the represen-
tations ρ0 and ρk.
22
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Let us consider now Theorem 1.2. For the convenience of the reader we re-state it. We keep the
usual setting. Recall that Mφ is the interior of a compact manifold ¯
Mφ with boundary made by tori.
Second Main Theorem. There is a neighborhood of i∗(rh) in i∗(X0(Mφ)) ⊂X(S) such that:
(1) For any isomorphism class of local representations of Tq
S whose holonomy lies in this neighbor-
hood, there are:
• A representative ρ of the class, and representations ρλ, ρλ′ belonging to ρ and acting on
(CN)⊗2m,
• a layered QH triangulation (T,˜b, w) of Mφ such that Hred
N (T,˜b, w) = Hred
N (Mφ, r, κ), for some
weight κ ∈H1(∂¯
Mφ, C∗) and augmented character r of π1(Mφ) such that the restriction of r
to π1(S) is the holonomy of ρ,
such that the operator Hred
N (TCφ,˜b, w)T is a QHI intertwiner which intertwins ρλ and ρλ′ as in Propo-
sition 4.5. The load of ρ is determined by the values of the weight κ at the meridian curves that form
¯S ∩¯
Mφ.
(2) The family of QHI intertwiners {Hred
N (TCφ,˜b, w)T } consists of the QT intertwiners which inter-
twin ρλ to ρλ′ and whose traces are well deﬁned invariants of triples (Mφ, r, κ) such that the restriction
of r to π1(S) is the holonomy of ρ.
Proof. (1) Let ρ: Tq
λ →End((CN)⊗2m) be a local representation with parameters ({x(e)}e∈λ(1), h).
Recall Proposition 3.1 and the discussion that follows. Assume that the augmented character [(r, {ξΓ}Γ)]
associated to ρ lies in i∗(X0(Mφ)), and can be encoded by a system of shape parameters w ∈A0 ⊂A,
the simply connected open neighborhood of wh in G(T,˜b) chosen before Remark 3.4. Then we can lift
w to a system of quantum shape parameters w ∈A0,N, and using the QH-triangulation (TCφ,˜b, w),
we can deﬁne a local representation ρ′ : Tq
λ →End((CN)⊗2m) in the same way as ρ0 in the proof
of Proposition 4.5 (see (31)). It has quantum shear-bend coordinates x(e), e ∈λ(1), and parameters
({x(e)}e∈λ(1), h′), where h′ = Q
e∈λ(1) x(e). The system {x(e)}e∈λ(1) is the same for ρ and ρ′, so in order
that ρ′ ∼= ρ, it remains to show that we can choose w so that h′ = h. But (h′)N = Q
e∈λ(1) x(e) = hN,
so h′ = ζh for some N-th root of unity ζ. On the other hand, by Theorem 3.5 (1), at all the meridian
curves mj of ∂¯
Mφ we have
κN(w)(mj)N = ±a−2
j
where aj is deﬁned before the identity (22), and we note that a−2
j
is the dilation factor of the similarity
transformation associated to the conjugate of r(mj) ﬁxing ∞, whence the squared eigenvalue at mj
selected by [(r, {ξΓ}Γ)]. Hence
(h′)2N = a−2
1
. . . a−2
r
= ±κN(w)(m1)N . . . κN(w)(mr)N.
Moreover, there is w′ ∈A0,N so that κN(w′)(m1) . . . κN(w′)(mr) is any given N-th root of a−2
1
. . . a−2
r .
Let ζ′ be the N-th root of unity such that (h′)2 = ζ′κN(w)(m1) . . . κN(w)(mr). By using the formula
(6) it is easy to check that
(35)
κN(w)(mj) = (−q−1)tj
Y
e|pj∈∂e
W+(e)
where W+(e) is the lateral quantum shape parameter of (S, λ) at the edge e of λ, tj is the number
of spikes of the triangles of λ at the j-th puncture pj of S, and the product is over all the edges e,
counted with multiplicity, having pj as an endpoint. Recalling that there are 3m = −3χ(S) edges in
λ, we deduce
κN(w)(m1) . . . κN(w)(mr) = (−q−1)3.2m Y
e∈λ(1)
W+(e)2
(36)
= (−q−1)6m(−q)6m Y
e∈λ(1)
x(e)2 = (h′)2.
(37)
Hence ζ′ = 1. Then take w′ ∈A0,N so that κN(w′)(m1) . . . κN(w′)(mr) = (h′)2ζ−2. The load h′′
of the representation ρ′′ associated to w′ satisﬁes (h′′)2 = (h′)2ζ−2 = h2. Since N is odd, and again
(h′′)N = hN, eventually h = h′′. This achieves the proof of the claim (1) of the theorem.
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
23
(2) We need to describe the general form of the QT intertwiners associated to sequences of diagonal
exchanges λ →. . . →λ′, for arbitrary standard local representations ρλ, ρλ′ of Tq
λ, Tq
λ′. This is done
in Lemma 4.8. For that, we reconsider the arguments of the proof of the claim (1) in the First Main
Theorem. First, we look at the case of a diagonal exchange λ →λ′, occuring in squares Q, Q′ as in
Figure 3. We ﬁx standard local representations ρλ, ρλ′ of Tq
λ, Tq
λ′ such that ρλ′ ◦(ϕq
λλ′)−1 is isomorphic
to ρλ, and diﬀers from it only on Q, Q′, where ρλ, ρλ′ are represented by irreducible representations
ρj of the triangle algebra with parameters yj
k, where j ∈{0, 1, 2, 3} and k ∈{0, 1, 2}.
Lemma 4.6. With the above notations we have
(38)
y3
0/y2
0 = y1
2/y0
2 , y1
1/y2
1 = y3
2/y0
0 , y3
1y1
0 = (y2
2y0
1)−1.
Moreover, denoting these scalars by ˜w0, ˜w1 and ˜w2 respectively, (w0, w1, w2) := ( ˜wN
0 , ˜wN
1 , ˜wN
2 ) is a
triple of shape parameters on (∆, b), that is wi+1 = (1 −wi)−1 for i = 0, 1.
We say that ( ˜w0, ˜w1, ˜w2) is a triple of rough q-shape parameters on (∆, b). Each of the scalars ˜wj
corresponds to a pair of opposite edges of ∆. Note that, in general, the product ˜w0 ˜w1 ˜w2 can be any
N-th root of −1, the special case of −q being achieved by the q-shape parameters.
Proof. We prove ﬁrst the second claim, that is, the N-th powers of the scalars set equal in (38) are
indeed equal, and form a triple of shape parameters (w0, w1, w2). By the relations (15) we have
ϕq
λλ′((X′
5)N) = ϕq
λλ′((X′
5))N = X−N
5
ϕq
λλ′((X′
1)N) = ϕq
λλ′(X′
1)N = (X1 + qX5X1)N = XN
1 + XN
5 XN
1
ϕq
λλ′((X′
2)N) = ϕq
λλ′(X′
2)N = (X−1
2
+ qX−1
2 X−1
5 )−N = (X−N
2
+ X−N
2
X−N
5
)−1
and a relation like the second for X′
3, X3, and like the fourth for X′
4, X4. Note that we use the
q-binomial formula and the fact that q2 is a primitive N-th root of 1, N odd, to deduce the results.
Hence the shear-bend parameters xi, x′
i at the edges ei, i ∈{1, . . . , 5}, satisfy
x′
5 = x−1
5
, x′
1 = x1(1 + x5) , x′
3 = x3(1 + x5) , x′
2 = x2(1 + x−1
5 )−1 , x′
4 = x4(1 + x−1
5 )−1.
Set x5 = −w2. By a mere rewriting of formulas, it follows easily from this, (30) and x(e)N = x(e) for
all edges e of λ, that
(39)
−w2 = (y3
1y1
0)N = (y2
2y0
1)−N
w0 = x1/x′
1 = x3/x′
3 = (y3
0/y2
0)N = (y1
2/y0
2)N
w1 = x2/x′
2 = x4/x′
4 = (y1
1/y2
1)N = (y3
2/y0
0)N.
and wi+1 = (1−wi)−1 for i = 0, 1. Now we prove (38). Let us reconsider Proposition 4.1 in the present
situation. Instead of ρλ and the system (w0, w1, w2) of quantum shape parameters on (∆, b), it is the
pair of local representations ρλ, ρλ′ that are given on Q, Q′, and we are looking for ( ˜w0, ˜w1, ˜w2) such
that the identity (25) holds true. Again (25) yields the ﬁrst equality of (27), which is the last relation
of (38), without implying any constraints on ( ˜w0, ˜w1, ˜w2). Then, use it to deﬁne ˜w2 by the same
formula. Replacing all uses of the relation (13) by (12) in the other computations deﬁnes ˜w0 = y3
0/y2
0
and ˜w1 = y1
1/y2
1, and eventually proves the ﬁrst two identities in (38). For instance, in the case of
X = X4 the result becomes
LT
N(∆, b, ˜w) ◦(y3
2A2 ⊗IN) = (1 −q2 ˜w−1
2 A2 ⊗A1) ◦
 IN ⊗(−q−1 ˜w0 ˜w2y3
2A0)

◦LT
N(∆, b, ˜w)
and hence (28) holds true whenever ˜w0 = −qy0
0/y3
2 ˜w2. Comparing with the result of the similar
computation for X = X2 we ﬁnd the second identity in (38). The other cases are similar.
2
Now we have:
Proposition 4.7. (See [7, 11]) Assume that S is an ideal polygon with p ≥3 vertices. Then for every
ideal triangulation λ of S, every local representation of Tq
λ is irreducible.
In the situation of the lemma we have the ideal squares Q, Q′, and so the proposition implies that
LT
N(∆, b, ˜w) is a representative of the unique projective class of intertwiners from ρλ to ρλ′ ◦(ϕq
λλ′)−1.
More generally, let λ, λ′ be ideal triangulations of S connected by a sequence of diagonal exchanges,
and let ρ, ρ′ be isomorphic standard local representations of Tq
S. Then every QT intertwiner Lρρ′
λλ′
24
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
between ρλ and ρ′
λ′ has a representative of the form (24), where Lρρ′
λiλi+1 = LT
N(∆, b, ˜w) for some
system ˜w := ( ˜w0, ˜w1, ˜w2) of rough q-shape parameters (as in Lemma 4.6) on the tetrahedron (∆, b)
associated to the i-th diagonal exchange.
Hence, proceeding as in the proof of Proposition 4.5 we deduce that:
Lemma 4.8. Every projective class of QT intertwiner in Lρρ′
λλ′ is represented by a QH state sum
Hred
N (TCφ,˜b, ˜w)T , where ˜w is a system of rough q-shape parameters on TCφ.
The proof of the claim (2) of the Second Main Theorem then follows by analysing the invariance
properties of the QH state sums Trace

Hred
N (TCφ,˜b, ˜w)

. Such an analysis has been done in [4] and
[5] in the case of the unreduced QH state sums on arbitrary closed pseudo-manifold triangulations.
It applies verbatim to the reduced QH state sums by combining the results of Section 5 of [4] with
Proposition 6.3 (1) and 8.3 of [6].
The result is that Trace

Hred
N (TCφ,˜b, ˜w)

is an invariant of the triple (Mφ, r, κ) if and only if it
is invariant under any layered ‘2 ↔3 transit’ or ‘lune transit’ of (TCφ,˜b, ˜w); such transits enhance
to ˜b and ˜w the usual 2 ↔3 and lune moves between layered triangulations (which correspond to the
pentagon and square relations for diagonal exchanges between surface triangulations). This invariance
property happens if and only if ˜w satisﬁes the tetrahedral and edge relations along every interior
edge of TCφ, that is, when ˜w is a genuine system of quantum shape parameters. In that situation
Trace

Hred
N (TCφ,˜b, ˜w)

a QHI intertwiner.
For instance, the relation (27) implies that, modifying TCφ by introducing in the sequence λ →
. . . →λ′ two consecutive diagonal exchanges along an edge e, Hred
N (TCφ,˜b, ˜w) is unchanged if and
only if the total quantum shape parameter at e satisﬁes W(e) = q2.
This concludes the proof of our Second Main Theorem.
2
Finally, let us consider Corollary 1.3 and 1.4. For the reader’s convenience we re-state them below
as Corollary 1 and 2. We keep the usual setting. Let us ﬁx a QH-triangulation (TCφ,˜b, w) of the
cylinder Cφ. Recall that Hred
N (Mφ, r, κ) = Trace
 Hred
N

TCφ,˜b, w)

, and that Mφ is the interior of a
compact manifold ¯
Mφ with boundary made by tori. Call longitude any simple closed curve in ∂¯
Mφ
intersecting a ﬁbre of ¯
Mφ in exactly one point.
Corollary 1. The reduced QH invariants Hred
N (Mφ, r, κ) do not depend on the values of the weight
κ on the longitudes.
Proof. Denote by ρλ the local representation of Tq
λ associated to (TCφ,˜b, w) as in Proposition 4.5,
where λ = λ0. Since κ = κN(w) is given by its values on the longitudes and the meridian curves mj
of ∂¯
Mφ, it is enough to show that r and the scalars κ(mj) determine the parameters ({x1, . . . , xn}, h)
of ρλ. We already know that x1, . . . , xn are determined by r. Now, by the identities (36) and (37) we
have h2 = κ(m1) . . . κ(mr). Among the two square roots of h2, the load h is the only one which is an
N-th root of (−1)ra−1
1
. . . a−1
r
(using the notations of (22)). The eigenvalues ai being determined by
the augmented character r, the conclusion follows.
2
Recall that given a local representation ρλ and an irreducible representation µ of Tq
λ, we denote by
ρλ(µ) the isotypical component associated to µ in the direct sum decomposition of ρλ into irreducible
factors. Consider the isotypical intertwiners Lφ
ρλ(µ) := Hred
N (TCφ,˜b′, w)T
|ρλ(µ).
Corollary 2. (1) The trace of Lφ
ρλ(µ) is an invariant of (Mφ, r, κ) and µ, well-deﬁned up to multipli-
cation by 4N-th roots of unity. It depends on the isotopy class of φ and satisﬁes
Hred
N (Mφ, r, κ) =
X
ρλ(µ)⊂ρλ
Trace

Lφ
ρλ(µ)

.
(2) The invariants Trace

Lφ
ρλ(µ)

do not depend on the values of the weight κ on longitudes.
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
25
Proof. (1) We take back the notations used for Corollary 1. Once again, Hred
N (Mφ, r, κ) is determined
by φ and the isomorphism class of the local representation ρλ, because it is the trace of Hred
N (TCφ,˜b, w).
Each isotypical component of ρλ is the intersection of one eigenspace of each of the so called puncture
elements of Tq
λ (see [7] and [13]). Hence it is determined by the parameters ({x1, . . . , xn}, h) of ρλ,
together with a system of puncture weights pj ∈C∗, the eigenvalues of the puncture elements. These
can be any N-th root of κ(mj)N, where κ(mj) is computed in (35). Hence r and κ determine one
isotypical component of ρλ. The others correspond to all other systems of puncture weights obtained
by multiplying each pj with some N-th root of unity. Since Hred
N (TCφ,˜b, w) intertwins ρλ and ρλ′, it
intertwins their isotypical components too. The usual invariance proof of the reduced QHI still apply,
and we get that the traces of the isotypical intertwiners are singly invariant.
By the results of [5, 6], the invariants Hred
N (Mφ, r, κ) actually depend on the choice of mapping
torus realization Mφ of M. Therefore the invariants Trace(Lφ
ρλ(µ)) do as well. By the same arguments
as for Hred
N (Mφ, r, κ), they are also deﬁned for any augmented character r in a Zariski open subset of
the eigenvalue subvariety of X0(M) (see the comments on Theorem 1.2 in the Introduction).
The proof of (2) is the same as the one of the previous corollary.
2
References
[1] H. Bai, A uniqueness property for the quantization of Teichm¨uller Spaces, Geom. Dedicata 128:1 (2007) 1–16
[2] H. Bai, Quantum Teichm¨uller space and Kashaev’s 6j-symbols, Alg. Geom. Topol. 7 (2007) 1541–1560
[3] S. Baseilhac, R. Benedetti, Quantum Hyperbolic invariants of 3-manifolds with PSL(2, C)-characters, Topology
43 (6) (2004) 1373–1423
[4] S. Baseilhac, R. Benedetti, Classical and quantum dilogarithmic invariants of ﬂat PSL(2, C)-bundles over 3-
manifolds, Geom. Topol. 9 (2005) 493–570
[5] S. Baseilhac, R. Benedetti, Analytic families of quantum hyperbolic invariants, Alg. Geom. Topol. 15 (2015) 1983–
2063
[6] S. Baseilhac, R. Benedetti, Non ambiguous structures on 3-manifolds and quantum symmetry defects, to appear
in Quantum Topology, ArXiv:1506.01174v2 (2016)
[7] H. F. Bonahon, X. Liu, Representations of the quantum Teichm¨uller space and invariants of surface diﬀeomor-
phisms, Geom. Topol. 11 (2007) 889–937
[8] H. Bai, F. Bonahon, X. Liu, Local representations of the quantum Teichm¨uller space, ArXiv:0707.2151 (2007)
[9] L.D. Faddeev, R.M. Kashaev, Quantum dilogarithm, Mod. Phys. Lett. A 9 (5) (1994) 427–434
[10] M. Lackenby, Taut ideal triangulations of 3manifolds, Geom. Topol. 4 (2000) 369-395
[11] F. Mazzoli, Intertwining operators of the quantum Teichm¨uller space, ArXiv:1610.06056 (2016)
[12] B. Klaﬀ, S. Tillmann, A birationality result for character varieties, Math. Res. Lett. (4) 23 (2016), 1099–1110
[13] J. Toulisse, Irreducible decomposition for local representations of quantum Teichm¨uller space, Arxiv:1404.4938v2
(2016)
