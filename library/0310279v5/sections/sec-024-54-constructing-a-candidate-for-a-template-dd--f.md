---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO"
section_id: sec-024-54-constructing-a-candidate-for-a-template-dd--f
section_title: "Constructing a candidate for a template (D+,D-) from CA"
section_number: 5.4
pages: 88-94
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
We interrupt the ﬂow of the argument, brieﬂy. The procedure that we gave in Section 5.3.2
for constructing a candidate for a template from thin annuli is almost identical to the
procedure for constructing a candidate for a template (D+, D−) from the foliation of
CA . We will need to know how to do it when we reach the end of Section 6, and since
the alert reader will have the essential ideas in mind right now, this seems like a good
moment to go through the steps in the construction. The argument will be repetitious,
because it is modeled on that in Section 5.3.2, however it seems better to be repetitious
than to keep asking the reader to turn back.
Assume that we are givenCA , with boundary X+− X−. Assume that the complexity
(c1, c2) has been minimized by the use of exchange moves. Assume further that we
have removed all short clasp arcs, and that all non-short clasp arcs are in normal
neighborhoods. We will show that we can construct a pair of diagrams (D+,D−), and
an isotopyD+→D− such that (D+,D−) carries (X+, X−), and the motionD+→D−
sends X+→ X−. As in Proposition 5.3.2 we do not know whether D+ andD− are
block strand diagrams because we do not know whether condition (4) for a block-strand
diagram holds. That matter will not concern us now. (Look ahead to Section 6.2 for
more on this. See, in particular, Corollary 6.2.1).
As in Section 5.3.2 there are four ingredients in the structure of (D+, D−): the moving
blocks, the ﬁxed blocks, the moving strands, and the ﬁxed strands. The precise
description of how we construct each is very close to that in Section 5.3.2, except that:
• CA replacesS ,
• CAtiled (the portion ofCA not foliated by s–arcs) replacesStiled. As a conse-
quence, we are constructing the pair (D+,D−) (instead of the pair (D, D)). Also
the motion that takesD+→D− now takes X+→ X− (instead of the motion
that takes D→ D taking X→ X).
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 501
(i) The Moving Blocks If there are no doubly long clasp arcs, then there also are no
moving blocks, and this part of the construction ends. So we assume that there are
doubly long clasp arcs. Therefore the two tab neighborhoods of the clasp arcs reach all
the way from X+ to X−. We are in the situation of Figure 52, and we may construct
black and grey microstrands, exactly as we did in Section 5.3.2, only now the black
and grey microstrands are subarcs of X+ and X−. Notice that the isotopy of X+ across
CA pushes X+ across Ni
+ to X−, so the two X+ microstrands are always mapped to
the two X− microstrands. Exactly as in Section 5.3.2 we have cylinders Bi, Bi for our
microblocks. The local projection of the microstrands in Bi (resp. Bi) are determined by
the intersections ofS+ (resp.S−) with the walls of Bi (resp. Bi). As in Section 5.3.2,
the double points of the local projections are labeled with the index of gi.
Recall the amalgamation of microblocks, and the example of a template in Figure 51.
Before the two ﬂypes it looks as if X and W (and also Y and Z) can be amalgamated,
but after the ﬂype we see that is impossible. The requirement that we introduced, that
the projections be reﬂections of each other, is violated if we attempt to amalgamate X
and W , or Y and Z. We developed a ‘projection criterion’ for when this is possible.
The essential idea was that the block amalgamations that we used maintained their
integrity during the passage from the black side to the grey side.
Let’s begin the construction of the black microblocks. The blocksB and B have the same
structure as in Section 5.3.2. We continue to use the terms ‘top’, ‘cylinder’, ‘bottom’,
with the same meaning as in Section 5.3.2. Then B is an amalgamation of microblocks
{B1,..., Br} for microstrands{x1
+, x1
−,... xr
+, xr
−} ofCA if the following hold:
(1) As in Section 5.3.2: Each Bi⊂ int(B) for i≤ i≤ r.
(2) As in Section 5.3.2: Its support, ie{θ| B∩ Hθ⁄=∅}, is a closed interval having
length less than 2π. Every component of X∩ B contains a microstrand.
(3) A subtle change from (3) in Section 5.3.2: note that t∩CA and b∩CA are each
still a collection of subarcs of a+–arcs and, possibly, subarcs in b–arcs. This
necessarily implies that t and b are contained in a generic disc ﬁber of H. We
can assume that neither t nor b intersect any microstrands. Continuing, we have
the immersion ρ : PA−→CA . Each component of R⊂ρ−1(B∩CA )⊂PA
is a rectangular region that does not contain any singular points. Speciﬁcally:
(a) If R∩X+⁄=∅ then R is trivially foliated with∂R =β+1∪β+2∪β+3∪β+4,
where (i)β+1⊂ X+, andβ+1 intersects some microstrands in our speciﬁed
set. (ii) β+2 and β+4 are subarcs of a+–arcs. (iii) β+3 is transverse to the
foliation ofPA . Moreover the only non-singular leaves it intersects are
a+–arcs .
Geometry &Topology 10 (2006)
502 Joan S Birman and William W Menasco
(b) If R∩X =∅ then R is trivially foliated, with∂R =β+1∪β+2∪β+3∪β+4
whereβ+1 andβ+3 are in leaves; alsoβ+2 andβ+4 are transverse to the
foliation ofPA .
(4) As in Section 5.3.2: If xi
+ (resp. xi
−)⊂ int(B), then its partner xi
− (resp. xi
+) is
also a subset of int(B). Also, the dotted segment between each qi
+ and qi
− is a
subset of int(B).
(5) As in Section 5.3.2: Replacing
{B, t, c, b, a,{B1,..., Br},{x1
+, x1
−,..., xr
+, xr
−}}
by
{B, t, c, b, a,{B1,..., Br},{x1
+, x1
−,..., xr
+, xr
−}},
we can also deﬁne the amalgamation of microblocks{B1,..., Br}.
As before, we also have related concepts for B, the amalgamation of microblocks
{B1,..., Br}.
Our deﬁnition of the braid projection of X+ ontoB⊂ ∂B has changed a little bit
because of the new conditions in (3) above. For a given amalgamating block B we
consider{R1,..., Rl}⊂ ρ−1(B∩CA ). These are the regions referred to in condition
(3)(a). Let{β1
+3,...,β l
+3} be the corresponding β+3 boundary sides of these regions.
Then the graphρ(∪1≤i≤lβi
+3)⊂ c, along with the clasp arc index labeling of the double
points, are in π(B). Similarly, π(B) is just the labeled graph ρ(∪1≤i≤lβi
−3)⊂ c. Using
this deﬁnition of the braid projection of X+ ontoB⊂ ∂B, our deﬁnition of ‘related
amalgamating blocks’ is the same as before, viz:
Let B be an amalgamating block. The braid projection π(B) of X+ onto c⊂∂B is the
graph c∩S . regarded as a subset of c together with the clasp arc index labeling of this
graph’s double points. We deﬁneπ(B) in a similar fashion. Amalgamating blocks B
and B are a pair of related amalgamating blocks if the following hold:
(a) {B1,..., Br} and{B1,..., Br} are microblocks associated with clasp intersec-
tions{γ1,...,γ r}.
(b) B is a block amalgamation of microblocks{B1,..., Br}.
(c) B is a block amalgamation of microblocks {B1,..., Br}.
(d) π(B) and π(B) are reﬂections of each other.
Look back to Figure 53 for an example.
(ii) Fixed Blocks The ﬁxed blocks are associated to braiding between the strands of
X (and so also of X) in the part ofS which is foliated by bands of s–arcs. The braiding
between bands of s–arcs is not part of our geometry.S only detects the places where
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 503
X and X differ in a non-trivial way, but in regions where there are bands of s–arcs they
essentially coincide. However, what might happen is that there is braiding between
the bands of s–arcs, but that the braiding is interrupted by, for example, strands ofX
which separate two potential blocks. In order to determine the angular regions where
the blocks occur, we therefore look for singularities in the tiled part ofS . The block
subdivision so-obtained will be too extensive, and we will then need to amalgamate
ﬁxed blocks. For further details, see the proof of Proposition 5.3.2, which applies
without any changes at all.
(iii) Moving Strands The moving strands in D are all subarcs of X which are not
amalgamated into moving blocks and are not in the bands of s–arcs. We will give
details on how they are placed in in the proof of Proposition 6.3.1.
(iv) Fixed Strands It may happen that we have two blocks, B(C) and B(C′), for
which ( C∩ Hθi+1)∩ (C′∩ Hθi+1)⁄=∅, but ( C∩ Hθi+1)⁄= (C′∩ Hθi+1), so that the
amalgamating condition fails. In this situation there are strands that run between B(C)
and B(C′), however not all of the s–bands coming out of B(C) go into B(C′), and/or
not all of the strands going into B(C′) are strands that emerge from B(C). Any braiding
between the s bands that run between B(C) and B(C′) can obviously be pushed into
either B(C) or B(C′) (eliminating Hθi+1 as a singular ﬁber) and they will then become
ﬁxed strands.
We are now in a position to takeCA and construct an associated candidate for a template
(D+, D−). It is clear from the construction that ( D+ and D−) will carry X+ and X−.
Remark 5.4.1 Go back to Figure 9. The bottom two sketches show the actual pair
of block-strand diagrams (D+,D−) that make up the template in Figure 9, whereas
the other 5 sketches give it meaning by showing the actual combination of ﬂypes (not
necessarily admissible), exchange moves and destabilizations that explain the isotopy
fromD+ toD−.
The construction that we just gave falls short of doing what we did in Figure 9 in two
ways. The ﬁrst has been noted before this, and we stress it again, but the second is new:
(1) As noted earlier, the blocks may not either be ‘consolidated’ or ‘optimal’, two
matters that will be discussed in Section 6. That’s why we have said, repeatedly,
that ourD+ andD− are candidates for block-strand diagrams, and the pair
(D+,D−) is a candidate for a template.
(2) We have not constructed the intermediate stages that explain the isotopy. That
is clear, because all we dealt with is the long clasp arcs, but to explain the
intermediate isotopy we would have had to also look at clasp arcs which are not,
initially, doubly long but become doubly long after part ofCA has been crossed.
Geometry &Topology 10 (2006)
504 Joan S Birman and William W Menasco
That construction remains for future work, for readers who may be interested in,
for example, in working on our ‘open problem (3)’ in Section 7 of this paper.♦
5.5 Pushing across regions with a G–ﬂype foliation
We have seen that ifPA contains a long clasp arc, then there is a family of thin annuli
S1⊂PA having ∂S1 = X0∪ X1, where X0 = X+, also X0 can be pushed across
S1 to X1 using a sequence of ﬂypes. The complement of S1 inPA will be a new
family of annuli which has boundary X1∪ X−. It may happen that we can then apply
Proposition 5.1.1 to simplify S1 via (ab)⋆ exchange moves; or it may happen that
PA\S 1 has long clasp arcs, in which case we can iterate the construction. Putting the
two cases together we can construct a second annulusS2 with∂S2 = X1∪ X2 such
that the movement acrossS2 is either an (ab)⋆ exchange move or a sequence of ﬂypes.
This procedure can be iterated until either we produce thin annuli that have X− as a
boundary component, or there are no more (ab)⋆ exchange moves, or there are no more
long clasp arcs. If we do have thin annuli with X− in the boundary then we will have
decomposedCA into a sequence of thin annuli. And, we have moved acrossCA using
ﬂypes and ab or ab⋆ exchange moves. The difﬁculty in moving acrossPA this way is
that it may happen that we needed to use inadmissible ﬂypes.
With that difﬁculty in mind, we say that a family of thin annuliSk∪S k+1∪···∪S k+l
supports a G–ﬂype foliation if (i) it is possible to cross the region using only ﬂypes and
ab or (ab)⋆ exchange moves, and (ii) there exist integersk, q such that b(Xk+i)≥ b(Xk)
for 1≤ i≤ (q− 1) and b(Xk+q)≤ b(Xk). In this situation the combined ﬂyping and
ab or (ab)⋆ motion across the regionSk∪S k+1∪···∪S k+q is a G–ﬂype. It is readily
seen that if (B, B) is a pair of related amalgamating blocks for the pair (X+, X−) then
B maintains its integrity through successive ﬂypes and is isotopied to B.
Example 5.5.1 The template in Figure 56 is an illustration of a G–ﬂype.
It shows the foliated annulusPA which was used to construct the template which we
saw in Section 1 in the boxed sketches at the bottom of Figure 9. The labels ‘block Y ’
and ‘block Z’ refer to the blocks in Figure 9. In the interest of keeping the foliation
as simple and understandable as possible, we decided to position the clasp arcs only
in tab neighborhoods, and not in normal neighborhoods. Thus, the clasp arcs are not
contained in the ﬁnite union of leaves. (The addition of 12 vertices and 12 singularities
would be needed in order to position the clasps in normal neighborhoods.) In order
to remove distracting details from the picture, we have eliminated inessential b–arcs,
collapsing the normal neighborhoods of the clasp arcs γ1
+ and γ2
+. This is always
possible, and we did it to save space. The arcsγ1 andγ2 in sketch (d) are the clasp arcs
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 505
(a) from strand 3 of block
Y to strand 1 of block Z
(b) from strand 2 of block
Z to strand 2 of block Y
(c) from strand 3 of block
Z to strand 3 of block Y (d) from strand 2 of block
Y to strand 2 of block Z
1
3
4
5
1314
γ3 γ4
+ +
+
+
1
2
4
7
7
8
10 12
14
15
17
18
γ3
γ1+
+
+ +
+
+ +
3
5
6
6
8
9
9 11
11
16
17
18
γ4
γ2
+
+
++
+
+ +
2
10
12
13
15 16
γ1 γ2
+ +
+ ++
Figure 56: The foliation ofPA , in the situation of the 6–braid template of Figure 9
used to construct the ﬁrst thinly foliated annuli that are split off by the dotted curves
in sketches (b) and (c). After we have ﬂyped across this initial thin annulus (the ﬁrst
negative ﬂype of Figure 9) we will have four resulting vertices where we can perform
(ab) exchange move. These are the two double-strand exchange moves in the isotopy
sequence of Figure 9. Finally, the remaining portion ofCA will just be the region in
sketch (a) and tab neighborhoods around clasp arcsγ3 andγ4 in sketches (b) and (c).
All of these individual motions were across thin annuli, giving us a decomposition of
CA into thin annuli. Since the braid index starts at b(X+) = 6, goes to 7 after the ﬁrst
ﬂype, remains at 7 for all of the exchange moves and only returns to 6 = b(X−) after
the last ﬂype, all of the thin annuli in this decomposition go to make up the motion
acrossPA . The combination of all of these isotopies is the 6–braid G–ﬂype which we
illustrated in Figure 9 and Figure 56.
Notice that there are no moving blocks in Figure 9 because there are no doubly long
clasp arcs in Figure 56. The following features of the template in Figure 9 are outside
the support of the isotopy: the four blocks X, Y, Z, W and the following strands that
join them: all strands that enter and leave W and X, also strand 1 entering Y , strand
1 leaving Y , strands 3 and 4 entering Z and strands 1 and 4 leaving Z. We need to
account for the changes in strands 2 and 3 enteringY , strands 2 and 3 leaving Y , strands
1 and 2 entering Z and strands 2 and 3 leaving Z. These are all described completely
by the data in the foliated annulus.
Geometry &Topology 10 (2006)
506 Joan S Birman and William W Menasco
