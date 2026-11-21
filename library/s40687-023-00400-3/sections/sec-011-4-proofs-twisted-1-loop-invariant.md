---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-011-4-proofs-twisted-1-loop-invariant
section_title: "Proofs: twisted 1-loop invariant"
section_number: 4
pages: 16-21
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
In this section, we give proofs of the properties of the twisted 1-loop invariant.
Proof Theorem 1.6 We will use the notation of Theorem 1.5 which relates the NZ matrices
of two triangulations T and T obtained by a 2–3 Pachner move shown in Fig. 2. Recall that
a 2–3 Pachner move on T is determined by two tetrahedra α and β with a common
face in T . Dividing the bipyramid α ∪β into three tetrahedra a, b, and c as in
Fig. 2, we obtain a new ideal triangulation T with one additional edge e0. Note that one
can read oﬀrelations of shape parameters between T and T directly from Fig. 2:
z′
a = zαzβ, z′
b = 1 −1/zβ
1 −zα
, z′
c = 1 −1/zα
1 −zβ
and zα = 1 −1/z′
b
1 −z′c
, zβ = 1 −1/z′
c
1 −z′
b
(46)
with the gluing equation z′
az′
bz′
c = 1 for the edge e0.
We ﬁrst consider the ﬂattening part of the deﬁnition (22). A combinatorial ﬂattening of
T satisﬁes the equation f ′
a + f ′
b + f ′
c = 2 (coming from the edge e0) and determines one of
T by
fα = fb + f ′′
c ,
f ′
α = f ′′
a + fc
f ′′
α = fa + f ′′
b ,
fβ = f ′′
b + fc,
f ′
β = f ′′
a + fb,
f ′′
β = fa + f ′′
c .
(47)
Then a straightforward computation shows that

□
ζ □f □
a
a
ζ
□f □
b
b
ζ □f □
c
c
= ±zα(1 −zα)zβ(1 −zβ)
1 −zαzβ

□
ζ □f □
α
α
ζ
□f □
β
β
.
(48)
Moreover, combining Equation (37) with (46), one checks that

□
G
□(t)aζ □
a

□
G
□(t)bζ □
b

□
G
□(t)cζ □
c

⎛
⎜⎜⎝
1
zαzβ
1
zαzβ −1
1
zαzβ −1
0
zβ(1−zα)(1−zαzβ)
1−zβ
0
0
0
zα(1−zβ)(1−zαzβ)
1−zα
⎞
⎟⎟⎠
= Q
⎛
⎝
1
0
0
∗

□
G□(t)αζ □
α

□
G□(t)βζ □
β
⎞
⎠
⎛
⎝
1
0
0
0 zαzβ(1 −zα)
zα(1 −zα)
0 zβ(1 −zβ) zαzβ(1 −zβ)
⎞
⎠,
where the determinant of the 3 × 3 matrix in the left (resp., right) hand side is (1 −zαzβ)2
(resp., zα(zα −1)zβ(zβ −1)(1 −zαzβ)). Combining this fact with the equation (48) and the
fact that det Q = 1, we conclude that τ CS(T , t) = ±τ CS(T , t).
⊓⊔
Proof of Theorem 1.7 Using Equation (28) and the fact that a combinatorial ﬂattening of
T (n) is simply given by n copies of that of T , it follows that
τ CS(T (n), tn) = det

k∈Z

□
G(n)□
k
diag(ζ □, . . . , ζ □)

tnk

·
⎛
⎝
N

j=1
ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
⎞
⎠
−n
(49)
= det
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
W0
W1 · · · Wn−2 Wn−1
tnWn−1 W0 · · · Wn−3 Wn−2
...
...
...
...
tnW2
tnW3 · · ·
W0
W1
tnW1
tnW2 · · · tnWn−1
W0
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
·
⎛
⎝
N

j=1
ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
⎞
⎠
−n
(50)
where Wr = 

k∈Z

