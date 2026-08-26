---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-027-42-jones-polynomial-19
section_title: "Jones polynomial 19"
section_number: 4.2
pages: 19-20
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
For the proof of theorem 4.2 we use the previous work in [St2] (that in particular answered Birman’s question) on the
skein polynomial. We apply again the result in [St2] that max degz P = 1 − χ for closed 3-braids. As in that paper, we
distinguish the cases of band-positive, band-negative 3-braids, and such of Xu’s formL−1R.
By the Morton-Williams-Franks inequalities (13), a 3-braid β of exponent sum (writhe)[β] has v-degrees of P in [β]−2
we call left degree, [β] we call middle degree and [β] +2 we call right degree. The terms of [P]zk for some k in these
degrees will be called left, middle and right terms1.
Lemma 4.4
(a) If β is band-positive, then maxcf zP has v-terms in the left degree and possibly in the middle degree. I f β is band-
negative, maxcf zP has v-terms in the right degree and possibly in the middle degree. In either situation a term in the
middle degree occurs if and only if ˆβ is not ﬁbered.
(b) If β is L−1R then maxcf zP has v-terms in the middle degree only.
In both cases all non-zero occurring coefﬁcients are ±1.
Proof. In (a) we prove only the ﬁrst claim (the second claim is analog ous). Let χ = χ(ˆβ). Since mindeg l P ≤
maxdeg z P = 1 − χ and 1 − χ = [β] − 2 ≥ mindeg l P by MWF, we have mindegl P = maxdeg z P, and then (17) implies
that maxcf zP has a v-term in the left degree, with coefﬁcient ±1. From [St2, Theorem 3] we have then that it has
no right-degree term, and that if it has a middle-degree term , the coefﬁcient is ±1. Now the previous work and the
substitution v = 1, z = t1/ 2 − t−1/ 2 for ∆ in (4) easily show that the middle term occurs if and only if ˆβ is not ﬁbered.
Now consider (b). If maxcf zP has a left-degree term, then using the substitution (17), we saw that β is band-positive.
Otherwise, [β] < 3 − χ, so the contribution of the coefﬁcient of z1−χv[β]−2 in (17), which is not cancelled, is not in
degree 0. Analogously one argues if maxcf zP has a right-degree term. ✷
Note that keeping track of [β] and distinguishing between left and middle term is importan t here. By remark 3.1, we
have links with equal polynomials such that the left term of the one is the middle term of the other.
Lemma 4.5 (a) If β is L−1R and L has exponent sum [L] > 1, then [P]z−1−χ has a left-degree term, and the coefﬁcient
is ±1.
(b) If [L] = 1 and [P]z−1−χ has a left-degree term, then the coefﬁcient is ±2.
The two analogous statements hold replacing L by R and left-degree term by right-degree term.
Proof. We proved already that maxcf zP has only a middle-degree term. So it must remain under the sub stitution of
(17) if and only if [β] = 1 − χ. The cases (a) and (b) occur when this term must be cancelled, and complemented to 1,
respectively. ✷
Proof of theorem 4.2. The statements follow mainly by putting together the last tw o lemmas and looking in which
degrees the non-cancelling contributions of the coefﬁcients of P occur under the substitution (5).
If part (a) of lemma 4.4 applies, we established already (in theorem 1.1) that the positive band form of β is equivalent
to the strong quasi-positivity of ˆβ. In this case mindeg V comes from the left-degree term in maxdeg z P. If ˆβ is
not ﬁbered, then [P]z−1−χ must have a right-degree term (with coefﬁcient ±1) to cancel the middle-degree term of
maxdeg z P under (17).
If part (b) of lemma 4.4 applies, we use the further informati on of lemma 4.5. In case (a) of lemma 4.5, the left and
right terms in [P]z−1−χ determine the degrees and edge coefﬁcients of V.
In case (b) of lemma 4.5, the maximal term in V comes from the right-degree term in [P]z−1−χ. A coefﬁcient in
t(−1−χ)/ 2 may come only from a left-degree term in [P]z−1−χ, which, if occurring, is with coefﬁcient ±2. ✷
This proof underscores the signiﬁcance of (5) as a tool for st udying the Jones polynomial. So far it seems to have
been useful just for calculating speciﬁc Jones polynomials from P. In §6 we will see further results that come out of
considering this substitution.
We note the following equalities that follow from the proof of theorem 4.2. These will be needed in the study of the Q
polynomial, and are also helpful for corollary 4.8.
1Note that here the brackets for polynomials and for braids have a completely different meaning.
20 4 Polynomial invariants
Lemma 4.6 If β is a not strongly quasi-signed 3-braid of exponent sum e and V, χ the Jones polynomial resp. Euler
characteristic of its closure, then
maxdeg V − e = 1 − χ
2 + 1(21)
mindeg V − e = − 1 − χ
2 − 1(22)
Exceptions are (22) if β is strongly almost quasi-positive, and (21) if β is strongly almost quasi-negative. ✷
Proof of corollary 4.8. Depending on whether a 3-braid representation β is strongly quasi-signed, almost quasi-
signed, or none of both, V determines e = [β] via χ(ˆβ) and/or (21) or (22). With V and e, one can recover the trace of
the Burau matrix ψ 2(β), and from that also P(ˆβ) (see [B] or (58) below). Again, if mindeg V · maxdeg V ≤ 0, then the
options that β is strongly quasi-signed or almost quasi-signed are ruled out easily. ✷
