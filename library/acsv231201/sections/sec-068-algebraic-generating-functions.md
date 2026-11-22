---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-068-algebraic-generating-functions
section_title: "Algebraic generating functions"
section_number: null
pages: 420-422
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Algebraic generating functions in one variable can be analyzed asymptotically
by the transfer theorems of Section 3.4 in Chapter 3, and often exactly by La-
grange inversion as described in Section 12.3 above. Of course, the situation
in several variables is more complicated. For the purposes of asymptotics, we
can sometimes ignore the fact that the generating function is algebraic, because
the contributing points determining asymptotics might occur in regions where
the generating function is meromorphic (this happens in several Riordan array
examples). The more diﬃcult cases occur when asymptotics are determined
by an algebraic singularity. Assuming that we have an analytic branch at the
origin, we aim to compute asymptotics of the coeﬃcients of its power series
expansion as done for rational and meromorphic functions in previous chap-
ters.
Section 2.4 gives an approach to asymptotics by embedding algebraic gen-
erating functions as subseries of higher-dimensional rational functions. Un-
fortunately, there are several diﬃculties with this approach. First, the results
of Chapters 9–11 cannot capture asymptotics of all algebraic generating func-
tions: for any β ∈Z there exists a univariate sequence an with an algebraic
generating function such that an ∼Cαnnβ, but our results for nondegenerate
critical points only give asymptotics of this form with β = k/2 for k ∈Z. This
asymptotic behavior also shows that the leading terms in our asymptotic ex-
pansions often vanish when applied to rational functions constructed by such
lifting procedures (Exercise 12.11 asks you to prove that this vanishing always
occurs for an embedding given by the method presented in Proposition 2.36).
Algebraic generating functions are often well-behaved as they are built from
nice combinatorial constructions, but the rational functions obtained from a
lifting procedure are built from algebraic machinery and are thus often worse
12.6 Algebraic generating functions
403
behaved. For instance, the lifted functions usually have negative power series
coeﬃcients, making the determination of minimal points harder to verify, and
may have critical points at inﬁnity. Finally, there is no guarantee that the ratio-
nal generating function will have a contributing singularity of a type that we
can deal with using current technology.
Despite these qualiﬁcations, the rational embedding approach does work in
many situations.
Example 12.18. Consider the shifted Catalan number GF f(x) = P
n anxn =
(1 −
√
1 −4x)/2 with minimal polynomial P(x, y) = y2 −y + x. Proposi-
tion 2.34 implies that f(x) is the main diagonal of the bivariate rational function
F(y, z) = y(1 −2y)/(1 −x −y). The singular variety V of F is globally smooth
and the critical point equations yield the single solution (1/2, 1/2) which is
strictly minimal. The ﬁrst term in the expansion (9.4) vanishes, as expected,
while the second term does not vanish and implies an ∼4n−1/
√
πn3.
◁
Remark 12.19. For bivariate algebraic singularities it is also possible to de-
termine asymptotics through a transfer theorem [Gre18].
Example 12.20. As shown in Example 2.37, the generating function for the
Narayana numbers ars is the subseries of
F(w, x, y) = w(1 −2w −wx(1 −y))
1 −w −xy −wx(1 −y)
consisting of terms whose powers of w and x are equal. Since F can be written
F(w, x, y) =
(1 −w)−1
1 −xy −
wx
1−w
,
its power series expansion is combinatorial. To determine asymptotics of aαn,βn
as n →∞with α > β > 0, we compute asymptotics of the power series
coeﬃcients of F in the direction (α, α, β). The critical point equations yield the
unique solution
(w, x, y) =
 β
α, (α −β)2
αβ
,
β2
(α −β)2
!
,
which can be shown to be minimal as F is combinatorial. An asymptotic ex-
pansion can thus be computed using Theorem 9.5 in Chapter 9. In particular,
the exponential growth of aαn,βn is

αα
ββ(α−β)α−β
2, with the maximum exponential
growth of 4 achieved when α/β = 2.
◁
One positive feature of the embedding approach is that there are many possi-
ble embeddings of a given algebraic generating function, so if a rational func-
404
Combinatorial applications
tion obtained by one embedding procedure is too diﬃcult to analyze, it may be
possible to ﬁnd one better suited to ACSV.
Example 12.21. The combinatorial univariate algebraic generating function
√
1 −x −1 = P
n anxn is the main diagonal of
2 (Yx −1)(Y + 1)Y
Y2x + 2 Yx −Y + x −2.
It is easily checked that among aﬃne points of the singular variety, there are
no non-smooth points and no critical points for the main diagonal direction,
so asymptotics are determined by a critical point at inﬁnity. The generating
function 2xY/(2 −x −Y) has the same main diagonal but is much easier to
analyze, giving an ∼(πn)−1/2, as we expect from Newton’s binomial theorem
and Stirling’s approximation.
◁
See Section 13.5 for further discussion on ACSV and algebraic generating
functions.
