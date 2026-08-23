---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension"
section_id: sec-002-3-two-q-exponential-functions
section_title: "Two q-exponential functions"
section_number: 3
pages: 8-11
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
doc_brief: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension — We show connection formulae of local solutions of the Ramanu - jan equation between the origin and the"
---
We review two diﬀerent q-exponential functions eq(x) and Eq(x) to consider
the connection problem on the Ramanujan equation. In this section , we show
the relation between them. We review two diﬀerent q-exponential functions
from the viewpoint of the connection problems. One of the q-exponential
function eq(x) is given by
eq(x) := 1ϕ 0(0; −;q,x ) =
∑
n≥0
xn
(q;q)n
.
The other q-exponential function Eq(x) is
Eq(x) := 0ϕ 0(−; −;q, −x) =
∑
n≥0
q
n(n− 1)
2
(q;q)n
xn.
8
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
function. It is known that there exists the relation between these functions
[2]:
eq(x)Eq(−x) = 1, e q− 1(x) = Eq(−qx).
But another relation has not known. We show the connection formu la be-
tween them and give alternate representation of eq(x).
At ﬁrst, we show the following connection formula between eq(x) and
Eq(x).
Theorem 3.1. For any x ∈ C∗ \ [1;q],
eq(x) = (q;q)∞
θq(−x)Eq
(
−q
x
)
where |x|< 1.
Proof. The function eq(x) and Eq(x) have inﬁnite product as follows:
eq(x) = 1
(x;q)∞
, |x|< 1
and
Eq(x) = ( −x;q)∞.
We remark that eq(x) can be described as
eq(x) = 1
θq(−x)
(
q, q
x;q
)
∞
= (q;q)∞
θq(−x)Eq
(
−q
x
)
where |x|< 1. We obtain the conclusion.
9
Therefore, these q-exponential functions are related by the connection
formula between the origin and the inﬁnity. If we replace x byx/q , we obtain
the following lemma. This is useful to consider the connection problem in
the last section.
Lemma 3.2. For any x ∈ C∗ \ [1;q], the function eq(x/q ) has the following
alternate representation.
eq
(x
q
)
= (q;q)∞
θq
(
− x
q
) 0ϕ 1
(
−;q;q2, q5
x2
)
− (q;q)∞
θq
(
− x
q
) q2
(1 −q)x 0ϕ 1
(
−;q3;q2, q7
x2
)
.
Proof. From theorem 3.1,
1ϕ 0
(
0; −;q, x
q
)
= (q;q)∞
θq
(
− x
q
) Eq
(
−q2
x
)
= (q;q)∞
θq
(
− x
q
) 0ϕ 0
(
−; −;q, q2
x
)
.
Here,
0ϕ 0
(
−; −;q, q2
x
)
=
∑
k≥0
1
(q;q)k
(−1)kq
k(k− 1)
2
(q2
x
) k
and we remark that ( a;q)2k = (a,aq ;q2)k [2]. By separating the terms with
even and odd k ≥ 0, we obtain the conclusion.
By separating the terms with r-th order terms, we have the following
corollary.
Corollary 3.3. For any x ∈ C∗ \ [1;q], we have
eq(x) = (q;q)∞
θq(−x)
[
0ϕ r−1
(
−;q,q 2,...,q r−1;qr, (qr)
r− 1
2
(q
x
) r)
+ (−1)
1 −q
q
x 0ϕ r−1
(
−;q2,...,q r−1,q r+1;qr, (qr)
r+1
2
(q
x
) r)
+ · · · + (−1)r−1q
(r− 1)(r− 2)
2
(1 −q)(1 −q2)... (1 −qr−1)
(q
x
) r−1
0ϕ r−1
(
−;qr+1,...,q 2(r−1);qr, (qr)
3(r− 1)
2
(q
x
) r)]
.
10
