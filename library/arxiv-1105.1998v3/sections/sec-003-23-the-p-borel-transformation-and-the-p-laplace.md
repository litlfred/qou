---
doc_id: arxiv-1105.1998v3
doc_title: ""
section_id: sec-003-23-the-p-borel-transformation-and-the-p-laplace
section_title: "The p-Borel transformation and the p-Laplace transformation"
section_number: 2.3
pages: 3-6
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
doc_brief: "A Connection Formula of the Hahn–Exton q-Bessel Function Takeshi MORITA — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
between the origin and the infinity. These transformations are useful to consider connection
problems. We assume that q ∈ C∗ satisfies 0 < |q| < 1 and q = p2. The q-difference operator σq
is given by σqf (x) = f (qx).
2.1 The theta function of Jacobi
Before we study connection problems, we review the theta fun ction of Jacobi. The theta function
of Jacobi is given by the following series:
Deﬁnition 1. For any x ∈ C∗,
θq(x) = θ(x) :=
∑
n∈ Z
q
n(n− 1)
2 xn.
4 T. Morita
We denote by θq(x) or more shortly θ(x). The theta function satisfies Jacobi’s triple product
identity:
θ(x) =
(
q, −x, − q
x ; q
)
∞
.
The theta function satisfies the q-difference equation as follows
θ(qkx) = q− k(k− 1)
2 x− kθ(x), ∀ x ∈ C∗.
The theta function has the inversion formula xθ(1/x ) = θ(x). For all fixed λ ∈ C∗, we define
a q-spiral [λ; q] := λq Z = {λq k : k ∈ Z}. We remark that θ
(
λq k/x
)
= 0 if and only if x ∈ [−λ; q].
2.2 The Hahn–Exton q-Bessel function
The Hahn–Exton q-Bessel function is defined by
J (3)
ν (x; q) := (qν+1; q)∞
(q; q)∞
xν∑
n≥ 0
(−1)nq
n(n− 1)
2
(qν+1, q ; q)n
(
qx2)n
.
The function J (3)
ν (x; q) satisfies the q-difference equation
[
σ 2
p −
{
(pν + p− ν ) − x2p2− ν}
σp + 1
]
y(x) = 0 . (5)
If we replace ν by −ν and x by xp− ν, we obtain J (3)
− ν (xp− ν ; q) which is another solution of (5)
around the origin. This solution corresponds to the classic al Neumann function Yν (x) [5]. We
consider the behavior of equation (5) around the infinity. W e set 1 /t , formally t2 ↦→t and
z(t) = y(1/t ). Then z(t) satisfies
[
σ 2
p −
{
(pν + p− ν) − p− 2− ν
t
}
σp + 1
]
z (t) = 0 . (6)
We set E(t) = 1 /θ p(−pν+2t) and f (t) = ∑
n≥ 0
antn, a0 = 1. We assume that z(t) can be
described as
z(t) = E(t)f (t) = 1
θp(−pν+2t)

∑
n≥ 0
antn

 .
Since E(t) satisfies the following q-difference equation
σpE(t) = −pν+2tE(t), σ 2
pE(t) = p2ν+5t2E(t),
we can check out that the function f (t) satisfies the equation
{
p2ν+5t2σ 2
p + pν+2(pν + p− ν )tσ p − σp + 1
}
f (t) = 0 . (7)
2.3 The p-Borel transformation and the p-Laplace transformation
We define the p-Borel transformation and the p-Laplace transformation to solve the equation (7),
following Zhang [8].
A Connection Formula of the Hahn–Exton q-Bessel Function 5
Deﬁnition 2. For f (t) = ∑
n≥ 0
antn, the p-Borel transformation is defined by
g(τ) = ( Bpf ) (τ) :=
∑
n≥ 0
anp− n(n− 1)
2 τn,
and the p-Laplace transformation is given by
(Lpg) (t) := 1
2πi
∫
|τ|=r
g(τ)θp
( t
τ
) dτ
τ .
Here, r0 > 0 is enough small number.
The p-Borel transformation is considered as a formal inverse of t he p-Laplace transformation.
Lemma 1. We assume that the function f can be p-Borel transformed to the analytic func-
tion g(τ) around τ = 0. Then,
Lp ◦ Bpf = f.
Proof . We can prove this lemma calculating residues of the p-Laplace transformation around
the origin. ■
The p-Borel transformation has the following operational relat ion.
Lemma 2. For any l, m ∈ Z≥ 0,
Bp
(
tmσ l
p
)
= p− m(m− 1)
2 τmσ l− m
p Bp.
Applying the p-Borel transformation to the equation (7) and using Lemma 2, g(τ) satisfies
the first order difference equation
g(pτ) =
(
1 + p2ν+2τ
)(
1 + p2τ
)
g(τ).
Since g(0) = 1, we get an infinite product of g(τ):
g(τ) = 1
(−p2ν+2τ; p)∞ (−p2τ; p)∞
.
Then g(τ) has single poles at
{
−p− 2ν− 2− k, −p− 2− k; k ∈ Z≥ 0
}
.
We set
0 < r < r 0 := min
{ 1
|p2ν+2| , 1
|p2|
}
.
and choose the radius r > 0 such that 0 < r < r 0. By Cauchy’s residue theorem, the p-Laplace
transform of g(τ) is
f (t) = 1
2πi
∫
|τ|=r
g(τ)θp
( t
τ
) dτ
τ
= −
∑
k≥ 0
Res
{
g(τ)θp
( t
τ
)1
τ ; τ = −p− 2ν− 2− k
}
−
∑
k≥ 0
Res
{
g(τ)θp
( t
τ
)1
τ ; τ = −p− 2− k
}
,
where 0 < r < r 0. To calculate the residue, we use the following lemma.
6 T. Morita
Lemma 3. For any k ∈ N, λ ∈ C∗, we have
1. Res
{ 1
(τ /λ ; p)∞
1
τ : τ = λp − k
}
= (−1)k+1p
k(k+1)
2
(p; p)k(p; p)∞
,
2. 1
(λp − k; p)∞
= (−λ)− kp
k(k+1)
2
(λ; p)∞ (p/λ ; p)k
, λ ⁄∈pZ.
Summing up all of the residues, we obtain the convergent seri es f (t) as follows
f (t) = θp
(
−p2ν+2t
)
(p− 2ν , p ; p)∞
1ϕ 1
(
0, p 1+2ν ; p, x
)
+ θp
(
−p2t
)
(p2ν , p ; p)∞
1ϕ 1
(
0, p 1− 2ν ; p, p − 2ν x
)
,
where xt = 1. Therefore, we acquire the connection formula for z(t) = E(t)f (t).
