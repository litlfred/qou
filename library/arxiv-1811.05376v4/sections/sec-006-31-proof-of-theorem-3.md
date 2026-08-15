---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-006-31-proof-of-theorem-3
section_title: "Proof of Theorem 3"
section_number: 3.1
pages: 20-26
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
We now consider X = Σ(p1,...,p n) in more detail. Choose q1,...,q n ∈ N such that for each
j = 1,...,n we have(pj,qj) = 1, pj≤qj and
p0 :=−1
P −
∑
j=1
qj
pj
∈ Z<0.
Then e =−1/P <0 is the Seifert Euler number. Choose a continued fraction expansion ofqj/pj
for eachj = 1,...,n
qj
pj
=kj,1− 1
kj,2− 1
...−kj,sj
.
Resurgence Analysis of Quantum Invariants 21
p0 −k2,1 −k2,s2−k2,2
−k1,1 −k1,2 −k1,s1
−k3,1 −k3,2 −k3,s3
Figure 3: Plumbing graph forX in the casen = 3.
As explained in [28],X has a negative deﬁnite plumbing graphΓ deﬁned as follows. The graphΓ
is star-shaped withn arms and central vertexv0 with weightp0. For eachj = 1,...,n thej′th arm
has sj vertices. If these are ordered(vj,1,...,v j,sj) with vj,1 being closest to the central vertexv0,
then vi,j have weight−kj,i. This graph is illustrated forn = 3 in Figure 3
Before proving Theorem 3, we ﬁrst give a formula for the rational exponent∆∈ Q. For each
j = 1,...,n let Xj be the plumbed manifold whose graphΓj is identical toΓ except that on the
j′th arm, we delete the terminal vertexvj,sj. Deﬁnehj∈ N as
hj =|H1(Xj, Z)|.
Observe that the total number of vertices ofΓ is given bys = 1 +∑n
j=1sj. Deﬁne∆∈ Q by
∆ =−1
4


n∑
j=1
hj− 3s−p0 +
n∑
j=1
(
− P
pj2 +
sj∑
i=1
kj,i
)
 (50)
