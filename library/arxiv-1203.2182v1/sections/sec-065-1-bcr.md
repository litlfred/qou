---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-065-1-bcr
section_title: "(bc)−r"
section_number: 1
pages: 70-73
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
= (−1)rA−2rq
− r(r+1)
2
1 qr
2(bc)−r
r∑
ℓ=0
(q2;q1)ℓ(1 −q2q2ℓ
1 )
(q1;q1)ℓ(1 −q2)
(A;q1)r+ℓ(q−1
2 A;q1)r−ℓ
(q2q1;q1)r+ℓ(q1;q1)r−ℓ
(−1)ℓq
− ℓ(ℓ+1)
2
1 q−ℓ
2 ,
where (x/b;q)n → (−x)nq
n(n−1)
2 b−n and (xb;q)n → 1 under b → 0 limit. This coincides with
(A10) and proves the gamma factor for R =Sr.
For theγ factor for the anti-symmetric representation Λr, we expect the following relation:
PΛ r(q̺
2;q1,q 2) = (−1)rAr/2qr/2
2
(A−1;q2)r
(q2;q2)r
=
r∑
ℓ=0
(q1;q2)ℓ(q2;q2)r+ℓ(A−1;q2)r+ℓ(q−1
1 A−1;q2)r−ℓ
(q2;q2)ℓ(q1q2;q2)r+ℓ(q2;q2)r+ℓ(q2;q2)r−ℓ
(1 −q1q2ℓ
2 )
(1 −q1) (−1)ℓA
3r
2qr
1q
ℓ(ℓ−1)−r(r−2)
2
2 .
(A12)
Choosing q =q2, λ =q1, and a =A−1 and taking b,c → ∞ in (A11), we also ﬁnd the same
identity as (A12).
– 69 –
A3 WKB analysis
A3.1 Another expression for Pn(T 2,2p+1;q,t )
As an analogy with an expression for the colored Jones polyno mial for T 2,2p+1,we ﬁnd a
conjecture for yet another expression of Pn(T 2,2p+1;q,t ) which is consistent with (3.97).
In [94, 95, 96, 97], the expression for the colored Jones poly nomial for (2, 2p + 1) torus
knots is given as:
Jn(T 2,2p+1;q) = qp(n2−1) ∑
kp≥···≥k2≥k1≥0
(−1)kpq− kp(kp+1)
2
(q1−n;q)kp(q1+n;q)kp
(q;q)kp
×
p−1∏
a=1
q−(ka−kp)(ka−kp−1)+ka(ka−ka+1)
[
ka+1
ka
]
q
, (A13)
where the q-binomial coeﬃcient is deﬁned by
[
n
m
]
q
:= (q;q)n
(q;q)n−m(q;q)m
. (A14)
By comparison with (3.97) for some lower orders in r and p, we can introduce the t
deformation as follows:
Pn=r+1(T 2,2p+1;q,t )
= q(p−1)r(r+2) ∑
i+j≤r
[ ∑
r−i=kp≥kp−1≥···≥k2≥k1≥0
(
qr+(r+1)(i+j)+ j(j+1)
2 t2pi+3j [r]′!
[i]′![j]′![r −i −j]′!
×
p−1∏
a=1
t2kaq−(ka−kp)(ka−kp−1)qka(ka−ka+1) [ka+1]′!
[ka]′![ka+1 −ka]′!
)]
. (A15)
where
[n]′! = [1]′[2]′ · · ·[n − 1]′[n]′, [n]′ = qn − 1
q − 1 = 1 +q +... +qn−1.
Furthermore, we can simplify the expression using the Cauch y’s q-binomial identity:
(−xq;q)k =
k∑
j=0
xjq
j(j+1)
2
(q;q)k
(q;q)j(q;q)k−j
. (A16)
Specializing x =qr+1t3 and k =r −i in the above identity, we ﬁnd
Pn=r+1(T 2,2p+1;q,t )
= q(p−1)r(r+2) ∑
r=kp≥kp−1≥···≥k2≥k1≥i≥0
[
qr+(r+1)it2pi (−t3qr+2;q)r−i(q;q)r
(q;q)i(q;q)k1−i
×
p−1∏
a=1
t2(ka−i)q−(ka−kp)(ka−kp−1)q(ka−i)(ka−ka+1) 1
(q;q)ka+1−ka
]
. (A17)
– 70 –
Now let us study the asymptotic behavior of (A17). In ℏ → 0 limit, we ﬁnd the following
expansion:
Pn=r+1(T 2,2p+1;q,t ) ∼
∫ p−1∏
α=0
dzα e
1
ℏ (V(2,2p+1)(zα,x,t))+O(ℏ), (A18)
V(2,2p+1)(⃗ z,x,t) = (p − 1)(logx)2 + 2p(logt) · (logz0) + (logx) · (logz0)
+
p−1∑
a=1
[
2(logt) · (log(zaz−1
0 )) − (logzax−1)2 + (logzaz−1
0 ) · (logzaz−1
a+1)
]
+Li2(−t3x) − Li2(−t3x2z−1
0 ) − Li2(x) + Li2(z0) + Li2(z1z−1
0 )
−pLi2(1) +
p−1∑
a=1
Li2(za+1z−1
a ), (A19)
where ka = 1
ℏ logza for a = 1, · · ·p, i = 1
ℏ logz0, and r = 1
ℏ logx.
The critical point of this potential is determined by
1 = exp
[
zα
∂V(2,2p+1)(⃗ z,x,t)
∂zα
]
, (α = 0, · · ·,p − 1). (A20)
Combining a condition y = exp
(
x∂V(2,2p+1)/∂x
)
, we ﬁnd the following set of algebraic equa-
tions for zα:
1 = t2x2(z1 −z0)
z1(z0 − 1)(t3x2 +z0), 1 = t2x(x −zp−1)
zp−1(zp−1 −zp−2),
1 = t2x2(zp−2 −zp−1)
zp−1zp−2(zp−3 −zp−2), · · ·, 1 = t2x2(za −za+1)
zaza+1(za−1 −za), · · ·, 1 = t2x2(z1 −z2)
z1z2(z0 −z1),
y =
(−1 +x)z2
1z2
2 · · ·z2
p−1(t3x2 +z0)2
(1 +t3x)(x −zp−1) . (A21)
After eliminatingzα (α = 0, · · ·,p −1), we obtain the same reﬁned A-polynomialsAT 2,2p+1(x,y ;t)
as given in Table 3, which are computed on the basis of (3.61) f or p = 1, 2, 3, 4, 5.
A3.2 Asymptotic limit of P Sn−1
DGR (T 2,2p+1;a,q,t ) with a =q2t2
As we discussed in section 3.3.4, for the (colored) superpol ynomials in grading conventions of
[27], the right limit to consider is
q2t2 → 1, (A22)
with x = qn and t kept ﬁxed. In other words, in this grading conventions, the c ombination
log(qt) plays the role of a small expansion parameter ℏ → 0. On the other hand, if we
think of the HOMFLY variable a as a = eN ℏ (as opposed to a = qN), then it might be
natural to consider a specialization of the superpolynomia l to a = (eℏ)2 = q2t2 (instead of
a =q2). With this motivation in mind, here we consider the “large c olor” asymptotics of the
superpolynomial specialized to a =q2t2.
– 71 –
Much as in (3.166), we ﬁnd
P Sn−1
DGR (T 2,2p+1;a =q2t2,q,t ) ∼
∫
dz e
1
ℏ
(
V DGR′
(2,2p+1)(z,x;t)+O(ℏ)
)
, (A23)
with the potential function
V DGR′
(2,2p+1)(z,x ;t) = Li2(−t3) − Li2(x) + Li2(−tx) + Li2(xz−1) − Li2(−t3xz−1)] + Li2(z)
−Li2(zt−2) + Li2(xzt−2) − Li2(−txz) − π2
6
+(logt) · (logzx−2) + (2p + 1)(logxz−1) · (log(−x
1
2z
1
2 )). (A24)
From this potential function, eqs. (3.168) and (3.171) yiel d the equations for the saddle point
that dominates the integral:
1 = t(t2 −z0)z−2p−1
