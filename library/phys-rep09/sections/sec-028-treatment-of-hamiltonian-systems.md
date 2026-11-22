---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-028-treatment-of-hamiltonian-systems
section_title: "Treatment of Hamiltonian systems"
section_number: null
pages: 35-36
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
We have seen how the algebraic setting we have developed for linear systems of differential equations may be extended
formally to nonlinear systems. We will next review how it can be adapted to the important class of Hamiltonian systems. In
this context, the role of a Lie bracket of vector fields (156) is played by the classical Poisson bracket [113].

The Lie algebraic presentation of Hamiltonian systems in Classical Mechanics has been approached in different ways, and
the Magnus expansion invoked in this context by diverse authors [114-116]. More explicit use of the Magnus expansion is
done in [109] where the evolution operator for a classical system is constructed and its differential equation analyzed.

To particularize to this situation the preceding general treatment, let us consider a system with | degrees of freedom
and phase space variables x = (q, p) = (q1,.--, 41, Pi, ---, Pi), where (qi, pi), i= 1,..., | are the usual pairs of canonical
conjugate coordinate and momentum, respectively. By defining the Poisson bracket of two scalar functions F(q, p) and
G(q, p) of phase space variables in the conventional way [113]

!\(9F 0G OF OG
Fa =o( sae ase ).

<i \0qi Opi Op; Gi
186 S. Blanes et al. / Physics Reports 470 (2009) 151-238

we have
2
oF aG
F,G}= —Jji—.,
{F, G} » ax Ox,
ij=1
and in particular
{xi, Xj} = Jij-

Here J is the basic symplectic matrix appearing in Eq. (20) (with n = 1). With these definitions, the set of (sufficiently
smooth) functions on phase space acquires the structure of a Lie algebra and we can associate with any such function F(x)
a Lie operator

21

=)> oF, 8 (166)

is
= Ox; OX;

which acts on the same set of functions as LrG = {F, G}. It is then a simple exercise to show that the set of all Lie operators
is also a Lie algebra under the usual commutator [Lr, L¢] = LpL¢ — Lol and furthermore

[Lr, Le] = Lyr,c}-

Given the Hamiltonian function H(q, p, t) : R27! x R — R, where q, p € R', the equations of motion are

qd = V>H, p’ = —VqH, (167)
or, equivalently, in terms of x,
x =JV,xH.
It is then elementary to show that the Lie operator L_y is nothing but the Lie derivative Lr (152) associated with the function
f=] V,H.
Therefore, the operational equation (160) becomes
So: = OL =
ae! HE-Hyy,t)s Y= Xo (168)

and the previous treatment also holds in this setting. As a result, the Magnus expansion reads
}, = exp(Lw), (169)

where W = )°;°, W; and the first two terms are
c
Wi (Xo) = -| H (Xo, s)ds (170)
0

it Sy
W(X) = ->/ as, [ ds2{H (Xo, 51), H(Xo, S2)}-
0 0
