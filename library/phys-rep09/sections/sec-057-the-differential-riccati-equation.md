---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-057-the-differential-riccati-equation
section_title: "The differential Riccati equation"
section_number: null
pages: 76-78
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Let us now consider the two-point boundary value problem in the t variable defined by the linear differential equation
y′ ≡

y′
1
y′
2

=

A(t)
B(t)
C(t)
D(t)
 
y1
y2

,
0 < t < T
(334)
with separated boundary conditions
(K11 K12)

y1
y2

t=0
= γ1,
(K21 K22)

y1
y2

t=T
= γ2.
(335)
Here A ∈Cq×q , B ∈Cq×p, C ∈Cp×q , D ∈Cp×p , whereas y1, γ2 ∈Cp, y2, γ1 ∈Cq and the matrices Kij have appropriate
dimensions. We next introduce the time-dependent change of variables (or picture) y = Y0(t)w, with
Y0(t) =

Ip
0
X(t)
Iq

(336)
and choose the matrix X ∈Cp×q so as to ensure that in the new variables w = Y −1
0 (t)y the system assumes the partly
decoupled structure [191]
w′ ≡

w′
1
w′
2

=

A + BX
B
O
D −XB
 
w1
w2

,
(337)
S. Blanes et al. / Physics Reports 470 (2009) 151–238
227
together with the corresponding boundary conditions for w. It turns out that this is possible if, and only if, X(t) satisfies the
so-called differential Riccati equation [192]
X′ = C(t) + D(t)X −XA(t) −XB(t)X,
X(0) = X0
(338)
for some X0. By requiring
X0 = −K −1
12 K11,
(339)
then the boundary conditions (335) also decouple as
(O K12)w(0) = γ1,
(K21 + K22X(T)
K22) w(T) = γ2.
(340)
Here we assume, without loss of generality, that K12 is invertible. In this way, the original boundary value problem can be
solved as follows [191,192]: (i) solve Eq. (338) with initial condition (339) from t = 0 to t = T; (ii) solve the w2-equation
in (337) and (340), also from zero to T; (iii) solve the w1-equation in (337) from t = T to t = 0 and recover y = Y0(t)w. In
other words, the solution of the original two-point boundary value problem can be obtained by solving a sequence of three
different initial value problems, one of which involves the nonlinear equation (338). Obviously, steps (i) and (iii) can be solved
using numerical integrators based on the Magnus expansion. It could be perhaps more surprising that these algorithms can,
indeed, be used to integrate the Riccati equation in step (ii).
Although the boundary value problem (334) is a convenient way to introduce the differential Riccati equation (338),
this equation arises in many fields of science and engineering, such as linear quadratic optimal control, stability theory,
stochastic control, differential games etc. Accordingly, it has received considerable attention in the literature, both focused
on its theoretical aspects [193,194] and its numerical treatment [191,195,196].
In order to apply Magnus methods to numerically solve the Riccati equation, we first apply the transformation
X(t) = V(t)W −1(t),
(341)
with V ∈Cp×q, W ∈Cq×q and V(0) = X0, W(0) = Iq, in the region where W(t) is invertible. Then Eq. (338) is equivalent
to the linear system
Y ′ = S(t) Y(t),
Y(0) =

Iq
X0

(342)
with
Y(t) =

W(t)
V(t)

,
S(t) =

A(t)
B(t)
C(t)
D(t)

(343)
so that the previous Magnus integrators for linear problems can be applied here. Apparently, this system is similar to (334),
but now we are dealing with an initial value problem and Y is a matrix instead of a vector.
When dealing in general with the differential Riccati equation (338), it is meaningful to distinguish the following three
cases:
(i) The so-called symmetric Riccati equation, which corresponds to q = p, D(t) = −A(t)T real, and B(t), C(t) real
and symmetric matrices. In this case, the solution satisfies X T = X. It is straightforward to show that this problem
is equivalent to the treatment of the generalized time-dependent harmonic oscillator, described by the Hamiltonian
function
H =
1
2
pTB(t)p + pTA(t)q −
1
2
qTC(t)q.
The approximate solution attained by Magnus integrators, when applied to (342)–(343), can be seen as the exact
solution corresponding to a perturbed symplectic matrix ˜S(t) ≃S(t). In other words, we are solving, exactly, a
perturbed Hamiltonian system so that the approximate solution, ˜X, will share several properties of the exact solution,
in particular ˜X T = ˜X.
(ii) The linear non-homogeneous problem
X′ = D(t)X + C(t)
(344)
corresponds to the particular case A = 0 and B = 0 in (338).
(iii) The problem
X′ = D(t)X + XA(t)
(345)
is recovered from (338) by taking C = 0 and B = 0. It has been treated in [36] by developing an ad hoc Magnus-type
expansion. Notice that the case p = q, D = −A corresponds to the linear isospectral system (238).
228
S. Blanes et al. / Physics Reports 470 (2009) 151–238
