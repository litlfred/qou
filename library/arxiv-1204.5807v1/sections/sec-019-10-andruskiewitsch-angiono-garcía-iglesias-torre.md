---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-019-10-andruskiewitsch-angiono-garcía-iglesias-torre
section_title: "ANDRUSKIEWITSCH, ANGIONO, GARCÍA IGLESIAS, TORRECILLA S, V AY"
section_number: 10
pages: 10-11
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect exampl es."
---
Step 2. V is a simple object in RepH iﬀ there exists W ∈ RepH indecom-
posable with qdimW ⁄= 0 which is isomorphic to V in RepH.
Assume that W ∈ RepH is indecomposable. If f ∈ EndH(W ), then f
is either bijective or nilpotent by the Fitting Lemma. If als o qdimW ⁄= 0 ,
then EndRep H(W ) is a ﬁnite dimensional division algebra over k, necessarily
isomorphic to k. Now, assume that V is a simple object in RepH. Let
π ∈ EndH(V ) be a lifting of idV = 1 ∈ EndRep H(V ) ≃ k. We can choose
π to be a primitive idempotent. Then the image W of π is indecomposable
andπ|W induces an isomorphism between W andV in RepH. Again by the
Fitting Lemma, EndH(W ) ≃ kπ|W ⊕ Rad EndH(W ). Hence qdimW ⁄= 0
since π is a lifting of idV ∈ EndRep H(V ).
Step 3. Let V,W ∈ RepH indecomposable with qdimV ⁄= 0, qdimW ⁄= 0,
which are isomorphic in RepH. Then V ≃W in RepH.
Letf ∈ HomH(V,W ) andg ∈ HomH(W,V ) such thatgf = id V in RepH;
that is
trV (ϑ(gf − id)ω) = 0 for every ϑ ∈ EndH(V ).(2.9)
Since V is indecomposable, gf is invertible in End(V ), or otherwise (2.9)
would fail for ϑ = id . Thus g is surjective and f is injective. But W is
also indecomposable, hence f is surjective and g is injective, and both are
isomorphisms.
To ﬁnish the proof of the statement about the irreducibles, o bserve that
an indecomposable U ∈ RepH with qdimU = 0 satisﬁes U ≃ 0 in RepH.
Since any M ∈ RepH is a direct sum of indecomposables, we see that M
is isomorphic in RepH to a direct sum of indecomposables with non-zero
quantum dimension.
Finally observe that the additive k-linear category RepH, being isomor-
phic to a direct sum of copies of Veck, is abelian. □
Here is a consequence of the Theorem: let ι :֒→W be a proper
inclusion of indecomposable H-modules with qdimV ⁄= 0 , qdimW ⁄= 0 .
Then ι ∈ J (V,W ).
Remark 2.8. From Theorem 2.7 we see the relation between the construc-
tions of [BaW1] and [GK]. For, let C = Rep H and let C0, resp. C⊥, be
the full subcategory whose objects are direct sums of indeco mposables with
quantum dimension ⁄= 0, resp. 0. Then RepH is the quotient of C by C⊥ as
described in [GK, Section 1].
Even when H is ﬁnite-dimensional, Irr RepH is not necessarily ﬁnite. It
is then natural to look at suitable subcategories of RepH that give rise to
ﬁnite tensor subcategories of RepH. A possibility is tilting modules, that
proved to be very fruitful in the case of quantum groups at roo ts of one. We
shall discuss this matter in Section 3.
FROM HOPF ALGEBRAS TO TENSOR CATEGORIES 11
2.5. Pointed or copointed pivotal Hopf algebras.
