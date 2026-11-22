---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-049-cayley-transform-methods
section_title: "Cayley-transform methods"
section_number: null
pages: 57-58
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
We have seen in Section 1.2 that, for the J-orthogonal group O,(n), the Cayley transform (23) provides a useful alternative
to the exponential mapping, relating the Lie algebra to the Lie group. This fact is particularly important for numerical
methods where the evaluation of the exponential matrix is the most computation-intensive part of the algorithm.

If the solution of Eq. (223) is written as

1 7 1
Y(t) = (: - 12) (' + 12) Yo (268)
then C(t) € 0;(n) satisfies the equation [135]
1 1
C=A- 5IC. Al - rae t>to,  C(to) =0. (269)

Time-symmetric methods of order 4 and 6 have been obtained, based on the Cayley transform (268), by expanding the
solution of (269) in a recursive manner and constructing quadrature formulae for the multivariate integrals that appear
in the procedure [135-137]. It turns out that efficient Cayley based methods can be built directly from Magnus based
integrators [40]. In particular, we get:

Order 4:

cl4l — gil (: i

1 1
io") = a1 — Flas, 2] — aj} + O(h°), (270)

12
where C!4! = C(h) + O(h?).
208 S. Blanes et al. / Physics Reports 470 (2009) 151-238

Order 6:
1 1
[6] _ oI6) _ [6])2 _ [6])2 = 7
cl = 2 (: pe ) (: 10 2 r)) = C(h) + O(h’). (271)

Three matrix-matrix products are required in addition to the three commutators involved in the computation of 2!°!, fora
total of nine matrix-matrix products per step.
