---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-058-3b-the-relation-of-iteration-of-the-harmonic-fro
section_title: "3B. The relation of iteration of the harmonic Frobenius of series"
section_number: null
pages: 69-71
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
can now formalize the iteration of the harmonic Frobenius from the point of view of series. We refer to
K⟨⟨e0∪µN⟩⟩6
har=∏
w harmonic word K.w deﬁned in [Jarossay 2015, Section 3].
Deﬁnition 3B.1. Let the map of iteration of the harmonic Frobenius of series be the mapiter6
har(3,3 a, a):
K⟨⟨e0∪µN⟩⟩6
har→ K[3,3 a, a]⟨⟨e0∪µN⟩⟩6
har deﬁned by, for any wordw,
iter6
har( f)[w]=
∑
w′ word on e0∪µN
Pw,w′,(li)d(3a, a,( Bl
m(ξ)) 0⩽m⩽∑d
i=1 li+d+1, ξ∈µN(K)) f[w′].
Let us now ﬁnish the proof of (0 -5). By Lemmas 3A.1, 3A.2 and Proposition 3A.4, the only thing to
check is the convergence of the series, which are inﬁnite sums over (li)d∈ Nd. This follows from the
following facts:
(a) For any n∈ N∗, it follows from pvp(n)⩽ n thatvp(1/n)>− log(n)/log(p); moreover, for any
n∈ N∗, we havevp(Bn)>−1 (this is part of von Staudt–Clausen’s theorem). Thus for all l, m, we
havevp(Bl
m)>−1− log(l+ 1)/log(p), and, given that|ξ|p=| 1−ξ|p= 1 for allξ∈µN(K)\{ 1},
we have, for all l, m, andξ∈µN(K)\{ 1},vp(Bl
m(ξ))> 0.
1736 David Jarossay
(b) If T1, T2 are formal variables and m∈ N∗, we have (T m
1 − 1)/(T1− 1)−(T m
2 − 1)/(T2− 1)=
(T m
1 − T1)/(T1− 1)−(T m
2 − T2)/(T2− 1).
(c) For any z∈ K such thatvp(z)⁄= 0, we havevp(1/(z− 1))> 0 ifvp(z)> 0, andvp(1/(z−1− 1))>
vp(z−1) ifvp(z)< 0.
Remark 3B.2. Equation (0-5) is related to the formula harpαN= harpα◦6
har har(pα)
N proved in [Jarossay
2015], where◦6
har is the pro-unipotent harmonic action of series introduced in [loc. cit., Section 4.3]:
restricting that equation to harm with m a power of p gives a functional equation satisﬁed by the map
α↦→ harpα, which expresses har pα+β in terms of har pα and har(pα)
pβ .
Remark 3B.3. As in [Jarossay 2015], the computation which leads to the above result remains true
for the generalization of cyclotomic multiple harmonic sums obtained by replacing the factors 1/mni
i ,
1⩽ i⩽ d in (0-2) by, more generally, factorsχi(mi) whereχi are locally analytic group endomorphisms
of the multiplicative group K∗, which are analytic on disks of radius p−α.
Remark 3B.4. The main theorem gives formulas for p-adic cyclotomic multiple zeta values which
depend on an additional parameter, a number of iterations of the Frobenius different from the one
under consideration. Here is another way to obtain formulas with parameters. The computation of
regularized iterated integrals in [Jarossay 2019, Section 3] can be done by replacing the Euclidean
division by pα in N by the Euclidean division by pβ withβ≥α. This gives, for example, ζp,α(n)=
pαn/(n− 1) lim|m|p→0 1/(pβm)∑
0<m1<pβm, pα ∤m 1/mn
1, and this gives formulas in which the prime
weighted multiple harmonic sums are replaced by the following generalization, where (l1,..., ld)∈ Nd,
I, I′⊂{ 1,..., d} andβ:
pα∑d
i=1 ni+β∑d
i=1 li
∑
0=m0<m1<···<md<pβ
for j∈I, m j−1≡m j[pα]
for j∈I′, m j≡0[pα]
(ξ2
ξ1
)m1
···
(ξd+1
ξd
)md( 1
ξd+1
)pβ
mn1+l1
1 ··· mnd+ld
d
.
Example 3B.5. Let us consider the case of P1\{ 0, 1,∞}(N= 1), for which we have q= p,˜α=α,
˜α0=α0, and depth one and two. Equation (0-5) is, for all n∈ N∗,
harpα(n)
=−
∑
l>0
(−n
l
)
harpα0(l+ n)
l+1∑
u=1
Bl
u
1
1− pα0(u+n)−
∑
u>n+1
pαu 1
1− pα0u
∑
l>u−n−1
(−n
l
)
harpα0(l+ n)Bl
u−n.
For all n1, n2∈ N∗, harpα(n1, n2) is the sum of the following terms, where the variables v1,v 2 are
those deﬁned in Lemma 3A.1 and where, for a set E, 1E means the characteristic function of E:
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1737
• The term “v1=v2”:
∑
u>1
l1,l2>0
l1+l2>u−1
pα(u+n1+n2)− 1
pα0(u+n1+n2)− 1
2∏
i=1
(−ni
li
)
(Bl1,l2
u
2∏
i=1
harpα0(ni+ li)+ Bl1+l2
u harpα0(n1+ l1, n2+ l2)).
• The term “v1<v 2”:
∑
M1,M2>−1
u,t>1
[ 1t⁄=u+n2
pα0(n2+u−t)− 1
( pα(n1+n2+u)− pα0(n1+n2+u)
pα0(n2+n1+u)− 1 − pα(n1+t)− pα0(n1+t)
pα0(n1+t)− 1
)
+ 1t=u+n2
( αpα(n1+n2+u)
pα0(n1+n2+u)− 1+ 1− pα(n1+n2+u)
(pα0(n1+n2+u)− 1)2
)
BM1+t
t BM2+u
u
×
min(t,M2+u)∑
j=0
( t
j
)(−n1
M1+t
)( −n2
M2+u− j
)
harpα0(n1+ M1+ t) harpα0(n2+ M2+ u− t)
]
.
• The term “v1>v 2”: by the change of variable (m1, m2)↦→(pα− m1, pα− m2), it is
∑
0<m1<m2<pα
vp(n1)>vp(n2)
(pα)n1+n2
nn1
1 nn2
2
=
∑
l1,l2>0
0<n1<n2<pα
vp(n1)<vp(n2)
(−n1
l1
)(−n2
l2
)(pα)l1+l2+n1+n2
nn1
1 nn2
2
.
