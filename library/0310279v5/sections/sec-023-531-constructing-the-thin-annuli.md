---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-023-531-constructing-the-thin-annuli
section_title: "Constructing the thin annuli"
section_number: 5.3.1
pages: 69-88
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
Preparing for the shortening of long clasp arcs, we will construct a familyS of ‘thin
annuli’ which is a subset ofPA . Normal neighborhoods will play a key role in the
construction. We will prove:
Lemma 5.3.1 Assume thatX has µ components. Suppose that PA contains long
clasp arcsγi
+,γ j
+, i⁄= j. Then there exists a familyS ofµ annuli, each a subannulus
ofPA , and each with a component of X+ as one of its boundaries, such that every
annulus inS is either trivially foliated by s–arcs, or is a standard annulus, or has a
foliation satisfying the following (see Figure 43 for examples):
(i) Each non-trivially foliated annulus contains at least one long clasp arc. Moreover,
all of its clasp arcs are doubly long and of length 1, with respect to the induced
foliation ofS .
(ii) After an isotopy ofPA which leaves X+ and the other components of ∂S ﬁxed,
each b–arc inS may be assumed to have at least one of its endpoints on a clasp
arc.
Proof The case when there is exactly one long clasp arc was just discussed in
Section 5.2, so we assume that there are at least two long clasp arcs. Let γi
+ be a long
clasp arc, so thatγi
− begins on X− and ends near X+. Assume that γi
+ andγi
− have
been pushed into a union of leaves in their normal neighborhoods. This is possible,
by the construction in Proposition 4.5.1. Let Ni
− be the normal neighborhood ofγi
−.
Geometry &Topology 10 (2006)
482 Joan S Birman and William W Menasco
We focus our attention on a rectangle which we call N
i
−. See sketches (1) and (2) in
Figure 45. It is a subset of Ni
−, and it coincides with Ni
− when the clasp arc has length
2. It has three edges which are in ∂Ni
−. We choose an arc which is transverse to the
foliation as its other ‘horizontal’ boundary.
++
- -
++
- -
+ +
--
+ +
--
(1) (2) (3) (4)
δ
−δ
δ
−δ −δ
δ
−δ
δ
−δ
δ
−δ
δ
−δ
δ
−δ
δ
γi
− γi
−
γi
+ γi
+
Figure 45: Sketches (1) and (2) illustrate the two possibilities for N
i
− . Sketches (3) and (4)
illustrate the two possibilities for N
i
+ .
There are corresponding subrectangles N
i
+ and we show the two possible arrangements
in sketches (3) and (4) of Figure 45. As in the case of N
i
−, the rectangle N
i
+ has 3
boundary edges which are in∂Ni
+. We choose its 4th boundary edge to be an arc which
is transverse to the foliation, so that the rectangle has 4 vertices and 4 singularities.
In the special case whenγi
+ has length 2 the puncture endpoint of the arcγi
+ will be
an interior point of N
i
+, but ifγi
+ has length≥ 3 then γi
+∩ N
i
+ will have both of its
endpoints on the boundary. We correct this by modifyingγi
+∩ N
i
+ to a subarc ofγi
+
which has the same image in CA as the intersection of γi
− with its induced normal
neighborhood. This will give us a shortened induced arc which (by an abuse of notation)
we continue to refer to as γ+. It begins on X+ and ends at a point in the interior of
N
i
+. By construction, γi
− and the newγi
+ have the same image inCA , and determine
the clasp intersection between the rectangles N
i
− and N
i
+ which is induced by the
clasp intersection inCA corresponding toγi. The four cases which are illustrated in
Figure 45 will be referred to as types (1),(2),(3),(4).
LetNS be the union of all of the N
i
− and N
i
+. Note that, while N
i
±∩ (γj
−∪γj
+) =∅
for all j⁄= i, there is no reason why N
i
±∩ N
j
± should be empty. This leads us to the
following preliminary deﬁnition of a connected collection of normal neighborhoods:
Choose N, N
′
∈NS . We say that N and N
′
are connected, and write N←→ N
′
, if
N∩ N
′
⁄=∅ inPA . Two examples are given in Figure 46. In the top row, N has
type 1 and N
′
has type 2 and N∩ N
′
= ∂N∩∂N
′
. In the middle row N has type
1, N
′
has type 3 and they intersect along two singular leaves and the disc between
them. Observe that this is the maximal possible intersection, because the normal
neighborhood of a clasp arc never intersects another clasp arc. It follows that the
possible sequences in a connected set are 12, 13, 14, 23, 24, 34, 21, 31, 41, 32,
42, 43. A collection of normal neighborhoods {N
1
,..., N
p
}⊂N S is connected
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 483
+
--
+
-
++
-
+
-
+
-
++
- -
+
-
-
+
- -
+
-
+
- -
+ + +
-
++
-
++
- -
-
12
13
eliminateinessentialb–arc
eliminateinessentialb–arc
(a) (b) (c) (d)
γi
− γj
− γi
− γj
−
γi
−
γj
+
γi
−
γj
+
γi
− γj
−
γi
+ γj
+
γi
−
γj
+ γi
+
γj
−
−δ
δ
−δ
Figure 46: Adjacent pairs of foliated connected normal neighborhoods. Sketches a,b,c,d in the
bottom row show all possibilities, after the elimination of inessential b–arcs.
if there is a connecting path between any two neighborhoods in the collection, ie if
N
′
, N
′′
∈{ N
1
,... N
p
} then there exists a subcollection{N
i1
,..., N
iq
}⊂{ N
1
,..., N
p
}
such that N
′
←→N
i1
←→N
i2
←→···←→ N
iq
←→N
′′
. A connected component of
NS is called a region and is denoted by the symbolR.
We now observe that each b–arc in eachR is in a normal neighborhood of some clasp
arc. We distinguish between two types of b–arcs: those whose endpoints are vertices
which do not meet a clasp arc, and those which have at least one vertex endpoint which
is on a clasp arc. Let’s look ﬁrst at the former. Examples can be seen in the darkly
shaded subrectangles in the left sketches in rows 1 and 2 of Figure 46. Recall that
our normal neighborhoods were created by the repeated use of ﬁnger moves, which
necessarily created some inessential b–arcs. But all of the b–arcs which do not intersect
clasp arcs are inessential, and may be deleted by an isotopy ofPA which is supported
on a disc in the interior of the connected region, as in the passage from the left to the
right in Figure 46. Therefore we may assume thatR contains no such b–arcs. Notice
that we have chosen our deﬁnition of complexity so that this modiﬁcation does not
alter the complexity. With the modiﬁcation, it is easy to see that there are precisely 4
possible sequences of two modiﬁed normal neighborhoods, as illustrated in the bottom
row in Figure 46, sketches (a),(b),(c),(d).
A regionR is either an annulus or a rectangle, as illustrated in Figure 43. If it is an
Geometry &Topology 10 (2006)
484 Joan S Birman and William W Menasco
annulus, then it satisﬁes properties (i)–(ii) of Lemma 5.3.1. Assume it’s a rectangle.
The lower horizontal boundary of R is a subarc of a component of X+, and so the
connected componentsR1,..., Rq associated to any given component of X+ have a
natural cyclic order on X+. We would like to use this natural order to join them by
bands of s–arcs to obtain annuli. However the vertical edges of the rectangles are not
s–arcs. The following observation saves the day: the grey dotted horizontal boundary
of each rectangle was chosen in a rather arbitrary way as an arc which is transverse to
the foliation and in the interior ofPA , and if we now modify our choices by replacing
the vertical edges of the rectangles in (a),(b),(c),(d) by the sketches in (e),(f),(g),(h) of
Figure 47 we will be in business.
-
+
- -
+
-
+ + ++
- -
(e) (f) (g) (h)
(e′) (f ′) (g′) (h′)
γi
+ γj
+
γi
− γj
−
γi
− γj
−
γi
+ γj
+
Figure 47: Possible arrangements of clasp arcs in adjacent intersecting normal neighborhoods
inPA , near the right and left boundaries of a connected collection of normal neighborhoods
Sketches (e) and (f) are obtained from sketch (a) of Figure 47 by modifying the grey
boundary on the left and right respectively. Note that the modiﬁed grey boundary is
everywhere transverse to the leaves of the foliation. On the other hand, if we attempt
to do the same thing in the situation of (b), choosing the grey boundary to be close to
the left (resp. right) clasp arc, a point of tangency with leaves of the foliation will be
introduced, so it is necessary to include the singular leaf which is on the left (resp. right)
in the modiﬁed connected region, as illustrated in (g) (resp. (h)). We leave it to the reader
to check that (e) and (h) are modiﬁcations of (c), and that (f) and (g) are modiﬁcations
of (d). In (e)–(h), which are based directly upon the sketches in Figure 45, all have their
rightmost singular leaf in G−,δ . But there is a second possibility: we are given the
foliation near X+, and we do not know much about it outside the normal neighborhoods.
In fact there are 4 other possible patterns for the right and left boundaries, also restricted
by the fact that X+ must be transverse to ﬁbers of H. They are illustrated in sketches
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 485
(e′),(f′),(g′),(h′) of Figure 47, and were obtained from (e),(f),(g),(h) by interchanging
the roles of grey and black.
Let’s examine the possibilities for the regions. Figure 43 shows the foliated annulus and
the four possible foliated disc regions inS , up to the number of pairs of components
of G−,δ and G+,−δ . In each, we give examples of how the clasp arcs might be
placed. To constructS from the various non-trivially foliated regions we ﬁrst join disc
regions which are consecutive as one travels along a component of X+ with bands of
s–arcs which run between X+ and X−. We may also need some number of standard
annuli which have long clasp arcs. (See Figure 43 again.) Finally we may need some
number of annuli which are foliated entirely by s–arcs. This completes the proof of
Lemma 5.3.1.
LetS be an annular subset ofPA which contains X+ (or a component of X+ in the
case whenX is a link) as one of its boundary components. We consider the foliation
ofS which is induced by the foliation onPA . A (possibly empty) family of s–arcs
S ={s1,..., sl : si⊂S} is a complete collection of s–arcs inS if (i) no two s–arcs in
the collection split off a sub-band ofS that is foliated entirely by s–arcs, and (ii) for
any other s–arc s⊂PA there exists an si∈ S such that s∪ si splits off a sub-band
ofS that is foliated entirely by s–arcs. It is immediate that cutting S open along a
complete collection S of s–arcs decomposesS into a disjoint union of thin regions and
bands of s–arcs. This construction will be used in what follows.
The grey boundary of the thin annuli will in general be in the interior ofPA , although
in special cases it will coincide with X−. Observe that the difference in braid index
b(X+)− b(X−) across the union of the annuli which make upS is the total number of
positive vertices inS minus the total number of negative vertices inS . From Figure 43
we see that this difference is always either 0, 1 or−1 in a single non-trivially foliated
region. Thus the motion of X+ acrossS to X− increases braid index if and only if
there are more regions of type −1 than of type +1 inS . The regions of type 0 do
not affect the count. We call our regions types 1 d,−1d, 0d,1 and 0 d,2, the subscript
indicating that the region is a disc. (The two cases of type 0 d are distinguished by the
placement of their clasp arcs.) There is also the special case of the standard annulus.
The standard annulus ﬁrst appeared in Corollary 5.1.2 as an embedded annulus. We are
now allowing for the occurrence of clasp arcs.
The previous construction of a thin annular subset S inPA has X+ as one of its
boundary components. But, we can also use the same construction to produce a thin
annular subset which has X− as one of its boundary components. LetS+ (resp.S−) be
the thin annular subset ofPA having X+ (resp. X−) as one of its boundary components.
Notice thatS−, like S+, will have type 0 d, 1d,−1d regions that are connected by
Geometry &Topology 10 (2006)
486 Joan S Birman and William W Menasco
s–bands. However, the dotted grey boundary will be replaced by a solid grey boundary
since it will now be X−; and the solid black boundary will be replace by a dotted black
boundary since it may or may not be X+.
Referring to the regions in Figure 43 we consider the cyclic ordering of the singularities
in H. We say a type 0 d,1 or 1 d (resp. 0 d,2 or−1d ) region is a fan if all of its
singularities of parity−δ (resp.δ) occur in sequence in the ﬁbration, followed by all of
its singularities of parityδ (resp.−δ).
We now have a proposition that allows us to useb(X+) and b(X−) to limit the occurrences
of these regions inS+ andS−. It will play a key role, later, when we prove the ﬁniteness
of the set of templates. (Look ahead to part (6) of Lemma 6.3.2 in Section 6.)
Letρ :PA→CA be the natural immersion.
Proposition 5.3.1 The annular regionsS+,S−⊂PA contribute to b(X+) and b(X−)
in the following ways.
(1) The number of type 1d regions inS+ is bounded by b(X+).
(1′) The number of type−1d regions inS− is bounded by b(X−).
(2) IfR1⊂S + is a type 0d,1 region andR2⊂S + is a type 0d,2 region with
ρ(R1)∩ρ(R2)⁄=∅, then the pair (R1,R2) contributes at least +1 to b(X+).
(2′) IfR1⊂S − is a type 0d,1 region andR2⊂S − is a type 0d,2 region with
ρ(R1)∩ρ(R2)⁄=∅, then the pair (R1,R2) contributes at least +1 to b(X−).
(3) SupposeR1,R2⊂S + are regions of type 0d.1 and 0d,2 and thatR3⊂S + is a
region of any type that is a fan. Assume that
(a) ρ(R1)∩ρ(R3)⁄=∅,
(b) ρ(R2)∩ρ(R3)⁄=∅,
(c) R1 andR2 are adjacent to a common s–bandRs.
Then the triple (R1,R2,Rs) contributes at least +1 to b(X+).
(3′) SupposeR1,R2⊂S− are regions of type 0d.1 and 0d,2 and thatR3⊂S− is a
region of any type that is a fan. Assume that
(a) ρ(R1)∩ρ(R3)⁄=∅,
(b) ρ(R2)∩ρ(R3)⁄=∅,
(c) R1 andR2 are adjacent to a common s–bandRs.
Then the triple (R1,R2,Rs) contributes at least +1 to b(X−).
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 487
Proof of (1) Consider a type 1d region. Its boundary is a union of two s–arcs, labeled
s and s′, and subarcs x+, x− of X+, X−. Let Hθ, Hθ′ be the ﬁbers which contain s, s′.
Then x+ (resp. x−) begins on Hθ , travels around the braid axis some number of times,
staying transverse to ﬁbers, and ends at Hθ′ . Since there are more positive than negative
vertices in a type 1 d region, it follows that x+ makes at least one more circuit about
the braid axis than x−. In particular, x+ makes at least one full circuit about A and so
contributes at least 1 to b(X+).
Proof of (2) Sinceρ(R1) and ρ(R2) intersect along a common clasp arc, we can cut
open their preimages in the thin annulus subset S ofPA along the two components of
the clasp arc. Paste them together in the unique new way to obtain two new regions
which resemble type 1d and−1d regions in S. Observe that, while the new regions look
like they are type±1d , their images inCA will have the property: the Xϵ boundary,
ϵ =±, say xϵ will be a union of two arcs, xϵ,1∪ xϵ,2, where the ﬁnal endpoint of xϵ,1
and the initial endpoint of xϵ,2 are on the same ﬁber, but are at different points of that
ﬁber. We call this a ‘surgery’. After the surgery, we may use the same argument that we
used to prove (1), to show that the angular support of x+,1∪ x+,2 is 2π greater than the
angular support of x−,1∪ x−,2. Therefore x+,1∪ x+,2 contributes at least 1 to b(X+).
Proof of (3) We have the following list of possibilities:
Case (i) R1 andR2 have different types, sayR1 is type 0d,1 andR2 is type 0d,2.
(ia) As we traverse X+ onR3 we encounter an a+–arc that is adjacent to a clasp
arc thatR3 shares withR1 before we encounter an a+–arc that is adjacent to a
clasp arc thatR3 shares withR2.
We surger our three regionsR1,R2 andR3, inPA , along the pre-images of the
clasp arcs inρ(R1)∩ρ(R3) and ρ(R2)∩ρ(R3). Since the angular support for
Rs is either contained within the angular support of X+∩R 3, or is outside the
angular support of X+∩R 3, the angular length of X+∩ (R1∪R s∪R 2) must
be greater than 2π. (Conceptually,R3 creates an ‘adequate amount of spacing’
betweenR1 andR2 so that the triple (R1,R2,Rs) contributes +1 to b(X+).)
(ib) As we traverse X+ onR3 we encounter an a+–arc that is adjacent to a clasp
arc thatR3 shares withR2 before we encounter an a+–arc that is adjacent to a
clasp arc thatR3 shares withR1.
We need to consider the positioning of the s–band,Rs, that runs fromR1 toR2.
If the angular length ofRs is greater than 2π then we are done. So assume that
the angular length ofRs is less than 2π. Next, we can assume that the angular
length of X+∩R 3 is also less than 2π.
Now, a convenient way of accounting for braid index is to line up the foliations of
R1,R2 andR3 (which are still thought of as being inPA ) so that corresponding
Geometry &Topology 10 (2006)
488 Joan S Birman and William W Menasco
clasp arcs line up. (For examples the reader should jump ahead to Figures 48 and
50). Since our argument is concerned with the measurement of angular length
we need only focus on where we start and end this measurement. It is convenient
to use the endpoint of a clasp arc in R1 (orR2) as our starting point and the
endpoint a clasp arc inR2 (or, reversing the interplay,R1) as our ending point.
Thus, as a simplifying measure in drawing such a illustration we can focus in on
the portion of the foliation ofR1 andR2 where these clasp arcs are placed, for
each such portion of the foliation has just two vertices, two singularities and a
single clasp arc. Consider the position ofRs in this superimposed picture. IfRs
is not next toR3 then we can again do a cut-and-paste to produce a topological
annulus that contributes +1 to the braid index of b(X+). If Rs is next to the
foliation ofR3 then it is easy to see that X+∩ (R1∪R s∪R 2) contributes +1
to b(X+). In the superimposed image ofR1∪R s∪R 2 inR3 it can be seen that
X+∩ (R1∪R s∪R 2) bounds a type 1 d region. Again, the assumption thatR3
is a fan is not needed. (In the right sketch of Figure 48(ii), the short s–band that
runs from dot g to dot c′ is an example of an s–band that would be superimposed
in the foliation of the right sketch in Figure 48(ii).
Case (ii) R1 andR2 are both type 0d,1 (or both type 0d,2). Suppose regionsR1,R2
are of type 0 d,1 andR3 is a region that is a fan. We now employ this procedure of
superimposing the foliations ofR1 andR2 onto the foliation ofR3. We again consider
the positioning ofRs. As before we assume that the angular support ofRs and X+∩R 3
is less than 2π. When we superimposeR1∪R s∪R 2 ontoR3 we will see two copies
of a type 0d,1 region side-by-side. (Please refer to Figure 43 for a understanding of the
labels s and s′.) We have two sub-possibilities:
(iia) Rs runs from the s′ label of the left region (which will beR1 in our side-by-side
image) to the s label of the right region, which isR2.
Notice that the cyclic ordering of the singularities inR3 imposes an order on the
singularities ofR1 andR2 where they intersectR3. Thus, sinceR3 is a fan the
−δ singularity inR1 must occur after theδ singularity inR2. (Recall we are
making the simplifying assumption thatR1 andR2 only have two singularities.)
So the angular support of Rs must overlap with the angular support of ∂R1
forcing X+∩ (R1∪R s) to have angular length greater than 2π. Thus, the triple
(R1,R2,Rs) contributes +1 to b(X+).
(iib) Rs runs from the s label of the left region, which isR1, to the s′ label of the
right region, which isR2.
We cut-and-pasteR1,R2,R3 to produce a type 0d,1 region having a portion of
X+ in its boundary but sheared in two places. If we adjoinRs to this new 0d,1
region we see that the resulting X+ boundary contributes +1 to b(X+).
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 489
The proofs of (1′), (2′) and (3′) are almost identical to the proofs of (1),(2),(3), and we
leave them to the reader.
5.3.2 Using ﬂypes to push X+ acrossS
In this subsection we assume thatS is a collection of thin (but not standard) annuli.
The case of standard annuli will be considered separately, in Section 5.7.
To simplify the notation, we use ‘ bold-faced type’ for the black boundary and all
its auxiliary structures; and ‘Roman type’ for the grey boundary and all its auxiliary
structure. In particular, S is foliated by s–arcs, a–arcs (adjacent to X), b–arcs and
a–arcs (adjacent to X). (We will specify further auxiliary structure in due course.)
Thus, ifS⊂CA is thin, then∂S = X∪ X where X⊂CA is on the X+ side ofS in
CA , and X⊂CA is on the X− side ofS inCA .
The main goal of this section is to establish that the isotopy of X acrossS to X is the
result of a collection of ﬂypes, not necessarily all admissible. Speciﬁcally, givenS we
will produce a recipe for constructing a template ( D, D) where, via a common braiding
assignment to the blocks of D and D, we have that D carries X and D carries X. Our
recipe will tell us how to designate blocks of both ﬂavors (ﬁxed and moving), and how
to designate the strands connecting the blocks. Moreover, we will show how the thin
structure ofS gives rise to a collection of ﬂypes that carries D to D.
To motivate our work, we begin with examples. The key to understanding the moving
blocks will be a ‘block amalgamation’ process. Here we give two examples which
illustrate: (i) how the clasp arcs of S are used to designate the microblocks ﬁrst
mentioned in Section 5.2; (ii) how the foliation of S is used to amalgamate the
microblocks into larger moving blocks; and how the foliation ofS is used to ﬂype these
moving blocks.
Example 1 is illustrated in Figures 48 and 49. Figure 48(i) depicts two regions of the
preimage ofS sharing two clasp intersections,γ1 andγ2. For each clasp intersection
inS there is a readily identiﬁable pair of tab neighborhoods in the preimage (just look
at what remains after stabilizing X (resp. X) along the singular leaf θ4 (resp.θ3)). So
for each microﬂype we have an associated microblock that contains a positive full twist.
Figure 48(i) coupled with the left sketch in Figure 49 illustrates the strands in the two
microblocks: strands ab and df are associated with the microblock for γ1; and strands
a′b′ and d′f′ are associated with the microblock forγ2.
Next, notice that the foliation ofS yields the following sequence of isotopies for moving
X to X: in Figure 48(i)–(ii) we stabilize X along theθ4 singular leaf; in (ii)–(iii) we
Geometry &Topology 10 (2006)
490 Joan S Birman and William W Menasco
-
-
- -
+
+
- -+
+
+
+
+
+
+
+
-
+
+
++
+ -
+
+
-
-
-
-
+ -
-
Figure 48: The isotopy of X+ acrossS in a simple example
+
+
+
+
a
e
b
d
f
g′
c′
d′
f′
g
c
a′
b′
e′
axis
a
e
b f
d g′
a′
e′
b′
d′
f′ c
a
b
a′
b′
f
d′
g′
c
ﬂype
a
b′
g′
c
Figure 49: The 3–space embedding of X+ and X− in the Example in Figure 48
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 491
perform two microﬂypes; and in (iii)–(iv) we destabilize X. The geometric realization
of Figure 48(ii) is depicted in the left sketch of Figure 49. (The alphabetic labeling of
points on X and X are meant to correspond between the two ﬁgures and the reader is
encouraged to check the details of this correspondence.)
Now observe that the right two sketches in Figure 49 illustrates an amalgamation between
the two full twists of the microblocks, allowing us to consolidate this stabilization,
microﬂypes, destabilization sequence into a single ﬂype. Also, observe that the two
regions in Figure 48(i) will be fans. This can be veriﬁed by checking the ordering of
the angular support of the edgepaths cdefd′e′f′g′ and aba′b′ that are in X, along with
the corresponding angular support of the analogous edgepaths in X, since all singular
leaves have an endpoint on the boundary of these regions.
+
+
-
-
-
+
+
(i) (ii) (iii) (iv)
a
b
a′
b′
c
d
e
f g
c′
d′
e′
f′ g′
a
c
b
d
e
f
g
a′
c′
b′
d′
e′
f′
g′ a
b′ cc′
g g′
Figure 50: Amalgamating microﬂypes can result in ﬂypes with weighted strands
The three regions ofS for Example 2 are illustrated in Figure 50(i) and (ii). Again,
there are two clasp intersections in S along with two pairs of tab neighborhoods
which clearly delineate the microﬂypes and microblocks associated with each clasp
intersection. Figure 50(iii) shows the geometric realization of X: strands ab and df
properly contains a full twist in one microblock; and strands a′b′ and d′f′ properly
contains a full twist in the another microblock. And, again the foliation ofS supplies us
with a sequence of stabilizations, microﬂypes, destabilization for moving X to X: the
starting stabilization is along the segment ba′⊂ X; perform the two microﬂypes; and
then do the two remaining destabilizations. The question is, can we amalgamate the two
microblocks to achieve a three strand block that would contain the braiding depicted in
Figure 50(iv)? The answer is that the information in the foliation is ambiguous; we
have not assigned any angular information to the singularities in Figure 50(i) and (ii). In
Geometry &Topology 10 (2006)
492 Joan S Birman and William W Menasco
Figure 50(iii) we have illustrated the point f (resp. d′) as occurring after (resp. before)
the point b′ (resp. d) in the ﬁbration, however there is no information in Figure 50(i)
and (ii) that forces this choice. The occurrences might have been reversed. If they were
reversed then the amalgamation of Figure 50(iv) would not have been possible. Thus,
the foliation of Figure 50(i) and (ii) could depict either one braid -index-decreasing
ﬂype with a three strand block, or two elementary ﬂypes followed by a destabilization.
As in Example 1 of Figure 48, it is easy to see that the region in Figure 50(ii) will be a
fan. This will be independent of how the amalgamation of blocks occurs.
Example 3 (see Figure 51) shows a situation where successive ﬂypes cannot be
amalgamated. We see four ﬂypes, with associated braid blocks X,Y ,Z,W. In the initial
diagram it looks as if it might be possible to amalgamate X and Y , but if we study the
ﬁnal diagram we see that this is impossible.
W
X
Y
Z
W
X
Y
Z
Figure 51: Four independent ﬂypes which cannot be amalgamated
Remark 5.3.1 Observations based on these examples lead us to the following remarks
about thin annuliS :
(i) The foliation ofS enables us to readily identify tab neighborhoods of clasp arcs.
(ii) For each pair of tab neighborhoods (where the pairing is via the pairing of the
clasp arcs) we have an associated microﬂype and microblock. By our parity
conditions on the singularities of a region (refer to Figure 43) we know that all of
the microﬂypes associated with a particular region are of the same parity, ie either
all positive ﬂypes or all negative ﬂypes. In particular, any type 0 d,1, 0d,2, 1d,−1d
region used in a ﬂype will be a fan.
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 493
(iii) We can moveX across the regions ofS to X through a sequence of stabilizations
of X, microﬂypes and destabilizations of the resulting new X. ♦
Recall that our main goal in this subsection is to establish that the isotopy of X across
S to X is the result of a collection of ﬂypes, not necessarily all admissible. For that
we need to understand when it is possible to amalgamate a collection of microblocks
into a larger block that is moved by a ﬂype. So let us ﬁnally formalize the deﬁnition of
‘amalgamation’. To do this we ﬁrst need to re-characterize microblocks in term of the
foliation ofS .
By hypothesis, all clasp arcs inS are doubly long. In particular, there are no short clasp
arcs. For any pair γi
+,γ i
− we have pushed both arcs into a chains of leaves. (For thin
annuli these chains will always have exactly two leaves.) Sinceγi
+ begins on X, one of
the endpoints of γi
+ is a point qi
+∈ X. The fact that γi is doubly long shows that one
of the endpoints of γi
− is also near X. The singular leaf which contains it ends at a
point qi
−∈ X. Since our clasp arc is doubly long, there is an analogous picture near
X. Both are illustrated in Figure 52. The part of CA that belongs to the two normal
neighborhoods runs all the way from the black boundary to the grey boundary. The two
normal neighborhoods intersect along the clasp arc.
xi
−
qi
+
qi
−
xi
+
γi
qi
+
xi
+
xi
− qi
−
Bi
Bi
γi γi
(i) (ii) (iii)
Figure 52: (i) The four microstrands associated to a doubly long clasp arc. (ii) The associated
microblocks. (iii) The braid projection of the microstrands on the cylinder walls.
We ﬁx subarcs xi
+ and xi
− of X, where xi
+ (resp. xi
−)) is a closed neighborhood of
qi
+ (resp. qi
−) on X. The subarc xi is chosen so that it does not intersect the subarc
associated to adjacent singular leaves on X, also so that the arcs xi
+ and xi
− have the
Geometry &Topology 10 (2006)
494 Joan S Birman and William W Menasco
same angular support [θi1,θ i2]⊂ H. We call these arcs the black microstrands. There
are, of course, similar thick grey microstrands xi
+ and xi
− of X. Notice that the isotopy
of X acrossS pushes X across Ni
+ (resp. Ni
−) to X, so the two black microstrands are
mapped to the two grey microstrands.
Construct disjoint solid cylinders Bi, Bi in 3–space which have the structure of blocks,
as deﬁned in Section 1 of this paper. These cylinders are, of course, microblocks,
as deﬁned in Section 5.2. The microblock Bi is foliated by discs and contains the
braided arcs xi
+ and xi
−, which meet the disc ﬁbers transversally inside Bi. It intersects
the ﬁbers of H in the interval [θi1,θ i2]. We also have, without further work, a grey
microblock. (See Figure 52(ii).)
There is an additional and very important feature of the geometry: The fact that our
clasp arcs are doubly long tells us, immediately, that the two tab neighborhoods of
the clasp arcs reach all the way from X to X, joining the black and grey microblocks.
In fact, they intersect the side boundaries of the black (resp. grey) microblocks, and
the intersection is a pair of intersecting arcs. We label the double points of the black
and grey projection with the index ofγi. (See Figure 52(iii).) We can think of these
crossed arcs as ‘local projections’ of the microblocks. The very interesting feature of
this projection is that the black and grey projections are joined to one-another by the tab
neighborhoods of γ+ and γ−. (This is easy to see in Figure 52(ii), even though we
omitted it to keep the picture as simple as possible).
Construct the black and grey microblocks, {B1,..., Br} and{B1,..., Br}, one for
each clasp arc in S. Let B⊂ S3\ A be a 3–ball having the structure of a 2–disc
cross an interval, ∆2× [0, 1]. Decompose ∂B as c∪ t∪ b, where c =∂∆2× [0, 1];
t = ∆2×{0}; and b = ∆2×{1}. (Our notation was chosen to suggestt for ‘top’;c for
‘cylinder’; andb for ‘bottom’.) ThenB is an amalgamating block for the microblocks
{B1,..., Br} associated to the microstrands{x1
+, x1
−,... xr
+, xr
−} ofS if the following
hold:
(1) Each Bi⊂ int(B) for i≤ i≤ r.
(2) Its support, ie{θ| B∩ Hθ⁄=∅}, is a closed interval having length less than 2π.
Every component of X∩ B contains a microstrand.
(3) The top t and bottom b of∂B are contained in generic disc ﬁbers ofH. Moreover,
each component of t∩S (resp. b∩S ) is a subarc of ana–arc having one endpoint
on∂t (resp.∂b) and one endpoint on X. The leaves of the induced foliation on
c⊂∂B are circles. The only non-singular leaves that c intersect are a–arcs and
c∩ X =∅.
(4) If xi
+ (resp. xi
−)⊂ int(B), then its partner xi
− (resp. xi
+) is also a subset of
int(B). Also, the dotted segment between each qi
+ and qi
− is a subset of int(B).
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 495
(5) Replacing
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
−}}
we can also deﬁne the amalgamation of microblocks{B1,..., Br}.
Our next question is: what conditions need to be met so that we can say the isotopy
acrossS takes B to B? A hint comes from Figure 52(iii). Consider the projection of
the microstrands in Bi onto its cylinder boundary and the projection of the microstrands
in Bi onto its cylinder boundary. Notice that these two projections are reﬂections of
each other. This observation leads us to the following two deﬁnitions.
First, let B be an amalgamating block. The braid projectionπ(B) of X+ onto c⊂∂B
is the graph c∩S , regarded as a subset of c together with the clasp arc index labeling
of this graph’s double points. We deﬁneπ(B) in a similar fashion.
Second, amalgamating blocks B and B are a pair of related amalgamating blocks if the
following hold:
(a) {B1,..., Br} and{B1,..., Br} are microblocks associated with clasp intersec-
tions{γ1,...,γ r}.
(b) B is a block amalgamation of microblocks{B1,..., Br}.
(c) B is a block amalgamation of microblocks {B1,..., Br}.
(d) π(B) and π(B) are reﬂections of each other.
Recall Figure 51 and see Figure 53 for an example.
Proposition 5.3.2 LetS be a collection of thin annuli with boundary components
X and X. Then the motion of X to X may be realized by a collection of ﬂypes and
destabilizations.
Proof We will construct a pair of candidates for block-strand diagrams (D, D) such
that D (resp. D) carries X (resp. X) and the motion D→ D is a sequence of ﬂypes.
We say that our diagrams (D, D) are merely candidates for block-strand diagrams is
that condition (4) in the deﬁnition of a block-strand diagram may not hold. Indeed, it
may be difﬁcult to verify whether (4) does or does not hold at this stage of the argument.
For example, it’s possible that we could amalgamate blocks, and so produce new blocks
which have full braid index. That is a matter which we are not ready to discuss at this
time. (Look ahead to Section 6.2 for more on this. See, in particular, Corollary 6.2.1).
However, if we can construct D and D so that they carry X and X, and prove that the
Geometry &Topology 10 (2006)
496 Joan S Birman and William W Menasco
γ1 γ2 γ1 γ2
Figure 53: The projection of related microstrands onto the cylindrical walls in the boundaries of
amalgamating blocks
motion D→ D is a sequence of ﬂypes and destabilizations, we will have accomplished
our task.
To construct D and D we need to understand several aspects of their structure. Observe
that the strands of X which change position during the passage to X are precisely those
which bound the ‘tiled’ part ofCA , that is the part which is away from the bands of
s–arcs. On the other hand, the part that stays ﬁxed is the part that intersects the bands
of s–arcs. So we can consider, separately, the ‘moving’ and ‘ﬁxed’ parts of (D, D):
Moving blocks An amalgamating block B will be moved to an amalgamating block
B if and only if they are related amalgamating blocks, as deﬁned above. Note that there
may be some choices involved when we select the amalgamating blocks. We make
those choices in such a way that the set of all moving blocks has minimal cardinality.
Moving Strands The moving strands in D are all subarcs of X which are not
amalgamated into moving blocks and are not in the bands of s–arcs.
Fixed blocks Here is the intuitive idea: The ﬁxed blocks are associated to braiding
between the strands of X (and so also of X) in the part of S which is foliated by bands
of s–arcs. The braiding between bands of s–arcs is not part of our geometry.S only
detects the places where X and X differ in a non-trivial way, but in regions where there
are bands of s–arcs they essentially coincide. However, what might happen is that there
is braiding between the bands of s–arcs, but that the braiding is interrupted by, for
example, strands of X which separate two potential blocks. In order to determine the
angular regions where the blocks occur, we therefore look for singularities in the tiled
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 497
part ofS . The block subdivision so-obtained will be too extensive, and we will then
need to amalgamate ﬁxed blocks.
We consider the Hθ –sequence forS . Let Stiled⊂S be the portion ofS that is not
foliated by s–arcs. Let{θ0,θ 1,...,θ ζ}⊂ [0, 2π) be a cyclic listing of all the angles
at which the corresponding Hθi∈ H contains a singularity, ordered according to their
natural cyclic order in H. Since the bands of s–arcs are foliated without singularities,
they must be located in
H′ =
i=ζ⋃
θ∈(θi,θi+1), i=0
{ Hθ \ Hθ ∩S tiled}.
Each component of H′ is a disc, and it contains only s–arcs. Let C be a connected
component of H′. Then C has a ∆2× [θi,θ i+1] structure, and it may contain some
number of bands of s–arcs which braid with one-another insideC. If so, we amalgamate
this braiding of s–arc bands in C into a single block B(C), which will be a ﬁxed block
in the template ( D, D). If C has no s–arcs then B(C) is vacuous. If C has a single
s–arc then B(c) is a single ﬁxed strand.
Suppose that there is another connected component C′ in H′, with its ﬁxed block B(C′),
and suppose further that {s− arcs}∩ C′∩ Hθi+1⊂{ s− arcs}∩ C∩ Hθi+1 . If this
happens, the singularity at θi+1 could have been ignored. Another way to say this is
that we can amalgamate the blocks B(C) and B(C′) into a larger ﬁxed block of the
template B(C∪ C′) of (D, D). There may be some choices involved, and we make them
so that the set of all ﬁxed blocks has minimal cardinality.
Fixed strands It may happen that we have two blocks, B(C) and B(C′), for which
(C∩ Hθi+1)∩ (C′∩ Hθi+1)⁄=∅, but (C∩ Hθi+1)⁄= (C′∩ Hθi+1), so that the amalgamating
condition fails. In this situation there are strands that run between B(C) and B(C′),
however not all of the s–bands coming out of B(C) go into B(C′), and/or not all of the
strands going into B(C′) are strands that emerge from B(C). Any braiding between the
s bands that run between B(C) and B(C′) can obviously be pushed into either B(C) or
B(C′) (eliminating Hθi+1 as a singular ﬁber) and they will then become ﬁxed strands.
It is clear from the construction of (D, D) that the template ( D, D) carries ( X, X).
We still need to show that for each moving block pair (B, B) we have a ﬂype (possibly
with weighted strands) taking B to B as in Figure 4(a). To do this we ﬁrst need to
isolate each moving black block. Speciﬁcally, we wish to subdivide the foliation ofS
so that there is a subannular regionS′⊂S such that if y⊂ X is a strand of D then
y intersects s–arcs in the foliation ofS′. We refer to Figure 54 to see howS′ can be
obtained through the stabilization of X. Suppose we have two clasp intersections γi
Geometry &Topology 10 (2006)
498 Joan S Birman and William W Menasco
andγj where the black microblock associated withγi is in an amalgamated black block
B(i) and the black microblock associated withγj is in an amalgamated black block B(j).
Let y⊂ X be a strand of D that has its endpoints on B(i) and B(j). Since y is a strand it
- -
+
-
+
- -
+ ++
- -
+ ++
+
--
++
- -
+
-
++
- -
+
-
+
+
-
+ +
-
- -
++
- -
(a)
(b)
(c)
(d)
gi
+ gj
+ gi
+ gj
+
gi
− gj
− gi
− gj
−
−δ
gi
+
gj
−
gi
+
gj
−
gi
−
gj
+
gi
−
gj
+
−δ
Figure 54: Subdividing non-trivially foliated regions in S . The black (resp. dotted grey)
horizontal arcs are the arcs we refer to in the text as ‘ y’ (resp. ‘y’). The intersections of the
clasp arcs with the regions of interest are labeled gi
± and gj
± .
cannot intersect any microstrands of X. Thus, it either intersects s–arcs in the foliation
ofS (in which case no subdivision is necessary), or the only non-singular leaves it
intersects are a–arcs. To describe the needed subdivision in the latter situation, we
look at the corresponding grey microblocks associated with our two clasp intersections;
the corresponding grey amalgamating blocks B( i) and B( j); and the corresponding
grey strand y⊂ X which has endpoints on B( i) and B( j). By assumption, the only
non-singular leaves intersected by the strand y are a–arcs in the foliation of S . If y
intersects an ab–singular leaf (as illustrated in Figure 54(a)) then we can stabilize X
along this singular leaf to produce a subannulus ofS that has y intersecting s–arcs. If
the strand y does not intersect an ab–singular leaf then we can enlarge the foliation ofS
thru the addition of two vertices and singularities, as illustrated in the three remaining
sequences, Figure 54(b)–(d). (The new b–arc will necessarily be inessential.) The
strand y will now intersect the endpoint of an ab–singular leaf and a stabilization of X
is possible. The corresponding black strand y will then intersect s–arcs in the resulting
S′, isolating the block B(i) from the block B(j).
LetS′⊂S be thin subannuli that isolate all the moving blocks. Then there is a pair
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 499
+ + + +
stabilization
ﬂype 1 braid isotopy ﬂype 2
destabilization
ﬂype
P
Q
P
Q
P
Q PQ
P
Q
P
Q
Figure 55: An example that shows how a stabilization, two microﬂypes and a destabilization are
amalgamated into a ﬂype. The bottom left and right sketches show the corresponding subsets of
D and D. The top right sketch illustrates the part of the diagram that we refer to as D′ in the
text.
(D, D′) where D′ is obtained from D by the stabilizations in the subdivision of Figure 54.
Part of it is illustrated in Figure 55. Saying the moving blocks of ( D, D′) are isolated is
saying that every strand of D or D intersects s–arcs in the foliation ofS′. Now, if we
can show that moving acrossS′ is a collection of ﬂypes, then it will follow that the
destabilizations come from going from D′ to D.
To show that the isotopy across S′ takes D to D′, using a collection of ﬂypes, we
proceed as follows: since the blocks are isolated, we need only consider what the isotopy
is for one block. This means we are back in a situation similar to that of Example 1
and Example 2 at the beginning of this section. We have a subcollection of regions
{R1,..., Rh}⊂S ′ in the foliation ofS′ (as deﬁned in Section 5.3.1) that are grouped
together by clasp intersections. These regions are all either type 0 d,1, 0d,2, 1d or−1d .
All of the associated microblocks of the clasp intersections of this collection of regions
can be amalgamated into a block pair (B, B). Our claim is that the isotopy of B across
the regions{R1,..., Rh} to B is a ﬂype. By statement (ii) of Remark 5.3.1 we know
that we can subdivide the microblocks in B and ﬂype them across to the microblocks in
B. Also, the fact π(B) and π(B) are reﬂections tells us that we can re-amalgamate them
into B. In the simplest case of a subdivision into two blocks (Figure 55) we see that
the entire isotopy of statement (ii) of Remark 5.3.1 can be consolidated into a single
ﬂype. This situation can obviously be generalized into a larger number of blocks in the
subdivision by an iterated nesting, the ﬁrst iteration being: before doing ‘ﬂype 1’ we
Geometry &Topology 10 (2006)
500 Joan S Birman and William W Menasco
subdivide block P into two new blocks and, since block P in the upper-left sketch could
have been ﬂyped, perform the entire sequence on these two new blocks ﬁrst. Thus, B is
ﬂyped to B and the proof of Proposition 5.3.2 is complete.
Example 5.3.1 The projection criterion is essential to choosing block amalgamations
that maintain their integrity during a ﬂype isotopy. This is clear from the example that
we gave earlier, in Figure 51. Before the ﬂype it looks as ifX and W (and also Y and Z )
can be amalgamated, but after the ﬂype that is impossible. Indeed, the requirement that
the projections be reﬂections of each other will be violated if we attempt to amalgamate
X and W , or Y and Z. ♦
