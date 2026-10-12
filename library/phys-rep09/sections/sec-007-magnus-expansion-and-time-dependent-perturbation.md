---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-007-magnus-expansion-and-time-dependent-perturbation
section_title: "Magnus expansion and time-dependent perturbation theory"
section_number: null
pages: 12-14
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
It is not difficult to establish a connection between Magnus series and Dyson perturbative series [13]. The latter gives the
solution of (30) as
Y(t) = I +
∞
X
n=1
Pn(t),
(52)
S. Blanes et al. / Physics Reports 470 (2009) 151–238
163
where Pn are time-ordered products
Pn(t) =
Z t
0
dt1 . . .
Z tn−1
0
dtn A1A2 . . . An,
where Ai ≡A(ti). Then
∞
X
j=1
Ωj(t) = log
 
I +
∞
X
j=1
Pj(t)
!
.
As stated by Salzman [55],
Ωn = Pn −
n
X
j=2
(−1)n
j
R(j)
n ,
n ≥2,
(53)
where
R(k)
n
=
X
Pi1Pi2 . . . Pik
(i1 + · · · + ik = n)
obeys the quadratic recursion formula
R(j)
n =
n−j+1
X
m=1
R(1)
m R(j−1)
n−m ,
(54)
R(1)
n
= Pn,
R(n)
n
= Pn
1.
Eq. (54) represents the Magnus expansion generator in Salzman’s approach. It may be useful to write down the first few
equations provided by this formalism:
Ω1 = P1
Ω2 = P2 −
1
2
P2
1
(55)
Ω3 = P3 −
1
2(P1P2 + P2P1) +
1
3
P3
1.
A similar set of equations was developed by Burum [56], thus providing
P1 = Ω1,
P2 = Ω2 +
1
2!Ω2
1,
(56)
P3 = Ω3 +
1
2!(Ω1Ω2 + Ω2Ω1) +
1
3!Ω3
1
and so on. The general term reads
Ωn = Pn −
n
X
j=2
1
j
Q (j)
n ,
n ≥2,
(57)
where
Q (k)
n
=
X
Ωi1 . . . Ωik,
(i1 + · · · + ik = n).
(58)
As before, subscripts indicate the order with respect to the parameter ε, while superscripts represent the number of factors
in each product. Thus, the summation in (58) extends over all possible products of k (in general non-commuting) operators
Ωi such that the overall order of each term is equal to n. By regrouping terms, one has
Q (k)
n
= Ω1
X
i2+···+ik=n−1
Ωi2 · · · Ωik + Ω2
X
i2+···+ik=n−2
Ωi2 · · · Ωik + · · · + Ωn−k+1
X
i2+···+ik=k−1
Ωi2 · · · Ωik,
(59)
where Q (j)
n
may also be obtained recursively from
Q (j)
n
=
n−j+1
X
m=1
Q (1)
m Q (j−1)
n−m ,
(60)
Q (1)
n
= Ωn,
Q (n)
n
= Ωn
1.
By working out this recurrence, one gets the same expressions as (54) for the first terms. Further aspects of the relationship
between Magnus, Dyson series and time-ordered products can be found in [57,58].
164
S. Blanes et al. / Physics Reports 470 (2009) 151–238
