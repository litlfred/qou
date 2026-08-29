---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu"
section_id: sec-005-24-diagrammatic-volume-bounds
section_title: "Diagrammatic volume bounds"
section_number: 2.4
pages: 9-11
source_pdf: 1406.7337v4 (1).pdf
source_sha256: 5bae8237742733b9
doc_brief: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and"
---
In this section, we apply Lemma 2.1 and Theorem 2.1 to produce diagrammatic volume bounds for the
complements of the closed n-braids considered in this paper. We now begin with a lemma for the case of
3-braids.
Lemma 2.2. Let D(K) = ˆβ denote the closure of a nice 3-braid β∈ B3. Furthermore, assume that the
positive syllables of β are cyclically neighbored on both sides by negative syllables. Then the all-A state HA
of D(K) satisﬁes precisely one of the following conditions:
(1) HA contains exactly one nonwandering circle and no wandering circles.
(2) HA contains exactly one wandering circle and no nonwandering circles.
Proof. A 3-braid β∈B3 is either alternating or nonalternating.
Case 1: Suppose β is alternating. Then one of the braid generators must always occur with positive exponents
and the other generator must always occur with negative exponents. Hence, by the proof of Sublemma 2.1,
since a generator occurs with only positive exponents, then there will be a nonwandering circle. Since only
one generator occurs with only positive exponents, then there is only one such nonwandering circle. Also,
since adjacent negative syllables cannot occur in β, then wandering circles cannot occur in HA.
Case 2: Suppose β is nonalternating. Since positive syllables are cyclically neighbored on both sides by
negative syllables, then the nonalternating behavior ofβ must come from a pair of adjacent negative syllables.
Hence, by the proof of Sublemma 2.1, this implies the existence of a wandering circle in HA and prevents
the existence of a nonwandering circle (since both generators occur once with negative exponent). Finally,
since a wandering circle (which is always essential in the case that n = 3) “uses up” a braid string from the
braid closure and since a wandering circle must wander from braid string position 1 to braid string position
3 and back before closing up, then the existence of a second such wandering circle is impossible.
Deﬁnition 2.8. Let D(K) = ˆβ be the closure of an n-braid β∈ Bn. With the sign conventions for braid
generators given in Figure 4, we call a twist region positive if its crossings correspond to a positive syllable
in the braid word β and negative if its crossings correspond to a negative syllable in the braid word β. Let
t+(D) denote the number of positive twist regions in D(K) and let t−(D) denote the number of negative
twist regions in D(K).
The following theorem, which is the ﬁrst main result of this paper, is a more precise version of Theorem 1.1
from the introduction.
Theorem 2.2. Let D(K) = ˆβ, where β∈ Bn satisﬁes the assumptions of Lemma 2.1. Let m denote the
number of non-essential wandering circles in the all-A state HA of D(K). In the case that n = 3, we have
that
−χ(G′
A) =t−(D)− 1≥ 1
2· (t(D)− 2),
which gives the volume bounds
v8
2 · (t(D)− 2)≤v8· (t−(D)− 1)≤ vol(S3\K)< 10v3· (t(D)− 1).
9
In the case that n≥ 4 and that the only positive syllables of β possibly occur in the generators σ1 and σn−1,
we have the volume bounds
v8
2 · (t(D)− 2(n +m− 2))≤v8· (t−(D)− (n +m− 2))≤ vol(S3\K)< 10v3· (t(D)− 1).
In the case that n≥ 4 and that positive syllables of β occur in a generator σi for some 2≤ i≤ n− 2, we
have the volume bounds
v8· (t−(D)−t+(D)− (n +m− 2))≤ vol(S3\K)< 10v3· (t(D)− 1) = 10v3· (t−(D) +t+(D)− 1).
It is worth noting that the lower bounds on volume in terms of t(D) given above are sharper than the
general lower bounds given in the Main Theorem (Theorem 1.1) of [12] when t(D) is large compared to the
sum n +m. Speciﬁcally, the lower bounds are sharper when t(D) > 4 for the case when n = 3 (in which
m = 0 and t(D)≥ 4 = 2(n− 1)) and when t(D)> 6(n +m)− 16 for the case when n≥ 4.
Proof of Theorem 2.2. To begin, note that we may apply the many results of Lemma 2.1. Since D(K) is
connected, A-adequate, and satisﬁes the TELC, then Lemma 3.4 of [12] implies that
−χ(G′
A) =t(D)− #{OCs},
where #{OCs} is the number of all-A circles in HA, called other circles, that are not small inner circles.
Note that, by Sublemma 2.1, the set of other circles consists of the medium inner circles, essential wandering
circles, non-essential wandering circles, and nonwandering circles in HA. By Remark 2.1 and Figure 5, it
can be seen that
t+(D)≤ #{medium inner circles}≤ 2t+(D),
which says that each positive twist region corresponds to either one or two medium inner circles. In particular,
looking at the left side (up to reﬂection) of Figure 5, it can be seen that
#{medium inner circles} =t+(D)
in the case that n = 3 and in the case that n≥ 4 when the only positive syllables of β possibly occur in the
generators σ1 and σn−1. Additionally, Condition (2a), Condition (2b), and Condition (2c) of Lemma 2.1
imply that at least half of the twist regions in D(K) must be negative twist regions.
Case 1: Suppose n = 3. By Lemma 2.2, we know that the total number of wandering circles and nonwan-
dering circles is one. Therefore, using all of what was said above, we get
−χ(G′
A) = t(D)− #{OCs}
= t(D)− #{medium inner circles}− #{wandering circles}
−#{nonwandering circles}
= t(D)−t+(D)− 1
= t−(D)− 1
≥ t(D)
2 − 1
= 1
2· (t(D)− 2).
Case 2: Suppose n≥ 4. Note that both essential wandering circles and nonwandering circles “use up”
a braid string from the braid closure. Also, note that Lemma 2.1 implies that there can be at most two
nonwandering circles in the all-A state HA. These two facts imply that
#{essential wandering circles} + #{nonwandering circles}≤ n− 2. (1)
10
Subcase 1: Suppose that the only positive syllables of β possibly occur in the generators σ1 and σn−1, in
which case we have that #{medium inner circles} =t+(D). Then, by using Inequality 1 and what was said
in the beginning of the proof, we get
−χ(G′
A) = t(D)− #{OCs}
= t(D)− #{medium inner circles}− #{non-essential wandering circles}
−#{essential wandering circles}− #{nonwandering circles}
≥ t(D)−t+(D)−m− (n− 2)
= t−(D)− (n +m− 2)
≥ t(D)
2 − (n +m− 2)
= 1
2· (t(D)− 2(n +m− 2)).
Subcase 2: Suppose that positive syllables of β occur in a generator σi for some 2 ≤ i≤ n− 2, in which
case we have that # {medium inner circles}≤ 2t+(D). Then, by using Inequality 1 and what was said in
the beginning of the proof, we get
−χ(G′
A) = t(D)− #{OCs}
= t(D)− #{medium inner circles}− #{non-essential wandering circles}
−#{essential wandering circles}− #{nonwandering circles}
≥ t(D)− 2t+(D)−m− (n− 2)
= t−(D)−t+(D)− (n +m− 2).
By applying the inequalities for −χ(G′
A) above to Theorem 2.1, we get the desired volume bounds.
