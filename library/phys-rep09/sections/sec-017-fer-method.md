---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-017-fer-method
section_title: "Fer method"
section_number: null
pages: 23-25
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
An intuitive way to introduce Fer formalism is the following [59]. Given the matrix linear system Y ′ = A(t)Y, Y(0) = I,
we know that
Y(t) = exp(F1(t))
(95)
is the exact solution if A commutes with its time integral F1(t) =
R t
0 A(s)ds, and Y(t) evolves in the Lie group G if A lies in
its corresponding Lie algebra g. If the goal is to respect the Lie-group structure in the general case, we need to ‘correct’ (95)
without losing this important feature.
Two possible remedies arise in a quite natural way. The first is just to seek a correction ∆(t) evolving in the Lie algebra
g so that
Y(t) = exp (F1(t) + ∆(t)) .
174
S. Blanes et al. / Physics Reports 470 (2009) 151–238
This is nothing but the Magnus expansion. Alternatively, one may correct with Y1(t) in the Lie group G,
Y(t) = exp(F1(t))Y1(t).
(96)
This is precisely the approach pursued by Fer, i.e. representing the solution of (30) in the factorized form (96), where
(hopefully) Y1 will be closer to the identity matrix than Y, at least for small t.
The question now is to find the differential equation satisfied by Y1. Substituting (96) into Eq. (30) we have
d
dt
Y =

d
dt
eF1

Y1 + eF1 d
dt
Y1 = AeF1Y1,
(97)
so that, taking into account the expression for the derivative of the exponential map (Lemma 2), one arrives easily at
Y ′
1 = A1(t)Y1
Y1(0) = I,
(98)
where
A1(t) = e−F1AeF1 −
Z 1
0
dx e−xF1AexF1.
(99)
The above procedure can be repeated to yield a sequence of iterated matrices Ak. After n steps we have the following recursive
scheme, known as the Fer expansion:
Y = eF1eF2 · · · eFnYn
(100)
Y ′
n = An(t)Yn
Yn(0) = I,
n = 1, 2, . . .
with Fn(t) and An(t) given by
Fn+1(t) =
Z t
0
An(s)ds
A0(t) = A(t),
n = 0, 1, 2, . . .
An+1 = e−Fn+1AneFn+1 −
Z 1
0
dx e−xFn+1AnexFn+1
=
Z 1
0
dx
Z x
0
du e−(1−u)Fn+1 [An, Fn+1] e(1−u)Fn+1
=
∞
X
j=1
(−)j j
(j + 1)!
ad
j
Fn+1(An),
n = 0, 1, 2 . . . .
(101)
When, after n steps we impose Yn = I, we are left with an approximation to the exact solution Y(t).
Inspection of the expression of An+1 in (101) reveals an interesting feature of the Fer expansion. If we assume that a
perturbation parameter ε is introduced in A (i.e. if we substitute A by εA in the formalism), since Fn+1 is of the same order in
ε as An then an elementary recursion shows that the matrix An starts with a term of order ε2n (correspondingly the operator
Fn contains terms of order ε2n−1 and higher). This should greatly enhance the rate of convergence of the product in Eq. (100)
to the exact solution.
It is possible to derive a bound on the convergence domain in time of the expansion [30]. The idea is just to look for
conditions on A(t) which ensure Fn →0 as n →∞. As in the case of the Magnus expansion, we take A(t) to be a
bounded matrix with ∥A(t)∥≤k(t) ≡k0(t). Fer’s algorithm, Eqs. (100) and (101), then provides a recursive relation among
corresponding bounds kn(t) for ∥An(t)∥. If we denote Kn(t) ≡
R t
0 kn(s)ds, we can write this relation in the generic form
kn+1 = f (kn, Kn), which, after integration, gives
Kn+1 = M(Kn).
(102)
The question now is: when is Kn →0 as n →∞? This is certainly so if 0 is a stable fixed point for the iteration of the
mapping M and K0 is within its basin of attraction. To see when this is the case, we have to solve the equation ξ = M(ξ)
to find where the next fixed point lies. Let us do it explicitly. By taking norms in the recursive scheme (101) we have
∥An+1∥≤
Z 1
0
dx
Z x
0
du e2(1−u)Kn ∥[An, Fn+1]∥,
which can be written as ∥An+1∥≤kn+1, with
kn+1 =
1 −e2Kn(1 −2Kn)
2Kn
dKn
dt
S. Blanes et al. / Physics Reports 470 (2009) 151–238
175
and consequently Kn+1 is given by Eq. (102) with
M(Kn) =
Z Kn
0
1 −e2x(1 −2x)
2x
dx.
(103)
That is the mapping we have to iterate. It is clear that ξ = 0 is a stable fixed point of M. The next, unstable, fixed point is
ξ = 0.8604065. So we can conclude that we have a convergent Fer expansion, at least for values of time t , such that
Z t
0
∥A(s)∥ds ≤K0(t) < 0.8604065.
(104)
Notice that the bound for the convergence domain provided by this result is smaller than that corresponding to the Magnus
expansion (Theorem 9).