We now prove Theorem 3.
Proof. Recall that q = exp(2πiτ ) where τ ∈ h. For the sake of notational simplicity, we also
introduce the paramterh = 2πiτ so thatq = exp(h). We start by proving that
I(h) = Ψ(q), (51)
where Ψ(q) is the series introduced in (10) andI(h) is the contour integral introduced in (11) (with
h = 2πiτ ). Observe that for the purpose of proving (51) we can and will assume that
τ∈iR>0,
because if the identity (51) holds true on this half-line, it has to hold on the entire upper half-plane
h, since both functions are holomorphic inh.
Set
B(ζ) = 1
2
√
P
B(Z0)
( ζ
2πi
)
. (52)
For allt∈ C with
√
t∈{z∈ C| Re(z)< 0} the normalized Borel transformB satisﬁes by Theorem
2
B(t) = 1√
t
∞∑
m=m0
cm exp
(
m
√
t
P
)
= 1√
tG
(
exp
(√
t
P
))
(53)
where for allm∈ N we have that
cm = (−1)nχm.
For eachm∈ Z≥m0 introduce the polynomial
pm(w) =−w2
h + m√
P
w.
Resurgence Analysis of Quantum Invariants 22
This is a Morse function with a unique saddle point atwm = hm
2
√
P and we have that
pm(wm) =hm2
4P.
Let D(R) be the closed ball centered at the origin with radiusR> |m0|. We can deformiR slightly
to a contour∆m⊂{ z∈ C : Re(z) < 0}∪ D(R), which passes through the saddle pointwm and
such that the function given by
w↦→ exp(pm(w)),
have exponential decay along∆m. The orientation of∆m is as depicted in Figure 4. We remark
that Figure 4 depicts the situation wherem0≥ 0. Recall that if Γ is a steepest descent contour
R
i R
∆ m
•
w m
Figure 4: The contour∆m.
through the unique saddle point of a degree two polynomialp(z) =−αz2 +βz, then we have the
following exact formula known as Gaussian integration
∫
Γ
exp(p(z)) dz =
√π
α exp
(β2
4α
)
.
Applying Gaussian integration to the polymonialspm gives us the following identity
(−1)nΨ(q) =
∞∑
m=m0
cmq
m2
4P =
∞∑
m=m0
cm
1√
πh
∫
iR
exp (pm(w)) dw. (54)
Choose a small postive parameterδ >0 and introduce the contour
∆0 =eiδiR+∪e−iδiR−⊂{z∈ C : Re(z)< 0}.
Let Υ⊂{z∈ C :ℜ(z)< 0} be the Hankel contour which enclosesR− and satisﬁes
√
Υ = ∆0. The
orientation of these contours are given as in Figure 5. We let
Υ± = Υ∩{z∈ C : Im(z)∈ R∓},
so that
√
Υ+ =eiδiR+ and−
√
Υ− =e−iδiR− where√· denotes the principal branch of the square
root. Introduce the variable
w2 =v.
Resurgence Analysis of Quantum Invariants 23
R
i R
Υ
∆ 0
Figure 5: The contoursΥ and ∆0.
As ∆0 is a small deformation of∆m for eachm∈ Z≥m0, we obtain
∞∑
m=m0
cm√
πh
∫
iR
exp(pm(w)) dw =
∞∑
m=m0
∑
ϵ=±1
cm√
πh
∫
Υ(ϵ)
exp
(
−v
h +ϵ m√
P
√v
)
ϵ2√v dv
=
∑
ϵ=±1
1
2
√
πh
∫
ϵΥ(ϵ)
exp(−v
h)√v
∞∑
m=m0
cmeϵm√v√
P dv
=
∑
ϵ=±1
1
2
√
πh
∫
ϵΥ(ϵ)
exp
(
−v
h
)
B(v) dv
(55)
In the second equality of (55) we used thatϵ√v∈{ z∈ C : Rez <0} for allv∈ Υ(ϵ), and the
contour−Υ(−1) denotes Υ(−1) but oriented in the direction from the origin and towards inﬁnity.
In the third equality of (55) we used equation (53) and the identity
G(z) =G
(1
z
)
,
which follows directly from the deﬁnition ofG. Now introduce the variable
ξ = v
2πi.
This identiﬁes (up to a small deformation) thev contour Υ+−Υ− with theξ contourΓ introduced
in Figure 1.
We have
∑
ϵ=±1
1
2
√
πh
∫
ϵΥ(ϵ)
exp
(
−v
h
)
B(v) dv
=
∑
ϵ=±1
2πi
2
√
πh
∫
exp(ϵπi
4 )iR+
exp
(
−2πiξ
h
)
B(2πiξ) dξ
=
∑
ϵ=±1
2πi
2
√
πh
√
2πi
8κ
∫
exp(ϵπi
4 )iR+
exp
(
−2πiξ
h
)
B(Z0)(ξ) dξ. (56)
In the last equality of (56) we used Equation (52), which relatesB andB(Z0). Now recall that
κ =
√
2πiP, sinceH = 1 and recognize the pre-factor in the last line of (56) as
2πi
2
√
πh
1√
P 2
= (−1)n λ√τ,
Resurgence Analysis of Quantum Invariants 24
where λ is the scalar introduced in the statement of Theorem 3. By combining Equations (54),
(55) and (56), we see that Equation (51) holds.
Write ˆZ0(X;q) = ˆZ0(q). We now show that
Ψ(q) =q∆ˆZ0(q), (57)
where ∆∈ Q is the scalar introduced in (50). This will establish (6) and thereby ﬁnish the proof.
We start withˆZ0(q). By Deﬁnition 1 and since in this caseφ = 0, we have that
ˆZ0(q) =q
3σ−∑
vmv
4
∑
⃗l∈2M Zs
q− (⃗l,M−1⃗(l))
4
∮
|zv|=1
∏
v∈V
dzv
2πizv
(
zv− 1
zv
)2−deg(v)
zlv
v . (58)
Here it is understood that we have taken the principal value of the integral as explained above.
Recall that for a Laurent seriesa(z) =∑
j∈Zajzj we have that
v.p.
∮
|z|=1
dz
2πiza(z) =a0.
For our star-shaped plumbing graphΓ, the non-zero contributions to (58) comes from⃗l∈ 2M Zs
with lw = 0 for all of the entries corresponding to an internal vertexw of an arm, andlv =±1 if
v is a terminal vertex of an arm and then from the central vertexv0, which we will now consider.
In comparing ˆZ0(q) with Ψ(q) it is useful to introduce the integer sequence{aj}∞
j=0 determined
by
(
t−t−1)2−n
=



∑∞
j=0ajt2j+n−2, if|t|< 1
∑∞
j=0(−1)najt−2j−n+2, if|t|> 1.
(59)
The aj’s can be explicitly evaulated: By the formula for the geometric series(1−t)−1 =∑∞
j=0tj
and Cauchy multiplication of power series, we see that
1
(1−t)m =
∞∑
j=0

 ∑
j1+···+jm=j
1

tj =
∞∑
j=0
(j +m− 1
j
)
tj,
and therefore one sees that
aj = (−1)n
(j +n− 3
j
)
.
However for the comparison ofˆZ0(q) and Ψ(q) given below, we don’t need the closed form foraj,
but rather the equation (59).
Writezv0 =z and l =lv0. We obtain
v.p.
∮
|z|=1
dz
2πiz
(
z−z−1)2−n
zl =



1
2al−n+2
2
if 2−n−l∈ 2Z+,
1
2(−1)na 2−n−l
2
if l−n + 2∈ 2Z+,
a0 if l = 0,n = 2.
We know that the adjacency matrix M is unimodular, and so M Zs = Zs. Deﬁne a map
⃗l :{±1}× N×{± 1}n→ Zs as follows: For the central vertexv0 we have
⃗l(ε,j,ϵ )v0 =ε(−2j + 2−n).
Form = 1,...,n and the terminal vertexv of them′th arm, we have
⃗l(ε,j,ϵ )v =ϵm,
Resurgence Analysis of Quantum Invariants 25
and for every internal vertexw of the arms, we have
⃗l(ε,j,ϵ )w = 0.
With this notation, the above considerations show that
ˆZ0(q) =q−
3s+∑
vmv
4
∑
ε=±1
∞∑
r=0
∑
ϵ∈{±1}n
(−1)
(1−ε)(n−2)
2
ar
2


