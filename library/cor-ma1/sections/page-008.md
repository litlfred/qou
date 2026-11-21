---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
7
Figure 5. This path has four peaks: two NES peaks (located at (2, 2) and (6, 1)) and two
NESE peaks (located at (4, 1) and (7, 1)). Its major index is 2 + 4 + 6 + 7 = 19.
Let Ek,i(n, j, N) be the number of paths of major index n with N peaks and j South steps which satisfy
the special (k, i)-conditions.
Let Ek,i(N) be the generating function for these paths, that is Ek,i(N) =
Ek,i(N, a, q) = P
n,j Ek,i(n, j, N)ajqn. Moreover, for 0 ≤i < k, let Γk,i(N) be the generating function for
paths obtained by deleting the ﬁrst NE step of a path which is counted in Ek,i+1(N) and begins with a NE
step.
Then
Proposition 3.1.
Ek,i(0)
=
1;
(3.1)
Ek,i(N)
=
qNEk,i+1(N) + qNΓk,i−1(N);
i < k
(3.2)
Γk,i(N)
=
qNΓk,i−1(N) + (a + qN−1)Ek,i+1(N −1);
i > 0
(3.3)
Ek,k(N)
=
qN
1 −qN Γk,k−1(N);
(3.4)
Γk,0(N)
=
0.
(3.5)
Proof. If N = 0 the only path counted in Ek,i(0) is the path with only South-East steps, which starts at
(0, k −i) and ends at (k −i, 0) (if i = k, it is just the empty path, starting and ending at (0, 0)). This
path has no peaks and its major index is thus 0. This proves (3.1). Now if the path has at least one peak,
then we take oﬀits ﬁrst step. If i < k, then a path counted in Ek,i(N) starts with a North-East (deﬁned
by qNΓk,i−1(N)) or a South-East step (qNEk,i+1(N)). This gives (3.2). If i > 0, Γk,i(N) is the generating
function for paths counted by Ek,i+1(N) that start with a North-East step where the ﬁrst step was deleted.
These paths can start with a North-East step (qNΓk,i−1(N)), a South step (aEk,i+1(N −1)) or a South-East
step (qN−1Ek,i+1(N −1)) and we get (3.3). If i = k then a path counted by Ek,k(N) starts with a North-
East (qNΓk,k−1(N)) or an East step (qNEk,k(N)). This gives (3.4). The height of the paths is less than
k, therefore no path which starts at height k −1 can start with a North-East step and Γk,0(N) = 0 as in
(3.5).
□
These recurrences uniquely deﬁne the series Ek,i(N) and Γk,i(N). We get that:
Theorem 3.2.
Ek,i(N)
=
aNq(N+1
2 )(−1/a)N
N
X
n=−N
(−1)n qkn2+n(k−i)−(n
2)
(q)N−n(q)N+n
Γk,i(N)
=
aNq(
N
2)(−1/a)N
N−1
X
n=−N
(−1)n qkn2+n(k−i)−(
n+1
2 )
(q)N−n−1(q)N+n
Proof. Let

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
E′k,i(N) = aNq(
N+1
2 )(−1/a)N
N
X
n=−N
(−1)n qkn2+n(k−i)−(n
2)
(q)N−n(q)N+n
Γ′k,i(N) = aNq(N
2)(−1/a)N
N−1
X
n=−N
(−1)n qkn2+n(k−i)−(
n+1
2 )
(q)N−n−1(q)N+n
Note that E′k,i(0) = 1.