□G□
nk+r diag(ζ □) tnk for 0 ≤r ≤n −1.
The block matrix in the equation (50) is called a factor block circulant matrix where
the factor is diag(tn, . . . , tn). It is known that a factor block circulant matrix admits a
37
Page 18 of 23
block-diagonalization in terms of the representer P(z) = W0 + W1z + · · · + Wn−1zn−1:
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
W0
W1 · · · Wn−2 Wn−1
tnWn−1 W0 · · · Wn−3 Wn−2
...
...
...
...
tnW2
tnW3 · · ·
W0
W1
tnW1
tnW2 · · · tnWn−1
W0
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
= V
⎛
⎜⎜⎜⎜⎝
P(t)
P(ω t)
...
P(ωn−1 t)
⎞
⎟⎟⎟⎟⎠
V −1
(51)
where ω is a primitive n-th root of unity and V is a block Vandermonde matrix
V =
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
I
I
· · ·
I
H0
H1
· · · Hn−1
H2
0
H2
1
· · · H2
n−1
...
...
...
Hn−1
0
Hn−1
1
· · · Hn−1
n−1
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
,
Hi = ωi diag(t, . . . , t).
(52)
We refer to [24] for details. In particular, we have
det
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
W0
W1 · · · Wn−2 Wn−1
tnWn−1 W0 · · · Wn−3 Wn−2
...
...
...
...
tnW2
tnW3 · · ·
W0
W1
tnW1
tnW2 · · · tnWn−1
W0
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
=

ωn=1
det P(ω t)
(53)
where, by deﬁnition,
P(ω t) =
n−1

r=0
Wr(ω t)r
=
n−1

r=0

k∈Z

□
G□
nk+rdiag(ζ □)(ωt)nk

(ωt)r
=
n−1

r=0

k∈Z

□
G□
nk+rdiag(ζ □)

tnk+rωnk+r
=

k∈Z

□
G□
k diag(ζ □)

(ω t)k
(since ωn = 1).
Combining the above calculations, we obtain
τ CS(T (n), tn) =

ωn=1
det


k∈Z

□G□
k diag(ζ □) (ω t)k
N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
=

ωn=1
τ CS(T , ω t).
(54)
⊓⊔
Proof of Theorem 1.8 Let R(t) = 

□G□(t) diag(ζ □) and Ri(t) denote its i-th row. Since
the sum of all rows of G□(1) = G□is (2, . . . , 2) and ζj + ζ ′
j + ζ ′′
j = 0, the sum R1(1) +
· · · + RN(1) is a zero vector. It follows that det R(1) = 0 and thus τ CS(T , 1) = 0.
Since the determinant is a multilinear map, we have
∂
∂t

t=1
det R(t) =
N

i=1
det
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
R1(1)
...
∂
∂t

t=1 Ri(t)
...
RN(1)
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
.
(55)
For i̸ = N, we exchange the i-th row
∂
∂t

t=1 Ri(t) with the N-th row RN(1) and replace
RN(1) by −R1(1) −· · · −RN−1(1). Then after some elementary row operations, we obtain
∂
∂t

t=1
det R(t) =
N

i=1
det
⎛
⎜⎜⎜⎜⎝
R1(1)
...
RN−1(1)
∂
∂t

t=1 Ri(t)
⎞
⎟⎟⎟⎟⎠
= det
⎛
⎜⎜⎜⎜⎝
R1(1)
...
RN−1(1)
∂
∂t

t=1

N
i=1 Ri(t)
⎞
⎟⎟⎟⎟⎠
.
(56)
Comparing the deﬁnitions of equation (20) and (22), it suﬃces to show that
∂
∂t

t=1

N
i=1 Ri(t)
agrees
with
1
2

□C□
λ diag(ζ □)
up
to
linear
combination
of
R1(1), . . . , RN(1).
Let  be the pre-image of the peripheral torus  under the covering map 
M →M.
Note that T induces a triangulation of  where vertices and triangles of  correspond
to edges and tetrahedra of T , respectively. For each triangle  of  corresponding to the
tetrahedron μk · j, we assign a corner parameter tk log z□
j to each corner of  according
to the quad type of j. Then the sum ri(t) of corner parameters around a vertex of 
corresponding to the edgeei is
ri(t) =
N

j=1

□
(G□(t))ij log z□
j .
(57)
It follows that (see Equation (6))
Ri(t) =

∂
∂z1 ri(t) · · ·
∂
∂zN ri(t)

.
(58)
We choose any lift λ of λ to . Since α(λ) = 0, λ is still a loop in . Up to homotopy,
we may assume that λ is an edge-path in  so that the surface S bounded by λ and μ ·λ
is triangulated. Here we view S as a closed cylinder whose boundary is consisted ofλ and
μ ·λ. Let cλ(t) (resp., ˇcλ(t)) be the sum of corner parameters in S that are adjacent (resp.,
not adjacent) to λ. By deﬁnition, the equation cλ(1) = 0 represents the completeness
equation of λ. Hence,

