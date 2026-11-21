---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-006-21-q--holonomicity-in-many-variables
section_title: "q--holonomicity in many variables"
section_number: 2.1
pages: 6-8
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
We brieﬂy review here the deﬁnition of q–holonomicity. First of all, we need an
r–dimensional version of the q–Weyl algebra. Consider the operators Ei and
Qj for 1 ≤i, j ≤r which act on discrete functions f : Nr −→Z[q±] by:
(Qif)(n1, . . . , nr)
=
qnif(n1, . . . , nr)
(Eif)(n1, . . . , nr)
=
f(n1, . . . , ni−1, ni + 1, ni+1, . . . , nr).
It is easy to see that the following relations hold:
QiQj = QjQi
EiEj = EjEi
QiEj = EjQi for i̸ = j
EiQi = qQiEi
(Relq)
We deﬁne the q–Weyl algebra Ar to be a noncommutative algebra with pre-
sentation
Ar = Z[q±1]⟨Q1, . . . , Qr, E1, . . . , Er⟩
(Relq)
.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1259
Given a discrete function f with domain Nr or Zr and target space a Z[q±1]–
module, one can deﬁne the left ideal If in Ar by
If := {P ∈Ar|Pf = 0}.
If we want to determine a function f by a ﬁnite list of initial conditions, it does
not suﬃce to ensure that f satisﬁes one nontrivial recursion relation if r ≥2.
The key notion that we need instead is q–holonomicity.
Intuitively, a discrete function f : Nr −→Z[q±] is q–holonomic if it satisﬁes
a maximally overdetermined system of linear diﬀerence equations with polyno-
mial coeﬃcients. The exact deﬁnition of holonomicity is through homological
dimension, as follows.
Suppose M = Ar/I , where I is a left Ar–module. Let Fm be the sub-space of
Ar spanned by polynomials in Qi, Ei of total degree ≤m. Then the module
Ar/I can be approximated by the sequence Fm/(Fm ∩I), m = 1, 2, ....
It
turns out that, for m >> 1, the dimension (over the fractional ﬁeld Q(q)) of
Fm/(Fm ∩I) is a polynomial in m whose degree d(M) is called the homological
dimension of M .
Bernstein’s famous inequality (proved by Sabbah in the q–case, [31]) states
that d(M) ≥r, if M̸ = 0 and M has no monomial torsions, ie, any non-trivial
element of M cannot be annihilated by a monomial in Qi, Ei. Note that the
left Ar–module Mf := Ar · f ∼= Ar/If does not have monomial torsion.
Deﬁnition 2.1 We say that a discrete function f is q–holonomic if d(Mf) ≤r.
Note that if d(Mf) ≤r, then by Bernstein’s inequality, either Mf = 0 or
d(Mf) = r. The former can happen only if f = 0.
Although we will not use in this paper, let us point out an alternative cohomo-
logical deﬁnition of dimension for a ﬁnitely generated Ar module M . Let us
deﬁne
c(M) := min{j ∈N | Extj
Ar(M, Ar)̸ = 0}.
Then the homological dimension d(M) := 2r −c(M) equals to the dimension
d(M) deﬁned above.
Closely related to Ar is the q–torus algebra Tr with presentation
Tr = Z[q±1]⟨Q±1
1 , . . . , Q±1
r , E±1
1 , . . . , E±1
r ⟩
(Relq)
.
Elements of Tr acts on the set of functions with domain Zr, but not on the set
of functions with domain Nr. Note that Tr is simple, but Ar is not. If I is a
left ideal of Tr then the dimension of Tr/I is equal to that of Ar/(I ∩Ar).
Geometry & Topology, Volume 9 (2005)
1260
Stavros Garoufalidis and Thang T Q Lˆe
2.2
