---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-002-12-absolute-versus-relative-donaldsonthomas-theo
section_title: "Absolute versus relative Donaldson–Thomas theory"
section_number: 1.2
pages: 3-5
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
Thomas theory and cohomological Hall algebras associated to quive rs, a vital role
is always played by the grading by NQ0 , the semigroup of dimension vectors, which
should be seen as a weight space decomposition in the language of Lie a lgebras and
quantum groups. As an illustration, consider the case in which we for get about po-
tentials and stability conditions, set S to be the category of all ﬁnite-dimensional
CQ-modules, and consider the NQ0 -graded vector space
(2)
⨁
d∈NQ0
H(Md, Q[dim(Md)]).
4 BEN DA VISON AND SVEN MEINHARDT
Considering the resulting cohomology as a NQ0 × Z-graded vector space, where
the extra Z factor keeps track of cohomological degree, each graded piece is ﬁnite-
dimensional. The initial role of the NQ0 grading is to break the above inﬁnite-
dimensional vector space into inﬁnitely many manageable, ﬁnite-dime nsional pieces.
Moreover, the cohomological Hall algebra structure respects th e NQ0 × Z-grading,
so that this grading provides a route to understanding this algebra .
Choosing a bijection between the vertices Q0 and the numbers {1, . . . , n}, motivic
DT partition functions are expressed as formal power series in var iables q1/2, x1, . . . , xn.
For d = (d1, . . . ,dn) the coeﬃcient of
xd :=
∏
i∈Q0
xdi
i
is a formal Laurent power series in q1/2, given by the characteristic function of
the dth graded piece of the right hand side of (2) — for now q1/2 records the
cohomological degree. These power series may have ﬁnite order po les at q1/2 = 0,
due to the shifts appearing in (2). In the general case this formal Laurent power
series is replaced by a formal Laurent power series recording the ﬁ nite dimensions
of the weight ﬁltration of an inﬁnite-dimensional NQ0 -graded (monodromic) mixed
Hodge structure associated to the quiver Q, a potential W and a stability condition
ζ — in the ﬁnal version of the theory, q1/2 records weights.
In order to make the presentation in this paper conceptually unifor m, we slightly
change the perspective on the NQ0 -grading. We consider NQ0 -graded vector spaces
(respectively, mixed Hodge structures) as sheaves of vector sp aces (respectively,
mixed Hodge modules) on the monoid NQ0 , considered as a scheme with inﬁnitely
many components, each isomorphic to Spec( C). Then our main object of study (1)
can be thought of as the direct image of the restriction to the stac k of modules in
S of
(3) ICζ
W,µ :=
⨁
d∈Λ ζ
µ
L− dim(Mζ -ss
d )/2 ⊗φ Tr(W )ζ
µ
QMζ -ss, S
d
along the map
Dim : Mζ -ss
µ →Λζ
µ
taking each component of the moduli stack to the dimension vector of the modules
it parametrises.Instead of studying this direct image directly, we st udy the direct
image
(4) H(Aζ
W,µ ) := H
(
(Mζ -ss
µ
pζ
µ
− − → Mζ -ss
µ )∗ICζ
W,µ
)
where the map pζ
µ takes a CQ-module to its semisimpliﬁcation in the category of
ζ-semistable CQ-modules, i.e. the associated polystable object. Since Dim factors
through pζ
µ , understanding the direct image along pζ
µ turns out to be the key to
understanding the direct image along Dim.
We ﬂag at the outset the curious role of the symbol H on the right hand side
of (4). Firstly, its purpose is to make our lives simpler: we will not actu ally give
a deﬁnition of the pushforward of ICζ
W,µ , nor indeed of ICζ
W,µ itself, and we only
deﬁne the result of applying the total cohomology functor to this p ushforward,
i.e. we deﬁne the right hand side of (4) without deﬁning its constituen t pieces.
This apparent bug turns out to be a feature; because of this extr a H, taking the
dual compactly supported hypercohomology of the right hand side of (4) does not
produce something that is a priori isomorphic to the right hand side o f (1), and the
comparison between them turns out to be a central aspect of the paper. In brief: the
compactly supported hypercohomology of the right hand side of (4 ) is the associated
COHAS AND QUANTUM ENVELOPING ALGEBRAS 5
graded of the perverse ﬁltration of H
(
Aζ ,S
W,µ
)
. This perverse ﬁltration is one of the
central structures that we introduce in order to understand th e cohomological Hall
algebra.
Here and elsewhere, if L ∈ D is an element of a triangulated category with a
t-structure (for example the bounded derived category of an Ab elian category A,
such as the category of monodromic mixed Hodge modules on Mζ -ss
µ ) then
H(L) :=
⨁
n∈Z
Hi(L)[−i],
considered as an element in D with zero diﬀerential. If moreover D has inﬁnite
coproducts (for example, the unbounded derived category of A as above) then the
natural functor from Z-graded objects in A to the essential image of the functor H
is an embedding of categories; it is bijective on isomorphism classes of objects and
faithful, but not full in general.
Note that Dim ζ
µ = dimζ
µ pζ
µ , where dim ζ
µ : Mζ
µ → Λζ
µ is the natural map. We
furthermore prove that there is an isomorphism of cohomologically g raded mon-
odromic mixed Hodge modules
H
(
Dimζ
µ ,∗ ICζ
W,µ
)
∼
= H
(
dimζ
µ ,∗ H
(
(Mζ -ss
µ
pζ
µ
− − → Mζ -ss
µ )∗ICζ
W,µ
))
(5)
= H
(
dimζ
µ ,∗ H
(
Aζ
W,µ
))
in Section 4, so that an understanding of (4) can indeed be used to g ain an under-
standing of the left hand side of (5). As noted above, because of t he second H on
the right hand side of (5), this isomorphism would not follow directly fr om the usual
six functor formalism for monodromic mixed Hodge modules on stacks , but instead
relies essentially on the “hidden properness” of the morphism pζ
µ . The key obser-
vation is that pζ
µ , while not proper or representable, is in some sense approximated
by proper maps of schemes (see Section 4.1).
Working over the base Mζ -ss
µ instead of Λζ
µ is what we mean by the relative
theory. The payoﬀ for working in the relative setting is that we obta in more reﬁned
results, which are nevertheless easier to prove, since in this relativ e setting, because
of hidden properness, we are able to make extensive use of Morihiko Saito’s version
[40, 42, 43] of the famous decomposition theorem of Beilinson, Bern stein, Deligne
and Gabber [3], as well as the rest of Saito’s theory of mixed Hodge mo dules.
The idea of proving local results on Mζ -ss
µ to deduce global results about Donaldson–
Thomas invariants was already present in the work of Joyce and Son g [25], and later
the proof of the integrality conjecture for path algebras in the ab sence of a potential
by the second author and Markus Reineke [35], which utilised Eﬁmov’s t heorem [16]
on free supercommutativity for cohomological Hall algebras withou t potentials to
understand the local behaviour of the morphism pζ
µ .
