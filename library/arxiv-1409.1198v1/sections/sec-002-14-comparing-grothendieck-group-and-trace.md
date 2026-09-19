---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-002-14-comparing-grothendieck-group-and-trace
section_title: "Comparing Grothendieck group and trace"
section_number: 1.4
pages: 3-7
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
ﬁcation. One which we will refer to as the Grothendieck decategoriﬁcation which is closely connected
to the notion of dimension, graded dimension, and Euler characteris tic. Our second notion of decate-
goriﬁcation, which we will call the trace decategoriﬁcation, seems to generalize the Grothendieck group
decategoriﬁcation in much the same way that the trace of linear map generalizes the dimension of a
vector space dim(V ) = tr(1 V ). The trace decategoriﬁcation is closely connected with the usual trace
and it gives rise to a notion of traced Euler characteristic.
These two notions of decategoriﬁcation can actually produce the s ame results in some very interesting
examples. One of the most spectacular examples is the categoriﬁca tion of the Jones polynomial by the
Khovanov complex of graded /CI -modules, where the Jones polynomial can be recovered as the gra ded
Euler characteristic [31, 32]. Bar-Natan generalized Khovanov’s co nstruction by deﬁning the so-called
Khovanov bracket: a complex over an additive category of special 2-dimensional cobordisms. In his
setting, one recovers the Jones polynomial by means of the trace d Euler characteristic (Theorem 6
[4]). Hence, the functor Tr or the zeroth Hochschild–Mitchell homo logy replaces K0 in the Bar-Natan
setting.
This survey paper is devoted to the comparison of K0 and Tr as decategoriﬁcation functors. The
interplay between these two notions of decategoriﬁcation is surpr isingly rich. It can be thought of as a
categorical counterpart to the Chern character map, see for e xample [16].
4 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LA UDA
1.5. Quantum group categoriﬁcations. There is a strong interplay between quantum link invari-
ants and algebraic objects known as quantum groups. Given the ex istence of link homology theories
categorifying link invariants, it is perhaps not surprising to discover that quantum groups can also be
categoriﬁed. In this article we will examine how the two notions of dec ategoriﬁcation given by the
Grothendieck group and the trace can be applied to categoriﬁed qu antum groups.
Quantum groups are Hopf algebras associated to Lie algebras g. They are obtained by q-deforming
the universal enveloping algebra U(g). Lusztig’s modiﬁed, or idempotented, form ˙U(g) of the quantum
group Uq(g) is well suited for categoriﬁcation. These algebras are equipped wit h a family of orthogonal
idempotents 1 λ indexed by the weight lattice X of g. Any /CZ -algebra A equipped with orthogonal
idempotents indexed by a set X can be regarded as an additive category whose objects are the ele ments
of X. Given two elements λ,µ ∈X, /CZ -vector space of maps from λ to µ can be deﬁned by 1 µA1λ. In
this framework, the idempotents 1 λ are thought of as identity morphisms from the object λ to itself.
Composition in the category
1µ′A1λ′ × 1µA1λ →δµ,λ′ 1µ′A1λ
is given by multiplication in A.
By thinking of a quantum group Uq(g) as a linear category in this way, we are naturally led to
consider a categoriﬁcation of Uq(g) given by the structure of a 2-category and our decategoriﬁcat ion
map must reduce a linear 2-category to a linear 1-category.
Associated to a ﬁeld /CZ and a symmetrizable Kac-Moody algebra g, a 2-category ˙U (g) was deﬁned in
[33] generalizing the sl2 case from [37]. The 2-category ˙U(g) is the idempotent completion, or Karoubi
envelope, of a 2-category U(g) deﬁned in terms of a graphical calculus. More precisely, the objec ts of
the category U(g) are indexed by the weight lattice X of g. The morphisms are formal direct sums of
composites of maps 1λ : λ →λ, Ei1λ : λ →λ+αi, and Fi1λ : λ →λ−αi corresponding to the Chevalley
basis of g. For each 1-morphism x there is also a grading shifted 1-morphism x⟨t⟩ in U(g). The 2-
morphisms are given by k -linear degree preserving combinations of certain planar diagrams m odulo
local relations. See Figure 1 for an example of planar diagram in U(g).
/d79/d79/d15/d15 /d79/d79/d15/d15
/d79/d79/d18/d18 /d15/d15/d79/d79
i
k
λ′
/d13/d13
•
/d15/d15
•
/d15/d15
•
/d15/d15
•
/d79/d79
••
/d80/d80/d79/d79
/d15/d15
/d77/d77
•m/d77/d77
•
iki
ℓ i j
j
ℓ •
•
•
/d79/d79 /d79/d79 /d79/d79
•
i i k
λ
Figure 1. An example of a diagram representing a 2-morphism in U(g) from
E 2
i EℓFiFkFiEiEiEk1λ to EℓEiFjFjFiEjEiEkEi1λ⟨t⟩. The degree ⟨t⟩ of this 2-morphism
is determined by the relationship between the simple roots i,j,k,ℓ in the Cartan datam
associated to g.
Extending the split Grothendieck group decategoriﬁcation map for linear categories, it is possible
to deﬁne the split Grothendieck group K0 of a linear 2-category. It was shown in [33] for g = sln
that applying this notion of decategoriﬁcation to the Karoubi enve lope ˙U(sln) of the 2-category U(sln)
produces the integral idempotented form of the quantum envelop ing algebra Uq(sln). Hence, with this
notion of decategoriﬁcation the 2-category ˙U(sln) can be viewed as a categoriﬁcation of the quantum
group Uq(sln). The n = 2 case of this result was proven in [37] and the case of general g appears in
[64]. For a closely related construction see [57].
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 5
More recently it has been shown that using a 2-categorical analog o f the trace as the decategoriﬁ-
cation map produces some very rich structures [8, 65, 7]. The trac e relation can be realized diagram-
matically by considering the diagrams for U(g) on an annulus.
λλ′
/d15/d15/d79/d79
/d79/d79/d79/d79 /d15/d15 /d15/d15
/d15/d15/d79/d79 ii
•
The invariance of the graphical calculus of U(g) under planar deformations allows us to slide portions
of the diagram around the annulus imposing the trace relation.
1.6. T races of categoriﬁed quantum groups. In this article we hope to emphasize that the trace
decategoriﬁcation map Tr has various advantages to K0.
• Using Tr we can work with the 2-category U(g) rather than its Karoubi envelope, since Tr does
not change under the passage to the Karoubi envelope. This is a nic e advantage as the passage
to the Karoubi envelope often takes us out of the purely diagramm atic world.
• Trace is deﬁned for linear categories; in order for K0 to be deﬁned the category needs to be
additive.
• The trace can have a richer structure than K0 as is demonstrated by Theorems 5.1 and 6.2.
We outline the methods and tools used in studying K0 and traces for categoriﬁed quantum groups.
1.6.1. Trace and K0 of ˙U . Just as the Euler characteristic and traced Euler characteristic a gree for
Khovanov homology, we will explain that the 2-categories U(g) simultaneously categorify the quantum
group U(sln) via the Grothendieck group decategoriﬁcation functor K0 and the trace decategoriﬁcation
functor Tr.
Theorem 1.1 ([33, 7]) . Let /CZ be a ﬁeld of characteristic 0 and g = sln. Then there are isomorphisms
Tr(U) ∼=K0( ˙U) ⊗
/CI
/CZ
∼= ˙U.
and HH i(U) = 0 for i> 0.
Again, this result is somewhat surprising since these two decategor iﬁcation procedures need not
agree in general. We will explain that there is a large class of examples c losely connected to geometric
settings where this phenomenon is likely to occur.
Very recently a direct connection was established between catego riﬁed quantum groups and sln link
homology theories [40, 54]. Working in an enhanced foam category int roduced by Christian Blanchet,
one can realize all the foam relations in a Bar-Natan like setting as aris ing from the relations in the
categoriﬁed quantum group U(sln) via so called foamation functors ﬁrst studied in [48]. Once translat ed
through these foamation functors, the theorem above immediate ly implies that the traced and usual
Euler characteristics in the sln link homology theories coincide.
Corollary 1.2. In sln link homology theories, traced and usual Euler characteristics do c oincide.
6 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LA UDA
1.6.2. Trace and K0 of U ∗. By allowing homogeneous, but not necessarily grading preserving 2-
morphisms in U(g) we can deﬁne a version of the 2-category with larger 2-hom space s. Let U ∗(g)
denote the 2-category with the same objects and one morphisms a s U(g), but with 2-hom spaces
between one morphisms X1λ and Y 1λ given by
U ∗(g)(X1λ,Y 1λ) :=
⨁
t∈ /CI
U(g)(X1λ,Y 1λ⟨t⟩).
One can alternatively think of U ∗ as the result of adding isomorphisms X1λ →X1λ⟨t⟩ for all t ∈ /CI .
This essentially kills the grading making Grothendieck ring K0(U ∗) only a /CI -module, rather than a
/CI [q,q −1]-module. While this version of the 2-category is less interesting from a K0 perspective, it has
interesting consequences for the trace.
The trace of the graded version U ∗ of the categoriﬁed quantum sl2 is isomorphic to the idempotent
form of the current algebra U(sl2[t]) := U(sl2 ⊗ /C9 [t]) [8]. In [8] it is also shown that for the integral
version U
/CI
(sl2) ( /CZ is replaced by /CI in the deﬁnition), we have
Tr(U
/CI
) = K0( ˙U
/CI
) = K0( ˙U).
It is interesting that one loses the q by considering the graded category U ∗, but one sees the positive
part of the loop algebra sl2 ⊗ /C9 [t,t −1] appear.
We expect that these results generalize to ﬁnite type simply-laced K ac-Moody algebras g. However,
to ease the exposition in this article, we set g = sln and describe evidence for the following conjecture
in section 5.2.
Conjecture 1. For g = sln, we have
K0( ˙U
/CI
) = Tr(U
/CI
) = K0( ˙U )
and Tr(U ∗
/CI
) coincides with the integral idempotented version of the current a lgebra U(sln[t]) deﬁned
in Section 5.2.
In this paper we construct a homomorphism U(sln[t]) → Tr(U ∗(sln)) utilizing the graphical calculus
and verifying relations directly (see Proposition 23). This implies that the center of objects Z( ˙U ) :=⨁
λ∈X End ˙U (1λ) of ˙U (see section 6 for more details) is a module over the current algebra U(sln[t]).
An immediate consequence of this result is the following theorem.
Theorem 1.3. Any 2-representation U(sln) → K gives rise to an action of the current algebra U(sln[t])
on Tr(K) and the center Z(K) of objects in K.
This theorem is proven in Section 6. Let us discuss one implication of th is result. Brundan made the
surprising discovery that one could deﬁne an action of the Lie algebr a ˆg := gl∞(C) on the center Z(O) =⨁
νZ(Oν) of all integral blocks Oν of category O [12]. In this action, the Chevalley generators of ˆg
act as certain trace maps associated to canonical adjunction map s between special translation functors
that arise from tensoring with a g-module and its dual. In [15] it is explained that this action is closely
connected to Ginzburg’s geometric construction of representat ions of the general linear group [25].
Theorem 1.3 provides a context for understanding this surprising a ction by traces on category O.
Indeed, Brundan’s action is part of a broad phenomenon that occu rs within the context of higher
representation theory: any categoriﬁed representation of the quantum group Uq(sln) immediately gives
rise to an action of U(sln[t]) on the center of objects in the 2-representation via categorica l traces.
In particular, an action of ˙U(sln) on graded category O would automatically imply and generalize
Brundan’s result. More details about this action will be given in [7].
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 7
1.6.3. Organization of this paper. This paper is organized as follows. After recalling the diagrammatics
for the trace in pivotal categories, taking as example V ect
/CZ
, we deﬁne the trace functor for linear and
additive 1- and 2-categories and study its properties. In Section 3 we recall the notion of (strongly)
upper-triangular category from [8], which is particularly convenient for computing all Hochschild–
Mitchell homology groups. In the next sections diﬀerent versions o f the categoriﬁed quantum sln are
deﬁned and their decategoriﬁcations by means of K0 and Tr are compared. The last chapter is devoted
to the proof of Theorem 1.3.
To make this paper more accessible for graduate students, each s ection is supplied with many
examples, exercises, pictures and references to textbooks. Pla ces where special knowledge is required
are marked and can be ignored in the ﬁrst reading.
Acknowledgments: A.B. and Z.G. were supported by Swiss National Science Foundation u nder
Grant PDFMP2-141752/1. K.H. was partially supported by JSPS Gra nt-in-Aid for Scientiﬁc Research
(C) 24540077. A.D.L was partially supported by NSF grant DMS-1255 334 and by the John Templeton
Foundation. A.D.L is extremely grateful to Mikhail Khovanov for sha ring his insights and vision about
higher representation theory. Some of the ideas and calculations a ppearing in this article were done as
part of this collaboration. He is also grateful to Arun Ram for helpfu l decategoriﬁcation discussions.
A.B. would like to thank Benjamin Cooper for helpful conversations.
