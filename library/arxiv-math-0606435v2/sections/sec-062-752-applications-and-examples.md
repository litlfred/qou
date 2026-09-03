---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-062-752-applications-and-examples
section_title: "Applications and examples"
section_number: 7.5.2
pages: 55-56
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The image of the r.h.s. of (60) under (61) will be some curve in C that generically intersects S1 in a ﬁnite num-
ber of points. This parametric equality can be examined nume rically and allows to recover A = tr ψ 3 up to ﬁnite
indeterminacy. In particular, we have
Proposition 7.4 Assume for some t ∈ S1 with |argt| ≤ π/ 2 we cannot ﬁnd y as in (60), such that λ1 given by (61)
has norm 1 and (63) holds. Then there is no β ∈ B4 with the given e whose closure has the given Alexander and Jones
polynomial. ✷
Remark 7.5 To apply the test in practice, one chooses a small stepwidth s for y in the interval (60), and calculates
the derivative of the r.h.s. of (61) in y to have an error bound on ||λ1| −1| in terms of s. When some of the radicands
in (62) becomes close to 0, some care is needed. One situation where such degeneracy occurs are the knots 15 144634,
15144635, and 15 145731. They have representations β ∈ B4, whose Burau matrix is trivial for t = eπi/ 3. This may be
noteworthy on its own in relation to the problem whether ψ 3 is faithful. (Clearly ψ 3 is unfaithful at any root of unity
on the center of B4, but here β is not even a pure braid.)
Example 7.5 Applying proposition 7.4 we can exclude 11 387, one of the 7 prime 11 crossing knots with b = 5 but
MW F ≤ 4. Eleven prime knots with 12 crossings, and 63 of 13 crossing s where braid index 4 is not prohibited by
MWF can be ruled out. The correctness of these examples was later veriﬁed by the 2-cabled MWF. Up to 16 crossings
more than 4000 examples were obtained. (Let us note that from them only about 100 can be identiﬁed using the norm
estimates.)
Example 7.6 The check of prime 14 crossing knots to which our criterion ap plied, revealed 6 knots with 2-cable
MWF bound 8. One, 14 22691, can be excluded from braid index 4 (as done with 14 45759 in [St3]), by making the v-
degrees of the polynomial of the 2-cable contradict the exponent sum of its possible 8-braid representation. However,
for the other 5 knots, 1428220, 1430960, 1441334, 1441703, and 1444371, the argument fails, and so our condition seems the
only applicable one. (Clearly a 3-cable polynomial is not a c omputationally reasonable option, and even the 2-cable
requires up to several hours, while our test lasts a few seconds.)
Still our criterion leaves open several interesting examples of (apparent) failure of the 2-cable MWF inequality, among
them the knot 139684 encountered with M. Hirasawa. A more general, and important, possible application is as follows.
Remark 7.6 In relation to Jones’s conjecture 7.1, we already quoted (in the proof of theorem 7.1) the observation in
[St3] that counterexamples to the conjecture would make MWFand all of its cabled versions unsharp. In that sense, our
4-braid test may be the ﬁrst possible approach toward identi fying such a counterexample. Birman-Menasco claimed
indeed a family of 6-string potential counterexamples, and K. Kawamuro gave later a simpler family on 5 strings.
Extensive checks with our test of Kawamuro’s knots failed to turn up successful cases. This puzzled us a while,
until Kawamuro reported recently that in fact H. Matsuda falsiﬁed all Birman-Menasco (and hence also Kawamuro’s)
candidates.
56 7 Applications of the representation theory
