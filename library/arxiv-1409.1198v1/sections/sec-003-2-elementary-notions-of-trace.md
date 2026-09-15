---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-003-2-elementary-notions-of-trace
section_title: "Elementary notions of trace"
section_number: 2
pages: 7-9
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
2.1. T races of linear maps. In this section we recall the deﬁnition and properties of the trace f or
any linear endomorphism. Throughout this paper /CZ is assumed to be a ﬁeld.
The trace of an n ×n matrix M = {Mij}1≤i,j,≤n is the sum of its diagonal entries ∑
iMii. Given
two square matrices A,B , the trace satisﬁes the trace property
(2.1) tr( AB) = tr(BA).
Exercise 2. Show that property (2.1) uniquely characterize the trace in the following sense: Two linear
functions on the space of matrices satisfying (2.1) are proportional. Hint: any non-diagonal elementary
matrix can be written as a commutator, i.e. Eij = [Eii,E ij].
More generally, for any ﬁnite-dimensional /CZ -vector space V , trace is a linear map
tr : End
/CZ
(V ) → /CZ
such that the trace relation holds:
tr(fg ) = tr(gf ) for any f,g ∈ End
/CZ
(V ).
Exercise 3. Show that this (basis independent) deﬁnition of the trace co incides with the usual one,
where the trace of a matrix representing f in some basis is taken. Hint: use Exercise 2.
As a simple invariant of any linear endomorphism, the trace has a varie ty of important applications.
Let us just mention few of them.
• For any representation φ : G → Aut
/CZ
(V ) of a group G, the character χφ : G → /CZ of the
representation φ is the function sending each group element g ∈ G to the trace of φ(g). The
character of a representation carries much of the essential info rmation about a representation.
In particular, for G a ﬁnite group and /CZ = C, the complex representations of G are determined
up to isomorphism by their characters.
• A Lie algebra g deﬁned over /CZ acts on itself via the adjoint action sending x ∈ g to the
endomorphism ad x deﬁned by ad x(y) = [x,y ] for all y ∈ g. When g is ﬁnite dimensional, there
is a symmetric bilinear form (or Killing form) B : g × g → /CZ deﬁned by B(x,y ) := tr(ad xady).
The non-degeneracy of this form is used to determine if a Lie algebra is semisimple.
8 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LA UDA
• In topology Markov trace is used to construct link invariants out of representations of braid
groups.
2.1.1. Diagrammatics for the trace. The category V ect
/CZ
has the structure of a pivotal monoidal cate-
gory. What this means is that this category admits a surprisingly rich diagrammatic calculus. In this
calculus, edges are labelled by ﬁnite dimensional vector spaces and p lanar diagrams represent linear
maps between the tensor product of vector spaces labelling the bo ttom strands to the tensor product
of vector spaces labelling the top strands.
f
V2V1
W1 W2W3
f : V1 ⊗V2 − →W1 ⊗W2 ⊗W3.
In this graphical calculus the ground ﬁeld /CZ is depicted by the empty strand. The ability to compose
linear maps and to tensor linear maps is reﬂected in the graphical calc ulus by stacking the diagrams
on top of each other and juxtaposing them side by side, respective ly.
The “pivotal” structure on the category V ect
/CZ
of ﬁnite-dimensional vector spaces indicates the
existence of certain diagrams in the graphical calculus. To be concr ete, ﬁx a basis {e1,...,e n} of the
vector space V . Denote by {e∗
1,...,e ∗
n} the basis for the dual space V ∗ = Hom(V, /CZ ), with e∗
i (ej) = δij.
Then there are linear maps
ev
V ∗ V
ev : V ∗ ⊗V → /CZ
e∗
i ⊗ej ↦→e∗
i (ej) coev
V V ∗ coev : /CZ →V ⊗V ∗.
1 ↦→∑
iei ⊗e∗
i
Exercise 4. Prove that the maps ev and coev satisfy the following identities
(IdV ⊗ev) ◦ (coev ⊗ IdV ) = Id V, and (ev ⊗ IdV ∗ ) ◦ (IdV ∗ ⊗coev) = Id V ∗
and depict these relations in the graphical calculus descri bed above.
It is common practice in this diagrammatic calculus to simplify these diag rams
V ∗ V :=
ev
V ∗ V
V V ∗
:=
coev
V V ∗
used to represent ev and coev. Using the ﬂip map in V ect
/CZ
V W
W V τ : V ⊗W → W ⊗V
v ⊗w ↦→ w ⊗v,
we can also deﬁne other caps and caps
V V ∗ :=
ev
V ∗ V
V ∗ V :=
coev
V V ∗
Exercise 5. Given a linear endomorphism f :V →V the following diagram
V
f
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 9
is multiplication by an element of the ground ﬁeld /CZ . Show that this element is exactly the trace of f .
Utilizing the evaluation and coevaluation map it is possible to dualize any m ap f : V →W to get a
map f ∗ : W ∗ →V ∗. Using these dual morphisms it is possible to slide linear maps through c aps and
cups
V
W V ∗
f =
W ∗
W V ∗
f ∗
V
W ∗ W
f =
W ∗
V ∗ V
f ∗
Using these facts and the identiﬁcation of ( V ∗)∗ with V , it is not hard to verify the trace property:
f
g
=
g
f
In particular, for f = 1 V , the identity endomorphism of V , tr(1 V ) = dim(V ). Here we are using the
“right” trace. In a pivotal category one could also take the “left” trace and these two traces need not
coincide.
This pictorial presentation was extended to the category of color ed ribbon graphs, graphically de-
scribing arbitrary ribbon categories such as the category of ﬁnite dimensional representation of quantum
groups [55, 60]. This graphical calculus can also be seen as a speciﬁc in stance of string diagrams in a
2-category [59, 26, 38].
