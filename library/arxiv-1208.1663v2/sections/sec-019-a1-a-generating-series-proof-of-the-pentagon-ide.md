---
doc_id: arxiv-1208.1663v2
doc_title: "The 3D index of an ideal triangulation and angle structures"
section_id: sec-019-a1-a-generating-series-proof-of-the-pentagon-ide
section_title: "A.1. A generating series proof of the pentagon identity"
section_number: null
pages: 23-26
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "The 3D index of an ideal triangulation and angle structures — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
prove that I∆ satisﬁes the pentagon identity using generating series. We will abbreviate
the Pochhammer symbol
(x;q)∞ =
∞∏
n=0
(1−xqn)
by (x)∞ = (x;q)∞. The proof
• starts from an associativity identity
(z1z2)∞
(z1)∞(z2)∞
· (x1z−1
1 q)∞(x2z−1
2 q)∞
(x1x2z−1
1 z−1
2 q)∞
= (x1z−1
1 q)∞
(z1)∞
· (x2z−1
2 q)∞
(z2)∞
· (z1z2)∞
(x1x2z−1
1 z−1
2 q)∞
that uses 4 additional variables{x1,x 2,z 1,z 2} in addition to the 4 variables
{m1,m 2,e 1,e 2},
• extracts coeﬃcients with respect to (z1,z 2) and
• specializes (x1,x 2) = (q−m1,q−m2). This last part is not algebraic and requires to
show convergence. The latter follows from Corollary 2.7.
24 STA VROS GAROUF ALIDIS
Let us now give the details. Consider
(A.1) Fe(x) =
∑
n
(−1)nq
1
2n(n+1)xn
(q)n(q)n+e
∈ Z[[x,q ]].
Here and below, summation is over the set of integers, with the understanding that 1/(q)n = 0
for n< 0.
We will show that
(A.2) qe1e2Fe1(qe2x1)Fe2(qe1x2) =
∑
e3
(x1x2q)e3Fe1+e3(x1)Fe2+e3(x2)Fe3(x1x2)
in the ring Z((x1,x 2,q )). Since
Fe(q−m) =q
em
2 I∆(m,e ),
the substitution (x1,x 2) = (q−m1,q−m2) (which converges by Corollary 2.7) implies the pen-
tagon identity of Equation 3.5.
Lemma A.1. For|q|< 1 we have:
1
(x)∞
=
∑
n
xn
(q)n
|x|< 1
(xq)∞ =
∑
n
(−1)nq
1
2n(n+1)xn
(q)n
(xy)∞
(x)∞
=
∑
n
(y)nxn
(q)n
|x|< 1
(xy)∞
(x)∞(y)∞
=
∑
r,s
qrsxrys
(q)r(q)s
|x|< 1,|y|< 1
(xq)∞(yq)∞
(xyq)∞
=
∑
r,s
(−1)r+sq
1
2 (r−s)2+ 1
2 (r+s)xrys
(q)r(q)s
|xyq|< 1
Proof. The ﬁrst three identities are well-known and appear in [29, Prop. 2]. The last two
follow from the ﬁrst three:
∑
r,s
qrsxrys
(q)r(q)s
=
∑
r
xr
(q)r
∑
s
(qry)s
(q)s
=
∑
r
xr
(q)r
1
(qry)∞
= 1
(y)∞
∑
r
(y)rxr
(q)r
= (xy)∞
(x)∞(y)∞
,
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 25
∑
r,s
(−1)r+sq
1
2 (r−s)2+ 1
2 (r+s)xrys
(q)r(q)s
=
∑
r
(−1)rq
1
2r2+ 1
2rxr
(q)r
∑
s
(−1)rq
1
2s2+ 1
2s(q−ry)s
(q)s
=
∑
r
(−1)rq
1
2r2+ 1
2rxr
(q)r
(q1−ry)∞
= ( yq)∞
∑
r
(y−1)r(xyq)r
(q)r
= (xq)∞(yq)∞
(xyq)∞
.
□
Remark A.2. The identities of Lemma A.1 also hold in the ring Z((x,y,q )).
Observe that Fe(x) is an analytic function of (x,q ) when|q|< 1 and x∈ C. With|q|< 1
and|y|< 1, Lemma A.1 gives
∑
e
Fe(x)ye =
∑
n
(−1)nq
1
2n2+ 1
2nxn
(q)n
∑
e
ye
(q)n+e
= 1
(y)∞
∑
n
(−1)nq
1
2n2+ 1
2n(xy−1)n
(q)n
= (xy−1q)∞
(y)∞
.
Thus, the generating function of the left hand side of Equation (A.2) is
∑
e1,e2
qe1e2Fe1(qe2x1)Fe2(qe1x2)ze1
1 ze2
2
=
∑
n1,n2
(−1)n1+n2q
1
2n2
1+ 1
2n2
2+ 1
2n1+ 1
2n2xn1
1 xn2
2
(q)n1(q)n2
∑
e1,e2
qe1e2+n2e1+n1e2ze1
1 ze2
2
(q)n1+e1(q)n2+e2
= (z1z2)∞
(z1)∞(z2)∞
∑
n1,n2
(−1)n1+n2q
1
2 (n1−n2)2+ 1
2n1+ 1
2n2(x1z−1
1 )n1(x2z−1
2 )n2
(q)n1(q)n2
= (z1z2)∞
(z1)∞(z2)∞
· (x1z−1
1 q)∞(x2z−1
2 q)∞
(x1x2z−1
1 z−1
2 q)∞
.
Likewise, the generating function of the right hand side of Equation (A.2) is the same
∑
e1,e2
(∑
e3
(x1x2q)e3Fe1+e3(x1)Fe2+e3(x2)Fe3(x1x2)
)
ze1
1 ze2
2
=
(∑
e1
Fe1(x1)ze1
1
)(∑
e2
Fe2(x2)ze2
2
)(∑
e3
Fe3(x1x2)(x1x2z−1
1 z−1
2 q)e3
)
= (x1z−1
1 q)∞
(z1)∞
· (x2z−1
2 q)∞
(z2)∞
· (z1z2)∞
(x1x2z−1
1 z−1
2 q)∞
.
26 STA VROS GAROUF ALIDIS
The above identities for each side of Equation (A.2) hold when |q| < 1, |z1| < 1,
|z2| < 1 and |x1x2z−1
1 z−1
2 q| < 1. Remark A.2 implies that they also hold in the ring
Z((x1,x 2,z 1,z 2,q )). Extracting the coeﬃcient of ze1
1 ze2
2 from the above concludes the proof
of Equation (A.2). □
