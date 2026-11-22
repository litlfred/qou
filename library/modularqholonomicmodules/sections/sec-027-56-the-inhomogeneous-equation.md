---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-027-56-the-inhomogeneous-equation
section_title: "The inhomogeneous equation"
section_number: 5.6
pages: 47-52
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
toc_source: outline
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
this into a homogeneous equation of one degree higher
tf(t; q) + (1 −3qt)f(qt; q) + (3tq2 −1)f(q2t; q) −tq3f(q3t; q) = 0
(253)
with Newton polygon shown in Figure 5.
g(0,0)
g(0,1)
g(0,2)
f (−1)
f (1)
f (0)
Figure 5. The Newton polygon of Equation (35).
Now from the general theory the solutions f (±1) and g(0,0) and g(0,1) are the same as the
solutions in Section 5.1. We do ﬁnd two additional solutions which are in fact solutions to
the inhomogeneous equation, namely
ˆf (0)(t, q) =
∞
X
k=0
(−1)kq−k(k+1)/2(q; q)2
ktk ,
(254)
a divergent formal power series solution at t = 0 and
g(0,2)(t; q) =
∞
X
k=0

1
2
 
1
2E1(q) −1
2 +
k
X
j=1
1 + qj
1 −qj


2
−

1
2E1(q) −1
2 +
k
X
j=1
1 + qj
1 −qj

θ′(t−1; q)
θ(t−1; q)
+ 1
2
θ′′(t−1; q)
θ(t−1; q) +
k
X
j=1
qj
(1 −qj)2 −1
24 −1
24E2(q)
!
(−1)k qk(k+1)/2
(q; q)2
k
t−1−k ,
(255)
48
STAVROS GAROUFALIDIS AND CAMPBELL WHEELER
where E2(q) = 1 −24 P∞
k=0 qk/(1 −qk)2, a convergent solution at t = ∞. So, we must resum
ˆf (0)(t, q). For |ξ| < 1, we have
B1 ˆf (0)(ξ, q) =
∞
X
k=0
(q; q)2
kξk
(256)
which can be analytically continued away from ξ ∈qZ≤0 using the relation
(1 −ξ)B1 ˆf (0)(ξ, q) + 2qξB1 ˆf (0)(qξ, q) −q2ξB1 ˆf (0)(q2ξ, q) = 1.
(257)
f(0)
B1
B1f(0)
Therefore, we deﬁne
f (0)(t, λ2, q) = (L1B1 ˆf (0))(t, λ2, q) =
1
θ(λ2; q)
X
k∈Z
(−1)kqk(k+1)λk
2B1 ˆf (0)(qkλ2t, q).
(258)
Now we consider the matrices
U(t, λ1, λ2, q) = W(f (1)(t, λ1, q), f (−1)(t, q), f (0)(t, λ2, q))
=


0
1
0
0
0
1
q−2t−1
−q−2
q−2t−1 −2q−1




0
0
1
f (1)(t, λ1, q)
f (−1)(t, q)
f (0)(t, λ2, q)
f (1)(qt, λ1, q)
f (−1)(qt, λ1, q)
f (0)(qt, λ2, q)


(259)
and
V (t, q) = W(g(0,0)(t, q), g(0,1)(t, q), g(0,2)(t, q))
=


0
1
0
0
0
1
q−2t−1
−q−2
q−2t−1 −2q−1




0
0
1
g(0,0)(t, q)
g(0,1)(t, q)
g(0,2)(t, q)
g(0,0)(qt, q)
g(0,1)(qt, q)
g(0,2)(qt, q)

