---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-004-15-modular-q-holonomic-modules-in-chernsimons-th
section_title: "Modular q-holonomic modules in Chern–Simons theory"
section_number: 1.5
pages: 7-12
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
present threeq-holonomic modules whose cocycles play a key role in complex Chern–Simons
theory and prove their modularity. We will not need a detailed knowledge of Chern–Simons
theory, but focus on the fact that it is a gauge theory with gauge group a complex Lie group,
whose partition function can be identiﬁed by a ﬁnite dimensional integrals of products of
the Faddeev quantum dilogarithm. A detailed exposition of Chern–Simons theory is given
in the work of Andersen–Kashaev and Beem, Dimofte and Pasquetti [3, 18, 5, 62]. The
quasi-periodicity of the Faddeev quantum dilogarithm implies that the partition function of
complex Chern–Simons theory satisﬁes aq-holonomic module of linearq-diﬀerence equations.
In the modularq-holonomic modules discussed below, we prove their modularityand at the
same time deﬁne and compute fundamental matrices U and V of solutions algorithmically,
and give explicit formula for their monodromy. This is possible because of two key features,
namely:
(a) The fundamental matrices U and V are meromorphic functions with explicit poles
and with residues expressed linearly in terms of U and V . This is some kind of
resurgence property and it is ultimately responsible for determining the monodromy.
8 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
(b) The monodromy is uniquely determined by its elliptic property, the explicit poles
and principle parts, and its limiting values at t = 0 or t =∞.
Our ﬁrst module, the linear q-diﬀerence equation for the inﬁnite Pochhammer symbol
(1−qt)f(qt,q )−f(t,q ) = 0, (19)
has trivial monodromy but its cocycle is a very interesting function, the Faddeev quantum
dilogarithm function which is the building block of the partition function of complex Chern–
Simons theory. With the deﬁnition off (0) andg(1) given in Equations (156) and (161) below,
we deﬁne the fundamental matrices U(t,q ) and V (t,q ) of solutions at t = 0 and t =∞ by
U(t,q ) =W (f (0)(t,q )), V (t,q ) =W (g(1)(t,q )), (20)
with equal weights κ = 0. In our theorems below, we will use the terms “a q-holonomic
module is modular” and “its cocycle in modular” interchangeably.
Theorem 1.5. The monodromy matrix is
−→
M(t,q ) = (1). The two cocycles (4) ΩU and ΩV
are equal, modular and when γ =S, they are given explicitly by
ΩS(z,τ ) = Φb
(iz
b + ib
2 + 1
2ib
)−1
(21)
where Φ is the Faddeev quantum dilogarithm function [23, 24].
In forthcoming work [31], the cocycle Ω γ will be identiﬁed with an SL 2(Z )-extension of
the Faddeev quantum dilogarithm, and its modularity will be deduced independently, using
properties of the odd Eisenstein series.
Our second module is the q-diﬀerence equation of the Appell-Lerch sums studied in [9, 74]
and given by
f(q2t,q ) + (qt− 1)f(qt,q )−tf(t,q ) = 0. (22)
The cocycle of (22) is the Appell-Lerch sum, which is the building block for the extension
of the partition function of complex Chern–Simons theory that detects the trivial ﬂat con-
nection, see [28]. In the above equation, some formal power series solutions are divergent,
and theirq-Laplace resummation is expressed in terms of an Appell-Lerch sum that depends
on an additional elliptic variable. The monodromy of this equation is an explicit product
of theta functions that depends on two elliptic variables, but the cocycle is independent of
them, and is expressed explicitly in terms of the Mordell integral. Our results give a new
interpretation of the Mordell integral and Appell-Lerch sums emphasising the role of the lin-
earq-diﬀerence equations as opposed to the aspects of modular forms advocated by Zwegers
in his thesis [74] and by Dabholkar–Murthy–Zagier [17] in the study of mock modular forms
and their incarnations in the mathematical physics of black holes.
With the deﬁnition of f (−1), f (0), g(0) and g(1) given in Equations (175), (170), (177)
and (178) below, we deﬁne the fundamental matrices U(t,λ,q ) and V (t,µ,q ) of solutions at
t = 0 and t =∞ by
U(t,λ,q ) =W (f (0)(t,λ,q ),f (−1)(t,q )), V (t,µ,q ) =W (g(0)(t,µ,q ),g (−1)(t,q )), (23)
with equal weights κ = (0, 1).
MODULAR q-HOLONOMIC MODULES 9
Theorem 1.6. (a) The monodromy matrix
−→
M(t,λ,µ,q ) =V (t,µ,q )−1U(t,λ,q ) is given by
−→
M(t,λ,µ,q ) =
(
1 0
∗ 1
)
(24)
where
−→
M2,1(t,λ,µ,q ) =−(q;q)3
∞θ(q−1t;q)θ(λ−1µ;q)θ(λ−1µ−1t−1;q)
θ(λ−1;q)θ(µ;q)θ(λ−1t−1;q)θ(µ−1t−1;q) . (25)
The matrix
−→
M satisﬁes the modular transformation (6).
(b) The two cocycles (4) ΩU and ΩV are equal, modular, independent of λ and µ and when
γ =S, are given explicitly by
ΩS(z,τ ) =
(0 1
1 −˜t
)( τ−1 0
e( 1
8)√τ
˜t− 1
2 ˜q
1
8e
(
z2
2τ
)
h(z,τ )
e( 1
8)√τ e
(
− (z+1/2−τ/ 2)2
2τ
)
)(
0 1
1 −t
)−1
(26)
where
h(z,τ ) =
∫
R
eπi(τx 2+2izx)
2 cosh(πx)dx. (27)
is the Mordell integral.
Our third module is a linear q-diﬀerence equation associated to quantum invariants of the
simplest hyperbolic knot 4 1,
tqf (qt;q) + (1− 2t)f(t;q) +tq−1f(q−1t;q) = 0. (28)
This equation, which is also related to theq-Hahn Bessel function, appeared in homogeneous
form in [27, Eqn.(11)]. With the deﬁnition of f (−1), f (1) and g(0,0) and g(0,1) given in Equa-
tions (201), (205) and (209) below, we deﬁne the fundamental matrices U(t,λ,q ) andV (t,q )
of solutions at t = 0 and t =∞ by
U(t,λ,q ) =W (f (1)(t,λ,q ),f (−1)(t,q )), V (t,q ) =W (g(0,0)(t,q ),g (0,1)(t,q )), (29)
and equal weights κ = (1, 0).
Theorem 1.7. (a) The monodromy matrix
−→
M(t,λ,q ) =V−1(t,q )U(t,λ,q ) is given by
−→
M(t,λ,q ) =
( −1 0
−→
M2,1(t,λ,q ) 1
)
(30)
where
−→
M2,1(t,λ,q ) = θ(qt;q)θ(tλ;q)θ(tλq−1/2;q)θ(tλ2q−1/2;q)
θ(tλq1/4;q)θ(−tλq1/4;q)θ(tλq−1/4;q)θ(−tλq−1/4;q)θ(q−1λ;q)θ(q−3/2λ;q).
(31)
The matrix M satisﬁes the modular transformations
∆T 2,κ
−→
M|κT 2 =
−→
M, ∆STS,κ
−→
M|κSTS =
−→
M, ∆TST,κ
−→
M|κTST =
−→
M. (32)
It follows that the SL2(Z )-orbit of M consists of three functions M, ∆T,κ
−→
M|κT, ∆S,κ
−→
M|κS.
(b) The two cocycles (4) Ω Av(U ) and ΩV , deﬁned by the averaging
Av(U) =V Av(
−→
M), Av(
−→
M) = 1
3
(−→
M + ∆T,κ
−→
M|κT + ∆S,κ
−→
M|κS
)
, (33)
10 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
are equal, modular, independent ofλ and whenγ =S, they are given by elementary functions
times the state integrals
∫
R +iε
Φb(x)2 exp
(
−πix2− 2πb−1zx
)
dx. (34)
The above can be phrased by saying that M is modular on an index three subgroup Γ′ of
SL2(Z ) (conjugate to theθ subgroup and to the congruence subgroup Γ0(2) of SL2(Z )) and if
γ∈ Γ′ then ΩU,γ = ΩV,γ is independent of λ and modular. The corresponding state integrals
are deﬁned in forthcoming work [31]. However, the modularity of the module follows from
Theorem 1.2.
The equation (28) has two important extensions, each containing important information
about the knot. The ﬁrst extension is an inhomogeneous version, which for the 4 1 knot,
takes the form (see [37, Eqn.(98)] and [28, Sec.2.2])
tqf (qt;q) + (1− 2t)f(t;q) +tq−1f(q−1t;q) = 1. (35)
The solution f (0) at t = 0 given in Equation (255) below is a resummation of the Kashaev
invariant of the 4 1 knot, whereas the solution g(0,2) given in Equation (258) below is a q-
series that appeared recently in [28] in relation to the asymptotic expansion of the Kashaev
invariant at the trivial representation. With those two solutions, we deﬁne the fundamental
matrices
U(t,λ 1,λ 2,q ) =W (f (1)(t,λ 1,q ),f (−1)(t,q ),f (0)(t,λ 2,q ))
V (t,q ) =W (g(0,0)(t,q ),g (0,1)(t,q ),g (0,2)(t,q )),
(36)
with equal weights κ = (2, 1, 0). The monodromy matrix involves the Weierstrass elliptic
function ℘, a well-known function discussed in detail for example in [2].
Theorem 1.8. (a) The monodromy matrix
−→
M(t,λ 1,λ 2,q ) =V (t,q )−1U(t,λ 1,λ 2,q ) is given
by
−→
M(t,λ 1,λ 2,q ) =


