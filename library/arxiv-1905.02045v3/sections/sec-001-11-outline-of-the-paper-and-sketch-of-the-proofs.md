---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-001-11-outline-of-the-paper-and-sketch-of-the-proofs
section_title: "Outline of the paper and sketch of the proofs"
section_number: 1.1
pages: 6-7
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
based on two new relations for the q-Pochhammer symbol, given in Theorems 6 (cf. (1.5))
and 7. These relations are proved in Section 2 and both make use of the Abel-Plana sum-
mation formula [1, p.23], [37, p.408], [36, Chapter 8.3.1], which is a form of Euler-Maclaurin
summation with an explicit form of the error term. In the case of Theorem 6, one starts by
dividing the product in the deﬁnition (1.4) of (e( γα))r into appropriate intervals and congru-
ence classes. One then take the logarithm and apply the summation formula to the resulting
sum of the function log(1 − e(z)). As this function is close to a primitive of π cot(πz), which
has poles at integers, then through a residue computation one eventually arrives to the dual
object (e(α))r′. In the case of Theorem 7, the reciprocity relation for the q-Pochhammer
symbol relates h
k and k
h. In this case one starts by applying the simple relation h
k ≡− k
h +
1
hk (mod 1). After some initial manipulations, one is lead to consider sums of the function
log(1− cot(πξ) tan(πξz)) + cot(πξ) tan(πξz) for some choices of ξ∈ (0, 1/2). This is again
performed using Abel-Plana summation formula followed by a careful analysis, with particular
care needed in the reassembling of various main terms.
In both our reciprocity relations for theq-Pochhammer symbol, we show that the error terms
extend to holomorphic functions of controlled growth. This is crucial for the applications to
the modularity relations for the Kashaev invariant for knots other than 4 1.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 7
Once the reciprocity formulas for the q-Pochhammer symbol are established the proofs of
Theorem 1 and Theorem 2, given in Section 3 and 4 respectively, follow in similar ways.
We ﬁrst split the sums in the deﬁnition of the Kashaev invariant into congruence classes
(and suitable intervals) and apply the reciprocity relations, reducing the problem to that of
estimating certain sums of exponentials of linear combinations of dilogarithms. These sums
are very similar to the ones one needs to consider for the the volume conjecture with only two
relevant diﬀerences: the variables of summation range over some convex space rather than
some larger cubic regions, and inside the exponential we have also some new error terms. For
all the knots we consider the ﬁrst diﬀerence is easily treated since, as shown in Lemma 10,
the neglected terms are much smaller than the main terms (for other knots, such as 7 2, a
treatment as in [33, Section 8] should be possible). In the case of Theorem 1, the second
diﬀerence is also surpassed thanks the holomorphicity of the error terms mentioned above,
since the complex analytic methods of [32, 34, 33], using Poisson summation and the saddle-
point method, go through essentially unchanged. In the case of Theorem 2, while we still have
the holomorphicity of the error terms, the fact that the errors are not o(1) forces us to use
positivity to avoid possible cancellations in the main terms, thus restricting the applicability
to the 4 1 knot only.
Theorems 3, 4 and 5 are proved in Section 5 and all use the reciprocity formulas (1.3)
and (1.7) (the latter being more crucial) in conjunction with the recent work [10] on the
distribution of Σ( α). The diﬀerence between the reciprocity relations (1.3) and (1.7) can
be better understood in terms of the continued fraction expansions [0; b1,...,b m] of h/k (for
simplicity we assume m odd). Indeed, (1.3) relates the values of J41,0 at e([0; b1,...,b m])
and at e([0; b𝓁,...,b m]) provided that b𝓁→∞ for some 𝓁∈{ 1,...,m } with all the other bi
bounded, whereas (1.7) relates the values ofJ41,0 at e([0;b1,...,b m]) and at e([0;b1,...,b m−1])
provided thatbm→∞ and that the otherbi are not too large (for example log(bi) =o(bm) for
alli<m would suﬃce). Because of its uniformity, (1.7) can be successfully iterated removing
each time the last convergent bm fromJ41,0(e([0;b1,...,b m])). We keep doing so untill we
reach the last step for which we need to apply (1.3). In this process, we pick up a main term
of Vol(41)
2π bm at each step and thus arrive to (1.9). Equation (1.10) then follows by the law of
large numbers for Σ(α) established in [10].
Theorem 4 follows a similar line, with the diﬀerence that in this case the previous argu-
ment and Conjecture 2 give that logJ41,0(e(α))− Vol(41)
2π Σ(α) can be well approximated by a
diﬀerentiable function. The theorem then follows invoking again [10].
Finally, Theorem 5 follows via a simple argument from Theorem 8, a version of Theorem 2
which becomes useful when there is a middle partial quotient which is extremely large.