.
(260)
With these formulae we will now go on to prove Theorem 1.8.
Proof of Theorem 1.8. The identiﬁcation of the ﬁrst two columns of
−→
M(t, λ1, λ2, q) with those
in Equation (37) follows from Theorem 1.7.
Equations (259) and (260), together with
Lemma 5.4 imply that
−det(U(t, λ1, λ2, q)) = det(V (t, q)) = q−3t−3 .
(261)
Hence, det(
−→
M(t, λ1, λ2, q)) = −1 which in turn implies that
−→
M3,3(t, λ2, q) = 1.
Now, Equation (37), written in the form U(t, λ1, λ2, q) = V (t, q)
−→
M(t, λ1, λ2, q), together
with Equations (259) and (260) and the fact that
−→
M3,3 = 1 imply that
f (0) =
−→
M1,3g(0,0) +
−→
M2,3g(0,1) + g(0,2) .
(262)
MODULAR q-HOLONOMIC MODULES
49
Thus, to determine the two remaining entries of the monodromy matrix, we need to show
that the function
E3 := f (0) −(m1,3g(0,0) + m2,3g(0,1) + g(0,2))
(263)
vanishes identically, where
m1,3(t, q) = ℘(t, q),
m2,3(t, λ2, q) = 1
2
℘′(t, q) −℘′(λ2, q)
℘(t, q) −℘(λ2, q)
(264)
denote the two entries of the matrix on the right hand-side of Equation (37). Note that
E3(t, λ2, q) is a meromorphic function of t with potential simple poles at λ−1
2 qZ (coming from
f (0) and m2,3) and potential double poles at qZ (coming from g(0,1), g(0,2), m1,3 and m2,3).
Since Rest=q−mλ−1
2 m2,3(t, λ2, q) dt
2πit = 1 , combined with equation (211) gives
Rest=q−mλ−1
2 m2,3(t, λ2, q)g(0,1)(t, q) dt
2πit = f (−1)(q−mλ−1
2 , q) ,
(265)
we see from Lemma 5.6 that E3 has no poles at λ−1
2 qZ. Now noting that
m2,3(t, λ2, q) = θ′(t−1; q)
θ′(t−1; q) + θ′(λ−1; q)
θ′(λ−1; q) −θ′(λ−1t−1; q)
θ′(λ−1t−1; q) + 1
2 ,
(266)
the only terms that contribute to the polar part of
g(0,2)(t, q) + m2,3(t, λ2, q)g(0,1)(t, q) + m1,3(t, q)g(0,0)(t, q)
(267)
at t = qmε for ε ∼1 are
∞
X
k=0

−

k −2E(k)
1 (q)
 θ′(ε−1; q)
θ(ε−1; q) + 1
2
θ′′(q−mε−1; q)
θ(q−mε−1; q)
+

k −m −θ′(ε−1; q)
θ(ε−1; q) −2E(k)
1 (q)
 θ′(ε−1; q)
θ(ε−1; q) −1
2
θ′(ε−1; q)
θ(ε−1; q)
+ θ′(ε−1; q)2
θ(ε−1; q)2 −θ′′(ε−1; q)
θ(ε−1; q)

(−1)k qk(k+1)/2−m−mk
(q; q)2
k
ε−1−k
=
∞
X
k=0
1
2
θ′′(q−mε−1; q)
θ(q−mε−1; q) −

m + 1
2
 θ′(ε−1; q)
θ(ε−1; q) −θ′′(ε−1; q)
θ(ε−1; q)

