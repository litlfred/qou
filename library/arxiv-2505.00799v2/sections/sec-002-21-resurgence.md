---
doc_id: arxiv-2505.00799v2
doc_title: "QUANTUM MODULAR FORMS AND RESURGENCE"
section_id: sec-002-21-resurgence
section_title: "Resurgence"
section_number: 2.1
pages: 6-7
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
doc_brief: "QUANTUM MODULAR FORMS AND RESURGENCE — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
Corollary 1.4. Letf(z) be the periodic function of the real-analytic Eisenstein seriesE1/2(z),
defined in Equation 2.4. Define
ψ(z) :=f(z)−z−1f(−1/z).
Then the function ψ has an analytic continuation to C′.
We remark that our methods are likely generalizable to more general spectral parameter
and level for both Maass cases.
As an additional result showing the flexibility of these methods, we reprove the quantum
modularity of cusp forms and of Eichler integrals of integer weight cusp forms using a variant
of the same framework. We remark that in these cases, resurgence analysis on its face will
not apply; see Remark 3.2 of [15]. Our main result is the following:
Theorem 1.5. Supposeg is one of the following:
(1) a cusp form of weight κ∈ N for Γ = Γ0(N);
(2) a cusp form of weight κ∈ 1
2 + N0 for Γ = Γ0(N), 4|N;
(3) the Eichler integral of a cusp form of weight 2−κ∈ N for Γ = Γ0(N);
(4) the Eichler integral of a cusp form of weight 2−κ∈ 1
2 + N0 for Γ = Γ0(N), 4|N;
(5) the periodic function of a Maass waveform with s = 1
2 =κ/2 for Γ = SL2(Z);
(6) the periodic function of Eκ/2(z) with s = 1
2 =κ/2 for Γ = SL2(Z).
Theng is a holomorphic quantum modular form of weight κ for Γ. Moreover, for each γ∈ Γ,
the modular obstruction hγ equals a Borel–Laplace sum of the asymptotic series of g as z
approachesγ−1(i∞) along a geodesic, and analytically continues to Cγ.
For the remainder of the paper, we will refer to these cases as Type 1 through Type 6.
We note that the results above for Types 1 and 2 are immediate from their definitions.
However, the methods developed for the remaining types in this paper can be applied to
functions related to those of Types 1 and 2 to give an interesting resurgence perspective on
these functions which themselves have no resurgent structure.
Remark. Many of the above functions have a natural “companion” in the lower half-plane
like the example of σ and σ∗. Our results can equivalently be proven for the corresponding
functions on C\R.
QUANTUM MODULAR FORMS AND RESURGENCE 7
We note that the quantum modularity of these functions is not new, but the quantum
modularity of half-integral weight Eichler integrals has been strengthened to holomorphic
quantum modularity, and the relationship of Borel resummation to their quantum modularity
across all cases was previously conjectured but unproven.
Theorem 1.5 and its proof additionally give evidence towards some conjectures of Fantini
and Rella [15]:
Corollary 1.6. The asymptotic series of Eichler integrals of half-integral weight cusp forms,
periodic functions of Maass waveforms with s = 1/2, and the periodic function of the real-
analytic Eisenstein series with s = 1/2 are modular resurgent series. Moreover, the median
resummation of each of these series recovers the original function, which is a holomorphic
quantum modular form.
The paper is organized as follows. In Section 2, we develop the necessary background on
resurgence, as well as holomorphic modular and Maass forms. In Section 3, we collect a
variety of intermediate results in service of our main theorem. This will be broken up into
three main subsections. Subsection 3.1 will compute the asymptotic expansions of functions
of Types 1 through 6 at the relevant rational points. Subsection 3.2 will use a Gaussian
integration identity to relate each function to the median resummation of its asymptotic
series. Subsection 3.3 will locate the image of each function under the relevant slash operator
in the decomposition coming from Subsection 3.2. In Section 4, we prove Theorem 1.5 and
in Section 5, we prove that the obstructions to modularity have the desired properties for
the statements of our corollaries. In Section 6, we offer some future directions and open
questions that may be of interest to the reader.
