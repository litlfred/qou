---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-032-102-x-coordinates
section_title: "X-coordinates"
section_number: 10.2
pages: 33-39
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
ments. These are deﬁned for face points and agree with the X-coordinates of Fock and
Goncharov [8, p. 133].
The natural A4 action on vertices of ∆ has two orbits. Let εv0v1v2
⟲ be a sign, which is
positive if and only if v0v1v2 is in the orbit of 012.
34 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Deﬁnition 10.8. Let c be a Ptolemy assignment and let t∈ ∆3
n(Z) be a face point. The
X-coordinate at t is given by
(10.10) Xt =
∏
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1
where the product is taken over the six ordered triples of vertices v0,v 1,v 2 spanning the face
containingt.
As an example, the X-coodinate of t = (t0,t 1,t 2, 0) is given by
(10.11) X(t0,t1,t2,0) = ct+e0−e1ct+e1−e2ct+e2−e0
ct+e0−e2ct+e1−e0ct+e2−e1
.
Deﬁnition 10.9. Let z be a shape assignment on ∆ 3
n and let t be a face point spanned by
v0, v1 and v2. The X-coordinate at t is given by
(10.12) Xt =−
∏
s+e=t
ze
s.
Remark 10.10. Note that the product (10.12) consists of half of the terms involved in a
face equation. More precisely, if v0v1v2∈ ∆0 is glued to w0w1w2∈ ∆1, the face equations
are given by
(10.13) X
εv0v1v2
⟲
t0v0+t1v1+t2v2 =X
εw0w1w2
⟲
t0w0+t1w1+t2w2.
Note that εv0v1v2
⟲ and εw0w1w2
⟲ are equal if and only if the face pairing preserves orientation.
For oriented triangulations the signs are always opposite.
Lemma 10.11. The X-coordinates transform as the shapes under reordering, i.e. we have
(10.14) X(σ∗(c))t =X(c)sgn(σ)
σ(t) , X (σ∗(z))t =X(z)sgn(σ)
σ(t) .
Proof. Unwinding the deﬁnitions, we have
(10.15) X(σ∗c)t =
∏
t∈face(v0v1v2)
(σ∗c)
εv0v1v2
⟲
t+v0−v1 =
∏
t∈face(v0v1v2)
det(Iσ,σ(t+v0−v1))c
εv0v1v2
⟲
σ(t)+σ(v0)−σ(v1) =

 ∏
t∈face(v0v1v2)
det(Iσ,σ(t+v0−v1))

X(c)sgn(σ)
σ(t) =X(c)sgn(σ)
σ(t) .
The fact that the product of determinants equals 1 follows from Remark 5.7, which implies
that det(Iσ,σ(t+v0−v1)) = det(Iσ,σ(t+v1−v0)). Since both are ±1, their product is 1. The second
equation is obvious. □
Lemma 10.12. TheX-coordinates of a Ptolemy assignmentc agree with theX-coordinates
of the corresponding shape assignment µ(c).
Proof. We must prove that
(10.16) −
∏
s+e=t
µ(c)e
s =
∏
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1.
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 35
By compatibility under reordering, it is enough to prove this for t = (t0,t 1,t 2, 0) = t0e0 +
t1e1 +t2e2. Let t =α + (1110). By (6.8),
(10.17)
−
∏
s+e=t
µ(c)e
s =z1100
α+0010z0110
α+1000z1010
α+0010
= cα+2010,0cα+1200,0cα+0120,0
cα+2100,0cα+0210,0cα+1020,0
= ct+e0−e1ct+e1−e2ct+e2−e0
ct+e0−e2ct+e1−e0ct+e2−e1
=
∏
t∈face(v0v1v2)
c
εv0v1v2
⟲
t+v0−v1,
where the last equality follows from (10.11). □
Lemma 10.13. One can express the X-coordinates in terms of diamond coordinates:
(10.18) Xt =
(dv0v1v2
t−v0−v1
dv0v1v2
t−v0−v2
)εv0v1v2
⟲
Here t is a face point spanned by v0, v1 and v2.
Proof. It is enough to prove this for t = (t0,t 1,t 2, 0). Since
(10.19) d012
t−e0−e1 =−ct+e0−e1ct+e2−e0
ctct+e2−e1
, d 012
t−e0−e2 =−ct+e0−e2ct+e1−e0
ct+e1−e2ct
,
the result follows from (10.11). □
0
1
2
+
+
+_
_
_
t
0
1
2
+_
+
+
+_
_
_
Figure 23. Exponents of the
Ptolemy coordinates involved in the
X-coordinate at t.
Figure 24. An X-coordinate as
a quotient of two diamond coordi-
nates.
36 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
10.3. From natural(SL(n, C),N )-cocycles to natural (PGL(n, C),B,H )-cocycles. The
natural map π : SL(n, C)→ PGL(n, C) induces a map from decorations by N-cosets to dec-
orations by B-cosets. Given a generic SL( n, C)/N-decoration D on ∆ 3
n, we show how the
natural (PGL(n, C),B,H )-cocycleLαβγ(π(D)) can be obtained from the natural cocycle
Lαβ(D) by the coboundary action (9.2) of an explicit coboundary given in terms of the di-
amond coordinates. This deﬁnes the map τ in diagram (1.5) and gives rise to an explicit
formula forLαβγ(π(D)) in terms of the shapes.
Given an SL( n, C)/N-decoration D with diamond coordinates dv0,v1,v2
1,i consider the 0-
cochain on ∆3
n given by
(10.20) τv0v1v2(D) =


