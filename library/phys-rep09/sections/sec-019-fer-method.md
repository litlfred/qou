---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-019-fer-method
section_title: "Fer method"
section_number: null
pages: 23-25
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
An intuitive way to introduce Fer formalism is the following [59]. Given the matrix linear system Y’ = A(t)Y, Y(O) = I,
we know that

Y(t) = exp(Fi(t)) (95)

is the exact solution if A commutes with its time integral F,(t) = Io A(s)ds, and Y(t) evolves in the Lie group @ if A lies in
its corresponding Lie algebra g. If the goal is to respect the Lie-group structure in the general case, we need to ‘correct’ (95)
without losing this important feature.

Two possible remedies arise in a quite natural way. The first is just to seek a correction A(t) evolving in the Lie algebra
g so that

Y(t) = exp (Fi(t) + A(t)).
174 S. Blanes et al. / Physics Reports 470 (2009) 151-238

This is nothing but the Magnus expansion. Alternatively, one may correct with Y;(t) in the Lie group 3,
Y(t) = exp(Fi(t))¥i(t). (96)

This is precisely the approach pursued by Fer, i.e. representing the solution of (30) in the factorized form (96), where
(hopefully) Y; will be closer to the identity matrix than Y, at least for small t.
The question now is to find the differential equation satisfied by Y,. Substituting (96) into Eq. (30) we have

aye (Ser) Yreoy = Aelly,, (97)

dt dt dt

so that, taking into account the expression for the derivative of the exponential map (Lemma 2), one arrives easily at
Y,=A(t)Y, —-¥,(0) = 1, (98)

where

1
Aj(t) = e'AeM -[ dx e**1fe*h, (99)
0

The above procedure can be repeated to yield a sequence of iterated matrices Ay. After n steps we have the following recursive
scheme, known as the Fer expansion:

Y=elte®... ery, (100)
Yi =An(t)Yn  Yn(0)=1, n=1,2,...

with F,(t) and A,(t) given by
t
Fryi(t) = i] An(s)ds — Ao(t) = A(t), n=0,1,2,...
0

1
Anyi = eft Apel -[ dx e*fn+1 A, ene
0

(101)

1 x
| ax | due~O-Fntt (A, Fy]
0 0

(Yi
= De Gr Ditte - n=0,1,2....
=

When, after n steps we impose Y, = I, we are left with an approximation to the exact solution Y(t).

Inspection of the expression of A,; in (101) reveals an interesting feature of the Fer expansion. If we assume that a
perturbation parameter ¢ is introduced in A (i.e. if we substitute A by eA in the formalism), since F,+, is of the same order in
€ as A, then an elementary recursion shows that the matrix A, starts with a term of order e (correspondingly the operator
F, contains terms of order 2" and higher). This should greatly enhance the rate of convergence of the product in Eq. (100)
to the exact solution.

It is possible to derive a bound on the convergence domain in time of the expansion [30]. The idea is just to look for
conditions on A(t) which ensure F, — 0Oasn — oo. As in the case of the Magnus expansion, we take A(t) to be a
bounded matrix with ||A(t) || < k(t) = ko(t). Fer’s algorithm, Eqs. (100) and (101), then provides a recursive relation among
corresponding bounds kn(t) for ||An(t)||. If we denote Kn(t) = ty kn(s)ds, we can write this relation in the generic form
Kn41 =f (Kn, Kn), which, after integration, gives

Kny1 = M(Kn). (102)

The question now is: when is K, — 0asn — oo? This is certainly so if 0 is a stable fixed point for the iteration of the
mapping M and K, is within its basin of attraction. To see when this is the case, we have to solve the equation € = M(é)
to find where the next fixed point lies. Let us do it explicitly. By taking norms in the recursive scheme (101) we have

1 x
nll < | dx | duu 20-6 ILA, Fysalll
0 0

which can be written as ||An+1|| << Kn41, with

1 —e2%(1 — 2K,) dKy

k =
mt 2Kn dt
S. Blanes et al. / Physics Reports 470 (2009) 151-238 175

and consequently K,,+1 is given by Eq. (102) with

Kn _ p2x _
M(Kn) = [ 1 e*( = 2x) (103)
0 2x

That is the mapping we have to iterate. It is clear that € = O is a stable fixed point of M. The next, unstable, fixed point is
&— = 0.8604065. So we can conclude that we have a convergent Fer expansion, at least for values of time t , such that

t
i] |A(s)||ds < Ko(t) < 0.8604065. (104)
0

Notice that the bound for the convergence domain provided by this result is smaller than that corresponding to the Magnus
expansion (Theorem 9).