−1 0 ℘(t,q )
−→
M2,1(t,λ 1,q ) 1 1
2
℘′(t,q)−℘′(λ2,q)
℘(t,q)−℘(λ2,q)
0 0 1

 (37)
where
−→
M2,1 is given by (31). The matrix M satisﬁes the modular transformations (32) with
weight κ = (2, 1, 0).
(b) The two cocycles (4) ΩAv(U ) and ΩV are equal, modular, independent of λ1,λ 2 and when
γ =S, they are given by combinations of elementary functions times the state integrals
∫
R +iε
Φb(x)2 exp (−πix2− 2πb−1zx)
1 + ˜q1/2 exp (−2πb−1x)dx. (38)
The second and last extension of equation (35) is the addition of an x-variable in C ×,
which topologically measures the holonomy of the meridian of the knot, or the color of the
colored Jones polynomial, and behaves like a Jacobi variable. The new equations are now a
two variable holonomic system and take the form
tqf (qt,x,q ) + (1− (x−1 +x)t)f(t,x,q ) +tq−1f(q−1t,x,q ) = 1 (39a)
MODULAR q-HOLONOMIC MODULES 11
(1−qx)(1−q−1x2)f(t,qx,q )
−(x− 1)2(x + 1)(x2t−x− (q−1 +q)t−x−1 +x−2t)f(t,x,q )
+(1−qx2)(1−q−1x)f(t,q−1x,q ) = (1 +x−1)(1−qx2)(1−q−1x2),
(39b)
(1−xq)(f(t,qx,q )−x−1f(qt,qx,q )) = (1−x−1)(f(t,x,q )−qxf (qt,x,q )). (39c)
This is not a random system of equations, instead they are the deﬁning equations of the
descendant colored Jones polynomial of the 41 knot, and appeared explicitly in [28, Eqn.(97)].
This is a q-holonomic module of rank 3, with fundamental solutions f (j)(t,x,q ) for j =
−1, 0, 1 at t = 0 and g(0,xj )(t,x,q ) for j =−1, 0, 1 at t =∞ deﬁned in Equations (283),
(290) and (291). With these solutions we can deﬁne the fundamental matrices with respect
to the shift in t as
U(t,x,λ 1,λ 2,q ) =W (f (1)(t,x,λ 1,q ),f (−1)(t,x,q ),f (0)(t,x,λ 2,q )),
V (t,x,q ) =W (g(0,x−1)(t,x,q ),g (0,x)(t,x,q ),g (0,1)(t,x,q )),
(40)
with weightsκU = (0, 1, 0) and κV = (1, 1, 0). The next theorem gives the properties of this
monodromy.
Theorem 1.9. (a) The monodromy matrix is given by
−→
M(t,x,λ 1,λ 2,q ) =


