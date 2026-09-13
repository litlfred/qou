---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-014-7-mahler-volumes-of-every-funk-scale
section_title: "Mahler volumes of every Funk scale"
section_number: 7
pages: 22-26
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
---
Deﬁne the Funk-Mahler volume of radius 0<r< ∞ (aroundq∈ int(K)) by
Mr(K,q ) =ωnr−n volF
K(BF
r (q,K )), M r(K) = inf
q∈int(K)
Mr(K,q ).
In Euclidean terms, we have
Mr(K,q ) =r−n
∫
z∈q+(1−e−r)(K−q)
|Kz|dz,
whereKz denotes the dual body with respect toz. Evidently,Mr(K,q ) is invariant
under the full linear group with q at the origin.
Lemma 7.1. For any convex K, Mr(K,q ) is a strictly convex function of q. In
particular, if K =−K then Mr(K) =Mr(K, 0).
Proof. The function z↦→| Kz| is well-known to be strictly convex in z∈ int(K).
This follows at once by writing
|Kz| =ωn
∫
Sn−1
max
x∈K
⟨θ,x−z⟩−ndσ(θ),
where σ is the rotation-invariant probability measure on Sn−1, and noticing that
for any ﬁxed x,θ , the function z↦→ (⟨x,θ⟩−⟨ z,θ⟩)−n is strictly convex.
It follows that
Mr(K,q ) =r−n
∫
(1−e−r)K
|Ke−rq+w|dw
is convex as well.
If K =−K then Mr(K,q ) =Mr(K,−q), and so q = 0 must be a minimum.
□
The Funk-Mahler volume enjoys invariance under duality, as follows.
Proposition 7.2. It holds for all K⊂ Rn that Mr(K,q ) =Mr(Kq,q ). In partic-
ular, if K =−K then Mr(K) =Mr(Ko).
23 A Funk perspective on billiards, projective geometry and Mahler volume
Proof. We may assume q = 0. Put ρ = 1−e−r, so that BF
r = ρK is the ball of
radius r in the Funk metric, centered at the origin. Then
Mr(K, 0) = ωn
rn volF
K(ρK) = ωn
rn volF
ρ−1Ko(Ko) =Mr(ρ−1Ko, 0) =Mr(Ko, 0),
where the second equality is due to Corollary 3.11, the penultimate equality holds
since Ko is the ball of radius r around the origin in the Funk geometry of ρ−1Ko,
and the last equality is due to GL-invariance.
The second statement now follows by Lemma 7.1. □
Remark 7.3. In projective-invariant terms, this duality assumes the following
form. For K ⊂ P, q ∈ int(K) and η ∈ int(K∨), let Bη
r (K,q ) be the outward
ball of radius r centered at q in Funkη(K). Then Bη
r (K,q ) ⊂ Funkη(K) and
Bq
r(K∨,η )⊂ Funkq(K∨) have equal volume.
Asr→ 0,Mr(K,q )→M0(K,q ) :=|K||Kq|. Thus the Mahler volumeM0(K) :=
limr→0Mr(K) is recovered at inﬁnitesimal scale.
On the opposite end of the scale, the asymptotics of Mr(K,q ) is governed by
the regularity of the boundary of K. When K is smooth and strictly convex, we
recover the centro-aﬃne surface area as r→∞ , as established in [9]. Recall that
the centro-aﬃne surface area relative to q∈ int(K) is given by
Ωn(K,q ) =
∫
∂K
k
1
2
p
⟨p−q,νp⟩
n+1
2
dµK(p;q) =
∫
∂K
k
1
2
p
⟨p−q,νp⟩
n−1
2
dHn−1(p), (5)
where kp is the Gaussian curvature of ∂K at p, νp the unit outward normal, and
µK(p;q) the cone measure with the origin at q.
As [9] focuses on the Hilbert metric with the Busemann volume, we provide for
the sake of completenss the details of the computation in our case.
Lemma 7.4. Let A be a positive-deﬁnite n×n matrix, and QA ={x∈ Rn :
⟨Ax,x⟩≤ 1}. Then for p∈∂QA and 0<ρ< 1, we have
|Qρp
A| =ωn
(detA)1/2
(1−ρ2)
n+1
2
=ωn
1
(1−ρ2)
n+1
2
k1/2
p
⟨p,νp⟩
n+1
2
.
Proof. For the ﬁrst equality, we compute that Qρp
A ={ξ :⟨B(ξ−c),ξ−c⟩≤ 1},
where, denoting B0 =A−1−ρ2ppT , we have
c =ρB−1
0 p, B = B0
1 +ρ2⟨B−1
0 p,p⟩.
Now by the Sherman-Morrison formula,
B−1
0 =A + ρ2
1−ρ2AppTA⇒⟨B−1
0 p,p⟩ = 1
1−ρ2,
while by the matrix determinant lemma we h ave
detB0 = (1−ρ2) detA−1.
It follows that
|Qρp
A| =ωn
√
detB
−1
=ωn
√
detA
1−ρ2 (1−ρ2)−n
2 =ωn
√
detA
(1−ρ2)
n+1
2
24 A Funk perspective on billiards, projective geometry and Mahler volume
For the second equality, recall that νx = Ax
|Ax|. It follows that for v∈TpQA,
Dpνx(v) = Av
|Ap|−⟨ Av
|Ap|,νp⟩νp = 1
|Ap|πTpQA◦A.
Take an orthonormal basis v1,...,v n−1 of TpQA, and evaluate the volume of
A(v1∧···∧ vn−1∧p) in two ways. We get
|A(v1∧···∧ vn−1∧p)| = detA·⟨p,νp⟩ = det(πTpQA◦A)·|Ap|.
Noting also that⟨p,νp⟩ = 1
|Ap| since⟨Ap,p⟩ = 1, we ﬁnd detA = kp
⟨p,νp⟩n+1. □
Lemma 7.5. ForK∈K 0(Rn) smooth and strictly convex, and p∈∂K , we have
|Kρp| = (1−ρ)−n+1
2
(
2−n+1
2 ωn
k1/2
p
⟨p,νp⟩
n+1
2
+err(p)
)
,
whereerr(p)→ 0 as ρ→ 1, uniformly in p∈∂K .
Proof. Throughout the proof,c,c′ will be positive constants that are bounded away
from 0 and∞, uniformly in p∈∂K, and may change between occurrences.
As both|Kρp| and the main term on the right hand side are SL(n)-invariant, we
may assume without loss of generality thatp =−en andTp∂K = Span(e1,...,e n−1).
We may further assume thatyn =−1+ap
2|y′|2 is the quadratic approximation of∂K
nearp, where we write y′ = (y1,...,y n−1). Let Q be the ellipsoid ap|y′|2 +y2
n = 1,
osculating ∂K at p. Write 1−ρ =ϵ2, and note that c≤ap≤c′.
Let νx be the Euclidean normal at x∈∂K. One has
‖νx‖Kρp =hK(νx)−⟨νx,ρp⟩ =⟨x−ρp,νx⟩.
We may therefore parametrize the points of Kρp by
ζK : [0, 1]×∂K→Kρp, ζ K(α,x ) =α νx
⟨x−ρp,νx⟩.
Then by Cauchy-Schwartz,
⟨x−ρp,νx⟩≥⟨ x−p,νx⟩− (1−ρ)|⟨p,νx⟩|≥⟨ x−p,νx⟩− ϵ2.
LetH be the hyperplane parallel toTp∂K at distanceϵ from it, andH+,H− the
half-spaces it deﬁnes, withp∈H+. We claim that|ζK([0, 1]×∂(K∩H−))|≤ cϵ−n.
Consider x∈ ∂K∩H−, so |x−p|≥ ϵ. If νx is proportional to x−p then
⟨x−p,νx⟩|x−p|≥ ϵ, and |ζK(α,x )|≤ 2
ϵ . Otherwise, consider the aﬃne plane
P =p + Span(x−p,νx), and consider the planar convex body KP =K∩P . Using
Euclidean cooridnates (x1,x 2) in which TpKP = Re1, QP =Q∩P is osculated at
p by the parabola x2 =−1 + 1
2apx2
1.
We orient ∂K in such a way that the tangent at x makes an acute angle with
x−p. Let y∈H∩∂KP belong to the oriented arc [ p,x ]⊂∂KP . It holds by the
convexity ofKP that
⟨x−p,νx⟩≥| x−p| sin∡pxy =|p−y| sin∡pyx≥c√ϵ sin∡pyx.
Denoting by v the tangent ray to ∂KP at y, we have
c√ϵ =∡pyz≤∡pyx≤π−∡(y−p,v ) =π−c√ϵ.
Therefore,
⟨x−p,νx⟩≥ c√ϵ sin∡pyx≥cϵ.
25 A Funk perspective on billiards, projective geometry and Mahler volume
x
p
ϵ
νx
KP
QP
H−
H +
y
c√ϵ
z
v
Figure 9.
Thus again we ﬁnd that |ζK(α,x )|≤ c
ϵ. That is, ζK([0, 1]×∂K∩H−)⊂ c
ϵBn,
and so
|ζK([0, 1]× (∂K∩H−))|≤ cϵ−n. (6)
DeﬁnezK(y′),zQ(y′) : Rn−1→ R for|y′|<c√ϵ by havingxK(y′) := (y′,zK(y′))∈
∂K,xQ(y′) := (y′,zQ(y′))∈∂Q, and let νK(y′),νQ(y′) be the correspondning unit
normals. Then zK(y′) =zQ(y′) +O(|y′|3) =−1 + ap
2|y′|2 +O(|y′|3).
p
ϵ
K
Q
H −
H +
o
ρp
Q−
Q+
Figure 10.
Deﬁne the ellipsoids Q± = {y : 1
2(ap± 2ϵ1/3)|y′|2 +y2
n = 1}. It holds that
zQ±(y′) =−1 + 1
2(ap± 2ϵ1/3)|y′|2 +O(|y′|3), and so for ϵ≪ 1,
Q+∩H+⊂K∩H+⊂Q−∩H+.
Moreover, as|νK(y′)−νQ(y′)| =O(|y′|) and|y′|≤ cϵ1/2≪ϵ1/3, it is evident that
ζQ−([0, 1]×Q−∩H+)⊂ζK([0, 1]×K∩H+)⊂ζQ+([0, 1]×Q+∩H+).
By estimate (6) applied to Q± and combined with Lemma 7.4, we have
ζQ±([0, 1]×Q±∩H+) =ϵ−(n+1)
(
2−n+1
2 ωn
k1/2
p
⟨p,νp⟩
n+1
2
+err±(p)
)
,
and applying (6) for K, the claim follows.
□
Proposition 7.6. Forq∈ int(K),
lim
R→∞
volF
K(BF
R(q,K ))
e
n−1
2 R = 1
n− 12−n−1
2 Ωn(K,q ).
26 A Funk perspective on billiards, projective geometry and Mahler volume
Proof. We may put q = 0. Parametrize the outward Funk ball of radius R around
0 by p∈∂K, 0≤r≤R using φ(p,r ) = (1−e−r)p. Then
volF
K(BF
R(0,K )) =
∫ R
0
∫
∂K
|Kφ(p,r)|Jac(φ(p,r ))dHn−1(p)dr.
Now Jac(φ(p,r )) = (1−e−r)n−1e−r⟨p,νp⟩, while by Lemma 7.5
|Kφ(p,r)| = 2−n+1
2 ωne
n+1
2 r k1/2
p
⟨p,νp⟩
n+1
2
+o(e
n+1
2 r),
where the error term is uniform in p. Applying l’Hospital’s rule we ﬁnd
lim
r→∞
volF
K(BF
r (0,K ))
e
n−1
2 r = lim
r→∞
2
n− 1
(1−e−r)n−1e−r∫
∂K|Kφ(p,r)|⟨p,νp⟩dHn−1(p)
e
n−1
2 r
= 1
n− 12−n−1
2
∫
∂K
k1/2
p
⟨p,νp⟩
n−1
2
dHn−1(p).
□
