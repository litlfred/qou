---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-002-ii-the-system-of-partial-differential-equations
section_title: "THE SYSTEM OF PARTIAL DIFFERENTIAL EQUATIONS"
section_number: II
pages: 9-16
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
A. Derivation of the Equations
A central role in the derivation of our equations is played by the commutator identity
h
L, (I −K)−1i
= (I −K)−1 [L, K] (I −K)−1
(2.1)
for any operators K and L. Taking L to be D (= d/dx) or M (=multiplication by the
independent variable) give two of the three basic ingredients from which the equations are
derived. The third is the equally simple fact that if K depends upon a parameter α then
d
dα (I −K)−1 = −(I −K)−1 dK
dα (I −K)−1 .
(2.2)
It will be very useful for us to think of K as acting not on J but on (−∞, ∞) and to
have kernel
K(x, y)χJ(y)
(2.3)
where χJ is the characteristic function of J. We continue to denote the resolvent kernel of
K by R(x, y) but note that while it is smooth in x it is discontinuous at y = aj. Thus the
quantity R(aj, aj) appearing in (1.1) must be interpreted to mean
lim
y→aj
y∈J
R(aj, y);
similarly for pj and qj in (1.2) and like quantities appearing later. The deﬁnitions of u and
v must be modiﬁed to read
u =

AχJ, (I −K)−1 A

,
v =

AχJ, (I −K)−1 A′
.
(2.4)
Notice that since
(I −K)−1 A = (I −K)−1 AχJ
in J
this agrees with the original deﬁnitions of u and v given by (1.3).
9
We can think of K as an operator taking smooth functions to smooth functions and
so the operators KD and DK make sense, the former having distributional kernel. The
transpose operator Kt takes distributions to distributions.
With these preliminaries out of the way we begin with the derivation of the representa-
tions of the quantities R(aj, ak) in terms of the qj, pj, u and v. We introduce the notation
Q = (I −K)−1 A,
P = (I −K)−1 A′ ,
(2.5)
so that qj = Q(aj), pj = P(aj). (For the moment we ignore the dependence of Q and P on
the parameter a = (a1, · · · , a2m); this will come later.)
The ﬁrst commutator relation we use is the simple
[M, K] .= (A(x)A′(y) −A′(x)A(y)) χJ(y)
(where .= means “has kernel equal to”). Hence from (2.1) with L = M
h
M, (I −K)−1i .= Q(x)

I −Kt−1 A′χJ(y) −P(x) (I −K)−1 AχJ(y)
(2.6)
(The transpose here arises from the general fact that if L .= U(x)V (y), then T1LT2
.=
T1U(x) T t
2V (y).) If we use the fact that

I −Kt−1 AχJ = (I −K)−1 A
on J,
(2.7)
we deduce from (2.5) and (2.6) that [15]
R(x, y) = Q(x)P(y) −P(x)Q(y)
x −y
(x, y ∈J, x̸ = y) .
(2.8)
In particular, therefore,
R(aj, ak) = qjpk −pjqk
aj −ak
(j̸ = k),
(2.9)
R(aj, aj) = Q′(aj)pj −P ′(aj)qj
 
′ = d
dx
!
.
(2.10)
To compute Q′(x) and P ′(x) we consider ﬁrst the commutator [D, K]. If an operator L
has distributional kernel L(x, y) then
10
[D, L] .=
 ∂
∂x + ∂
∂y
!
L(x, y) .
(2.11)
It is an easy veriﬁcation, using the equation A′′(x) = xA(x), that
 ∂
∂x + ∂
∂y
!
K(x, y) = −A(x)A(y)
(2.12)
and so (recall the deﬁnition (2.3) of the kernel of K)
[D, K] .= −A(x)A(y)χJ(y) −
X
k
(−1)kK(x, ak)δ(y −ak) .
Hence, applying (2.1) with L = D (and recalling deﬁnitions (2.5)),
h
D, (I −K)−1i
= −Q(x)

