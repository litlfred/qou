---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-004-112-characterization-and-interpretation-of-the-j
section_title: "Characterization and interpretation of the Jones polynomial"
section_number: 1.1.2
pages: 10-14
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
Problem 1.2 ([188, Problem 2]) Characterize those elements of Z[t;t−1] of
the form VK(t).
Remark [188] The corresponding problem for the Alexander polynomial has
been solved; it is known that a polynomial f(t) 2 Z[t;t−1] is equal to the
Alexander polynomial of some knot K if and only if f(1) = 1 and f(t)=
f(t−1). The formulas VK(1) = 1 and VK (exp 2p−1
3 ) = 1 are obtained by the
skein relation (1). These formulas give weak characterizations of the required
elements.
Remark (X.-S. Lin [262]) The Mahler measure (see [119] for its exposition)
of a polynomial F(x)= aQ
i(x−
i)2C[x] is de
ned by
m(F)=l o gjaj +
X
i
log maxf1;j
ijg =
Z 1
0
logjF(e2p−1)jd:
The Mahler measure can be de
ned also for a Laurent polynomial similarly. Is
it true that m(VK ) > 0 for the Jones polynomial VK of a knot K ,i f K is a
non-trivial knot?
Problem 1.3 Find a 3-dimensional topological interpretation of the Jones
polynomial of links.
Remark The Alexander polynomial has a topological interpretation such as
the characteristic polynomial of H1( ^S3−K;Q) of the in
nite cyclic cover of
the knot complement S3−K ,w h e r eH1( ^S3−K;Q)i sr e g a r d e da saQ[t;t−1]-
module by regarding t as the action of the deck transformation on ^S3−K .
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 383
Remark In the viewpoint of mathematical physics, Witten [403] gave a 3-
dimensional interpretation of the Jones polynomial of a link by a path integral
including a holonomy along the link in the Chern-Simons 
eld theory.
Remark Certain special values of the Jones polynomial have some interpre-
tations. The formulas VL(1) = (−2)#L−1 and VL(exp 2p−1
3 )=1a r es h o w n
by the skein relation (1), where # L denotes the number of components of L.
It is known that jVL(−1)j is equal to the order of H1(M2;L)i fi t so r d e ri s

nite, and 0 otherwise. Here, M2;L denotes the double branched cover of S3
branched alongL. It is shown, in [290], that VL(p−1) = (−
p
2)#L−1(−1)Arf(L)
if Arf(L) exists, and 0 otherwise. It is shown, in [257], that VL(exp
p−1
3 )=
p−1#L−1p−3dimH1(M2;L;Z=3Z) .I f ! is equal to a 2nd, 3rd, 4th, 6th root of
unity, the computation ofVL(!) can be done in polynomial time of the number
of crossings of diagrams of L by the above interpretation of VL(!). Otherwise,
VL(!) does not have such a topological interpretation, in the sense that com-
puting VL(!) of an alternating link L at a given value ! is #P-hard except
for the above mentioned roots of unity (see [183, 399]).
Problem 1.4 (J. Roberts) Why is the Jones polynomial a polynomial?
Remark (J. Roberts) A topological invariant of knots should ideally be de-

ned in an intrinsically 3-dimensional fashion, so that its invariance under
orientation-preserving di
eomorphisms of S3 is built-in. Unfortunately, almost
all of the known constructions of the Jones polynomial (via R-matrices, skein
relations, braid groups or the Kontsevich integral, for example) break the sym-
metry, requiring the introduction of an axis (Morsi
cation of the knot) or plane
of projection (diagram of the knot). I believe that the \perturbative" con-
struction via con
guration space integrals [381], whose output is believed to
be essentially equivalent to the Kontsevich integral, is the only known intrinsic
construction.
In the de
nitions with broken symmetry, it is generally easy to see that the
result is an integral Laurent polynomial in q or q
1
2 . In the perturbative ap-
proach, however, we obtain a formal power series in ~, and although we know
that it ought to be the expansion of an integral Laurent polynomial under the
substitution q =e~ , it seems hard to prove this directly. A related observation
is that the analogues of the Jones polynomial for knots in 3-manifolds other
than S3 are not polynomials, but merely functions from the roots of unity to
algebraic integers. What is the special property of S3 (or perhaps R3 )w h i c h
Geometry &TopologyMonographs, Volume 4 (2002)
384 T. Ohtsuki (Editor)
causes this behaviour, and why does the variable q seem natural only when one
breaks the symmetry?
The typical raison d’etre of a Laurent polynomial is that it is a character of the
circle. (In highbrow terms this is an example of \categori
cation", but it is also
belongs to a concrete tradition in combinatorics that to prove that something
is a non-negative integer one should show that it is the dimension of a vector
space.) The idea that the Jones polynomial is related to K -theory [402] and
that it ought to be the S1 -equivariant index of some elliptic operator de
ned
using the special geometry of R3 or S3 is something Simon Willerton and I
have been pondering for some time. As for the meaning of q, Atiyah suggested
the example in equivariant K -theory
KSO(3)(S2)=KS1 (pt)= Z[q1];
in to make the 
rst identi
cation requires ac h o i c eo fa x i si nR3 .( T h i s w o u l d
suggest looking for an SO(3)-equivariant S2 -family of operators.)
Problem 1.5 (J. Roberts) Is there a relationship between values of Jones
polynomials at roots of unity and branched cyclic coverings of a knot?
Problem 1.6 (J. Roberts) Is there a relationship between the Jones polyno-
mial of a knot and the counting of points in varieties de
ned over 
nite 
elds?
Remark (J. Roberts) These two problems prolong the \ri
 in the key of q":
