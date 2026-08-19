---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
2 Complex Chern–Simons theory and the A-polynomial 3
2.1 Classical and quantum A-polynomials 3
2.2 The case of SL(2 , C) gauge group 5
3 The structure of the wave function 8
3.1 General conjectures 8
3.2 Cancellation of singularities 11
3.3 The wave function in the rational case, I 13
3.4 The wave function in the rational case, II 16
3.4.1 Solving a second-order q-difference equation 16
3.4.2 Solving a third-order q-difference equation 19
4 Examples 22
4.1 The figure-eight knot 22
4.2 The three-twist knot 25
5 The wave function from the state integral 28
5.1 Evaluation at rational points 29
5.2 Factorization and two special subcases 33
6 Conclusions 35
A Computing the ϵ-expansions 36
B An alternative way of obtaining the integer sequences 37
C Faddeev’s quantum dilogarithm and other special functions 38
1 Introduction
Chern–Simons (CS) theory with a complex gauge group has been an excellent laboratory for studying
various aspects of quantum field theory (QFT) since it is essentially exactly solvable. In recent years,
building on previous work by physicists and mathematicians, perturbative and non-perturbative
methods have been introduced, making it possible to calculate various observables, and many beau-
tiful and interesting results have been obtained. For example, for the complements of hyperbolic
knots in the three-sphere, the wave function of the theory with gauge group SL(2 , C) has been de-
fined rigorously [1], inspired in part by physics developments [2, 3]. This wave function satisfies,
in addition, a difference equation, which can be determined by an appropriate quantization of the
classical A-polynomial of the knot [4], as expected from physics arguments [5].
– 1 –
In this paper, we will further study the wave functions for complements of hyperbolic knots
in CS theory with gauge group SL(2 , C). As we will show, they share many structural similarities
with the wave functions occurring in topological string theory and, more precisely, in the context
of the so-called topological string/spectral theory (TS/ST) correspondence [6–9] and its open string
version [10–13]. Indeed, it has been found in both cases that the WKB expansion in ℏ of the
perturbative wave function of the topological string can be resummed into a q-series1, whereq = eiℏ.
However, thisq-series displays singularities at all points of the form
ℏ∈ 2πQ. (1.1)
Since these singularities are not present in the non-perturbative definition of the wave function, they
are an artifact of the resummed WKB expansion. This feature, in turn, requires the presence of a
non-perturbative sector that cancels the singularities and leads to a finite answer for the full wave
function. The cancellation of singularities at the values of ℏ in Eq. (1.1) is a defining attribute of
Faddeev’s quantum dilogarithm [14], which can be regarded as a simple example of a wave function
in complex CS theory. A similar cancellation mechanism has appeared in a more complicated
context in ABJM theory, where it is sometimes referred to as the HMO mechanism [15], and is
one of the facets of the non-perturbative proposal for topological string theory put forward in [6–8].
Moreover, the concrete realization of the cancellation of singularities in topological string theory is
a consequence of the integrality structure of the topological string amplitudes. In the closed string
case, one has the Gopakumar–Vafa integrality [16] and its refinement [17]. In the open string case,
as shown in [10, 12, 18], one needs an integrality property akin to the one found in [19–21]. In this
paper, we conjecture a similar integrality structure for the resummed WKB expansion of the wave
functions of complex CS theory and support our claims with explicit evidence obtained in examples.
This integrality structure, indeed, guarantees the cancellation of singularities. A similar integrality
property has been found in [22], and it would be interesting to clarify its relationship with our results.
Our integrality conjecture characterizes the so-called holomorphic blocks of the wave func-
tions [23], and the corresponding integer invariants can be calculated from these blocks when they
are explicitly known. Analogously to the case of topological string theory, at the special values of
ℏ in Eq. (1.1), which we refer to as rational points, the generic formula for the exact wave function
has an apparent singularity. However, after the cancellation mechanism takes place, one typically
finds a relatively simpler expression. It is an interesting task to determine this expression for general
rational numbers, as it was done for Faddeev’s quantum dilogarithm in [24]. In this paper, we de-
velop various independent techniques to achieve this goal, following ideas proposed in the context of
the open TS/ST correspondence [12, 25, 26]. To begin with, one can use the underlying integrality
structure to derive an explicit answer at rational values of ℏ in terms of the newly introduced integer
invariants. Second, one can start directly from the AJ equation for the wave function and specialize
it to rational values, where one finds a quasi-periodic structure similar to the one appearing in spec-
tral problems on lattices. Finally, one can directly evaluate the Andersen–Kashaev state integral at
rational points using the techniques of [24]. We apply these three distinct methods and explicitly
show that they lead to the same results in various examples.
The paper is organized as follows. In Section 2, we review the necessary background notions on
complex CS theory and the AJ conjecture. In Section 3, we present most of our results. In particular,
we state the integrality conjecture for the WKB resummed wave function and show how it implies
the cancellation of singularities at rational values of ℏ. We also provide two different techniques
1This is a resummation of aconvergentseries, so it does not involve the more sophisticated techniques of resummation
of divergent series, like Borel resummation.
– 2 –
for evaluating the wave function at rational points. In Section 4, we illustrate these results by
performing explicit computations in the concrete examples of the figure-eight and the three-twist
knots. In Section 5, we evaluate directly the state integral in the rational case for the figure-eight
knot. Finally, we conclude and list some open problems in Section 6. In the three Appendices,
we provide additional details on the calculations we perform in Section 3 and recall some useful
properties of Faddeev’s quantum dilogarithm.
