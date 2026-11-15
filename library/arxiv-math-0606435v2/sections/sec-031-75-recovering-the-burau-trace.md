---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-031-75-recovering-the-burau-trace
section_title: "Recovering the Burau trace"
section_number: 7.5
pages: 53-53
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Recovering the Burau trace
53
Proof. From e, V and ∆we know
˜Xa =
3
∑
i=0
Xi(q)qa(i+(e−3)/2),
for a ∈{−2,−1,0,1}. (For a = −2 and a = 0 we have the trivializing substitutions, a = −1 corresponds to ∆and
a = 1 to V.) So one can recover Xi from ˜Xa and e. (One can write down an explicit formula easily.)
✷
This condition is thus equally unhelpful as a 4-braid test. For a similar reason, I expect (though I have not rigorously
derived) an explanation of the (experimentally observed) failure of Jones’s conditions [J, §8] (see formula (8.10)) to
obstruct to a 4-braid.
Example 7.3 The knot 11386, known from [LM], has the Jones polynomial of the ﬁgure-8-knot. So 11386 and its
mirror image show that the dependence of P on e in proposition 7.3 is essential.
Question 7.2 Are there 5-braids β1,2 (at least one of which has MWF = 5), with the same exponent sum, V(ˆβ) and
∆(ˆβ), but different P(ˆβ)?
The lack of such examples, after some check in the knot tables, is at least not fully explainable. Only 6-braids could
be found.
Example 7.4 The knots 16443392 and !15223693 have the same V and ∆but different P polynomial. They have MWF =
5 resp. 4, with 5- resp. 4-braid representations of exponent sum 2 resp. −1, so one obtains 6-braids of exponent sum
1 by stabilization.
One can now, as before, go over to the norms in each row in table 3, or of arbitrary linear combinations of such
rows. Then for q where J0 is deﬁnite we obtain again estimates on |Xi(q)|, or of |X(q,λ)| for any non-zero complex
number λ. (In particular, for λ = q we obtain theorem 7.3 and for λ = 1/q corollary 7.3.) Although they still contain
the Jones and Alexander polynomial conditions (which were observed both non-trivial in comparison to MWF), such
skein polynomial norm estimates have not proved in practice, as a 4-braid test, an efﬁcient improvement over their
special cases and MWF. Below we will explain how to do much better.
Knots like 10132 and 10156 in example 7.2 show a disadvantage of our test, resulting from not taking into account
information of other invariants. On the opposite hand, the mere use of ∆or P reduces calculation complexity, and
excludes any potential further knot with such polynomial. In the case of P this gives yet a different way to answer
negatively Birman’s question if one can realize any skein polynomial by a link making MWF sharp (see [St3, St2]).
Using the Brandt-Lickorish-Millett-Ho polynomial, Murakami [Mr] and later Kanenobu [K] gave with theorem 4.7 a
more efﬁcient (in excluding examples, though less in calculation complexity) test for a 3-braid. But the work in [St2]
and in the previous sections of this paper makes the study of polynomials of 3-braids anyway less relevant. 4-braids
become much more of interest, and in this case, after MWF, the problem to ﬁnd applicable conditions has been largely
unsettled for quite a while.
7.5.
Recovering the Burau trace
