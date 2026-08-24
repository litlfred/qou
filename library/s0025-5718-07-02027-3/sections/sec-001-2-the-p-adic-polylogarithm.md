---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-001-2-the-p-adic-polylogarithm
section_title: "The p-adic polylogarithm"
section_number: 2
pages: 2-2
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
The p-adic polylogarithm is an analogue of its complex cousin. It was deﬁned
by Coleman [7] using the technique now referred to as Coleman integration.O n
the open unit disc in Cp, the so called ﬁeld of p-adic complex numbers, it is again
deﬁned by the power series (1.1). To extend it to a function deﬁned on Cp \{ 1}
Coleman uses a technique he called “analytic continuation along Frobenius”, which
is rather involved. As a consequence, it is not so easy to compute the functions
deﬁned in this way. To our knowledge there has been only one attempt to compute
Coleman integrals in the literature [8], with very limited precision.
Recently we embarked on a project of testing numerically thep-adic analogue of
Borel’s theorem (see [4]). This requires the computation of p-adic L-functions and
p-adic polylogarithms up to a given precision. The present work is concerned with
an algorithm for the latter. In the process of describing the set-up for the algorithm
we obtain bounds for |Li
n(ζ)| for a root of unity ζ of order not a power of p that
may be of independent interest (see the end of Section 4).