∏n−1
i=1 dv0v1v2
1,i ∏n−1
i=2 dv0v1v2
1,i
...
dv0v1v2
1,n−i
1


=
n−1∏
i=1
Hi(dv0v1v2
1,i ).
We shall make use of the abbreviations
(10.21) Xk,i =Xv0v1v2
kv2+iv0+(n−k−i)v1
, z i =zv0+v1
(i−1)v0+(n−1−i)v1
.
Theorem 10.14. Let D be a generic PGL(n, C)/B-decoration of ∆3
n. The natural cocycle
Lαβγ(D) is given by
(10.22)
αv0v1v2 =q1, β v0v1v2 =
n−1∏
k=1
(n−k∏
i=1
xi(1)
n−k−1∏
i=1
Hi(X
εv0v1v2
⟲
k,i )
)
d±1
γv0v1v2 =
n−1∏
i=1
Hi(z
−εv0v1v2
⟲
i ).
Moreover, if ~D is any SL(n, C)/N-decoration liftingD,L(D) =τLαβ(~D). □
Before embarking on the proof, we give some examples.
Example 10.15. Forn = 2,
(10.23) β012 =x1(1)d±1 =
(
−1 1
1
)
, γ 012 =H1(z−1
1 ) =
(
z−1
1
1
)
.
Forn = 3, we have
(10.24)
β012 =x1(1)x2(1)H1(X1,1)x1(1)d±1 =


X1,1 −X1,1 1
−1 1
1

,
γ012 =H1(z−1
1 )H2(z−1
2 ) =


z−1
1 z−1
2
z−1
2
1

