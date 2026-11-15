---
doc_id: arxiv-math-9805023v1
doc_title: "q-Laguerre polynomials and big q-Bessel functions and their orthogonality relations"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-3
source_pdf: 9805023v1.pdf
source_sha256: ea8758b2a2bf9d85
toc_source: inferred
doc_brief: "q-Laguerre polynomials and big q-Bessel functions and their orthogonality relations — The q-Laguerre polynomials correspond to an indetermined moment problem."
---
This paper answers two seemingly diﬀerent questions, which both originated from
quantum groups. First, consider the system of Moak’s [21] q-Laguerre polynomials with
respect to their familiar discrete orthogonality measure, and extend this in an explicit
way to a complete orthogonal system of eigenfunctions of a doubly inﬁnite Jacobi matrix
originating from analysis on SUq(1, 1), the quantum SU(1, 1) group. Second, obtain or-
thogonality relations and dual orthogonality relations for certain (big) q-Bessel functions
originating (see [4]) on Eq(2), the quantum group of plane motions, and give rigorous
proofs of these orthogonalities. The two questions are related because the dual orthogo-
nality relations for the big q-Bessel functions turn out to be the orthogonality relations for
the completed q-Laguerre polynomials.
It is well known that the moment problem corresponding to Moak’s q-Laguerre poly-
nomials is indetermined as a Stieltjes moment problem. Moak [21, Thm. 1, 2] gives several
orthogonality measures for the q-Laguerre polynomials: an absolutely continuous measure
on [0, ∞) and purely discrete measures supported on the set {cqk | k ∈Z} for any constant
c > 0, see §4 for the explicit weights. See also Ismail and Rahman [10] for the explicit
calculation of the entire functions in the Nevanlinna parametrisation of the orthogonality
measures for the moment problem for the q-Laguerre polynomials. We are interested in
the discrete orthogonality measures. From the general theory of orthogonal polynomials
it follows that the polynomials are not dense in the corresponding space of quadratically
1991 Mathematics Subject Classiﬁcation. 33D45, 33D80.
Key words and phrases. orthogonal polynomials, indetermined moment problem, non-extremal mea-
sures, q-Bessel functions , SU(1, 1) and E(2) quantum groups.
First author partly supported by C.N.R. - G.N.S.A.G.A. Second author supported by the Netherlands
Organization for Scientiﬁc Research (NWO) under project number 610.06.100.
1
integrable functions, since the support is not the set of zeros of an entire function. This
is expressed by saying that the measure is not N-extremal, see [1] for more information
on moment problems and orthogonal polynomials. In this paper we complement the q-
Laguerre polynomials to an orthogonal basis of the L2-space for the discrete measure by
using a certain q-analogue of the Bessel function of order α. The dual basis functions can
be recognized as big q-Bessel functions, see below.
q-Analogues of Bessel functions exist in several sorts. Most well-known and probably
the oldest ones are Jackson’s ﬁrst and second q-Bessel functions, see Ismail [8]. They occur
in many places, including the present paper, but they have the draw-back that they do not
form an orthogonal system (possibly they form a biorthogonal system). Other q-analogues
of Bessel functions can be obtained as formal limit cases of the three q-analogues of Jacobi
polynomials, i.e., of little q-Jacobi polynomials, big q-Jacobi polynomials and Askey-Wilson
polynomials. For this reason we propose to speak about little q-Bessel functions, big q-
Bessel functions and AW type q-Bessel functions for the corresponding limit cases. Little,
big and AW type q-Bessel functions have interpretations on Eq(2), completely analogous to
the interpretations of little and big q-Jacobi polynomials and Askey-Wilson polynomials on
SUq(2), the quantum SU(2) group, see Vaksman and Korogodski˘ı [23], Koelink [14], [15],
Bonechi et al. [4]. See also Ismail et al. [9] for the Fourier-Bessel transform for the AW
type q-Bessel function. The duals of the AW-type q-Bessel functions can also be viewed
as the little q-Jacobi functions, which live on SUq(1, 1), see Masuda et al. [20]. These
three types of q-Bessel functions satisfy orthogonality relations which can be obtained as
formal limits of the corresponding orthogonality relations for q-Jacobi polynomials. In
the q-Bessel case it is not suﬃcient to give orthogonality relations, but one also has to
prove completeness, either directly or by giving dual orthogonality relations. For rigorous
proofs of orthogonality and completeness we mention three diﬀerent techniques: (i) spectral
theoretic methods, (ii) direct proofs by use of generating functions, (iii) rigorous limit
transitions from the orthogonal polynomials case. Usually, only the ﬁrst method yields
both orthogonality and completeness.
The second method was used for little q-Bessel
functions by Koornwinder and Swarttouw [18], and was suﬃcient there because of self-
duality. The ﬁrst method was used for little q-Jacobi functions by Kakehi, Masuda and
Ueno [11], [12]. In the present paper we give two diﬀerent proofs, ﬁrst by the spectral
method, and next by method (ii) for the extension of the q-Laguerre orthogonality and by
method (iii) for the big q-Bessel orthogonality.
The spectral method, developed in sections 2 and 3, is based on the spectral analysis
of a doubly inﬁnite Jacobi matrix, see e.g. Masson and Repka [19]. This operator arises in
a natural way from SUq(1, 1). The spectral analysis is very similar to the spectral analysis
for second order diﬀerential equations (see [6]), such as for the second order diﬀerential
equation satisﬁed by the Jacobi functions (see a survey of these functions in [17]). The
support of the spectral measure is determined by the zeros of a c-function. We calculate the
Green function and we obtain the spectral measure for the doubly inﬁnite Jacobi matrix
from the Green function. The spectral measure is discrete and its support falls into two
sets; one set corresponding to eigenvectors in terms of the q-Laguerre polynomials and the
other set corresponding to eigenvectors in terms of the q-Bessel coeﬃcients. It should be
noted that this method corresponds to the one employed by Kakehi, Masuda and Ueno [11],
2
[12] giving the Plancherel measure for the little q-Jacobi functions from its interpretation
as matrix elements of irreducible representations of SUq(1, 1).
The orthogonality relations and squared norms resulting from the spectral analysis
are explicitly given in §4. Since we give a basis for this space we also obtain the dual
orthogonality relations as an immediate consequence. Using a method of Berg [3] we can
easily construct more non-N-extremal orthogonality measures for the q-Laguerre polyno-
mials on the same set {cqk | k ∈Z} by perturbing with any of the q-Bessel functions,
which is bounded on this set.
In §5 we give a straightforward proof of the orthogonality relations for the q-Laguerre
polynomials and q-Bessel functions using two generating functions for the q-Bessel func-
tions. This technique is motivated by [18], [13].
In §6 we obtain the orthogonality relations for the big q-Bessel functions as a rigorous
limit of the big q-Jacobi polynomial case.
The formal limit is suggested by the limit
transition of SUq(2) group to Eq(2). Big q-Jacobi polynomials have an interpretation as
basis elements for the regular representation of SUq(2) on quantum spheres, see [22]. In
the limit transition these basis elements tend to the corresponding basis elements for the
regular representation of Eq(2) on quantum hyperboloids, and these latter basis elements
can be written as big q-Bessel functions, see [4].
So we see that the same result on q-special functions can be obtained from two dif-
ferent quantum group interpretations: by considering the quantum SU(1, 1) group or the
quantum group of plane motions. This is also the case for the little q-Jacobi functions
studied in [11], [12], which originated as spherical functions on SUq(1, 1), but which can
also be viewed as certain q-analogues of Bessel functions and then have an interpretation
on the quantum group of plane motions, see [15].
Notation. We follow the notation of Gasper and Rahman [7] for basic (or q-)hypergeometric
series. Throughout we assume that 0 < q < 1.
