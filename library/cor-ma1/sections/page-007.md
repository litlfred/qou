---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
6
SYLVIE CORTEEL AND OLIVIER MALLET
This decomposition shows that the generating function for overpartitions with generalized Durfee square
of size N where the exponent of q counts the weight and the exponent of a counts the number of overlined
parts is
aNq(N+1
2 )(−1/a)N
(q)N(q)N
.
Deﬁnition 2.4. The successive Durfee squares of an overpartition are its generalized Durfee square and the
successive Durfee squares of the partition below the generalized Durfee square, if we represent the partition
as in Figure 3, with the overlined parts above the non-overlined ones. We can also deﬁne similarly the
successive Durfee rectangles by dissecting the overpartition with d×(d+1)-rectangles instead of squares (see
Figure 4). In this case, we also impose the condition that the partition on the right of a d×(d+1)-rectangle
cannot have more than d parts.
Figure 4. Successive Durfee squares and successive Durfee rectangles of (6, 5, 5, 4, 4, 3, 2, 2, 2, 1).
These deﬁnitions imply that the generating function for overpartitions with i−1 successive Durfee squares
followed by k −i successive Durfee rectangles (the ﬁrst one being a generalized Durfee square/rectangle) is
X
n1≥...≥nk−1≥0
q(n1+1
2 )+ni+...+nk−1(−1/a)n1an1
(q)n1
×
 
qn2
2
n1
n2

q
! 
qn2
3
n2
n3

q
!
· · ·
 
qn2
k−1
nk−2
nk−1

q
!
(2.1)
where
n
k

q
=
(q)n
(q)k(q)n−k
is the generating function of partitions into at most k parts less or equal to n −k.
3. Paths and generating function
In this section we will deﬁne the paths, compute their generating function and therefore prove Theorem
1.5. This part is an extension of papers of Andrews and Bressoud [8, 14] based on ideas of Burge [16, 17]. We
study paths in the ﬁrst quadrant, that start on the y-axis, end on the x-axis, and use four kinds of unitary
steps:
• North-East NE: (x, y) →(x + 1, y + 1),
• South-East SE: (x, y) →(x + 1, y −1),
• South S: (x, y) →(x, y −1),
• East E: (x, 0) →(x + 1, 0).
The height corresponds to the y-coordinate. A South step can only appear after a North-East step and an
East step can only appear at height 0. The paths are either empty or end with a South-East step or a South
step. A peak is a vertex preceded by a North-East step and followed by a South step (in which case it will be
called a NES peak) or by a South-East step (in which case it will be called a NESE peak). The major index
of a path is the sum of the x-coordinates of its peaks (see Figure 5 for an example). Let k and i be positive
integers with i ≤k. We say that a path satisﬁes the special (k, i)-conditions if it starts at height k −i and
its height is less than k. When the path has no South steps, this is the deﬁnition of the paths in [14].
