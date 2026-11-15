---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-041-effective-computations-and-acsv
section_title: "Effective computations and ACSV"
section_number: null
pages: 239-240
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Eﬀective computations and ACSV
In this chapter we revisit the key ACSV concepts introduced in Chapters 6
and 7 — critical points, minimal points, Whitney stratiﬁcations, and polyno-
mial amoebas — through the viewpoint of explicit computation. First, Sec-
tion 8.1 describes techniques for manipulating the solutions of polynomial sys-
tems. Section 8.2 then illustrates how to use these techniques to characterize
the critical points of a rational function by determining an algebraic Whitney
stratiﬁcation, computing a set of polynomial equalities and inequalities for the
critical points on each stratum, and reducing these polynomial equalities into
a convenient form. Our most explicit results hold for minimal critical points,
which are the critical points on the boundary of the domain of convergence of
the series under consideration. Section 8.3 describes how to verify minimal-
ity of critical points, which can be viewed as determining boundary points on
amoeba complements. Finally, Section 8.4 describes additional computations
that must be performed in order to ﬁnd coeﬃcient asymptotics.
Throughout this chapter we ﬁx a ratio F(z) = P(z)/Q(z) of coprime poly-
nomials P and Q and a convergent Laurent expansion F(z) = P
r∈Zd arzr that
holds in the domain of convergence D = Relog−1(B) for a component B of
amoeba(H)c (the most common case occurring when D is the domain of con-
vergence of a power series expansion). We say that a property involving Q is a
generic property if it holds for all choices of Q except those whose coeﬃcients
lie in a proper algebraic set depending only on the degree of Q (this is an al-
gebraic analog of a property holding almost surely). Our goal is to determine
asymptotics of a coeﬃcient sequence ar = [zr]F(z) as r →∞with ˆr varying
in some compact set of directions.
Because the vanishing set of a polynomial is the same as the vanishing set of
any positive integer power of that polynomial, we recall from Chapter 7 that the
square-free part ˜Q of a polynomial Q is the product of its distinct irreducible
factors over the complex numbers.
221
222
Eﬀective computations and ACSV
Exercise 8.1. Show that ˜Q can be computed by dividing Q by the greatest
common divisor of all of its ﬁrst order partial derivatives.
