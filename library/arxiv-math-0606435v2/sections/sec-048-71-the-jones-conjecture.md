---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-048-71-the-jones-conjecture
section_title: "The Jones conjecture"
section_number: 7.1
pages: 42-43
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
There is a conjecture, often attributed to Jones (who specul ated on it at least for knots and in it its weaker form, as
given below; see 357 l.-6 of his paper), stating that a minimal string braid representation has a unique exponent sum.
Conjecture 7.1 (Jones’s conjecture)
1) (weaker version) If β,β′ ∈ Bn satisfy ˆβ = ˆβ′ = L and n = b(L), then [β] = [β′] =: wmin(L).
2) (stronger version) Part 1 holds, and if β′′ ∈ B′
n for n′ > n has ˆβ′′ = L, then
⏐⏐[β′′] − wmin(L)
⏐⏐ ≤ n′ − n .(44)
It was observed in [St3] that counterexamples to the conject ure would make MWF and all of its cabled versions
unsharp. (In [St3] the weaker version was focussed on, but th e same arguments address the stronger version too.)
Thus, for example, corollary 6.8 can also be regarded as a par tial solution to Jones’s conjecture. Similarly, the work
in §5.1 shows:
Corollary 7.1 If a link L is the closure of a positive braid, andb(L) ≤ 4, then the strong Jones conjecture is true forL.
Proof. We use theorem 5.1, with the remark that the exceptional braid words therein were shown to have braid index
4 using the 2-cabled MWF. ✷
For 3-braids the weaker version was known to be true again fro m Birman-Menasco’s classiﬁcation result. We will
show now the stronger version, as a consequence of the descri ption in [St2] of 3-braid links with unsharp MWF
inequality (and thus with a much simpler proof than appealing to Birman-Menasco). See also remark 7.6.
Theorem 7.1 The stronger version of Jones’s conjecture holds for 3-braid links.
Convention. The letter ∆, with an integer subscript n, is used in §7.1, in deviation from other sections, exclusively for
the half-twist braid on n strings, and not for the Alexander polynomial. (The Alexander polynomial will not appear in
§7.1.)
Proof of theorem 7.1. As explained, it sufﬁces to deal only with the 3-braid links o f unsharp MWF inequality. In
[St2] these links were described fully. If µ = σ6a±1
1 σ∓1
2 , then for the Birman dual β = µ∗ of µ (see deﬁnition 4.1) we
have ˆµ∗ ⁄= ˆµ when 6a ± 1 > 6, but K = ˆβ has the skein polynomial of the (2,6a ± 1)-torus knot ˆµ. In [St2] is was
proved that these knots K form the full list of 3-braid links with unsharp MWF inequality.
Consider ﬁrst the knots K = ˆβ with β = µ∗ for µ = σ6a+1
1 σ−1
2 and a > 0. It is easy to bring β into Xu’s normal form,
and to observe that it has exactly one negative band. This exh ibits a Seifert ribbon (see [Ru]) of smaller genus than
g(K), i.e. gs(K) < g(K) (see also the proof of theorem 1.1). Now from Xu’s form one see s wmin(K) = [β] = 2g(K).
Take this for a moment as a deﬁnition ofwmin(K); this writing will be justiﬁed when we show that the writhe isunique.
(One could also quote Birman-Menasco here, but the complexity of their argument is unnecessary.) So
1 − χs(L) < wmin(L) .(45)
Using (13), we see that if (44) is violated for some β′′ ∈ Bn′, then [β′′] = wmin(L) + 2 + (n′ − 3). However, by the
Rudolph-Bennequin inequality [Ru2] (see also [St7]), we would have then
1 − χs(L) ≥ [β′′] − n′ + 1 = wmin(L) ,
