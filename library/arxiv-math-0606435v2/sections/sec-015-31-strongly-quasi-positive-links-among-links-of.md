---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-015-31-strongly-quasi-positive-links-among-links-of
section_title: "Strongly quasi-positive links among links of braid ind ex 3"
section_number: 3.1
pages: 11-12
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Theorem 1.1 follows relatively easily from the work in [St2], but it is a good starting point for the later more substantial
arguments basing on Xu’s form.
Proof of theorem 1.1. The inequalities of (13) for the v-degree of P applied on a positive band representation show
that, with P = P(L) and χ = χ(L),
mindeg v P ≥ 1 − χ.(16)
Because of [LM, proposition 21], which now says
P(v,v−1 − v) = 1 ,(17)
we have mindegl P ≤ maxdeg z P, and by [St2] maxdegz P = 1 − χ. So from (16) we obtain
mindeg l P = 1 − χ.(18)
It is known that the minimal degree term inz of the skein polynomial of an-component link is divisible by(v−v−1)n−1.
(In [Kn] in fact all occurring terms are classiﬁed.) So ifMW F(K) = 1, then K is a knot. Now, the identity (17) implies
that if MWF = 1 for some knot K, then P(K) = 1. For any non-trivial knot 1 − χ = 2g > 0, so for any non-trivial
strongly quasi-positive knot from (16) we have mindegv P > 0, and so P ⁄= 1.
So a strongly quasi-positive link cannot have P = 1, and always MW F ≥ 2. Therefore, when the braid index is 3, we
have MW F ∈ {2,3}. Then (18) and the inequalities (13) for the v-degree of P show that a 3-braid representation β has
exponent sum [β] = 3 − χ, unless MWF = 2 and [β] = 1 − χ.
In former case, we can ﬁnd a minimal genus band representatio n from β by Xu’s algorithm [Xu], and this represen-
tation must be positive. In latter case, we will have one nega tive band, and have Xu’s form L−1R. Here L and R are
positive words in the letters σ1,σ2,σ3 = σ2σ1σ−1
2 with σi followed by σi or σi mod 3+1 (as described in §2.5), and L is
a single letter.
W.l.o.g. assume L = σ3. If the ﬁrst or last letter in R is a σ3 then we can cancel two bands, and have a positive
representation. If some σ3 occurs in R, then we can write L−1R = σ−1
3 ασ3α′ where α,α′ are positive band words.
Such a representation is quasi-positive with a Seifert ribb on [Ru] of smaller genus. However, it is known that for
strongly quasi-positive links the genus and 4-genus coinci de (see for example [St]). If R has no σ3, then we have up
to cyclic letter permutation a braid of the form σk
1σl
2σ−1
1 σ−1
2 with k ≥ 0, l > 0. This braid is easily seen to reduce to (a
positive one on) two strands. ✷
Remark 3.1 It is not true that all 3-braids that have the skein polynomia l of (2,n)-torus links have positive 3-band
representations. Birman’s [B] construction (see deﬁnitio n 4.1 below) yields examples like 12 2037 in [HT] with one
negative band. This construction gives in fact all non-obvi ous 3-braid MW F = 2 examples, a circumstance shown in
[St4] by applying theorem 4.5 (and reportedly in previous unpublished work of El-Rifai). The result is explained and
used below in the proof of theorem 7.1.
12 3 Xu’s form and Seifert surfaces