the amusing fact that traditional, apparently independent uses of that letter,
denoting the number of elements in a 
nite 
eld, the deformation parameter
q =e~ , the variable in the Poincare series of a space, the variable in the theory
of modular forms, etc. turn out to be related.
The 
rst problem addresses a relationship which holds for the Alexander poly-
nomial. For example, the order of the torsion in H1 of the n-fold branched
cyclic cover equals the product of the values of the Alexander polynomial at all
the nth roots of unity. It’s hard not to feel that the variable q has some kind
of meaning as a deck translation, and that the values of the Jones polynomial
at roots of unity should have special meanings.
The second has its roots in Jones’ original formulation of his polynomial using
Hecke algebras. The Hecke algebra Hn(q) is just the Hall algebra of double
cosets of the Borel subgroup inside SL(n;Fq); the famous quadratic relation
2 =(q−1) +q falls naturally out of this. Although the alternative de
nition
of Hn(q) using generators and relations extends to allow q to be any complex
number (and it is then the roots of unity, at which Hn(q) is not semisimple,
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 385
which are the obvious special values), it might be worth considering whether
Jones polynomials at prime powers q =ps have any special properties.
Ideally one could try to 
nd a topological de
nition of the Jones polynomial
(perhaps only at such values) which involves 
nite 
elds. The coloured Jones
polynomials of the unknot are quantum integers, which count the numbers of
points in projective spaces de
ned over 
nite 
elds; might those for arbitrary
knots inS3 count points in other varieties? Instead of counting counting points,
one could consider Poincare polynomials, as the two things are closely related
by the Weil conjectures.
One obvious construction involving 
nite 
elds is to count representations of a
fundamental group into a 
nite group of Lie type, such asSL(n;Fq). V ery much
in this vein, Je
rey Sink [369] associated to a knot a zeta-function formed from
the counts of representations into SL(2;Fps ), for 
xed p and varying s.H i s
hope, motivated by the Weil conjectures, was the idea that the SU (2) Casson
invariant might be related to such counting. For such an idea to work, it is
probably necessary to 
nd some way of counting representations with signs, or
at least to enhance the counting in some way. Perhaps the kind of twisting used
in the Dijkgraaf-Witten theory [108] could be used.
Problem 1.7 (J. Roberts) De
ne the Jones polynomial intrinsically using
homology of local systems.
Remark (J. Roberts) The Alexander polynomial of a knot can be de
ned
using the twisted homology of the complement. In the case of the Jones poly-
nomial, no similar direct construction is known, but the approach of Bigelow
[55] is tantalising. He shows how to construct a representation of the braid
group B2n on the twisted homology of the con
guration space of n points in
the 2n-punctured disc, and how to use a certain \matrix element" of this rep-
resentation to obtain the Jones polynomial of a knot presented as a plait. Is
there any way to write the same calculation directly in terms of con
guration
spaces of n points in the knot complement, for example?
Problem 1.8 (J. Roberts) Study the relation between the Jones polynomial
and Gromov-Witten theory.
Remark (J. Roberts) The theory of pseudo-holomorphic curves or \Gromov-
Witten invariants" has been growing steadily since around 1985, in parallel
with the theory of quantum invariants in three dimensional topology. During
Geometry &TopologyMonographs, Volume 4 (2002)
386 T. Ohtsuki (Editor)
that time it has come to absorb large parts of modern geometry and topol-
ogy, including symplectic topology, Donaldson/Seiberg-Witten theory, Floer
homology, enumerative algebraic geometry, etc. It is remarkable that three-
dimensional TQFT has remained isolated from it for so long, but 
nally there
is a connection, as explained in the paper by Vafa and Gopakumar [149] (though
pre
gured by Witten [404]), and now under investigation by many geometers.
The basic idea is that the HOMFLY polynomial can be reformulated as a gen-
erating function counting pseudo-holomorphic curves in a certain Calabi-Yau
manifold, with boundary condition a Lagrangian submanifold associated to the
knot. (This is the one place where the HOMFLY and not the Jones polynomial
is essential!) The importance of this connection can hardly be overestimated, as
it should allow the exchange of powerful techniques between the two subjects.
1 2 3
-1.5
-1
-0.5
0.5
1
1.5
1 2 3
-1.5
-1
-0.5
0.5
1
1.5
-2 -1 1 2 3
-1.5
-1
-0.5
0.5
1
1.5
Figure 2: The upper pictures show the distribution of zeros of the Jones polynomial for
alternating knots of 11 and 12 crossings [262]. The lower picture shows the distribution
of zeros of the Jones polynomial for 12 crossing non-alternating knots [262]. See [262]
for further pictures for alternating knots with 10 and 13 crossings.
