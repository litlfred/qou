---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-072-125-theorems-on-functors-satisfying-finiteness-c
section_title: "Theorems on Functors Satisfying Finiteness Conditions"
section_number: 12.5
pages: 231-235
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
section we apply the deﬁnitions from the previous subsection (on cohomological
dimensions of functors), combined with noetherian conditions, to prove Theorems
12.5.2, 12.5.7 and 12.5.8. These results (or their analogues) were originally proved
in [62, Section II.7].
As always, there is a ﬁxed base ringK, and Convention 1.2.4 is in force.
Deﬁnition 12.5.1.Suppose A is a left noetherian ring.
(1) We denote byMf(A) the full subcategory ofM(A) = ModA on the ﬁnitely
generated modules.
(2) We denote by Df(A) the full subcategory of D(A) = D(ModA) on the
complexes with cohomology modules inMf(A).
Because A is left noetherian, the categoryMf(A) is a thick abelian subcategory
of M(A), and the categoryDf(A) is a full triangulated subcategory ofD(A). When
viewed as a left module,A∈Mf(A)⊆Db
f (A). Note the similarity to Deﬁnition
11.4.37.
Theorem 12.5.2.LetA be a left noetherian ring, letN be an abelian category, let⋆
be a boundedness indicator, letF,G : D⋆
f (A)→D(N) be triangulated functors, and
let ζ:F→G be a morphism of triangulated functors. Assume that the morphism
ζA :F (A)→G(A) in D(N) is an isomorphism.
(1) If ⋆=−, and ifF and G have bounded above cohomological displacements,
then ζM :F (M)→G(M) is an isomorphism for everyM∈D−
f (A).
231
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) If ⋆=⟨empty⟩, and ifF andG have bounded cohomological displacements,
then ζM is an isomorphism for everyM∈Df(A).
We shall require the next lemmas for the proof of the theorem.
Lemma 12.5.3. Let D be a triangulated category, letF,G : D→D(N) be trian-
gulated functors, letζ: F →G be a morphism of triangulated functors, and let
L
φ
− →M→N
∆
−−→be a distinguished triangle inD.
(1) If the morphismsζL and ζM are both isomorphisms, thenζN is an isomor-
phism.
(2) Letj be an integer. IfHj−1(F (N)), Hj−1(G(N)), Hj(F (N)) and Hj(G(N))
are all zero, and ifHj(ζL) is an isomorphism, thenHj(ζM) is an isomor-
phism.
Proof. (1) In D(N) we get the commutative diagram
(12.5.4) F (L) //
ζL

F (M) //
ζM

F (N) //
ζN

F (L)[1]
ζL[1]

G(L) //G(M) //G(N) //G(L)[1]
with horizontal distinguished triangles. According to Proposition 5.3.2,ζN is an
isomorphism.
(2) Passing to cohomologies in (12.5.4) we have a commutative diagram with exact
rows
Hj−1(F (N)) //
Hj−1(ζN)

Hj(F (L))
Hj(F(φ)) //
Hj(ζL)

Hj(F (M)) //
Hj(ζM)

Hj(F (N))
Hj(ζN)

