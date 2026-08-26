---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-037-513-the-proof-of-theorem-51-initial-simpliﬁcatio
section_title: "The proof of Theorem 5.1: Initial simpliﬁcations"
section_number: 5.1.3
pages: 28-29
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The following fact is well-known:
Theorem 5.3 MWF (β) = 1 if an only if [β]i = 1 for i = 1, . . . ,n − 1.
Now for MW F = 3 it sufﬁces to ensure that (either we can reduce the braids) o r can ﬁnd words, whose non-maximal
subwords do not give an unknot. For the rest of the section we assume that β′ gives the unknot.
We will work by induction on the number of strands, and for ﬁxed number of strands on the index sum. So we consider
a positive braid word β, and assume w.l.o.g. it has the smallest index sum among posi tive braid representatives of its
closure link for the same number of strands. For such β, we will either reduce it (by at least one strand or crossing), or
show MW F ≥ 4.
Most braids β will be easily dealt with, but there remain certain families of words that require a case-by-case study.
We decided not to omit too many of the (tedious) details of thi s part, in order to keep the proof followable, even if it
may not contribute to its (esthetic) appearance.
Note that in order to prove MWF (β) ≥ 4, it sufﬁces to go over to a (link in a) suitably chosen node in a positive
resolution tree for β and show MWF ≥ 4 for this node. In particular, we can remove from β all syllables of index ≤ k
and the k resulting left isolated strands.
The case of reductions is more delicate. In some situations w e can describe them directly, but this is not always
the case. Then we proceeded as follows. First we took generic examples, in making all syllables non-trivial whose
triviality we have not argued about. We adjust parities so that the closure is a knot, and checked using KnotScape [HT]
that the braid reduces (by at least one strand/crossing).
Later we wrote a computer program that seeks reductions by ke eping given crossings rigid. Such reductions would
commute with replacing rigid crossings by any tangle, in particular by any non-trivial braid word syllable. (Non-trivial
syllables behave similarly to rigid vertices, and suggest t hat the reduction is likely to work in general.) This way we
can ﬁnd reductions for inﬁnite families of braids on a given number of strands. By turning all summit index-1 syllables
into rigid crossings, one can also handle the braids that occur for an increasing number of strands.
The technical details of the application of this program are , however, tedious and little insightful. Instead we conten t
ourselves with giving the examples we processed with KnotScape.
