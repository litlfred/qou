---
doc_id: arxiv-1912.13486v2
doc_title: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds"
section_id: sec-001-22-analysis-on-homological-block-and-index-of-le
section_title: "Analysis on homological block and index of lens space theory"
section_number: 2.2
pages: 9-21
source_pdf: 1912.13486v2.pdf
source_sha256: 9a8dbc1a143f7448
doc_brief: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds — We consider theS2×qS1 supersymmetric index of a 3dN = 2 theory T [M3] when M3 is a plumbed 3-manifold."
---
When the 3-manifold is a lens space M3 =L(p, 1)≃S3/Zp, the corresponding 3d N = 2
theoryT [L(p, 1)] has been discussed in [20, 25, 26] and more recently in [1, 2] in the context
of homological blocks. Since our analysis for the plumbed 3-manifolds can be regarded as
an extrapolation of this example, we study the homological block and the index of the lens
space theory in detail.
The 3dN = 2 theory T [L(p, 1),U (N)] (resp. T [L(p, 1),SU (N)]) corresponding to the
lens space M3 = L(p, 1) is given by a 3d N = 2 vector multiplet for G = U(N) (resp.
SU (N)), an adjoint chiral multiplet with R-charge 2 which is charged +1 under U(1)t
global symmetry, and there is a Chern-Simons term with a level p.
The homological blocks for the lens space when the gauge group is G = U(N) was
obtained in [1] from the WRT invariant [27], and it is given by
ˆZb(t,q ) = 1
|Wb|
1
(tq;q)N∞
∮
|sj|=1
N∏
j=1
dsj
2πisj
∏
1≤i⁄=j≤N
(sis−1
j ;q)∞
(sis−1
j qt;q)∞
Θp·IdN
b (s;q) (2.33)
where Θp·IdN
b (s;q) is the theta function for a lattice ZN with a quadratic form p· IdN
Θp·IdN
b (s;q) =
∑
n∈pZN+b
q
∑N
j=1
n2
i
2p
N∏
j=1
sni
i . (2.34)
The homological block (2.33) as the D2×qS1 partition function can be obtained from the
vector multiplet VN with the Neumann boundary condition (2.22) and the adjoint chiral
multiplet Φ +
R=2,N whose R charge is 2 and U(1)t charge is +1 also with the Neumann
boundary condition (2.24). Θ p·IdN
a (s;q) is interpreted as the contribution from the bound-
ary degrees of freedom that cancel the anomaly inﬂow from the CS term whose level is
p, which we don’t know how to derive from the Lagrangian description of the N = (0, 2)
boundary theory. Also, there would be an extra factor ∏
1≤i,j≤Nθ((−q
1
2 )1−Rv−1)1/2 in
the calculation, which captures information of the background CS contributions for U(1)t
symmetry and U(1)R symmetry at the level of the index. If we would like to cancel the
– 8 –
background CS contributions, this theta function (or an equivalent term up to theta func-
tion ambiguity) needs to be included in (2.33) because q-Pochhammer symbols have − 1
2
background CS levels. But we may ignore this contribution in the calculation of homolog-
ical block because it gives just an overall factor. Then we obtain (2.33).
The unreﬁned limit t = 1 of the homological block (2.33) is
ˆZb(q) =
ˆZb(t,q )
(tq;q)N∞
⏐⏐⏐⏐
t→1
= 1
|Wb|
∮
|si|=1
N∏
j=1
dsj
2πizj
∏
1≤i⁄=j≤N
(1−sis−1
j ) Θp·IdN
b (s;q). (2.35)
The index of T [L(p, 1),U (N)] is
IU(N) =
∑
m1≥···≥mN∈Z
1
|Wm|
∮
|zi|=1
N∏
j=1
dzj
2πizj
ICSIvect(z,m,q )Iadj(z,m,t,R,q ) (2.36)
=
∑
m1≥···≥mN∈Z
1
|Wm|
∮
|zi|=1
N∏
j=1
dzj
2πizj
N∏
j=1
zpmj
i
×
∏
1≤i⁄=j≤N
t−|mi−mj|/2(−1)|mi−mj|/2q−R|mi−mj|/4(1−q|mi−mj|/2ziz−1
j )
×
∏
1≤i⁄=j≤N
(z−1
i zjt−1q|mi−mj|/2+1−R/2;q)∞
(ziz−1
j tq|mi−mj|/2+R/2;q)∞
((t−1q1−R/2;q)∞
(tqR/2;q)∞
)N
,
(2.37)
which is obtained from (2.5) and (2.6) with R = 2. When G =SU (N),∑N
j=1mj = 0 and∏N
j=1zj = 1 are imposed and the contribution from the Cartan part of the adjoint chiral
multiplet is
(
(t−1q1−R/2;q)∞/(tqR/2;q)∞
)N−1. In particular, when G =SU (2), we have
ISU (2) = 1
2
∑
m∈Z
∮
|z|=1
dz
2πizz2pmt−|2m|q−|2m|(1−q|m|z2)(1−q|m|z−2)
× (z2t−1q|m|+1−R/2;q)∞
(z2tq|m|+R/2;q)∞
(z−2t−1q|m|+1−R/2;q)∞
(z−2tq|m|+R/2;q)∞
((t−1q1−R/2;q)∞
(tqR/2;q)∞
) (2.38)
with R = 2. The G = SU (2) case was studied in the context of homological block in [2].
More speciﬁcally, it was checked that ISU (2) =∑
b|Wb|ˆZb(q,v )ˆZb(˜q,v−1) where ˜q = q−1,
v = t, and ˜v = t−1 as before. The index (2.38) can also be obtained via (2.32). From
these calculations we see that the CS contribution to the index comes only from the theta
function Θp·IdN
b (s;q).
3 Supersymmetric index of a 3d N = 2 theory on S2×q S1 for plumbed
3-manifolds
In this section, we would like to extend the discussion above to the case of plumbed 3-
manifolds. After having an eﬀective description of a 3dN = 2 theoryT [M3] for a plumbing
graph from the homological blocks, we obtain the index ofT [M3] and discuss the invariance
of it under the 3d Kirby moves. We also give some remarks on the topologically twisted
index of T [M3] on S2×qS1.
– 9 –
3.1 Engineering a 3d N = 2 theory T [M3] from homological blocks
We consider the case G =SU (2) with t turned oﬀ. The homological block for a plumbed
3-manifold with G =SU (2) [2, 28] is given by
ˆZb(q) = (−1)πq
1
4 (3σ−∑
vwv) v.p.
∮
|sv|=1
∏
v∈Vertices
dsv
2πisv
(sv−s−1
v )2−deg(v)Θ−M
b (⃗ s) (3.1)
where
Θ−M
b (⃗ s) =
∑
⃗l∈2M ZL+⃗b
q− 1
4 (⃗l,M−1⃗l) ∏
v∈Vertices
slv
v , (3.2)
and v.p. denotes the principle value integration. wv∈ Z is the weight of a vertex v and
L is the number of vertices. M is called the adjacency matrix, which is an L×L matrix,
with diagonal components Mvv = wv. When the vertices v and v′ are connected by an
edge, Mvv′ =Mv′v = 1, and other components of M are zero. π is the number of positive
eigenvalues of M and σ is the signature of the adjacency matrix M, which is the number
of positive eigenvalues minus the number of negative eigenvalues of M. It was shown in
[28] that ˆZb is invariant under the 3d Kirby moves.
The formula (3.1) can also be expressed as
ˆZb(q) = (−1)πq
1
4 (3σ−∑
vwv) v.p.
∮
|sv|=1
∏
v∈Vertices
dsv
2πisv
(sv− 1/sv)2
×
∏
(v1,v2)∈Edges
1
(sv1−s−1v1 )
1
(sv2−s−1v2 )Θ−M
b (⃗ s).
(3.3)
We consider (sv− 1/sv)2−deg(v) factor ﬁrst. When deg( v) = 0, there is only a vertex
without edges. From [1, 2], ( sv−s−1
v )2 is interpreted as the contributions from vector
multiplet V and an adjoint chiral multiplet Φ +
R=2 with R-charge 2 whose U(1)t charge is
+1.
When deg(v)≥ 1 where edges are attached to a vertex v, the exponent of ( sv−s−1
v )
decreases. This would imply that we need to assign supermultiplets to each end of an edge
whose contribution can cancel the contributions from the vector multiplet or the adjoint
chiral multiplet. From (2.31), it is expected that the both ends of the edge are interpreted
as the adjoint chiral multiplets with R-charge 0 where they are charged under the gauge
groups SU (2)v and SU (2)v′ given an edge (v,v′).
In particular, when deg(v) = 2 there is no (sv−s−1
v ) at the vertex v in the integrand.
Therefore, the contribution from the ends of two edges should cancel the contribution from
the vertex. Thus, we would assign the U(1)t charge−1 and 0 to the adjoint chiral multi-
plets at each end of an edge. The reason for such assignment is because the contribution
from Φ−
R=0 cancels the contribution from the adjoint chiral multiplet Φ +
R=2 as they form a
superpotential. The contribution from Φ 0
R=0 can cancel the one from the vector multiplet,
which can be interpreted as the Higgs mechanism [29, 30]. With this assignment of U(1)t
charges, deg(v) = 2 can be realized in the homological block by attaching two diﬀerent
– 10 –
edges in such a way that Φ −
R=0 part of one edge and Φ 0
R=0 part of another edge are at-
tached to the vertex v. At the level of homological block, the boundary condition needs to
be imposed and for a proper cancellation discussed above, Φ −
R=0 and Φ0
R=0 should satisfy
the Dirichlet and the Neumann boundary condition, respectively.
ForM3 =O(−p)→ Σg in [2], T [M3] is given by a vector multiplet with the CS level
p and an adjoint chiral multiplet Φ +
R=2. There are also g pairs of adjoint chiral multiplets
(Φ−
R=0, Φ0
R=0)i, i = 1,··· ,g with R = 0 and U(1)t charge−1 and 0, which correspond
to g loops attached at the vertex whose weight is −p. In addition, the Dirichlet and the
Neumann boundary condition were imposed to Φ−
R=0 and Φ0
R=0, respectively, in [2]. In the
plumbing graph, a loop is basically an edge whose ends attached to the same vertex, so the
case M3 =O(−p)→ Σg seems to indicate that charge assignment above can be regarded
as one of natural choices.
Regarding the theta function, we know from the lens space case with G =U(N) [1, 2]
that
Θp
b(⃗ s;q) =
∑
⃗ n∈pZN+⃗b
q
1
2p
∑N
i=1n2
i
N∏
i=1
sni
i , (3.4)
which is associated to the quadratic form p· IdN, gives the Chern-Simons term with
level p and contributes to the index as ∏N
i=1zpmi
i . By generalizing this to the theta
function Θ−M
b (⃗ s) = ∑
⃗l∈2M ZL+bq− 1
4 (⃗l,M−1⃗l)∏L
i=1sli
i , we see that this provides the mixed
Chern-Simons terms and they contribute to the index as z−2Mv,vmv
v when v = v′ and
(zmv′
v z′mv
v )−2Mv,v′ when v ⁄= v′ where zv,1 = z−1
v,2 = zv and zv is the fugacity for the
U(1)⊂SU (2)v. This implies that the level of the mixed Chern-Simons term is −Mv,v′.
In sum, given a plumbing graph,10 the vertex corresponds to a vector multipletVN with
the Neumann boundary condition and an adjoint chiral multiplet Φ +
R=2,N withR-charge 2
and U(1)t charge +1 and with the Neumann boundary condition. Ends of an edge ( v,v′)
would correspond to the adjoint chiral multiplets, Φ −
R=0,D and Φ 0
R=0,N with R-charge 0
andU(1)t charge−1 and 0, and with the Dirichlet and the Neumann boundary condition,
where they are adjoint under the gauge groups, SU (2)v and SU (2)v′, respectively. The
theta function Θ−M
b (z) cancels the anomaly from mixed Chern-Simons terms with levels
−Mv,v′ and it contributes to the index as Chern-Simons terms with levels −Mv,v′. Since it
10Here, we consider plumbing graphs without loops. For plumbing graphs Γ with loops, which gives
plumbed 3-manifolds with b1 > 0, the homological blocks are also labeled by s∈ Hom(π1(Γ), Z2)∼= Zb1(Γ)
2
and this is encoded in the “twisted linking matrix” Qs in (3.1) with M =Qs [9]. Since the Chern-Simons
level of T [M3] is determined by the adjacency or the linking matrix M, and since there are multiple Qs’s,
this would mean that there are multiple 3dN = 2 theories for a given plumbing graph Γ with loops, which
is not appropriate. Meanwhile, there are some clues that the homological blocks for plumbing graph with
loops or more generally for 3-manifolds withb1 > 0 are expressed as an integral over the continuous variable
[9]. If it is so, such integral expression might be more suitable for ﬁnding T [M3].
– 11 –
mixes v with v′, it could be regarded as the line part of the edge ( v,v′).
Though we will focus on the case that t = 1, we give some remarks on the case that
t is not turned oﬀ. When t⁄= 1, each end of the edge gives diﬀerent contributions. So we
may consider that the edge has information of a direction, for example, with arrow from
Φ0
R=0,N with U(1)t charge 0 to Φ−
R=0,D with U(1)t charge−1. Accordingly, depending on
how we attach the edges to the vertex, the homological block and the index are diﬀerent.
For example, when deg( v) = 1, such a vertex v corresponds to a vector multiplet VN if
the arrow goes in to the vertex. Or if the arrow goes out from the vertex, such a vertex
corresponds to a vector multipletVN with Φ+
R=2,N and Φ0
R=0,N where the contribution only
from Φ+
R=2,N is left in the integrand. This is similar for the vertex with other degrees. But
as will be discussed below, when considering invariance under the 3d Kirby moves, only
certain types of pluming graphs with arrows are allowed when t⁄= 1. So when t is turned
on, there is a limitation, which is one of reasons why we call T [M3] discussed in this paper
as an eﬀective description. We note that when t is set to 1, contributions from Φ −
R=0,D
and Φ0
R=0,N to the index are the same up to an overall factor so we don’t distinguish the
directions of arrows.
We also note that when M3 is a Seifert manifold, which admits a semi-free U(1)
action, there is an additional U(1) global symmetry, which is denoted by U(1)t in this
paper, and it is possible to have the homological block or the supersymmetric index on
S2×qS1 with the homological variable turned on, which is related to t via “homological-
ﬂavor locking” [1, 2, 31]. For general M3 that doesn’t have such an action, there is no U(1)
global symmetry, and a general homological variable other than 1 would not be allowed in
the supersymmetric index [32]. So, in principle, t can be turned on in this work when a
plumbed 3-manifold is a Seifert manifold. But we may just turn on t for the case of general
plumbed 3-manifolds and see what we get.
Anomaly and homological block
When considering a theory on S2×qS1 there wouldn’t be an issue, but when considering
a theory on D2×q S1 anomaly inﬂow should be taken into account. The 3d bulk ﬁelds
and the Chern-Simons term lead to the anomaly inﬂow to the boundary and this must
be canceled by introducing appropriate boundary degrees of freedom. For the case of lens
spacesM3 =L(p, 1), a vector multipletVN and an adjoint chiral multiplet Φ+
R=2,N ofT [M3]
satisfy the Neumann boundary condition, and their boundary anomalies cancel out. Also,
the anomaly from the Chern-Simons term with a level p is canceled by the theta function.
Similarly, for the case ofO(−p)→ Σg, in addition to the cancellation of anomaly discussed
above, boundary anomalies from additional g pairs of Φ−
R=0,D and Φ0
R=0,N satisfying the
Dirichlet and the Neumann boundary condition, respectively, also cancel out.
For plumbed 3-manifolds, the homological block contains (sv−s−1
v )2−d with arbitrary
d≥ 0. We note that ( sv−s−1
v )±1 in (2.27) or (2.31) itself is already anomaly-free, so
there is no issue of anomaly in the formula of homological block for plumbed 3-manifolds
with arbitrary powers of ( sv−s−1
v )±1. But for the interpretation in the context of a 3d-
2d coupled system, we consider, for example, a case that a single edge is attached to a
– 12 –
vertexv where the contribution from such a vertex v contains (sv−s−1
v ) in the integrand,
which can be regarded as the contribution from the vector multiplet. From the previous
calculations, for the vertex with deg( v) = 1, the integrand of homological block at the
vertexv contains a factor whose numerator is (s−2q;q)∞(s2q;q)∞ and whose denominator
is a Jacobi theta function, which can be, for example, θ(−q1/2s−2;q)1/2θ(−q1/2s2;q)1/2 or
s−1θ(−q1/2s−2;q) where their contributions to the index are all the same. Combined with
the numerator, they give sv−s−1
v up to an overall factor. However, contributions from
the 2d boundary degrees of freedom take particular forms of the Jacobi theta function
depending on their representations under the gauge group in the context of Lagrangian 3d-
2d coupled system, and we see that a proper interpretation of, for example, these two Jacobi
theta functions in terms of boundary N = (0, 2) multiplets are not available. Considering
other possibilities, we see that there is no natural candidate for boundary N = (0, 2)
multiplets whose contribution gives rise to (s−s−1)±1.11 Though a proper interpretation
on the boundary degrees of freedom that gives (s−s−1)±1 is not available even whent = 1,
since from the perspective of the index there is no issue on the anomaly due to the absence
of a boundary, the eﬀective description of T [M3] obtained from the formula of homological
block to calculate the index is expected to work ﬁne.
3.2 Index for an eﬀective description of T [M3]
From the calculations above, with t = 1 we would have
plumbing graph homological block index eﬀective description
v∈ vertex ↝ (zv−z−1
v )2 ↝ ‖(zv−z−1
v )‖2
id VN, Φ+
R=2,D
(v1,v 2)∈ edge ↝ (zv1−z−1
v1 )−1(zv2−z−1
v2 )−1↝ ‖(zv1−z−1
v1 )(zv2−z−1
v2 )‖−2
id Φ−
R=0,D, Φ0
R=0,N
−Mv,v′ ↝ Θ−M
b (⃗ s;q) ↝ z−2Mv,vmv
v or (zmv′
v zmv
v′ )−2Mv,v′ CS levels −Mv,v′
(3.5)
The S2×qS1 index is given by
ISU (2) =
∑
m∈Z
∮
|zv|=1
∏
v∈Vertices
dzv
2πizv
‖‖(sv−s−1
v )2‖‖2
idz−2Mv,vmv
v
×
∏
(v1,v2)∈Edges
‖‖‖‖
1
(sv1−s−1v1 )
1
(sv2−s−1v2 )
‖‖‖‖
2
id
(z
mv2
v1 z
mv1
v2 )−2Mv1,v2
(3.6)
up to an overall (log q)∗ factor where s = zqm/2 and ˜s = z−1qm/2. We also chose a
normalization that 2L is multiplied to the standard expression. With t parameter turned
on, the index of an eﬀective description of T [M3] would be given by
ISU (2) =
∑
m∈Z
∮
|zv|=1
∏
v∈Vertices
dzv
2πizv
Ivect(z,m,q )IR=2
adj (z,m,t,q )z−2Mv,vmv
v
×
∏
(v1,v2)∈Edges
IR=0
adj (z,m,t−1,q )IR=0
adj (z,m,q ) (z
mv2
v1 z
mv1
v2 )−2Mv1,v2,
(3.7)
11If we regard every term in the homological block in theU(1) perspective and treat the eﬀective descrip-
tion of T [M3] as U(1) quiver gauge theories, it is possible to have an interpretation as boundary chiral or
Fermi multiplets with desired expression up to an overall factor.
– 13 –
whereIvect(z,m,q ) andIR
adj(z,m,t,q ) are from (2.5) and (2.6), respectively, andIR=0
adj (z,m,q )
is a regularized index (2.18).
Invariance under 3d Kirby moves
We check the invariance of the index under the 3d Kirby moves. We consider the case with
t = 1 and provide remarks on the case of general t.
a1±1
<latexit sha1_base64="tLIz9KmDWFNeB/0/MoTLwLV8pwA=">AAAB8HicbZDLSgMxFIbPtF5qvVVdugm2gqsycaPLghuXFexF2qFk0kwbmmSGJCOUoU/hxoUibn0Kn8GF4NNoello6w+Bj/8/h5xzwkRwY33/y8vl19Y3Ngtbxe2d3b390sFh08SppqxBYxHrdkgME1yxhuVWsHaiGZGhYK1wdDXNW/dMGx6rWztOWCDJQPGIU2KddVchPdxNJK70SmW/6s+EVgEvoFzLf36/A0C9V/ro9mOaSqYsFcSYDvYTG2REW04FmxS7qWEJoSMyYB2Hikhmgmw28ASdOqePoli7pyyaub87MiKNGcvQVUpih2Y5m5r/ZZ3URpdBxlWSWqbo/KMoFcjGaLo96nPNqBVjB4Rq7mZFdEg0odbdqOiOgJdXXoXmeRX7VXyDyzUf5irAMZzAGWC4gBpcQx0aQEHCAzzBs6e9R+/Fe52X5rxFzxH8kff2AzGfkjo=</latexit><latexit sha1_base64="L6eoQIBnoZ3seAZ58D5RJWtRVnM=">AAAB8HicbVBNSwMxEJ2tX7V+VT16CbaCp7LxoseCF48V7Ie0S8mm2TY0yS5JVihLf4UXD4p49ed489+YbvegrQ8GHu/NMDMvTAQ31ve/vdLG5tb2Tnm3srd/cHhUPT7pmDjVlLVpLGLdC4lhgivWttwK1ks0IzIUrBtObxd+94lpw2P1YGcJCyQZKx5xSqyTHutkiAeJxPVhteY3/BxoneCC1KBAa1j9GoximkqmLBXEmD72ExtkRFtOBZtXBqlhCaFTMmZ9RxWRzARZfvAcXThlhKJYu1IW5erviYxIY2YydJ2S2IlZ9Rbif14/tdFNkHGVpJYpulwUpQLZGC2+RyOuGbVi5gihmrtbEZ0QTah1GVVcCHj15XXSuWpgv4Hvca3pF3GU4QzO4RIwXEMT7qAFbaAg4Rle4c3T3ov37n0sW0teMXMKf+B9/gBbb49i</latexit>
a1±1
<latexit sha1_base64="tLIz9KmDWFNeB/0/MoTLwLV8pwA=">AAAB8HicbZDLSgMxFIbPtF5qvVVdugm2gqsycaPLghuXFexF2qFk0kwbmmSGJCOUoU/hxoUibn0Kn8GF4NNoello6w+Bj/8/h5xzwkRwY33/y8vl19Y3Ngtbxe2d3b390sFh08SppqxBYxHrdkgME1yxhuVWsHaiGZGhYK1wdDXNW/dMGx6rWztOWCDJQPGIU2KddVchPdxNJK70SmW/6s+EVgEvoFzLf36/A0C9V/ro9mOaSqYsFcSYDvYTG2REW04FmxS7qWEJoSMyYB2Hikhmgmw28ASdOqePoli7pyyaub87MiKNGcvQVUpih2Y5m5r/ZZ3URpdBxlWSWqbo/KMoFcjGaLo96nPNqBVjB4Rq7mZFdEg0odbdqOiOgJdXXoXmeRX7VXyDyzUf5irAMZzAGWC4gBpcQx0aQEHCAzzBs6e9R+/Fe52X5rxFzxH8kff2AzGfkjo=</latexit><latexit sha1_base64="L6eoQIBnoZ3seAZ58D5RJWtRVnM=">AAAB8HicbVBNSwMxEJ2tX7V+VT16CbaCp7LxoseCF48V7Ie0S8mm2TY0yS5JVihLf4UXD4p49ed489+YbvegrQ8GHu/NMDMvTAQ31ve/vdLG5tb2Tnm3srd/cHhUPT7pmDjVlLVpLGLdC4lhgivWttwK1ks0IzIUrBtObxd+94lpw2P1YGcJCyQZKx5xSqyTHutkiAeJxPVhteY3/BxoneCC1KBAa1j9GoximkqmLBXEmD72ExtkRFtOBZtXBqlhCaFTMmZ9RxWRzARZfvAcXThlhKJYu1IW5erviYxIY2YydJ2S2IlZ9Rbif14/tdFNkHGVpJYpulwUpQLZGC2+RyOuGbVi5gihmrtbEZ0QTah1GVVcCHj15XXSuWpgv4Hvca3pF3GU4QzO4RIwXEMT7qAFbaAg4Rle4c3T3ov37n0sW0teMXMKf+B9/gBbb49i</latexit>
±1
<latexit sha1_base64="8mse9ySRTWCKJoO23tXvazpx330=">AAAB7nicbZDLSgMxFIbP1Futt6pLN8FWcFVm3OjOghuXFewF2qFk0kwbmmRCkhHK0Idw40Ipbn0ed76IazNtF9r6Q+Dj/88h55xIcWas7395hY3Nre2d4m5pb//g8Kh8fNIySaoJbZKEJ7oTYUM5k7RpmeW0ozTFIuK0HY3v8rz9RLVhiXy0E0VDgYeSxYxg66x2tacECqr9csWv+XOhdQiWULn9nkGuRr/82RskJBVUWsKxMd3AVzbMsLaMcDot9VJDFSZjPKRdhxILasJsPu4UXThngOJEuyctmru/OzIsjJmIyFUKbEdmNcvN/7JuauObMGNSpZZKsvgoTjmyCcp3RwOmKbF84gATzdysiIywxsS6C5XcEYLVldehdVUL/FrwEFTqPixUhDM4h0sI4BrqcA8NaAKBMTzDK7x5ynvxZt77orTgLXtO4Y+8jx9He5BP</latexit><latexit sha1_base64="QKnKO0RACm3FgLNrawfPWYfs0XI=">AAAB7nicbVBNSwMxEJ31s9avqkcvwVbwVDZe9Fjw4rGC/YB2Kdk024Ym2ZBkhbL0R3jxoIhXf483/41puwdtfTDweG+GmXmxFty6MPwONja3tnd2S3vl/YPDo+PKyWnbppmhrEVTkZpuTCwTXLGW406wrjaMyFiwTjy5m/udJ2YsT9Wjm2oWSTJSPOGUOC91an0tEa4NKtWwHi6A1gkuSBUKNAeVr/4wpZlkylFBrO3hULsoJ8ZxKtis3M8s04ROyIj1PFVEMhvli3Nn6NIrQ5SkxpdyaKH+nsiJtHYqY98piRvbVW8u/uf1MpfcRjlXOnNM0eWiJBPIpWj+Oxpyw6gTU08INdzfiuiYGEKdT6jsQ8CrL6+T9nUdh3X8gKuNsIijBOdwAVeA4QYacA9NaAGFCTzDK7wFOngJ3oOPZetGUMycwR8Enz/QBo59</latexit>
±1
<latexit sha1_base64="8mse9ySRTWCKJoO23tXvazpx330=">AAAB7nicbZDLSgMxFIbP1Futt6pLN8FWcFVm3OjOghuXFewF2qFk0kwbmmRCkhHK0Idw40Ipbn0ed76IazNtF9r6Q+Dj/88h55xIcWas7395hY3Nre2d4m5pb//g8Kh8fNIySaoJbZKEJ7oTYUM5k7RpmeW0ozTFIuK0HY3v8rz9RLVhiXy0E0VDgYeSxYxg66x2tacECqr9csWv+XOhdQiWULn9nkGuRr/82RskJBVUWsKxMd3AVzbMsLaMcDot9VJDFSZjPKRdhxILasJsPu4UXThngOJEuyctmru/OzIsjJmIyFUKbEdmNcvN/7JuauObMGNSpZZKsvgoTjmyCcp3RwOmKbF84gATzdysiIywxsS6C5XcEYLVldehdVUL/FrwEFTqPixUhDM4h0sI4BrqcA8NaAKBMTzDK7x5ynvxZt77orTgLXtO4Y+8jx9He5BP</latexit><latexit sha1_base64="QKnKO0RACm3FgLNrawfPWYfs0XI=">AAAB7nicbVBNSwMxEJ31s9avqkcvwVbwVDZe9Fjw4rGC/YB2Kdk024Ym2ZBkhbL0R3jxoIhXf483/41puwdtfTDweG+GmXmxFty6MPwONja3tnd2S3vl/YPDo+PKyWnbppmhrEVTkZpuTCwTXLGW406wrjaMyFiwTjy5m/udJ2YsT9Wjm2oWSTJSPOGUOC91an0tEa4NKtWwHi6A1gkuSBUKNAeVr/4wpZlkylFBrO3hULsoJ8ZxKtis3M8s04ROyIj1PFVEMhvli3Nn6NIrQ5SkxpdyaKH+nsiJtHYqY98piRvbVW8u/uf1MpfcRjlXOnNM0eWiJBPIpWj+Oxpyw6gTU08INdzfiuiYGEKdT6jsQ8CrL6+T9nUdh3X8gKuNsIijBOdwAVeA4QYacA9NaAGFCTzDK7wFOngJ3oOPZetGUMycwR8Enz/QBo59</latexit>
a2±1
<latexit sha1_base64="QBuU1QnsfI2QRIqtWHacvutSmLc=">AAAB8XicbZDLSgMxFIbPWC+13qou3QRbwVWZdKPLghuXFewF26Fk0kwbmmSGJCOUoW/hxoUibn0Jn8GF4NNoello6w+Bj/8/h5xzwkRwY33/y1vLrW9sbuW3Czu7e/sHxcOjpolTTVmDxiLW7ZAYJrhiDcutYO1EMyJDwVrh6Gqat+6ZNjxWt3acsECSgeIRp8Q6665MetVuIhEu94olv+LPhFYBL6BUy31+vwNAvVf86PZjmkqmLBXEmA72ExtkRFtOBZsUuqlhCaEjMmAdh4pIZoJsNvEEnTmnj6JYu6csmrm/OzIijRnL0FVKYodmOZua/2Wd1EaXQcZVklqm6PyjKBXIxmi6PupzzagVYweEau5mRXRINKHWHangjoCXV16FZrWC/Qq+waWaD3Pl4QRO4RwwXEANrqEODaCg4AGe4Nkz3qP34r3OS9e8Rc8x/JH39gOLK5Jl</latexit><latexit sha1_base64="MoUeaT7rHe3reaJoJiiyQ/g2kgk=">AAAB8XicbVBNTwIxEJ3FL8Qv1KOXRjDxRLZc8EjixSMm8hFhQ7qlCw1td9N2TciGf+HFg8Z49d94899YYA8KvmSSl/dmMjMvTAQ31ve/vcLW9s7uXnG/dHB4dHxSPj3rmDjVlLVpLGLdC4lhgivWttwK1ks0IzIUrBtObxd+94lpw2P1YGcJCyQZKx5xSqyTHqtkWB8kEuHqsFzxa/4SaJPgnFQgR2tY/hqMYppKpiwVxJg+9hMbZERbTgWblwapYQmhUzJmfUcVkcwE2fLiObpyyghFsXalLFqqvycyIo2ZydB1SmInZt1biP95/dRGN0HGVZJapuhqUZQKZGO0eB+NuGbUipkjhGrubkV0QjSh1oVUciHg9Zc3Sadew34N3+NK08/jKMIFXMI1YGhAE+6gBW2goOAZXuHNM96L9+59rFoLXj5zDn/gff4AtPuPjQ==</latexit>
a2±1
<latexit sha1_base64="QBuU1QnsfI2QRIqtWHacvutSmLc=">AAAB8XicbZDLSgMxFIbPWC+13qou3QRbwVWZdKPLghuXFewF26Fk0kwbmmSGJCOUoW/hxoUibn0Jn8GF4NNoello6w+Bj/8/h5xzwkRwY33/y1vLrW9sbuW3Czu7e/sHxcOjpolTTVmDxiLW7ZAYJrhiDcutYO1EMyJDwVrh6Gqat+6ZNjxWt3acsECSgeIRp8Q6665MetVuIhEu94olv+LPhFYBL6BUy31+vwNAvVf86PZjmkqmLBXEmA72ExtkRFtOBZsUuqlhCaEjMmAdh4pIZoJsNvEEnTmnj6JYu6csmrm/OzIijRnL0FVKYodmOZua/2Wd1EaXQcZVklqm6PyjKBXIxmi6PupzzagVYweEau5mRXRINKHWHangjoCXV16FZrWC/Qq+waWaD3Pl4QRO4RwwXEANrqEODaCg4AGe4Nkz3qP34r3OS9e8Rc8x/JH39gOLK5Jl</latexit><latexit sha1_base64="MoUeaT7rHe3reaJoJiiyQ/g2kgk=">AAAB8XicbVBNTwIxEJ3FL8Qv1KOXRjDxRLZc8EjixSMm8hFhQ7qlCw1td9N2TciGf+HFg8Z49d94899YYA8KvmSSl/dmMjMvTAQ31ve/vcLW9s7uXnG/dHB4dHxSPj3rmDjVlLVpLGLdC4lhgivWttwK1ks0IzIUrBtObxd+94lpw2P1YGcJCyQZKx5xSqyTHqtkWB8kEuHqsFzxa/4SaJPgnFQgR2tY/hqMYppKpiwVxJg+9hMbZERbTgWblwapYQmhUzJmfUcVkcwE2fLiObpyyghFsXalLFqqvycyIo2ZydB1SmInZt1biP95/dRGN0HGVZJapuhqUZQKZGO0eB+NuGbUipkjhGrubkV0QjSh1oVUciHg9Zc3Sadew34N3+NK08/jKMIFXMI1YGhAE+6gBW2goOAZXuHNM96L9+59rFoLXj5zDn/gff4AtPuPjQ==</latexit>
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
a2
<latexit sha1_base64="VuNU+xmx+vqlDxS1FqmmTFntG8M=">AAAB7HicbZC7SgNBFIbPJl5ivEUtbQYTwSrsptEyYGMZwU0CSQhnJ7PJkNnZZWZWCEuewcZCEVufw2ewEHwanVwKTfxh4OP/z2HOOUEiuDau++Xk8hubW9uFneLu3v7BYenouKnjVFHm01jEqh2gZoJL5htuBGsnimEUCNYKxtezvHXPlOaxvDOThPUiHEoecorGWn4F+7VKv1R2q+5cZB28JZTr+c/vdwBo9Esf3UFM04hJQwVq3fHcxPQyVIZTwabFbqpZgnSMQ9axKDFiupfNh52Sc+sMSBgr+6Qhc/d3R4aR1pMosJURmpFezWbmf1knNeFVL+MySQ2TdPFRmApiYjLbnAy4YtSIiQWkittZCR2hQmrsfYr2CN7qyuvQrFU9t+rdeuW6CwsV4BTO4AI8uIQ63EADfKDA4QGe4NmRzqPz4rwuSnPOsucE/sh5+wFydJCp</latexit><latexit sha1_base64="4prNiupZVD6U9ihhFk3Er8Su1fk=">AAAB7HicbVBNT8JAEJ3iF+IX6tHLRjDxRFoueiTx4hETCyTQkOmyhQ3bbbO7NSENv8GLB43x6g/y5r9xgR4UfMkkL+/NZGZemAqujet+O6Wt7Z3dvfJ+5eDw6PikenrW0UmmKPNpIhLVC1EzwSXzDTeC9VLFMA4F64bTu4XffWJK80Q+mlnKghjHkkecorGSX8dhsz6s1tyGuwTZJF5BalCgPax+DUYJzWImDRWodd9zUxPkqAyngs0rg0yzFOkUx6xvqcSY6SBfHjsnV1YZkShRtqQhS/X3RI6x1rM4tJ0xmole9xbif14/M9FtkHOZZoZJuloUZYKYhCw+JyOuGDViZglSxe2thE5QITU2n4oNwVt/eZN0mg3PbXgPXq3lFnGU4QIu4Ro8uIEW3EMbfKDA4Rle4c2Rzovz7nysWktOMXMOf+B8/gCcRI3R</latexit>
a2
<latexit sha1_base64="VuNU+xmx+vqlDxS1FqmmTFntG8M=">AAAB7HicbZC7SgNBFIbPJl5ivEUtbQYTwSrsptEyYGMZwU0CSQhnJ7PJkNnZZWZWCEuewcZCEVufw2ewEHwanVwKTfxh4OP/z2HOOUEiuDau++Xk8hubW9uFneLu3v7BYenouKnjVFHm01jEqh2gZoJL5htuBGsnimEUCNYKxtezvHXPlOaxvDOThPUiHEoecorGWn4F+7VKv1R2q+5cZB28JZTr+c/vdwBo9Esf3UFM04hJQwVq3fHcxPQyVIZTwabFbqpZgnSMQ9axKDFiupfNh52Sc+sMSBgr+6Qhc/d3R4aR1pMosJURmpFezWbmf1knNeFVL+MySQ2TdPFRmApiYjLbnAy4YtSIiQWkittZCR2hQmrsfYr2CN7qyuvQrFU9t+rdeuW6CwsV4BTO4AI8uIQ63EADfKDA4QGe4NmRzqPz4rwuSnPOsucE/sh5+wFydJCp</latexit><latexit sha1_base64="4prNiupZVD6U9ihhFk3Er8Su1fk=">AAAB7HicbVBNT8JAEJ3iF+IX6tHLRjDxRFoueiTx4hETCyTQkOmyhQ3bbbO7NSENv8GLB43x6g/y5r9xgR4UfMkkL+/NZGZemAqujet+O6Wt7Z3dvfJ+5eDw6PikenrW0UmmKPNpIhLVC1EzwSXzDTeC9VLFMA4F64bTu4XffWJK80Q+mlnKghjHkkecorGSX8dhsz6s1tyGuwTZJF5BalCgPax+DUYJzWImDRWodd9zUxPkqAyngs0rg0yzFOkUx6xvqcSY6SBfHjsnV1YZkShRtqQhS/X3RI6x1rM4tJ0xmole9xbif14/M9FtkHOZZoZJuloUZYKYhCw+JyOuGDViZglSxe2thE5QITU2n4oNwVt/eZN0mg3PbXgPXq3lFnGU4QIu4Ro8uIEW3EMbfKDA4Rle4c2Rzovz7nysWktOMXMOf+B8/gCcRI3R</latexit>
Figure 1: 3d Kirby move 1
We begin with the move (··· ,a 1,a 2,··· )↔ (··· ,a 1± 1,±1,a 2± 1,··· ), which we call
the move 1 (Fig. 1). In the parentheses, ··· denotes arbitrary vertices and edges on the
LHS/RHS, which we will omit for notational convenience. For (a1±1,±1,a 2±1), we label
their vertices as v1, v0, and v2. Since deg(v0) = 2 at the vertex v0, the contributions from
supermultiplets vanish and only Chern-Simons contributions remain. Contributions from
Chern-Simons terms for (a1− 1,−1,a 2− 1) are given by
z−2(a1−1)m1
1 (zm1
0 zm0
1 )−2z2m0
0 (zm2
0 zm0
2 )−2z−2(a2−1)m2
2 (3.8)
and z0 part is z2(m0−m1−m2)
0 . Then the residue integral for z0 picks the condition m0 =
m1 +m2 and we obtain z−2a1m1
1 (zm2
1 zm1
2 )−2z−2a2m2
2 from (3.8). This correctly produces
the Chern-Simons contribution of (a1,a 2) with other parts untouched.
For (a1 + 1, +1,a 2 + 1), we proceed similarly. The Chern-Simons contributions in this
case are
z−2(a1+1)m1
1 (zm1
0 zm0
1 )−2z−2m0
0 (zm2
0 zm0
2 )−2z−2(a2+1)m2
2 (3.9)
and after the similar calculation we have
z−2a1m1
1 (zm2
1 zm1
2 )2z−2a2m2
2 . (3.10)
Taking the change of variables z2→ z−1
2 and m2→− m2, the other parts stay the same.
Therefore, from (3.10) with the change of variables, we obtain z−2a1m1
1 (zm2
1 zm1
2 )−2z−2a2m2
2 ,
which is the Chern-Simons contribution of (a1,a 2) while other parts stay the same. Hence,
the index is invariant under the move 1.
When t is general, the discussion above also holds if an arrow goes in to and another
arrow goes out from the vertexv0 so that the contribution from supermultiplets is empty at
v0 and only the contributions from Chern-Simons term remain as in the case oft = 1. Thus,
– 14 –
a1±1
<latexit sha1_base64="tQW9wpvwxhn3bTuiTizqwxPLcws=">AAAB8nicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCvYC06Fk0kwbmmSGJCOUoY/hxoUibn0In8GF4NNoello6w+Bj/8/h5xzolRwY33/y1srrG9sbhW3Szu7e/sH5cOjlkkyTVmTJiLRnYgYJrhiTcutYJ1UMyIjwdrR6Hqat++ZNjxRd3acslCSgeIxp8Q6K6iSHkbdVCJc7ZUrfs2fCa0CXkClXvj8fgeARq/80e0nNJNMWSqIMQH2UxvmRFtOBZuUuplhKaEjMmCBQ0UkM2E+G3mCzpzTR3Gi3VMWzdzfHTmRxoxl5ColsUOznE3N/7Igs/FVmHOVZpYpOv8ozgSyCZruj/pcM2rF2AGhmrtZER0STah1Vyq5I+DllVehdVHDfg3f4krdh7mKcAKncA4YLqEON9CAJlBI4AGe4Nmz3qP34r3OS9e8Rc8x/JH39gPg7JKO</latexit><latexit sha1_base64="eB3eSsv3yc06R4rlFXZvIWYSEQs=">AAAB8nicbVDLSgNBEOz1GeMr6tHLYCJ4Cjte9Bjw4jGCecBmCbOTSTJkHsvMrBCWfIYXD4p49Wu8+TdOkj1oYkFDUdVNd1eSCm5dGH4HG5tb2zu7pb3y/sHh0XHl5LRtdWYoa1EttOkmxDLBFWs57gTrpoYRmQjWSSZ3c7/zxIzlWj26acpiSUaKDzklzktRjfQx6qUS4Vq/Ug3r4QJoneCCVKFAs1/56g00zSRTjgpibYTD1MU5MY5TwWblXmZZSuiEjFjkqSKS2ThfnDxDl14ZoKE2vpRDC/X3RE6ktVOZ+E5J3NiuenPxPy/K3PA2zrlKM8cUXS4aZgI5jeb/owE3jDox9YRQw/2tiI6JIdT5lMo+BLz68jppX9dxWMcPuNoIizhKcA4XcAUYbqAB99CEFlDQ8Ayv8Ba44CV4Dz6WrRtBMXMGfxB8/gAKy4+2</latexit>
a1±1
<latexit sha1_base64="tQW9wpvwxhn3bTuiTizqwxPLcws=">AAAB8nicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCvYC06Fk0kwbmmSGJCOUoY/hxoUibn0In8GF4NNoello6w+Bj/8/h5xzolRwY33/y1srrG9sbhW3Szu7e/sH5cOjlkkyTVmTJiLRnYgYJrhiTcutYJ1UMyIjwdrR6Hqat++ZNjxRd3acslCSgeIxp8Q6K6iSHkbdVCJc7ZUrfs2fCa0CXkClXvj8fgeARq/80e0nNJNMWSqIMQH2UxvmRFtOBZuUuplhKaEjMmCBQ0UkM2E+G3mCzpzTR3Gi3VMWzdzfHTmRxoxl5ColsUOznE3N/7Igs/FVmHOVZpYpOv8ozgSyCZruj/pcM2rF2AGhmrtZER0STah1Vyq5I+DllVehdVHDfg3f4krdh7mKcAKncA4YLqEON9CAJlBI4AGe4Nmz3qP34r3OS9e8Rc8x/JH39gPg7JKO</latexit><latexit sha1_base64="eB3eSsv3yc06R4rlFXZvIWYSEQs=">AAAB8nicbVDLSgNBEOz1GeMr6tHLYCJ4Cjte9Bjw4jGCecBmCbOTSTJkHsvMrBCWfIYXD4p49Wu8+TdOkj1oYkFDUdVNd1eSCm5dGH4HG5tb2zu7pb3y/sHh0XHl5LRtdWYoa1EttOkmxDLBFWs57gTrpoYRmQjWSSZ3c7/zxIzlWj26acpiSUaKDzklzktRjfQx6qUS4Vq/Ug3r4QJoneCCVKFAs1/56g00zSRTjgpibYTD1MU5MY5TwWblXmZZSuiEjFjkqSKS2ThfnDxDl14ZoKE2vpRDC/X3RE6ktVOZ+E5J3NiuenPxPy/K3PA2zrlKM8cUXS4aZgI5jeb/owE3jDox9YRQw/2tiI6JIdT5lMo+BLz68jppX9dxWMcPuNoIizhKcA4XcAUYbqAB99CEFlDQ8Ayv8Ba44CV4Dz6WrRtBMXMGfxB8/gAKy4+2</latexit>
±1
<latexit sha1_base64="8mse9ySRTWCKJoO23tXvazpx330=">AAAB7nicbZDLSgMxFIbP1Futt6pLN8FWcFVm3OjOghuXFewF2qFk0kwbmmRCkhHK0Idw40Ipbn0ed76IazNtF9r6Q+Dj/88h55xIcWas7395hY3Nre2d4m5pb//g8Kh8fNIySaoJbZKEJ7oTYUM5k7RpmeW0ozTFIuK0HY3v8rz9RLVhiXy0E0VDgYeSxYxg66x2tacECqr9csWv+XOhdQiWULn9nkGuRr/82RskJBVUWsKxMd3AVzbMsLaMcDot9VJDFSZjPKRdhxILasJsPu4UXThngOJEuyctmru/OzIsjJmIyFUKbEdmNcvN/7JuauObMGNSpZZKsvgoTjmyCcp3RwOmKbF84gATzdysiIywxsS6C5XcEYLVldehdVUL/FrwEFTqPixUhDM4h0sI4BrqcA8NaAKBMTzDK7x5ynvxZt77orTgLXtO4Y+8jx9He5BP</latexit><latexit sha1_base64="QKnKO0RACm3FgLNrawfPWYfs0XI=">AAAB7nicbVBNSwMxEJ31s9avqkcvwVbwVDZe9Fjw4rGC/YB2Kdk024Ym2ZBkhbL0R3jxoIhXf483/41puwdtfTDweG+GmXmxFty6MPwONja3tnd2S3vl/YPDo+PKyWnbppmhrEVTkZpuTCwTXLGW406wrjaMyFiwTjy5m/udJ2YsT9Wjm2oWSTJSPOGUOC91an0tEa4NKtWwHi6A1gkuSBUKNAeVr/4wpZlkylFBrO3hULsoJ8ZxKtis3M8s04ROyIj1PFVEMhvli3Nn6NIrQ5SkxpdyaKH+nsiJtHYqY98piRvbVW8u/uf1MpfcRjlXOnNM0eWiJBPIpWj+Oxpyw6gTU08INdzfiuiYGEKdT6jsQ8CrL6+T9nUdh3X8gKuNsIijBOdwAVeA4QYacA9NaAGFCTzDK7wFOngJ3oOPZetGUMycwR8Enz/QBo59</latexit>
±1
<latexit sha1_base64="8mse9ySRTWCKJoO23tXvazpx330=">AAAB7nicbZDLSgMxFIbP1Futt6pLN8FWcFVm3OjOghuXFewF2qFk0kwbmmRCkhHK0Idw40Ipbn0ed76IazNtF9r6Q+Dj/88h55xIcWas7395hY3Nre2d4m5pb//g8Kh8fNIySaoJbZKEJ7oTYUM5k7RpmeW0ozTFIuK0HY3v8rz9RLVhiXy0E0VDgYeSxYxg66x2tacECqr9csWv+XOhdQiWULn9nkGuRr/82RskJBVUWsKxMd3AVzbMsLaMcDot9VJDFSZjPKRdhxILasJsPu4UXThngOJEuyctmru/OzIsjJmIyFUKbEdmNcvN/7JuauObMGNSpZZKsvgoTjmyCcp3RwOmKbF84gATzdysiIywxsS6C5XcEYLVldehdVUL/FrwEFTqPixUhDM4h0sI4BrqcA8NaAKBMTzDK7x5ynvxZt77orTgLXtO4Y+8jx9He5BP</latexit><latexit sha1_base64="QKnKO0RACm3FgLNrawfPWYfs0XI=">AAAB7nicbVBNSwMxEJ31s9avqkcvwVbwVDZe9Fjw4rGC/YB2Kdk024Ym2ZBkhbL0R3jxoIhXf483/41puwdtfTDweG+GmXmxFty6MPwONja3tnd2S3vl/YPDo+PKyWnbppmhrEVTkZpuTCwTXLGW406wrjaMyFiwTjy5m/udJ2YsT9Wjm2oWSTJSPOGUOC91an0tEa4NKtWwHi6A1gkuSBUKNAeVr/4wpZlkylFBrO3hULsoJ8ZxKtis3M8s04ROyIj1PFVEMhvli3Nn6NIrQ5SkxpdyaKH+nsiJtHYqY98piRvbVW8u/uf1MpfcRjlXOnNM0eWiJBPIpWj+Oxpyw6gTU08INdzfiuiYGEKdT6jsQ8CrL6+T9nUdh3X8gKuNsIijBOdwAVeA4QYacA9NaAGFCTzDK7wFOngJ3oOPZetGUMycwR8Enz/QBo59</latexit>
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
Figure 2: 3d Kirby move 2
for this particular assignment of arrows, the reﬁned index is also invariant under the move 1.
We consider the move ( a1± 1,±1)↔ (a1), which we call the move 2 (Fig. 2). We
label the vertices in the plumbing graph ( a1± 1,±1) as v1 and v0. The Chern-Simons
contributions of (a1− 1,−1) are given by
z−2a1m1
1 (z0z−1
1 )2(m0−m1) (3.11)
At the vertex v0, other than the Chern-Simons contributions, there is also ‖s0−s−1
0 ‖2
id =
qm0 +q−m0−z2
0−z−2
0 . So we perform a residue calculation for
z−2a1m1
1 (z0z−1
1 )2(m0−m1)(qm0 +q−m0−z2
0−z−2
0 ). (3.12)
Forqm0z2(m0−m1)
0 part, the residue integral gives qm1z−2a1m1
1 . Similarly, for z2
0z2(m0−m1)
0
part, we have z2
1z−2a1m1
1 . In general, in this move, the residue calculation for z2l
0 z2(m0−m1)
0
givesz2l
1 z−2a1m1
1 in (3.12). After calculation, we havez−2a1m1
1 ‖(s1−s−1
1 )‖2
id, which correctly
gives the integrand at v1 of (a1) because deg(v1) at v1 is supplemented by +1 from‖(s1−
s−1
1 )‖2
id, which is lost when attaching an edge to ( a1) to make (a1− 1,−1).
The Chern-Simons contributions of (a1 + 1, +1) are given by
z−2a1m1
1 (z0z1)−2(m0+m1) (3.13)
and there is also‖s0−s−1
0 ‖2
id atv0. A similar calculation forq±m0z−2(m0+m1)
0 andz2l
0 z−2(m0+m1)
0
giveq∓m1z−2a1m1
1 and z−2l
1 z−2a1m1
1 , respectively. Therefore, we have z−2a1m1
1 ‖s1−s−1
1 ‖2
id,
which is a desired result. Therefore, the index above is invariant under the move 2.
Ift is turned on, the invariance holds when the direction of the arrow is from v1 tov0,
which gives a similar setup as in the case of t = 1 above.
We also consider, for example, a sequence of moves that restricts the possible plumbing
graphs with arrows. We consider a setup that a vertexv0 of a weightwv0 = 0 is attached to
three edges, deg(v0) = 3, and at least one of three vertices, sayv3, has degree 1, deg(v3) = 1
with a weight wv3 = +1. We denote other weights by wv1 = a1 and wv2 = a2. Suppose
that all arrows goes from v0 to all other three vertices. Then from the move 2 for the edge
(v0,v 3), the original plumbing graph P becomes a plumbing graph P′ with deg(v0) = 2
and wv0 =−1, and now there is no vertex v3. The conﬁguration of P′ without arrows
allows the move 1, which would give ( wv1,wv0,wv2) = (a1,−1,a 2)→ (a1 + 1,a 2 + 1) if t
– 15 –
were turned oﬀ, but since both arrows go out from v0, it is not invariant under the move
1. For such a conﬁguration, directions of arrows need to be aligned in such a way that
the reﬁned index is invariant under a sequence of moves. For example, if the direction of
the arrow for (v0,v 2) is reversed, the reﬁned index is also invariant under the move 1. Or
putting diﬀerently, only certain types of plumbing graphs with arrows are allowed for the
reﬁned index to be a topological invariant.
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
a1
<latexit sha1_base64="+BVFtEoN1suIHyD9naOmZZY/Bug=">AAAB7HicbZDLSgMxFIbPWC+13qou3QRbwVWZuNFlwY3LCk5baIeSSTNtaJIZkoxQhj6DGxeKuPU5fAYXgk+j6WWhrT8EPv7/HHLOiVLBjfX9L2+tsL6xuVXcLu3s7u0flA+PmibJNGUBTUSi2xExTHDFAsutYO1UMyIjwVrR6Hqat+6ZNjxRd3acslCSgeIxp8Q6K6iSHq72yhW/5s+EVgEvoFIvfH6/A0CjV/7o9hOaSaYsFcSYDvZTG+ZEW04Fm5S6mWEpoSMyYB2Hikhmwnw27ASdOaeP4kS7pyyaub87ciKNGcvIVUpih2Y5m5r/ZZ3MxldhzlWaWabo/KM4E8gmaLo56nPNqBVjB4Rq7mZFdEg0odbdp+SOgJdXXoXmRQ37NXyLK3Uf5irCCZzCOWC4hDrcQAMCoMDhAZ7g2VPeo/fivc5L17xFzzH8kff2A3DvkKg=</latexit><latexit sha1_base64="BZZa/cxkoBAlEUaLOVjuwJRNLWI=">AAAB7HicbVA9TwJBEJ3zE/ELtbTZCCZW5NZGSxIbS0w8IIELmVsW2LC3d9ndMyEXfoONhcbY+oPs/DcucIWCL5nk5b2ZzMyLUimM9f1vb2Nza3tnt7RX3j84PDqunJy2TJJpxgOWyER3IjRcCsUDK6zknVRzjCPJ29Hkbu63n7g2IlGPdpryMMaREkPB0DopqGGf1vqVql/3FyDrhBakCgWa/cpXb5CwLObKMonGdKmf2jBHbQWTfFbuZYanyCY44l1HFcbchPni2Bm5dMqADBPtSlmyUH9P5BgbM40j1xmjHZtVby7+53UzO7wNc6HSzHLFlouGmSQ2IfPPyUBozqycOoJMC3crYWPUyKzLp+xCoKsvr5PWdZ36dfpAqw2/iKME53ABV0DhBhpwD00IgIGAZ3iFN095L96797Fs3fCKmTP4A+/zB5q/jdA=</latexit>
0
<latexit sha1_base64="D8unj5TQx8IFzsiwHQu2r0sEtg8=">AAAB6nicbZDLSgMxFIbP1Futt6pLN8FWcFUybnRnwY3LivYC7VAyaaYNTTJDkhHq0Edw40IRtz6CT+LOpW9iello6w+Bj/8/h5xzwkRwYzH+8nIrq2vrG/nNwtb2zu5ecf+gYeJUU1ansYh1KySGCa5Y3XIrWCvRjMhQsGY4vJrkzXumDY/VnR0lLJCkr3jEKbHOui3jcrdYwhU8FVoGfw6ly4+H7yoA1LrFz04vpqlkylJBjGn7OLFBRrTlVLBxoZMalhA6JH3WdqiIZCbIpqOO0YlzeiiKtXvKoqn7uyMj0piRDF2lJHZgFrOJ+V/WTm10EWRcJallis4+ilKBbIwme6Me14xaMXJAqOZuVkQHRBNq3XUK7gj+4srL0Dir+Lji3/ilKoaZ8nAEx3AKPpxDFa6hBnWg0IdHeIYXT3hP3qv3NivNefOeQ/gj7/0HnhqPiQ==</latexit><latexit sha1_base64="vtiDjf6o0mQdgUQPkFzMP7pc4Dk=">AAAB6nicbVA9SwNBEJ2LXzF+RS1tFhPBKuzZaBmwsYxoPiA5wt5mkizZ2zt294Rw5CfYWChi6y+y89+4Sa7QxAcDj/dmmJkXJlIYS+m3V9jY3NreKe6W9vYPDo/KxyctE6eaY5PHMtadkBmUQmHTCiuxk2hkUSixHU5u5377CbURsXq00wSDiI2UGArOrJMeqrTaL1dojS5A1omfkwrkaPTLX71BzNMIleWSGdP1aWKDjGkruMRZqZcaTBifsBF2HVUsQhNki1Nn5MIpAzKMtStlyUL9PZGxyJhpFLrOiNmxWfXm4n9eN7XDmyATKkktKr5cNEwlsTGZ/00GQiO3cuoI41q4WwkfM824demUXAj+6svrpHVV82nNv/crdZrHUYQzOIdL8OEa6nAHDWgChxE8wyu8edJ78d69j2VrwctnTuEPvM8fKjCM+w==</latexit>
0
<latexit sha1_base64="D8unj5TQx8IFzsiwHQu2r0sEtg8=">AAAB6nicbZDLSgMxFIbP1Futt6pLN8FWcFUybnRnwY3LivYC7VAyaaYNTTJDkhHq0Edw40IRtz6CT+LOpW9iello6w+Bj/8/h5xzwkRwYzH+8nIrq2vrG/nNwtb2zu5ecf+gYeJUU1ansYh1KySGCa5Y3XIrWCvRjMhQsGY4vJrkzXumDY/VnR0lLJCkr3jEKbHOui3jcrdYwhU8FVoGfw6ly4+H7yoA1LrFz04vpqlkylJBjGn7OLFBRrTlVLBxoZMalhA6JH3WdqiIZCbIpqOO0YlzeiiKtXvKoqn7uyMj0piRDF2lJHZgFrOJ+V/WTm10EWRcJallis4+ilKBbIwme6Me14xaMXJAqOZuVkQHRBNq3XUK7gj+4srL0Dir+Lji3/ilKoaZ8nAEx3AKPpxDFa6hBnWg0IdHeIYXT3hP3qv3NivNefOeQ/gj7/0HnhqPiQ==</latexit><latexit sha1_base64="vtiDjf6o0mQdgUQPkFzMP7pc4Dk=">AAAB6nicbVA9SwNBEJ2LXzF+RS1tFhPBKuzZaBmwsYxoPiA5wt5mkizZ2zt294Rw5CfYWChi6y+y89+4Sa7QxAcDj/dmmJkXJlIYS+m3V9jY3NreKe6W9vYPDo/KxyctE6eaY5PHMtadkBmUQmHTCiuxk2hkUSixHU5u5377CbURsXq00wSDiI2UGArOrJMeqrTaL1dojS5A1omfkwrkaPTLX71BzNMIleWSGdP1aWKDjGkruMRZqZcaTBifsBF2HVUsQhNki1Nn5MIpAzKMtStlyUL9PZGxyJhpFLrOiNmxWfXm4n9eN7XDmyATKkktKr5cNEwlsTGZ/00GQiO3cuoI41q4WwkfM824demUXAj+6svrpHVV82nNv/crdZrHUYQzOIdL8OEa6nAHDWgChxE8wyu8edJ78d69j2VrwctnTuEPvM8fKjCM+w==</latexit>
a2
<latexit sha1_base64="VuNU+xmx+vqlDxS1FqmmTFntG8M=">AAAB7HicbZC7SgNBFIbPJl5ivEUtbQYTwSrsptEyYGMZwU0CSQhnJ7PJkNnZZWZWCEuewcZCEVufw2ewEHwanVwKTfxh4OP/z2HOOUEiuDau++Xk8hubW9uFneLu3v7BYenouKnjVFHm01jEqh2gZoJL5htuBGsnimEUCNYKxtezvHXPlOaxvDOThPUiHEoecorGWn4F+7VKv1R2q+5cZB28JZTr+c/vdwBo9Esf3UFM04hJQwVq3fHcxPQyVIZTwabFbqpZgnSMQ9axKDFiupfNh52Sc+sMSBgr+6Qhc/d3R4aR1pMosJURmpFezWbmf1knNeFVL+MySQ2TdPFRmApiYjLbnAy4YtSIiQWkittZCR2hQmrsfYr2CN7qyuvQrFU9t+rdeuW6CwsV4BTO4AI8uIQ63EADfKDA4QGe4NmRzqPz4rwuSnPOsucE/sh5+wFydJCp</latexit><latexit sha1_base64="4prNiupZVD6U9ihhFk3Er8Su1fk=">AAAB7HicbVBNT8JAEJ3iF+IX6tHLRjDxRFoueiTx4hETCyTQkOmyhQ3bbbO7NSENv8GLB43x6g/y5r9xgR4UfMkkL+/NZGZemAqujet+O6Wt7Z3dvfJ+5eDw6PikenrW0UmmKPNpIhLVC1EzwSXzDTeC9VLFMA4F64bTu4XffWJK80Q+mlnKghjHkkecorGSX8dhsz6s1tyGuwTZJF5BalCgPax+DUYJzWImDRWodd9zUxPkqAyngs0rg0yzFOkUx6xvqcSY6SBfHjsnV1YZkShRtqQhS/X3RI6x1rM4tJ0xmole9xbif14/M9FtkHOZZoZJuloUZYKYhCw+JyOuGDViZglSxe2thE5QITU2n4oNwVt/eZN0mg3PbXgPXq3lFnGU4QIu4Ro8uIEW3EMbfKDA4Rle4c2Rzovz7nysWktOMXMOf+B8/gCcRI3R</latexit>
a2
<latexit sha1_base64="VuNU+xmx+vqlDxS1FqmmTFntG8M=">AAAB7HicbZC7SgNBFIbPJl5ivEUtbQYTwSrsptEyYGMZwU0CSQhnJ7PJkNnZZWZWCEuewcZCEVufw2ewEHwanVwKTfxh4OP/z2HOOUEiuDau++Xk8hubW9uFneLu3v7BYenouKnjVFHm01jEqh2gZoJL5htuBGsnimEUCNYKxtezvHXPlOaxvDOThPUiHEoecorGWn4F+7VKv1R2q+5cZB28JZTr+c/vdwBo9Esf3UFM04hJQwVq3fHcxPQyVIZTwabFbqpZgnSMQ9axKDFiupfNh52Sc+sMSBgr+6Qhc/d3R4aR1pMosJURmpFezWbmf1knNeFVL+MySQ2TdPFRmApiYjLbnAy4YtSIiQWkittZCR2hQmrsfYr2CN7qyuvQrFU9t+rdeuW6CwsV4BTO4AI8uIQ63EADfKDA4QGe4NmRzqPz4rwuSnPOsucE/sh5+wFydJCp</latexit><latexit sha1_base64="4prNiupZVD6U9ihhFk3Er8Su1fk=">AAAB7HicbVBNT8JAEJ3iF+IX6tHLRjDxRFoueiTx4hETCyTQkOmyhQ3bbbO7NSENv8GLB43x6g/y5r9xgR4UfMkkL+/NZGZemAqujet+O6Wt7Z3dvfJ+5eDw6PikenrW0UmmKPNpIhLVC1EzwSXzDTeC9VLFMA4F64bTu4XffWJK80Q+mlnKghjHkkecorGSX8dhsz6s1tyGuwTZJF5BalCgPax+DUYJzWImDRWodd9zUxPkqAyngs0rg0yzFOkUx6xvqcSY6SBfHjsnV1YZkShRtqQhS/X3RI6x1rM4tJ0xmole9xbif14/M9FtkHOZZoZJuloUZYKYhCw+JyOuGDViZglSxe2thE5QITU2n4oNwVt/eZN0mg3PbXgPXq3lFnGU4QIu4Ro8uIEW3EMbfKDA4Rle4c2Rzovz7nysWktOMXMOf+B8/gCcRI3R</latexit>
a1+a2
<latexit sha1_base64="9N7mX1MhgO0kX2guk3lCDZyxTuA=">AAAB8HicbZDLSgMxFIbPtF5qvVVdugm2giCUmW50WXDjsoK9SDsMmTTThiaZIckIZehTuHGhiFufwmdwIfg0ml4W2vpD4OP/zyHnnDDhTBvX/XJy+bX1jc3CVnF7Z3dvv3Rw2NJxqghtkpjHqhNiTTmTtGmY4bSTKIpFyGk7HF1N8/Y9VZrF8taME+oLPJAsYgQba91VcOCd46BWCUplt+rOhFbBW0C5nv/8fgeARlD66PVjkgoqDeFY667nJsbPsDKMcDop9lJNE0xGeEC7FiUWVPvZbOAJOrVOH0Wxsk8aNHN/d2RYaD0Woa0U2Az1cjY1/8u6qYku/YzJJDVUkvlHUcqRidF0e9RnihLDxxYwUczOisgQK0yMvVHRHsFbXnkVWrWq51a9G69cd2GuAhzDCZyBBxdQh2toQBMICHiAJ3h2lPPovDiv89Kcs+g5gj9y3n4Au9CR7Q==</latexit><latexit sha1_base64="5CJRU+yy4Urohye7XmMUhiQ97Fg=">AAAB8HicbVBNSwMxEJ2tX7V+VT16CbaCIJRNL3osePFYwX5IuyzZNG1Dk+ySZIWy9Fd48aCIV3+ON/+NabsHbX0w8Hhvhpl5USK4sb7/7RU2Nre2d4q7pb39g8Oj8vFJ28SppqxFYxHrbkQME1yxluVWsG6iGZGRYJ1ocjv3O09MGx6rBztNWCDJSPEhp8Q66bFKQnxFwno1LFf8mr8AWic4JxXI0QzLX/1BTFPJlKWCGNPDfmKDjGjLqWCzUj81LCF0Qkas56gikpkgWxw8QxdOGaBhrF0pixbq74mMSGOmMnKdktixWfXm4n9eL7XDmyDjKkktU3S5aJgKZGM0/x4NuGbUiqkjhGrubkV0TDSh1mVUciHg1ZfXSbtew34N3+NKw8/jKMIZnMMlYLiGBtxBE1pAQcIzvMKbp70X7937WLYWvHzmFP7A+/wB5aCPFQ==</latexit>
a1+a2
<latexit sha1_base64="9N7mX1MhgO0kX2guk3lCDZyxTuA=">AAAB8HicbZDLSgMxFIbPtF5qvVVdugm2giCUmW50WXDjsoK9SDsMmTTThiaZIckIZehTuHGhiFufwmdwIfg0ml4W2vpD4OP/zyHnnDDhTBvX/XJy+bX1jc3CVnF7Z3dvv3Rw2NJxqghtkpjHqhNiTTmTtGmY4bSTKIpFyGk7HF1N8/Y9VZrF8taME+oLPJAsYgQba91VcOCd46BWCUplt+rOhFbBW0C5nv/8fgeARlD66PVjkgoqDeFY667nJsbPsDKMcDop9lJNE0xGeEC7FiUWVPvZbOAJOrVOH0Wxsk8aNHN/d2RYaD0Woa0U2Az1cjY1/8u6qYku/YzJJDVUkvlHUcqRidF0e9RnihLDxxYwUczOisgQK0yMvVHRHsFbXnkVWrWq51a9G69cd2GuAhzDCZyBBxdQh2toQBMICHiAJ3h2lPPovDiv89Kcs+g5gj9y3n4Au9CR7Q==</latexit><latexit sha1_base64="5CJRU+yy4Urohye7XmMUhiQ97Fg=">AAAB8HicbVBNSwMxEJ2tX7V+VT16CbaCIJRNL3osePFYwX5IuyzZNG1Dk+ySZIWy9Fd48aCIV3+ON/+NabsHbX0w8Hhvhpl5USK4sb7/7RU2Nre2d4q7pb39g8Oj8vFJ28SppqxFYxHrbkQME1yxluVWsG6iGZGRYJ1ocjv3O09MGx6rBztNWCDJSPEhp8Q66bFKQnxFwno1LFf8mr8AWic4JxXI0QzLX/1BTFPJlKWCGNPDfmKDjGjLqWCzUj81LCF0Qkas56gikpkgWxw8QxdOGaBhrF0pixbq74mMSGOmMnKdktixWfXm4n9eL7XDmyDjKkktU3S5aJgKZGM0/x4NuGbUiqkjhGrubkV0TDSh1mVUciHg1ZfXSbtew34N3+NKw8/jKMIZnMMlYLiGBtxBE1pAQcIzvMKbp70X7937WLYWvHzmFP7A+/wB5aCPFQ==</latexit>
Figure 3: 3d Kirby move 3
We consider a move (a1, 0,a 2)↔ (a1 +a2), which we call the move 3 (Fig. 3). We label
the vertices of (a1, 0,a 2) as v1, v0, and v2. The Chern-Simons contributions for ( a1, 0,a 2)
are given by
z−2a1m1
1 (zm1
0 zm0
1 )−2(zm2
0 zm0
2 )−2z−2a2m2
2 . (3.14)
Itsz0 part isz−2(m1+m2)
0 and the contour integral forz0 givesm2 =−m1 and∑
m0∈Z(z1z2)−2m0
×z−2a1m1
1 z2a2m1
2 , so the whole integrand takes a form of ∑
m0∈Z(z1z2)−2m0··· . Since the
index can be calculated by picking the coeﬃcients of the zeroth power of zv after the q-
expansion of the integrand in (3.7), upon the integral for z1 and z2, there are nonzero
contributions from the other terms in the integral when the exponents of z1 and z2 are
the same even number. Therefore, the integral can also be expressed as an integral with
a single integral variable z = z1 = z−1
2 . This gives z−2a1m1
1 z2a2m1
2 = z−2(a1+a2)m1. We
may then put the q-expansion back to the original expression of the integrand that we
started from. Other contributions to the vertex v2 are expressed in terms of z2 =z−1 and
m2 =−m1, and since they are invariant under z2↔ z−1
2 = z and m2↔− m2 = m1, the
integrand stays the same now expressed in terms of ( z,m 1) rather than ( z2,m 2). Also,
since (2− deg(v1)) + (2− deg(v2)) = (2− deg(vnew)) where vnew is the vertex for (a1 +a2),
the index with t = 1 is invariant under the move 3.
When t is general, the discussion above goes parallel if an arrow goes in to v0 and
another arrow goes out from v0. For such arrows, we have a right integrand for a vertex
vnew and the reﬁned index is also invariant under move 3.
From the calculations above, we see that the index calculated at least from (3.6) is
invariant under the 3d Kirby moves. We also saw that with some constraints the reﬁned
index is invariant under the moves. Therefore, though we discussed an eﬀective description
of T [M3], the supersymmetric index on S2×q S1 calculated from it is expected to be a
– 16 –
right index at least in the limit t = 1.
To summarize, a model ofT [M3] discussed in this paper is an eﬀective description of a
complete T [M3] that is unknown in a sense that a (Lagrangian) description of N = (0, 2)
boundary degrees of freedom with a manifest SU (2) symmetry was not found and it has
a limitation to fully address the reﬁned case t⁄= 1. However, when t = 1 the eﬀective
description of T [M3] is expected to be valid for producing a correct supersymmetric index
on S2×qS1 of T [M3]. It will be interesting to ﬁnd a complete description of T [M3] with
boundary conditions speciﬁed.
Remarks on topologically twisted index on S2×qS1
We give some remarks on the topologically twisted index on S2×qS1 [29]. The one-loop
contributions of the vector multiplet V , adjoint chiral multiplets Φ +
R=2, Φ−
R=0, and Φ 0
R=0
for G =SU (2) are given by
ZV (z,m,q,t ) =q−m(1−z2qm)(1−z−2qm),
ZΦ+
R=2(z,m,q,t ) =t−1/2(t− 1) z4mt−1
(z2tq−m+1;q)2m−1(z−2tqm+1;q)−2m−1
,
ZΦ−
R=0(z,m,q,t ) = t1/2
t− 1
z4mt−1
(z2t−1q−m;q)2m+1(z−2t−1qm;q)−2m+1
,
ZΦ0
R=0(z,m,q ) = z4m
(z2q−m;q)2m+1(z−2qm;q)−2m+1
=qm(1−z2qm)−1(1−z−2qm)−1,
(3.15)
where
(y;q)n =
{∏n−1
j=0 (1−yqj) if n≥ 0
∏−n−1
j=0 (1−yqn+j)−1 if n≤ 0
. (3.16)
We also put an extra overall minus sign to Z
Φ+
R=2
1-loop compared to the formula in [29] in order
to haveZ
Φ+
R=2
1-loopZ
Φ−
R=0
1-loop = +1. In the limit t→ 1,ZV
1-loop≃Z
Φ+
R=2
1-loop≃ (Z
Φ−
R=0
1-loop)−1≃ (Z
Φ0
R=0
1-loop)−1
up to an overall (log q)∗ factor.
The topologically twisted index is given by the Jeﬀerey-Kirwan (JK) prescription
Itw
SU (2) =
∑
m∈Z
∫
JK
∏
v∈Vertices
dzv
2πizv
ZV
1-loop(zv,mv,q )Z
Φ+
R=2
1-loop(zv,mv,t,q )z−2Mv,vmv
v
×
∏
(v1,v2)∈Edges
Z
Φ−
R=0
1-loop(z,m,t,q )Z
Φ0
R=0
1-loop(z,m,q ) (z
mv2
v1 z
mv1
v2 )−2Mv1,v2
(3.17)
where we multiplied an overall factor 2L. As in the index on S2×qS1, we take a regularized
version for the limit t→ 1,
Itw
SU (2) =
∑
m∈Z
∫
JK
∏
v∈Vertices
dzv
2πizv
(q−mv(1−z2
vqmv)(1−z−2
v qmv))2z−2Mv,vmv
v
×
∏
(v1,v2)∈Edges
1
(q−mv1(1−z2v1qmv1)(1−z−2v1 qmv1))
1
(q−mv2(1−z2v2qmv2)(1−z−2v2 qmv2)) (z
mv2
v1 z
mv1
v2 )−2Mv1,v2
(3.18)
– 17 –
and the integrand is the same with that of the index as expected.
For the move 1, we see that (3.17) with the same assignment of the arrows as before
and (3.18) are invariant under the move but up to an overall sign. For example, when the
weight iswv0 =−1 at the vertexv0, which corresponds to minus the Chern-Simons level at
v0, there is an additional minus sign upon integration at v0 with the JK prescription. This
can be compensated by multiplying sign(wv0) in (3.17) at the vertexv0 that we perform the
move. Regarding the move 2, (3.17) with the arrow from v1 to v0 and (3.18) are invariant
under the move with sign(wv0) multiplied at the vertex v0.
For the move 3, we also consider (3.17) with the same assignment of the arrows as
before and (3.18). But there is a subtlety on the move 3. In the JK residue prescription
[29], if keﬀ(σ) = 0 at σ =±∞ wherez∼e−βσ withβ being a radius of S1, which happens
for the vertexv0, then the pole at zero or at inﬁnity, which are the only available poles that
we have at v0, are not chosen. Meanwhile, considering a plumbing graph with a2 =±1
and deg(v2) = 1, if we apply the move 2 in a row, it leads to a vertex with a weight
a1±1, which is the plumbing graph that can be obtained by applying the standard residue
calculation to the vertex v0 in the process of the move 3 on the original plumbing graph
that we started from. So we may just take the standard residue calculation when wv0 = 0
at vertex v0 and see what we have. With this assumption, we see that (3.17) is invariant
for a few examples such as the case where the degree of at least one of vertices v1 or v2 is
1 or 2. It will be interesting to prove the invariance of the twisted index under the move 3
for general plumbing graphs.
Acknowledgments
I would like to thank Sergei Gukov, Hee-Cheol Kim, Du Pei, and Jaewon Song for discus-
sion. In particular, I am grateful to Sergei Gukov for helpful remarks on the draft. I would
also like to thank the Korea Institute for Advanced Study (KIAS) and the Institute for
Basic Science - Center for Geometry and Physics (IBS-CGP) for hospitality at some stages
of this work.
References
[1] S. Gukov, P. Putrov and C. Vafa, Fivebranes and 3-manifold homology , JHEP 07 (2017)
071, [1602.05302].
[2] S. Gukov, D. Pei, P. Putrov and C. Vafa, BPS spectra and 3-manifold invariants , J. Knot
Theor. Ramiﬁcations 29 (2020) 2040003, [ 1701.06567].
[3] S. Gukov, M. Marino and P. Putrov, Resurgence in complex Chern-Simons theory ,
1605.07615.
[4] M. C. Cheng, S. Chun, F. Ferrari, S. Gukov and S. M. Harrison, 3d Modularity, JHEP 10
(2019) 010, [ 1809.10148].
[5] H.-J. Chung, BPS Invariants for Seifert Manifolds , JHEP 03 (2020) 113, [ 1811.08863].
[6] P. Kucharski, ˆZ invariants at rational τ, JHEP 09 (2019) 092, [ 1906.09768].
[7] H.-J. Chung, BPS Invariants for 3-Manifolds at Rational Level K, 1906.12344.
– 18 –
[8] S. Park, Higher rank ˆZ and FK, SIGMA Symmetry Integrability Geom. Methods Appl. 16
(2020) Paper No. 044, 17.
[9] S. Chun, S. Gukov, S. Park and N. Sopenko, 3d-3d correspondence for mapping tori , JHEP
20 (2020) 152, [ 1911.08456].
[10] J. Eckhard, H. Kim, S. Schafer-Nameki and B. Willett, Higher-Form Symmetries, Bethe
Vacua, and the 3d-3d Correspondence , JHEP 01 (2020) 101, [ 1910.14086].
[11] A. Kapustin and B. Willett, Generalized Superconformal Index for Three Dimensional Field
Theories, 1106.2484.
[12] S. Kim, The Complete superconformal index for N=6 Chern-Simons theory , Nucl. Phys.
B821 (2009) 241–284, [ 0903.4172].
[13] Y. Imamura and S. Yokoyama, Index for three dimensional superconformal ﬁeld theories with
general R-charge assignments, JHEP 04 (2011) 007, [ 1101.0557].
[14] T. Dimofte, D. Gaiotto and S. Gukov, 3-Manifolds and 3d Indices , Adv. Theor. Math. Phys.
17 (2013) 975–1076, [ 1112.5179].
[15] C. Beem, T. Dimofte and S. Pasquetti, Holomorphic Blocks in Three Dimensions , JHEP 12
(2014) 177, [ 1211.1986].
[16] S. Pasquetti, Factorisation of N = 2 Theories on the Squashed 3-Sphere , JHEP 04 (2012)
120, [1111.6905].
[17] C. Hwang and J. Park, Factorization of the 3d superconformal index with an adjoint matter ,
JHEP 11 (2015) 028, [ 1506.03951].
[18] D. Pei and K. Ye, A 3d-3d appetizer , JHEP 11 (2016) 008, [ 1503.04809].
[19] A. Gadde, S. Gukov and P. Putrov, Walls, Lines, and Spectral Dualities in 3d Gauge
Theories, JHEP 05 (2014) 047, [ 1302.0015].
[20] A. Gadde, S. Gukov and P. Putrov, Fivebranes and 4-manifolds , Prog. Math. 319 (2016)
155–245, [1306.4320].
[21] Y. Yoshida and K. Sugiyama, Localization of 3dN = 2 Supersymmetric Theories on
S1×D2, 1409.6713.
[22] T. Dimofte, D. Gaiotto and N. M. Paquette, Dual boundary conditions in 3d SCFT’s , JHEP
05 (2018) 060, [ 1712.07654].
[23] E. Witten, Fivebranes and knots , Quantum Topol. 3 (2012) 1–137, [ 1101.3216v1].
[24] T. Dimofte, D. Gaiotto and S. Gukov, Gauge Theories Labelled by Three-Manifolds ,
Commun. Math. Phys. 325 (2014) 367–419, [ 1108.4389].
[25] H.-J. Chung, T. Dimofte, S. Gukov and P. Su lkowski, 3d-3d Correspondence Revisited, JHEP
04 (2016) 140, [ 1405.3663].
[26] S. Gukov and D. Pei, Equivariant Verlinde formula from ﬁvebranes and vortices , Commun.
Math. Phys. 355 (2017) 1–50, [ 1501.01310].
[27] M. Marino, Chern-Simons theory, matrix integrals, and perturbative three manifold
invariants, Commun. Math. Phys. 253 (2004) 25–49, [ hep-th/0207096].
[28] S. Gukov and C. Manolescu, A two-variable series for knot complements , 1904.06057.
– 19 –
[29] F. Benini and A. Zaﬀaroni, A topologically twisted index for three-dimensional
supersymmetric theories, JHEP 07 (2015) 127, [ 1504.03698].
[30] F. Benini and A. Zaﬀaroni, Supersymmetric partition functions on Riemann surfaces , Proc.
Symp. Pure Math. 96 (2017) 13–46, [ 1605.06120].
[31] M. Aganagic and S. Shakirov, Knot Homology and Reﬁned Chern-Simons Index , Commun.
Math. Phys. 333 (2015) 187–228, [ 1105.5117].
[32] E. Witten, Fivebranes and knots , Quantum Topol. 3 (2012) 1–137.
– 20 –
