---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-010-23-semiadequacy-7
section_title: "Semiadequacy 7"
section_number: 2.3
pages: 7-8
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The Kauffman polynomial [Ka] F is usually deﬁned via a regular isotopy invariant Λ(a,z) of unoriented links. We
use here a slightly different convention for the variables i n F, differing from [Ka, Th2] by the interchange of a and
a−1. Thus in particular we have for a link diagram D the relation F(D)(a,z) = aw(D)Λ(D)(a,z), where Λ(D) is the
writhe-unnormalized version of the polynomial, given in our convention by the properties
Λ
( )
+ Λ
( )
= z
(
Λ
( )
+ Λ
( ) )
,(6)
Λ
( )
= a−1 Λ
( )
; Λ
( )
= a Λ
( )
,(7)
Λ
(
©
)
= 1 .(8)
The Brandt-Lickorish-Millett-Ho polynomial [BLM] Q is given by Q(z) = F(1,z).
2.3. Semiadequacy
An alternative description of V is given by the Kauffman bracket in [Ka2]. We do not need this d escription directly,
but for self-containedness is it useful to recall the related concept of semiadequacy that was popularized in [LT].
Let D be an unoriented link diagram. A state is a choice of splittings of type A or B for any single crossing (see ﬁgure
4), Let the A-state of D be the state where all crossings are A-spliced; similarly deﬁne the B-state.
We call a diagram A-(semi)adequate if in the A-state no crossing trace (one of the dotted lines in ﬁgure 4) c onnects a
loop with itself. Similarly we deﬁne B-(semi)adequate. A diagram is semiadequate if it is A- or B-semiadequate,
and adequate if it is simultaneously A- and B-semiadequate. A link is adequate/semiadequate if it has an ade-
quate/semiadequate diagram. (Here A-adequate and B-adequate is what is called +adequate resp. −adequate in [Th].)
AA
B
B
AA
B
B
Figure 4: The A- and B-corners of a crossing, and its both splittings. T he corner A (resp.
B) is the one passed by the overcrossing strand when rotated c ounterclockwise (resp.
clockwise) towards the undercrossing strand. A type A (resp . B) splitting is obtained by
connecting the A (resp. B) corners of the crossing. It is usef ul to put a “trace” of each
splitted crossing as an arc connecting the loops at the splitted spot.
We also need a part of the semiadequacy formulas for the Jones polynomial. As in [St4], for an non-negative integer
i, we write Vi for [V ]mindeg V +i and ¯Vi = [V ]maxdeg V −i. (These are the i + 1-st and i + 1-st last coefﬁcient of V in its
coefﬁcient list.) For an A- (resp. B-) semiadequate diagram , in [St4], and independently in [DL], formulas were
obtained for V1,2 (resp. ¯V1,2).
From the A-state A(D) of a diagram D we deﬁne two graphs. The ﬁrst graph, we call it
the A-graph G(A) = G(A(D)) has vertices for each loop in A(D), and an edge between
each pair of loops that are connected by a trace of at least one crossing in D. If there are
at least two such traces, we call the edge multiple.
Let △(D) = △(A(D)) be the number of cycles of length 3 (triangles) in G(A(D)).
The second graph, we call it the intertwining graph IG (A) = IG(A(D)), has vertices for
each multiple edge in A(D), and an edge in IG(A) is drawn between each pair of vertices
in IG(A), whose corresponding multiple traces in A(D) contain traces of the form shown
on the right.
8 2 Preliminaries, basic deﬁnitions and conventions
Theorem 2.1 ([St4, DL]) Assume that D is a connected A-adequate diagram. Then V0V1 = χ(G(A)) − 1 and
V0V2 =
( 2 − χ(G(A))
2
)
+ χ(IG(A)) − △(A(D)) .
Here χ is the Euler characteristic (number of vertices minus number of edges); V0 = ±1 by [LT]. Analogous formulas
hold for B-adequate diagrams.