□
C□
λ diag(ζ □) =

∂
∂z1 cλ(1) · · ·
∂
∂zN cλ(1)

.
(59)
Also, since S consists of triangles and ζj + ζ ′
j + ζ ′′
j = 0 for all j, we have
∂
∂zj
(cλ(t) + ˇcλ(t)) = 0.
(60)
On the other hand, tcλ(t) is the sum of corner parameters adjacent to μ ·λ and not in S. It
follows that the sum of corner parameters around vertices in S\λ is given by tcλ(t)+ ˇcλ(t).
Since S\λ is a fundamental domain of , exactly two vertices in S \λ correspond to a lift
37
Page 20 of 23
of ei for each 1 ≤i ≤N. It follows that
tcλ(t) + ˇcλ(t) =
N

i=1
(tai + tbi) ri(t).
(61)
for some ai and bi ∈Z and thus
∂
∂t

t=1
(tcλ(t) + ˇcλ(t)) =
N

i=1
(ai + bi)ri(1) + 2 ∂
∂t

t=1
N

i=1
ri(t).
(62)
Taking the partial derivative with respect to zj, we obtain
∂
∂t

t=1
∂
∂zj
N

i=1
ri(t) = 1
2
∂
∂zj
∂
∂t

t=1
(tcλ(t) + ˇcλ(t)) −1
2
N

i=1
(ai + bi) ∂
∂zj
ri(1)
(63)
= 1
2
∂
∂zj
cλ(1) −1
2
N

i=1
(ai + bi) ∂
∂zj
ri(1) ,
(64)
where the second equation is followed from the equation (60) with the fact tcλ(t) +
ˇcλ(t) = (t −1)cλ(t) + cλ(t) + ˇcλ(t). Combining the equations (58), (59), and (64), we
obtain the desired result that ∂
∂t

t=1

N
i=1 Ri(t) agrees with 1
2

□C□
λ diag(ζ □) up to linear
combination of R1(1), . . . , RN(1):
∂
∂t

t=1
N

i=1
Ri(t) = 1
2

□
C□
λ diag(ζ □) + 1
2
N

i=1
(ai + bi)Ri(1).
(65)
⊓⊔
Remark 4.1 Rewriting Equation (65) in terms of NZ matrices, we have
Xλ =
⎛
⎜⎜⎜⎜⎜⎝
x1(1)
...
xN−1(1)
2 d
dt

t=1 (x1(t) + · · · + xN(t))
⎞
⎟⎟⎟⎟⎟⎠
for X = A and B where x1(t), . . . , xN(t) are the rows of X(t).
Proof of Corollary 1.9 The statement is equivalent to
det

A(t) diag(ζ) + B(t) diag(ζ ′′)

= εtr det

A(1/t) diag(ζ) + B(1/t) diag(ζ ′′)

(66)
forsomeε = ±1andsomeintegerr andsomechoiceofquadsofT .Wemakesuchachoice
such that B is non-singular. This is always possible; see [6, App.A]. Then, det B(t)̸ = 0,
since B(1) = B. Conjecture 1.4 implies that det B(t) = εtr det B(1/t)̸ = 0. This, combined
with Theorem 1.2 gives
det

A(t) diag(ζ) + B(t) diag(ζ ′′)

= det B(t) det

B(t)−1A(t) + diag(ζ ′′/ζ)

det(diag(ζ))
= εtr det B(1/t) det

B(1/t)−1A(1/t) + diag(ζ ′′/ζ)

det(diag(ζ))
= εtr det

A(1/t) diag(ζ) + B(1/t) diag(ζ ′′)

Note that Theorem 1.2 implies that B(t)−1A(t) = (B(1/t)−1A(1/t))T which is used in the
second equality above.
⊓⊔
We end this section by giving a proof of Equation (26). Taking the derivative of Equa-
tion (25) at t = 1 and then simplifying the result by Theorem 1.8, we obtain
τ CS
λ (T (n))
τ CS
λ (T )
= 1
n

ωn=1
ω̸=1
τ CS(T , w)
(67)
which is equivalent to Equation (26) due to Theorem 4.1 of [23] (explicitly, the ratio
τ CS
λ (T )/τ CS
μ (T ) is the cusp shape of M and τ CS
λ (T (n))/τ CS
μ (T (n)) is n times of that).
