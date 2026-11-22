---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-020
section_title: "Page 20"
section_number: null
pages: 20-20
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
19
An example of such a path, taken from [14], is shown on Figure 10. For that path, we have k = 4, i = 1,
n1 = 3, n2 = 1 and n3 = 1.
×
×
×
×
×
×
1
3
1
Figure 10. Another example of a path and its relative heights.
We can now move on to the proof of Proposition 6.3.
Proof. We generalize the argument of Bressoud in [14]. Consider a path with no South steps that starts at
height k −i, whose height is less than k −1 and that has nj peaks of relative height ≥j −1 for 2 ≤j ≤k −1.
By Lemma 6.4, such paths are counted by
(6.4)
Pk,i(q) =
qn2
2+···+n2
k−1+ni+···+nk−1
(q)n2−n3 · · · (q)nk−2−nk−1(q)nk−1
where 2 ≤i ≤k. Note that we have replaced nj by nj+1 so that the terms in n1 should be introduced by
the algorithm described below, which will then give us the generating function in the same form as in (6.3).
For any given k ≥2 and i such that 1 ≤i ≤k, we describe an algorithm which generates a path counted
by (6.3) from a path counted by Pk,i(q) if i ≥2 or Pk,2(q) if i = 1, a partition λ into distinct parts which lie
in [0, n1 −1] and a partition b into n1 −n2 nonnegative parts.
We will need to prove that this contruction is uniquely reversible, that the algorithm generates all of our
paths, that the distribution of relative heights is not modiﬁed (except at the ﬁrst step where all the peaks
will be raised by one) and that the algorithm aﬀects the generating function in the appropriate way.
We ﬁrst perform a “volcanic uplift” by inserting a NES peak at each peak (see Figure 11). This increases
all the relative height by one.
×
×
×
×
×
×
×
×
×
2
4
2
Figure 11. Eﬀect of the volcanic uplift on the path from Figure 10.
We then insert n1 −n2 NES peaks at the beginning of the path (see Figure 12). Note that all these peaks
have relative height one and that they are the only peaks of relative height one since the volcanic uplift has
increased all the relative heights by one.
×
×
×
×
×
×
×
×
×
1 1 1 1
2
4
2
Figure 12. After adding the n1 −n2 = 4 NES peaks of relative height one to the path
from Figure 11.
If i = 1, we introduce an extra SE step at the beginning of the path, from (0, k −1) to (1, k −2).
Now if λ contains a part j −1 (1 ≤j ≤n1), we transform the jth NES peak from the right into a NESE
peak (see Figure 13).
Finally, for 1 ≤j ≤n1 −n2, we move the jth peak of relative height one from the right bj times according
to the rules illustrated in Figure 14.