Hj−1(G(N)) // Hj(G(L))
Hj(G(φ)) // Hj(G(M)) // Hj(G(N))
in N. The vanishing assumption implies thatHj(F (φ)) and Hj(G(φ)) are isomor-
phisms. Hence Hj(ζM) is an isomorphism. □
Lemma 12.5.5. Let D be a triangulated category, letF,G : D→D(N) be trian-
gulated functors, and letζ:F→G be a a morphism of triangulated functors. The
following conditions are equivalent forM∈D :
(i) ζM is an isomorphism.
(ii) ζM[i] is an isomorphism for every integeri.
(iii) The morphism Hj(ζM) : H j(F (M))→Hj(G(M)) is an isomorphism for
every integerj.
Proof. The equivalence (i)⇔(ii) is because bothF and G are triangulated func-
tors. The equivalence (i) ⇔(iii) is because the functor H : D(N)→Gstr(N) is
conservative; see Corollary 7.2.13. □
Proof of Theorem12.5.2.
(1) First assume P is a bounded complex of ﬁnitely generated freeA-modules.
Then P is obtained fromA by ﬁnitely many standard cones and translations. By
Lemmas 12.5.3(1) and 12.5.5 it follows thatζP is an isomorphism.
Next letP be a bounded above complex of ﬁnitely generated freeA-modules.
Choose some integerj. Leti1 be an integer such that the integer interval[−∞,i 1]
contains the cohomological displacements ofF andG. DeﬁneP′:= stt≤j−i1−2(P ),
the stupid truncation of P below j−i1−2; and let P′′:= stt≥j−i1−1(P ), the
complementary stupid truncation. See Deﬁnition 11.2.11. According to Proposition
232
Derived Categories | Amnon Yekutieli | 14 Apr 2019
7.3.5, the short exact sequence (11.2.12) gives a distinguished triangleP′′→P→
P′∆
−→in D−
f (A). The complexP′′is a bounded complex of ﬁnitely generated free
A-modules, so we already know thatζP′′is an isomorphism. Hence Hj(ζP′′) is
an isomorphism. On the other handH(P′) is concentrated in the degree interval
[−∞,j −i1−2]. Therefore Hk(F (P′)) = H k(G(P′)) = 0 for all k≥j−1. By
Lemma 12.5.3(2),Hj(ζP ) is an isomorphism. Becausej is arbitrary, Lemma 12.5.5
says thatζP is an isomorphism.
Now take an arbitraryM∈D−
f (A). By Theorem 11.4.40 and Example 11.4.44
there is a resolution P →M, where P is a bounded above complex of ﬁnitely
generated freeA-modules. SinceζP is an isomorphism, so isζM.
(2) Now we assume that the functorsF andGhave ﬁnite cohomological dimensions.
Take any complexM∈Df(A). By Lemma 12.5.5 it suﬃces to prove thatHj(ζM)
is an isomorphism for every integerj.
Let [i0,i 1]beaboundedintegerintervalthatcontainsthecohomologicaldisplace-
ments of the functorsF and G. DeﬁneM′′:= smt≤j−i0(M), the smart truncation
ofM belowj−i0; and letM′:= smt≥j−i0+1(M), the complementary smart trunca-
tion. See Deﬁnition 7.3.6. According to Proposition 7.3.10 there is a distinguished
triangle M′′→M →M′∆
−→in Df(A). The cohomologies of these complexes
satisfy Hi(M′′) = H i(M) and Hi(M′) = 0 for i≤j−i0; and Hi(M′′) = 0 and
Hi(M′) = Hi(M) for i≥j−i0 + 1. Note thatM′′∈D−
f (A).
By part (1) we know thatζM′′is an isomorphism, and therefore alsoHj(ζM′′)
is an isomorphism. The cohomology H(M′) is concentrated in the degree inter-
val [j−i0 + 1,∞], and therefore the cohomologiesH(F (M′)) and H(G(M′)) are
concentrated in the interval [j + 1,∞]. In particular the objects Hj−1(F (M′)),
Hj−1(G(M′)), Hj(F (M′)) and Hj(G(M′)) are zero. By Lemma 12.5.3(2),Hj(ζM)
is an isomorphism. □
The triangulated structure ofD(A)op was introduced in Subsection 7.6. By our
notational conventions,Df(A)op is the full subcategory ofD(A)op on the complexes
with ﬁnitely generated cohomology modules, and it is triangulated, by Propositions
7.6.2 and 7.6.3.
Exercise 12.5.6. State and prove the contravariant modiﬁcation of Theorem
12.5.2. (Hint: study the proofs of Theorems 12.5.2 and 12.5.7.)
Theorem 12.5.7. Let A be a left noetherian ring, letN be an abelian category,
let N0⊆N be a thick abelian subcategory, let⋆be a boundedness condition, and
let F : D⋆
f (A)op→D(N) be a triangulated functor. Assume thatF (A) belongs to
DN0(N).
(1) If ⋆=−, and if F has bounded below cohomological displacement, then
F (M) belongs to DN0(N) for everyM∈D−
f (A).
(2) If ⋆=⟨empty⟩, and if F has bounded cohomological displacement, then
F (M) belongs to DN0(N) for everyM∈Df(A).
Proof.
(1) First assume P is a bounded complex of ﬁnitely generated freeA-modules.
The complex P is obtained from the free moduleA by ﬁnitely many extensions
and translations in Cstr(A)op. These come either from stupid truncations as in
(11.2.12) or from breaking up ﬁnite direct sums. According to Proposition 8.5.9,P
is obtained fromA by ﬁnitely many standard cones and translations inD⋆
f (A)op.
Since DN0(N) is a full triangulated subcategory andF is a triangulated functor, it
follows thatF (P )∈DN0(N).
233
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Next letP be a bounded above complex of ﬁnitely generated freeA-modules.
Choose some integerj. We want to prove thatHj(F (P ))∈N0. Leti0 be an integer
such that the integer interval[i0,∞] contains the cohomological displacement ofF.
DeﬁneP′:= stt≤−j−1+i0(P ), the stupid truncation ofP below−j−1 +i0; and
let P′′:= stt≥j+i0(P ), the complementary stupid truncation. These truncations
are done in the categoryCstr(A). The short exact sequence (11.2.12) gives, upon
applying Op, a short exact sequence inCstr(A)op. According to Proposition 8.5.9
there is a distinguished triangleP′→P →P′′∆
−→in D−
f (A)op. Since F is a
triangulated functor, there is a distinguished triangleF (P′)→F (P )→F (P′′)
∆
−→
in D(N). The complex P′′is a bounded complex of ﬁnitely generated freeA-
modules, so we already know thatF (P′′)∈DN0(N), and in particularHj(F (P′′))∈
N0. On the other hand H(P′) is concentrated in the interval[−∞,−j−1 +i0].
Therefore H(F (P′)) is concentrated in the interval [j + 1,∞], and in particular
Hj−1(F (P′)) = H j(F (P′)) = 0 . As we saw in the proof of Lemma 12.5.3(2),
Hj(F (P′′))→Hj(F (P )) is an isomorphism. The conclusion is thatHj(F (P ))∈N0.
Now take an arbitraryM ∈D−
f (A). There is a quasi-isomorphism P →M,
where P is a bounded above complex of ﬁnitely generated freeA-modules. So
F (M)∼=F (P ), and thusF (M)∈DN0(N).
(2) Now we assume that the functorF has ﬁnite cohomological dimension. Take any
complex M∈Df(A). We want to prove that for everyj∈Z the object Hj(F (M))
lies in N0.
Let [i0,i 1] be a bounded integer interval that contains the cohomological dis-
placement of the functorF. DeﬁneM′′:= smt≤−j+1+i1(M), the smart trunca-
tion of M below−j + 1 +i1; and let M′:= smt≥−j+2+i1(M), the complemen-
tary smart truncation. These truncations are preformed in the categoryCstr(A).
By Proposition 8.5.10 there is a distinguished triangle M′→M →M′′∆
−→
in Df(A)op. Since F is a triangulated functor, there is a distinguished trian-
gle F (M′) →F (M) →F (M′′)
∆
−→in D(N). The cohomology of M′is con-
centrated in the integer interval[−j + 2 +i1,∞], and therefore the cohomology
of F (M′) is concentrated in the interval [−∞,j −2]. In particular the objects
Hj−1(F (M′)) and Hj(F (M′)) are zero. By the proof of Lemma 12.5.3(2), the mor-
phism Hj(F (M′′))→Hj(F (M)) is an isomorphism. ButM′′∈D−
f (A), so as we
proved in part (1), its cohomologies are insideN0. □
Here is the covariant version of Theorem 12.5.7.
Theorem 12.5.8. Let A be a left noetherian ring, letN be an abelian category,
let N0⊆N be a thick abelian subcategory, let⋆be a boundedness indicator, and let
F : D⋆
f (A)→D(N) be a triangulated functor. Assume thatF (A) belongs toDN0(N).
(1) If ⋆=−, and if F has bounded above cohomological displacement, then
F (M) belongs to DN0(N) for everyM∈D−
f (A).
(2) If ⋆=⟨empty⟩, and if F has bounded cohomological displacement, then
F (M) belongs to DN0(N) for everyM∈Df(A).
Exercise 12.5.9. Prove Theorem 12.5.8. (Hint: study the proofs of Theorems
12.5.2 and 12.5.7.)
Remark 12.5.10. In Theorems 12.5.2, 12.5.7 and 12.5.8 the source category is
D⋆
f (A), for a left noetherian ringA. There are variants of these theorems in which
the source category isD⋆
f (A), for a left pseudo-noetherian DG ringA; and also with
source category D⋆
M0(M) for suitable abelian categoriesM0⊆M. We leave it to the
reader to investigate these variations.
234
Derived Categories | Amnon Yekutieli | 14 Apr 2019
