---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential asymptotics, trans-series and generalized Borel summation for analytic nonlinear rank one systems of ODE’s Ovidiu Costin ∗"
section_id: sec-002-the-convolution-equation-away-from-stokes-rays
section_title: "The convolution equation away from Stokes rays"
section_number: null
pages: 12-30
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
doc_brief: "Exponential asymptotics, trans-series and generalized Borel summation for analytic nonlinear rank one systems of ODE’s Ovidiu Costin ∗ — For analytic nonlinear systems of ordinary diﬀerential equa"
---
For any star-shaped set E in the complex plane containing the origin (i.e.,
a region such that the origin can be connected with any other point in E
by a straight line segment contained in E) we denote by Lray(E) the set of
functions which are locally integrable along each ray in E.
Proposition 6 There is a unique solution of (1.25) in Lray(D) (cf. (1.11))
namely Y0 =B˜y0.
This solution is analytic in D, Laplace transformable along any ray Φ
contained inD andLφY0 is a solution of (1.1).
For the proof we need a few more results.
Remark 7 There is a constant K > 0 (independent of p and l) such that
for all p∈ C and all l≥ 0
|Gl(p)|∧ < Kµ |l|eµ|p| (2.1)
12
for µ > max{ξ−1
0 , y−1
0 } (cf. (1.21)) ( |f|∧ := max 1..n{|f1|, ..,|fn|} is an Eu-
clidean norm; for the deﬁnition of G see (1.23), (1.21) and (1.1)).
Proof.
From the analyticity assumption it follows that
|gm,l|∧ < Const µm+|l| (2.2)
where the constant is independent on m and l.
Then, by (1.23),
|Gl(p)|∧ < Const µ|l|+1 eµ|p|− 1
µ|p| < Const µ|l|+1eµ|p|
Consider the ray segments
Φ D ={αeiφ : 0≤ α < D} (2.3)
and along Φ D the L1 norm with exponential weight
‖f‖b,Φ =‖f‖b :=
∫
Φ
e−b|p||f (p)||dp| =
∫ D
0
e−bt|f (teiφ)|dt (2.4)
and the space
L1
b(Φ D) :={f :‖f‖b <∞}
(if D < ∞, L1
b(Φ D) = L1
loc(Φ D)). We mention the following elementary
property:
Remark 8 The Laplace transformL is a continuous operator from L1
b(Φ D)
to the space of analytic functions in the half plane ℜ(x) > b with the uniform
norm.
LetK∈ C be a bounded domain, diam ( K) = D < ∞. On the space
of continuous functions on K we take the uniform norm with exponential
weight:
‖f‖u := D sup
p∈K
{|f (p)|e−b|p|} (2.5)
(which is equivalent to the usual uniform norm).
13
LetO⊂D , O∋ 0 be a star-shaped, open set , diam(O) = D containing
a ray segment Φ. Let A be the space of analytic functions f inO such that
f (0) = 0, endowed with the norm (2.5).
Proposition 9 The spaces L1
b(Φ D) andA are Banach algebras with respect
to the usual addition of functions and the convolution (1.20 ). Furthermore
‖f∗ g‖b≤‖ f‖b‖g‖b (f, g∈ L1
b(Φ D))
‖f∗ g‖u≤‖ f‖u‖g‖u (f, g∈A )
‖f∗ g‖u≤‖ f‖u‖g‖b (f∈ C(Φ D), g∈ L1
b(Φ D)
(2.6)
(D =∞ is allowed in the ﬁrst inequality).
With F (s) := f (seiφ) and G(s) := g(seiφ) we have:
∫ D
0
dte−bt
⏐
⏐
⏐
⏐
∫ t
0
dsF (s)G(t− s)
⏐
⏐
⏐
⏐≤
∫ D
0
dte−bt
∫ t
0
ds|F (s)G(t− s)| =
∫ D
0
∫ D−v
0
e−b(u+v)|F (v)||G(u)|dudv≤
∫ D
0
∫ D
0
e−b(u+v)|F (v)||G(u)|dudv =‖f‖b‖g‖b
(2.7)
On the other hand, for f, g∈A we have f∗ g∈A . Also,
‖f∗ g‖u = D sup
p∈O
e−b|p|
⏐
⏐
⏐
⏐
∫ p
0
f (s)g(p− s)ds
⏐
⏐
⏐
⏐≤
D sup
p∈O
∫ |p|
0
⏐
⏐f (tei arg p)e−btg(p− tei arg p)e−b(|p|−t)⏐
⏐dt (2.8)
which is less than both ‖f‖u‖g‖u and‖f‖u‖g‖b.
Remark 10 For f inA or f in L1
b(Φ D),
‖f‖u,b→ 0 as b→∞ (2.9)
where‖‖u,b is either of the ‖‖u or‖‖b and D =∞ is allowed in the second
case.
14
For‖‖b, Eq. (2.9) is an immediate consequence of the dominated conver-
gence theorem whereas for ‖‖u it follows from the deﬁnition of A.
Corollary 11 Let f be continuous along Φ D, D < ∞ and g∈ L1
b(Φ D).
Given ǫ > 0 there exists a large enough b and K = K(ǫ, Φ D) such that for
all k
‖f∗ g∗k‖u < K ǫ k
By Remark 10 we can choose b = b(ǫ, Φ D) so large that ‖g‖b < ǫ. Then,
by Proposition 9 and Eq. (2.5) we have:
⏐
⏐
⏐
⏐
⏐
∫ peiφ
0
f (peiφ− s)g∗k(s)ds
⏐
⏐
⏐
⏐
⏐≤ D−1eb|p|‖f‖u
∫ peiφ
0
e−b|s||g∗k(s)||ds|≤
D−1eb|p|‖f‖u‖g‖k
b < K ǫ k
Remark 12 By (2.1), for any b > µ , and Φ D⊂ C, D≤∞
‖Gl‖b≤ Kµ |l|
∫ ∞
0
|dp|e|p|(µ−b) = K µ|l|
b− µ (2.10)
where, to avoid cumbersome notations, we write
f∈ L1
b(Φ D) iﬀ ‖|f|∧‖b∈ L1
b(Φ D) (2.11)
(and similarly for other norms of vector functions).
Proof of Proposition 6.
We ﬁrst show existence and uniqueness in Lray(D) which amounts to
nothing more then existence and uniqueness along each Φ D⊂D .
Then we show that for large enough b there exists a unique solution of
(1.25) in L1
b(Φ ∞). Since this solution is also in L1
loc(Φ ∞) it follows that our
(unique) L1
loc solution is Laplace transformable. Analyticity is proven by
ﬁnding the solution as a ﬁxed point of a contraction with respect to t he
uniform norm in a suitable space of analytic functions.
15
Proposition 13 i) For Φ D∈D and large enough b, the operator
N1 := Y(p)↦→(ˆΛ− p)−1
(
F0(p)− ˆB
∫ p
0
Y(s)ds +N (Y)(p)
)
(2.12)
is a contraction in a small enough neighborhood of the origin with respect to
‖‖u if D <∞ and with respect to ‖‖b for D≤∞ .
ii) For D≤∞ the operatorN given formally in (1.22) is continuous in
L1
loc(Φ D). The last sum in (1.22) converges uniformly on compact subse ts of
Φ D. N (L1
loc(Φ D))⊂ AC(Φ D), the absolutely continuous functions on Φ D.
Moreover, if vn→ v in‖‖b on Φ D, D≤∞ , then for b′≥ b large enough,
N (vn) exist and converge in ‖‖b′ to v.
The last statements amounts to saying that N is continuous in the topol-
ogy of the inductive limit of the L1
b.
Proof.
Since ˆΛ and ˆB are constant matrices,
‖N1(Y)‖u,b≤ Const(Φ) (‖F0‖u,b +‖Y‖u,b‖1‖b +‖N (Y)‖u,b) (2.13)
As both ‖1‖b and‖F0‖u,b are O(b−1) for large b, the fact that N1 maps a
small ball into itself follows from the following Remark.
Remark 14 Let ǫ > 0 be small enough. Then, there is a K such that for
large b and all v such that ‖v‖u,b =: δ < ǫ ,
‖N (v)‖u,b≤ K
(
b−1 +‖v‖u,b
)
‖v‖u,b (2.14)
By (2.2) and (2.10), for large b and some positive constants C1, .., C5,
‖N (v)‖u,b≤ C1

