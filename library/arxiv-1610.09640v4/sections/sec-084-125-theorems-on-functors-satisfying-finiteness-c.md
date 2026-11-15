---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-084-125-theorems-on-functors-satisfying-finiteness-c
section_title: "Theorems on Functors Satisfying Finiteness Conditions"
section_number: 12.5
pages: 231-235
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
12.5. Theorems on Functors Satisfying Finiteness Conditions. In this sub-
section we apply the deﬁnitions from the previous subsection (on cohomological
dimensions of functors), combined with noetherian conditions, to prove Theorems
12.5.2, 12.5.7 and 12.5.8. These results (or their analogues) were originally proved
in [62, Section II.7].
As always, there is a ﬁxed base ring K, and Convention 1.2.4 is in force.
Deﬁnition 12.5.1. Suppose A is a left noetherian ring.
(1) We denote by Mf(A) the full subcategory of M(A) = Mod A on the ﬁnitely
generated modules.
(2) We denote by Df(A) the full subcategory of D(A) = D(Mod A) on the
complexes with cohomology modules in Mf(A).
Because A is left noetherian, the category Mf(A) is a thick abelian subcategory
of M(A), and the category Df(A) is a full triangulated subcategory of D(A). When
viewed as a left module, A ∈Mf(A) ⊆Db
f (A). Note the similarity to Deﬁnition
11.4.37.
Theorem 12.5.2. Let A be a left noetherian ring, let N be an abelian category, let ⋆
be a boundedness indicator, let F, G : D⋆
f (A) →D(N) be triangulated functors, and
let ζ : F →G be a morphism of triangulated functors. Assume that the morphism
ζA : F(A) →G(A) in D(N) is an isomorphism.
(1) If ⋆= −, and if F and G have bounded above cohomological displacements,
then ζM : F(M) →G(M) is an isomorphism for every M ∈D−
f (A).
231
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) If ⋆= ⟨empty⟩, and if F and G have bounded cohomological displacements,
then ζM is an isomorphism for every M ∈Df(A).
We shall require the next lemmas for the proof of the theorem.
Lemma 12.5.3. Let D be a triangulated category, let F, G : D →D(N) be trian-
gulated functors, let ζ : F →G be a morphism of triangulated functors, and let
L
φ−→M →N
△
−−→be a distinguished triangle in D.
(1) If the morphisms ζL and ζM are both isomorphisms, then ζN is an isomor-
phism.
(2) Let j be an integer. If Hj−1(F(N)), Hj−1(G(N)), Hj(F(N)) and Hj(G(N))
are all zero, and if Hj(ζL) is an isomorphism, then Hj(ζM) is an isomor-
phism.
Proof. (1) In D(N) we get the commutative diagram
(12.5.4)
F(L)
/
ζL

F(M)
/
ζM

F(N)
/
ζN

F(L)[1]
ζL[1]

G(L)
/ G(M)
/ G(N)
/ G(L)[1]
with horizontal distinguished triangles. According to Proposition 5.3.2, ζN is an
isomorphism.
(2) Passing to cohomologies in (12.5.4) we have a commutative diagram with exact
rows
Hj−1(F(N))
/
Hj−1(ζN)

Hj(F(L))
Hj(F (φ)) /
Hj(ζL)

Hj(F(M))
/
Hj(ζM)

Hj(F(N))
Hj(ζN)

