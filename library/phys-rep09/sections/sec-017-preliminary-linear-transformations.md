---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-017-preliminary-linear-transformations
section_title: "Preliminary linear transformations"
section_number: null
pages: 22-23
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
To improve the accuracy and the bounds on the convergence domain of the Magnus series for a given problem, it is quite
common to first consider a linear transformation on the system in such a way that the resulting differential equation can be
more easily handled in a certain sense, to be specified for each problem. To illustrate the procedure, let us consider a simple
example.

Example. Suppose we have the 2 x 2 matrix
A(t) = a(t)X1 + B(t)X2, (84)

where X;, and X; are given by (76) and @ and # are complex functions of time, a, 8 : R —> C. Then the exact solution of
Y’ =A(t)Y, Y(0) = Lis

t
Jf a(s)ds ds, els: %(s2)482 ~ fg! a(s2)ds2
e isyerel syye
V(t) = , B(s1) ; (85)
0 en Jo a(sids

Let us factorize the solution as Y(t) = Yo(t)Y1 (t), with Yo(t) the solution of the initial value problem defined by

% = Ao(t)¥o — An(t) = a(t)X = (0 20) (86)

and Yo (0) = I. Then, the equation satisfied by Y, is

~ ~ ~ ~ 2 [fb a(s)ds
=A (OK, with; = ¥oA¥o — Ao = (° pipers ). (87)

so that the first term of the Magnus expansion applied to (87) already provides the exact solution (85). O

This, of course, is not the typical behavior, but in any case, if the transformation Yo in the factorization Y(t) = Yo(t)Y1 (t)
is chosen appropriately, the first few terms in the Magnus series applied to the equation satisfied by Y; usually give very
accurate approximations.

Since this kind of preliminary transformation is frequently used in Quantum Mechanics, we specialize the treatment to
this particular setting here, and consider Eq. (4) instead. In other words, we write (30) in the more conventional form of the
time dependent Schédinger equation

VO ~ Aue, (88)
dt
where H = H/(ih), h is the reduced Planck constant, H is the Hamiltonian and U corresponds to the evolution operator.

As in the example, suppose that H can be split into two pieces, H= Ho + eH, with Ho a solvable Hamiltonian and
€ < 1asmall perturbation parameter. In such a situation, one tries to integrate out the Ay piece so as to circumscribe
the approximation to the Ay piece. In the case of Eq. (88), this is carried out by means of a linear time-dependent
transformation. In Quantum Mechanics, this preliminary linear transformation corresponds to a new evolution picture, such
as the interaction or the adiabatic picture.

Among other possibilities, we may factorize the time-evolution operator as

U(t) = G(t)Ug(t)G*(0), (89)

where G(t) is a linear transformation whose purpose is yet to be defined. In the new G-Picture, the corresponding time-
evolution operator Uc obeys the equation

Ug(t) =He(t)Uc(t), Ag (t) = GI (A (HGct) — Gh(Ne'(t). (90)

The choice of G depends on the nature of the problem at hand. There is no generic formal recipe to find out the
most appropriate G. In the spirit of canonical transformations of Classical Mechanics, one should build up the very Uc
S. Blanes et al. / Physics Reports 470 (2009) 151-238 173

perturbatively. However, the aim here is different because G is defined from the beginning. Two rather common choices
are:

e Interaction picture. It is well suited when Ao(t) is diagonal in some basis, or else, it is constant. In that case

G(t) = exp (/ fo(rydr) (91)
0

so that

t t
He(t) = ¢ exp (-/ fin(e)tr) y(t) exp (/ fi(e)tr) . (92)
0 0

e Adiabatic picture. A time scale of the system, much smaller than that of the interaction, defines an adiabatic regime.
For instance, suppose that the Hamiltonian operator H(t) depends smoothly on time through the variable t = t/T,
where T determines the time scale and T > oo. Then the quantum mechanical evolution of the system is described by
dU/dt = H(et)U, with e = 1/T < 1, or equivalently

aU(z) _ 1,
= —H(r)U(t), (93)

dt eg
with t = et. In this case the appropriate transformation is a G that renders H(t) instantaneously diagonal, i.e.,

Gi(t)H()G(t) = E(t) = diag[E(t), Ep(t), ...]. (94)

The term G'G’ of the new Hamiltonian in (90) is, under adiabatic conditions, very small. Its main diagonal generates the
so-called Berry, or geometric, phase [82].

Both types of G do not exclude mutually, but they may be used in succession. As a matter of fact, corrections to the
adiabatic approximation must be followed by the former one. In turn, an adiabatic transformation may be iterated, as
proposed by Garrido [83] and Berry [84].

In Section 4 we shall extensively use these preliminary linear transformations on several standard problems of Quantum
Mechanics to illustrate the practical features of the Magnus expansion.
