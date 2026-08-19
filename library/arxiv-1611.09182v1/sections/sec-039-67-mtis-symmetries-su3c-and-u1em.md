---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-039-67-mtis-symmetries-su3c-and-u1em
section_title: "MTIS symmetries: su(3)c and u(1)em"
section_number: 6.7
pages: 57-58
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
Having obtained these minimal left ideals, we would now like to know how they transform,
so as to justify the labels we gave to their coeﬃcients in equations (6.19) and (6.21). Up
until now, however, we have not speciﬁed under which groups these spinors transform.
A popular choice in the literature for this symmetry group is take the Cliﬀord algebra’s
spin group. For example, the well-known “SO(10)” grand uniﬁed theory is built from the
Spin(10) group acting on 16-dimensional spinors. (Here, spinors are deﬁned as irreducible
representations of Spin(10).) We point out, though, that Spin(10) is a 45-dimensional
group, meaning that 33 generators will need to be explained away in order to arrive ﬁnally
atSU (3)c×SU (2)L×U(1)Y. Could there (alternately, or additionally) be another type of
symmetry, which leads directly toSU (3)c×SU (2)L×U(1)Y? Or to the surviving unbroken
symmetries, SU (3)c×U(1)em?
We would now like to point out some symmetries in the construction of our minimal
left ideals. These symmetries will be called unitary MTIS symmetries, or simply MTIS
symmetries. (Readers may wish to refer back to Section 4.5.1, where maximal totally
isotropic subspaces were ﬁrst deﬁned.) We propose here to consider MTIS symmetries
when building covariant derivatives in gauge theories.
In the case of complex Cliﬀord algebras, Cl(n), with even n, the generating space can
always be partitioned into two maximal totally isotropic subspaces, [1], each of dimension
n/2. For Cl(6) which we have here, the generating space spanned by{ie1,ie 2,...ie 6} is par-
49
titioned into an MTIS spanned by{α1,α 2,α 3}, and another MTIS spanned by{α†
1,α†
2,α†
3}.
Loosely speaking, MTIS symmetries will preserve this structure.
Unitary MTIS symmetries. We are interested in operator transformations of the
formeiφkgk ieje−iφkgk, whereφk∈ R andgk∈ C⊗← −O. Already, with this constraint, we ﬁnd
that the anti-commutation relations of equations (6.12), (6.13), and (6.14) are preserved.
Furthermore, as the name indicates, we will restrict our attention to those transformations
under which each MTIS is closed. That is, to ﬁrst order, theαi rotate only into themselves,
and the α†
i rotate only into themselves,
[ gk,
∑
i
biαi ] =
∑
j
cjαj [ gk,
∑
i
b′
iαi
† ] =
∑
j
c′
jαj
†, (6.22)
for some complex coeﬃcients, cj,c′
j. Here, bi,b′
i are some given complex coeﬃcients, and
gk is a generator of the MTIS symmetry.
Finally, we demand that the group transformation on αj commute with hermitian
conjugation,†,
eiφkgk α†
je−iφkgk =
(
e−iφkgk
)†
α†
j
(
eiφkgk
)†
. (6.23)
Under these conditions, in the case of Cl(6), our unitary MTIS symmetries are then
found to be generated uniquely by su(3) and u(1). Explicitly, the SU (3) generators are
given by the Λ i of equation (6.5), and the U(1) generator is found to be given by Q of
equation (6.3).
