---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-037-62-cleaning-up-the-templates-in-tm
section_title: "Cleaning up the templates in T(m)"
section_number: 6.2
pages: 106-109
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Cleaning up the templates in T (m)
Our goal is to prove that no block in any template in T (m) has full braid index, however
we will do that in a setting that yields additional information for later use. The concept
of a block-strand diagram is, at this moment, rather loose. One can imagine that blocks
could be slid around and amalgamated with one-another, and also subdivided. We would
like them to be more canonical. But even if we succeed to make them canonical, a direct
attack on the problem seems difﬁcult. We use a more roundabout approach. When we
organized the moves of the MTWS into three separate subsequences, we separated the
subsequence (1–2), which requires only exchange moves, and the subsequence (1–3),
which requires only exchange moves and destabilizations, from subsequence (1–4),
which requires admissible ﬂypes as well as the more general moves in T (m). We will
see that, as a consequence, the templates in T (m) have no blocks whose braid index is
equal to the braid index of the diagram. In fact, we will be able to show more: that
the templates of T (m) are ‘consolidated’ in a sense that will be made precise below,
with the braid index condition on the blocks being just one of the nice properties of
consolidated templates.
Let D be a block-strand diagram having blocks B and B′. We use the notation t, b ⊂∂B
(resp. t′, b′ ⊂∂B′) for the top and bottom of B (resp. top and bottom of B′). Recall
our use of the term ‘amalgamating blocks’ in Section 5.3.2. We now say that B′ (resp.
B) can be amalgamated into B (resp. B′) if via a braid isotopy we can move t′ ⊂b
(resp. b ⊂t′). (These are two ways of looking at the same phenomenon.) We say the
blocks of D are consolidated if no two blocks of D can be amalgamated. Next, let s
and s′ be strands in D having endpoints on common blocks (still called) B and B′. We
say that strands s and s′ are topologically parallel if there exists a rectangular disc R
such that R ∩D = ∂R = s ∪βb ∪s′ ∪βt′ where βb ⊂b and βt′ ⊂t′. Note that if
strands s, s′ are topologically parallel, it could happen, for example, that s travels from
B to B′ without winding around the axis, but s′ winds about the axis as it does so. To
rule out this sort of complication, we say that s and s′ are braid parallel if they are
topologically parallel and R ∩A = ∅. We say that D is consolidated if the blocks of D
are consolidated and all of its topologically parallel strands are braid parallel.
Proposition 6.2.1 Given a template (D+, D−) with D−having minimal braid index
there exists a new template (D′
+, D′
−), where D′
+ is obtained from D+ via a sequence
of exchange moves and destabilizations; also D′
−is obtained from D−via a sequence
of exchange moves; also D′
+ and D′
−are both consolidated block-strand diagrams. In
particular, we can assume that the block-strand diagrams in every template in T (m) are
consolidated.
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
519
Proof Let R be a rectangular disc that demonstrates that strands s and s′ are topologi-
cally parallel for, say, D+. We look at the induced foliation of H on R. We can make
the standard assumptions about R being transverse to A and all but ﬁnitely many disc
ﬁbers of H being transverse to R. For the ﬁnitely many non-transverse disc ﬁbers, we
can assume that each one contains a single saddle singularity. We can then argue that
there are no leaves in the foliation that are circles. The foliation of R can then be seen
as a union of aa–, ab–, bb– and sb–tiles. In particular, since the two sides βb and
βt′ can be assumed to be s–arcs, R will either be trivially foliated by s–arcs, or will
contain sb–singularities.
In the case where R is not trivially foliated we assign an arbitrary orientation to R.
We can then talk about the Gϵ,δ graphs of R. We wish to invoke the statements of
Proposition 5.1.1 to simplify the graph of R through a sequence of exchange moves
and destabilizations. Since R is embedded all discs corresponding to those satisfying
statements (5), (6) and (7) of Proposition 5.1.1 will automatically be good. It is clear
that after applying Proposition 5.1.1 repeatedly, R will be trivially foliated, thus our
resulting strands will be braid parallel.
We have a similar argument in the case where our strands are in D−. The only change is
that our application of Proposition 5.1.1 cannot yield any destabilizations because D−
has minimal braid index. This establishes that we can replace a template (D+, D−) with
(D′
+, D′
−) via the sequence mentioned in statements 1 and 2, so that any topologically
parallel strands in D′
+ or D′
−are braid parallel.
Next, suppose there are two blocks, B(1) and B(2), in the template (D′
+, D′
−) such
that we can amalgamate B(2) into B(1) in, say D′
−. (These blocks may be moving
or ﬁxed.) Such an amalgamation occurs because all of the strands entering the top of
B(2) are braid parallel and start at the bottom of B(1). If we could also amalgamate
them in D′
+, then there would be nothing to stop us from doing the amalgamation
in both block-strand diagrams—our template would still be a template and would be
simpliﬁed. The obstruction to amalgamating B(2) into B(1) in D′
−is that there is no
similar amalgamation of B(2) into B(1) in D′
+. But, since the strands entering the
top of B(2) are all braid parallel in D′
−, they must be topologically parallel in D′
+.
But, we are assuming that all topologically parallel strand in D′
+ are braid parallel. So
there is no obstruction. Thus, the block amalgamation is possible. After an iteration of
amalgamations we may assume that (D′
+, D′
−)is consolidated.
Corollary 6.2.1 Let T = (D+, D−) be a template in T (m). Then there is no block
B ⊂D−such that b(B) = b(D−).
Proof Suppose that D−does contain a block B such that the number of strands
entering the top of B or leaving the bottom of B is equal to the braid index of D−. Then
Geometry & Topology 10 (2006)
520
Joan S Birman and William W Menasco
we can amalgamate all other blocks in D−with B. That is, we can push all braiding of
strands immediately before and after B into B, thus making all such braiding parallel.
This allows us to amalgamate any block immediately before or after B in D−with
B. We then iterate this procedure to amalgamate all blocks in D−with B. After this
comprehensive amalgamation the consolidated block-strand diagram D′
−will have a
single block and will still carry X−. By Proposition 6.2.1 we will thus have gone from
X+ (carried by D+) to X−(carried by the consolidated D′
−) through a sequence of
braid isotopies, exchange moves and destabilizations. But note that these are the moves
that made up the sequences (1–3) and (1–2). This means that our X′
+ of sequence (1–3)
is braid isotopic to our X′
−of sequence (1–2). Thus, sequence (1–4) is vacuous and
there is no template to construct. We conclude that we can assume that the templates
of T (m), which are all constructed using sequence (1–4), have no blocks of full braid
index.
Our main goal for this section, the proof that no block in a template in T (m) has full
braid index, has been achieved. In so-doing, we learned a little bit more: we may assume
that the templates of T (M) are consolidated. In fact, there is still is one more step we
can take to make them more canonical. Referring back to the discussion of Fixed Blocks
in Section 5.3, in the ﬁrst two paragraphs we used the occurrence of singularities in
the ﬁbration H to designate ﬁxed blocks. In the third paragraph we then speciﬁed how
some of these just-constructed ﬁxed blocks can be amalgamated. Essentially, we were
observing the existence of “missing blocks”. We make this concept and its implications
rigorous below. While this is not necessary for pushing our ﬁniteness argument forward,
it does tie up this loose end coming from Section 5.3. Our brief detour will end at the
end of this subsection.
Let D be a block-strand diagram having braid structure (A, H). Suppose there exist
3–balls B in the braid structure having a ∆× [0, 1] structure with the discs ∆× p
contained in ﬁbers of H, 0 ≤p ≤1. Assume that int(B) contains at least one block of
D and intersects only the strands of D, but that B \ (B ∩D) is not homeomorphic to an
interval cross a 2k–punctured 2–sphere. We call such a 3–ball B a missing block in D.
Let (D+, D−) be a template that is consolidated. Then (D+, D−) is an optimal template
if for every missing block of D−, the ambient isotopy of S3 that takes D−to D+ does
not result in an missing block of D+. In fact, we claim that we may assume that all
templates of T (M) are optimal.
To see this, let (D+, D−) = T ∈T (m) and let {B1, . . . , Bk} be a complete listing of
all the blocks in T . As before, b(Bi) is the braid index of the block Bi. We deﬁne the
complexity of T to be a lexicographically ordered 2–tuple (k, Pk
1(n −b(Bi)). Now, if
B−is a missing block of D−that is taken to a missing block B+ of D+ by the ambient
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
521
isotopy of S3 that relates D−and D+ then by assumption B+ must contain at least one
of the Bi blocks plus something else. That something else could be either additional
blocks or strands of D+ that do not intersect Bi in the set B+ ∩D+ ⊂B+. We now
replace T ∈T (m) with a new template
T ′ = ([(D+ \ int(B+)) ∪B+], [(D−\ int(B−)) ∪B−]).
Notice that the complexity of T ′ is less than the complexity of T : if B+ contains more
than one block then T ′ has fewer blocks than T ; and, if B+ contains just one block,
Bi ⊂D+, along with some number of extra strands then m −b(B+) < m −b(Bi). In
both situations the complexity is reduced.
It is not hard to see that employing the recipe given in Section 5.4 for producing
a (D+, D−) from an arbitrary triplet (X+, X−, CA) does not necessarily produce an
optimal template. We emphasize this point by ending this subsection with a useful
deﬁnition which we will need in our ﬁniteness argument.
Let {l1
+, . . . , lh
+} be a listing of the components of X+ ∩CAtiled and, similarly,
{l1
−, . . . , lh
−} be a listing of the components of X−∩CAtiled such that the isotopy
across CA has li
+ being taken to li
−for 1 ≤i ≤h. Speciﬁcally, there is a component
Ri ⊂CAtiled that has li
± ⊂∂Ri, 1 ≤i ≤h. Now, if we collapse each of the s–arcs of
CA −CAtiled to a point we can conceptually think of X−as being obtained from X+
by replacing every li
+ in X+ with li
−, or to abuse notation [(X+ \ (l1
+ ∪· · · ∪lh
+)) ∪
(l1
−∪· · · ∪lh
−)] = X−. (We will continue this abuse of notation below.)
Recall that by Morton [26, Theorem 1] the conjugacy class of X+ is determined by
the link type X+ ⊔A. We say that a triplet has unnecessary motion if its complexity
can be reduced in the following manner. Suppose now that there exists a proper subset
{li1
+, . . . , lil
+} ⊂{l1
−, . . . , lh
−} such that [(X+ \ (li1
+ ∪· · · ∪lil
+)) ∪(li1
−∪· · · ∪lil
−)] ⊔A
has the same link type as X+ ⊔A. Then let CA′ be the clasp annulus that is obtained
from CA by replacing each component {Ri1, . . . , Ril} ⊂CAtiled with an s–band that
is parallel to the strands {li1
−, . . . , lil
−}. Our new clasp annulus is still cobounded by
X+ −X−and C(X+, X−, CA′) < C(X+, X−, CA).