1 −1 0
−1 −1 0
0 0 1

×


θ(x−2;q)θ(t;q)2(q;q)3
∞
2θ(q−1x;q)2θ(tx;q)θ(tx−1;q) 0 θ(x−2;q)θ(t;q)2(q;q)3
∞
2θ(q−1x;q)2θ(tx;q)θ(tx−1;q)
m2,1(t,x,λ 1,q ) 1
(
θ′(tλ2)
θ(tλ2)− θ′(tx)
2θ(tx)− θ′(tx−1)
2θ(tx−1)− θ′(λ2)
θ(λ2)− 1
2
)
0 0 1


(41)
where m2,1(t,x,λ 1,q ) is the unique elliptic function in t satisfying m2,1(1,x,λ 1,q ) = 0 with
simple poles at t0∈{x±qZ ,±λ−1q
1
2 Z } and residues ρt0 := Rest=t0m2,1(t,x,λ 1,q ) dt
2πit given by
ρx±qZ =−1
2
ρ±λ−1
1 q−1/4−Z = θ(±q3/4λ−1
1 ;q)θ(±q−1/4x;q)θ(±q−3/4x;q)θ(±q−3/4λ1;q)
2θ(x;q)θ(x−1;q)θ(q−1λ1;q)θ(q−3/2λ1;q)
ρ±λ−1
1 q−3/4−Z = θ(±q1/4λ−1
1 ;q)θ(±q−1/4x;q)θ(±q−3/4x;q)θ(±q−1/4λ1;q)
2θ(x;q)θ(x−1;q)θ(q−1/2λ1;q)θ(q−1λ1;q) .
(42)
The monodromy satisﬁes the following modular transformations
∆T 2,κV
−→
M|κUT 2 =
−→
M, ∆STS,κV
−→
M|κUSTS =
−→
M, ∆TST,κV
−→
M|κUTST =
−→
M. (43)
(b) The two cocycles (4) ΩAv(U ) and ΩV are equal, modular, independent of λ1,λ 2 and when
γ =S, they are given by combinations of elementary functions times the state integrals
∫
C
Φb(x +ibu)Φb(x−ibu)exp (−πix2− 2πb−1zx)
1 + ˜q1/2 exp (−2πb−1x)dx. (44)
12 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
An explicit formula for the function m2,1 is given in Equation (296) below.
The next theorem identiﬁes the function f (0)(t,x,λ 1,q ) with the q-Borel resummation of
the descendant of the colored Jones polynomial, and provides a lift of the colored Jones
polynomial (as a function of N and q) to an analytic function of x and q. Its extension to
all knots will be discussed in forthcoming work.
Theorem 1.10. The N-th colored Jones polynomial JN(q) of 41 for|q|< 1 is given by
JN(q) =f (0)(1,qN,λ 2,q ). (45)
Note that there is noλ2 dependence on the left hand side of (45) and that λ2 parametrises
a family of analytic continuations of the colored Jones polynomial as we vary x away from
qN.
The cocycles given in the previous theorems reveal the relation of the following three
special functions (all being entries of a matrix-valued S-cocycle of a modular q-diﬀerence
equation)
(a) the Fadeev quantum dilogarithm
(b) the Mordell integral
(c) the Andersen-Kashaev state integral.
We end this section with some comments regarding modular q-holonomic modules. It is
not obvious that q-holonomic modules exist or occur naturally. Yet, they are abundant, for
instance all properq-hypergeometric multidimensional sums areq-holonomic; see Zeilberger–
Wilf [69]. A detailed introduction of q-holonomic modules and their functional and closure
properties can be found in [33, 49, 63].
Regarding the occurence of q-holonomic modules, they are often given in the form Mf =
Wf wheref : Z r→ Q (q) is a quantum invariant. For instance, iff denotes the colored Jones
polynomial of a link (colored with an arbitrary representation of a ﬁxed simple Lie group),
or the colored HOMFLY-PT polynomial of a link (colored by arbitrary partitions with a
ﬁxed number of rows or columns), the corresponding modules Mf are q-holonomic; see [34]
and [32]. In addition, the special q-hypergeometric sums (so-called Nahm sums) studied
in [37, Sec.4.7] that depend on the upper-half of a symplectic matrix, are q-holonomic.
Moreover, the linearq-diﬀerence equations in quantum cohomology or in quantumK-theory
are often (and perhaps always?) specialisations of q-hypergeometric series; see [61, 35, 44,
68]. Finally, the q-GKZ modules of Gelfand–Kapranov–Zelevinsky [39, 40, 41] which are
constructed by combinatorial data (a matrix of integers) together with some “charge vectors”
are q-holonomic.
The above discussion leads naturally to the following conjecture.
Conjecture 1.11. Every q-holonomic module associated to a proper q-hypergeometric
multi-dimensional sum is modular.
