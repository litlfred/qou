---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: sec-004-3-paths-and-generating-function
section_title: "Paths and generating function"
section_number: 3
pages: 7-9
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
In this section we will deﬁne the paths, compute their genera ting function and therefore prove Theorem
1.5. This part is an extension of papers of Andrews and Bresso ud [8, 14] based on ideas of Burge [16, 17]. We
study paths in the ﬁrst quadrant, that start on the y-axis, end on the x-axis, and use four kinds of unitary
steps:
• North-East N E: ( x, y)→ (x + 1, y + 1),
• South-East SE : ( x, y)→ (x + 1, y− 1),
• South S: ( x, y)→ (x, y− 1),
• East E: ( x, 0)→ (x + 1, 0).
The height corresponds to the y-coordinate. A South step can only appear after a North-East step and an
East step can only appear at height 0. The paths are either emp ty or end with a South-East step or a South
step. A peak is a vertex preceded by a North-East step and followed by a Sou th step (in which case it will be
called a NES peak ) or by a South-East step (in which case it will be called a NESE peak ). The major index
of a path is the sum of the x-coordinates of its peaks (see Figure 5 for an example). Let k and i be positive
integers with i≤ k. We say that a path satisﬁes the special (k, i)-conditions if it starts at height k− i and
its height is less than k. When the path has no South steps, this is the deﬁnition of the paths in [14].
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 7
Figure 5. This path has four peaks: two NES peaks (located at (2 , 2) and (6 , 1)) and two
NESE peaks (located at (4 , 1) and (7 , 1)). Its major index is 2 + 4 + 6 + 7 = 19.
Let Ek,i(n, j, N) be the number of paths of major index n with N peaks and j South steps which satisfy
the special ( k, i)-conditions. Let E k,i(N ) be the generating function for these paths, that is E k,i(N ) =
E k,i(N, a, q) = ∑
n,j Ek,i(n, j, N)ajqn. Moreover, for 0 ≤ i < k , let Γ k,i(N ) be the generating function for
paths obtained by deleting the ﬁrst NE step of a path which is c ounted inE k,i+1(N ) and begins with a NE
step.
Then
Proposition 3.1.
E k,i(0) = 1;(3.1)
E k,i(N ) = qNE k,i+1(N ) + qN Γ k,i−1(N ); i < k(3.2)
Γ k,i(N ) = qN Γ k,i−1(N ) + (a + qN −1)E k,i+1(N− 1); i > 0(3.3)
E k,k(N ) = qN
1− qN Γ k,k−1(N );(3.4)
Γ k,0(N ) = 0 .(3.5)
Proof. If N = 0 the only path counted in E k,i(0) is the path with only South-East steps, which starts at
(0, k− i) and ends at ( k− i, 0) (if i = k, it is just the empty path, starting and ending at (0 , 0)). This
path has no peaks and its major index is thus 0. This proves (3. 1). Now if the path has at least one peak,
then we take oﬀ its ﬁrst step. If i < k , then a path counted in E k,i(N ) starts with a North-East (deﬁned
by qN Γ k,i−1(N )) or a South-East step ( qNE k,i+1(N )). This gives (3.2). If i > 0, Γ k,i(N ) is the generating
function for paths counted by E k,i+1(N ) that start with a North-East step where the ﬁrst step was del eted.
These paths can start with a North-East step ( qN Γ k,i−1(N )), a South step ( aE k,i+1(N− 1)) or a South-East
step ( qN −1E k,i+1(N− 1)) and we get (3.3). If i = k then a path counted by E k,k(N ) starts with a North-
East ( qN Γ k,k−1(N )) or an East step ( qNE k,k(N )). This gives (3.4). The height of the paths is less than
k, therefore no path which starts at height k− 1 can start with a North-East step and Γ k,0(N ) = 0 as in
(3.5). □
These recurrences uniquely deﬁne the series E k,i(N ) and Γ k,i(N ). We get that:
Theorem 3.2.
E k,i(N ) = aN q(N +1
2 )(−1/a)N
N∑
n=−N
(−1)n qkn2+n(k−i)−(n
2)
(q)N −n(q)N +n
Γ k,i(N ) = aN q(
N
2 )(−1/a)N
N −1∑
n=−N
(−1)n qkn2+n(k−i)−(
n+1
2 )
(q)N −n−1(q)N +n
Proof. Let 












E ′k,i(N ) = aN q(
N +1
2 )(−1/a)N
N∑
n=−N
(−1)n qkn2+n(k−i)−(n
2)
(q)N −n(q)N +n
Γ ′k,i(N ) = aN q(N
2 )(−1/a)N
N −1∑
n=−N
(−1)n qkn2+n(k−i)−(
n+1
2 )
(q)N −n−1(q)N +n
Note thatE ′k,i(0) = 1.
