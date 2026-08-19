---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae Takeshi MORITA∗"
section_id: sec-006-36-the-connection-formula-of-the-q-airy-function
section_title: "The connection formula of the q-Airy function"
section_number: 3.6
pages: 12-14
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae Takeshi MORITA∗ — We show connection formulae of local solutions of the Ramanu jan equation between the origin and the"
---
Applying the q-Borel transformation in 3.5 to the equation (12) and using
lemma 3, we obtain the ﬁrst order q-diﬀerence equation
g(qτ) = (1 + q2τ)(1 −q2τ)g(τ).
Since g(0) = 1, g(τ) is given by an inﬁnite product
g(τ) = 1
(−q2τ;q)∞(q2τ;q)∞
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
where 0 <r<r 0 := 1/ |q2|. We can culculate the residue from lemma 4.
12
Lemma 4. For any k ∈ N, λ ∈ C∗, one can get;
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
Theorem 1. For any x ∈ C∗,
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
4 Connection formula of the divergent series
2ϕ 0(0, 0; −;q, ·)
In this section, we show a connection formula of the divergent serie s 2ϕ 0.
This series appears in the second solution of the Ramanujan equatio n (9).
At ﬁrst, we review two q-exponential functions to consider our connection
formula.
4.1 Two diﬀerent q-exponential functions
In this section, we review two diﬀerent q-exponential functions from the
viewpoint of the connection problems. One of the q-exponential function
eq(x) is given by
eq(x) := 1ϕ 0(0; −;q,x ) =
∑
n≥0
xn
(q;q)n
.
13
The other q-exponential function Eq(x) is
Eq(x) := 0ϕ 0(−; −;q, −x) =
∑
n≥0
q
n(n− 1)
2
(q;q)n
xn.
The function eq(x) satisﬁes the following ﬁrst order q-diﬀerence equation
{σq − (1 −x)}u(x) = 0
and Eq(x) satisﬁes
{(1 +x)σq − 1}u(x) = 0.
The limit q → 1 − 0 converges the exponential function
lim
q→1−0
eq (x(1 −q)) = lim
q→1−0
Eq (x(1 −q)) = ex.
In this sense, these functions considered as q-analogues of the exponential
function. It is known that there exists the relation between these functions:
eq(x)Eq(−x) = 1, e q− 1(x) = Eq(−qx).
But another relation has not known. We show the connection formu la be-
tween them and give alternate representation of eq(·).
