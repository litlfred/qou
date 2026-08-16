---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-008-c-from-the-physical-point-of-view-this-is-not-ve
section_title: "From the physical point of view, this is not very"
section_number: C
pages: 8-11
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
7
surprising since we start with a Chern-Simons theory, which has vanishing Hamiltonian
and, therefore, is expected to be a topological quantum ﬁeld theory.
The quantum invariant Z(M ;γi,R i) is particularly interesting for the complex gauge
group GC =SL(2,C), which is related to three-dimensional Euclidean gravit y with nega-
tive cosmological constant. In particular, classical solu tions in the gravity theory (1.6) cor-
respond to manifolds with constant negative curvature, and one can also interpret certain
Wilson line operators WR(γ) as operators creating cusps in M . Therefore, Z(M ;γi,R i) is
a natural invariant of hyperbolic three-manifolds with cus ps. If we remove the cusps from
M , we can also interpret Z(M ;γi,R i) as a topological invariant of the complement of the
link, whose components are γi.
According to a famous theorem by Thurston, many 3-manifolds are hyperbolic [31].
For example, the complement of a knot in S3 admits a hyperbolic structure unless it is a
torus or satellite knot. Moreover, after the Mostow Rigidit y Theorem [32], any geometric
invariant of a hyperbolic 3-manifold is a topological invar iant. Important geometric invari-
ants, which can be deﬁned even if the hyperbolic manifold M has cusps [33], are the volume
and the Chern-Simons invariant. Thurston suggests to combi ne these two invariants into
a single complex invariant Z(M ) whose absolute value is e2/π Vol(M ) and whose argument
is the Chern-Simons invariant of M [31]:
Z(M )∼ exp
( 2
π Vol(M ) + 4πiCS (M )
)
(1.14)
As one might expect from (1.7), the path integral (1.2) reduc es to an invariant like this in
the semi-classical limit.
More surprisingly, extending the well-known volume conjec ture [34,35,36], we ﬁnd that
the N -colored Jones polynomial, JN (γ,e 2πi/k ), also has a similar asymptotic behavior in
the limit k,N → ∞, such that the ratio, a = N/k, is ﬁxed. Namely, depending on
whether the parameter a is rational or not, the asymptotic behavior of JN (e2πi/k ) is either
polynomial or exponential (the value a = 1 is somewhat special). According to a seminal
work of Witten [3], the ﬁrst case is related to the SU (2) Chern-Simons gauge theory
and rational conformal ﬁeld theory in two dimensions. On the other hand, as we show
below, the exponential growth of the colored Jones polynomi al encodes a lot of interesting
information about the hyperbolic geometry of the knot compl ement and, therefore, is more
suggestive of the SL(2,C) Chern-Simons theory. Schematically, the whole picture c an be
summarized in the following table:
8
a =N/k asymptotic behavior CFT Chern-Simons
of JN (e2πi/k ) theory
Rational Polynomial Rational SU (2)
Non-Rational Exponential Non-Rational SL(2,C)
T able 1: Asymptotic behavior of the colored Jones polynomial for hyp erbolic knots.
This heuristic picture agrees with the fact that, when k = 0 and σ∈ Z Z, the partition
function (1.2) of the SL(2,C) Chern-Simons theory can be formally regarded as a product
of two SU (2) partition functions by treating A andA as independent SU (2) gauge ﬁelds.
Moreover, it was argued in [37] that at these values of the cou pling constants the Hilbert
space of the SL(2,C) Chern-Simons theory on a torus factorizes into two copies of the
Hilbert space of an SU (2) theory.
The analytic continuation to non-integer values ofk in theSU (2) Chern-Simons theory
can be also motivated by connection with topological string theory. Just like ordinary
quantum ﬁeld theory can be embedded in string theory, topolo gical Chern-Simons theory
can be realized in topological open string theory [38], wher e the string coupling constant
is related to the level k. In many cases, these theories admit a dual description in te rms
of closed topological strings on a (non-compact) Calabi-Ya u manifold [39]. Therefore,
from the point of view of topological string theory, it is als o natural (and sometimes
even necessary) to consider non-integer values of k, which via duality is identiﬁed with
the complexiﬁed K¨ ahler parameter of the Calabi-Yau manifo ld [40]. Then, the results of
this paper suggest that certain invariants of hyperbolic 3- manifolds might emerge from
topological closed string theory in the “zero radius limit” .
Finally, we note that Chern-Simons theory with SL(2,C) gauge group also has a
number of interesting applications in string theory, see e.g. [41,42] for some recent work.
Organization of the Paper
The rest of the paper is organized as follows: In section 2, we study classical aspects
of Chern-Simons theory with complex gauge group. In particu lar, we introduce the A-
polynomial of a knot and identify it with the space of classic al solutions in the SL(2,C)
Chern-Simons theory on the knot complement. Section 3 is dev oted to quantization of
this theory (in a real polarization). Starting with section 4, we discuss various extensions
9
and applications of this approach, including mathematical applications. In section 5, we
present some evidence for the picture summarized in Table 1 a nd propose a generalization of
the volume conjecture to incomplete hyperbolic structures on knot complements. Further
aspects of the relation with SU (2) Chern-Simons theory and the colored Jones polynomial
are discussed in section 6, where we propose an analog of the M elvin-Morton-Rozansky
conjecture for a non-trivial (“hyperbolic”) ﬂat connectio n. Finally, in the appendices we
illustrate the general ideas using simple examples. Thus, i n Appendix A, we use the
geometry of the BTZ black hole to explain the origin and the in terpretation of the A-
polynomial for the trivial knot. In Appendix B, we discuss qu antization of the SL(2,C)
Chern-Simons theory for torus knots, which leads to a partic ularly simple (Gaussian)
quantum mechanics.
