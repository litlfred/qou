---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-031-43-q-polynomial-25
section_title: "Q polynomial 25"
section_number: 4.3
pages: 25-26
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Then (27) becomes equivalent to
1 − χ
4 + e
4 > 1 .
So, assuming χ ≤ 0 and e ≤ 1 − χ, for (27) we are left to consider only (e,χ) = (0,−1), (0,−3), (1,0), (1,−2), or
(2,−1), which are trivial cases to check.
For (28) we must deal with A-adequate but not B-adequate braids with e ≥ −3 − χ, i.e. ≤ 3-almost strongly quasi-
positive braids. For ≤ 2-almost strongly quasi-positive braids we can use lemma 4. 9. While one may extend the
argument there to 3-almost strongly quasi-positive braids, it would require a longer case-by-case analysis. We provide
instead a different argument.
We try to modify the argument for proposition 4.1. In case ˆβ is a link of 2 or 3 components, we can argue again as
there, and are left with the cases e = 0,1 of 6 and 7 bands, which are easy to deal with.
So assume ˆβ is a knot. Now from (31), we have m3 = m1 + 1, so if still some of the ﬁrst two coefﬁcients of T1, T2
do not cancel, we have mindeg t Q1 ≤ m1 + 1/2, and are done. Otherwise again V1V0 = −1. So by the proof of lemma
4.10,
β = [1−k2−21−2 . . .1−22−11l2−1] ,
with k ≥ 3 and l ≥ 1. Since ˆβ is a knot, k and l are easily observed to be odd. Now a ≤ 3-almost positive word in Xu’s
form can be chosen, when written out as a word in σ1,2 of c letters, to have c− ≤ c/ 5 + 3 negative letters/crossings. If
we reduce the word by cancelling crossings, this inequality remains true.
We estimate the Casson invariantv2 of ˆβ using the Gauß diagram formula of Polyak-Viro (15). Let us put the basepoint
right after the group of l positive crossings (which of either strands is immaterial).
Now l is odd and the l positive crossings are pairwise linked, so their contribut ion to the Gauß diagram sum (15)
is, independently on the location of the basepoint, equal to v2(T2,l) = l2 − 1
8 , where T2,l is the (2,l)-torus knot. The
analogous claim is true for the group of k negative crossings.
If some of the positive crossings is linked with a negative cr ossing, it must be a negative crossing of a σ−1
2 . Now by
our choice of basepoint, in each syllable σ−2
2 only one of the two crossings gives a pair that contributes to (15), and
the contribution is always −1/ 2. Putting this together, we have
v2 ≥ l2 − 1
8 + k2 − 1
8 − c− − k + 2
4 · l · 1
2 .(32)
Assuming c ≥ 10 (the other cases are checked directly), we have
l ≥ 4c
5 − 3 ≥ c
5 + 3 ≥ c− = c − l .
So the r.h.s. in (32) is minimized for l ≥ 4c
5 − 3 when putting l = 4c
5 − 3. Then we have, with k ≥ 3 and c− = c − l,
the estimate
v2 ≥ 3c2
50 − 29c
40 + 11
4 ,
which is positive for c ≥ 10, and grows when c → ∞.
With this theorem 4.3 is proved. ✷
Remark 4.1 It is interesting whether maxdeg Q → ∞ also for the strongly quasi-positive braids, but in Murakam i’s
formula massive cancellations become possible and Q1 cannot be easily controlled. At least one can prove using
theorem 4.5 and some results of Thistlethwaite in [Th] that t here are only ﬁnitely many 3-braid links with given
maxdeg z F, where F is the Kauffman polynomial.
