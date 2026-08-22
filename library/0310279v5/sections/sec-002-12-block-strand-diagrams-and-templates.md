---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-002-12-block-strand-diagrams-and-templates
section_title: "Block-strand diagrams and templates"
section_number: 1.2
pages: 5-7
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
Before we can state our main result, we need to introduce new concepts. Our moves
will be described in terms of certain pairs of ‘block-strand diagrams’ which we call
‘templates’. Examples are the block-strand diagram pairs which make up the templates in
Figures 1, 2 and 3. The reader may wish to look ahead to the boxed pairs of block-strand
diagrams in Figures 8, 9 and 10 for examples of more complicated templates.
A block B in R3− A is a 3–ball having the structure of a 2–disk ∆ crossed with
an interval [0, 1] such that (i) for any ﬁber Hθ∈ H the intersection Hθ∩ B is either
∅ or ∆×{θ} for some θ∈ [θ1,θ 2], and (ii) there exists some θ∈)0, 2π) such that
Hθ∩ B =∅. The disc t = B∩ Hθ1 is the top of B and the disc b = B∩ Hθ2 is the bottom
of B. A strand l is homeomorphic to an interval [0, 1] or a circle S1. It is oriented
and transverse to each ﬁber of H such that its orientation agrees with the forward
direction of H. When l is homeomorphic to an interval,∂l = l0∪ l1, where l0 is the
beginning endpoint of l and l1 is the ending endpoint of l. A block-strand diagramD
is a collection of pairwise disjoint blocks{B1,..., Bk} and pairwise disjoint strands
{l1,..., ll} which together have the following structure:
(1) If li∩ Bj⁄=∅ then li∩ Bj = (li
1∩ tj)∪ (li
0∩ bj) where tj is the top of Bj and bj
is the bottom of Bj. (We allow for the possibility that either (li
1∩ tj) or ( li
0∩ bj)
is empty.)
(2) For each li
0 (resp. li
1) there is some bj⊂ Bj (resp. tj⊂ Bj) such that li
0⊂ bj
(resp. li
1⊂ tj).
(3) For each block Bj we have|tj∩ (∪1≤i≤lli
1)| =|bj∩ (∪1≤i≤lli
0)|≥ 2.
The fact that for each j = 1,..., k there is a ﬁber which misses Bj shows that, by
rescaling, we may ﬁnd a distinguished ﬁber Hθ0 which does not intersect any block. We
deﬁne the braid index b(D) of the block-strand diagramD to be the number of times the
Geometry &Topology 10 (2006)
418 Joan S Birman and William W Menasco
strands ofD intersect the distinguished ﬁber Hθ0 . Condition (3) above makes b(D) well
deﬁned. For a speciﬁed block Bj⊂D we deﬁne its braid index b(Bj) =|tj∩(∪1≤i≤lli
1)|.
Continuing the deﬁnition of a block-strand diagram, we assume:
(4) If Bj⊂D then the braid index b(Bj) is strictly less than the braid index b(D),
with one exception. The exception occurs whenD is the block strand diagram
that results after a destabilization has been performed, as in Figure 1.
A templateT is a pair of block-strand diagrams (D+,D−), both with blocks B1,..., Bk
and an isotopy which takesD+ toD−, in such a way that for every ﬁxed choice of
braiding assignments to the blocksB1,..., Bk the resulting closed braidsX, X′ represent
the same oriented link type X . The diagrams D+ andD− are the initial and ﬁnal
block-strand diagrams in the pair. The ﬁxed blocks and ﬁxed strands inT = (D+,D−)
are the blocks and strands where the isotopy is pointwise the identity. All other blocks
and strands are moving. For example, in Figure 3 the blocks P and Q are ﬁxed blocks,
whereas R is a moving block. A braiding assignment to a block-strand diagramD is
a choice of a braid on mj strands for each Bj∈D . That is, we replace Bj with the
chosen braid, so that Bj with this braiding assignment becomes a braided tangle with
mj in-strands and mj out-strands. In this way a block strand diagram gives us a closed
braid representative of a linkX .
Let X be a closed m–braid. We say that X is carried byD if there exists a braiding
assignment for the blocks inD such that the resulting closed braid is braid-isotopic to
X.
When we ﬁrst began to understand that templates were the appropriate settings for our
work on the MTWS we wondered whether our deﬁnition was so broad (because the
diagrams in question support so many knot and link types) as to be content-free! In this
regard, the following fact is fundamental:
Proposition 1.2.1 LetD be a block-strand diagram of braid index n. Then there exist
n–braids thatD does not carry.
Proof Up to conjugation, a block-strand diagram may be described by a word
V1W1V2W2....VkWk in the standard elementary braid generators σ1,...,σ n−1 of the
n–strand braid group, where each Vj represents a word which describes the braid carried
by the jth block (after making a braiding assignment to the block) and eachWi is a braid
word on n strands which describes the strands that connect the blocks. By hypothesis
no block has more than n− 1 strands entering or leaving it, so by modifying the Wi’s
we may assume without loss of generality that each Vj is a braid on the ﬁrst qj–strands,
where qj < n. After this modiﬁcation, the only places where the elementary braid
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 419
generator σn−1 appears is in the braid words that describe the strands that join the
blocks, ie the words W1,..., Wk .
Now let|Wi| be the number of times σn−1 occurs in Wi. The|Wi|′s are ﬁxed numbers
since we were handed a block-strand diagram. For an arbitrary conjugacy class
{C} of n–braids, let |C| be the minimum number of times the generator σn−1 is
used, in all possible words which represent{C}. Our block diagram can only carry
closed n-braids C such that (up to conjugacy)|C|≤| W1| +|W2| +... +|Wk|. But
there are closed n-braids X such that|Y| is arbitrarily large for all Y∈{ X}. An
example is X = (σ1σ2...σ n−1)nN for a large positive integer N . For, the braid word
(σ1σ2...σ n−1)n is a full twist of the braid strands. It generates the center of the n-string
braid group. It cannot be represented by any braid word that does not use all the
elementary braid generators. Therefore it’s Nth power uses the generatorσn−1 at least
nN times.
Having Proposition 1.2.1 on hand, we proceed to deﬁne the templates that we will
use in the statement of the MTWS. Our main theorem begins with an arbitrary closed
n–braid representative X+ of an arbitrary oriented knot or link typeX in 3–space. Let
X− be a second such representative, where b(X−) = b(X ). Our goal in the subsections
which follow is to describe some of the templates that we need, and at the same time
to describe the building blocks of all of them. Note that we regard braid isotopy as
a trivial move, sometimes even forgetting to mention it. By a result of Morton [ 26,
Theorem 1] braids β,β′ in the n–string braid group Bn are conjugate if and only if the
associated closed braids are isotopic in the complement of the braid axis. In keeping
with our motivating idea of codifying Markov towers, the names that we give some
of our templatesT = (D+, D−) correspond to the name of the isotopy that is used to
move D+ to D−.
