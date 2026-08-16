---
doc_id: arxiv-1912.13486v2
doc_title: ""
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-9
source_pdf: 1912.13486v2.pdf
source_sha256: 9a8dbc1a143f7448
doc_brief: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds Hee-Joong Chung — We consider theS2×qS1 supersymmetric index of a 3dN = 2 theory T [M3] when M3 is a plumbed 3-manifold."
---
2 Supersymmetric index on S2×qS1 and factorization 2
2.1 Supersymmetric index, factorization, and D2×qS1 partition function 2
2.2 Analysis on homological block and index of lens space theory 8
3 Supersymmetric index of a 3d N = 2 theory on S2×q S1 for plumbed
3-manifolds 9
3.1 Engineering a 3d N = 2 theory T [M3] from homological blocks 10
3.2 Index for an eﬀective description of T [M3] 13
1 Introduction
The categoriﬁcation of the Witten-Reshetikhin-Turaev (WRT) invariants for closed 3-
manifolds has not been known. This is because ﬁrstly the integrality for the WRT in-
variants was not obvious. However, recently, a conjecture in [1, 2] states that the WRT
invariant can be expressed in a speciﬁc way in terms of the q-series with integer powers
and integer coeﬃcients, which would allow the categoriﬁcation. These q-series invariants
were called the homological block in [1, 2]. 1
Via the 3d-3d correspondence, the homological block is expected to correspond to the
D2×qS1 partition function or the half-index of the corresponding 3d N = 2 theory T [M3]
with an appropriate boundary condition,
ˆZb(q) =
∑
i,j
(−1)iqjdimH(b)
i,j (1.1)
whereH(b)
i,j is the Hilbert space of BPS states of T [M3] on D2× R1 and i,j denote the
charges under certain linear combinations of the U(1)R symmetry and the U(1) rotational
symmetry on D2. b denotes the boundary condition, which is given by the abelian ﬂat
connections on M3. Therefore, it is expected that the desired homology for the WRT in-
variants is given by the Hilbert space of BPS states in T [M3] on D2× R1. Some examples
of T [M3] including the 3-sphere, the lens spaces, and O(−p)→ Σg have been discussed in
[2].
The homological block for plumbed 3-manifolds with G = SU (2) was obtained in
[2]. A plumbed 3-manifold is represented by a plumbing graph that is made of vertices
and edges where an integer is assigned to each vertex. It is a large class of 3-manifolds,
1For its properties and developments, we refer to [3–9]
– 1 –
which includes Seifert manifolds. Therefore, it would be interesting to consider T [M3] for
plumbed 3-manifolds.
In this paper, we don’t give a complete answer for it. Rather, via an experimental
approach, we engineer an eﬀective description of T [M3] for plumbed 3-manifolds M3 to
calculate the S2×q S1 supersymmetric index. Such an eﬀective description of T [M3] is
useful for the calculation of the index, but it has limitations for being a complete descrip-
tion of the theory as will be discussed in section 3. Nevertheless, we check that the index
without reﬁnement is invariant under the 3d Kirby moves, so the analysis here could shed
some light on a complete description of T [M3].
In section 2, we discuss some aspects of the S2×q S1 supersymmetric index and its
factorization. Also, we study the case of the lens space in detail, which is a well known
example, for extrapolation to the case of plumbed 3-manifolds in section 3. In section 3,
from the expression of homological blocks for plumbed 3-manifolds, we engineer an eﬀec-
tive description of a 3d N = 2 theory T [M3] and consider its S2×qS1 index. We discuss
the invariance of the index under the 3d Kirby moves. We also give some remarks on the
S2×qS1 topologically twisted index.
Note added : Near completion of the main part of this work, a paper [10] on a similar
topic appeared, but the approach, the quantities under interest, and the theory discussed
in this paper are diﬀerent from it.
2 Supersymmetric index on S2×q S1 and factorization
We discuss the index and its factorization that are relevant to later discussion. We also re-
view the lens space theory, which is a well known example in the context of the homological
block and the index.
2.1 Supersymmetric index, factorization, and D2×qS1 partition function
We begin with a brief review on the formula for the index of the 3d N = 2 theory with a
Lagrangian description at the UV.
Supersymmetric index on S2×qS1
The supersymmetric index on S2×qS1 with fugacities for ﬂavor symmetries turned on was
obtained in [11] based on [12, 13]. The 1-loop contributions from the vector multiplet and
the chiral mutiplet are
Ivect(z =eih,m,q ) =
∏
α∈∆G
q− 1
4|α(s)|(1−eiα(h)q
1
2|α(s)|) (2.1)
Ichiral(z =eih,m,q ) =
∏
ρ∈RΦ
(
q
1
2 (1−R(Φ))∏
j
e−iρ(h)∏
a
t−fa(Φ)
a
) 1
2|ρ(m)| (e−iρ(h)t−fa(Φ)
a q
1
2|ρ(m)|+1− 1
2R(Φ);q)∞
eiρ(h)tfa(Φ)
a q
1
2|ρ(m)|+ 1
2R(Φ);q)∞
(2.2)
– 2 –
where zj are the Wilson lines, mj are the magnetic ﬂuxes, RΦ is the representation of a
chiral multiplet Φ under the gauge groupG,ta’s are the fugacities for the global symmetries,
fa(Φ) is the charge of a chiral multiplet Φ under the global symmetries, and R(Φ) is the
R-charge of Φ. The contribution from the Chern-Simons (CS) term for G =U(N) with a
levelk is
ICS(z =eih,m ) =eik ∑
jhjmj =
N∏
j=1
zkmj
j . (2.3)
The index is given by
IS1×S2 =
∑
m
1
|Wm|
∮
TrankG
dz
2πizIvectIchiralsICS (2.4)
whereWm is a symmetrization factor from the Weyl group of the gauge group that is
unbroken in the presence of the magnetic ﬂux m, which is given by∏
l rank(Gl)! when the
gauge group is broken to ⊗lGl.
In particular, when the gauge group is G =SU (N), the contributions from the vector
multiplet and the adjoint chiral multiplet charged +1 under the global symmetry U(1)t
with R-chargeR are given by
Ivect(z,m,q ) =
∏
1≤i⁄=j≤N
q− 1
4|mi−mj|(1−ziz−1
j q
1
2|mi−mj|), (2.5)
Iadj(z,m,t,R,q ) = (t−1q1−R
2 ;q)N−1
∞
(tq
R
2 ;q)N−1∞
∏
1≤i⁄=j≤N
(−q
1
2 (1−R)t−1)
1
2|mi−mj| (z−1
i zjt−1q
1
2|mi−mj|+1−R
2 ;q)∞
(ziz−1
j tq
1
2|mi−mj|+R
2 ;q)∞
,
(2.6)
respectively, where∏N
j=1zj = 1 and∑N
j=1mj = 0 are imposed. 2 Also, the q-Pochhammer
symbol,
(x;q)∞ =
∞∏
n=0
(1−xqn), (2.7)
is used. We will consider only G =SU (N), in particular, G =SU (2) in this paper. 3
Factorization of index
The index can be factorized as a fusion of two D2×qS1 partition functions [15, 16]. 4 For
the vector multiplet V ,
Ivect =
∏
i⁄=j
q− 1
4|mi−mj|(1−ziz−1
j q
1
2|mi−mj|) (2.8)
=
∏
1≤i<j≤N
(s1/2
i s−1/2
j −s−1/2
i s1/2
j )(˜s1/2
i ˜s−1/2
j − ˜s−1/2
i ˜s1/2
j ) =:
∏
1≤i<j≤N
‖(s1/2
i s−1/2
j −s−1/2
i s1/2
j )‖2
id
(2.9)
2The expression for Iadj in (2.6) comes from [14, 15] where there is an additional phase factor∏
1≤i⁄=j≤N(−1)
1
2|mi−mj| in (2.6) compared to the expression in [11, 13].
3If we include a factor ∏
1≤i⁄=j≤N(−1)
1
2|mi−mj| in (2.5) or include it in (2.6), the analysis on the G =
SU (2) case in this paper where such a factor is 1 would be generalized to G =SU (N) or U(N) cases.
4See also [17] for adjoint chiral multiplets.
– 3 –
where‖·‖ id denotes the identity fusion [15] of half- and anti-half-index with sj =zjqmj/2
and ˜sj =z−1
j qmj/2.
For the adjoint chiral multiplet Φ±
R charged±1 under the global symmetry U(1)t with
R-chargeR,
I±,R
adj = (t∓q1−R
2 ;q)N−1
∞
(t±q
R
2 ;q)N−1∞
∏
1≤i⁄=j≤N
(z−1
i zjt∓q− 1
2 (mi−mj)+1−R
2 ;q)∞
(ziz−1
j t±q− 1
2 (mi−mj)+R
2 ;q)∞
(z−1/2
i z1/2
j )−(mi−mj)
(2.10)
=‖(t∓q1−R
2 ;q)∞‖N−1
id
∏
1≤i⁄=j≤N
‖‖‖‖
(s−1
i sjv∓q1−R
2 ;q)∞
θ(−q1/2s−1
i sj;q)1/2
‖‖‖‖
2
id
(2.11)
where ˜q = q−1, v = tqn/2, and ˜v = t−1qn/2. We also set the magnetic ﬂux for U(1)t
symmetry to zero, n = 0, so v =t and ˜v =t−1. Here,
θ(x;q) = (−q1/2x;q)∞(−q1/2x−1;q)∞ (2.12)
is the Jacobi theta function. In (2.11), we may also choose ∏
1≤i⁄=j≤Nθ((−q1/2)bs−1
i sjvc;q)
in (2.11) with arbitrary b,c∈ Z and zero ﬂux n = 0 for U(1)t, which gives the same index
after the identity fusion. Or, since the square root to the Jacobi theta function is rather
unusual, we may also replace the theta function part with other Jacobi theta functions
such as∏
1≤i<j≤Nθ(s−1
i sj;q)−1, which gives the same index upon the identity fusion.
The index for the adjoint chiral multiplet can also be written in another way,
I±,R
adj = (t∓q1−R
2 ;q)N−1
∞
(t±q
R
2 ;q)N−1∞
∏
1≤i⁄=j≤N
(z−1
i zjt∓q
1
2 (mi−mj)+1−R
2 ;q)∞
(ziz−1
j t±q
1
2 (mi−mj)+R
2 ;q)∞
(z−1/2
i z1/2
j )(mi−mj) (2.13)
= 1
‖(v±q
R
2 ;q)∞‖N−1
id
∏
1≤i⁄=j≤N
‖‖‖‖
θ(−q1/2s−1
i sj;q)1/2
(sis−1
j v±q
R
2 ;q)∞
‖‖‖‖
2
id
. (2.14)
We note that whent is turned oﬀ,t = 1, the contribution to the index from the adjoint
chiral multiplets Φ±
R with R = 2 and R = 0 become
I±,R=2
adj
⏐⏐⏐
t→1
= (t∓;q)N−1
∞
(t±q;q)N−1∞
⏐⏐⏐⏐
t→1
∏
1≤i<j≤N
(−1)mi−mj‖(s1/2
i s−1/2
j −s−1/2
i s1/2
j )‖2
id, (2.15)
I±,R=0
adj
⏐⏐⏐
t→1
= (t∓q;q)N−1
∞
(t±;q)N−1∞
⏐⏐⏐⏐
t→1
∏
1≤i<j≤N
(−1)mi−mj‖(s1/2
i s−1/2
j −s−1/2
i s1/2
j )‖−2
id , (2.16)
and they need to be regularized. As in [2, 18], we may take t =qϵ and multiply an overall
factor ϵ−N+1 and ϵN−1 to (2.15) and (2.16), respectively. Then for the case of R = 2,
upon ϵ→ 0, (t∓;q)N−1
∞
(t±q;q)N−1
∞
ϵ−N+1
⏐⏐⏐
t→1
becomes (± logq)N−1. Similarly, (t∓q;q)N−1
∞
(t±;q)N−1
∞
ϵN−1
⏐⏐⏐
t→1
→
(∓ logq)−N+1 for the case of R = 0. Or we may rescale (2.15) and (2.16) by multiplying
– 4 –
(t±q;q)N−1
∞
(t∓;q)N−1
∞
and (t±;q)N−1
∞
(t∓q;q)N−1
∞
, respectively. 5 In this paper, when t = 1 we will consider the
regularized index for the adjoint chiral multiplets,
I±,R=2
adj
⏐⏐⏐
t→1
≃
∏
1≤i<j≤N
(−1)mi−mj‖(s1/2
i s−1/2
j −s−1/2
i s1/2
j )‖2
id, (2.17)
I±,R=0
adj
⏐⏐⏐
t→1
≃
∏
1≤i<j≤N
(−1)mi−mj‖(s1/2
i s−1/2
j −s−1/2
i s1/2
j )‖−2
id , (2.18)
up to an overall factor, (± logq)N−1 and (∓ logq)−N+1, respectively. The contribution from
the adjoint chiral multiplet Φ 0
R=0 with R = 0 and U(1)t charge 0 is given by (2.18) after
the regularization or the rescaling of t→ 1 limit (2.16). In particular, when G = SU (2),
since m1 =−m2, (2.17) and (2.18) with R = 2 and R = 0, respectively, are equal and are
inverse precisely to Ivect in (2.9).
The D2×q S1 partition function with given N = (0, 2) boundary conditions on 3d
N = 2 multiplets and with boundary degrees of freedom was studied in [19–22]. The
contribution from the 3d bulk vector multiplet forG =SU (N) with the Neumann boundary
condition [21] is given by
∏
1≤i⁄=j≤N
e
1
4ℏ (logsis−1
j )2
(sis−1
j ;q)∞ =
∏
1≤i<j≤N
e
1
2ℏ (logsis−1
j )2
(sis−1
j ;q)∞(s−1
i si;q)∞ (2.19)
where q =eℏ. We note that the asymptotic expansion of the Jacobi theta function termi-
nates at ℏ1
θ(x;q) = (−q1/2x;q)∞(−q1/2x−1;q)∞≃C−1e− 1
2ℏ (logx)2
as ℏ→ 0 (2.20)
whereC =e
π2
6ℏ− ℏ
24 . Since we take |q|< 1 (i.e. q⁄= 1) in the calculation of the homological
block or the index, we can use the approximation (2.20) in (2.19). Or such replacement of
exponential term in (2.19) by the theta function can be regarded as the elliptic completion
of a partition function of quantum mechanics on R+ ofD2×S1≃ R+×T 2 [15]. Then, the
exponential term in (2.19) can be expressed as
∏
i<j
e
1
2ℏ (logsis−1
j )2
=
∏
i<j
e
1
4ℏ (logsis−1
j )2+ 1
2ℏ (logsis−1
j )(πi+ℏ/2)e
1
4ℏ (logsis−1
j )2− 1
2ℏ (logsis−1
j )(πi+ℏ/2)
≃
∏
i<j
θ(−q1/2sis−1
j ;q)−1/2θ(−q−1/2sis−1
j ;q)−1/2
(2.21)
up to an irrelevant overall constant factor and the theta function ambiguity. 6 Therefore,
5This could also be regarded as introducing extra N−1 free chiral multiplets withU(1)R×U(1)t charge
(0,∓1) and (2,∓1) by hand, respectively.
6Here, what we mean by theta function ambiguity is that there can be various theta functions that gives
the same contribution to the index upon the identity fusion. For example, contributions from θ(s2;q) and
θ(s;q)4 to the index are the same. But at the level of the half-index, only speciﬁc types of expressions of
the Jacobi theta function arise from the N = (0, 2) boundary degrees of freedom, so not all Jacobi theta
functions can have a proper interpretation in the 3d-2d system onD2×qS1 as contributions from boundary
N = (0, 2) chiral or Fermi multiplets.
– 5 –
in the region|q|< 1, (2.19) can be expressed as
∏
1≤i<j≤N
e
1
2ℏ (logsis−1
j )2
(sis−1
j ;q)∞(s−1
i sj;q)∞≃
∏
1≤i<j≤N
(sis−1
j ;q)∞(s−1
i sj;q)∞
θ(−q1/2sis−1
j ;q)1/2θ(−q−1/2sis−1
j ;q)1/2
(2.22)
=
∏
1≤i<j≤N
( θ(−q1/2sis−1
j ;q)
θ(−q−1/2sis−1
j ;q)
)1/2
(1−sis−1
j ) =
∏
1≤i<j≤N
q−1/4(s1/2
i s−1/2
j −s−1/2
i s1/2
j )
(2.23)
and this agrees with the factorization in (2.9) up to an irrelevant overall factor q−1/4. We
can also see that the original expression (2.19) and (2.23) give the same index∏
i<j‖(s1/2
i s−1/2
j −
s−1/2
i s1/2
j )‖2
id upon the identity fusion.
Similarly, the contribution from the 3d bulk adjoint chiral multiplet Φ ±
R,N and Φ±
R,D
with the Neumann or the Dirichlet boundary condition 7 [21] are given by, respectively,
Z±,(N)
adj (sj,v,R,q ) =
∏
1≤i,j≤N
e− 1
4ℏ
(
logsi/sj+( ℏ
2 +πi)(R−1)+logv±1
)2
+ ℏ
48 (sis−1
j v±1(−q1/2)R;q)−1
∞ ,
(2.24)
Z±,(D)
adj (sj,v,R,q ) =
∏
1≤i,j≤N
e
1
4ℏ
(
logsi/sj+( ℏ
2 +πi)(R−1)+logv±1
)2
− ℏ
48 (s−1
i sjv∓1(−q1/2)2−R;q)∞.
(2.25)
As discussed above, the exponential factor in (2.24) and (2.25) can be approximated to
the exact asymptotic expansion of, for example, ∏
1≤i,j≤Nθ((−q1/2)1−Rs−1
i sjv−1;q)±1/2 or∏
1≤i,j≤Nθ((−q1/2)#s−1
i sj)±1/2×θ((−q1/2)1−Rv−1;q)±1/2 up to irrelevant constant factors.
The exponential factors and the Jacobi theta function in the contributions to D2×qS1
partition function above can be regarded as the factors that cancel out the (mixed) CS
contributions that the q-Pochhammer symbols have. Putting diﬀerently, each contribu-
tions (2.19), (2.24), and (2.25) above are regarded as the contributions purely from the
supermultiplet without any CS levels.
Summarizing the calculations above, there are two equivalent expressions for each
contribution from vector multiplets and adjoint chiral multiplets in the perspective of the
index. When G =SU (2), for the vector multiplet with the Neumann boundary condition,
we had
e
1
2ℏ (logs2)2
(s−2;q)∞(s2;q)∞ (2.26)
from the localization (2.19), and
s−s−1 (2.27)
7In this paper, we work with Tr(−1)R··· instead of Tr(−1)F··· . They are equivalent when R-charges
are integer, which is the case in our example. We replace −q1/2 with q1/2 if we want to use Tr(−1)F [15].
– 6 –
from the factorization of the index (2.9) and also from the approximation to (2.26) up
to an irrelevant overall factor and the theta function ambiguity. They all give the same
contribution to the index, which is (2.8). 8
Similarly, for the adjoint chiral multiplets, Φ +
R=2,N, Φ−
R=0,D, and Φ 0
R=0,N, the contri-
butions to the half-index are, respectively,
e− 1
2ℏ (logs2)2(
(s−2tq;q)∞(s2tq;q)∞(tq;q)∞
)−1, e
1
2ℏ (logs2)2
(s−2tq;q)∞(s2tq;q)∞(tq;q)∞, e− 1
2ℏ (logs2)2(
(s−2;q)∞(s2;q)∞
)−1
(2.28)
from the localization where we ignore the background CS contributions, and
θ(−q1/2s−2;q)1/2θ(−q1/2s2;q)1/2
(s−2tq;q)∞(s2tq;q)∞(tq;q)∞
, (s−2tq;q)∞(s2tq;q)∞(tq;q)∞
θ(−q1/2s−2;q)1/2θ(−q1/2s2;q)1/2, θ(−q1/2s−2;q)1/2θ(−q1/2s2;q)1/2
(s−2;q)∞(s2;q)∞
(2.29)
from the factorization of the index (2.11) and (2.14) and also from the approximation to
(2.28) up to theta function ambiguity and an irrelevant overall factor. 9 They all give the
same contributions to the index, (2.10) or (2.13). In particular, when t = 1, we have
e− 1
2ℏ (logs2)2(
(s−2q;q)∞(s2q;q)∞
)−1, e
1
2ℏ (logs2)2
(s−2q;q)∞(s2q;q)∞, e − 1
2ℏ (logs2)2(
(s−2;q)∞(s2;q)∞
)−1
(2.30)
from (2.28) and
s−s−1, (s−s−1)−1, (s−s−1)−1, (2.31)
from (2.29), respectively, up to an overall factor.
Homological block and D2×qS1 partition function
It was discussed in [1, 2] that the Witten-Reshetikhin-Turaev (WRT) invariants for closed 3-
manifolds can be expressed in terms of q-series with integer powers and integer coeﬃcients,
which was called the homological block. Interestingly, the homological blocks are labeled
by abelian ﬂat connections, i.e. it can be regarded as the contribution from abelian ﬂat
connections to the partition function of analytically continued Chern-Simons theory whose
gauge group is complex, GC, and at the same time it contains all the information of
the contribution from non-abelian ﬂat connections [3]. In the perspective of the 3d-3d
correspondence, this means that the homological block ofM3 which is labeled by an abelian
ﬂat connection corresponds to the D2×q S1 partition function of the corresponding 3d
N = 2 theory with a boundary condition given by the abelian ﬂat connection [23, 24].
8For explicitness, the identity fusion for e
1
2ℏ (logs2)2
is given by e
1
2ℏ (logs2)2
e− 1
2ℏ (log ˜s2)2
.
9Also from s−1θ(−q1/2s−2;q) instead of θ(−q1/2s−2;q)1/2θ(−q1/2s2;q)1/2, we have the same desired
result (s−s−1)±1 upon t = 1 limit. We could choose a diﬀerent Jacobi theta functions, e.g. θ(s−2;q),
which gives the same contribution to the index, but with this expression, we don’t have ( s−s−1)±1 when
t = 1.
– 7 –
Since the homological block is the D2×qS1 partition function with a boundary condi-
tion, the index of T [M3] onS2×qS1 is also expected to be expressed as the identity fusion
of homological block and anti-homological block,
I =
∑
m
1
|Wm|
∮
|z|=1
dz
2πiz
‖‖Integrand[ZD2×qS1(q;s,··· )]
‖‖2
id (2.32)
where Integrand[ZD2×qS1(q;s,··· )] denotes the integrand of the integral expression of ho-
mological blocks.
In the next section, we discuss how the discussion above ﬁts in the case of the lens
space.