.
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 37
Forn = 4,
(10.25)
β012 =x1(1)x2(1)x3(1)H1(X1,1)H2(X1,2)x1(1)x2(1)H1(X2,1)x1(1)d±1
γ012 =d(z−1
1 z−1
2 z−1
3 ,z−1
2 z−1
3 ,z−1
3 , 1).
Remark 10.16. The formula for βv0v1v2 is inspired by [8, (9.14)].
Remark 10.17. Note that the diagonal entries of βv0v1v2 and γv0v1v2 are given by
(10.26) βv0v1v2
ll = (−1)n−l
n−2∏
i=l
n−1−i∏
k=1
X
εv0v1v2
⟲
k,i , γ v0v1v2
ll =
n−1∏
i=l
z
−εv0v1v2
⟲
i .
Proof of Theorem 10.14. We prove that τ(~D)Lαβ(~D) is given by (10.22). Since the last
column of∏n−1
i=1 xi(1) consists of 1’s and since none of the other terms aﬀect the last column,
the middle edges are thus normalized, so by Lemma 9.15, the cocycle is indeed the natural
cocycle of D.
Let~α, ~β (and~γ = id) be the labelings, of long, middle and short edges given by Lαβ(~D).
By Proposition 10.4 these are given by (10.4). Let τ =τ(~D).
Long edges: We must prove that (τv0v1v2)−1~αv0v1v2τv1v0v2 =q1. Letting
(10.27) lk =
n−1∏
i=k
dv0v1v2
1,i , m k = (−1)k−1ev0v1
(n−k)v0+(k−1)v1
, r k =
n−1∏
i=k
dv1v0v2
1,i ,
this is equivalent to proving that
(10.28) d(l1,...,l n)−1q(m1,...,m n)d(r1,...,r n) =q1∈ PGL(n, C).
Hence, we must prove thatl−1
n−k+1mkrk is independent ofk. From Figure 25 it follows that
(10.29)
n−1∏
i=k
dv0v1v2
1,i =εn−kcnv0c(k−1)v0+(n−k)v1+v2
c(n−1)v0+v2ckv0+(n−k)v1
,
n−1∏
i=k
dv1v0v2
1,i = (−ε)n−kcnv1c(k−1)v1+(n−k)v0+v2
c(n−1)v1+v2ckv1+(n−k)v1
where ε =−εv0,v1,v2
< . Hence, we have
(10.30)
ln−k+1 =εk−1 c(n−k)v0+(k−1)v1+v2
c(n−k+1)v0+(k−1)v1c(n−1)v0+v2
, m k = (−1)k−1 c(n−k)v0+kv1
c(n−k+1)v0+(k−1)v1
rk = (−ε)n−k c(k−1)v1+(n−k)v0+v2
c(n−1)v1+v2ckv1+(n−k)v0
,
from which it follows that
(10.31) l−1
n−k+1mkrk = (−ε)n−1c(n−1)v0+v2
c(n−1)v1+v2
,
which is independent of k. This proves the result.
Middle edges: We must prove that τ−1
v0v1v2
~βv0v1v2τv0v2v1 =βv0v1v2. Using the basic commu-
tator relations
(10.32) Hi(x)xj(y) =xj(y)Hi(x) if i⁄=j, x i(y) =Hi(y)xi(1)Hi(y)−1
38 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
d1,n−1
v0 v2
v1
d1,k+1
d1,k
Figure 25. Cancellations.
the expression
(10.33) ~βv0v1v2 =
n−1∏
k=1
n−k∏
i=1
xi(dk,i) =
n−1∏
k=1
n−k∏
i=1
Hi(dk,i)xi(1)Hi(dk,i)−1
expands to
(10.34) ~βv0v1v2 =
n−1∏
k=1
(n−k∏
i=1
Hi(dk,i)
n−k∏
i=1
xi(1)
(n−k−1∏
i=1
Hi(dk,i)−1
)
Hn−k(dk,n−k)−1
)
.
We have for brevity omitted the superscript v0v1v2 of the diamond coordinates. Letting
Hk =
n−k∏
i=1
Hi(dk,i) and H′
k =
n−k−1∏
i=1
Hi(dk,i),
and moving the terms Hn−k(dk,n−k)−1 to the right, we have
(10.35) ~βv0v1v2 =
n−1∏
k=1
(
Hk
(n−k∏
i=1
xi(1)
)
H′−1
k
)n−1∏
k=1
Hn−k(dk,n−k)−1.
SinceHn = 1, the product (H1···H ′−1
1 )(H2···H ′−1
2 )··· equalsH1(···H ′−1
1 H2)(···H ′−1
2 H3)··· ,
and we obtain
(10.36) ~βv0v1v2 =H1
n−1∏
k=1
((n−k∏
i=1
xi(1)
)
H′−1
k Hk+1
)n−1∏
k=1
Hn−k(dk,n−k)−1.
Using (10.3), we have
(10.37) dv0v2v1
1,i =dv0v2v1
(i−1)v0+(n−1−i)v2
=−dv0v1v2
(i−1)v0+(n−1−i)v2
=−dv0v1v2
n−i,i ,
and since (last equality follows from (10.37))
(10.38) τv0v1v2 =
n−1∏
i=1
Hi(dv0v1v2
1,i ) =H1, τ v0v2v1 =
n−1∏
i=1
Hi(dv0v2v1
1,i ) =
n−1∏
k=1
Hn−k(−dk,n−k).
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 39
we have
(10.39) βv0v1v2 =τ−1
v0v1v2
~βv0v1v2τv0v2v1 =
n−1∏
k=1
((n−k∏
i=1
xi(1)
)
H′−1
k Hk+1
)
d±1.
By Lemma 10.13, dk+1,i
dk,i
=Xε⟲(v0v1v2)
k,i , so that
(10.40) H′−1
k Hk+1 =
n−k∏
i=1
Hi(dk,i)−1Hi(dk+1,i) =
n−k∏
i=1
Hi(Xε⟲(v0v1v2)
k,i ).
This proves the result.
Short edges: We must prove that (τv0v1v2)−1τv0v1v3 =γv0v1v2. We have
(10.41) ( τv0v1v2)−1τv0v1v3 =
(n−1∏
i=1
Hi(dv0v1v2
1,i )
)−1n−1∏
i=1
Hi(dv0v1v3
1,i ) =
n−1∏
i=1
Hi(dv0v1v3
1,i
dv0v1v2
1,i
).
The result now follows from Lemma 10.18 below.
Lemma 10.18. The shape parameters in (10.22) are given in terms of diamond coordinates:
(10.42) z
−εv0v1v2
⟲
i = dv0v1v3
1,i
dv0v1v2
1,i
Proof. Let α = (i− 1)v0 + (n− 1−i)v1, so that zi =zv0+v1
α and dv0v1vk
1,i =dv0v1vk
α , k = 2, 3.
By compatibility under reordering, it is enough to prove the result for vi =i. We have
(10.43) z1100
α = cα+e0+e3cα+e1+e2
cα+e0+e2cα+e1+e3
, d 01k
α =− cα+2e0cα+e1+ek
cα+e0+e1cα+e0+ek
.
Hence, z−1
i =d013
1,i/d012
1,i proving the result. □
This concludes the proof of Theorem 10.14. □
Remark 10.19. Theorem 10.14 implies that for a generic PGL( n, C)/B-decoration on
(M,T ), the restriction of the natural cocycle to ∂M has a canonical lift to a cocycle with
values in B⊂ GL(n, C) (not just in PGL(n, C)).
