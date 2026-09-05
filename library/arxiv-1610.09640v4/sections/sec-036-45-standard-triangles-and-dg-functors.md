---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-036-45-standard-triangles-and-dg-functors
section_title: "Standard Triangles and DG Functors"
section_number: 4.5
pages: 85-87
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
standard triangle associated to a strict morphism; and in Subsection 3.5 we deﬁned
DG functors. Now we show how these notions interact with each other. As before,
we consider abelian categoriesM and N, and DG ringsA and B.
Let F : C(A, M)→C(B, N) be a DG functor. Given a morphismφ:M0→M1
in Cstr(A, M), we have a morphismF (φ) : F (M0)→F (M1) in Cstr(B, N), and
objects F (ConeA,M(φ)) and ConeB,N(F (φ)) in C(B, N). By deﬁnition, and using
the fully faithful graded functorUnd from Proposition 3.8.18, there is a canonical
isomorphism
(4.5.1) ConeA,M(φ)∼=M1⊕TA,M(M0)
in Gstr(A, M). SinceF is a linear functor, it commutes with ﬁnite direct sums, and
therefore there is a canonical isomorphism
(4.5.2) F (ConeA,M(φ))∼=F (M1)⊕F (TA,M(M0))
in Gstr(A, M). And by deﬁnition there is a canonical isomorphism
(4.5.3) ConeB,N(F (φ))∼=F (M1)⊕TB,N(F (M0))
in Gstr(A, M). Warning: the isomorphisms (4.5.1), (4.5.2) and (4.5.3) might not
commute with the diﬀerentials. The diﬀerentials on the right sides are diagonal
matrices, but on the left sides they are upper-triangular matrices (see Deﬁnition
4.2.1).
Lemma 4.5.4. LetF,G : G(A, M)→G(B, N) be graded functors, and letη:F→
G be a degreej morphism of graded functors. SupposeM∼=M0⊕M1 in Gstr(A, M),
with embeddingsei :Mi→M and projectionspi :M→Mi. Then
ηM =
(
G(e0),G (e1)
{
◦(ηM0,ηM1)◦
(
F (p0),F (p1)
{
,
as degreej morphisms F (M)→G(M) in G(B, N).
85
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The lemma says that the diagram
F (M)
(F(p0),F(p1)) //
ηM

F (M0)⊕F (M1)
(ηM0,ηM1)

G(M) G(M0)⊕G(M1)
(G(e0),G(e1))oo
in G(B, N) is commutative.
Proof. It suﬃces to prove that the diagram below is commutative fori = 0, 1 :
F (Mi)
F(ei) //
ηMi

id

F (M)
F(pi) //
ηM

F (Mi)
ηMi

G(Mi)
G(ei) //
id
CCG(M)
G(pi) //G(Mi)
This is true becauseηis a morphism of functors (a natural transformation). □
Theorem 4.5.5. Let F : C(A, M)→C(B, N) be a DG functor, and letφ:M0→
M1 be a morphism inCstr(A, M). Deﬁne the isomorphism
cone(F,φ) :F (ConeA,M(φ))
≃
− →ConeB,N(F (φ))
in Gstr(A, M) to be
cone(F,φ) :=
(
idF(M1),τF,M0
{
.
Then:
(1) The isomorphism cone(F,φ) commutes with the diﬀerentials, so it is an
isomorphism in Cstr(A, M).
(2) The diagram
F (M0)
F(φ) //
id

F (M1)
F(eφ) //
id

F (ConeA,M(φ))
F(pφ) //
cone(F,φ)

F (TA,M(M0))
τF,M0

F (M0)
F(φ) //F (M1)
eF(φ)
// ConeB,N(F (φ))
pF(φ)
// TB,N(F (M0))
in Cstr(B, N) is commutative.
When deﬁningcone(F,φ) above, we are using the decompositions (4.5.2) and
(4.5.3) in the categoryGstr(A, M), and the isomorphismτF,M0 from Deﬁnition 4.4.1.
The slogan summarizing this theorem is “A DG functor sends standard triangles
to standard triangles”.
Proof.
(1) To save space let us writeθ:= cone(F,φ). We have to prove thatdB,N(θ) = 0.
Let’s writeP := ConeA,M(φ) andQ := ConeB,N(F (φ)). Recall thatdB,N(θ) = dQ◦
θ−θ◦dF(P). We have to prove that this is the zero element inHomB,N
(
F (P ),Q
{1
.
Writing the cones as column modules:
P =
 M1
TA,M(M0)

and Q =
 F (M1)
TB,N(F (M0))

,
86
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the matrices representing the morphisms in question are
θ=
idF(M1) 0
0 τF,M0

, dP =
dM1 φ◦t−1
M0
0 d TA,M(M0)

and
dQ =
dF(M1) F (φ)◦t−1
F(M0)
0 d TB,N(F(M0))

.
Let us write γ:= γF for simplicity. According to Theorem 4.3.2, the gauge
γ: F→F is a degree 1 morphism of DG functorsC(A, M)→C(B, N). Because
the decomposition (4.5.1) is in the categoryGstr(A, M), Lemma 4.5.4 tells us that
γP decomposes too, i.e.
γP =
γM1 0
0 γTA,M(M0)

.
By deﬁnition ofγP we havedF(P) =F (dP ) +γP in HomB,N
(
F (P ),F (P )
{1
. It
follows that
dF(P) =F (dP ) +γP
=
F (dM1) F (φ◦t−1
M0)
0 F (dTA,M(M0))

+
γM1 0
0 γTA,M(M0)

=
F (dM1) +γM1 F (φ◦t−1
M0)
0 F (dTA,M(M0)) +γTA,M(M0)

=
dF(M1) F (φ◦t−1
M0)
0 d F(TA,M(M0))

.
Finally we will check thatθ◦dF(P) and dQ◦θare equal as matrices of morphisms.
We do that in each matrix entry separately. The two left entries in the matrices
θ◦dF(P) and dQ◦θagree trivially. The bottom right entries in these matrices
are τF,M0◦dF(TA,M(M0)) and dTB,N(F(M0))◦τF,M0 respectively; they are equal by
Proposition 4.4.2. And in the top right entries we haveF (φ◦t−1
M0) and F (φ)◦
t−1
F(M0)◦τF,M0 respectively. NowF (φ◦t−1
M0) =F (φ)◦F (t−1
M0); so it suﬃces to prove
that F (t−1
M0) = t−1
F(M0)◦τF,M0. This is immediate from the deﬁnition ofτF,M0.
(2) By deﬁnition ofθ= cone(F,φ), the diagram is commutative inGstr(A, M). But
by part (1) we know that all morphisms in it commute with the diﬀerentials, so
they lie inCstr(B, N). And the functorUnd from Proposition 3.8.18 is faithful.□
Corollary 4.5.6. In the situation of Theorem4.5.5, the diagram
F (M0)
F(φ) //
id

F (M1)
F(eφ) //
id

F (ConeA,M(φ))
τF,M0◦F(pφ) //
cone(F,φ)

TB,N(F (M0))
id

F (M0)
F(φ) //F (M1)
eF(φ)
// ConeB,N(F (φ))
pF(φ)
// TB,N(F (M0))
is an isomorphism of triangles inCstr(B, N).
Proof. Just rearrange the diagram in item (2) of the theorem. □
