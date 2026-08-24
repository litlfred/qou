---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: sec-009-2-xi-xi1-yi-yi1-ui-ui1-1-since-ui-ui1-it-is-suﬃc
section_title: "(xi− xi+1− yi− yi+1 + ui− ui+1 + 1). Since ui≥ ui+1, it is suﬃcient"
section_number: 2
pages: 13-14
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
to prove that xi− xi+1− yi− yi+1≥ 0. This comes from the fact that there is an East step between
the two peaks (see Figure 7). If the ith peak is of type 1 and the ( i + 1)st is of type 0, the proof is
similar.
≥ yi+1 ≥ yi
xi+1 xi
Figure 7. If the ith peak of is type 0 and the ( i + 1)st peak is of type 1, we have xi− xi+1≥
yi + yi+1.
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 13
• The sequence t is an overpartition (where the ﬁrst occurrence of a part can b e overlined) . We need
to prove that for all i, ti− ti+1 > 0 if ti+1 is overlined and ti− ti+1≥ 0 otherwise. The fact that
we always have ti− ti+1≥ 0 is proved in the same way as with the si. If ti+1 is overlined, then it
corresponds to a NESE peak, so we have xi− xi+1≥ 2 and ui+1 = ui. By considering the expression
of ti− ti+1 in the four cases (the peaks i and i + 1 are both of type 0, both of type 1, of type 0 and
of type 1, or of type 1 and of type 0), the result is easily shown .
□
Therefore
(s1 s2 ···sN
t1 t2 ···tN
)
is the Frobenius representation of an overpartition whose w eight is
N∑
i=1
(si + ti + 1) =
N∑
i=1
xi
i.e. the major index of the corresponding path.
As an example, the path in Figure 8 corresponds to the overpar tition
(14 11 6 4 2
7 6 5 4 3
)
.
× ×
×
× ×
× ×
× ×
×
×
×
×
(6, 4, 0)
(9, 3, 0) (12 , 3, 1)
(18, 2, 1)
(22, 4, 1)
Figure 8. Illustration of the correspondence between paths and succe ssive ranks. The
values of x, y and u are given for each peak.
The peaks all have height at least one, thus for a peak ( x, y) which is preceded by an even number of East
steps, we have:
1≤ y = a + 1 + t− s + u≤ k− 1
⇔ a− k + 2≤ s− t− u≤ a
⇔ the corresponding successive rank is ≥ a− k + 2 and≤ a
and if the peak is preceded by an odd number of East steps, we ha ve:
1≤ y = s− t− u− a≤ k− 1
⇔ a + 1≤ s− t− u≤ k + a− 1
⇔ the corresponding successive rank is ≥ a + 1 and≤ k + a− 1.
Thus, given a Frobenius representation of an overpartition and a nonnegative integer a, there is a unique
corresponding path which starts at (0 , a).
In our paths, a = k− i, therefore in the ﬁrst case the successive rank r∈ [−i + 2, k− i] and in the second
case r∈ [k− i + 1, 2k− i− 1].
The map is easily reversible. This proves Proposition 4.1.
