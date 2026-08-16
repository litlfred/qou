---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-007-4-paths-and-successive-ranks
section_title: "Paths and successive ranks"
section_number: 4
pages: 12-13
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
In this section we prove the case C k,i(n, j) = Ek,i(n, j) of Theorem 1.4. In fact, we prove a reﬁnement of
this case:
Proposition 4.1. There exists a one-to-one correspondence between the paths of major index n with j
south steps counted by
Ek,i(n, j) and the overpartitions of n with j non-overlined parts in the bottom line
of their Frobenius representation and whose successive ran ks lie in [−i + 2, 2k− i− 1] counted by Ck,i(n, j).
This correspondence is such that the paths have N peaks if and only if the Frobenius representation of the
overpartition has N columns.
This proposition can be proved with a recursive argument. We can show that Ck,i(N ), the generating
function for overpartitions whose Frobenius representati on has N columns and whose successive ranks lie
in [−i + 2, 2k− i− 1], follows the same recurrences as E k,i(N ), as done by Burge [16, 17] for the case of
partitions. Details are given in [34]. We propose here a dire ct mapping that is a generalization of a bijection
of Bressoud [14].
Given a lattice path which starts at (0 , a) and a peak ( x, y) with u South steps to its left, we map this
peak to the pair ( s, t) where
s = (x + a− y + u)/2
t = (x− a + y− 2− u)/2
if there are an even number of East steps to the left of the peak (we then say that the peak is of type 0 ),
and
s = (x + a + y− 1 + u)/2
t = (x− a− y− 1− u)/2
