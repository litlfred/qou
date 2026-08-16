---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-002-3-cqg-algebras-and-quantum-dimensions
section_title: "CQG algebras and quantum dimensions"
section_number: 3
pages: 6-10
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
The category of Compact Quantum Group algebras ( CQG ) is a full subcategory of the
category of Hopf ∗-algebras that includes the standard noncommutative deformatio ns of
algebras of representative functions on compact Lie groups. In p articular, CQG algebras
are Hopf ∗-algebras with positive deﬁnite Haar functionals which have natural analogs of
the Peter-Weyl decomposition and the Schur orthogonality relatio ns. This leads to the
notion of the quantum dimension of an irreducible, ﬁnite dimensional c omodule over a
given CQG algebra. One of the main aims of the paper is to explicitly compute quan tum
dimensions of irreducible comodules which arise in the context of (qua ntum) Grassmanni-
ans. Following [4], we recall in this section the deﬁnition of a CQG algebra and its basic
properties. We furthermore discuss the notion of a quantum Gelfa nd pair in the context
of CQG algebras (cf. [7]), and the associated quantum zonal spherical fu nctions.
Let A be a Hopf ∗-algebra with comultiplication ∆, counit ǫ and antipode S. A linear
functional h :A → C is called a normalized Haar functional if h(1) = 1 and
(
h ⊗ IdA
)(
∆(a)
)
=h(a)1A =
(
IdA ⊗h
)(
∆(a)
)
, a ∈A.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 7
A Haar functional h on A is called positive deﬁnite if h(a∗a) > 0 for all 0 ⁄= a ∈ A.
There are diﬀerent equivalent deﬁnitions of Dijkhuizen’s and Koornw inder’s [4] notion of
a CQG algebra, the following is a convenient starting point for our purpose s.
Deﬁnition 3.1. We call the Hopf ∗-algebraA a Compact Quantum Group (CQG ) algebra
if there exists a positive deﬁnite Haar functional on A.
The positive deﬁnite Haar functional on a CQG algebra A is unique. Several concrete
examples of CQG algebras (such as the algebra of representative functions on a co mpact
group, the basic commutative example) will be discussed in detail in th e following two
sections.
Let A be a CQG algebra with normalized, positive deﬁnite Haar functional h. The fol-
lowing results are all from [4]. Any ﬁnite-dimensional right A-comodule is unitarizable,
hence completely reducible. We denote Σ for the set of equivalence c lasses of ﬁnite di-
mensional, (unitary) irreducible right A-comodules. For α ∈ Σ let πα : Lα → Lα ⊗A
be a representative of the corresponding irreducible, ﬁnite dimens ional A-comodule. Let
π∗
α :L∗
α →L∗
α ⊗A be the corresponding dual right A-comodule, deﬁned by requiring
(
π∗
α(φ)
)(
v ⊗ 1A) =
(
φ ⊗S
)(
πα(v)
)
, v ∈Lα, φ ∈L∗
α,
where 1 A denotes the unit element of A. Then {L∗
α ⊗Lα |α ∈ Σ } is a complete set of
representatives of the irreducible, ﬁnite dimensional A ⊗A-comodules.
Consider A as a right A ⊗A-comodule by
R(a) =
∑
(a)
a(2) ⊗S(a(1)) ⊗a(3), a ∈A,
where we use the standard Sweedler notation for (iterated) applic ations of the comultipli-
cation. The ﬁrst key property of CQG algebras is the irreducible decomposition
A ≃
⨁
α∈Σ
L∗
α ⊗Lα
of A as right A ⊗A-comodule (the Peter-Weyl Theorem for CQG algebras). Concretely,
the isomorphism is realized by mapping φ ⊗v ∈ L∗
α ⊗Lα to (φ ⊗ IdA)(πα(v)) ∈ A. We
denote Ah for the Hilbert space completion of A with respect to the pre-Hilbert structure
⟨a,b ⟩h :=h(b∗a).
Let (π,V ) be a ﬁnite dimensional, irreducible, right A-comodule. Consider the canonical
linear isomorphism ϕ :V →V∗∗ deﬁned by ϕ(v)f :=f (v) for f ∈V∗ andv ∈V . We turn
V into a ﬁnite dimensional Hilbert space such that ( π,V ) is a unitary right A-comodule
(such scalar product is unique up to a strictly positive scalar multiple) . Since the double-
dual right A-comodule (π∗∗,V ∗∗) is equivalent to ( π,V ), there exists a unique positive
deﬁnite, linear isomorphism F =FV :V →V such that
TrV (F ) = Tr V (F−1)> 0
and such that ϕ ◦F : (π,V ) → (π∗∗,V ∗∗) is an intertwiner of right A-comodules (see [4,
Prop. 3.6]).
8 URI ONN AND JASPER V. STOKMAN
Deﬁnition 3.2. Let A be a CQG algebra, (π,V ) a ﬁnite dimensional, irreducible right
A-comodule and F :V →V the linear isomorphism as deﬁned above. Then
DimA(V ) := Tr V
(
F
)
is called the quantum dimension of the right A-comodule (π,V ).
A second key property of CQG algebras is the generalized Schur orthogonality relations
[4, Prop. 3.4 & 3.5], which we now proceed to recall.
Proposition 3.3. Let A be a CQG algebra. Let (π,V ) and (π′,V ′) be ﬁnite dimensional,
irreducible, unitary right A-comodules with associated scalar products ⟨·, ·⟩π and ⟨·, ·⟩π′.
(a) If π ⁄≃π′, then
⟨⟨π(u),v ⟩π, ⟨π′(u′),v′⟩π′⟩h = 0
for u,v ∈V and u′,v′ ∈V′.
(b) Foru1,u 2,v 1,v 2 ∈V we have
⟨⟨π(u1),v 1⟩π, ⟨π(u2),v 2⟩π⟩h = ⟨u1,u 2⟩π⟨F−1
V v2,v 1⟩π
DimA(V ) .
Let A be a CQG algebra. A quantum subgroup of A is a pair ( B,p ) with B a Hopf
∗-algebra and p :A →B a surjective Hopf ∗-algebra homomorphism. In this situation, we
write
AB = {a ∈A |
(
IdA ⊗p
)(
∆(a)
)
=a ⊗ 1B}
for the ∗-subalgebra of right B-invariant elements in A. The ∗-subalgebra AB ⊂ A is a
rightA-comodule under the right regular co-action
ρB(a) =
∑
(a)
a(2) ⊗S(a(1)), a ∈AB.
By the Peter-Weyl Theorem for A, the right A-comodule AB decomposes into irreducibles
as
(3.1) AB ≃
⨁
α∈Σ
L∗
α
DimC(LB
α ),
where for a right A-comodule (π,V ),
V B = {v ∈V |
(
1 ⊗p)
(
π(v)
)
=v ⊗ 1B}
is the space of B-invariant elements in V .
Deﬁnition 3.4. A CQG algebra A with quantum subgroup (B,p ) is called a quantum
Gelfand pair if
DimC(LB
α ) ≤ 1 ∀α ∈ Σ,
(compare with [7]).
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 9
We ﬁx a quantum Gelfand pair ( A,B ). We call a ﬁnite dimensional, irreducible A-
comodule B-spherical if it has nonzero B-invariant vectors. We denote Σ B ⊂ Σ for the
corresponding subset of equivalence classes of the B-spherical, irreducible, ﬁnite dimen-
sional right A-comodules.
In the various examples associated to (quantum) Grassmannians w hich we discuss in
the following sections, we will identify Σ B with a certain ﬁxed set of partitions. An im-
portant, but case-by-case diﬀerent, aspect is the concrete ch aracterization of the spherical
irreducibles in terms of their parameterizing set Σ B. To maintain uniform notations as
much as possible, it will therefore be convenient to denote irreducib le comodules labeled
by Σ B by new symbols {Vα | α ∈ Σ B}.
We write ⟨·, ·⟩α for a scalar product on Vα that turns Vα into a unitary right A-comodule.
Note that Σ B is invariant under ◦, were ◦ is the involution on Σ such that V∗
α ≃ Vα◦ for
all α ∈ Σ. In fact, if we ﬁx a nonzero vector vα ∈ V B
α (α ∈ Σ B), then ⟨·,v α⟩α ∈ V∗
α
B.
Combined with (3.1), we obtain the multiplicity free irreducible decompo sition
(3.2) AB =
⨁
α∈Σ B
Vα
as right A-comodules.
From the present perspective, the natural deﬁnition of the quan tum zonal spherical
functions would be
~ϕα = ⟨πα(vα),v α⟩α, ∀α ∈ Σ B,
since they form a C-basis of the ∗-algebra
BAB = {a ∈A |
(
IdA ⊗p ⊗p
)
R(a) = a ⊗ 1B ⊗ 1B}
of B-biinvariant elements in A. It turns out though that the following slightly modiﬁed
deﬁnition of the quantum zonal spherical functions is a better cho ice.
Deﬁnition 3.5. The quantum zonal spherical functions associated to the qua ntum Gelfand
pair (A,B ) are deﬁned by
ϕα = ⟨πα(vα),F
1
2
Vαvα⟩α ∈A, ∀α ∈ Σ B,
where 0 ⁄= vα ∈ V B
α and F
1
2
Vα is the square root of the positive deﬁnite linear operator FVα
on Vα.
Note that the quantum zonal spherical function ϕα (α ∈ Σ B) is uniquely determined up
to nonzero scalar multiples. The square root of the positive deﬁnite operatorFVα naturally
appears in the deﬁnition of quantum zonal spherical functions on q uantum homogeneous
spaces using Noumi’s [19] two-sided coideal approach. It is this appr oach, and its gener-
alization in terms of coideal algebras by Letzter (see [17] and refer ences therein), which
has led to the identiﬁcation of Macdonald polynomials as radial parts o f quantum zonal
spherical functions, see also Section 8 for the quantum complex Gr assmannian.
It now follows from the preceding discussions that we have the follow ing expression for
the quantum dimension of Vα in terms of the associated quantum zonal spherical function
ϕα and the associated B-invariant vector vα ∈V B
α .
10 URI ONN AND JASPER V. STOKMAN
Proposition 3.6. Let (A,B ) be a quantum Gelfand pair. For α ∈ Σ B we have
DimA
(
Vα
)
= ‖vα‖4
α
‖ϕα‖2
h
.
Proof. This follows directly using the deﬁnition of ϕα and the generalized Schur orthogo-
nality relations (Proposition 3.3b). □
