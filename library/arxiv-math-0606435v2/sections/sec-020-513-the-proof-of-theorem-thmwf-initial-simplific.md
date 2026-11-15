---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-020-513-the-proof-of-theorem-thmwf-initial-simplific
section_title: "The proof of Theorem thmwf: Initial simplifications"
section_number: 5.1.3
pages: 28-29
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The following fact is well-known:
Theorem 5.3 MWF(β) = 1 if an only if [β]i = 1 for i = 1,...,n −1.
Now for MWF = 3 it sufﬁces to ensure that (either we can reduce the braids) or can ﬁnd words, whose non-maximal
subwords do not give an unknot. For the rest of the section we assume that β′ gives the unknot.
We will work by induction on the number of strands, and for ﬁxed number of strands on the index sum. So we consider
a positive braid word β, and assume w.l.o.g. it has the smallest index sum among positive braid representatives of its
closure link for the same number of strands. For such β, we will either reduce it (by at least one strand or crossing), or
show MWF ≥4.
Most braids β will be easily dealt with, but there remain certain families of words that require a case-by-case study.
We decided not to omit too many of the (tedious) details of this part, in order to keep the proof followable, even if it
may not contribute to its (esthetic) appearance.
Note that in order to prove MWF(β) ≥4, it sufﬁces to go over to a (link in a) suitably chosen node in a positive
resolution tree for β and show MWF ≥4 for this node. In particular, we can remove from β all syllables of index ≤k
and the k resulting left isolated strands.
The case of reductions is more delicate. In some situations we can describe them directly, but this is not always
the case. Then we proceeded as follows. First we took generic examples, in making all syllables non-trivial whose
triviality we have not argued about. We adjust parities so that the closure is a knot, and checked using KnotScape [HT]
that the braid reduces (by at least one strand/crossing).
Later we wrote a computer program that seeks reductions by keeping given crossings rigid. Such reductions would
commute with replacing rigid crossings by any tangle, in particular by any non-trivial braid word syllable. (Non-trivial
syllables behave similarly to rigid vertices, and suggest that the reduction is likely to work in general.) This way we
can ﬁnd reductions for inﬁnite families of braids on a given number of strands. By turning all summit index-1 syllables
into rigid crossings, one can also handle the braids that occur for an increasing number of strands.
The technical details of the application of this program are, however, tedious and little insightful. Instead we content
ourselves with giving the examples we processed with KnotScape.
5.1
Positive braid links
29
Deﬁnition 5.3 A valley resp. mountain is a subword of the maximal word that starts with same index syllables and
contains only one minimal resp. maximal syllable. This syllable is called the bottom of the valley resp. summit or top
of the mountain. The index of the bottom/top is the depth resp. height.
