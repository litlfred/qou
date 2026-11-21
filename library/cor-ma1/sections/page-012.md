---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-012
section_title: "Page 12"
section_number: null
pages: 12-12
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
11
Summing on N we get
X
N≥0
Ek,i(N)
=
X
N≥0
aNq(
N+1
2 )(−1/a)N
N
X
n=−N
(−1)n qkn2+n(k−i)−(
n
2)
(q)N−n(q)N+n
=
X
N≥0
N
X
n=−N
aNq(
N+1
2 )(−1/a)N(−1)n qkn2+n(k−i)−(n
2)
(q)N−n(q)N+n
=
∞
X
n=−∞
X
N≥|n|
aNq(N+1
2 )(−1/a)N(−1)n qkn2+n(k−i)−(
n
2)
(q)N−n(q)N+n
=
∞
X
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
·
X
N≥|n|
(−aq)n( −qn
a )N−nq(N+1
2 )−(n+1
2 )aN−n
(q)N−n(q)N+n
=
∞
X
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
(−aq)∞
(q)∞
by Proposition 3.3
=
(−aq)∞
(q)∞
∞
X
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
.
This is equation (1.1) of Theorem 1.5.
4. Paths and successive ranks
In this section we prove the case Ck,i(n, j) = Ek,i(n, j) of Theorem 1.4. In fact, we prove a reﬁnement of
this case:
Proposition 4.1. There exists a one-to-one correspondence between the paths of major index n with j
south steps counted by Ek,i(n, j) and the overpartitions of n with j non-overlined parts in the bottom line
of their Frobenius representation and whose successive ranks lie in [−i + 2, 2k −i −1] counted by Ck,i(n, j).
This correspondence is such that the paths have N peaks if and only if the Frobenius representation of the
overpartition has N columns.
This proposition can be proved with a recursive argument. We can show that Ck,i(N), the generating
function for overpartitions whose Frobenius representation has N columns and whose successive ranks lie
in [−i + 2, 2k −i −1], follows the same recurrences as Ek,i(N), as done by Burge [16, 17] for the case of
partitions. Details are given in [34]. We propose here a direct mapping that is a generalization of a bijection
of Bressoud [14].
Given a lattice path which starts at (0, a) and a peak (x, y) with u South steps to its left, we map this
peak to the pair (s, t) where
s = (x + a −y + u)/2
t = (x −a + y −2 −u)/2
if there are an even number of East steps to the left of the peak (we then say that the peak is of type 0),
and
s = (x + a + y −1 + u)/2
t = (x −a −y −1 −u)/2
