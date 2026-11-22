---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-023-516-4-braids
section_title: "4-braids"
section_number: 5.1.6
pages: 33-35
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
4-braids
If some mountain is not of height 3, or > 2 valleys of depth 1 exist, then we are done as before (see §5.1.3).
So the maximal subword is of the form 1,2,3,(2!,3)p,2,1,1,2,3,(2!,3)n,2,1, and the non-maximal subword is a
single σ1
1. We separate the summit syllables and their letters by the summit syllables of index 1 into a left and right
plateau. Assume w.l.o.g. the (non-summit) σ1
1 is in the left plateau. The word ‘in’ is to mean that in cyclic order of
the syllables of β the syllable σ1
1 can be written to occur just before or after a syllable with index n−1 that belongs to
the left plateau. This means that we can write β as
βl,m,n = [12.3(223)n1(223)m2..1123(223)l21]
(36)
with n,m,l ≥0, or some of its extensions. Note that MWF will be monotonous in m,n,l, i.e. MWF(βl,m,n+1) ≥
MWF(βl,m,n) etc. Using symmetry assume n ≥m.
One can check already at this stage that such words are not B-adequate. So we obtain corollary 5.1, and for the proof
of theorem 1.3 the rest of the argument here can be replaced by the application of theorem 4.5. Note that B-adequacy
is invariant under isotopy preserving writhe and crossing number, so any other positive 4-braid word giving the same
link is not B-adequate either.
If n +l > 0, then the 2-index syllable 2.. in (36) must be trivial. Otherwise remove all 2! in (2!,3)m (if any), and split
two loops as explained after (34). The ‘2!’ in (2!,3)l or (2!,3)n remain, and so MWF = 4. With a similar argument
we see that if m+l > 0, then the 2-index syllable 2. is trivial.
We distinguish 3 cases depending on whether these arguments apply or not.
Case 1. Both non-triviality arguments apply. So we have a family of words βl,m,n = [123(223)n1(223)m21123(223)l21]
with n,m > 0, or l > 0 and their extensions, and both 2.. and 2. are trivial.
Case 1.1. l = 0. We assumed n,m > 0, and already for n = m = 1, the word [12322312232112321],we have MWF = 4.
Case 1.2. l > 0.
Case 1.2.1. m = n = 0. These are extensions of [1231211123(223)l21], and the admissibility is found to be:
[1ˆ2ˆ31ˆ21123(223)l21].
The two letters ‘2’ in the left plateau cannot be doubled ([123122112322321], [122312112322321]), neither the ‘3’
([123132112322321]), since MWF = 4 already for l = 1.
Without extension, l = 1 ([123121112322321]) and l = 3 ([123121112322322322321]) reduce.
So we ﬁnd that
[12312112∗3[23] + 2 ∗1] reduce. (Recall that, while ‘2∗’ in a braid word should mean at least one letter ‘2’, the
term ‘[23]+’ should mean a possibly empty sequence of letters ‘2’ and ‘3’. We distinguish braid words from index
sequences by not putting commas between the numbers.)
Case 1.2.2. m + n > 0; this reduces to the case of m = n = 0 with some of the twos or the three in the left plateau
doubled, where we found MWF = 4.
Case 2. In the case one of the non-triviality conditions on 2.. and 2. does not apply, we have 123(223)n12112321 with
n > 0 and its extensions. (Now the right plateau is a mountain.)
The case n = 3 ([123223223223121112321]) simpliﬁes.
[122332232232232231211222321] simpliﬁes.
However, MWF([123223122112321])= 4, so the right 2-index syllable in the left plateau (2.. in (36)) must be trivial.
The right 2 and the 3 in the right plateau must be trivial:
[1232231211123221],
[1232231211123321] have MWF = 4.
But the left ‘2’ of the left and right plateau may not be trivial: [12223223223223121112222321] has MWF = 3.
[122232232232231211122222321] simpliﬁes.
So [12 ∗[23]+312112∗321] simpliﬁes.
We arrive at the form [123(223)n1ˆ2112ˆ3ˆ21].
34
5
Positivity of 3-braid links
Case 3. In case both non-triviality conditions do not apply, we have [12312112321] and its extensions. (So both
plateaus are mountains.)
Since non-triviality is nonetheless possible, we may have non-trivial 2-index syllables in the left plateau. We distin-
guish three cases again according to whether 2.. and 2. are trivial or not.
Case 3.1. Both 2-index syllables are trivial: [12312112321].
By direct check:
[123312112321] has MWF = 3,
[123121122321] has MWF = 3,
[123121123321] has MWF = 3,
[123121123221] has MWF = 3.
[12312112233221] has MWF = 3,
[123312112233221] has MWF = 4.
So one can extend the right mountain’s ‘2’s and one of the left or right mountain’s ‘3’s, but not both ‘3’s.
[123121122233221] reduces,
[123312112223221] reduces,
[1233121122233221] has MWF = 4.
So a reducing check is to be made on [11 ∗231211 ∗22∗3∗22∗].
[123121112233221] reduces,
[123121112222333322221] reduces,
[1233312111222322221] reduces.
Case 3.2. One 2-index syllable is non-trivial. This is the word [123122112321],with MWF = 3 (the case [122312112321]
is symmetric).
We have the following extensions:
[1233122112321] has MWF = 3 (and reduces),
[1231221122321] has MWF = 4,
[1231221123221] has MWF = 3 (and reduces),
[1231221123321] has MWF = 3 (and reduces).
The following combined extensions are to check: [12331221123321] has MWF = 4,
[12331221122321] has MWF = 4,
[12312211223321] has MWF = 4.
Thus we are left to deal with [1233 ∗122 ∗112321],
[123122 ∗112322∗1],
[123122 ∗11233∗21],
and check that they all reduce:
[12333312222112321] reduces,
[12312222112322221] reduces,
[12312222112333321] reduces.
Case 3.3. Both 2-index syllables are non-trivial: [1223122112321]. This is a braid word β0 for 139465. We have the
following extensions:
[12233122112321] has MWF = 3,
[12231221122321] has MWF = 4,
[12231221123221] has MWF = 4,
[12231221123321] has MWF = 3.
