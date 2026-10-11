---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-015-preliminary-linear-transformations
section_title: "Preliminary linear transformations"
section_number: null
pages: 22-23
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
To improve the accuracy and the bounds on the convergence domain of the Magnus series for a given problem, it is quite
common to first consider a linear transformation on the system in such a way that the resulting differential equation can be
more easily handled in a certain sense, to be specified for each problem. To illustrate the procedure, let us consider a simple
example.
Example. Suppose we have the 2 × 2 matrix
A(t) = α(t)X1 + β(t)X2,
(84)
where X1 and X2 are given by (76) and α and β are complex functions of time, α, β : R −→C. Then the exact solution of
Y ′ = A(t)Y, Y(0) = I is
Y(t) =

e
R t
0 α(s)ds
Z t
0
ds1e
R t
s1 α(s2)ds2 β(s1) e−
R s1
0
α(s2)ds2
0
e−
R t
0 α(s)ds

.
(85)
Let us factorize the solution as Y(t) = ˜Y0(t)˜Y1(t), with ˜Y0(t) the solution of the initial value problem defined by
˜Y ′
0 = A0(t)˜Y0
A0(t) = α(t)X1 =

α(t)
0
0
−α(t)

(86)
and ˜Y0(0) = I. Then, the equation satisfied by ˜Y1 is
˜Y ′
1 = A1(t)˜Y1,
with A1 = ˜Y −1
0
A ˜Y0 −A0 =

0
β(t)e2
R t
0 α(s)ds
0
0

,
(87)
so that the first term of the Magnus expansion applied to (87) already provides the exact solution (85).
□
This, of course, is not the typical behavior, but in any case, if the transformation ˜Y0 in the factorization Y(t) = ˜Y0(t)˜Y1(t)
is chosen appropriately, the first few terms in the Magnus series applied to the equation satisfied by ˜Y1 usually give very
accurate approximations.
Since this kind of preliminary transformation is frequently used in Quantum Mechanics, we specialize the treatment to
this particular setting here, and consider Eq. (4) instead. In other words, we write (30) in the more conventional form of the
time dependent Schödinger equation
dU(t)
dt
= ˜H(t)U(t),
(88)
where ˜H ≡H/(i¯h), ¯h is the reduced Planck constant, H is the Hamiltonian and U corresponds to the evolution operator.
As in the example, suppose that ˜H can be split into two pieces, ˜H = ˜H0 + ε ˜H1, with ˜H0 a solvable Hamiltonian and
ε ≪1 a small perturbation parameter. In such a situation, one tries to integrate out the ˜H0 piece so as to circumscribe
the approximation to the ˜H1 piece. In the case of Eq. (88), this is carried out by means of a linear time-dependent
transformation. In Quantum Mechanics, this preliminary linear transformation corresponds to a new evolution picture, such
as the interaction or the adiabatic picture.
Among other possibilities, we may factorize the time-evolution operator as
U(t) = G(t)UG(t)GĎ(0),
(89)
where G(t) is a linear transformation whose purpose is yet to be defined. In the new G-Picture, the corresponding time-
evolution operator UG obeys the equation
U′
G(t) = ˜HG(t)UG(t),
˜HG(t) = GĎ(t) ˜H(t)G(t) −GĎ(t)G′(t).
(90)
The choice of G depends on the nature of the problem at hand. There is no generic formal recipe to find out the
most appropriate G. In the spirit of canonical transformations of Classical Mechanics, one should build up the very UG
S. Blanes et al. / Physics Reports 470 (2009) 151–238
173
perturbatively. However, the aim here is different because G is defined from the beginning. Two rather common choices
are:
• Interaction picture. It is well suited when ˜H0(t) is diagonal in some basis, or else, it is constant. In that case
G(t) = exp
Z t
0
˜H0(τ)dτ

(91)
so that
˜HG(t) = ε exp

−
Z t
0
˜H0(τ)dτ

˜H1(t) exp
Z t
0
˜H0(τ)dτ

.
(92)
• Adiabatic picture. A time scale of the system, much smaller than that of the interaction, defines an adiabatic regime.
For instance, suppose that the Hamiltonian operator H(t) depends smoothly on time through the variable τ = t/T,
where T determines the time scale and T →∞. Then the quantum mechanical evolution of the system is described by
dU/dt = ˜H(εt)U, with ε ≡1/T ≪1, or equivalently
dU(τ)
dτ
=
1
ε
˜H(τ)U(τ),
(93)
with τ ≡εt. In this case the appropriate transformation is a G that renders ˜H(t) instantaneously diagonal, i.e.,
GĎ(t) ˜H(t)G(t) = E(t) = diag[E1(t), E2(t), . . .].
(94)
The term GĎG′ of the new Hamiltonian in (90) is, under adiabatic conditions, very small. Its main diagonal generates the
so-called Berry, or geometric, phase [82].
Both types of G do not exclude mutually, but they may be used in succession. As a matter of fact, corrections to the
adiabatic approximation must be followed by the former one. In turn, an adiabatic transformation may be iterated, as
proposed by Garrido [83] and Berry [84].
In Section 4 we shall extensively use these preliminary linear transformations on several standard problems of Quantum
Mechanics to illustrate the practical features of the Magnus expansion.