I −Kt
AχJ(y) −
X
k
(−1)kR(x, ak)ρ(ak, y)
(2.13)
where
ρ(x, y) = δ(x −y) + R(x, y)
is the distributional kernel of (I −K)−1.
We proceed with the computations of Q′(x) and P ′(x). Diﬀerentiating the ﬁrst relation
in (2.5) and using (2.13) give
Q′ = D(I −K)−1A = P +
h
D, (I −K)−1i
A
= P −Q

I −Kt−1 AχJ, A

−
X
k
(−1)kR(·, ak)qk .
Thus (recall (2.4))
Q′(x) = P(x) −Q(x)u −
X
k
(−1)kR(x, ak)qk .
(2.14)
Similarly
P ′ = (I −K)−1A′′ +
h
D, (I −K)−1i
A′ .
Since A′′(x) = xA(x) this is equal to
M (I −K)−1 A −
h
M, (I −K)−1i
A +
h
D, (I −K)−1i
A′ .
11
We now use formula (2.6) and (2.13) to deduce that
P ′(x) = xQ(x) −2Q(x)v + P(x)u −
X
k
(−1)kR(x, ak)pk .
(2.15)
Setting x = aj in (2.14) and (2.15) and using (2.10) give
R(aj, aj) = p2
j −ajq2
j + 2q2
jv −2pjqju +
X
k
(−1)kR(aj, ak)(qjpk −pjqk) .
In view of (2.9) this is precisely equation (1.10).
Most of the work is already done and we can derive the equations (1.4)–(1.9) very quickly.
First, we have the easy fact
∂
∂ak
K .= (−1)kK(x, ak)δ(y −ak)
and so by (2.2)
∂
∂ak
(I −K)−1 .= (−1)kR(x, ak)ρ(y −ak) .
(2.16)
At this point we must keep in mind that Q and P are functions of a as well, and so we
denote them now by Q(x, a) and P(x, a), respectively. We deduce immediately from (2.16)
and the deﬁnitions (2.5) that
∂
∂ak
Q(x, a) = (−1)kR(x, ak)qk,
∂
∂ak
P(x, a) = (−1)kR(x, ak)pk .
(2.17)
Since qj = Q(aj, a) and pj = P(aj, a) this gives
∂qj
∂ak
= (−1)kR(aj, ak)qk,
∂pj
∂ak
= (−1)kR(aj, ak)pk
(j̸ = k).
In view of (2.9) these are equations (1.4) and (1.5). Moreover
∂qj
∂aj
=
 ∂
∂x + ∂
∂aj
!
Q(x, a)

x=aj
,
∂pj
∂aj
=
 ∂
∂x + ∂
∂aj
!
P(x, a)

x=aj
and (2.17), (2.14) and (2.15) give
∂qj
∂aj
= pj −qju −
X
k̸=j
(−1)kR(aj, ak)qk ,
∂pj
∂aj
= ajqj −2qjv + pju −
X
k̸=j
(−1)kR(aj, ak)pk .
12
In view of (2.9) again, these are equations (1.6) and (1.7).
Finally, using the deﬁnition of u in (2.4), the fact
∂
∂aj
χJ(y) = (−1)jδ(y −aj) ,
and (2.16) we ﬁnd that
∂u
∂aj
= (−1)jA(aj)qj + (−1)j 
AχJ, R(·, aj)

qj .
But

AχJ, R(·, aj)

=
Z
J R(x, aj)A(x) dx =
Z
J R(aj, x)A(x) dx
since R(x, y) = R(y, x) for x, y ∈J. Since R(y, x) = 0 for x̸ ∈J the last integral equals
Z ∞
−∞R(aj, x)A(x) dx = A(aj) −qj .
Thus
∂u
∂aj
= (−1)jq2
j ,
which is (1.8). Equation (1.9) is derived analogously.
We end this section with two relations between u, v, the qj and the pj which in fact can
be used to represent u and v directly in terms of the qj and pj. These relations are
2v −u2 =
X
j
(−1)jq2
j ,
(2.18)
u = −
X
j

p2
j −ajq2
j −2pjqju + 2q2
jv

