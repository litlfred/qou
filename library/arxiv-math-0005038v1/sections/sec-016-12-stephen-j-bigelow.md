---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-016-12-stephen-j-bigelow
section_title: "STEPHEN J. BIGELOW"
section_number: 12
pages: 12-12
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
which lies entirely in the closed lower half plane such that the endpoints of T (F )
are pj and pk. Such an Fj,k is uniquely determined up to isotopy by j and k, and
will be called a standard fork.
Let D′ ⊂ D be a disc containing Fj,k such that D′ ∩ P = {pj, pk}. Let C′ be the
set of unordered pairs of distinct points in D′. Let ˜C′ be the pre-image of C′ in ˜C.
We can consider vj,k as an element of H2( ˜C′), in which case it generates H2( ˜C′) as
a Λ-module. The surface ˜Σ 2(Fj,k ) lies in ˜C′, so must represent the homology class
λvj,k for some λ ∈ Λ. The value of λ does not depend on j and k. (Actually λ = 1,
but we will not need this fact.)
To write σi(vj,k ) in terms of basis vectors, we must ﬁnd a Λ-linear combination
of standard forks which represents the same element of H2( ˜C) as the fork σi(Fj,k ).
In the cases i ⁄∈ {j − 1, j, k − 1, k}, i = j ⁄= k, and i = k, there is no problem
because σi(Fj,k ) is a standard fork.
In the case i = j = k − 1, the fork σi(Fj,k ) has the same tine edge as Fj,k .
It follows that it represents the same surface in ˜C, up to a change in orientation
and application of a covering transformation. With some thought, o r by pairing
with an appropriate noodle, it is not hard to check that the correct formula is
σi(vj,k ) = −tq2vj,k .
The remaining cases are i = j − 1 and i = k − 1 ⁄= j. We will use the following
claim.
Claim 4.2. σi(vj,k ) is a linear combination of basis vectors vj′,k ′ which satisfy
j′, k′ ∈ {i, i + 1, j, k}.
Proof. There exists a disc D′ ⊂ D such that D′ contains σ(Fj,k ), D′ contains Fj′,k ′
for all j′, k′ ∈ { i, i + 1, j, k} with j′ < k ′, and D′ ∩ P = {pi, pi+1, pj, pk}. Let C′
be the set of unordered pairs of distinct points in D′. Let ˜C′ be the pre-image of
C′ in ˜C. Then H2( ˜C′) is a free Λ-module with basis consisting of all vj′,k ′ with
j′, k′ ∈ { i, i + 1, j, k} and j′ < k ′. But σ(vj,k ) can be considered as an element of
H2( ˜C′), so must be a linear combination of these basis vectors.
In the case i = j − 1, this claim implies that σi(Fj,k ) represents the same element
of H2( ˜C) as some Λ-linear combination of the three standard forks Fi,j , Fi,k , and
Fj,k . By pairing with some appropriate noodles it is not hard to check that the
correct linear combination is as stated in Theorem 4.1. Similar methods can be used
to verify Theorem 4.1 in the last remaining case, i = k − 1 ⁄= j. This completes the
proof of Theorem 4.1.
We conclude with some remarks on the BMW representation of braid g roups, de-
ﬁned independently by Birman and Wenzl in [BW89], and by Murakami in [M ur87].
