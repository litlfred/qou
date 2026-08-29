---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-055-2-trh2-cn
section_title: "TrH2 = cN"
section_number: 2
pages: 68-72
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
N
Y
i=1
Z
dHiie−1
2 H2
ii
N
Y
i<j
Z
d2Hije−|Hij|2 = (2π)N2/2,
while according to eqs.(3.48) and (3.49) the same integral is equal to
1
N!
N
Y
i=1
Z +∞
−∞e−1
2h2
i
N
Y
i>j
(hi −hj)2 =
N
Y
j=1
|| Hej−1 ||2 .
Here || Hej−1 || stand for the norms of orthogonal Hermite polinomials (3.50),
|| Hek ||2=
√
2πk!. Comparing the two expressions for the same integral we
get:
c−1
N = (2π)
N2
2
N−1
Y
k=0
1
√
2πk! = (2π)
N(N−1)
2
QN−1
k=0 k! .
(3.71)
According to (3.5)
c−1
N = N! VolU(N)
(VolU(1))N
65
and VolU(1) = 2π. Thus we obtain eq.(3.6):
VolU(N) = (2π)
N(N+1)
2
QN
k=0 k! .
An example of somewhat more sophisticated (quantum) group-theoretical
quantity, arising from Gaussian matrix models, is provided by the following
formula for the q-factorial [71] (see also [72]):
1
(q, q)N
≡
N
Y
n=1
1
1 −qn =
R R
N×N dH[dU]e−m2TrH2+TrHUHU†
VolU(N)
R
N×N dHe−m2TrH2
.
(3.72)
Integral in the numerator is over Hermitean (H) and unitary (U) N × N
matrices, and q ≡m2 −
√
m4 −1.
Explicit expression (3.71) can be used to prove that cN = 0 for all negative
integer N [36]. Eq.(3.71) deﬁnes cN only for positive integer N as a ﬁnite
product. There is an obvious prescription for analytical continuation of such
products, provided continuation of the items is known (it can be considered
as implied by the similar formula for integrals with the varying upper limit):
Let
F(N) =
N
X
k=−∞
f(k).
(3.73)
Then
S(N) ≡
N
X
k=1
f(k) = F(N) −F(0)
(3.74)
and, obviously, F(0) −F(−N) = P0
k=1−N f(k), so that
S(−N) ≡F(−N) −F(0) = −
N−1
X
k=0
f(−k).
(3.75)
Exponentiation of this formula gives the rule for the products. In the case
of cN one can treat factorials in (3.71) as Gamma-functions,
(2π)
N(N−1)
2
cN =
N
Y
k=1
Γ(k),
(3.76)
66
and obtain:
(2π)−N(N+1)
2
c−N =
 N−1
