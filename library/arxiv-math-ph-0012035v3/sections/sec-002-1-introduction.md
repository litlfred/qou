---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
For tens years the (standard, i.e. Abelian) Stokes theorem is one of the central
points of (multivariable) analysis on manifolds. Lower-dimensional ve rsions of
this theorem, known as the (proper) Stokes theorem, in dimensions 1 and 2, and
the, so-called Gauss theorem, in dimensions 2 and 3, respectively, are well-known
and extremally useful in practice, e.g. in classical electrodynamics ( Maxwell
equations). In fact, it is diﬃcult, if not impossible, to imagine lectures on
classical electrodynamics without intensive use of the Stokes theo rem. The
standard Stokes theorem is also being called the Abelian Stokes theorem, as it
applies to (ordinary, i.e. Abelian) diﬀerential forms. Classical electr odynamics
is an Abelian (i.e. U(1)) gauge ﬁeld theory (gauge ﬁelds are Abelian forms),
therefore its integral formulas are governed by the Abelian Stokes theorem. But
much of interesting and physically important phenomena is described by non-
Abelian gauge theories. Hence it would be very desirable to have at our disposal
a non-Abelian version of the Stokes theorem. Since non-Abelian diﬀe rential
1e-mail: bobroda@krysia.uni.lodz.pl
1
forms need a bit diﬀerent treatment, one is forced to use a more so phisticated
formalism to deal with this new situation.
The aim of this chapter is to present a short review of the non-Abelia n
Stokes theorem. At ﬁrst, we will give an account of diﬀerent formulations of the
non-Abelian Stokes theorem and next of various applications of the reof.
1.1 Abelian Stokes theorem
Before we engage in the non-Abelian Stokes theorem it seems reaso nable to
recall its Abelian version. The (Abelian) Stokes theorem says (see, e.g. [Spi65],
for an excellent introduction to the subject) that we can convert an integral
around a closed curve C bounding some surface S into an integral deﬁned on
this surface. Namely, in e.g. three dimensions
∮
C
⃗A · d⃗ s=
∫
S
curl ⃗A · ⃗ n dσ, (1)
where the curve C is the boundary of the surface S, i.e. C = ∂S (see, Fig.1),
S ✻
∂S = C
Figure 1: Integration areas for the lowest-dimensional (non-triv ial) version of
the Abelian Stokes theorem.
⃗A is a vector ﬁeld, e.g. the vector potential of electromagnetic ﬁeld, and ⃗ nis a
unit outward normal at the area element dσ.
More generally, in any dimension,
∫
∂N
ω =
∫
N
dω, (2)
where now N is a d-dimensional submanifold of the manifold M, ∂N is its
(d − 1)-dimensional boundary, ω is a ( d − 1)-form, and dω is its diﬀerential, a
d-form. We can also rewrite Eq.1 in the spirit of Eq.2, i.e.
∮
∂S =C
Ai dxi = 1
2
∫
S
(∂iAj − ∂jAi) dxi ∧ dxj, (3)
2
where Ai (i = 1, 2, 3) are components of the vector ⃗A, and the Einstein summa-
tion convention after repeating indices is assumed.
In electrodynamics, we deﬁne the stress tensor of electromagne tic ﬁeld
Fij = ∂iAj − ∂jAi,
and the magnetic induction, its dual, as
Bk = 1
2 εijk Fij,
where εijk is the totally antisymmetric (pseudo-)tensor. RHS of Eq.3 represe nts
then the magnetic ﬂux through S. Thus, we can rewrite Eq.3 in the form of 1
∮
∂S =C
Ai dxi = 1
2
∫
S
Fij dxi ∧ dxj (4)
=
∫
S
Bini dσ.
In turn, in geometry ⃗A plays the role of connection (it deﬁnes the parallel
transport around C), and F is the curvature of this connection. A “global
version” of the Abelian Stokes theorem,
exp
(
i
∮
∂S =C
Ai(x) dxi
)
= exp
( i
2
∫
S
Fij(x) dxi ∧ dxj
)
, (5)
which is rather a trivial generalization of Eq.4, is a very good starting point for
our further discussion concerning the non-Abelian Stokes theore m. The object
on LHS of 5 is called the holonomy, and more generally, for open curve s C,
global connection.
