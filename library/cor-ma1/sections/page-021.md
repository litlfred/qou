---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-021
section_title: "Page 21"
section_number: null
pages: 21-21
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
20
SYLVIE CORTEEL AND OLIVIER MALLET
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
1 1
1
1
2
4
2
Figure 13. Eﬀect of transforming some NES peaks into NESE peaks in the path from
Figure 12. In this example, λ = (5, 4, 3, 1).
1
×
×
2
×
×
3
4
×
×
5
×
6
Figure 14. The rules for moving peaks of relative height one.
×
×
×
×
Figure 15. We want to move the leftmost peak to the right twice, but after the ﬁrst move,
we come up against a sequence of adjacent peaks. We then move the rightmost peak in this
sequence.
When we move a peak, it can meet the next peak to the right. We say that a peak (x, y) meets a peak
(x′, y′) if
x′ −x =
(
2 if (x, y) is a NESE peak
1 if (x, y) is a NES peak
.
If this happens, we abandon the peak we have been moving and move the next peak to the right. If we come
up against a sequence of adjacent peaks, we move the rightmost peak in the sequence (see Figure 15).
To conclude the proof, we must show that the distribution of relative heights is not modiﬁed by the
operations of Figure 14 (Proposition 6.5), that the construction procedure is uniquely reversible (Proposition
6.6), that we generate all of our paths (Proposition 6.7), and that the algorithm aﬀects the generating function
in the appropriate way (Proposition 6.8).
□
Proposition 6.5. The operations of Figure 14 preserve the number of peaks of relative height ≥j for all j.
Proof. Let us show it for each operation. We call p the peak which is moved. Remember that before the
move, the relative height of p is 1.
For operations 1 and 4, the relative height of p clearly remains 1 after the move. The other peaks are not
aﬀected and their relative heights are therefore not modiﬁed.
For operations 2 and 5, it can be easily shown that the relative height of p remains 1 (see Figure 16 for
an example) unless it meets a peak, in which case the two peaks will swap their relative heights (see Figure
17 for an example). In both cases, the relative heights of the other peaks are not modiﬁed.
For operations 3 and 6, the relative height of p will clearly remain 1 since the peak located to its left has
a larger (or equal) height (see Figure 18).