Y
k=0
Γ(−k)
!−1
= 0,
(3.77)
because of the poles of Γ-functions.
4
Integrable structure of eigenvalue models
4.1
The concept of integrability
Integrable structure of dynamical system implies that all the dynamical char-
acteristics - solutions of equations of motion for a classical system and func-
tional integrals for a quantum one - can be found exactly. According to this
description the notion of integrability is not very concrete, and in fact it
evolves with time, including more and more classes of theories into the class
of integable systems. Nowadays we consider the following types of theories
as clearly belonging to this class:
- Free motion (classical or quantum) on group manifolds and homogeneous
spaces;
- 2-dimensional conformal theories and their ”integrable massive defor-
mations”;
- Integrable hierarchies of the (multicomponent) KP and Toda type and
their reductions;
- Functional integrals, subjected to conditions of (generalized) Duistermaat-
Heckman theorem;
- (Eigenvalue) matrix models;
- Topological theories;
- Many supersymmetric models (at least those allowing for Nicolai trans-
formation and/or Duistermaat-Heckman-like description);
- Systems with (inﬁnitely) many local integrals of motion.
This list (nothing to say about the order of items) is rather arbitrary. Also
diﬀerent items are not really diﬀerent and (as it should be) can be considered
as diﬀerent descriptions of the same reality. Now we discuss very brieﬂy at
least some of the most important views on the concept of integrability.
67
Often the notion of integrability is related to occurence of ”many enough”
integrals of motion (”many enough” means equal to the number of degrees
of freedom). This is, however, not such a rigid deﬁnition as one can think.
In fact, in classical mechanics there is usually a complete set of integrals of
motion available: just initial conditions in the phase space (or, to be more
sophisticated, angle-action variables). The problem is, however, that
a) these obvious integrals are very complicated (non-local and multi-
valued) functionals of the current coordinates, and
b) in general situation they are very ”unstable” under a small change of
current coordinates (”divergency of trajectories”).
In order to avoid these problems one usually imposes a ”locality” con-
dition on equations of motion. While this is a reasonable thing to do for
particular classes of theories (e.g.
possessing a well deﬁned kinetic term,
which is quadratic in momenta), this is not a nice decription in general situ-
ation, since ”locality” is not invariant under arbitrary (including non-local)
change of variables. In practice, when approached from this side, integrabil-
ity implies a kind of ”regular” behaviour of trajectories and some more or
less nicel deﬁned transformation from ”natural” (or, better to say, ”original”)
coordinates to the action-angle variables.
Situation becomes even less clear when quantum theory is considered,
since ”chaotic behaviour” no longer implies anything really ”chaotic” for the
quantum system. Again, very much depends on what kind of observables
one wants to consider, and any notion of ”regularity” is not enough under
arbitrary change of variables.
This can be made even more transparent, if one recalls the idea of univer-
sality classes, so important in the modern theory. The idea is that even in the
cases when behaviour of the system seems absolutely haotic from any naive
point of view (like in the cases of turbulence or quantum gravity), one can
and should introduce new variables (which can be very complicated functions
of original ones), which have smooth and well deﬁned correlation functions.
In most cases one is not attempting to ﬁnd a complete set of such variables
(and thus some information is lost), but this reﬂects nothing but the current
state of knowledge, and in fact in studies of 2d quantum gravity the goal of
complete descrption is already clearly fromulated.
Despite these comments, the ”deﬁnition” of integrability in terms of
”many enough” local integrals of motion should be put at the ﬁrst place
in our discussion, because most of the systems which were so far considered
68
as integrable more or less naturally get into this class, allowing for some
prefered choice of dynamical variables (”more or less” appears because some
”minor” non-locality is usually present in any interesting examples, where
angle-action variables are not obvious from the very beginning).
This ”deﬁnition” is so unclear because we attempted to look for a generic
description of integrability. Most interesting approaches, however, go from
another direction. One starts from some simple system and then perform a
change of variables, which makes it looking much more complicated (being
still simple in its essense). This appears to be a much more fruitfull view on
the problem and in fact all the other items of our list above are describable
in this kind of terms.
A trivial, but surprisingly representative example of this approach is pro-
vided by a free particle, moving in ﬂat D-dimensional space.
The eigen-
functions of Laplace operator are just plain waves or, equivalently, spherical
harmonics. The radial part of the j-th harmonic is already a not very simple
function, satisfying the equation
 
−d2
dr2 + D −1
r
d
dr + C2(j)
r2
!
ψ(r) = Eψ(r).
(4.1)
This equation is of course less trivial than the original Laplace equation, but
their solutions are related in a simple way. In order to ﬁnd a solution of (4.1),
say, for j = 0, one should just take an angular average of a plane wave:
φk(r) =
Z
eik⃗r⃗νdD−1⃗ν;
|⃗ν |= 1.
(4.2)
This integral representation expresses the solutions of (4.1) through Bessel
functions, and this is in fact the proper way to derive the well-known formula:
φk(r) = 2
D
2 −1Γ
D
2

(kr)1−D
