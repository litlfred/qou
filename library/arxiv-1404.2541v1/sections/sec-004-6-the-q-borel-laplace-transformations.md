---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q-diﬀerence equation and its higher order extension Takeshi MORITA∗"
section_id: sec-004-6-the-q-borel-laplace-transformations
section_title: "The q-Borel-Laplace transformations"
section_number: 6
pages: 13-19
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
doc_brief: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension Takeshi MORITA∗ — We show connection formulae of local solutions of the Ramanu - jan equation between"
---
In this section, we show a connection formula of the divergent serie s 2ϕ 0.
This series appears in the second solution of the Ramanujan equatio n (12).
At ﬁrst, we deﬁne two types of the q-Borel-Laplace transformations.
Deﬁnition. We assume that f (x) is a formal power series f (x) =∑
n≥0anxn,
a0 = 1.
13
1. The q-Borel transformation of the ﬁrst kind is
(
B+
qf
)
(ξ) :=
∑
n≥0
anq
n(n− 1)
2 ξn (=:ϕ (ξ)).
2. The q-Laplace transformation of the ﬁrst kind is
(
L+
q,λ ϕ
)
(x) := 1
1 −q
∫ λ ∞
0
ϕ (ξ)
θq
(ξ
x
) dqξ
ξ =
∑
n∈Z
ϕ (λq n)
θq
(λq n
x
) ,
here, this transformation is given by Jackson’s q-integral [2].
We also deﬁne the q-Borel-Laplace transformations of the second kind as
follows:
1. The q-Borel transformation of the second kind is
(B−
qf )(ξ) :=
∑
n≥0
anq− n(n− 1)
2 ξn (=:g(ξ)).
2. The q-Laplace transformation of the second kind is
(
L−
qg
)
(x) := 1
2πi
∫
|ξ|=r
g(ξ)θq
(x
ξ
) dξ
ξ ,
where r >0 is enough small number.
We remark that the q-Borel transformation B+
q is formal inverse of the
q-Laplace transformation L+
q,λ as follows;
Lemma 6.1. For any entire function f (x), we have
L+
q,λ ◦ B+
qf =f.
Theq-Borel transformation B−
q also can be considered as a formal inverse
of the q-Laplace transformation.
Lemma 6.2. We assume that the function f can be q-Borel transformed to
the analytic function g(ξ) aroundξ = 0. Then, we have
L−
q ◦ B−
qf =f.
14
Proof. We can prove this lemma calculating residues of the q-Laplace trans-
formation around the origin.
The q-Borel transformation B−
q has following operational relation.
Lemma 6.3. For any l,m ∈ Z≥0,
B−
q (tmσ l
q) = q− m(m− 1)
2 τmσ l−m
q B−
q.
In the following subsection, we apply these resummation methods to deal
with the connection problem.
7 The connection formula of the series 2ϕ 0(0, 0; −;q, ·)
The aim of this section is to give a proof for the following theorem;
Theorem 7.1. For any x ∈ C∗ \ [−λ;q],
θq(x)2f0
(
0, 0; −;q, −x
q
)
= (q;q)∞
θq(x)θq2
(
− λ 2
qx
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q;q2, q2
x
)
+ (q;q)∞
1 −q
θq(x)θq2
(
− λ 2
x
)
θq
(
− λ
q
)
θq
(λ
x
)
λ
x
1ϕ 1
(
0;q3;q2, q3
x
)
.
We give the proof of theorem 7.1.
Proof. We apply theq-Borel transformation B+
q to the divergent seriesv(x) =
2ϕ 0(0, 0; −;q, −x/q ). We obtain
(
B+
qv
)
(ξ) = 1ϕ 0
(
0; −;q, ξ
q
)
=:ϕ (ξ).
From lemma 3.2,
ϕ (ξ) = (q;q)∞
θq
(
− ξ
q
) 0ϕ 1
(
−;q;q2, q5
ξ2
)
− (q;q)∞
θq
(
− ξ
q
) q2
(1 −q)ξ
0ϕ 1
(
−;q3;q2, q7
ξ2
)
where |ξ/q |< 1.
15
We apply the q-Laplace transformation L+
q,λ to ϕ (ξ):
(
L+
q,λ ϕ
)
(x) =
∑
n∈Z
ϕ (λq n)
θq
(λq n
x
) =
∑
n∈Z
1ϕ 0
(
0; −;q, λq n
q
)
θq
(λq n
x
)
= (q;q)∞
θq
(
− λ
q
)
θq
(λ
x
)
∑
n−m∈Z
(q2)
(n− m)(n− m− 1)
2
(
−λ 2
qx
) n−m
×
∑
m≥0
(−1)m(q2)
m(m− 1)
2
(q;q2;q2)m
(q2
x
) m
− (q;q)∞
θq
(
− λ
q
)
θq
(λ
x
)
q2
(1 −q)λ
∑
n−m∈Z
(q2)
(n− m)(n− m− 1)
2
(
− λ 2
q2x
) n−m
×
∑
m≥0
(−1)m(q2)
m(m− 1)
2
(q3,q 2;q2)m
(q3
x
) m
.
Therefore,
2f0
(
0, 0; −;q, −x
q
)
= L+
q,λ ◦ B+
q 2ϕ 0
(
0, 0; −;q, −x
q
)
= (q;q)∞
θq2
(
− λ 2
qx
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q;q2, q2
x
)
+ (q;q)∞
1 −q
θq2
(
− λ 2
x
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q3;q2, q3
x
)
.
We obtain the conclusion.
Remark. By theorem 7.1, we have
˜u2(x,λ ) = ˜C21v1(x) + ˜C22v2(x),
where
˜C21(x) = (q;q)∞θq2(−qx/λ 2)θq2(x)
θq(−q/λ )θq(x/λ )θq(x)
and
˜C22(x) = (q;q)∞θq2(−x/λ 2)θq2(x/q )
θq(−1/λ )θq(x/λ )θq(x/q ) .
This is a half of our connection formula.
16
8 The q-Airy equation around the inﬁnity and
the connection formula
We consider the behavior of the equation (13) around the inﬁnity. W e set
x = 1/t and z(t) = u(1/t ). Then z(t) satisﬁes
(
−σ 2
q + 1
q2tσq + 1
)
z(t) = 0.
We set E(t) = 1/θ (−q2t) and f (t) = ∑
n≥0antn, a 0 = 1. We assume that
z(t) can be described as
z(t) = E(t)f (t) = 1
θ(−q2t)
(∑
n≥0
antn
)
.
The function E(t) has the following property;
Lemma 8.1. For any t ∈ C∗,
σqE(t) = −q2tE(t), σ 2
q E(t) = q5t2E(t).
From this lemma, f (t) satisﬁes the following equation
(
−q5t2σ 2
q −σq + 1
)
f (t) = 0. (14)
Since (14) is the same as (10) for K = −q5, we obtain
f (t) = 0ϕ 1(−; 0;q2,q 5t2) = A q2(−q3t2).
We show a connection formula for f (t). In order to obtain a connection
formula, we need the q-Borel transformation and the q-Laplace transfor-
mation following Zhang [17]. Applying the q-Borel transformation to the
equation (10) and using lemma 6.3, we obtain the ﬁrst order q-diﬀerence
equation
g(qτ) = (1 + q2τ)(1 −q2τ)g(τ).
Since g(0) = 1, g(τ) is given by an inﬁnite product
g(τ) = 1
(−q2τ;q)∞(q2τ;q)∞
17
which has single poles at
{
τ;τ = ±q−2−k, ∀k ∈ Z≥0
}
.
By Cauchy’s residue theorem, the q-Laplace transform of g(τ) is
f (t) = 1
2πi
∫
|τ|=r
g(τ)θ
(t
τ
) dτ
τ
= −
∑
k≥0
Res
{
g(τ)θ
(t
τ
) 1
τ ;τ = −q−2−k
}
−
∑
k≥0
Res
{
g(τ)θ
(t
τ
) 1
τ ;τ =q−2−k
}
where 0 <r<r 0 := 1/ |q2|. We can culculate the residue from lemma 8.2.
Lemma 8.2. For any k ∈ N, λ ∈ C∗, we have:
1. Res
{ 1
(τ/λ ;q)∞
1
τ :τ =λq −k
}
= (−1)k+1q
k(k+1)
2
(q;q)k(q;q)∞
,
2. 1
(λq −k;q)∞
= (−λ)−kq
k(k+1)
2
(λ;q)∞ (q/λ ;q)k
, λ ⁄∈qZ.
Summing up all of residues, we obtain
f (t) = θ(q2t)
(q, −1;q)∞
1ϕ 1
(
0, −q;q, 1
t
)
+ θ(−q2t)
(q, −1;q)∞
1ϕ 1
(
0, −q;q, −1
t
)
.
We obtain a connection formula for z(t) = E(t)f (t). Finally, we acquire
the following connection formula between the Ramanujan function a nd the
q-Airy function.
Theorem 8.3. For any x ∈ C∗,
Aq2
(
−q3
x2
)
= 1
(q, −1;q)∞
{
θ
(x
q
)
Aiq(−x) +θ
(
−x
q
)
Aiq(x)
}
.
Here, both A q(x) and Ai q(x) are deﬁned by convergent series on whole of
the complex plain. The connection formula above is valid for any x ∈ C∗.
18