(−1)k qk(k+1)/2
(q; q)2
k
ε−1−k.
(268)
This has a potentially simple pole at ε = 1 however noting that
Resε=1
θ′′(q−mε−1; q)
θ(q−mε−1; q)
dε
2πiε = −2m + 1
Resε=1
θ′(ε−1; q)
θ(ε−1; q)
dε
2πiε = −1
(269)
we see that the residue vanishes and therefore (267) has a removable singularity at all points
t ∈qZ. Therefore, we see that E3 is a holomorphic (for t ∈C×) solution of Equation (28)
and therefore from Corollary 5.5 we see that E3(t, λ2, q) = C(q)g(0,0)(t, q). To ﬁnish the proof
50
STAVROS GAROUFALIDIS AND CAMPBELL WHEELER
we note that for t on some compact set where the functions are holomorphic, Lemma 5.1
and Lemma 5.7 implies that
−C(q)
(q; q)2
∞
= lim
r→∞
C(q)g(0,0)(tr, q)
θ(qrt; q)
= lim
r→∞
f (0)(t, λ2, q) −(g(0,2)(t, q) + m2,3(t, λ2, q)g(0,1)(t, q) + m1,3(t, q)g(0,0)(t, q))
θ(qrt; q)
=
1
(q; q)2
∞
(m1,3(t−1, q) −m1,3(t, q)) = 0 ,
where we note that m1,3(t, q) is the Weierstrass ℘-function plus a constant which is even in
z where t = e(z).
Our next task is to compute the residues of f (0).
Lemma 5.6. (a) The function B1 ˆf (0)(ξ, q) has simple poles at ξ ∈qZ with residue
R(m, q) := Resξ=q−mB1 ˆf (0)(ξ, q) dξ
2πiξ = −(q; q)2
∞
m
X
ℓ=0
qm
(q; q)ℓ(q; q)m−ℓ
.
(270)
(b) The function f (0)(t, q) has simple poles at t ∈λ−1
2 qZ with residue
Rest=q−mλ−1
2 f (0)(t, λ2, q) dt
2πit = f (−1)(q−mλ−1
2 , q) .
(271)
Proof. For part (a), notice that
B1 ˆf (0)(ξ, q) =
∞
X
k=0
(q; q)2
kξk = (q; q)2
∞
∞
X
k=0
1
(qk+1; q)∞
ξk
= (q; q)2
∞
∞
X
k,ℓ,n=0
qkn+kℓ+n+ℓ
(q; q)ℓ(q; q)n
ξk = (q; q)2
∞
∞
X
ℓ,n=0
qn+ℓ
(q; q)ℓ(q; q)n(1 −qn+ℓξ)
(272)
is the analytic continuation of B1 ˆf (0). From this, it clearly follows that the only poles are
simple, located at ξ = qZ. (Alternatively, one can also use the linear q-diﬀerence equation
satisﬁed by this function, though this is not needed here). We compute the residue as follows:
R(m, q) = Resξ=q−m(q; q)2
∞
∞
X
ℓ,n=0
qn+ℓ
(q; q)ℓ(q; q)n(1 −qn+ℓξ)
dξ
2πiξ
= −(q; q)2
∞
m
X
ℓ=0
qm
(q; q)ℓ(q; q)m−ℓ
.
(273)
For part (b), the pole structure is clear noting that Equation (258) is convergent if all the
terms are and that B1 ˆf (0)(qktλ2, q) has poles at t ∈λ−1
2 qZ≤−k. We compute the residues as
MODULAR q-HOLONOMIC MODULES
51
follows:
Rest=q−mλ−1
2 f (0)(t, λ2, q) dt
2πit = Rest=q−mλ−1
2 (L1B1 ˆf (0))(t, λ2, q) dt
2πit
= Rest=q−mλ−1
2
1
θ(λ2, q)
X
k∈Z
(−1)kqk(k+1)/2λk
2B1 ˆf (0)(qkλ2t, q) dt
2πit
=
1
θ(λ2, q)
X
k∈Z
(−1)kqk(k+1)/2λk
2R(m −k, q)
=
1
θ(λ2, q)(−1)mqm(m+1)/2λm
2
∞
X
k=0
(−1)kqk(k−1)/2(q−mλ−1
2 )kR(k, q)
= −(q; q)2
∞
θ(λ2, q) (−1)mqm(m+1)/2λm
2
∞
X
k,ℓ=0
(−1)k
qk(k+1)/2
(q; q)ℓ(q; q)k−ℓ
(q−mλ−1
2 )k
= f (−1)(q−mλ−1
2 , q) .
(274)
□
Lemma 5.7. For t in some compact set where the functions are holomorphic, we have
lim
r→∞
g(0,2)(qrt, q)
θ(qrt; q)
=
1
(q; q)2
∞
m1,3(t−1, q)
lim
r→∞
f (0)(qrt, q)
θ(qrt; q)
= 0 .
(275)
Proof. We have
(−1)rqr(r+1)/2tr+1g(0,2)(qrt, q)
=
∞
X
k=−r
 
