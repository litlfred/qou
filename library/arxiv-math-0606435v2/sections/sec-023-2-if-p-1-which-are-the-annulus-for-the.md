---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-023-2-if-p-1-which-are-the-annulus-for-the
section_title: "(if p > 1), which are the annulus for the"
section_number: 2
pages: 13-14
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
reverse (2,4)-torus link, and the ﬁber of the (2,2,−2)-pretzel link. ✷
3.3. Fiberedness
For the rest of the paper we normalize ∆ so that ∆(1) = 1 and ∆(t) = ∆(1/ t).
Theorem 3.2 Let L be a strongly quasi-positive 3-braid link. Then the following are equivalent:
1) L’s minimal genus surface is a Hopf plumbing,
2) L’s minimal genus surface is a ﬁber surface,
3) maxdeg ∆(L) = 1 − χ(L) and maxcf ∆(L) = ±1,
4) L’s Xu normal form isnot R, with syllable length of R divisible by 3. In other words, the Xu normal form is not
an extension (in the sense of deﬁnition 2.1) of [(123)k] for k > 0.
5) Some minimal band form of L contains σk
1σl
2σm
1 or σk
2σl
1σm
2 as subword for k,l,m > 0, or is σk
1σl
2.
Proof. (1) =⇒ (2) =⇒ (3) are clear.
(5) =⇒ (1). Assume after deplumbing, all letters occur in single power , and up to conjugacy the word starts with
σ1σ2σ1 or σ2σ1σ2. By adjusting one of the two, we can have a σ2
1 or σ2
2 if the next letter is σ1 or σ2. In that case we
deplumb a Hopf band. If the next letter is σ3, then we have σ1σ2σ1σ3 = σ1σ2
2σ1, can can also deplumb a Hopf band.
Then we reduce the surface for that of σ1σ2σ1 which is the Hopf band.
(3) =⇒ (4). We prove the contrary. Assume(4) does not hold. Band-positive surfaces are always of minimalgenus, so
that the properties we investigate are invariant under Hopf(de)plumbings. Under applying skein relations at non-trivial
syllables we are left with powers of σ1σ2σ3. Apply the skein relation for ∆ at the last band. Then β− and β0 are both
of minimal length. We already proved, in (5) ⇒ (1), that β0 is ﬁbered, so maxdeg ∆ = 1 − χ(β0) and maxcf ∆ = ±1.
The same holds for β− by [St2, proposition 2], since β− is of Xu’s minimal form L−1R and is not positive. So the
terms in degree 1 − χ(β) of ∆(β) either cancel, or give ±2.
(4) =⇒ (5). We prove the contrary. Assume (5) does not hold. If we do not have a word β = R in Xu’s form of length
divisible by 3, another option would be to have a word with cyclically decreasing indices. But note that [321] = [121]
is the Hopf band, while [321321] = [211211] contains a 121, too, and so we are done. Otherwise the index ar ray of
the syllables of β must contain the same entry with distance 2, and such a word is conjugate to the ones excluded. ✷
14 3 Xu’s form and Seifert surfaces
Theorem 3.3 Any closed braid of Xu’s formL−1R is ﬁbered.
The proof uses some work of Hirasawa-Murasugi. A consequenc e of their result is the following lemma, which we
require. It is proved in appendix A.1.
Lemma 3.1 The links Lk, given by the closed 3-braids [(123)k − 2] for k > 0, are ﬁbered.
Proof of theorem 3.3. We use induction on the length of L−1R and for ﬁxed length on the exponent sum. Under
Hopf deplumbings assume all syllables in L and R are trivial. Assume up to mirroring that L is not shorter than R.
Permute by conjugacy R to the left, and permute the indices so that L starts with −3.
The following transformations also offer a Hopf deplumbing
1 − 3 − 2 − 1 → −21 − 2 − 1 → −2 − 2 − 12 → −2 − 12
and
12 − 3 → −211
These reductions fail both if either L and R have length at most 2, or R has length 1. (Remember L is not shorter
than R.) In former case one checks directly that one has a disk, Hopf band or connected sum of two Hopf bands. We
consider latter case.
By conjugacy permute the indices so that R = 1; also assume L has length at least 3. If L starts and ends with −2 then
we do
1 − 2 − 1 . . .− 2 → −23 − 1 . . .− 2 → 3 − 1 . . .− 2 − 2
(where the right transformation is a conjugacy) and deplumb a Hopf band. If L starts with −3 then we transform as
before
1 − 3 − 2 − 1 → −21 − 2 − 1 → −2 − 2 − 1 − 2
and deplumb a Hopf band. So L starts with −2 and ends on −3. Then the mirror image of β is up to conjugacy of the
form [(123)k − 2] = [(1221)k(−2)k+1], which we dealt with in the lemma before. ✷
Combinedly, we obtain
Corollary 3.1 Let W be a 3-braid link. Then the following are equivalent:
1) W is ﬁbered,
2) maxdeg ∆(W ) = 1 − χ(W) and maxcf ∆(W ) = ±1,
3) W’s Xu form is not of the typeL−1 or R, with syllable length of L or R divisible by 3. ✷
Example 3.1 The routine veriﬁcation, with Mikami Hirasawa, of the table s in [HT] for ﬁbered knots, has shown