Hj−1(G(N))
/ Hj(G(L))
Hj(G(φ)) / Hj(G(M))
/ Hj(G(N))
in N. The vanishing assumption implies that Hj(F(φ)) and Hj(G(φ)) are isomor-
phisms. Hence Hj(ζM) is an isomorphism.
□
Lemma 12.5.5. Let D be a triangulated category, let F, G : D →D(N) be trian-
gulated functors, and let ζ : F →G be a a morphism of triangulated functors. The
following conditions are equivalent for M ∈D :
(i) ζM is an isomorphism.
(ii) ζM[i] is an isomorphism for every integer i.
(iii) The morphism Hj(ζM) : Hj(F(M)) →Hj(G(M)) is an isomorphism for
every integer j.
Proof. The equivalence (i) ⇔(ii) is because both F and G are triangulated func-
tors. The equivalence (i) ⇔(iii) is because the functor H : D(N) →Gstr(N) is
conservative; see Corollary 7.2.13.
□
Proof of Theorem 12.5.2.
(1) First assume P is a bounded complex of ﬁnitely generated free A-modules.
Then P is obtained from A by ﬁnitely many standard cones and translations. By
Lemmas 12.5.3(1) and 12.5.5 it follows that ζP is an isomorphism.
Next let P be a bounded above complex of ﬁnitely generated free A-modules.
Choose some integer j. Let i1 be an integer such that the integer interval [−∞, i1]
contains the cohomological displacements of F and G. Deﬁne P ′ := stt≤j−i1−2(P),
the stupid truncation of P below j −i1 −2; and let P ′′ := stt≥j−i1−1(P), the
complementary stupid truncation. See Deﬁnition 11.2.11. According to Proposition
232
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
7.3.5, the short exact sequence (11.2.12) gives a distinguished triangle P ′′ →P →
P ′
△
−→in D−
f (A). The complex P ′′ is a bounded complex of ﬁnitely generated free
A-modules, so we already know that ζP ′′ is an isomorphism. Hence Hj(ζP ′′) is
an isomorphism. On the other hand H(P ′) is concentrated in the degree interval
[−∞, j −i1 −2]. Therefore Hk(F(P ′)) = Hk(G(P ′)) = 0 for all k ≥j −1. By
Lemma 12.5.3(2), Hj(ζP ) is an isomorphism. Because j is arbitrary, Lemma 12.5.5
says that ζP is an isomorphism.
Now take an arbitrary M ∈D−
f (A). By Theorem 11.4.40 and Example 11.4.44
there is a resolution P →M, where P is a bounded above complex of ﬁnitely
generated free A-modules. Since ζP is an isomorphism, so is ζM.
(2) Now we assume that the functors F and G have ﬁnite cohomological dimensions.
Take any complex M ∈Df(A). By Lemma 12.5.5 it suﬃces to prove that Hj(ζM)
is an isomorphism for every integer j.
Let [i0, i1] be a bounded integer interval that contains the cohomological displace-
ments of the functors F and G. Deﬁne M ′′ := smt≤j−i0(M), the smart truncation
of M below j−i0; and let M ′ := smt≥j−i0+1(M), the complementary smart trunca-
tion. See Deﬁnition 7.3.6. According to Proposition 7.3.10 there is a distinguished
triangle M ′′ →M →M ′
△
−→in Df(A).
The cohomologies of these complexes
satisfy Hi(M ′′) = Hi(M) and Hi(M ′) = 0 for i ≤j −i0; and Hi(M ′′) = 0 and
Hi(M ′) = Hi(M) for i ≥j −i0 + 1. Note that M ′′ ∈D−
f (A).
By part (1) we know that ζM ′′ is an isomorphism, and therefore also Hj(ζM ′′)
is an isomorphism. The cohomology H(M ′) is concentrated in the degree inter-
val [j −i0 + 1, ∞], and therefore the cohomologies H(F(M ′)) and H(G(M ′)) are
concentrated in the interval [j + 1, ∞].
In particular the objects Hj−1(F(M ′)),
Hj−1(G(M ′)), Hj(F(M ′)) and Hj(G(M ′)) are zero. By Lemma 12.5.3(2), Hj(ζM)
is an isomorphism.
□
The triangulated structure of D(A)op was introduced in Subsection 7.6. By our
notational conventions, Df(A)op is the full subcategory of D(A)op on the complexes
with ﬁnitely generated cohomology modules, and it is triangulated, by Propositions
7.6.2 and 7.6.3.
Exercise 12.5.6. State and prove the contravariant modiﬁcation of Theorem
12.5.2. (Hint: study the proofs of Theorems 12.5.2 and 12.5.7.)
Theorem 12.5.7. Let A be a left noetherian ring, let N be an abelian category,
let N0 ⊆N be a thick abelian subcategory, let ⋆be a boundedness condition, and
let F : D⋆
f (A)op →D(N) be a triangulated functor. Assume that F(A) belongs to
DN0(N).
(1) If ⋆= −, and if F has bounded below cohomological displacement, then
F(M) belongs to DN0(N) for every M ∈D−
f (A).
(2) If ⋆= ⟨empty⟩, and if F has bounded cohomological displacement, then
F(M) belongs to DN0(N) for every M ∈Df(A).
Proof.
(1) First assume P is a bounded complex of ﬁnitely generated free A-modules.
The complex P is obtained from the free module A by ﬁnitely many extensions
and translations in Cstr(A)op. These come either from stupid truncations as in
(11.2.12) or from breaking up ﬁnite direct sums. According to Proposition 8.5.9, P
is obtained from A by ﬁnitely many standard cones and translations in D⋆
f (A)op.
Since DN0(N) is a full triangulated subcategory and F is a triangulated functor, it
follows that F(P) ∈DN0(N).
233
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Next let P be a bounded above complex of ﬁnitely generated free A-modules.
Choose some integer j. We want to prove that Hj(F(P)) ∈N0. Let i0 be an integer
such that the integer interval [i0, ∞] contains the cohomological displacement of F.
Deﬁne P ′ := stt≤−j−1+i0(P), the stupid truncation of P below −j −1 + i0; and
let P ′′ := stt≥j+i0(P), the complementary stupid truncation. These truncations
are done in the category Cstr(A). The short exact sequence (11.2.12) gives, upon
applying Op, a short exact sequence in Cstr(A)op. According to Proposition 8.5.9
there is a distinguished triangle P ′ →P →P ′′
△
−→in D−
f (A)op.
Since F is a
triangulated functor, there is a distinguished triangle F(P ′) →F(P) →F(P ′′)
△
−→
in D(N).
The complex P ′′ is a bounded complex of ﬁnitely generated free A-
modules, so we already know that F(P ′′) ∈DN0(N), and in particular Hj(F(P ′′)) ∈
N0. On the other hand H(P ′) is concentrated in the interval [−∞, −j −1 + i0].
Therefore H(F(P ′)) is concentrated in the interval [j + 1, ∞], and in particular
Hj−1(F(P ′)) = Hj(F(P ′)) = 0.
As we saw in the proof of Lemma 12.5.3(2),
Hj(F(P ′′)) →Hj(F(P)) is an isomorphism. The conclusion is that Hj(F(P)) ∈N0.
Now take an arbitrary M ∈D−
f (A). There is a quasi-isomorphism P →M,
where P is a bounded above complex of ﬁnitely generated free A-modules.
So
F(M) ∼= F(P), and thus F(M) ∈DN0(N).
(2) Now we assume that the functor F has ﬁnite cohomological dimension. Take any
complex M ∈Df(A). We want to prove that for every j ∈Z the object Hj(F(M))
lies in N0.
Let [i0, i1] be a bounded integer interval that contains the cohomological dis-
placement of the functor F. Deﬁne M ′′ := smt≤−j+1+i1(M), the smart trunca-
tion of M below −j + 1 + i1; and let M ′ := smt≥−j+2+i1(M), the complemen-
tary smart truncation. These truncations are preformed in the category Cstr(A).
By Proposition 8.5.10 there is a distinguished triangle M ′ →M →M ′′
△
−→
in Df(A)op.
Since F is a triangulated functor, there is a distinguished trian-
gle F(M ′) →F(M) →F(M ′′)
△
−→in D(N).
The cohomology of M ′ is con-
centrated in the integer interval [−j + 2 + i1, ∞], and therefore the cohomology
of F(M ′) is concentrated in the interval [−∞, j −2].
In particular the objects
Hj−1(F(M ′)) and Hj(F(M ′)) are zero. By the proof of Lemma 12.5.3(2), the mor-
phism Hj(F(M ′′)) →Hj(F(M)) is an isomorphism. But M ′′ ∈D−
f (A), so as we
proved in part (1), its cohomologies are inside N0.
□
Here is the covariant version of Theorem 12.5.7.
Theorem 12.5.8. Let A be a left noetherian ring, let N be an abelian category,
let N0 ⊆N be a thick abelian subcategory, let ⋆be a boundedness indicator, and let
F : D⋆
f (A) →D(N) be a triangulated functor. Assume that F(A) belongs to DN0(N).
(1) If ⋆= −, and if F has bounded above cohomological displacement, then
F(M) belongs to DN0(N) for every M ∈D−
f (A).
(2) If ⋆= ⟨empty⟩, and if F has bounded cohomological displacement, then
F(M) belongs to DN0(N) for every M ∈Df(A).
Exercise 12.5.9. Prove Theorem 12.5.8. (Hint: study the proofs of Theorems
12.5.2 and 12.5.7.)
Remark 12.5.10. In Theorems 12.5.2, 12.5.7 and 12.5.8 the source category is
D⋆
f (A), for a left noetherian ring A. There are variants of these theorems in which
the source category is D⋆
f (A), for a left pseudo-noetherian DG ring A; and also with
source category D⋆
M0(M) for suitable abelian categories M0 ⊆M. We leave it to the
reader to investigate these variations.
234
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
