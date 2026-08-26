---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-033-53-computation-of-the-gauss-sums
section_title: "Computation of the Gauss sums"
section_number: 5.3
pages: 39-41
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
If C is a braided spherical tensor category a theorem of Deligne, cf. [56, Proposition 2.11],
implies that Z1(C) is a ribbon category (or balanced). Namely,
θX =
ε(X) X
☛ ✟
X
❆❆
✁
✁
✁
❆❆
✡ ✠
ε(X) X
for X ∈ C
deﬁnes a natural automorphism {θX, X ∈ Obj C} of the identity functor which satisﬁes
θXY = θX ⊗ θY ◦ c(Y, X) ◦ c(X, Y ) ∀X, Y,
θX = θX, ∀X.
(A similar results hold for ∗-categories, cf. [31].) For the simple objects we have θX =
ωXidX with ωX ∈ F∗.
The quantum double Z1(C) is braided and by the arguments in Section 3 we know
that it has a spherical structure which is induced by the one o n C. We will show that
the numbers ω(X,eX ) can be computed in terms of the tube algebra and will compute t he
Gauss sum
∆ ±(Z1(C)) =
∑
(X,eX )
ω±1
(X,eX )d(X, eX )2,
which plays an important role in the construction of topolog ical invariants.
Following [19] we consider the element t ∈ Ξ L deﬁned by
t[i, j, k] = λ
di
δikδijidX 2
i
. (5.8)
It will turn out that t is in the center of Ξ L.
Lemma 5.17 For simple (X, ex) ∈ Z 1(C) we have
tz(X,eX ) = ω−1
(X,eX )z(X,eX ).
39
Proof. From (5.2), (5.4) and (5.8) we obtain
(tz(X,eX ))[i, j, k] = δik
λ
di
d(X)
λdi
∑
m∈Γ
N j
mi∑
α=1
N X
i∑
β=1
dmdi
djλ
Xj Xi
t′jα
mi ☛ ✟
Xm Xi
✎
✍
☞
✌
p′β
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
pβ
i
Xm
✡ ✠tjα
mi
Xi Xj
= δik
d(X)
λdi
∑
m∈Γ
N j
mi∑
α=1
N X
i∑
β=1
Xj ε(Xi) Xi
☛ ✟
smα
jı ✡ ✠
❆❆
✎
✍
☞
✌
p′β
i
X
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌pβ
i
❆❆
m
☛ ✟
✡ ✠ε(Xi)
Xi Xj
= δik
d(X)
λdi
N X
i∑
β=1
Xj ε(Xi) Xi
☛ ✟
✎
✍
☞
✌
p′β
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
❆❆
✡ ✠
ε(Xi)
✎
✍
☞
✌
pβ
i
Xi Xj
Now the claim is a consequence of the following computation
Xi
☛ ✟
✎
✍
☞
✌p′β
i
❆❆
✁
✁
✁
❆❆
✡ ✠
X
=
Xi
☛ ✟
✎
✍
☞
✌pβ
i
❆❆
✁
✁
✁
❆❆
✡ ✠
X
=
Xi
☛ ✟
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌
pβ
i
✡ ✠
X
=
Xi✎
✍
☞
✌
p′β
i
☛ ✟
❆❆
✁
✁
✁
❆❆
✡ ✠
X
=
Xi✎
✍
☞
✌
p′β
i
☛ ✟
❆
❆
❆ ✁✁
✁✁
✡ ✠
X
= ω−1
(X,eX ) p′β
i ,
which is justiﬁed by the same arguments as in the proof of Lemm a 5.9. Here we used
standard properties of the spherical structure in the ﬁrst a nd third equalities and natu-
rality of the half braiding eX(·) w.r.t. the second argument in the second equality. The
rest follows since ( X, eX ) is simple. ■
Proposition 5.18 We have
∆ ±(Z1(C)) = dim C.
40
Proof. In view of ∑ z(X,eX ) = 1Ξ L the lemma implies
t =
∑
(X,eX )
ω−1
(X,eX )z(X,eX ),
which proves that t is central in Ξ L. To this equation we apply the linear form φ ∈ Ξ ∗
L
φ(x) = λ
∑
i∈Γ
di trXi(x[i, 0, i]).
One one hand by (5.8) we clearly have φ(t) = λ2. On the other hand with (5.4) we
compute
φ(z(X,eX )) = d(X)
∑
i∈Γ
trXi


N X
i∑
α=1
p′α
i ◦ pα
i

 = d(X)
∑
i∈Γ
diN X
i = d(X)2.
Putting everything together we obtain ∆ −(Z1(C)) = λ2 = dim C. The equality for ∆ +
follows from dim Z1(C) = (dim C)2 and the fact ∆ +(M)∆ −(M) = dim M, which holds
for every modular category M [53, 48]. ■
This completes the proof of Theorem 1.2.
Remark 5.19 1. A modular category satisfying ∆ +(C) = ∆ −(C) gives rise to an anomaly-
free surgery TQFT, cf. [53]. Thus for quantum doubles the con struction of the associated
TQFTs simpliﬁes considerably.
