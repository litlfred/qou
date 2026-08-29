---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-025-4-polynomial-invariants
section_title: "Polynomial invariants"
section_number: 4
pages: 15-17
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
4.1. Alexander polynomial
In [B], Birman proposed (but considered as very difﬁcult) the problem to classify 3-braid links with given polynomials.
In [St2] we dealt with the skein polynomial. Now we can extend our results to the Alexander polynomial (with the
convention in the beginning of §3.3). The following discussion gives a fairly exact description how to ﬁnd the 3-braid
links, if such exist, for any possible admissible (as speciﬁed in §2.2) polynomial.
A solution for the Jones polynomial is presented afterwards.
Lemma 4.1 If β is strongly quasi-positive and ﬁbered, then maxcf ∆ = +1.
(Here it is essential to work with the leading, not trailing c oefﬁcient of ∆ and with strongly quasi-positive links and
not their mirror images.)
Proof. We know mindeg v P = maxdeg z P = 1 − χ. So [P]z1−χ has a term in degree v1−χ. The coefﬁcient must be
+1 because of (17) and because it is the only coefﬁcient that co ntributes to the absolute term in P(v,v−1 − v). Now
from the classiﬁcation of leading z-terms of P in [St2] it follows that [P]z1−χ can have at most one further term, with
coefﬁcient ±1. If such term exists, the substitution (4) would either cancel the terms in degree t(1−χ)/ 2 in ∆(t), or give
coefﬁcient ±2, so our link cannot be ﬁbered. Thus a second term does not exist, and the claim follows from (4). ✷
Lemma 4.2 Let β′ = [(123)k] be an even power k of [123]. Assume β has Xu normal form R, and after syllable
reduction becomes β′, but β ⁄= β′ itself (i.e. some syllable in β is non-trivial). Then ˆβ satisﬁes maxdeg ∆ = −1 − χ;
moreover maxcf ∆ > 0 and is equal to the number of non-trivial syllables in β.
Proof. We use for ﬁxed k induction on the exponent sum. If exactly one syllable is non -trivial with exponent 2,
then applying the skein relation at the exponent-2 syllable shows that β = β+ inherits the Alexander polynomial of
β− with positive sign (since β0 = β′, whose closure has zero polynomial). Now β− is positive and has an index
array with a subsequence of the form xyx, and so is ﬁbered by theorem 3.2. Then by lemma 4.2, maxcf ∆ = +1 and
maxdeg ∆ = 1 − χ(ˆβ−) = −1 − χ(ˆβ).
If [β] − [(123)k] > 1, then applying the skein relation at any non-trivial expon ent 2 syllable gives (with positive sign)
the Alexander polynomials of two closed braids β0 and β−, former of which is ﬁbered and latter of which has the
requested property by induction. Then the maximal terms in d egree 1 − χ(ˆβ−) = −χ(ˆβ0) are positive and do not
cancel. The one of β− is +1, while the one of β0 by induction one less than the number of non-trivial syllabl es in β
(since in β0 one more syllable becomes trivial).
If some syllable in β has exponent > 2 then β− is not minimal, and the degree and leading coefﬁcient of∆ are inherited
(with positive sign) from β0. ✷
Lemma 4.3 Assume β has Xu normal form R, which after syllable reduction becomes an odd power k of [123]. Then
maxdeg ∆ = 1 − χ, and maxcf ∆ = +2.
Proof. First we prove the claim if β = [(123)k]. We know that maxdeg ∆ = 1 − χ and maxcf ∆ = ±2, so we must
exclude maxcf ∆ = −2. Applying the skein relation gives the polynomials of β0 and β− with positive sign. β0 is
positive and ﬁbered as before, so maxcf ∆ = +1. Then clearly β− (which is of the form L−1R and also ﬁbered) cannot
have maxcf ∆ = −3.
If β ⁄= [(123)k], then it has a non-trivial syllable. Applying the skein relation at a letter in that syllable we ﬁnd that β−
reduces. So the leading term comes from β0, and with positive sign. ✷
Theorem 4.1 Fix some admissible Alexander polynomial ∆. Then
16 4 Polynomial invariants
1) If ∆ = 0, then the 3-braid links with such polynomial are the split links and the closures of (incl. negative) even
powers of [123].
2) If ∆ ⁄= 0, there are only ﬁnitely many 3-braid links with this ∆. They all have 1 − χ = 2maxdeg ∆ or −1 − χ =
2maxdeg ∆. In latter case they are up to mirroring strongly quasi-positive.
3) If maxcf ∆ ≤ −2, then no 3-braid knot or 3-component link has such Alexande r polynomial, and any 2-
component link is strongly quasi-negative.
4) If maxcf ∆ ≥ +2, any 3-braid knot or 3-component link with such Alexander p olynomial is strongly quasi-
positive or a mirror image of it. Any 2-component link is strongly quasi-positive.
5) If |maxcf ∆| > 2, then any 3-braid link with such Alexander polynomial has 2maxdeg ∆ = −1 − χ.
Deﬁnition 4.1 Let for β ∈ B3 with 6 | [β], the Birman dual β∗ be deﬁned by β−1δ2[β]/ 3, where δ = [121] and δ2
generates the center of B3.
Birman [B] shows that ˆβ and ˆβ∗ have the same skein polynomial. This observation relates to our explanation at a
couple of places, for example, in remark 3.1, and also in the below arguments.
Proof of theorem 4.1. Let us exclude a priori trivial and split links. The claims follow from the discussi on of
2maxdeg ∆ and maxcf ∆ in cases.
We know by theorem 3.3 (or by [St2, St4], as noted before) that if β ∈ B3 is not (up to mirroring) strongly quasi-
positive, then 2maxdeg ∆ = 1 − χ and maxcf ∆ = ±1.
It remains to deal with the Xu form R. The form L is just the mirror image, and mirroring preserves the Alexan der
polynomial for knots and 3-component links and alters the sign for 2-component links.
If making trivial all syllables in β, the new word β′ is not a power of [123], then we proved that ˆβ is ﬁbered, so again
2maxdeg ∆ = 1 − χ and maxcf ∆ = ±1.
If β′ is an even power of [123], then by Birman duality we conclude that ∆(ˆβ′) = 0. If β ⁄= β′, then one uses lemma
4.2. Thus 2maxdeg ∆ = −1 − χ.
If β′ is an odd power of [123], then use the observation in lemma 4.3 (or make one syllable t o exponent 4 and use
Birman duality) to conclude that 2maxdeg ∆ = 1 − χ and maxcf ∆ = +2. ✷
Example 4.1 In certain situations this theorem gives the most rapid test to exclude closed 3-braids. For example, the
knot 136149 has MW F = 3, but seeing that ∆ has maxcf ∆ = −2 we immediately conclude that it cannot be a closed
3-braid.
Corollary 4.1 There are only ﬁnitely many 3-braid links with given maxdeg ∆ (provided ∆ ⁄= 0). ✷
It is actually true (as we will prove below) that for links wit h any bounded braid index there are only ﬁnitely many
different Alexander polynomials of given degree admitted. However, such Alexander polynomials may be admitted
by inﬁnitely many different links (of that braid index). See §7.3 for some remarks.
Corollary 4.2 Non-split 3-braid links bound no disconnected Seifert surf aces (with no closed components). In par-
ticular there are no non-trivial 3-braid boundary links.
Proof. For such links the Alexander polynomial is zero. The only non -split 3-braid links L of zero polynomial are
closures of [(123)k] for even k. These cases are easily ruled out by linking numbers. Any pair of components of L has
non-zero linking number. So a connected component of any Sei fert surface S of L must have at least two boundary
components of L, and if S is disconnected, L has at least 4 components, which is clearly not the case. ✷
The examples that falsify this claim for 4-braids are again e asy: consider the (closure links of) words in [1 ± 2 − 1]
and [2 ± 3 − 2].
