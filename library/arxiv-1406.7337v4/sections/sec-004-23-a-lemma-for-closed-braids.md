---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu"
section_id: sec-004-23-a-lemma-for-closed-braids
section_title: "A lemma for closed braids"
section_number: 2.3
pages: 5-9
source_pdf: 1406.7337v4 (1).pdf
source_sha256: 5bae8237742733b9
doc_brief: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and"
---
The main goal of this section is to produce a family of closed n-braids that satisﬁes the hypotheses of
Theorem 2.1. We will work within this family of braids throughout the rest of this paper. We begin with
necessary deﬁnitions.
Deﬁnition 2.5. Call two induced subwordsγ1 andγ2 of a braid wordβ∈Bn disjoint if the subwords share
no common letters when they are viewed as part of β. As an example, given the braid word
β =σ3
1σ−3
2 σ2
1σ−2
3 σ2σ3 =σ2
1(σ1σ−3
2 σ1)σ1(σ−2
3 σ2)σ3,
the subwords γ1 =σ1σ−3
2 σ1 and γ2 =σ−2
3 σ2 are disjoint induced subwords of β.
Deﬁnition 2.6. Call a subword γ of a braid word β∈ Bn complete if it contains, at some point, each of
the generators σ1,...,σ n−1 of Bn. It is important to note that the generators σ1,...,σ n−1 need not occur
in any particular order and that repetition of some or all of these generators is allowed.
Because the majority of the braids considered in this paper will satisfy the same set of assumptions, we
make the following deﬁnition.
Deﬁnition 2.7. Call a braid β∈Bn nice ifβ is cyclically reduced into syllables and β contains two disjoint
induced complete subwords.
Note that, in the case when n = 3, the condition that the 3-braid β =σr1
i σr2
j ··· σr2l−1
i σr2l
j ∈B3 is nice is
equivalent to the condition that σ1 andσ2 each occur at least twice nontrivially in the braid word β (which
is equivalent to the condition that l≥ 2).
We now deﬁne, in the following Main Lemma, the family of closed n-braids that we will consider for the
remainder of this paper.
Lemma 2.1 (The Main Lemma). LetD(K) =ˆβ denote the closure of a nice n-braidβ =σr1
m1··· σrl
ml∈Bn.
View D(K) as lying in an annular region of the plane and assume that β satisﬁes the conditions
(1) all negative exponents ri < 0 in β satisfy the stronger requirement that ri≤− 3;
(2a) when ri > 0 and mi = 1, we have that ri−1≤− 3, that ri+1≤− 3, and that mi−1 =mi+1 = 2;
(2b) when ri > 0 and 2≤ mi≤ n− 2, we have that ri−2≤− 3, that ri−1≤− 3, that ri+1≤− 3, that
ri+2≤− 3, and that {mi−2,m i−1} ={mi+1,m i+2} ={mi− 1,m i + 1}; and
(2c) when ri > 0 and mi =n− 1, we have that ri−1≤− 3, that ri+1≤− 3, and that mi−1 =mi+1 =n− 2.
Then we may categorize the all-A circles of HA into the following types:
• small inner circles that arise from negative exponents ri≤− 3 in the braid word β
• medium inner circles that arise from cyclically isolated positive syllables in the braid word β
• essential wandering circles that are essential in the annulus and have wandering that arises from adja-
cent negative syllables in adjacent generators in the braid word β
• non-essential wandering circles that are non-essential (contractible) in the annulus and have wandering
that arises from adjacent negative syllables in adjacent generators in the braid word β
• nonwandering circles that arise from the case when all syllables in the generator σ1 are positive or the
case when all syllables in the generator σn−1 are positive.
Furthermore, we have that K is a hyperbolic link and that D(K) is a connected, prime, A-adequate link
diagram that satisﬁes the TELC and contains t(D) ≥ 2(n− 1) twist regions.
5
Figure 5: An example of an isolated positive syllable σri
1 corresponding to a single medium inner circle (left), an
example of an isolated positive syllableσri
mi, where 2 ≤mi ≤n−2, corresponding to two medium inner circles (center),
and an example of a wandering circle portion coming from a negative subword σri
miσ
ri+1
mi+1 =σri+1
mi (σ−1
miσ−1
mi+1)σ
ri+1+1
mi+1
(right).
Remark 2.1. Condition (2a) of the above theorem requires that positive syllables in the generator σ1 are
cyclically neighbored on both sides by negative syllables in the generator σ2. Similarly, Condition (2c) of
the above theorem requires that positive syllables in the generator σn−1 are cyclically neighbored on both
sides by negative syllables in the generator σn−2. Condition (2b) of the above theorem requires that positive
syllables in the generator σi, where 2 ≤ i≤ n− 2, are cyclically neighbored on both sides by a pair of
negative syllables in the far commuting generators σi−1 and σi+1.
Note that Condition (2a), Condition (2b), and Condition (2c) are in a spirit similar to the condition that
positive syllables are cyclically neighbored on both sides by negative syllables in Stoimenow’s classiﬁcation
of A-adequate closed 3-braid diagrams (Proposition 2.1).
We will prove Lemma 2.1 through a series of sublemmas.
Sublemma 2.1. LetD(K) =ˆβ satisfy the assumptions of Lemma 2.1. Then, as described in the statement
of Lemma 2.1, we may categorize the all-A circles of HA into small inner circles, medium inner circles,
essential wandering circles, non-essential wandering circles, and nonwandering circles.
Proof. First, note that Condition (2a), Condition (2b), and Condition (2c) of Lemma 2.1 imply that β
cannot be positive. Because positive syllables of β are cyclically neighbored by negative syllables, we may
decompose β as β =N1 (in the case that β is a negative braid) or as β =P1N1··· PtNt, where Pi denotes
a positive syllable of β and Ni denotes a maximal length negative induced subword of β.
Small Inner Circles: Let σri
mi, where ri≤− 3, denote a negative syllable. Then, except for the additional
n−2 surrounding vertical line segments, the A-resolution of this syllable will look like the left side of Figure 3.
In particular, having ri≤− 3 implies the existence of at least two small inner circles.
Wandering Circles: Let σri
miσri+1
mi+1 =σri+1
mi (σ−1
miσ−1
mi+1)σri+1+1
mi+1 , where ri≤− 3 and ri+1≤− 3, denote a pair
of adjacent negative syllables.
Case 1: Suppose mi+1 =mi− 1 or mi+1 =mi + 1. Then the pair of adjacent negative syllables involve
adjacent generators ofBn. Consequently, the corresponding portion ofHA will resemble (up to reﬂection and
except for the additional surrounding vertical line segments) the right side of Figure 5. The key feature of
this ﬁgure is the fact that we see a portion of a wandering circle, where the wandering behavior corresponds
to the existence of the σ−1
miσ−1
mi+1 induced subword.
Case 2: Suppose |mi+1−mi| ≥2. In this case, the pair of adjacent negative syllables involve far
commuting generators of Bn. Then, except for the additional n− 4 surrounding vertical line segments, we
get that the A-resolution will look like two copies of the left side of Figure 3. Thus, we return to the case of
small inner circles.
6
Medium Inner Circles and Nonwandering Circles : Let σri
mi, whereri > 0, denote a positive syllable of β that
is cyclically neighbored on both sides by negative syllables as in Remark 2.1. Then the A-resolution of the
induced subword will resemble either the left side (up to reﬂection and except for the additional surrounding
vertical line segments) or the center (except for the additional surrounding vertical line segments) of Figure 5.
In particular, the existence of an isolated positive syllable corresponds to the existence of one or two medium
inner circles, one in the case of Condition (2a) and Condition (2c) and two in the case of Condition (2b).
Furthermore, a nonwandering circle will occur in HA precisely when all syllables in the generator σ1 are
positive (see the left side of Figure 5) or when all syllables in the generator σn−1 are positive (which would
give a reﬂection of the left side of Figure 5).
Note that we may classify the wandering circles in the annulus into essential and non-essential circles.
Since the A-resolutions of all portions of the closure of β =N1 andβ =P1N1··· PtNt have been considered
locally and since gluing such portions together joins wandering and potential nonwandering circle portions
together to form wandering and nonwandering circles, then we have the desired classiﬁcation of all-A circles.
Sublemma 2.2. Let D(K) = ˆβ satisfy the assumptions of Lemma 2.1. Then D(K) is connected, prime,
and contains t(D)≥ 2(n− 1) twist regions.
Proof. Recall that D(K) is connected if and only if the projection graph of D(K) is path-connected. Since
β∈ Bn contains a complete subword, then each generator of Bn (each of which corresponds to a crossing
ofD(K) between adjacent braid string portions) must occur at least once. This fact implies that the closed
n-braid diagram D(K) must be connected.
Sinceβ contains two disjoint complete subwords, then it must be that each of the generatorsσ1,...,σ n−1
of Bn must occur at least twice in (two distinct syllables of) the braid word. Since the syllables of the
cyclically reduced braid word β correspond to the twist regions of D(K), then we have thatt(D)≥ 2(n− 1).
Let C be a simple closed curve that intersects D(K) = ˆβ exactly twice (away from the crossings) and
contains crossings on both sides. To show that D(K) is prime, we need to show that such a curve C cannot
exist. Recall that D(K) lies in an annular region of the plane.
Case 1: Suppose C contains a point p outside of this annular region. Since C only intersects D(K) twice
and must start and end at p, then C must intersect D(K) twice in braid string position 1 or twice in braid
string position n. This cannot happen because the crossings corresponding to the occurrences of σ1 and
σn−1 preventC from being able to close up in a way that will contain crossings on both sides.
Case 2: Suppose C contains a point p between braid string positions i andi + 1 for some 1≤i≤n− 1. See
Figure 6. Since C only intersectsD(K) twice and must start and end atp, thenC must intersectD(K) twice
in braid string position i or twice in braid string position i + 1. Suppose, as in Figure 6, that C intersects
D(K) twice in braid string position i. The case for braid string position i + 1 is very similar. If i = 1, then
C contains a point outside of the annular region and we return to Case 1. Suppose 2 ≤i≤n− 1. Since β
contains two disjoint induced complete subwords, then the generator σi−1 and the generator σi must each
occur at least twice, once above p and once below p. These occurrences prevent C from being able to close
up in a way that will contain crossings on both sides. Thus, this case cannot occur.
Sublemma 2.3. LetD(K) =ˆβ satisfy the assumptions of Lemma 2.1. Then D(K) is A-adequate.
Proof. To prove that D(K) is A-adequate, we need to show that no A-segment of the all-A state HA joins
an all-A circle to itself. Note that positive syllables in β (which include the short twist regions of D(K))
A-resolve to give horizontal A-segments and that negative syllables inβ (which include the long twist regions
of D(K)) A-resolve to give vertical A-segments. Suppose, for a contradiction, that an A-segment joins an
all-A circle to itself.
7
p C
σi−1,σ i,σ i+1
i i + 1
σi−1,σ i,σ i+1
Figure 6: A simple closed curve C intersectingD(K) twice and containing a point p between braid string positions
i and i + 1. Each box in the ﬁgure represents the eventual occurrence of the generator σi, the generator σi−1 (if it
exists), and the generator σi+1 (if it exists).
Case 1: Suppose the A-segment is a vertical segment. Condition (1) (that negative exponents are at least
three in absolute value) implies that it is impossible for a vertical A-segment to join an all-A circle to itself.
This is because all vertical A-segments either join distinct small inner circles or join a small inner circle to
a medium inner circle or a wandering circle. (See the left side of Figure 3.)
Case 2: Suppose the A-segment is a horizontal segment. By Remark 2.1 and Figure 5, it can be seen that
it is impossible for a horizontal A-segment to join an all-A circle to itself. This is because all horizontal
A-segments join a medium inner circle either to another medium inner circle, to a wandering circle, or to a
nonwandering circle.
Sublemma 2.4. LetD(K) =ˆβ satisfy the assumptions of Lemma 2.1. Then D(K) satisﬁes the TELC.
Proof. LetC1 andC2 be two distinct all-A circles that share a pair of distinct A-segments, call them s1 and
s2. To prove that D(K) satisﬁes the TELC, we need to show that these A-segments correspond to crossings
from the same short twist region of D(K).
Case 1: Suppose one of s1 ands2 is a horizontal segment (that must come from a cyclically isolated positive
syllable of β). Then it is impossible for the other segment to be a vertical segment. This is because one of
C1 andC2, sayC1, must be a medium inner circle. This circle is adjacent, via horizontal A-segments, to the
second circle C2, which will either be another medium inner circle, a wandering circle, or a nonwandering
circle. By Condition (1), the circle C1 is also adjacent to small inner circles above and below. Consequently,
the second segment cannot be vertical. Thus, if one of the segments s1 and s2 is horizontal, then the other
segment must also be horizontal. Since the horizontal segments incident to the medium inner circle C1
necessarily belong to the same resolution of a short twist region of D(K), then the TELC is satisﬁed. (See
the left side and center of of Figure 5.)
Case 2: Suppose both s1 ands2 are vertical segments. Since all vertical A-segments either join distinct small
inner circles or join a small inner circle to a medium inner circle or a wandering circle, then one of C1 and
C2 must be a small inner circle. By Condition (1), it is impossible for a small inner circle to share more
than one A-segment with another all-A circle. (See the left side of Figure 3.) Therefore, this case cannot
occur.
We now combine all of the necessary ingredients in order to prove the Main Lemma.
8
Proof of Lemma 2.1 (The Main Lemma). By applying Sublemma 2.1, Sublemma 2.2, Sublemma 2.3, and
Sublemma 2.4, we get every conclusion of Lemma 2.1 except the hyperbolicity of K, which follows from
Theorem 2.1.
