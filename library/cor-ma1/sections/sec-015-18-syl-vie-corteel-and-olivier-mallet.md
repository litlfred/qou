---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-015-18-syl-vie-corteel-and-olivier-mallet
section_title: "SYL VIE CORTEEL AND OLIVIER MALLET"
section_number: 18
pages: 19-21
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
Substituting into Lemma 6.1 and simplifying, we obtain
∑
n1≥···≥nk≥0
q(
n1+1
2 )+n2
2+···+n2
k+ni+1+···+nk (−1/a)n1an1
(q)n1−n2···(q)nk−1−nk (q)nk
= (−aq)∞
(q)∞
(
1 +
∞∑
n=1
q(k+1)n2+(k−i+1)n+(−a)n(−1/a)n
(−aq)n
+
∞∑
n=1
q(k+1)n2−(k−i)n(−a)n(−1/a)n
(−aq)n
)
= (−aq)∞
(q)∞
(
1 +
∞∑
n=1
q(k+1)n2+(k−i+1)n(−a)n(−1/a)n
(−aq)n
+
−1∑
n=−∞
q(k+1)n2+(k−i+1)n(−a)n(−1/a)n
(−aq)n
)
.
Replacing k by k− 1 and i by i− 1 gives (1.1). □
6.2. A combinatorial proof. We will use and generalize the notion of relative height of a p eak. This
notion was deﬁned by Bressoud in [14] for paths with no South s teps and a simpler version of the deﬁnition
was given in [10]. We adapt this deﬁnition for the paths with S outh steps.
Deﬁnition 6.2. The relative height of a peak ( x, y) is the largest integer h for which we can ﬁnd two vertices
on the path, ( x′, y− h) and ( x′′, y− h), such that x′ < x ≤ x′′ and such that between these two vertices
there are no peaks of height > y and every peak of height y has abscissa≥ x.
The original deﬁnition was the same except x≤ x′′ was x < x ′′. Indeed when there are no South steps
the case x = x′′ is impossible.
For example, the relative heights in the path from Figure 9 ar e, from left to right: 1, 2, 1, 4, 3, 2.
×
×
× ×
× ×
×
× ×
× × ×
×
1
2 1
4
3 2
Figure 9. An example of a path and its relative heights.
We will prove here that
Proposition 6.3. The coeﬃcient of qnaℓ in
(6.3) q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1 (−1/a)n1an1
(q)n1−n2···(q)nk−2−nk−1(q)nk−1
is the number of paths with major index n and ℓ South steps, starting at height k− i, whose height is less
than k and having nj peaks of relative height ≥ j for 1≤ j≤ k− 1. Therefore,
∑
n1≥···≥nk−1≥0
q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1(−1/a)n1an1
(q)n1−n2···(q)nk−2−nk−1 (q)nk−1
=E k,i(a, q).
To prove this proposition we will use a result of Bressoud [14 ]
Lemma 6.4. The coeﬃcient of qn in
qn2
1+n2
2+···+n2
k−1+ni+···+nk−1
(q)n1−n2···(q)nk−2−nk−1(q)nk−1
is the number of paths with major index n, no South steps, starting at height k− i, whose height is less than
k and having nj peaks of relative height ≥ j for 1≤ j≤ k− 1.
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 19
An example of such a path, taken from [14], is shown on Figure 1 0. For that path, we have k = 4, i = 1,
n1 = 3, n2 = 1 and n3 = 1.
×
× ×
× ×
×
1
3 1
Figure 10. Another example of a path and its relative heights.
We can now move on to the proof of Proposition 6.3.
Proof. We generalize the argument of Bressoud in [14]. Consider a pa th with no South steps that starts at
height k− i, whose height is less than k− 1 and that has nj peaks of relative height ≥ j− 1 for 2≤ j≤ k− 1.
By Lemma 6.4, such paths are counted by
(6.4) Pk,i(q) = qn2
2+···+n2
k−1+ni+···+nk−1
(q)n2−n3···(q)nk−2−nk−1 (q)nk−1
where 2≤ i≤ k. Note that we have replaced nj by nj+1 so that the terms in n1 should be introduced by
the algorithm described below, which will then give us the ge nerating function in the same form as in (6.3).
For any given k≥ 2 and i such that 1 ≤ i≤ k, we describe an algorithm which generates a path counted
by (6.3) from a path counted by Pk,i(q) if i≥ 2 orPk,2(q) if i = 1, a partition λ into distinct parts which lie
in [0 , n1− 1] and a partition b into n1− n2 nonnegative parts.
We will need to prove that this contruction is uniquely rever sible, that the algorithm generates all of our
paths, that the distribution of relative heights is not modi ﬁed (except at the ﬁrst step where all the peaks
will be raised by one) and that the algorithm aﬀects the gener ating function in the appropriate way.
We ﬁrst perform a “volcanic uplift” by inserting a NES peak at each peak (see Figure 11). This increases
all the relative height by one.
× ×
× ×
×
× ×
×
×
2
4 2
Figure 11. Eﬀect of the volcanic uplift on the path from Figure 10.
We then insert n1− n2 NES peaks at the beginning of the path (see Figure 12). Note th at all these peaks
have relative height one and that they are the only peaks of re lative height one since the volcanic uplift has
increased all the relative heights by one.
× ×
× ×
×
× ×
×
×
1 1 1 1
2
4 2
Figure 12. After adding the n1− n2 = 4 NES peaks of relative height one to the path
from Figure 11.
If i = 1, we introduce an extra SE step at the beginning of the path, from (0 , k− 1) to (1 , k− 2).
Now if λ contains a part j− 1 (1≤ j≤ n1), we transform the jth NES peak from the right into a NESE
peak (see Figure 13).
Finally, for 1≤ j≤ n1− n2, we move the jth peak of relative height one from the right bj times according
to the rules illustrated in Figure 14.