n∏
j=1
ϵj

q−⟨⃗l(ε,r,ϵ),M−1⃗l(ε,r,ϵ),⟩
4 .
If we apply the symmetry that simultaneously changes the sign of allϵj and ε, then we we obtain
ˆZ0(q) = (−1)nq−
3s+∑
vmv
4
∞∑
r=0
∑
ϵ∈{±1}n
ar


n∏
j=1
ϵj

q−⟨⃗l(−1,r,ϵ),M−1⃗l(−1,r,ϵ),⟩
4 .
The quadratic form
⃗l↦→⟨⃗l,M−1⃗l⟩/4
was computed forn = 3 in [28] in their proof of Proposition4.8. The size of the matrixM−1
is irrevelant to their computation, and their formula can be generalized to our case to give the
formula
ˆZ0(q) = (−1)nq−∆
∞∑
r=0
∑
ϵ∈{±1}n
ar


n∏
j=1
ϵj

q
P
4
(
2r+(n−2)+∑n
j=1ϵj 1
pj
)2
.
We now computeΨ(q). For|z|< 1 we have
G(z) =
n−2∏
j=1
(
z
P
pj−z
−P
pj
)(
zP−z−P)2−n
=
∞∑
r=0
∑
ϵ∈{±1}n
ar


n∏
j=1
ϵj

z
2Pr +P(n−2)+∑n
j=1ϵj P
pj.
It follows that
Ψ(q) = (−1)n
∞∑
r=0
∑
ϵ∈{±1}n
ar


n∏
j=1
ϵj

q
(
2Pr +P (n−2)+∑n
j=1ϵj P
pj
)2
4P .
This shows (57).
We obtain the following corollary.
Corollary 12. Let Z0∈ x−1/2C[[x−1]] be the normalization of the Ohtsuki series from Theorem
2. We have an asymptotic expansion
q∆ˆZ0(X;q)∼q→1
2λ√τ Z0(1/τ).
Proof. This is a consequence of the integral formula (6) from Theorem 3
q∆ˆZ0(X;q) = λ√τ
∫
Γ
exp(−ζ/τ )B(Z0)(ζ) dζ
= λ√τ
∑
ϵ∈{±1}
LΓϵ(B(Z0))(1/τ)
and Borel-Laplace resummation, which is stated as Theorem 15 below.
Resurgence Analysis of Quantum Invariants 26
Let us now recall previous work on theq-series Ψ. We start with the casen = 3, for which more
is known. As already mentioned in the introduction, Lawrence and Zagier have shown in [40] that
the quantum invariantτk(X) can be recovered as the radial limit ofΨ(q), asq tends toexp(2πi/k).
This was generalized ton = 4 by Hikami in [34] but with corrections terms appearing. The series
Ψ have interesting arithmetic properties; the coeﬃcientsχ(m) are periodic functions of period2P
and Ψ is the so-called Eichler integral of a mock modular form with weight3/2. As mentioned
in the introduction the connection between quantum invariants and number theory was further
pursued by Hikami in a number of articles [30, 32, 34, 35, 36]. For generaln≥ 3 we mention again
the work [25] of Fuji, Iwaki, Murakami and Terashima which was discussed in the introduction.
Let us now discuss what was previosly known about theq-series invariant ˆZ0(X). In [28] it
was shown that whenX is a Briskekorn sphereΣ(p1,p 2,p 3), (i.e. n = 3) then ˆZ0(X) is a linear
combination of so-called false theta functions. Theq-series invariant ˆZ0 was also considered for
certain Seifert ﬁbered manifolds (with up ton = 4 singular ﬁbers) in the work [14], as well as a
proposed analog ofˆZ0 for higher rank gauge group - see also [47] for further developments in this
direction. In this paper we work exclusively withG = SU(2)).
In connection with the work [40], Zagier invented the notion of a quantum modular form. This
notion was generalized by Bringmann et al. in [8], where they introduce the notion of a higher
depth quantum modular form. For any n≥ 3, it is known, that Ψ is a linear combination of
derivatives of quantum modular forms [9, 10]. It is interesting to observe thatΨ is obtained from
the Borel transform through a resummation process reminiscent of the median resummation of [15].
Moreover as explained in [12] it is expected that for a general3-manifold M, Mock/false modular
form duality is related toˆZa(M;q), i.e. there exists an associated pair of a so-called Mock modular
form and a so-called false modular form, and these are related by aq↦→q−1 transformation and
havethesametransseriesexpressionnear q→ 1.Thisisquitepossiblyconnectedtotheconjecture 2
in [26] (called the symmetry conjecture). Let us also mention the work [18] by Dimofte-Garoufalidis
which connects modularity in quantum topology with complex Chern-Simons theory.
