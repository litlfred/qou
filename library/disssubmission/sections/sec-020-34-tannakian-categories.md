---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-020-34-tannakian-categories
section_title: "Tannakian categories"
section_number: 3.4
pages: 59-62
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
51
the diagram is commutative because by adjunction there exists only one
morphism j!(K)⊠j!(L) −→R(j, j)∗(K ⊠L) which restricts over U to the
identity. By the same argument, the diagram
Rj∗(K)⊠Rj∗(L)
ad∗
/ R(j, j)∗(K ⊠L)
D(j!(D(K))⊠j!(D(L)))
D(ad!)
/ D((j, j)!(D(K)⊠D(L)))
commutes. Since the lower row is an isomorphism (being the Verdier dual
of an isomorphism), it follows that ad∗is an isomorphism as well, and this
ﬁnishes the proof of part (a) of the lemma.
(b) Suppose that K ∈T, and take a generic character χ ∈Π(X). We
know from lemma 3.5 that H•
c (X,Kχ) = 0, and the K¨unneth formula in
lemma 3.4 then implies that
H•
c (X,(K ∗! M)χ) = H•
c (X,Kχ)⊗Λ H•
c (X,Mχ) = 0
as well. So K ∗! M lies in T as required. The statement for K ∗∗M follows
in the same way or can be deduced via Verdier duality.
(c) For generic χ ∈Π(X) theorem 3.1 says that H•
c (X,Kχ) ∼= H•(X,Kχ)
and that this hypercohomology is concentrated in degree zero. The same
also holds with M in place of K. So lemma 3.4 shows that H•
c (X,K ∗! M)
and H•(X,K ∗∗M) are concentrated in degree zero for generic χ, and our
claim follows from corollary 3.3.
□
3.4. Tannakian categories
In this section we assume as before that for the semiabelian variety X
and its quotient A = X/T the axiom GV(A) and hence also GV(X) from
section 3.1 holds. The results of the previous section then imply
THEOREM 3.8. The two convolution products ∗! and ∗∗descend to the
same well-deﬁned bifunctor
∗: D×D −→D
which satisﬁes P ∗P ⊂P and with respect to which both D and P become
symmetric monoidal Λ-linear triangulated categories.
Proof. By lemma 3.7 (b) both ∗! and ∗∗descend to a bifunctor on D, and
part (a) of the lemma shows that these two bifunctors coincide. It follows
as in [106, sect. 2.1] that (D,∗) is a symmetric monoidal category. Part (c)
of lemma 3.7 furthermore shows that P ∗P ⊆P so that (P,∗) inherits the
structure of a symmetric monoidal category as well.
□
52
Chapter 3 – Perverse sheaves on semiabelian varieties
It is sometimes convenient to have a lift of the quotient category P to
a category of true perverse sheaves. To obtain such a lift, consider the full
subcategory Pint ⊂P of all perverse sheaves without subquotients in S. By
the same arguments as in [41, sect. 3.7] the functor P −→P restricts to an
equivalence of categories between Pint and P, and via this equivalence the
convolution product ∗induces a bifunctor
∗int :
Pint ×Pint −→Pint
with respect to which Pint becomes a Λ-linear symmetric monoidal category
equivalent to P. The unit object 1 of Pint is the rank one skyscraper sheaf
supported in the neutral element of the group variety X.
As an application we show that the category P is rigid in the sense of
section 2.1, i.e. that we have a notion of duality which involves evaluation
and coevaluation morphisms with the properties familiar from the case of
ﬁnite-dimensional vector spaces or group representations.
THEOREM 3.9. The symmetric monoidal abelian category P is rigid.
Proof. Let P ∈Pint be a perverse sheaf without constituents in S. Via
the adjunction property in lemma 3.4 the identity morphism idP : P −→P
deﬁnes two morphisms 1 −→P∨∗∗P and P ∗! P∨−→1 in D. Under the
quotient functor D −→D these induce morphisms in the full subcategory P
by lemma 3.7. Let us denote by
coev : 1 −→P∨∗int P
and
ev : P∗int P∨−→1
the corresponding morphisms in Pint. By deﬁnition, rigidity means that for
all P ∈Pint the composite morphism
γ : P = P∗int 1
id∗int coev / P∗int P∨∗int P
ev∗int id
/ 1∗int P = P
and its counterpart (id∗int ev) ◦(coev∗int id) : P∨−→P∨are the identity
morphisms. Since the argument is the same in both cases, we will only deal
with the morphism γ in what follows.
We must show γ −idP = 0. This assertion is invariant under character
twists, so by the generic vanishing property GV(X) we can assume that for
all subquotients Q of the perverse sheaf P the hypercohomology H•(X,Q)
is concentrated in degree zero. Then H•(X,−) behaves like an exact functor
on all short exact sequences which only involve subquotients of P. After a
suitable character twist we can furthermore assume that
H•(X,P∨∗! P) = H•(X,P∨∗int P) = H•(X,P∨∗∗P)
and that the forget support morphism for these hypercohomology groups
is an isomorphism. Then for H = H•(X,P) and H∨= HomΛ(H,Λ) the
3.4. Tannakian categories
53
diagrams in [41, appendix A.5.4] show that the morphism
Λ = H•(X,1)
coev∗/ H•(X,P∨∗int P) = H•(X,P∨∗∗P) = H∨⊗Λ H
is the coevaluation in the category of vector spaces, and dually for ev. Since
the category of vector spaces of ﬁnite dimension over Λ is rigid, it follows
that on hypercohomology γ −idP induces the zero morphism. Accordingly
the perverse subquotient Q = P/ker(γ −idP) of P has H•(X,Q) = 0. By
deﬁnition of Pint it follows that Q = 0 and hence that γ −idP = 0.
□
This in particular allows to deﬁne the Tannaka groups we are interested
in, generalizing those in corollary 2.14. For P ∈P we denote by ⟨P⟩⊂P
the full subcategory of all objects which are isomorphic to subquotients of
convolution powers of P ⊕P∨. Recall that full subcategories of this form
are said to be ﬁnitely tensor generated. By construction they inherit from P
the structure of a rigid symmetric monoidal Λ-linear abelian category, and
we claim that they are neutral Tannakian in the following sense.
COROLLARY 3.10. For every P ∈P there exists an afﬁne algebraic
group G = G(P) over Λ and an equivalence
ω : ⟨P⟩
∼
−→RepΛ(G)
with the rigid symmetric monoidal Λ-linear abelian category RepΛ(G) of
ﬁnite-dimensional algebraic representations of G.
Proof. Consider P as an object of the lifted category Pint ⊂P. By
theorem 3.1 there exists a character χ ∈Π(X) such that all constituents
of all convolution powers
(P⊕P∨)χ ∗int ··· ∗int (P⊕P∨)χ
have their hypercohomology concentrated in degree zero (indeed these are
countably many conditions, and identifying Π(X)l as in [41, sect. 3.2] with
the set of Λ-valued points of the afﬁne scheme Spec(Λ ⊗Zl Zl[[t1,...,tn]])
for some n > 0 one checks that Π(X)l cannot be covered by countably many
proper closed subsets — for this one may proceed by induction on n, using
the description of ideals given in proposition A.2.2.3 of loc. cit.). For such
a character χ the functor Q 7→H0(X,Qχ) is a ﬁbre functor from ⟨P⟩to
the category of ﬁnite-dimensional vector spaces, and our corollary follows
from theorem 3.9 via the Tannakian formalism [33, th. 2.11].
□
The above ﬁbre functor depends on the chosen character twist (though
all choices lead to isomorphic Tannaka groups), and this is the reason why
we have restricted ourselves to ﬁnitely tensor generated subcategories. For
a more canonical construction one may as in [41, th. 3.7.5] take the functor
which to a perverse sheaf assigns the generic ﬁbre of its Mellin transform,
54
Chapter 3 – Perverse sheaves on semiabelian varieties
but then the ﬁbre functor is only deﬁned over a large extension ﬁeld of Λ,
and the descent to Λ again involves non-canonical choices.
REMARK 3.11. If P ∈P(X) is a semisimple perverse sheaf, then G(P)
is a reductive algebraic group, and over k = C this group coincides with the
one that has been deﬁned in corollary 2.14.
Proof. The group G(P) acts faithfully on the representation V = ω(P)
which in the case at hand is semisimple, whereas the unipotent radical of
an algebraic group acts trivially on every irreducible representation. So
the unipotent radical must be trivial, i.e. G(P) is reductive. The remaining
statement follows easily from the universal property of the localization D
together with the last statement of corollary 2.9.
□