1
2
 
1
2E1(q) −r −1
2 −θ′(t−1; q)
θ(t−1; q) +
k+r
X
j=1
1 + qj
1 −qj
!2
−
 
1
2E1(q) −r −1
2 −θ′(t−1; q)
θ(t−1; q) +
k+r
X
j=1
1 + qj
1 −qj
!
θ′(t−1; q)
θ(t−1; q)
+ 1
2
θ′′(t−1; q)
θ(t−1; q) +
k+r
X
j=1
qj
(1 −qj)2 −1
24 −1
24E2(q)
!
(−1)k qk(k+1)/2
(q; q)2
k+r
t−k .
(276)
Then noting that 1/24 −E2(q)/24 −Pk
j=1 qj/(1 −qj)2) = O(qk+1) the proof then proceeds
as in Lemma 5.1.
□
To ﬁnish the proof of Theorem 1.8 we will use the state integrals introduced in [28,
Eqn.(73)].
Z
R+iε
Φb(x)2exp
 −πix2 −2π zx
b

1 + ˜q1/2 exp
 −2πx
b
 dx .
(277)
The factorisation of this integral was done in [28, Thm.7].
The fact this module is not
self dual (see Proposition 2.6) means that additional functions arise in the factorisation.
52
STAVROS GAROUFALIDIS AND CAMPBELL WHEELER
It was shown, using Equation (52), that Equation (277) factors as an elementary function
holomorphic in C′ times
I(z, τ) =τ 2g(0,2)(˜t, ˜q) + τg(0,1)(˜t, ˜q)L0(t, q) −g(0,0)(˜t, ˜q)L1(t, q)
(278)
where
L0(t, q) = 1 −1
2E1(q) + θ′(t−1; q)
θ(t−1; q) +
∞
X
k=1
(−1)k
qk(k+1)/2
(q; q)2
k(1 −qk)t−k
L1(t, q) = −5
12 + 1
2E1 −E1(q)2 −1
24E2(q) −
1
8 −1
8E1(q)
 θ′(t−1; q)
θ(t−1; q) −θ′′(t−1; q)
2θ(t−1; q)
+
∞
X
k=1
(−1)k
qk(k+1)/2
(q; q)2
k(1 −qk)t−k
 
1
2E1(q) −1
2 −θ′(t−1; q)
θ(t−1; q) +
k
X
j=1
1 + qj
1 −qj +
qk
1 −qk
!
.
(279)
These functions Li where then shown to satisfy
L0(t, q) −L0(qt, q) = −qtg(0,0)(qt, q)
L1(t; q) −L1(qt, q) = −qtg(0,1)(qt, q).
(280)
Notice that functions satisfying these equations are unique up to the addition of an elliptic
function. Therefore, with exactly the same argument in [28, Thm.4] with the addition of
checking the principal parts of the LHS and RHS we can then show that
V (t, q)−1
 
0
1
0
0
0
1
q−2t−1
−q−2
q−2t−1 −2q−1
!
=


−L1(t, q)
−qt2g(0,1)(qt, q)
qt2g(0,1)(t, q)
L0(t, q)
qt2g(0,0)(qt, q)
−qt2g(0,0)(qt, q)
1
0
0

.
(281)
Therefore, we see that the entries of ΩV,S are combinations of elementary functions times
I(z+n+mτ, τ) for m, n ∈{−2, −1, 0, 1, 2}. Using the explicit expressions for the monodromy
one can prove it satisﬁes Equation (32) with equal weights (2, 1, 0) and again using part (c)
of Theorem 1.2 complete the proof.
□