∑
|l|≥1
‖Gl‖b‖v‖|l|
u,b +
∑
|l|≥2
‖g0,l‖b‖v‖|l|
u,b


≤ C2
b

∑
|l|≥1
µ|l|
b− µδ|l| +
∑
|l|≥2
µ|l|δ|l|

≤
(
C2
∞∑
m=1
+
∞∑
m=2
)
µmδm∑
|l|=m
1
≤
( C4
b + µδ
) ∞∑
m=1
µmδm(m + 4)n≤
( C4
b + µδ
)
C5δ
16
(2.15)
To show thatN1 is a contraction we need the following:
Remark 15
‖hl‖ :=‖(f + h)∗l− f ∗l‖≤| l| (‖f‖ +‖h‖)|l|−1‖h‖ (2.16)
where‖‖ =‖‖u or‖‖b.
This estimate will be useful to us when h is a “small perturbation”. The
proof of (2.16) is a simple induction on l, with respect to the lexicographic
ordering. For |l| = 1, (2.16) is trivial; assume (2.16) holds for all l < l1 and
that l1 diﬀers from its predecessor l0 at the position k (we can take k = 1),
i.e., ( l1)1 = 1 + ( l0)1. We have:
‖(f + h)∗l1− f ∗l1‖ =‖(f + h)∗l0∗ (f1 + h1)− f ∗l1‖ =
‖(f ∗l0 + hl0)∗ (f1 + h1)− f ∗l1‖ =‖f ∗l0∗ h1 + hl0∗ f1 + hl0∗ h1‖≤
‖f‖|l0|‖h‖ +‖hl0‖‖f‖ +‖hl0‖‖h‖≤
‖h‖
(
‖f‖|l0| +|l0|(‖f‖ +‖h‖)|l0|)
≤
‖h‖(|l0| + 1)(‖f‖ +‖h‖)|l0| (2.17)
Remark 16 For small δ and large enough b,N1 deﬁned in a ball centered
at zero, of radius δ in the norms ‖‖u,b is contractive.
By (2.13) and (2.14) we know that the ball is mapped into itself for larg e
b. Let ǫ > 0 be small and let f, h be such that ‖f‖ < δ− ǫ,‖h‖ < ǫ . Using
(2.16) and the notations (1.25) (2.13) and ‖‖ =‖‖u,b we obtain, for some
positive constants C1, .., C4 and large b,
‖N1(f + h)−N 1(f)‖≤ C1‖