.
(2.19)
To obtain the ﬁrst of these observe that (1.4) and (1.6) imply
 X
k
∂
∂ak
!
qj = pj −qju
(2.20)
while from (1.8) and (1.9)
∂
∂aj

2v −u2
= 2(−1)jqj (pj −qju) .
13
Hence if we multiply both sides of (2.20) by 2(−1)jqj and sum over j we obtain
 X
k
∂
∂ak
! 
X
j
(−1)jq2
j

=
 X
k
∂
∂ak
! 
2v −u2
.
It follows that the two sides of (2.18) diﬀer by a function of (a1, · · · , a2m) which is invariant
under translation by any vector (s, · · · , s). Since, clearly, both sides tend to zero as all
ai →∞, their diﬀerence must be identically zero.
To deduce (2.19) we add (2.13) and (2.16) to obtain
 ∂
∂x + ∂
∂y +
X
k
∂
∂ak
!
R(x, y) = −Q(x)Q(y)
(x, y ∈J).
(Observe that the kernel of [D, (I −K)−1] is (∂/∂x + ∂/∂y)R(x, y).) Hence
 X
k
∂
∂ak
!
R(aj, aj) = −q2
j = −(−1)j ∂u
∂aj
,
the last by (1.8). Multiplying by (−1)j and summing over j gives
 X
k
∂
∂ak
! 
X
j
(−1)jR(aj, aj)

= −
 X
k
∂
∂ak
!
u .
From this we deduce, by an argument similar to the one at the end of the last paragraph,
that
X
j
(−1)jR(aj, aj) = −u .
(2.21)
If we substitute formula (1.10) into this we see that the resulting double sum vanishes and
we are left with (2.19).
B. Hamiltonian Structure
The partial diﬀerential equations (1.4)–(1.9) can be rewritten in a compact form that
reveals a symplectic structure with (1.10) deﬁning a family of commuting Hamiltonians. To
see this we ﬁrst change the notation slightly
q2j = −i
2x2j,
p2j = −iy2j,
q2j−1 = 1
2x2j−1,
p2j−1 = y2j−1,
14
for j = 1, 2, . . ., m, and
v = 1
2x0,
u = y0,
and introduce the canonical symplectic structure
{xj, xk} = {yj, yk} = 0,
{xj, yk} = δjk,
for j, k = 0, 1, . . ., m. Then equations (1.4)–(1.9) become
daxj = {xj, ω(a)}
and
dayj = {yj, ω(a)}
(j = 0, 1, . . ., m)
(2.22)
where
ω(a) = da log det (I −K)
=
2m
X
j=1
Gj(x, y) daj
(2.23)
and
Gj(x, y) = y2
j −1
4ajx2
j −xjyjy0 + 1
4x2
jx0 −1
4
2m
X
k=1
k̸=j
(xjyk −xkyj)2
aj −ak
.
Furthermore, the Gj’s are in involution
{Gj, Gk} = 0 .
This last result can be veriﬁed by a direct calculation, but as we discuss below, there is a
better way to understand why such Hamiltonians are in involution. We can summarize the
system of equations by saying, in words, that to ﬁnd the ak-ﬂow of the coordinates xj and
yj, one ﬂows according to Hamilton’s equation with Hamiltonian Gk. The consistency of
these equations (i.e. mixed partials are equal) follows immediately from this Hamiltonian
formulation (see, e.g. [28]).
When equations (1.4)–(1.9) are expressed in the Hamiltonian form (2.22), the equations
are exactly analogous to the case of the sine kernel [17] and in both cases the Hamiltonians
are deﬁned via (2.23). For the JMMS equations (see, e.g. [28]) this Hamiltonian system is
15
closely related to the Hamiltonian system studied by Moser [24]. In fact in both cases the
systems of partial diﬀerential equations can be formulated in terms of the classical R-matrix
approach to completely integrable systems. Such an approach identitﬁes the Lax operator
and hence the commuting ﬂow result above follows without any calculations. We refer the
reader to [12] for a discussion of this classical R-matrix formulation of these systems of
partial diﬀerential equations.
