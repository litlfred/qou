---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-009-graph-theoretical-analysis-of-magnus-expansion
section_title: "Graph theoretical analysis of Magnus expansion"
section_number: null
pages: 14-15
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The previous recursions allow us, in principle, to express any 2; in the Magnus series in terms of 21, ..., 2,—1. In fact,
this procedure has some advantages from a computational point of view. On the other hand, as we have mentioned before,
when the recursions are solved explicitly, 82, can be expanded as a linear combination of terms that are composed from
integrals and commutators acting iteratively on A. The actual expression, however, becomes increasingly complex with k, as
it should be evident from the first terms (42)-(46). An alternative form of the Magnus expansion, amenable also for recursive
derivation by using graphical tools, can be obtained by associating each term in the expansion with a binary rooted tree, an
approach worked out by Iserles and Norsett [37]. For completeness, in the sequel, we show the equivalence of the recurrence
(49)-(50) with this graph theoretical approach.

In essence, the idea of Iserles and Norsett is to associate each term in 2, with a rooted tree, according to the following
prescription.

Let J be the set consisting of the single rooted tree with one vertex, then Jo = { ©}, establish the relationship between
this tree and A through the map

e@ ~ A(t)
and define recursively

at
m= |\ 8 TE Ty, t € Ty kit ky =m—1

Next, given two expansion terms H,, and H,,, which have been associated previously with t; € J, and tz € Jj,, respectively
(ky + ky =m — 1), we associate

™%
7)

t
no =| [ Hy @)de, Ha with =\/7
0

Thus, each H; for t € Tm involves exactly m integrals and m commutators.

These composition rules establish a one-to-one relationship between a rooted tree tT € T = Um=>o Tm, and a matrix
function H, (t) involving A, multivariate integrals and commutators.

From here it is easy to deduce that every tT € Tm, m > 1, can be written in a unique way as

Ts

T3
T2

qT%
T=
Or T = a(t}, T2, ..., Ts). Then the Magnus expansion can be expressed in the form [37,59]
oO t
20=yVy ae) [ H, (é)dé, (61)
0

m=0 TETin

with the scalar a( © ) = 1 and, in general,
s

Bs
a(t) = 7 Il a(t).

* [=1
Let us illustrate this procedure by writing down, explicitly, the first terms in the expansion in a tree formalism. In 7; we
only have k; = kp = 0, so that a single tree is possible,

™W=°, H=°e, => mo

with w(t) = —1/2. In J, there are two possibilities, namely k; = 0, kz = 1 and k; = 1, kp = O, and thus one gets

WS °, ws > T= ; a(t) =
cal J‘ m=e > T= a(t) =

Sl-

rie
S. Blanes et al. / Physics Reports 470 (2009) 151-238 165

and the process can be repeated for any J. The correspondence between trees and expansion terms should be clear from
the previous graphs. For instance, the last tree is nothing but the integral of A, commuted with A, integrated and commuted
with A. In that way, by truncating the expansion (61) at m = 2 we have

wer ae .

i.e., the explicit expressions collected in Section 2.2.
Finally, the relationship between the tree formalism and the recurrence (49)-(50) can be established as follows. From
(61) we can write

> Yo a(t) H(t) = ar 2 & (Ty) +++ (3) Hates...)

m=1 TET

ky te we

Thus, by comparing (50) and (61) we have

Qn (t) = Yew f ieee = 11 A [seas

TETm—1

so that

SP= Yo YS ay) 0G) Hace...)

Kiyookj HTK;
ky te +ky=m—1-j

In other words, each term 5? in the recurrence (49) carries on a complete set of binary trees. Although both procedures are
equivalent, the use of (49) and (50) can be particularly well suited when high orders of the expansion are considered, for
two reasons: (i) the enormous number of trees involved for large values of m and (ii) in (61) many terms are redundant, and
a careful graph theoretical analysis is needed to deduce which terms have to be discarded [37].

Recently, an ME-type formalism has been developed in the more abstract setting of dendriform algebras. This generalized
expansion incorporates the usual one as a limit, but is formulated more in line with (non-commutative) Butcher series. In
this context, the use of planar rooted trees to represent the expansion and the so-called pre-Lie product, allows one to reduce
the number of terms at each order in comparison with expression (61) [60].
