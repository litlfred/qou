---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-021-43-f-is-essentially-surjective
section_title: "F is essentially surjective"
section_number: 4.3
pages: 25-29
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
In order to conclude that F establishes an equivalence B
⊗∼= Z1(C) of tensor categories it
remains to prove that F is essentially surjective, viz. that for every object Y of B there
is ( X, eX ) ∈ Z 1(C) such that F (X, eX ) ∼= Y . We begin with a result due to Izumi [19].
Lemma 4.8 Let Y ∈ C be simple. Then the 1-morphisms (Y ⊠ 1)J, (1 ⊠ Y op)J : B → A
and J(Y ⊠ 1), J(1 ⊠ Y op) : A → B are simple. Furthermore,
(Y ⊠ 1)J ∼= (1 ⊠ Y
op
)J,
J(Y ⊠ 1) ∼= J(1 ⊠ Y
op
).
Proof. Let Y, Z ∈ C . By duality be have the isomorphism
HomE ((Y ⊠ 1)J, (Z ⊠ 1)J) ∼= HomE ((Y ⊠ 1)JJ , Z ⊠ 1) = Hom A((Y ⊠ 1)Q, Z ⊠ 1)
of vector spaces. In view of Q ∼=
⨁
i Xi ⊠ X op
i this implies
HomE ((Y ⊠ 1)J, (Z ⊠ 1)J) ∼= HomC(Y, Z).
In particular, if Y ∈ C is simple then (Y ⊠1)J ∈ HomE (B, A) is simple, and so is ( 1⊠Y op)J
by a similar argument. Furthermore,
HomE ((Y ⊠ 1)J, (1 ⊠ Y
op
)J) ∼= HomE (Y ⊠ Y op, JJ ) = Hom A(Y ⊠ Y op, Q).
Now, Y ⊠ Y op is simple and contained in Q with multiplicity one, thus these spaces are
one dimensional and
(Y ⊠ 1)J ∼= (1 ⊠ Y
op
)J.
Similar arguments apply to the A − B-morphisms. ■
Corollary 4.9 Let X, Y ∈ C . Then there is Z ∈ C such that
J(X ⊠ Y op)J ∼= J(Z ⊠ 1)J
and such that the isomorphisms
e ∈ HomE (J (X ⊠ Y op)J, J(Z ⊠ 1)J) ≡ HomA((X ⊠ Y op)Q, Q(Z ⊠ 1)),
f ∈ HomE (J (Z ⊠ 1)J, J (X ⊠ Y op)J) ≡ HomA((Z ⊠ 1)Q, Q(X ⊠ Y op))
25
can be chosen such that
e = v ⊗ ˜e, f = v ⊗ ˜f
with ˜e ∈ HomA((X ⊠ Y op)Q, Z ⊠ 1) and ˜f ∈ HomA((Z ⊠ 1)Q, X ⊠ Y op). (Alternatively,
one can ﬁnd morphisms of the form e = ˜e ⊗ v′, f = ˜f ⊗ v′.)
Proof. Using the lemma we compute
J(X ⊠ Y op)J = J(X ⊠ 1)(1 ⊠ Y op)J ∼= J(X ⊠ 1)(Y ⊠ 1)J = J(XY ⊠ 1)J.
We put Z = XY and denote by ˆe the isomorphism ( 1 ⊠ Y op)J → (Y ⊠ 1)J provided by
the preceding lemma. Now the claim follows with ˜ e = id X⊠1 × ˆe if we keep in mind that
tensoring ˜e with idJ (in E) amounts to tensoring with v in A, as follows from the deﬁnition
of E. ˜f is deﬁned similarly. Alternatively, using the isomorphism J(X ⊠ 1) ∼= J(1 ⊠ X
op
)
one obtains a solution with e = ˜e ⊗ v′ etc. ■
The lemma implies that every object of B is isomorphic to one of the form ( J (X ⊗
1)J, pX ). This looks quite promising since also F (X, eX ) has this form. In fact, by Lemma
4.3 and Lemma 3.3 we obtain a family of morphisms {eX (Y ) : XY → Y X, Y ∈ C}
natural w.r.t. Y . Yet, in order to conclude that this is a half braiding (and th erefore
(J (X⊗1)J, p) = F (X, eX )) we need that p satisﬁes (4.10) and p[0] = id X. Not every object
of B satisﬁes these conditions as is exempliﬁed, e.g., the objec t J(X ⊠1)J = (J (X ⊠1)J, p)
where
p = id J(X⊠1)J = v ⊗ idX⊠1 ⊗ v′ ∈ HomA((X ⊠ 1)Q, Q(X ⊠ 1)).
One easily veriﬁes that p does not satisfy (4.10). In view of p[i] = δi0idX it is also clear
that the corresponding eX (Y ) fails to be invertible for all Y .
The following result on the 2-category E is quite general in that it does not rely on
A = C ⊠ Cop.
Lemma 4.10 Let X ∈ A and p = p • p ∈ EndE (J XJ). Then there is Y ∈ A, q = q • q ∈
EndE (J Y J) such that (J Y J, q) ∼= (J XJ, p) and in addition
Q Q Y
✡ ✠
q
Y Q
= λ
Q Q Y
q
q
✡ ✠
Y Q
(4.15)
Remark 4.11 The condition (4.15) implies q • q = q as is seen by multiplication with
w′ ⊗ idY from the left. ✷
26
Proof. Using the (non-strict) unit B − B morphism 1B = ( J J, λ−1idQ) we put ( Y, q) =
1B (X, p) = ( QX, λ−1idQ × p). The isomorphism ( J Y J, q) ∼= (J XJ, p) was proven in [38,
Theorem 3.12]. We claim that q satisﬁes (4.15). In terms of ( Y, q) (and keeping in mind
that Y = QX !) the left hand side of (4.15) is given by
λ−1
✡ ✠
☛ ✟
p
✡ ✠
Q X Q
For the right hand side we compute
λ · λ−2
☛ ✟
p
✡ ✠
☛ ✟
p
✡ ✠
✡ ✠
Q X Q
= λ−1
✚ ✙
✛ ✘
☛ ✟
p
p
✡ ✠
✡ ✠
Q X Q
= λ−1
✡ ✠
☛ ✟
p
✡ ✠
Q X Q
In the last step we have used p • p = p. That the result coincides with the left hand side
follows now from a standard computation using the propertie s of a Frobenius algebra. ■
Proposition 4.12 Every object of B is isomorphic to one of the form (J (Z ⊠ 1)J, q)
where q ∈ EndB(J (Z ⊠ 1)J) satisﬁes (4.15) (with Y = Z ⊠ 1).
Proof. By the preceding lemma every object ( J(X ⊠ Y op)J, p) of B is isomorphic to
one which satisﬁes (4.15), which allows us to assume this pro perty in the rest of the
proof. By Corollary 4.9 there is Z ∈ C such that J(X ⊠ Y op)J ∼= J (Z ⊠ 1)J. Let
e : J (X ⊠ Y op)J → J (Z ⊠ 1)J, f : J (Z ⊠ 1)J → J(X ⊠ Y op)J be a pair of mutually
inverse isomorphisms. Then with q = e • p • f we have ( J(Z ⊠ 1)J, q) ∼= (J (X ⊠ Y op)J, p).
If we can show that also q satisﬁes (4.15) Lemma 4.4 applies and the claim follows. Now
by Corollary 4.9 Z, e, f can be chosen such that e = v ⊗ ˜e, f = v ⊗ ˜f , where ˜e, ˜f are
27
mutually inverse 2-morphisms between ( X ⊗ Y )J and ( Z ⊗ 1)J. Therefore,
q = e • p • f =
Q Z
✁
✁
✁❆
❆
❆
e
X
p
X
f
❆
❆
❆
✁
✁
✁
Z Q
=
Q Z
˜e
X
p
X
˜f
❆
❆
❆
✁
✁
✁
Z Q
where the four-fold vertices denote triple (co)products. T hat q satisﬁes (4.15) is now
obvious from the respective property of p and ˜f • ˜e = id. ■
Proposition 4.13 The preceding proposition remains true if one adds the requir ement
that q[0] = λ−1idZ (notation of Lemma 4.3).
Proof. Let Z, q be as in the preceding proposition. Multiplying (4.15) with v′ ⊗ v′ ⊗ idZ⊠1
and using v′ ⊗ idZ⊠1 ◦ q = q[0] ⊗ v we obtain λq[0]2 = q[0] ∈ EndC(Z). Let f : ˜Z → Z, g :
Z → ˜Z be a splitting of the idempotent λq[0]. Then it is easy to verify that with
˜q = id Q ⊗ (g ⊠ id1) ◦ q ◦ (f ⊠ id1) ⊗ idQ
we have ( J ( ˜Z ⊠ 1)J, ˜q) ∼= (J (Z ⊠ 1)J, q). This ˜ q still veriﬁes (4.15) and, in addition,
˜q[0] = λ−1id ˜Z . ■
Now we are ready to state our ﬁrst main result.
Theorem 4.14 The tensor categories B and Z1(C) are equivalent as spherical categories,
thus we have the weak monoidal Morita equivalence (in the sen se of [38]) Z1(C) ≈ C ⊠ Cop.
In particular,
dim Z1(C) = (dim C)2.
Proof. We have shown that every simple object in B isomorphic to the image under F
of a simple object in Z1(C). Since Z1(C) and B are both semisimple (in particular closed
under direct sums and subobjects) we conclude that F is essentially surjective. Since F is
also fully faithful we have an equivalence of categories by [ 35, Theorem IV.4.1]. F being
monoidal we have an equivalence of monoidal categories by [5 1, I.4.4]. (This already
implies that B and Z1(C) have the same dimension, since by [38, Proposition 2.4] the
latter are well-deﬁned independently of the chosen spheric al or ∗-structure and, of course,
invariant under monoidal equivalence.)
28
eX (Xi) =
ε(X) Xi X
✬ ✩
☛ ✟
eX(Xı)
✡ ✠
✫ ✪
X X i ε(X)
peX =
ε(X ⊠ 1) Q X ⊠ 1
✬ ✩
r′☛ ✟
peX
✡ ✠r
✫ ✪
X ⊠ 1 Q ε (X ⊠ 1)
Figure 1: eX (Xi) and peX
It remains to show that the spherical structures are compati ble. As to the conjugation
maps, we have
F (X, eX ) = (J(X ⊠ 1)J, peX ) = ( J (X ⊠ 1)J, peX ),
F ((X, eX )) = F ((X, eX )) = ( J(X ⊠ 1)J, peX ).
Putting together Proposition 3.9 and Lemma 3.2, eX(Xi) is as in Fig. 1, where the pair of
unlabeled morphisms is any solution of the duality equation s. In view of the deﬁnition of
pX in Proposition 4.5 and of peX in [38, Theorem 5.14], cf. Fig. 1, it is clear that peX = peX
and therefore
F (X, eX ) = F ((X, eX )).
Now by Proposition 3.9, the spherical structure of Z1(C) is inherited from C, concretely
εZ1(C)(X, eX ) = εC(X). Considering how the spherical structures of E0 and E arise from
that of A in [38, Theorem 5.13] it is essentially obvious that F : Z1(C) → B is an
equivalence of spherical categories irrespective of the fa ct that the latter is neither strict
monoidal nor strict spherical. We omit the easy details. ■
Remark 4.15 1. In the case where C is the representation category of a ﬁnite dimensional
involutive semisimple and cosemisimple Hopf algebra H, Z1(C) is equivalent [22, Theorem
XIII.5.1] to the representation category of the quantum dou ble D(H) and our result is
just the fact dim D(H) = (dim H)2.
