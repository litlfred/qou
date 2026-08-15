---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-000-1-complex-chern-simons-theory-on-x
section_title: "Complex Chern-Simons theory on X"
section_number: 1
pages: 5-6
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
LetX be the oriented Seifert ﬁbered homology3-sphere from the introduction. Chooseq1,...,q n∈
Z such that (pj,qj) = 1 and
n∑
j=1
qj
pj
= 1
P.
Then X has a surgery diagram as depicted in Figure 2 below. Without loss of generality we can
p1/q1
p2/q2 p3/q3 pn/qn
Figure 2: Surgery link forX.
assume thatp2,...,p n are odd. The homeomorphism type ofX is unaltered under a transformation
qj↦→qj +yj for any choice of integersy1,...,y n such that (pj,qj +yj) = 1 and
n∑
j=1
qj
pj
=
∑
j=1
qj +yj
pj
. (13)
If qj is odd forj >1, we perform the transformationqj↦→qj +pj and q1↦→q1− (n− 1)p1 which
does not change the sum (13). Hence we can assume without loss of generality thatq2,...,q n are
all even. Recall that under our assumptions1 =P∑
j=1
qj
pj. Note that this implies thatq1 is odd.
We recall the computation ofτk(X) from [39]. LetS(·,· ) be the Dedekind sum. Introduce
the constants
ς =−
√
P
4 exp
(
−πi3
4
)
, φ = 3− 1
P + 12
n∑
j=1
S
(P
pj
,pj
)
. (14)
The quantityφ is related to the Casson-Walker invariantλ(X) [51] (in Casson’s normalization) as
follows
−24λ(X) =φ +P

n− 2−
n∑
j=1
p−2
j

.
Deﬁne the meromorphic functionF∈M (C) and g∈ C[y] explicitly as follows
F (y) = 1
4
(
sinh
(y
2
))2−n n∏
j=1
sinh
( y
2pj
)
,
g(y) = iy2
8πP.
(15)
Lawrence and Rozansky shows in [39] the following results. There exists a ﬁnite subsetR∗(X)⊂
Q∗/Z and non-vanishing polynomialsZθ(z)∈ C[z], θ∈R∗(X) of degree at mostn− 3 such that
∑
θ∈R∗(X)
e2πikθ Zθ(k) =−
2P−1∑
m=1
Res
(F (y)ekg(y)
1−e−ky ,y = 2πim
)
Resurgence Analysis of Quantum Invariants 6
for all non-negative integersk. Letγ to be the contour from(−1−i)∞ to (1 +i)∞. Observe that
γ(H) is a steepest descent path forg. Introduce the following notation
ZR(k) =
∑
θ∈R∗(X)
e2πikθ Zθ(k)
ZI(k) = 1
2πi
∫
γ
F (y)ekg(y) dy.
Recalling the deﬁnition of the normalized quantum invariant~Zk given in (1), Lawrence and Rozan-
sky proved that it can be decomposed into a sum of an integral partZI and a residue partZR
~Zk(X) = ZI(k) + ZR(k). (16)
This is Equation 4.8 on in Section 4.5 in [39]. We have used the same notation forF,g and φ
whereas the constantB in their notation is equal toς−1. Thus, if we deﬁne
Z0(x) = 1
2πi
√
Pπi 8
∞∑
n=0
F (2n)(0) (i8Pπ )n
(2n)!
Γ
(
n + 1
2
)
xn+ 1
2
∈ x−1/2C[[x−1]]
and setR(X) =R∗(X)⊔{ 0} then we have an asymptotic expansion
~Zk(X)∼k→∞
∑
θ∈R(X)
e2πikθ Zθ(k). (17)
In the work [39] it was observed thatZ0 is in fact a normalization of the Ohtsuki-series [44, 45, 46].
Let Z∞ denote the Ohtsuki series (with the normalization used in [39]). Introduce the variable
h =qk− 1, where as aboveqk = exp(2πi/k). In section4.6 of [40] they show the following identity
Z0(k) = Z∞(h). (18)
