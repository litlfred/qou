---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-029-43-q-polynomial-21
section_title: "Q polynomial 21"
section_number: 4.3
pages: 21-23
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Proposition 4.2 If K is a strongly quasi-positive 3-braid knot, then v2(K) ≥ g(K).
Note that in [St7] we proved the same inequality for a general positive knot. Since the pretzel knots with trivial
Alexander polynomial are strongly quasi-positive, nothin g like this holds for a general strongly quasi-positive knot ,
though.
We need some preparations. Let us ﬁrst ﬁx a convention. We num ber braid strands by 1,2,3 from left to right in the
bottom of the braid by and compose words from bottom to top. We propagate strand number through the crossings.
In particular strand( number)s may appear permuted in the mi ddle or on top of the braid. To refer to the ordering of
the strands with regard ot the local position in the braid dia gram, we speak of left, middle and right strand. So, for
example, if strands 1 and 2 enter below aσ1 (strand 1 as left strand and strand 2 as middle strand), then they exit above
in the order 2 1 (strand 2 as left strand and strand 1 as middle strand).
Let for a (not necessarily pure, and not closed) braid word th e linking numbers of strand i, j numbered as explained
above be the sum of the writhes of all crossings these two strands pass. (Note that for links this differs by the additional
factor 1/2, which is not relevant, though.)
Lemma 4.7 Let β be a strongly quasi-positive 3-braid word (not necessarily pure, and not closed). Then the linking
numbers li j between pairs (i, j) of strands satisfy l13 + l23 > 0, unless β is split.
Proof. The sum of writhes of crossings a strand passes through each o f σ1,2,3 is non-negative. So l13 + l23 ≥ 0. If
l13 + l23 = 0, then strand 3 passes only from below as left or middle strand into a σ3 = σ−1
1 σ2σ1. But since it starts (at
the bottom of the braid) as a rightmost strand, this means that is passes no crossing, so β is split. ✷
We prove proposition 4.2 by induction on the length of the positive word in σ1,2,3. Assume β is written as such a word.
We can w.l.o.g. cyclically permute the indices.
Lemma 4.8 If ˆβ is a strongly quasi-positive 3-braid, then a positive word β can be chosen so that it contains a non-
trivial syllable, unless β is a power of [123]. In particular, it is always possible if ˆβ is a knot, or a ﬁbered link.
Proof. Choose Xu’s form. It is [12]kβ′, where k ≥ 0 and β′ has cyclically non-decreasing indices. This word β has
a non-trivial syllable up to cyclic permutations of the lett ers, unless β′ is a power of [123]. In this case, if k > 0, we
apply a YB relation at the initial 121 in β, and are done. ✷
Proof of proposition 4.2. Let ˆβ be a knot. We can w.l.o.g. now assume β is written as a word with a non-trivial
syllable s. Now we apply the skein relation of ∆ at a letter of s. Let K = K,K−,K0 be the skein triple, and β±,0 the
corresponding braids. Also we can cyclically permute the indices in β±,0. We choose them so that the strand ﬁxed by
the permutation of β0 is number 3. We know from the skein relation of ∆ that v2(K) − v2(K−) = lk(L,M) where L,M
are the components of K0. Now that linking number is positive by lemma 4.7 (unless β0 is a split braid, but this is
impossible because s is non-trivial). By induction on g(K), the claim of proposition 4.2 follows. ✷
Proof of proposition 4.1. We distinguish three cases depending on the number of components of ˆβ.
Case 1. 1 component. In this case Q′(−2), by Kanenobu’s formula (23), is a multiple of Casson’s invariant v2. The
claim we wish to show then is implied by the estimate in proposition 4.2.
Case 2. 2 components. In this case Kanenobu’s formula involves only the square of the linking number of both
components K,L of the closure link of β and v2 of the 2-string subbraid component K. Looking at Xu’s normal
form, we see that if β is a strongly quasi-positive 3-braid, then writing β as a word in σ1,2,3, and then expanding
σ3 = σ−1
1 σ2σ1, we obtain a word in σ1,2 of some length c with at most c/ 5 negative letters. Since thus β has at most
c/ 5 negative crossings, it is easy to see that not both v2(K) and lk(K,L) can be zero, and one grows unboundedly
when c grows. So we are done.
Case 3. 3 components. In this case Kanenobu’s formula (23) reduces to the square sum of the linking number of pairs
components. Let l12,l13,l23 be these linking numbers. Again it is clear that not all of l12,l13,l23 = 0, and that when
l12 + l13 + l23 ≥ 2c/ 5 grows unboundedly, then so will l2
12 + l2
13 + l2
23, so again we are done. ✷
Now we move on to settle the remaining cases in theorem 4.3. Here the tools differ considerably. Beside the study of
Xu’s form, we need the help of the following theorem, proved in [St4].
22 4 Polynomial invariants
Theorem 4.5 Any 3-braid is up to conjugacy A-adequate or B-adequate.
We proved also the following
Theorem 4.6 A 3-braid word is B-adequate if and only if it is (a) a negative word, or (b) it con tains no [121] as
subword, and negative entries in the Schreier vector appear isolated. (That is, in cyclic order they are preceded and
followed by a positive entry.)
Using this criterion we prove now
Lemma 4.9 Assume β is strongly ≤ 2-almost positive and of exponent sum e ≥ 0. Then β is B-adequate.
Proof. If β is strongly quasi-positive or almost strongly quasi-positive, then it is of Xu’s formL−1R where L is a single
letter. By direct observation we can verify that when permut ing indices cyclicly properly and writing out σ3 in σ1,2,
then the resulting word has no [121] subword, and negative entries in the Schreier vector appear isolated. (In case of
[(312)k31 − 2], we must cancel 2 crossings ﬁrst.)
If β is 2-almost strongly quasi-positive, then then it is of Xu’s form L−1R where L has 2 letters. We can assume that
L = [12] or L = [12], then we write down the subword of L−1R consisting of the ﬁrst and last letters of R and L (herein
k ≥ 1):
[[23] . . .33 − 2 − 1] [[ 23] . . .22 − 1 − 1]
[[23] . . .23 − 2 − 1] [[ 23] . . .31k2 − 1 − 1]
[[23] . . .31k − 2 − 1] [[ 23] . . .33 − 1 − 1]
[[23] . . .23 − 1 − 1]
(Here ‘[23]’ means as in§2.4 that the word is to begin with ‘2’ or ‘3’.) The reductions and B-adequacy test are done
case-by-case. ✷
Using the formulas in §2.3, we prove
Lemma 4.10 If L = ˆβ is a link, which is the closure of an A-semiadequate 3-braid β, and V0V1 = −1, then V0V2 = 1
or 2.
Proof. By [St4] a A-semiadequate 3 braid is either positive, in which case V1 = 0, or has no [−1 − 2 − 1] and positive
entries are isolated in the Schreier vector. In [St4] we described the words for latter type which have V1 = 0. They are
(up to braid relations and cyclic letter permutations) of the form1
[1−22−21−2 . . .1−22−11p2−1] .
Analogously to that study, we can see that if V0V1 = −1, then β has a word which is obtained from the above type
by replacing some 1 −2 by 1−k for k ≥ 3. The intertwining graph of the A-state is a path (all vertices have valence 2,
except two of valence 1), so χ(IG) = 1. We have △ = 1 if k = 3, and otherwise △ = 0. So by theorem 2.1, we have
V0V2 = 1 for k = 3, and V0V2 = 2 otherwise. ✷
To explain what such a property has to do with Q, now we must introduce J. Murakami’s formula [Mr]. (See also
Kanenobu [K, Theorem 2].)
Let i = √−1, u = √−t and x = u + u−1. Let further2 for a braid β of exponent sum e,
χ(β,t) = ieu−2eVˆβ(t) +u−e(x2 − 2) .(24)
Then Murakami’s formula is
1Note that these are exactly the 3-braids which are reducible in the terminology of dynamic properties; this reducibilit y has nothing to do,
though, with the reducibility in Markov’s theorem.
2Note that V is here what is written as J, and not V , in [K].
