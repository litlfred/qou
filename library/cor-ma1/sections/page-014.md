---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-014
section_title: "Page 14"
section_number: null
pages: 14-14
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
13
• The sequence t is an overpartition (where the ﬁrst occurrence of a part can be overlined). We need
to prove that for all i, ti −ti+1 > 0 if ti+1 is overlined and ti −ti+1 ≥0 otherwise. The fact that
we always have ti −ti+1 ≥0 is proved in the same way as with the si. If ti+1 is overlined, then it
corresponds to a NESE peak, so we have xi −xi+1 ≥2 and ui+1 = ui. By considering the expression
of ti −ti+1 in the four cases (the peaks i and i + 1 are both of type 0, both of type 1, of type 0 and
of type 1, or of type 1 and of type 0), the result is easily shown.
□
Therefore
s1
s2
· · ·
sN
t1
t2
· · ·
tN

is the Frobenius representation of an overpartition whose weight is
N
X
i=1
(si + ti + 1) =
N
X
i=1
xi
i.e. the major index of the corresponding path.
As an example, the path in Figure 8 corresponds to the overpartition
14
11
6
4
2
7
6
5
4
3

.
×
×
×
×
×
×
×
×
×
×
×
×
×
(6, 4, 0)
(9, 3, 0) (12, 3, 1)
(18, 2, 1)
(22, 4, 1)
Figure 8. Illustration of the correspondence between paths and successive ranks.
The
values of x, y and u are given for each peak.
The peaks all have height at least one, thus for a peak (x, y) which is preceded by an even number of East
steps, we have:
1 ≤y = a + 1 + t −s + u ≤k −1
⇔a −k + 2 ≤s −t −u ≤a
⇔the corresponding successive rank is ≥a −k + 2 and ≤a
and if the peak is preceded by an odd number of East steps, we have:
1 ≤y = s −t −u −a ≤k −1
⇔a + 1 ≤s −t −u ≤k + a −1
⇔the corresponding successive rank is ≥a + 1 and ≤k + a −1.
Thus, given a Frobenius representation of an overpartition and a nonnegative integer a, there is a unique
corresponding path which starts at (0, a).
In our paths, a = k −i, therefore in the ﬁrst case the successive rank r ∈[−i + 2, k −i] and in the second
case r ∈[k −i + 1, 2k −i −1].
The map is easily reversible. This proves Proposition 4.1.
5. Paths and multiplicities
In this section we prove the case Bk,i(n, j) = Ek,i(n, j) of Theorem 1.4. We even prove a reﬁnement:
Proposition 5.1. There exists a one-to-one correspondence between the paths counted by Ek,i(n, j) and the
overpartitions counted by Bk,i(n, j). This correspondence is such that the paths have N peaks if and only if
the length of the multiplicity sequence of the overpartition is N (see Section 5.2 for the deﬁnition).