∑
|l|≥2
g0,l· +
∑
|l|≥1
Gl∗

(
(f + h)∗l− f ∗l)
‖≤
17
C2‖h‖

∑
|l|≥1
µ|l|
b− µ|l‖δ|l|−1 +
∑
|l|≥2
|l|µ|l|δ|l|−1

 < (C3b−1 + C4δ)‖h‖
(2.18)
To ﬁnish the proof of Proposition 13 take v∈A . Given ǫ > 0 we can
choose b large enough (by Remark 10) to make ‖v‖u < ǫ . Then the sum in
the formal deﬁnition of N is convergent in A, by (2.15). Now, if D < ∞
L1
loc(Φ D) = L1
b(Φ D) for any b > 0. If vn → v in L1
b(Φ D), we choose ǫ
small enough, then b large so that ‖v‖b < ǫ, and ﬁnally n0 large so that for
n > n 0‖vn− v‖b < ǫ (note that ‖‖b decreases w.r. to b) thus ‖vn‖b < 2ǫ
and continuity (in L1
b(Φ D) as well as in L1
loc(Φ ∞)≡∪ k∈Φ ∞L1
b(0, k)) follows
from Remark 16. Continuity with respect to the topology of the indu ctive
limit of the L1
b is proven in the same way. It is straightforward to show that
N (L1
loc(Φ))⊂ AC(Φ).
P13
The fact that LφY0 is a solution of (1.1) follows from Proposition 13,
from Remark 8 and the elementary properties of L (see also the proof of
Proposition 28).
Since Y0(p) is analytic for small p, (LY0)(x) has an asymptotic series for
large x, which has to agree with ˜y0 sinceLY0 solves (1.1). This shows that
Y0 =B˜y0.
P 6
Remark 17 For any δ there is a constant K2 = K2(δ,|p|) so that for all l
we have
|Y∗l
0 (p)|∧≤ K2δ|l| (2.19)
The estimates (2.19) follow immediately from analyticity and from Coro l-
lary 11.
2.3 Behavior of Y 0(p) near p = 1.
Let Y0 be the unique solution in Lray(D) of (1.25) and let ǫ > 0 be small.
Deﬁne
18
H(p) :=
{ Y0(p) for p∈D ,|p| < 1− ǫ
0 otherwise and h(1− p) := Y0(p)− H(p)
(2.20)
In terms of h, for real z = 1− p, z < ǫ , the equation (1.25) reads:
− (1− z)h(z) = F1(z)− ˆΛ h(z) + ˆB
∫ z
ǫ
h(s)ds +N (H + h) (2.21)
where
F1(1− s) := F0(s)− ˆB
∫ 1−ǫ
0
H(s)ds
Proposition 18 i) For small ǫ, H∗l(1 + z) extends to an analytic function
in the disk Dǫ :={z :|z| < ǫ}. Furthermore, for any δ there is an ǫ and
a constant K1 := K1(δ, ǫ) such that for z ∈ Dǫ the analytic continuation
satisﬁes the estimate
|H∗l(1 + z)|∧ < K 1δl (2.22)
Proof.
The case|l| = 1 is trivial: H itself extends as the zero analytic function.
We assume by induction on |l| that Proposition 18 is true for all l,|l|≤ l
and show that it then holds for (e.g.) H1∗ H∗l, for all l,|l|≤ l.
H is analytic in an ǫ–neighborhood of [0 , 1− 2ǫ], and therefore so is H∗l.
Taking ﬁrst z∈ R+, z < ǫ , we have
∫ 1−z
0
H1(s)H∗l(1− z− s)ds =
∫ 1−ǫ
0
H1(s)H∗l(1− z− s)ds =
∫ 1/2
0
H1(s)H∗l(1− z− s)ds +
∫ 1−ǫ
1/2
H1(s)H∗l(1− z− s)ds (2.23)
The integral on [1 /2, 1− ǫ] is analytic for small z, since the argument of H∗l
varies in an ǫ-neighborhood of [0 , 1/2]; the integral on [0 , 1/2) equals
∫ 1−z
1/2−z
H1(1−z−t)H∗l(t)dt =
( ∫ 1/2
1/2−z
+
∫ 1−ǫ
1/2
+
∫ 1−z
1−ǫ
)
H1(1−z−t)H∗l(t)dt
(2.24)
19
In (2.24) the integral on [1 /2− z, 1/2] is clearly analytic in Dǫ, the following
one is the integral of an analytic function of the parameter z with respect to
the absolutely continuous measure H∗ldt whereas in the last integral, both
H∗l (by induction) and H1 extend analytically in Dǫ.
To prove now the the induction step for the estimate (2.22), ﬁx δ small
and let:
η < δ ; M1 := max
|p|<1/2+ǫ
|H(p)|∧; M2(ǫ) := max
0≤x≤1−ǫ
|H(p)|∧; ǫ < δ
4M1
(2.25)
Let K2 := K2(η; ǫ) be large enough so that (2.19) holds with η in place of δ
for real x∈ [0, 1−ǫ] and also in an ǫ neighborhood in C of the interval [0, 1/2+
2ǫ]. We use (2.19) to estimate the second integral in the decomposition (2.23)
and the ﬁrst two integrals on the r.h.s. of (2.24). For the last integr al in (2.24)
we use the induction hypothesis. If K1 > 2K2 (2M1 + M2), it follows that
|H∗l∗ H1|∧ is bounded by (the terms are in the order explained above):
M2(ǫ)K2ηl + M1K2ηl + M1K2ηl + (2ǫ)M1K1δl < K 1δl+1 (2.26)
Proposition 19 The equation (2.21) can be written as
−(1−z)h(z) = F(z)− ˆΛ h(z)+ ˆB
∫ z
ǫ
h(s)ds−
n∑
j=1
∫ z
ǫ
hj(s)Dj(s−z)ds (2.27)
where
F(z) :=N (H)(1− z) + F1(z) (2.28)
Dj =
∑
|l|≥1
ljGl∗ H∗¯lj
+
∑
|l|≥2
ljg0,lH∗¯lj
; ¯lj := (l1, l2, ..(lj− 1), ..ln) (2.29)
(cf. also (1.24)) extend to analytic functions in Dǫ (cf. Proposition 18).
Moreover, if H is a vector in L1
b(R+) then, for large b, Dj∈ L1
b(R+) and the
functions F(z) and Dj extend to analytic functions in Dǫ.
20
Proof.
Noting that ( Y0− H)∗2(1− z) = 0 for ǫ < 1/2 and z∈ Dǫ the result is
easily obtained by re-expanding N (H + h) since Proposition 18 guarantees
the uniform convergence of the series thus obtained. The proof t hat Dj∈ L1
b
for large b is very similar to the proof of (2.18). The analyticity properties
follow easily from Proposition 18, since the series involved in N (H) and Dj
converge uniformly for |z| < ǫ.
Consider again the equation (2.27). Let ˆΓ = ˆΛ− (1− z)ˆ
1, where ˆ
1 is the
identity matrix. By construction ˆΓ and ˆB are block-diagonal, their ﬁrst block
is one-dimensional: ˆΓ 11 = z and ˆB11 = β. We write this as ˆΓ = z⊕ ˆΓ c(z)
and similarly, ˆB = β⊕ ˆBc, where ˆΓ c and ˆBc are ( n− 1)× (n− 1) matrices.
ˆΓ c(z) and ˆΓ −1
c (z) are analytic in Dǫ.
Lemma 20 The function Y0 given in Proposition 6 can be written in the
form
Y0(p) = (1− p)β−1a1(p) + a2(p) ( β⁄= 1)
Y0(p) = ln(1 − p)a1(p) + a2(p) ( β = 1) (2.30)
for p in the region (Dǫ + 1)∩D (Dǫ + 1 := {1 + z : z∈ Dǫ}) where a1, a2
are analytic functions in Dǫ + 1 and (a1)j = 0 for j > 1.
Proof.
Let Q(z) :=
∫ z
ǫ h(s)ds. By Proposition 6, Q is analytic in Dǫ∩ (1−D ).
From (2.27) we obtain
(z⊕ ˆΓ c(z))Q′(z)− (β⊕ ˆBc)Q(z) = F(z)−
n∑
j=1
∫ z
ǫ
Dj(s− z)Q′
j(s)ds (2.31)
or, after integration by parts in the r.h.s. of (2.31), ( Dj(0) = 0, cf. (2.29)),
(z⊕ ˆΓ c(z))Q′(z)− (β⊕ ˆBc)Q(z) = F(z) +
n∑
j=1
∫ z
ǫ
D′
j(s− z)Qj(s)ds (2.32)
With the notation ( Q1, Q⊥) := ( Q1, Q2, .., Qn) we write the system in the
form
21
(z−βQ1(z))′ = z−β−1
(
F1(z) +
n∑
j=1
∫ z
ǫ
D′
1j(s− z)Qj(s)ds
)
(e
ˆC(z)Q⊥)′ = e
ˆC(z) ˆΓ c(z)−1
(
F⊥ +
n∑
j=1
∫ z
ǫ
D′
⊥(s− z)Qj(s)ds
)
ˆC(z) :=−
∫ z
0
ˆΓ c(s)−1 ˆBc(s)ds
Q(ǫ) = 0 (2.33)
After integration we get:
Q1(z) = R1(z) + J1(Q)
Q⊥(z) = R⊥(z) + J⊥(Q) (2.34)
with
J1(Q) = zβ
∫ z
ǫ
t−β−1
n∑
j=1
∫ t
ǫ
Qj(s)D′
1j(t− s)dsdt
J⊥(Q)(z) := e− ˆC(z)
∫ z
ǫ
e
ˆC(t) ˆΓ c(t)−1
( n∑
j=1
∫ z
ǫ
D′
⊥(s− z)Qj(s)ds
)
dt
R⊥(z) := e− ˆC(z)
∫ z
ǫ
e
ˆC(t) ˆΓ c(t)−1F⊥(t)dt
R1(z) = zβ
∫ z
ǫ
t−β−1F1(t)dt (β⁄= 1)
R1(z) = F1(0) + F ′
1(0)z ln z + z
∫ z
ǫ
F1(s)− F1(0)− sF ′
1(0)
s ds (β = 1)
(2.35)
Consider the following space of functions:
Tβ =
{
Q analytic in Dǫ∩ (D− 1) : Q = zβA(z) + B(z)
}
for β⁄= 1 and
T1 =
{
Q analytic in Dǫ∩ (D− 1) : Q = z ln zA(z) + B(z)
}
(2.36)
where A, B are analytic in Dǫ. (The decomposition of Q in (2.36) is unam-
biguous since zβ and z ln z are not meromorphic in Dǫ.)
22
The norm
‖Q‖ = sup{|A(z)|∧,|B(z)|∧ : z∈ Dǫ} (2.37)
makesTβ a Banach space.
For A(z) analytic in Dǫ the following elementary identities are useful in what
follows:
∫ z
ǫ
A(s)srds = Const + zr+1
∫ 1
0
A(zt)trdt = Const + zr+1Analytic(z)
∫ z
0
sr ln s A(s)ds = zr+1 ln z
∫ 1
0
A(zt)trdt + zr+1
∫ 1
0
A(zt)tr ln tdt
(2.38)
where the second equality is obtained by diﬀerentiating with respect to r the
ﬁrst equality.
Using (2.38) it is straightforward to check that the r.h.s. of (2.34) e xtends
to a linear inhomogeneous operator on Tβ with image inTβ and that the norm
of J is O(ǫ) for small ǫ. For instance, one of the terms in J for β = 1,
z
∫ z
0
t−2
∫ t
0
s ln s A(s)D′(t− s)ds =
z2 ln z
∫ 1
0
∫ 1
0
σA(zτ σ)D′(zτ− zτ σ)dσdτ +
z2
∫ 1
0
dτ
∫ 1
0
dσσ(ln τ + ln σ)A(zτ σ)D′(zτ− zτ σ)
(2.39)
manifestly in Tβ if A is analytic in Dǫ. Comparing with (2.36), the extra
power of z accounts for a norm O(ǫ) for this term.
Therefore, in (2.33) (1−J) is invertible and the solution Q∈T β⊂L (D).
In view of the the uniqueness of Y0 (cf. Proposition 6), the rest of the proof
of Lemma 20 is immediate.
2.4 The solutions of (1.25) on [0, 1 + ǫ]
Let Y0 be the solution given by Proposition 6, take ǫ small enough and
denote byOǫ a neighborhood in C of width ǫ of the interval [0 , 1 + ǫ].
23
Remark 21 . Y0∈ L1(Oǫ). As φ→± 0, Y0(peiφ)→ Y±
0 (p) in the sense
of L1([0, 1 + ǫ]) and also in the sense of pointwise convergence for p⁄= 1 ,
where
Y±
0 :=
{
Y0(p) p < 1
(1− p± 0i)β−1a1(p) + a2(p) p > 1 (β⁄= 1)
Y±
0 :=
{
Y0(p) p < 1
ln(1− p± 0i)a1(p) + a2(p) p > 1 (β = 1) (2.40)
Moreover, Y±
0 are L1
loc solutions of the convolution equation (1.25) on the
interval [0, 1 + ǫ].
The proof is immediate from Lemma 20 and Proposition 13.
Proposition 22 For any λ∈ C the combination Yλ = λY+
0 + (1− λ)Y−
0
is a solution of (1.25) on [0, 1 + ǫ].
Proof. For p∈ [0, 1)∪ (1, 1 + ǫ] let yλ(p) := Yλ− H(p). Since y∗2
λ = 0
the equation (1.25) is actually linear in yλ (compare with (2.27)).
*
Note: We consider the application Y := y0↦→Yλ and require that it is
compatible with complex conjugation of functions Y(y0∗) = (Y(y0))∗ where
F ∗(z) := F (z). We get ℜ λ = 1 /2. It is natural to choose λ = 1 /2 to make
the linear combination a true average. This choice corresponds, on [0, 1 + ǫ],
to the balanced averaging (1.16).
*
Remark 23 For any δ > 0 there is a constant C(δ) such that for large b
‖(Yba
0 )∗l‖u < C (δ)δ|l| ∀ l with|l| > 1 (2.41)
(‖‖u is taken on the interval [0, 1 + ǫ]).
Without loss of generality, assume that l1 > 1. Using the notation (2.29),
‖
‖
‖
‖
∫ p
0
(Y0)ba
1 (s)(Yba
0 )∗¯l1
(p− s)ds
‖
‖
‖
‖
u
≤
24
‖
‖
‖
‖
‖
∫ p
2
0
(Yba
0 )1(s)(Yba
0 )∗¯l1
(p− s)ds
‖
‖
‖
‖
‖
u2
+
‖
‖
‖
‖
‖
∫ p
2
0
(Y0)1(p− s)(Yba
0 )∗¯l1
(s)ds
‖
‖
‖
‖
‖
u2
(2.42)
(‖‖u2 refers to the interval p∈ [0, 1/2 + ǫ/2].) The ﬁrst u2 norm can be
estimated directly using Corollary 11 whereas we majorize the secon d one by
‖(Yba
0 )1‖b‖(Yba
0 )∗¯l1
(x)‖u2
and apply Corollary 11 to it for |l| > 2 (if|l| = 2 simply observe that ( Yba
0 )∗l
is analytic on [0 , 1/2 + ǫ/2]).
Lemma 24 The set of all solutions of (1.25) in L1
loc([0, 1 + ǫ]) is parameter-
ized by a complex constant C and is given by
Y0(p) =
{
Yba
0 (p) for p∈ [0, 1)
Yba
0 (p) + C(p− 1)β−1A(p) for p∈ (1, 1 + ǫ] (2.43)
for β⁄= 1 or, for β = 1,
Y0(p) =
{ Yba
0 (p) for p∈ [0, 1)
Yba
0 (p) + C(p− 1)A(p) for p∈ (1, 1 + ǫ] (2.43)′
where A extend analytically in a neighborhood of p = 1.
Diﬀerent values of C correspond to diﬀerent solutions.
This result remains true if Yba
0 is replaced by any other combination Yλ :=
λY+
0 + (1− λ)Y−
0 , λ∈ C.
Proof.
We look for solutions of (1.25) in the form
Yba(p) + h(p− 1) (2.44)
By Lemma 20 , h(p− 1) = 0 for p < 1. Note that
N (Yba
0 ◦ τ−1 + h)(z) =N (Yba
0 )(1 + z) +
n∑
j=1
∫ z
0
hj(s)Dj(z− s)ds (2.45)
25
where the Dj are given in (2.29), and by Remark 2.41 all the inﬁnite sums
involved are uniformly convergent. For z < ǫ (1.25) translates to (compare
with (2.27)):
− (1 + z)h(z) =−ˆΛ h(z)− ˆB
∫ z
0
h(s)ds +
n∑
j=1
∫ z
0
hj(s)Dj(z− s)ds (2.46)
Let
Q(z) :=
∫ z
0
h(s)ds (2.47)
As we are looking for solutions h∈ L1, we have Q∈ AC[0, ǫ] and Q(0) = 0.
Following the same steps as in the proof of Lemma 20 we get the syste m of
equations:
(z−βQ1(z))′ = z−β−1
n∑
j=1
∫ z
0
D′
1j(z− s)Qj(s)ds
(e
ˆC(z)Q⊥)′ = e
ˆC(z) ˆΓ c(z)−1
n∑
j=1
∫ z
0
D′
⊥(z− s)Qj(s)ds
ˆC(z) :=−
∫ z
0
ˆΓ c(s)−1 ˆBc(s)ds
Q(0) = 0 (2.48)
which by integration gives
(ˆ
1 + J)Q(z) = CR(z) (2.49)
where C∈ C and
(J(Q))1(z) = zβ
∫ z
0
t−β−1
n∑
j=1
∫ t
0
Qj(s)D′
1j(t− s)dsdt
J(Q)⊥(z) := e− ˆC(z)
∫ z
0
e
ˆC(t) ˆΓ c(t)−1
( n∑
j=1
∫ z
0
D′
⊥(z− s)Qj(s)ds
)
dt
R⊥ = 0
26
R1(z) = zβ
(2.50)
First we note the presence of an arbitrary constant C in (2.49) (Unlike
in Lemma 20 when the initial condition, given at z = ǫ was determining the
integration constant, now the initial condition Q(0) = 0 is satisﬁed for all
C).
For small ǫ the norm of the operator J deﬁned on AC[0, ǫ] is O(ǫ), as in
the proof of Lemma 20. Given C the solution of the system (2.48) is unique
and can be written as
Q = CQ0; Q0 := (ˆ
1 + J)−1R⁄= 0 (2.51)
It remains to ﬁnd the analytic structure of Q0. We now introduce the
space
T =
{
Q : [0, ǫ)↦→Cn : Q = zβA(z)
}
(2.52)
where A(z) extends to an analytic function in Dǫ. With the norm (2.37) (with
B≡ 0),T is a Banach space. As in the proof of Lemma 20 the operator J
extends naturally to T where it has a norm O(ǫ) for small ǫ. It follows
immediately that
Q0∈T (2.53)
The formulas (2.43), (2.43’) follow from (2.44) and (2.47).
Remark 25 If Sβ⁄= 0 (cf. Lemma 20) then the general solution of (1.25)
is given by
Y0(p) = (1− λ)Y+
0 (p) + λY−
0 (p) (2.54)
with λ∈ C.
Indeed, if a1⁄≡0 (cf. Lemma 20) we get at least two distinct solutions of
(2.49) (i.e., two distinct values of C) by taking diﬀerent values of λ in (2.54).
The remark follows from (2.53) (2.52) and Lemma 24..
27
2.5 The solutions of (1.25) on [0,∞)
In this section we show that the leading asymptotic behavior of Yp as p→
1+ determines a unique solution of (1.25) in L1
loc(R+). Furthermore, any
L1
loc solution of (1.25) is exponentially bounded at inﬁnity and thus Laplace
transformable. We also study some properties of these solutions a nd of their
Laplace transforms.
Let H be a solution of (1.25) on an interval [0 , 1 + ǫ], which we extend to
R+ letting H(p) = 0 for p > 1 + ǫ. For a large enough b, deﬁne
SH :={f∈ L1
loc([0,∞)) : f (p) = H(p) on [0 , 1 + ǫ]} (2.55)
and
S0 :={f∈ L1
loc([0,∞)) : f (p) = 0 on [0 , 1 + ǫ]} (2.56)
We extend H to R+ by putting H(p) = 0 for p > 1 + ǫ; for p≥ 1 + ǫ (1.25)
reads:
− p(H + h) = F0− ˆΛ( H + h)− ˆB
∫ p
0
(H + h)(s)ds +N (H + h) (2.57)
with h∈S 0, or
h =−H + ( ˆΛ− p)−1
(
F0− ˆB
∫ p
0
(H + h)(s)ds +N (H + h)
)
:=M(h)
(2.58)
For small φ0 > 0 and 0 ≤ ρ1 < ρ 2≤∞ , consider the truncated sectors
S±
(ρ1,ρ2) :={z : z = ρe±iφ, ρ1 < ρ < ρ 2; 0 ≤ φ < φ 0} (2.59)
and the spaces of functions analytic in S±
(ρ1,ρ2) and continuous in its closure:
T ±
ρ1,ρ2 =
{
f : f∈ C(
S(ρ1,ρ2)); f analytic in S±
(ρ1,ρ2)
}
(2.60)
which are Banach spaces with respect to ‖‖u on compact subsets of S(ρ1,ρ2).
28
Proposition 26 i) Given H, the equation (2.58) has a unique solution in
L1
loc[1 + ǫ,∞). For large b, this solution is in L1
b([1 + ǫ,∞)) and thus Laplace
transformable.
ii) Let Y0 be the solution deﬁned in Proposition 6. Then
Y±
0 (p) := lim
φ→±0
Y0(peiφ)∈ C(R+\{1})∩ L1
loc(R+) (2.61)
(and the limit exists pointwise on R+\{1} and in L1
loc(R+).)
Furthermore, Y±
0 are particular solutions of (1.25) and
Y±
0 (p) = (1 − p)β−1a±(p) + a±
1 (p) ( β⁄= 1)
Y±
0 (p) = ln(1 − p) a±(p) + a±
1 (p) ( β = 1) (2.62)
where a± and a±
1 are inT ±
0,∞.
Proof
Note ﬁrst that by Proposition 13, M (eq. (2.58)) is well deﬁned on S0,
(eq.(2.56)). Moreover, since H is a solution of (1.25) on [0 , 1 + ǫ), we have,
for h0∈S 0,M(h) = 0 a.e. on [0 , 1 + ǫ), i.e.,
M(S0)⊂S 0
Remark 27 For large b,M is a contraction in a small neighborhood of the
origin in ‖‖u,b.
Indeed, sup{‖(ˆΛ− p)−1‖Cn↦→Cn : p≥ 1 + ǫ} = O(ǫ−1) so that
‖M(h1)−M (h2)‖u,b≤ Const
ǫ ‖N (f + h)−N (f)‖u,b (2.63)
The rest follows from (2.18) —Proposition 13 and Remark 10 applied to H.
The existence of a solution of (2.58) in S0∩ L1
b([0,∞)) for large enough b
is now immediate.
Uniqueness in L1
loc is tantamount to uniqueness in L1([1+ ǫ, K]) = L1
b([1+
ǫ, K], for all K− 1− ǫ∈ R+. Now, assuming M had two ﬁxed points in
L1
b([1 + ǫ, K]), by Remark 10, we can choose b large enough so that these
solutions have arbitrarily small norm, in contradiction with Remark 27 .
29
ii). For p < 1, Y±
0 (p) = Y0(p). For p∈ (1, 1 + ǫ) the result follows from
Lemma 20. Noting that (in view of the estimate (2.15)) M(T ±1+ǫ,∞)⊂
T ±1+ǫ,∞, the rest of the proof follows from the Remark 27 and Lemma 20.
Proposition 28 There is a one parameter family of solutions of equation
(1.25) in L1
loc[0,∞), branching oﬀ at p = 1 and in a neighborhood of p = 1
all solutions are of the form (2.43), (2.43’). The general so lution of (1.25)
is Laplace transformable for large b and the Laplace transform is a solution
of the original diﬀerential equation in the half-space ℜ(x) > b.
Note: As of now, the correspondence (2.43), (2.43’) with the balan ced
average (1.16) is proven only near p = 1; the complete correspondence is
established in Section 2.7.
Proof.
Let Y be any solution of (1.25). By Lemma 24 and Proposition 26, b
large implies that Y∈ L1
b([0,∞)) (thusLY exists), that‖Y‖b is small and,
in particular, that the sum deﬁning N in (1.22) is convergent in L1
b(R+).
By Remark 8,
L

∑
|l|≥1
Gl∗ Y∗l +
∑
|l|≥2
g0,lY∗l

 (x) =
∑
|l|≥1
(LGl)(LY)l(x) +
∑
|l|≥2
g0,l (LY)l =
∑
|l|≥1
gl(x)yl(x) = g(x, y(x))
(2.64)
(and g(x, y(x)) is analytic for ℜ(x) > b). The rest is straightforward.
