---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
arXiv:math/0102098v1  [math.GT]  13 Feb 2001
Skein theory and the Murphy operators
HUGH R. MORTON
Department of Mathematical Sciences, University of Liverpool,
Peach St, Liverpool, L69 7ZL, England.
morton@liv.ac.uk
Abstract
The Murphy operators in the Hecke algebra Hn of type A are ex-
plicit commuting elements whose sum generates the centre. They can
be represented by simple tangles in the Homﬂy skein theory version
of Hn. In this paper I present a single tangle which represents their
sum, and which is obviously central. As a consequence it is possible
to identify a natural basis for the Homﬂy skein of the annulus, C.
Symmetric functions of the Murphy operators are also central in
Hn. I deﬁne geometrically a homomorphism from C to the centre of
each algebra Hn, and ﬁnd an element in C, independent of n, whose
image is the mth power sum of the Murphy operators. Generating
function techniques are used to describe images of other elements of
C in terms of the Murphy operators, and to demonstrate relations
among other natural skein elements.
Keywords: skein theory; Murphy operators; power sums; symmetric
functions; annulus; Hecke algebras.
Introduction.
The Hecke algebra Hn of type A is a deformed version of the group algebra
C[Sn] of the symmetric group. It has a simple skein theory model in terms
of n-tangles and the Homﬂy skein relations.
Certain sums of transpositions,
m(j) =
j−1
X
i=1
(i j) ∈C[Sn], j = 2, . . . , n,
known as Jucys-Murphy elements, appeared in the work of Jucys [7] in 1974,
and later in work of Murphy [14]. These elements all commute, and every
1
symmetric polynomial in them can be shown to lie in the centre of the algebra
C[Sn]. For example m(2) = (1 2), m(3) = (1 3) + (2 3) and
m(2)m(3) = (1 3 2) + (1 2 3) = m(3)m(2).
Dipper and James [4] used a simple deformation of the transpositions
to deﬁne analogous elements M(j) ∈Hn, which they called the Murphy
operators. These elements again all commute, and symmetric polynomials
in them belong to the centre of Hn.
Dipper and James showed that for
generic values of the deformation parameter these account for the whole of
the centre. Katriel, Abdessalam and Chakrabarti [8] noted that in fact any
central element can be expressed as a polynomial in just the sum M =
Pn
j=2 M(j) of the Murphy operators. This is a stronger result than for the
non-deformed algebra C[Sn], although the centre has the same dimension in
each case, given by π(n), the number of partitions of n.
In this paper I present a skein theory version of the Murphy operators and
their sum, ﬁnishing with an elegant representation of their power sums and
other symmetric polynomials. Starting in section 2 with a choice of n-string
braids corresponding to the transpositions I exhibit a braid T(j) representing
each of the individual Murphy operators M(j), following Ram [15], and then
a very natural simple n-tangle T (n) which represents their sum M, up to a
linear combination with the identity element in Hn in each case. From the
tangle viewpoint it becomes immediately clear that M is central.
The Homﬂy skein of the annulus, C, has been exploited for many years, for
example in the work of Jun Murakami, and myself and Short, in constructing
and analysing Homﬂy-based invariants by the use of satellites. These invari-
ants cover the same ground as the quantum sl(N) invariants for all choices
of module and have been developed variously in algebraic and skein theoretic
ways, for example by Wenzl [17], Aiston and myself [13] and Blanchet [3].
In section 3 I show how the tangle view of the Murphy operators gives a
direct means for identifying the best linear basis for C when studying these
quantum invariants and establishing its multiplicative properties.
I then
introduce a rather overlooked homomorphism from C to the centre of Hn.
Using generating function methods I show how to realise other symmetric
functions of the Murphy operators as images of explicit elements of C. The
principal result is the identiﬁcation of an element Pm ∈C, independent of n,
whose image determines the mth power sum of the Murphy operators in Hn.
Section 4 gives the ﬁnal details of the results of section 3, based on a
2
further underused skein, A, whose unexpected algebraic properties allow for
some satisfyingly clean proofs.
