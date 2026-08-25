---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-020-51-how-the-data-was-computed
section_title: "How the data was computed"
section_number: 5.1
pages: 20-21
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
computes the Neumann-Zagier matrices of default ideal triangulations of the knots below, as
well as their exact shapes and trace ﬁelds (computed for instance from the Ptolemy module
of SnapPy) [GGZ15, CDW].
Given a Neumann-Zagier datum, the 2 and 3-loop invariants at level k are algebraic
numbers, elements of the ﬁeldFK,k =FK(ζk), whereFK is the trace ﬁeld ofK andζk =e
2πi
k .
However, these numbers are obtained by sums of algebraic numbers in a much larger number
ﬁeld. Moreover, the 1-loop invariant at level k already contains a k-th root of elements of
FK,k. This makes exact computations impractical. To produce the interesting factorization
of Equation (3), and keeping in mind the ambiguities of Section 4.5 we proceed as follows.
We know thatxk,𝓁 =τk
k/(τk
1ζ𝓁
24k)∈FK,k for some natural number 𝓁. Given this, we compute
the numerical valuexnum
k,𝓁 ofxk,𝓁 (for several values of𝓁) and ﬁnd a value of 𝓁 for which there
is an element xexact
k,𝓁 of FK,k which is reasonably close to our element. We accomplish this
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 21
by the LLL algorithm [LLL82]. The Quantum Modularity Conjecture asserts that the exact
element of FK,k should to have the form:
(55) xexact
k,𝓁 =εK,kβk
K,k
for εK,k∈O×
FK(ζk) (an algebraic unit) and βK,k∈FK(ζk)×. To ﬁnd ϵK,k and βK,k, factor the
fractional ideal
(56) xexact
k,𝓁 OFK(ζk) = pe1
1 ... per
r
into a product of prime ideals pi, i = 1,...,r . If all ramiﬁcation exponents ei are divisible
byk, and if the prime ideals are principal pi = (℘i) for ℘i∈F×
K,k (the latter happens when
the ideal class group of FK,k is trivial), then we deﬁne
βK,k =
r∏
i=1
℘
ei
k
i ∈F×
K,k, ε K,k =xexact
k,𝓁 /βk
K,k.
It follows that εK,k is a unit, and that (55) holds. This gives us strong conﬁdence that xexact
k,𝓁
is the correct element, and that the computation is correct.
In practice, we have used a Mathematica program to computexnum
k,𝓁 andxexact
k,𝓁 , and a Sage
program (that uses internally pari-gp) to compute the ideal factorization (56).
