---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-010-3-a-projective-outlook-on-the-funk-metric
section_title: "A projective outlook on the Funk metric"
section_number: 3
pages: 8-11
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
3.1. The projective co-nomadic Finsler structure. We start with some ter-
minology.
9
A Funk perspective on billiards, projective geometry and Mahler volume
Deﬁnition 3.1. Two Finsler structures F1, F2 on M are co-translate if F2 −F1
is a 1-form on M. A co-nomadic Finsler structure on a manifold is an equivalence
class of co-translate Finsler structures. Similarly, we deﬁne an exact co-nomadic
Finsler structure to be the equivalence class of Finsler norms up to an exact 1-form
on M.
Geometrically, a co-nomadic Finsler structure is the data of all cotangent unit
balls, ﬁxed up to translation in each cotangent space. Given a co-nomadic Finsler
structure [F], represented by a Finsler norm F, its symmetrization F S(v) :=
1
2(F(v)+F(−v)) is clearly a reversible Finsler metric that is independent of F. The
Holmes-Thompson volume element of a co-nomadic Finsler structure is similarly
well-deﬁned. Furthermore, if N ⊂M is a k-dimensional submanifold, it inherits
a co-nomadic Finsler structure, in particular its k-dimensional Holmes-Thompson
volume is well-deﬁned.
Lemma 3.2. Given an exact co-nomadic Finsler structure [F] on a manifold M,
represented by the Finsler norm F, and an oriented closed curve, its length only
depends on [F]. Moreover, the geodesics of F only depend on [F].
Proof. The ﬁrst statement is clear. For the second, recall that a geodesic is any
curve that locally extremizes the length functional of a curve with ﬁxed endpoints.
Modifying the norm by an exact 1-form simply adds a constant to the length func-
tional.
□
Take x ∈int(K), and consider the cone K∨⊂V ∗. For any non-zero ξ ∈V ∗,
set Bξ := K∨∩(x⊥+ ξ) −ξ ⊂x⊥. It is a convex body (projectively equivalent to
K∨). Furthermore, Btξ = tBξ for all t̸ = 0. Finally if ξ = ξ1 −ξ2 ∈x⊥, we get
Bξ2 = Bξ1 + ξ. Consequently, B• deﬁnes a convex set in (V ∗/x⊥)∗⊗x⊥= T ∗
xP, up
to translation. Let us call it the projective co-nomadic Finsler structure on int(K).
To obtain a true Finsler structure, one can proceed in several ways.
i) Fix a Euclidean structure on V . One can then take ξ = x⊥and obtain the
ﬁxed cotangent ball K∨∩(x⊥+ x) −x ⊂T ∗
xP = TxP = x⊥. We call it the
orthogonal Finsler structure.
ii) Fix η ∈int(K∨), and take B∗
xK := K∨∩(x⊥+η0)−η0 for any η0 ∈η ⊂V ∗.
As we will see, this is simply the reverse Funk metric, see Proposition 3.4.
iii) Fix an aﬃne-equivariant point selector S in the interior of convex bodies
(which need only be deﬁned on projective images of K∨), such as the center
of mass or Santal´o point. We then get a projectively invariant construction
of a Finsler metric on int(K) which is co-translate to the reverse Funk
metric.
Given an extra input α from the above list, we will say that the projective co-
nomadic Finsler structure is anchored by it.
The following lemma relates the notions of linear and projective polarity.
It
assumes V = Rn+1 is equipped with the standard Euclidean structure, and so all
linear spaces are identiﬁed with their duals.
Lemma 3.3. Identify a convex body K ⊂RPn with the cone ˜K ⊂V = Rn+1, and
with Kt = ˜K ∩{xn+1 = t}. For x ∈V \ {0}, write [x] = Rx ∈RPn. Then for
ˆp = (p, 1) ∈int(K1) ⊂Rn, the set −(K1 −ˆp)o ⊂Rn = {xn+1 = 0} coincides with
πn(K∨∩([ˆp]⊥+ en+1)), where πn projects orthogonally to Rn.
10
A Funk perspective on billiards, projective geometry and Mahler volume
Proof. Consider (−y, z) ∈Rn ⊕R which lies in K∨∩([ˆp]⊥+ en+1). Then for all
(κ, 1) ∈K1 we have ⟨(−y, z−1), (p, 1)⟩= ⟨−y, p⟩+(z−1) = 0, and ⟨(−y, z), (κ, 1)⟩=
⟨−y, κ⟩+ z ≥0.
Thus z = 1 + ⟨y, p⟩, and ⟨y, κ −p⟩≤1.
That is, πn(K∨∩
([ˆp]⊥+ en+1)) ⊂{(−y, 1) : y ∈(K1 −ˆp)o}. For the opposite inclusion, start with
(y, 1) ∈(K1 −ˆp)o, and verify that (−y, 1 + ⟨y, p⟩) ∈K∨∩([ˆp]⊥+ en+1).
□
In particular if K ⊂RPn is given in the aﬃne chart {xn+1 = 1} = Rn + en+1 by
K1 ⊂Rn, then K∨∩{xn+1 = 1} = −Ko
1 + en+1.
Proposition 3.4. Let K ⊂RPn be a convex set, and ﬁx η ∈int(K∨). The η-
anchored projective Finsler metric then coincides with RFunkη
K.
Proof. Using a Euclidean structure to identify TxP(V ) = T ∗
xP(V ) = x⊥, the cotan-
gent ball of the Euclidean-anchored Finsler metric is K∨∩(x⊥+ x), where x ∈Sn
is identiﬁed with x ∈P(V ).
Assume η = en+1. The aﬃne chart is {xn+1 = 1}, where the Funk cotangent
unit ball at ˆp = (p, 1) =
x
xn+1 =: A(x) is (K1 −p)o ⊂e⊥
n+1 = T ∗
p K1].
The
identiﬁcation between the two tangent spaces is the diﬀerential at x of the map
A : Sn →{xn+1 = 1}, namely dxA(v) =
v
xn+1 −
x
x2
n+1 vn+1 : x⊥→e⊥
n+1. The dual
map is
dxA∗: e⊥
n+1 →x⊥,
dxA∗(u) =
u
xn+1
−
1
x2
n+1
⟨x, u⟩en+1.
That is, dxA∗is a projection to x⊥parallel to en+1, followed by a
1
xn+1 - homothety.
Thus the inverse map (dxA∗)−1 is just the orthogonal projection on e⊥
n+1, followed
by an xn+1-homothety:
(dxA∗)−1 = xn+1πn.
Observe that K∨∩(x⊥+ en+1) = xn+1(K∨∩(x⊥+ x)).
The image of the
η-anchored cotangent ball at x, viewed inside x⊥= T ∗
xRPn, is therefore
(x⊥+ x) ∩K∨−en+1
xn+1
= (x⊥+ en+1
xn+1
) ∩K∨−en+1
xn+1
,
which is mapped by (dxA∗)−1 to
xn+1πn((x⊥+ en+1
xn+1
) ∩K∨) = πn((x⊥+ en+1) ∩K∨) = −(K1 −ˆp)o
using Lemma 3.3.
□
In light of the discussion following Deﬁnition 3.1, Theorem A part i) follows.
Corollary 3.5. The symmetrization of the projective co-nomadic Finsler metric is
the Hilbert metric.
Proof. Since the Hilbert metric is the symmetrization of the Funk metric, this
follows immediately from Proposition 3.4
□
Remark 3.6. Thus we obtain a construction of the Hilbert metric which is trans-
parently projectively invariant and Finslerian at the same time. An equivalent de-
scription can be found in [33, section 3].
A careful examination reveals that the Funk metric itself is projectively invariant,
up to the addition of an exact 1-form.
11
A Funk perspective on billiards, projective geometry and Mahler volume
Proposition 3.7. Fix η, θ ∈int(K∨), and let Fη, Fθ be the corresponding Funk
metrics on int(K). Then Fθ −Fη is an exact 1-form on int(K). The same holds
for the reverse Funk metric.
Proof. The statements for the Funk and reverse Funk metrics are trivially equiv-
alent. Assume η = en+1, and use a Euclidean structure to identify T ∗
xK with x⊥.
Examining the proof of Proposition 3.4 and using the notation therein, the corre-
sponding cotangent balls diﬀer by a shift of w =
θ
⟨x,θ⟩−en+1
xn+1 . To represent this
translation in the ﬁxed aﬃne hyperplane {yn+1 = 1}, we put ˆy = (y, 1) , x =
ˆy
|ˆy|,
θ = (α, β) ∈Rn ⊕R. Now apply (dxA∗)−1 = xn+1πn to w to get
s(y) := (dxA∗)−1w = xn+1
⟨x, θ⟩πn(θ) =
1
⟨y, α⟩+ β α.
Considered as a 1-form, s(y) is exact:
s(y) = d log(⟨y, α⟩+ β),
concluding the proof.
□
Thus the exact co-nomadic class of the Funk metric is projectively invariant.
