---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-008-12-syl-vie-corteel-and-olivier-mallet
section_title: "SYL VIE CORTEEL AND OLIVIER MALLET"
section_number: 12
pages: 13-13
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
if there are an odd number of East steps to the left of the peak ( we then say that the peak is of type
1 ). Moreover, we overline t if the peak is a NESE peak. In both cases, s and t are integers and we have
s + t + 1 = x. In the case of partitions treated in [14], u is always 0.
Let N be the number of peaks in the path and j the number of South steps of the paths. Let ( xi, yi) be
the coordinates of the ith peak from the right and ( si, ti) be the corresponding pair.
Proposition 4.2. The sequence (s1, s2, . . . , sN ) is a partition into distinct nonnegative parts and the se-
quence (t1, t2, . . . , tN ) is an overpartition into nonnegative parts with j non-overlined parts.
Proof. We need to prove the following results:
• sN≥ 0. If the last peak from the right ( xN , yN ) is of type 0, then sN = (xN + a− yN + uN )/2 and
it is suﬃcient to prove that xN− yN≥− a since uN = 0. It is obvious that any vertex has a greater
(or equal) value of x− y than the previous vertex in the path. Since the path begins at (0, a), we
have x− y =−a at the beginning of the path and thus we have x− y≥− a for all vertices. Now if
the peak is of type 1, then xN≥ 2 and sN = (xN + a + yN− 1 + uN )/2≥ 0.
• tN≥ 0. If the last peak from the right ( xN , yN ) is of type 0, then tN = (xN− a+ yN− 2− uN )/2. We
have uN = 0 and xN > 0. If yN≥ a, then tN≥ 0. Otherwise it is easy to see that xN≥ 2 + a− yN
(see Figure 6) and thus tN≥ 0. Now if this peak is of type 1, then tN = (xN− a− yN− 1− uN )/2.
We have uN = 0 and there is at least one East step to the left of the peak and therefore at least a
South-East steps before the East step and at least yN North-East steps after the East step. Hence
xN− yN− a > 0 and tN≥ 0.
a− yN
≥ 2
a
yN
Figure 6. We show that xN≥ 2 + a− yN in the case yN≤ a.
• The sequence s is a partition into distinct parts . We need to prove that for all i, si− si+1 > 0.
If the ith peak from the right and the ( i + 1) st peak are both of type 0, it is clearly true since
xi− yi > x i+1− yi+1 (two peaks cannot have the same value of x− y), and ui≥ ui+1 (remember
that ui is the number of South steps to the left of the ith peak). If the ith peak from the right and
the (i + 1)st peak are both of type 1, then si− si+1 = (xi + yi + ui− xi+1− yi+1− ui+1)/2. It is easy
to see that that xi + yi > x i+1 + yi+1 and ui≥ ui+1. If the ith peak is of type 0 and the ( i + 1)st is
of type 1, we have si− si+1 = 1
