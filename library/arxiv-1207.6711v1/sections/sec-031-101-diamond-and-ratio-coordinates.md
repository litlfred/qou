---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-031-101-diamond-and-ratio-coordinates
section_title: "Diamond and ratio coordinates"
section_number: 10.1
pages: 31-33
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
that the short edges of the natural cocycle of a generic SL( n, C)/N-decoration are given by
diamond coordinates, and that the long edges are given by ratios of two Ptolemy coordinates.
We review these results below.
Deﬁnition 10.1. Let c be a Ptolemy assignment on ∆ 3
n. For each vertex v0v1v2 of ∆3
n and
eachα∈ ∆3
n−2(Z) on the face containing v0v1v2, we associate a diamond coordinate
(10.3) dv0v1v2
α (c) =−εv0v1v2
<
cα+2v0cα+v1+v2
cα+v0+v1cα+v0+v2
.
Here εv0v1v2
< is the sign of the S3 permutation required to bring the sequence v0,v 1,v 2 into
lexicographic order.
Deﬁnition 10.2. Let c be a Ptolemy assignment on ∆ 3
n. For each vertex v0v1v2 of ∆3
n and
each point kv0 +lv1 on the long edge containing v0v1v2, we associate a ratio coordinate
ev0v1
kv0+lv1(c) = (−1)l ckv0+(l+1)v1
c(k+1)v0+lv1
where k +l =n− 1.
Notation 10.3. Whenc is clear from the context, we suppress it from the notation, i.e. we
write dv0v1v2
α and ev0v1
kv0+lv1 instead of dv0v1v2
α (c) and ev0v1
kv0+lv1(c).
32 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
0
1
3
2
d102
1120 = c1320c2130
c2220c1230
d312
0121 =−c0123c0231
c0222c0132c1320
c2220
c2130
c1230
c0222 c0123
c0132c0231
1
0 c(k−1,l,0,0)
c(k,l−1,0,0)
e1000,0100
(k,l,0,0) = (−1)lc(k,l−1,0,0)
c(k−1,l,0,0)
Figure 20. Diamond coordi-
nates.
Figure 21. Ratio coordinates.
As explained in Remark 9.7, we can view the natural cocycle of an SL(n, C)/N-decoration
as a cocycle on ∆3
n. We thus employ the labeling conventions of Section 9.2.1.
Proposition 10.4 (Garoufalidis-Thurston-Zickert [11]). The natural cocycle Lαβ(D) of a
generic SL(n, C)/N-decoration D on ∆3
n is given in terms of the Ptolemy assignment C(D)
by
(10.4)
γv0v1v2 = id, β v0v1v2 =
∏
(α0,α1,α2)∈∆2
n−2(Z)
xα1+1
(
dv0v1v2
α1v0+α2v1+α0v2
)
αv0v1v2 =q(ev0v1
(n−1)v0
,ev0v1
(n−2)v0+v1
,...,e v0v1
(n−1)v1
),
In the product, the order of the factors is given by the lexicographic order on ∆ 2
n−2(Z). □
Remark 10.5. It is convenient to introduce the notation
(10.5) dk,i =dv0v1v2
(i−1)v0+(n−i−k)v1+(k−1)v2
.
With this notation, the formula for the middle edge becomes
(10.6) βv0v1v2 =
n−1∏
k=1
n−k∏
i=1
xi(dk,i).
This agrees with the notation in [11]. Although this notation is convenient, it does not
behave properly under reordering.
10.1.1. Behavior under reordering.
Lemma 10.6. The diamond coordinates of c and σ∗(c) are related by
(10.7) d(σ∗(c))v0v1v2
α =d(c)σ(v0)σ(v1)σ(v2)
σ(α) .
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 33
d1,1
d1,2
d1,3
d1,4
d2,1
d2,2
d2,3
d3,1
d3,2 d4,1
v0 v2
v1
βv0v1v2 =x1(d1,1)x2(d1,2)x3(d1,3)x4(d1,4)
x1(d2,1)x2(d2,2)x3(d2,3)
x1(d3,1)x2(d3,2)
x1(d4,1)
Figure 22. Factorization of a middle edge βv0v1v2 in terms of diamond coordiates.
Proof. It is enough to prove this for vi = i and σ = σ01, σ = σ12 and σ = σ23. We prove
it for σ = σ01, the other cases being similar. Letting t = α +e0 +e1 and α′ = σ01(α), and
using that ε012
< = 1 and ε102
< =−1, we have
(10.8)
d(σ∗
01(c))012
α =− σ∗
01(c)α+2e0σ∗
01(c)α+e1+e2
σ∗
01(c)α+e0+e1σ∗
01(c)α+e0+e2
=−det(Iσ01,σ01(t+e0−e1)) det(Iσ01,σ01(t+e2−e0))
det(Iσ01,σ01(t)) det(Iσ01,σ01(t+e2−e1))
cα′+2e1cα′+e0+e2
cα′+e1+e0cα′+e1+e2
=−(−1)(t0+1)(t1−1)(−1)(t0−1)t1
(−1)t0t1(−1)t0(t1−1)
cα′+2e1cα′+e0+e2
cα′+e1+e0cα′+e1+e2
=−(−1) cα′+2e1cα′+e0+e2
cα′+e1+e0cα′+e1+e2
=d(c)102
α′ .
This proves the result. □
Lemma 10.7. The ratio coordinates of c and σ∗c are related by
(10.9) σ∗(e)v0v1
α =εn−1eσ(v0)σ(v1)
σ(α)
where ε is a sign depending on whether or not σ ﬂips the orientation of the edge v0v1.
Proof. We shall not need this, so we leave the proof to the reader. □
