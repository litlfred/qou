---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-001-11-deforming-the-volume-of-a-three-manifold
section_title: "Deforming the volume of a three-manifold"
section_number: 1.1
pages: 1-3
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
---
Deforming the volume of a three-manifold
2
1.2.
State integrals
4
1.3.
Proving Borel–Laplace summability
5
Acknowledgements
8
2.
From thimbles to state integrals
9
2.1.
Existence of thimbles
9
2.2.
A relative homology for state integrals contours
12
2.3.
A state integral basis
14
3.
Asymptotics of state integrals
16
3.1.
A steepest descent algorithm
17
3.2.
Proof of Theorem 1.4
19
4.
Examples
21
4.1.
The 41 knot
21
4.2.
The case of (A, B) = (4, 1)
27
Appendix A.
Critical points and independence of state integrals
36
Appendix B.
Faddeev’s dilogarithm
37
B.1.
Asymptotics of the Pochhammer symbol
37
B.2.
Asymptotics of Faddeev’s dilogarithm for Im(τ)̸ = 0
39
B.3.
Asymptotics of Faddeev’s dilogarithm for Im(τ) near 0
40
References
43
Date: October 29, 2024.
Key words and phrases: 3-manifolds, 3d index, asymptotic expansions, Borel transform, complex Chern–
Simons theory, Faddeev’s quantum dilogarithm, hyperbolic geometry, ideal triangulations, Kashaev invariant,
knots, Laplace transform, Neumann-Zagier data, perturbation theory, resurgence, Stokes constants, Stokes
phenomenon, summability, Andersen–Kashaev’s state-integrals, steepest descent, Teichm¨uller TQFT, thim-
ble integrals, volume conjecture.
1
2
VERONICA FANTINI AND CAMPBELL WHEELER
1. Introduction
The volume of a hyperbolic knot K ⊂S3 has a natural perturbative deformation con-
structed from the quantum dilogarithm [16]. This deformation is a formal power series
ΦK(ℏ) = exp
Vol(S3\K)
ℏ
ℏ3/2
√
δ
(1 + A1ℏ+ · · · )
(1)
where δ and Ak are elements in the trace ﬁeld of K. This formal power series ΦK is con-
jectured to agree to all orders with the asymptotic series of the Kashaev invariant of K—
expected to exist as part of Kashaev’s volume conjecture [17]. Independent of Kashaev’s
volume conjecture, the series ΦK can be explicitly described in terms of Neumann–Zagier
data [4] and proved to be a topological invariant [12]. This paper is concerned with the
analytic properties of ΦK.
It was conjecture by Garoufalidis [8] that ΦK is resurgent, which means that its Borel
transform has endless analytic continuation [5]. The singularities of the Borel transform are
expected to be located at the values of the Chern–Simons functional at parabolic SL2(C)-ﬂat
connections of the knot complement. While there have been many examples of resurgent
series associated to non-hyperbolic knots [25, 3], there has been no proof of resurgence of
the asymptotic series ΦK of any hyperbolic knot.
A step further in the study of the analytic properties of ΦK is to address its summa-
bility. This requires the existence of analytic functions with prescribed asymptotics. By
reﬁning Hikami’s original approach [16], Andersen–Kashaev [1] deﬁned a convergent integral
of products of Faddeev’s quantum dilogarithm associated to certain triangulations. These
integrals are called state integrals as they give a continuous analogue of state sums. Combin-
ing ideas from quantum modularity [13] and numerical Borel–Pad´e–Laplace resummation,
Garoufalidis–Gu–Mari˜no [9] gave precise conjectures for the Borel–Laplace resummation of
ΦK for the two simplest hyperbolic knots 41 and 52. The main result of this paper proves
their conjectures for these examples, and it can be summarised in the following theorem.
Theorem 1.1. The series Φ41 and Φ52 are Borel–Laplace summable and their resummations
are equal to combinations of state integrals.
The method that we use to prove these conjectures seems easily generalisable and will
likely lead to many resurgence and summability results for a wide class of asymptotic series
associated to q-hypergeometric functions. This would have a variety of applications in a
number of areas such as topological strings [15], quantum K-theory [14], and complex Chern–
Simons theory [9]. Hopefully, this can also lend insights to the inﬁnite dimensional approach
considered in [18].
1.1. Deforming the volume of a three-manifold. In this paper, we will consider a
two parameter family of examples of asymptotic series similar to those that would come
from a knot. These examples were considered in [10]. In particular, for some A, B ∈Z>0
with A̸ = B, we will consider the function
V : Σ →C/Z
such that
V (z, m) = B Li2(e(z))
(2πi)2
+ B
24 + A
2 z(z + 1) + mz ,
(2)
