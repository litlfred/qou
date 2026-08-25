---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-042-34-tannakian-categories-51
section_title: "Tannakian categories 51"
section_number: 3.4
pages: 59-61
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
the diagram is commutative because by adjunction there exists only one
morphismj!(K)⊠ j!(L)−→R(j, j)∗(K⊠L) which restricts overU to the
identity. By the same argument, the diagram
R j∗(K)⊠R j∗(L)
ad∗ // R(j, j)∗(K⊠L)
D(j!(D(K))⊠ j!(D(L)))
D(ad!) // D((j, j)!(D(K)⊠D(L)))
commutes. Since the lower row is an isomorphism (being the Verdier dual
of an isomorphism), it follows thatad∗ is an isomorphism as well, and this
ﬁnishes the proof of part(a) of the lemma.
(b) Suppose thatK∈ T, and take a generic characterχ∈ Π(X). We
know from lemma 3.5 thatH•c (X,Kχ) = 0, and the K¨unneth formula in
lemma 3.4 then implies that
H•
c (X,(K∗! M)χ) = H•
c (X,Kχ)⊗ΛH•
c (X,Mχ) = 0
as well. SoK∗! M lies inT as required. The statement forK∗∗ M follows
in the same way or can be deduced via Verdier duality.
(c)For genericχ∈ Π(X) theorem 3.1 says thatH•c (X,Kχ)∼=H•(X,Kχ)
and that this hypercohomology is concentrated in degree zero. The same
also holds withM in place ofK. So lemma 3.4 shows thatH•c (X,K∗! M)
and H•(X,K∗∗ M) are concentrated in degree zero for genericχ, and our
claim follows from corollary 3.3. □
3.4. Tannakian categories
In this section we assume as before that for the semiabelian varietyX
and its quotientA = X/T the axiomGV(A) and hence alsoGV(X) from
section 3.1 holds. The results of the previous section then imply
THEOREM 3.8. The two convolution products∗! and∗∗ descend to the
same well-deﬁned bifunctor
∗ : D×D−→D
which satisﬁesP∗P⊂ P and with respect to which bothD and P become
symmetric monoidalΛ-linear triangulated categories.
Proof.By lemma 3.7(b)both∗! and∗∗ descend to a bifunctor onD, and
part (a) of the lemma shows that these two bifunctors coincide. It follows
as in [106, sect. 2.1] that(D,∗) is a symmetric monoidal category. Part(c)
of lemma 3.7 furthermore shows thatP∗P⊆ P so that (P,∗) inherits the
structure of a symmetric monoidal category as well. □
52 Chapter 3 – Perverse sheaves on semiabelian varieties
It is sometimes convenient to have a lift of the quotient categoryP to
a category of true perverse sheaves. To obtain such a lift, consider the full
subcategoryPint⊂ P of all perverse sheaves without subquotients inS. By
the same arguments as in [41, sect. 3.7] the functorP−→P restricts to an
equivalence of categories betweenPint and P, and via this equivalence the
convolution product∗ induces a bifunctor
∗int : Pint×Pint−→Pint
with respect to whichPint becomes aΛ-linear symmetric monoidal category
equivalent toP. The unit object1 of Pint is the rank one skyscraper sheaf
supported in the neutral element of the group varietyX.
As an application we show that the categoryP is rigid in the sense of
section 2.1, i.e. that we have a notion of duality which involves evaluation
and coevaluation morphisms with the properties familiar from the case of
ﬁnite-dimensional vector spaces or group representations.
THEOREM 3.9. The symmetric monoidal abelian categoryP is rigid.
Proof. Let P∈ Pint be a perverse sheaf without constituents inS. Via
the adjunction property in lemma 3.4 the identity morphismidP : P−→P
deﬁnes two morphisms1−→P∨∗∗ P and P∗! P∨−→1 in D. Under the
quotient functorD−→D these induce morphisms in the full subcategoryP
by lemma 3.7. Let us denote by
coev: 1−→P∨∗intP and ev: P∗intP∨−→1
the corresponding morphisms inPint. By deﬁnition, rigidity means that for
all P∈ Pint the composite morphism
γ : P = P∗int1
id∗intcoev// P∗intP∨∗intP
ev∗intid // 1∗intP = P
and its counterpart(id∗intev)◦ (coev∗intid) : P∨−→P∨ are the identity
morphisms. Since the argument is the same in both cases, we will only deal
with the morphismγ in what follows.
We must showγ−idP = 0. This assertion is invariant under character
twists, so by the generic vanishing propertyGV(X) we can assume that for
all subquotientsQ of the perverse sheafP the hypercohomologyH•(X,Q)
is concentrated in degree zero. ThenH•(X,−) behaves like an exact functor
on all short exact sequences which only involve subquotients ofP. After a
suitable character twist we can furthermore assume that
H•(X,P∨∗! P) = H•(X,P∨∗intP) = H•(X,P∨∗∗ P)
and that the forget support morphism for these hypercohomology groups
is an isomorphism. Then for H = H•(X,P) and H∨ = HomΛ(H,Λ) the
