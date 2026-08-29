---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-026-42-jones-polynomial-17
section_title: "Jones polynomial 17"
section_number: 4.2
pages: 17-19
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Corollary 4.3 If ∆ is the Alexander polynomial of a 3-braid link, then |maxcf ∆| ≤ maxdeg ∆ + 2. For a knot
|maxcf ∆| ≤ maxdeg ∆ + 1.
Proof. If |maxcf ∆| ≤ 2 then we are easily done. (∆ = ±2 cannot occur for a knot.) Otherwise we have up to mirroring
a strongly quasi-positive word β reducing to an even power of [123]. Now |maxcf ∆| counts non-trivial syllables, so
[β] = 3 − χ ≥ 2|maxcf ∆|, and −1 − χ = 2maxdeg ∆. For a knot the number of syllables with exponent ⁄= 2 is at least
2, so [β] − 2 ≥ 2|maxcf ∆|. ✷
Note in particular that the proof shows that |maxcf ∆| can be any given natural number, and how to ﬁnd the link
that realizes this number. We emphasize this here, because l ater we will prove a contrary statement in the case of
alternating links for every arbitrary braid index (see corollary 6.6).
Corollary 4.4 A 3-braid knot is ﬁbered if and only if maxcf ∆ = ±1.
Proof. It remains to explain why no 3-braid knot has maxcf ∆ = ±1 but maxdeg ∆ < 1 − χ. Latter condition would
imply that we have up to mirroring a strongly quasi-positive word β reducing to an even power of [123], and former
condition that β has only one non-trivial syllable. But [(123)2k] has 3-component closure, and making one syllable
non-trivial cannot give a knot. ✷
In particular, it is worth noting
Corollary 4.5 No non-trivial 3-braid knot has trivial Alexander polynomial. ✷
Again, the two 11 crossing knots immediately show that this is not true for 4-braids.
Example 4.2 We can also easily determine the 3-braid links for some small degree Alexander polynomials. For
example, we see that no other 3-braid knot has the polynomial of 31, 41 or 52. Similarly we can check that no 3-braid
knot has the polynomial of 942 and 949 (which shows that these knots have braid index 4), a fact we will derive in the
last section using entirely different representation theory arguments.
4.2. Jones polynomial
The control of the Jones polynomial on 3-braid links was the object of main attention in [B]. We can accomplish this
with a similar argument to ∆. The result we obtain can be conveniently described in our setting and is as follows:
Theorem 4.2 Let L be a non-split 3-braid link, and L = ˆβ with β ∈ B3. Then
spanV (L) ≤ 4 − χ(L) .(20)
Equality holds if and only if L is strongly quasi-signed (i.e. -positive or -negative, or e quivalently |[β]| = 3 − χ(L)),
and not ﬁbered. More speciﬁcally, the following holds:
1) If L is strongly quasi-positive, then mindeg V = 1 − χ
2 and mincf V = ±1 .
Analogously, if L is strongly quasi-negative, then maxdeg V = χ − 1
2 and maxcf V = ±1 .
2) If L is strongly quasi-positive and ﬁbered, then span V (L) ≤ 3 − χ(L) . If L is strongly quasi-positive and not
ﬁbered, then (20) is an equality and maxcf V = ±1. (The properties for strongly quasi-negative are analogous.)
3) If L is not strongly quasi-signed and |[β]| < 1 − χ(L), then
mincf V (L) = ±1 , maxcf V (L) = ±1 and span V (L) = 3 − χ(L) .
18 4 Polynomial invariants
4) If L is not strongly quasi-signed and [β] = 1 − χ(L), then
maxcf V (L) = ±1 and maxdeg V (L) = 5
2 − 3
2 χ(L) .
Moreover, mindeg V ≥ −1 − χ
2 , and if equality holds, then mincf V = ±2. (The case [β] = χ(L) − 1 is analo-
gous.)
Apart from solving Birman’s problem how to determine 3-brai ds with given Jones polynomial, theorem 4.2 easily
implies that no non-trivial 3-braid link has trivial (i.e. unlink) polynomial. We defer the discussion of the non-triviality
of the Jones polynomial to [St4], where we work in the much more general context of semiadequate links. In that paper
we will show that semiadequate links have non-trivial Jones polynomial. This result in fact motivated theorem 4.5,
which then provides a different conclusion about the non-triviality of the polynomial. A further application will be the
classiﬁcation of the 3-braid links with unsharp Morton-Williams-Franks inequality (mentioned in remark 3.1).
Corollary 4.6 For a given Jones polynomial V (actually the pair (mindeg V,maxdeg V ) is enough), there are at most
three values of χ(L) of a 3-braid link L with V (L) = V. If mindeg V · maxdeg V ≤ 0, then χ(L) is unique.
Proof. The theorem shows that the value of χ is determined by one of maxdeg V, mindeg V or spanV = maxdeg V −
mindeg V . In particular for a pair (mindeg V,maxdeg V ) there exist at most three values of χ of 3-braid links with a
Jones polynomial realizing this pair. If mindeg V · maxdeg V ≤ 0, then the options that a 3-braid β with V (ˆβ) = V is
strongly quasi-signed or almost quasi-signed are excluded (up to a few simple cases that can be checked directly), so
χ(L) is determined (unambiguously) by spanV. ✷
In particular, since 3-braid links of given χ are only ﬁnitely many, we have
Corollary 4.7 There are only ﬁnitely many closed 3-braids with the same Jon es polynomial, actually with the same
pair (mindeg V,maxdeg V ). ✷
For example, one easily sees that no 3-braid knot has the poly nomial of 942. Similarly, no other 3-braid knot has the
polynomial of the ﬁgure-8-knot (there is, however, a 4-braid knot with such polynomial, 11386).
That there are only ﬁnitely many closed 3-braids with the sam e skein polynomial was known from [St2]. For the
Jones polynomial one should note that inﬁnite families wereconstructed by Traczyk [Tr] if one allows polynomials up
to units. Traczyk’s examples show that for ﬁbered (strongly quasi-)positive links spanV may remain the same while
χ → −∞, so one cannot expect a full (lower) control on span V from χ. From these links, one obtains by connected
sum inﬁnite families with the same polynomial for 5-braids. (The status of 4-braids remains unclear.) Also Kanenobu
[K2] constructed ﬁnite families of 3-braids of any arbitrary size, so that our result is the maximal possible.
A question that surfaces naturally with these remarks in mind is
Question 4.1 Does for 3-braid links the Jones polynomial (or Alexander polynomial) determine the skein polynomial?
In other words, do any two 3-braid links with the same V (or ∆) have also equal P?
We have at least the following partial result, whose proof wepostpone after the proof of theorem 4.2.
Corollary 4.8 A given Jones polynomial V = V (L) is realized for 3-braid links L by at most three different skein
polynomials P(L). If mindeg V · maxdeg V ≤ 0, then V (L) determines P(L).
In the general case one cannot expect a positive answer to the above question. At least for links there is now the
method of [EKT] available, which should yield large familie s of links with the same Jones but different skein (or
Alexander) polynomial. For constructing families with the same Alexander (but different Jones or skein) polynomial,
further techniques are available, applicable also for knot s, like the non-faithfulness of the Burau representation (s ee
[Bi]) or tangle surgeries (see [Bl]).
