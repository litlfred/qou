---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-024-22-jianqiang-zhao
section_title: "Jianqiang Zhao"
section_number: 22
pages: 22-24
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
N 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
δ 1 1 1 1 1 2 2 3 2 3 3 5 3 6 4 5 4
i 0 0 0 0 0 1 1 1 3 3 5 3 8 6 10 6
k 0 0 0 0 1 0 2 0 0 0 5 0 7 0 0 0
δ 2 0 0 1 1 2 2 4 3 6 5 10 5 14 9 14 10
sr 0 0 1 1 2 2 4 4 6 6 10 8 14 12 16 16
D 1 2 4 4 9 8 16 9 16 15 36 15 49 24 35 25
SR 1 2 4 4 8 8 14 10 16 16 31 18 42 27 37 31
d 1 2 4 4 8 8 14 9 16 15 31 15 42 24 35 25
N 17 18 19 20 21 22 23 24 25 26 27 28 29
δ1 8 4 9 5 7 6 11 5 10 7 9 7 14
i 16 6 21 10 21 15 33 10 40 21 36 21 56
k 12 0 15 0 0 0 22 0 5 0 0 0 35
δ2 24 9 30 14 27 20 44 14 50 27 45 27 70
sr 24 18 30 24 32 30 44 32 50 42 54 48 70
D 81 24 100 35 63 48 144 35 121 63 100 63 225
SR 69 33 85 45 68 58 122 53 116 78 109 84 190
d 69 24 85 35 63 48 122 35 116 63 100 63 190
N 30 31 32 33 34 35 36 37 38 39 40 41
δ 1 6 15 8 11 9 13 7 18 10 13 9 20
i 15 65 28 55 36 78 21 96 45 78 36 120
k 0 40 0 0 0 0 0 57 0 0 0 70
δ 2 19 80 36 65 44 90 27 114 54 90 44 140
sr 48 80 64 80 72 96 72 114 90 112 96 140
D 47 256 81 143 99 195 63 361 120 195 99 441
SR 76 216 109 158 127 201 108 304 156 217 151 371
d 47 216 81 143 99 195 63 304 120 195 99 371
N 42 43 44 45 46 47 48 49 121 125 169
δ1 8 21 11 13 12 23 9 21 55 50 78
i 28 133 55 78 66 161 36 175 1155 1200 2288
k 0 77 0 0 0 92 0 35 330 25 715
δ2 34 154 65 90 77 184 44 196 1210 1250 2366
sr 96 154 120 144 132 184 128 196 1210 1250 2366
D 79 484 143 195 168 576 99 484 3136 2601 6241
SR 141 407 198 249 223 484 183 449 2806 2576 5526
d 79 407 143 195 168 484 99 449 2806 2576 5526
Table 1: Upper bounds of d(2, N) by the standard relations and [17, 5.25].
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 23
Since dim G−2,−1 = ϕ(N )/2 if N > 2 and 0 otherwise the dimension of the
degree two part of G is
δ2(N ) := dim G−2,−1 + dim G−2,−2 =
{
i(N ), if N = 1 or 2;
ϕ(N )/2 + i(N ), if N ≥ 3.
(41)
Let sr(N ) be the upper bound of δ2(N ) obtained by the standard relations.
This can be computed by the method described in [30, §2]. Let SR(N ) be the
upper bound of d(2, N) similarly obtained by the standard relations. In Table
1 we use MAPLE to provide the following data: k(N ), sr(N ), and SR(N ).
Then we can calculate δ1(N ), i(N ) and δ2(N ) by (39), (40) (41), respectively.
From (38) we can check the consistency by verifying
sr(N ) − δ2(N ) = SR(N ) − d(2, N) = SR(N ) − D(2, N) + k(N )
which gives the number of linearly independent non-standar d relations (as-
suming the conjecture in [17, 5.27(c)]). In Table 1 we provid e some computa-
tional data of the above quantities. To save space we write D = D(2, N) and
d = d(2, N).
Definition 8.1. We call the level N standard if either (i) N = 1 , 2 or 3, or
(ii) N is a prime power pn (p ≥ 5). Otherwise N is called non-standard.
Remark 8.2. We now make the following comments in the weight two case from
Table 1.
(a) When p ≥ 11 the vector space ker βp contains a subspace isomorphic to the
space of cusp forms of weight two on X1(p) which has dimension (p−5)(p−7)/24
(see [20, Lemma 2.3 & Theorem 7.8]). So it must contain anothe r piece which
has dimension ( p − 3)/2 since dim(ker βp) = ( p2 − 1)/24 by [30, (6)]. One may
wonder if this missing piece has any signiﬁcance in geometry and/or number
theory.
(b) If N is a 2-power or a 3-power then D(2, N) should be sharp. See Re-
mark 5.4.
(c) If N has at least two distinct prime factors then D(2, N) seems to be sharp,
though we don’t have any theory to support it.
(d) Suppose the conjecture in [17, 5.27(c)] is true. Then by [ 17, 5.27], (b)
and (c) is equivalent to saying that the kernel of βN is trivial if the level N is
non-standard. We believe this is also a necessary condition on N for βN to be
trivial.
(e) If the level N > 3 is standard then βN is unlikely to be injective. We con-
jecture that non-standard relation doesn’t exist (i.e., SR(N ) is sharp), though
for prime power levels we only have veriﬁed this for the ﬁrst f our prime square
levels N = 5 2, 72, 112, 132, and the ﬁrst cubic power level N = 5 3.
The equation dim βp = ( p2 − 1)/24 (see [30, (6)]) together with Theorem 8.6
conﬁrms Remark 8.2(e) for prime levels if we assume a variant of Grothendieck’s
period conjecture [17, 5.27(c)]. The next result partially conﬁrms Remark
8.2(e) in the case when the level is a prime square.
Documenta Mathematica 15 (2010) 1–34
