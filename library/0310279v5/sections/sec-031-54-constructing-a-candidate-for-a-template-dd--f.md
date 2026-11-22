---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-031-54-constructing-a-candidate-for-a-template-dd--f
section_title: "Constructing a candidate for a template (D+,D-) from CA"
section_number: 5.4
pages: 88-92
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Constructing a candidate for a template (D+, D−) from CA
We interrupt the ﬂow of the argument, brieﬂy. The procedure that we gave in Section 5.3.2
for constructing a candidate for a template from thin annuli is almost identical to the
procedure for constructing a candidate for a template (D+, D−) from the foliation of
CA. We will need to know how to do it when we reach the end of Section 6, and since
the alert reader will have the essential ideas in mind right now, this seems like a good
moment to go through the steps in the construction. The argument will be repetitious,
because it is modeled on that in Section 5.3.2, however it seems better to be repetitious
than to keep asking the reader to turn back.
Assume that we are given CA, with boundary X+ −X−. Assume that the complexity
(c1, c2) has been minimized by the use of exchange moves. Assume further that we
have removed all short clasp arcs, and that all non-short clasp arcs are in normal
neighborhoods. We will show that we can construct a pair of diagrams (D+, D−), and
an isotopy D+ →D−such that (D+, D−) carries (X+, X−), and the motion D+ →D−
sends X+ →X−. As in Proposition 5.3.2 we do not know whether D+ and D−are
block strand diagrams because we do not know whether condition (4) for a block-strand
diagram holds. That matter will not concern us now. (Look ahead to Section 6.2 for
more on this. See, in particular, Corollary 6.2.1).
As in Section 5.3.2 there are four ingredients in the structure of (D+, D−): the moving
blocks, the ﬁxed blocks, the moving strands, and the ﬁxed strands.
The precise
description of how we construct each is very close to that in Section 5.3.2, except that:
•
CA replaces S,
•
CAtiled (the portion of CA not foliated by s–arcs) replaces Stiled. As a conse-
quence, we are constructing the pair (D+, D−) (instead of the pair (D, D)). Also
the motion that takes D+ →D−now takes X+ →X−(instead of the motion
that takes D →D taking X →X).
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
501
(i) The Moving Blocks If there are no doubly long clasp arcs, then there also are no
moving blocks, and this part of the construction ends. So we assume that there are
doubly long clasp arcs. Therefore the two tab neighborhoods of the clasp arcs reach all
the way from X+ to X−. We are in the situation of Figure 52, and we may construct
black and grey microstrands, exactly as we did in Section 5.3.2, only now the black
and grey microstrands are subarcs of X+ and X−. Notice that the isotopy of X+ across
CA pushes X+ across Ni
+ to X−, so the two X+ microstrands are always mapped to
the two X−microstrands. Exactly as in Section 5.3.2 we have cylinders Bi, Bi for our
microblocks. The local projection of the microstrands in Bi (resp. Bi) are determined by
the intersections of S+ (resp. S−) with the walls of Bi (resp. Bi). As in Section 5.3.2,
the double points of the local projections are labeled with the index of gi.
Recall the amalgamation of microblocks, and the example of a template in Figure 51.
Before the two ﬂypes it looks as if X and W (and also Y and Z) can be amalgamated,
but after the ﬂype we see that is impossible. The requirement that we introduced, that
the projections be reﬂections of each other, is violated if we attempt to amalgamate X
and W, or Y and Z. We developed a ‘projection criterion’ for when this is possible.
The essential idea was that the block amalgamations that we used maintained their
integrity during the passage from the black side to the grey side.
Let’s begin the construction of the black microblocks. The blocks B and B have the same
structure as in Section 5.3.2. We continue to use the terms ‘top’, ‘cylinder’, ‘bottom’,
with the same meaning as in Section 5.3.2. Then B is an amalgamation of microblocks
{B1, . . . , Br} for microstrands {x1
+, x1
−, . . . xr
+, xr
−} of CA if the following hold:
(1) As in Section 5.3.2: Each Bi ⊂int(B) for i ≤i ≤r.
(2) As in Section 5.3.2: Its support, ie {θ | B ∩Hθ̸ = ∅}, is a closed interval having
length less than 2π. Every component of X ∩B contains a microstrand.
(3) A subtle change from (3) in Section 5.3.2: note that t ∩CA and b ∩CA are each
still a collection of subarcs of a+–arcs and, possibly, subarcs in b–arcs. This
necessarily implies that t and b are contained in a generic disc ﬁber of H. We
can assume that neither t nor b intersect any microstrands. Continuing, we have
the immersion ρ: PA −→CA. Each component of R ⊂ρ−1(B ∩CA) ⊂PA
is a rectangular region that does not contain any singular points. Speciﬁcally:
(a) If R∩X+̸ = ∅then R is trivially foliated with ∂R = β+1∪β+2∪β+3∪β+4,
where (i) β+1 ⊂X+, and β+1 intersects some microstrands in our speciﬁed
set. (ii) β+2 and β+4 are subarcs of a+–arcs. (iii) β+3 is transverse to the
foliation of PA. Moreover the only non-singular leaves it intersects are
a+–arcs .
Geometry & Topology 10 (2006)
502
Joan S Birman and William W Menasco
(b) If R∩X = ∅then R is trivially foliated, with ∂R = β+1 ∪β+2 ∪β+3 ∪β+4
where β+1 and β+3 are in leaves; also β+2 and β+4 are transverse to the
foliation of PA.
(4) As in Section 5.3.2: If xi
+ (resp. xi
−) ⊂int(B), then its partner xi
−(resp. xi
+) is
also a subset of int(B). Also, the dotted segment between each qi
+ and qi
−is a
subset of int(B).
(5) As in Section 5.3.2: Replacing
{B, t, c, b, a, {B1, . . . , Br}, {x1
+, x1
−, . . . , xr
+, xr
−}}
by
{B, t, c, b, a, {B1, . . . , Br}, {x1
+, x1
−, . . . , xr
+, xr
−}},
we can also deﬁne the amalgamation of microblocks {B1, . . . , Br}.
As before, we also have related concepts for B, the amalgamation of microblocks
{B1, . . . , Br}.
Our deﬁnition of the braid projection of X+ onto B ⊂∂B has changed a little bit
because of the new conditions in (3) above. For a given amalgamating block B we
consider {R1, . . . , Rl} ⊂ρ−1(B ∩CA). These are the regions referred to in condition
(3)(a). Let {β1
+3, . . . , βl
+3} be the corresponding β+3 boundary sides of these regions.
Then the graph ρ(∪1≤i≤lβi
+3) ⊂c, along with the clasp arc index labeling of the double
points, are in π(B). Similarly, π(B) is just the labeled graph ρ(∪1≤i≤lβi
−3) ⊂c. Using
this deﬁnition of the braid projection of X+ onto B ⊂∂B, our deﬁnition of ‘related
amalgamating blocks’ is the same as before, viz:
Let B be an amalgamating block. The braid projection π(B) of X+ onto c ⊂∂B is the
graph c ∩S. regarded as a subset of c together with the clasp arc index labeling of this
graph’s double points. We deﬁne π(B) in a similar fashion. Amalgamating blocks B
and B are a pair of related amalgamating blocks if the following hold:
(a)
{B1, . . . , Br} and {B1, . . . , Br} are microblocks associated with clasp intersec-
tions {γ1, . . . , γr}.
(b)
B is a block amalgamation of microblocks {B1, . . . , Br}.
(c)
B is a block amalgamation of microblocks {B1, . . . , Br}.
(d)
π(B) and π(B) are reﬂections of each other.
Look back to Figure 53 for an example.
(ii) Fixed Blocks The ﬁxed blocks are associated to braiding between the strands of
X (and so also of X) in the part of S which is foliated by bands of s–arcs. The braiding
between bands of s–arcs is not part of our geometry. S only detects the places where
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
503
X and X differ in a non-trivial way, but in regions where there are bands of s–arcs they
essentially coincide. However, what might happen is that there is braiding between
the bands of s–arcs, but that the braiding is interrupted by, for example, strands of X
which separate two potential blocks. In order to determine the angular regions where
the blocks occur, we therefore look for singularities in the tiled part of S. The block
subdivision so-obtained will be too extensive, and we will then need to amalgamate
ﬁxed blocks. For further details, see the proof of Proposition 5.3.2, which applies
without any changes at all.
(iii) Moving Strands The moving strands in D are all subarcs of X which are not
amalgamated into moving blocks and are not in the bands of s–arcs. We will give
details on how they are placed in in the proof of Proposition 6.3.1.
(iv) Fixed Strands It may happen that we have two blocks, B(C) and B(C′), for
which (C ∩Hθi+1) ∩(C′ ∩Hθi+1)̸ = ∅, but (C ∩Hθi+1)̸ = (C′ ∩Hθi+1), so that the
amalgamating condition fails. In this situation there are strands that run between B(C)
and B(C′), however not all of the s–bands coming out of B(C) go into B(C′), and/or
not all of the strands going into B(C′) are strands that emerge from B(C). Any braiding
between the s bands that run between B(C) and B(C′) can obviously be pushed into
either B(C) or B(C′) (eliminating Hθi+1 as a singular ﬁber) and they will then become
ﬁxed strands.
We are now in a position to take CA and construct an associated candidate for a template
(D+, D−). It is clear from the construction that (D+ and D−) will carry X+ and X−.
Remark 5.4.1 Go back to Figure 9. The bottom two sketches show the actual pair
of block-strand diagrams (D+, D−) that make up the template in Figure 9, whereas
the other 5 sketches give it meaning by showing the actual combination of ﬂypes (not
necessarily admissible), exchange moves and destabilizations that explain the isotopy
from D+ to D−.
The construction that we just gave falls short of doing what we did in Figure 9 in two
ways. The ﬁrst has been noted before this, and we stress it again, but the second is new:
(1) As noted earlier, the blocks may not either be ‘consolidated’ or ‘optimal’, two
matters that will be discussed in Section 6. That’s why we have said, repeatedly,
that our D+ and D−are candidates for block-strand diagrams, and the pair
(D+, D−) is a candidate for a template.
(2) We have not constructed the intermediate stages that explain the isotopy. That
is clear, because all we dealt with is the long clasp arcs, but to explain the
intermediate isotopy we would have had to also look at clasp arcs which are not,
initially, doubly long but become doubly long after part of CA has been crossed.
Geometry & Topology 10 (2006)
504
Joan S Birman and William W Menasco
That construction remains for future work, for readers who may be interested in,
for example, in working on our ‘open problem (3)’ in Section 7 of this paper. ♦
