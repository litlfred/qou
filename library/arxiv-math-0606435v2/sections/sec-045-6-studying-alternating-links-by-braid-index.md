---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-045-6-studying-alternating-links-by-braid-index
section_title: "Studying alternating links by braid index"
section_number: 6
pages: 38-39
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Remark 5.2 Unfortunately, we cannot completely determine which of the almost positive braid representations with
l = 1 and n1 > 3 in (39) give positive links. For example the Perko knot 10 161 has such a representation, and it is
positive. The Perko move (see [HTW]), turning the closed braid diagram of 10161 into a positive diagram, applies for
more general examples. However, some knots, like 1446862, do not seem subjectable to this or similar moves, and their
positivity status remains unclear at this point.
Similarly, one would hope to prove that among these links non e is a positive braid link (and this way to obtain a
different, but much more insightful proof of theorem 1.3). U sing the polynomials, one can exclude certain families,
for example all links of n1 = 5, but a complete argument again does not seem possible.
6. Studying alternating links by braid index
The combination of the identity (17) and the skein-Jones sub stitution (5) was already used in §4.2 to translate the
determination of the 3-braid link genus from P to V. A similar line of thought will now enable us to extend the oth er
main result in [St2], the description of alternating links o f braid index 3. This result was motivated by the work of
Murasugi [Mu], and Birman’s problem in [Mo2] how to relate br aid representations and diagrammatic properties of
links. We will see how via (5) and the famous Kauffman-Murasugi-Thistlethwaite theorem [Ka2, Mu3, Th2] the Jones
polynomial enters in a new way into the braid representationpicture. The argument will lead to the braid index 3 result
surprisingly easily, and then also to the classiﬁcation for braid index 4 (which seems out of scope with the methods in
[St2] alone). We also obtain a good description of the general (braid index) case.
Our starting point is the following general result concerni ng the MWF-bound (11). A diagram is called special if it
has no separating Seifert circles; see [Cr]. The number of Seifert circles of D is denoted by s(D).
Theorem 6.1 Assume L is a non-trivial non-split alternating link, and MW F(L) = k. Then an alternating (reduced)
diagram D of L has s(D) ≤ 2k − 2 Seifert circles, and equality holds only if D is special.
Proof. As L is non-trivial and non-split, we have 1 − χ(L) > 0. It is also well known, that maxdeg z P(L) = 1 − χ(L)
(see [Cr]). Now spanv P(L) ≤ 2k − 2 by assumption. Under the substitution in (11) this translates to
spanV (L) ≤ 1 − χ(L) +2k − 2 .(41)
On the other hand, by [Ka2, Mu3, Th2], spanV (L) = c(D), and also 1 − χ(L) = c(D) − s(D) +1. So
c(D) ≤ c(D) − s(D) +1 + 2k − 2 ,(42)
and then s(D) ≤ 2k − 1. Now if this is an equality, then so is (41). Then one easily s ees that P(L) must have non-
zero coefﬁcients in both monomials zmaxdegz Pvmaxdeg v P and zmaxdeg z Pvmindegv P. Now under the substitution in (17),
both these monomials give a non-cancelling contribution, a nd one of them is not in ( v-)degree 0, so the identity (17)
cannot hold. Moreover, if (41) fails just by one, then still o ne of the two coefﬁcients must be non-zero. In order
its (non-cancelling) contribution on the left of (17) to be i n degree 0, we see that either maxdeg z P = mindeg v P,
or maxdeg z P = −maxdegv P. Using [Cr], one concludes then that these are precisely the cases of a (positively or
negatively) special alternating link. ✷
Using [Y] and [V o] we have some simple estimate on the unsharpness of MWF for alternating links.
Corollary 6.1 For an alternating non-trivial non-split link L, we have b(L) ≤ 2MW F(L) − 2. ✷
Of course, for many (in particular alternating) links b(L) = MW F(L) (that is, MWF is exact), or at least b − MWF is
small. So the above estimate should be considered as a worst- case-analysis. Even if not strikingly sharp, it is still far
from trivial, in view of what we already know can occur for non-alternating knots. Namely, using the construction in
[K2] and the work in [BM3] (see remark 6.1 below), one can ﬁnd sequences of knots (Ki) for which MW F (in fact the
full P polynomial) is constant, but b(Ki) → ∞.
Another observation is that one can now extend the outcome of the work in [SV] by replacing crossing number of an
alternating knot by its braid index.
39
Corollary 6.2 Let ng,b denote the number of alternating knots of braid index b and genus g. Then ng,b is ﬁnite.
Moreover, for g ﬁxed, we have that limb→∞ ng,b/ b6g−4 = Cg is a constant.
Proof. The ﬁniteness of ng,b follows by (42). When χ(L) is ﬁxed, and c(L) → ∞, one easily sees from (42) that
MW F(L) behaves asymptotically (up to an O(1), i.e. bounded, term) at least like c(D)/ 2. Now Ohyama’s result [Oh]
implies that b(L) (and MW F(L) as well) behave asymptotically exactly as c(L)/ 2. So from [SV] we have the result.
✷
Remark 6.1 Of course we could also gain, as in [SV], an estimate on the Cg and its asymptotics for g → ∞, it would
just multiply by 2 6g−4. One should also note that the ﬁniteness of ng,b, which one sees from (42), is not necessarily
clear a priori. In fact, however, Birman-Menasco proved [BM3] that ng,b is a ﬁnite number even for general (i.e.
without restriction to alternating) knots. Their methods s eem, though, quite unhelpful to estimate these numbers
properly.
Theorem 6.1 immediately leads to the ﬁrst slight sharpening of the description of alternating links of braid index 3 in
[St2]. (The case of MWF = 2 is even more obvious, and omitted.)
Corollary 6.3 An alternating link has MW F = 3 if and only if it has braid index 3.
Proof. If MW F(L) ≤ 3, then the alternating diagram has at most 4 Seifert circles , and exactly 4 only if it is special.
Apart from connected sums (which are easily handled), we obtain the diagrams of closed alternating 3-braids and the
(p,q,r,s)- pretzel diagrams. By direct calculation of P we saw in [St2] that if min(p,q,r,s) ≥ 2, then MW F ≥ 4, and
that otherwise the pretzel link has braid index 3. ✷
The case of 4-braids is now not too much more difﬁcult.
Theorem 6.2 Let L be a prime non-split alternating link. The following 3 conditions are equivalent:
