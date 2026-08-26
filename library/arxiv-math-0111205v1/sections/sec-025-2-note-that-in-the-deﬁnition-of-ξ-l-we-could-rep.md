---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-025-2-note-that-in-the-deﬁnition-of-ξ-l-we-could-rep
section_title: "Note that in the deﬁnition of Ξ L we could replace ˆYL by"
section_number: 2
pages: 31-34
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
ˆY N
L =
⨁
i∈Γ
Ni (Xi ⊠ 1)
with arbitrary {Ni} ∈ NΓ . The algebras End E (J ˆY N
L J), of which the tube algebra happens
to be the smallest, all have the same center, thus are Morita e quivalent. We emphasize
that only this common center has an invariant meaning, and in fact it has a well-known
interpretation in terms of TQFTs, see Subsection 8.2. ✷
Lemma 5.2 Let (X, eX ) ∈ Z 1(C) and Y ∈ C . Then there is a isomorphism between the
vector spaces Hom C(X, Y ) and Hom B(F (X, eX ), J(Y ⊠ 1)J).
Proof. The proof is similar to the one of Proposition 4.6, but simple r. Let s ∈ HomC(X, Y )
and let t ∈ HomB(J(X ⊠ 1)J, J (Y ⊠ 1)J) be deﬁned (using Lemma 4.3) by t[i] = δi0s.
Then the map π : s ↦→s = t • p(X,eX ) ∈ HomB(F (X, eX ), J (Y ⊠ 1)J) is injective since
(t • p(X,eX ))[i] = λ−1idXi ⊗ s ◦ eX(Xi), in particular ( t • p(X,eX ))[0] = λ−1s. Let, conversely,
s ∈ HomB(F (X, eX ), J (Y ⊠ 1)J), i.e. s = s • p(X,eX ) ∈ HomB(J(X ⊠ 1)J, J (Y ⊠ 1)J).
Then
dkλ2 · s[k] =
∑
m,l∈Γ
N k
ml∑
α=1
dmdl
Xk Y
t
′kα
m,l ☛ ✟
Xm
s[l]
❆❆
✁
✁
✁
❆❆ Xl
✡ ✠tkα
m,l
X X k
=
∑
m,l∈Γ
∑
α
dmdl
dk
dm
Xk ε(Xl) Y
☛ ✟
smα
kl
✡ ✠
s[l]
✁✁
❆❆
✁
✁
✁
❆❆Xm Xl
✁✁
s′mα
kl
☛ ✟
✡ ✠ε(Xl)
X X k
= dk
∑
m,l∈Γ
∑
α
dl
Xk Y
☛ ✟
✡ ✠
Xm s[l]
☛ ✟
❆❆
✁
✁
✁
❆❆ Xl
❆❆
✁
✁
✁
❆❆
✡ ✠
X X k
= dk
∑
l∈Γ
dl
Xk ε(Xl) Y
☛ ✟
s[l]
❆❆
✁
✁
✁
❆❆ Xl
❆❆
✁
✁
✁
❆❆
✡ ✠
ε(Xl)
X X k
31
Putting k = 0 we obtain
λ2 · s[0] =
∑
l
dl
Y☛ ✟
s[l]
❆❆
✁
✁
✁
❆❆ Xl
✡ ✠
X
and plugging this back into the preceding equation we obtain
s[k] = id Xi ⊗ s[0] ◦ eX (Xi).
Thus s is in the image of π, which proves that π is an isomorphism. ■
Proposition 5.3 Let (X, eX ) ∈ Z 1(C) be simple and let N X
i = dim HomC(Xi, X). Then
the (simple) object F (X, eX ) ∈ B is contained in J(Xi ⊠ 1)J with multiplicity N X
i . Let
{pα
i }, {p′α
i } be bases in Hom C(Xi, X), HomC(X, Xi), respectively, normalized by p′α
i ◦ pβ
i =
δαβidXi. Then qα
i ∈ HomE (F (X, eX ), J (Xi ⊠ 1)J), q′α
i ∈ HomE (J(Xi ⊠ 1)J, F(X, eX ))
deﬁned by
qα
i [k] =
( d(X)
λ2di
) 1/2
idXk ⊗ p′α
i ◦ eX (Xk),
q′α
i [k] =
( d(X)
λ2di
) 1/2
eX (Xk) ◦ pα
i ⊗ idXk
satisfy q′α
i • qβ
i = δαβ idF (X,eX ). The idempotent zi
(X,eX ) =∑ N X
i
α=1 qα
i • q′α
i in End E (J (Xi ⊠
1)J) corresponding to the isotypic component of (X, eX ) is given by
zi
(X,eX )[k] = d(X)
λdi
N X
i∑
α=1
idXk ⊗ p′
i
α ◦ eX (Xk) ◦ pα
i ⊗ idXk . (5.3)
Remark 5.4 The choice of square root of d(X) is immaterial, but it must be the same
in the equations deﬁning qα
i and q′α
i . ✷
Proof. In view of the preceding lemma all that remains to be veriﬁed i s the normalization.
Since ( X, eX ) is simple we have q′α
i • qβ
i = cαβ idF (X,eX ). Plugging qα
i [k], q′α
i [k] into (4.7)
and comparing with the middle term of the computation in Lemm a 3.10 (with Z = Xk)
we see that
(q′α
i • qβ
i )[k] = d(X)
λdi
idXk ⊗ EX,X (pα
i ◦ p′β
i ) ◦ eX(Xk)
= trX ◦ EX,X (pα
i ◦ p′β
i )
λdi
eX (Xk),
32
since EX,X (pα
i ◦ p′β
i ) is a scalar multiple of id X due to the simplicity of ( X, eX ). Now,
by deﬁnition of the functor F we have id F (X,eX )[k] = λ−1eX (Xk), thus by comparison we
ﬁnd cαβ = d−1
i trX ◦ EX,X (pα
i ◦ p′β
i ). Computing
trX ◦ EX,X (pα
i ◦ p′β
i ) = trX (pα
i ◦ p′β
i ) = trXi(p′α
i ◦ pβ
i ) = diδαβ,
where we used the invariance of the trace under the condition al expectation and cyclic
permutations, we obtain cαβ = δαβ as claimed.
Now we can compute zi
(X,eX ) =∑
α qα
i • q′α
i as follows:
zi
(X,eX )[k] = d(X)
λ2di
N X
i∑
α=1
∑
l,m∈Γ
N k
lm∑
β=1
dldm
λdk
Xk Xi
t′k,β
l,m ☛ ✟
Xl Xm
✎
✍
☞
✌
p′α
i
❆❆
✁
✁
✁
❆❆
X
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌
pα
i
Xl Xm
✡ ✠tk,β
l,m
Xi Xk
= d(X)
λdi
N X
i∑
α=1
Xk Xi
✎
✍
☞
✌
p′α
i
X
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌
pα
i
Xi Xk
We have pulled t′kβ
lm through the braiding and used (4.6). ■
Proposition 5.5 Let (X, eX ) ∈ Z 1(C) be simple. The minimal central idempotent z(X,eX )
in Ξ L corresponding to F (X, eX ) is given by
z(X,eX )[i, j, k] = δik
d(X)
λdi
N X
i∑
α=1
idXj ⊗ p′
i
α ◦ eX (Xj) ◦ pα
i ⊗ idXj , (5.4)
where the {pα
i }, {p′
i
α}, i ∈ Γ , α = 1, . . . , N X
i are bases as in Proposition 5.3.
Proof. Since J ˆYLJ is a direct sum ⨁
i J(Xi ⊠ 1)J we only need to add up the idempotents
in End E (J(Xi ⊠ 1)J), which we identiﬁed in Proposition 5.3, inside Ξ L = End E (J ˆYLJ).
With the isomorphism (5.1) the claimed identity follows. ■
As a ﬁrst application of the tube algebra we can give an easy bo und on the ‘size’ of
the quantum double:
Corollary 5.6 The number #Z1(C) of isomorphism classes of simple objects of Z1(C)
satisﬁes
#Z1(C) ≤
∑
i,j∈Γ
dim HomC(XiXj, XjXi).
33
Proof. By the equivalence Z1(C)
⊗
≃ B and the above considerations we have # Z1(C) =
dim Z(Ξ L). Since the center of Ξ L is spanned by the z(X,eX ) constructed above and since
z(X,eX )[i, j, k] = 0 if i ⁄= k we have
Z(Ξ L) ⊂
⨁
i,j
HomC(XiXj, XjXi),
which implies the bound. ■
Remark 5.7 If G is a ﬁnite abelian group whose order is non-zero in F then G − mod is
semisimple, symmetric and all simple objects have dimensio n one. Thus the right hand
side of the above inequality equals |G|2. In view of Z1(G − mod) ≃ D(G) − mod we have
#Z1(G − mod) = |G|2, which proves that the bound is optimal. ✷
The next two subsections, which do not pretend much original ity, will follow [19] quite
closely except for shortcuts in the proofs.
