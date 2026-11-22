---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-029-531-constructing-the-thin-annuli
section_title: "Constructing the thin annuli"
section_number: 5.3.1
pages: 69-77
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Constructing the thin annuli
Preparing for the shortening of long clasp arcs, we will construct a family S of ‘thin
annuli’ which is a subset of PA. Normal neighborhoods will play a key role in the
construction. We will prove:
Lemma 5.3.1 Assume that X has µ components. Suppose that PA contains long
clasp arcs γi
+, γj
+, i̸ = j. Then there exists a family S of µ annuli, each a subannulus
of PA, and each with a component of X+ as one of its boundaries, such that every
annulus in S is either trivially foliated by s–arcs, or is a standard annulus, or has a
foliation satisfying the following (see Figure 43 for examples):
(i) Each non-trivially foliated annulus contains at least one long clasp arc. Moreover,
all of its clasp arcs are doubly long and of length 1, with respect to the induced
foliation of S.
(ii) After an isotopy of PA which leaves X+ and the other components of ∂S ﬁxed,
each b–arc in S may be assumed to have at least one of its endpoints on a clasp
arc.
Proof The case when there is exactly one long clasp arc was just discussed in
Section 5.2, so we assume that there are at least two long clasp arcs. Let γi
+ be a long
clasp arc, so that γi
−begins on X−and ends near X+. Assume that γi
+ and γi
−have
been pushed into a union of leaves in their normal neighborhoods. This is possible,
by the construction in Proposition 4.5.1. Let Ni
−be the normal neighborhood of γi
−.
Geometry & Topology 10 (2006)
482
Joan S Birman and William W Menasco
We focus our attention on a rectangle which we call N
i
−. See sketches (1) and (2) in
Figure 45. It is a subset of Ni
−, and it coincides with Ni
−when the clasp arc has length
2. It has three edges which are in ∂Ni
−. We choose an arc which is transverse to the
foliation as its other ‘horizontal’ boundary.
+
+
-
-
+
+
-
-
+
+
-
-
+
+
-
-
(1)
(2)
(3)
(4)
δ
−δ
δ
−δ
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
−δ
δ
γi
−
γi
−
γi
+
γi
+
Figure 45: Sketches (1) and (2) illustrate the two possibilities for N
i
−. Sketches (3) and (4)
illustrate the two possibilities for N
i
+.
There are corresponding subrectangles N
i
+ and we show the two possible arrangements
in sketches (3) and (4) of Figure 45. As in the case of N
i
−, the rectangle N
i
+ has 3
boundary edges which are in ∂Ni
+. We choose its 4th boundary edge to be an arc which
is transverse to the foliation, so that the rectangle has 4 vertices and 4 singularities.
In the special case when γi
+ has length 2 the puncture endpoint of the arc γi
+ will be
an interior point of N
i
+, but if γi
+ has length ≥3 then γi
+ ∩N
i
+ will have both of its
endpoints on the boundary. We correct this by modifying γi
+ ∩N
i
+ to a subarc of γi
+
which has the same image in CA as the intersection of γi
−with its induced normal
neighborhood. This will give us a shortened induced arc which (by an abuse of notation)
we continue to refer to as γ+. It begins on X+ and ends at a point in the interior of
N
i
+. By construction, γi
−and the new γi
+ have the same image in CA, and determine
the clasp intersection between the rectangles N
i
−and N
i
+ which is induced by the
clasp intersection in CA corresponding to γi. The four cases which are illustrated in
Figure 45 will be referred to as types (1),(2),(3),(4).
Let NS be the union of all of the N
i
−and N
i
+. Note that, while N
i
± ∩(γj
−∪γj
+) = ∅
for all j̸ = i, there is no reason why N
i
± ∩N
j
± should be empty. This leads us to the
following preliminary deﬁnition of a connected collection of normal neighborhoods:
Choose N, N
′ ∈NS . We say that N and N
′ are connected, and write N ←→N
′, if
N ∩N
′̸ = ∅in PA. Two examples are given in Figure 46. In the top row, N has
type 1 and N
′ has type 2 and N ∩N
′ = ∂N ∩∂N
′. In the middle row N has type
1, N
′ has type 3 and they intersect along two singular leaves and the disc between
them. Observe that this is the maximal possible intersection, because the normal
neighborhood of a clasp arc never intersects another clasp arc. It follows that the
possible sequences in a connected set are 12, 13, 14, 23, 24, 34, 21, 31, 41, 32,
42, 43. A collection of normal neighborhoods {N
1, . . . , N
p} ⊂NS is connected
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
483
+
-
-
+
-
+
+
-
+
-
+
-
+
+
-
-
+
-
-
+
-
-
+
-
+
-
-
+
+
+
-
+
+
-
+
+
-
-
-
12
13
eliminate
inessential
b–arc
eliminate
inessential
b–arc
(a)
(b)
(c)
(d)
γi
−
γj
−
γi
−
γj
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
−γj
−
γi
+
γj
+
γi
−
γj
+
γi
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
′, N
′′ ∈{N
1, . . . N
p} then there exists a subcollection {N
i1, . . . , N
iq} ⊂{N
1, . . . , N
p}
such that N
′ ←→N
i1 ←→N
i2 ←→· · · ←→N
iq ←→N
′′. A connected component of
NS is called a region and is denoted by the symbol R.
We now observe that each b–arc in each R is in a normal neighborhood of some clasp
arc. We distinguish between two types of b–arcs: those whose endpoints are vertices
which do not meet a clasp arc, and those which have at least one vertex endpoint which
is on a clasp arc. Let’s look ﬁrst at the former. Examples can be seen in the darkly
shaded subrectangles in the left sketches in rows 1 and 2 of Figure 46. Recall that
our normal neighborhoods were created by the repeated use of ﬁnger moves, which
necessarily created some inessential b–arcs. But all of the b–arcs which do not intersect
clasp arcs are inessential, and may be deleted by an isotopy of PA which is supported
on a disc in the interior of the connected region, as in the passage from the left to the
right in Figure 46. Therefore we may assume that R contains no such b–arcs. Notice
that we have chosen our deﬁnition of complexity so that this modiﬁcation does not
alter the complexity. With the modiﬁcation, it is easy to see that there are precisely 4
possible sequences of two modiﬁed normal neighborhoods, as illustrated in the bottom
row in Figure 46, sketches (a),(b),(c),(d).
A region R is either an annulus or a rectangle, as illustrated in Figure 43. If it is an
Geometry & Topology 10 (2006)
484
Joan S Birman and William W Menasco
annulus, then it satisﬁes properties (i)–(ii) of Lemma 5.3.1. Assume it’s a rectangle.
The lower horizontal boundary of R is a subarc of a component of X+, and so the
connected components R1, . . . , Rq associated to any given component of X+ have a
natural cyclic order on X+. We would like to use this natural order to join them by
bands of s–arcs to obtain annuli. However the vertical edges of the rectangles are not
s–arcs. The following observation saves the day: the grey dotted horizontal boundary
of each rectangle was chosen in a rather arbitrary way as an arc which is transverse to
the foliation and in the interior of PA, and if we now modify our choices by replacing
the vertical edges of the rectangles in (a),(b),(c),(d) by the sketches in (e),(f),(g),(h) of
Figure 47 we will be in business.
-
+
-
-
+
-
+
+
+
+
-
-
(e)
(f)
(g)
(h)
(e′)
(f′)
(g′)
(h′)
γi
+ γj
+
γi
−
γj
−
γi
−γj
−
γi
+
γj
+
Figure 47: Possible arrangements of clasp arcs in adjacent intersecting normal neighborhoods
in PA, near the right and left boundaries of a connected collection of normal neighborhoods
Sketches (e) and (f) are obtained from sketch (a) of Figure 47 by modifying the grey
boundary on the left and right respectively. Note that the modiﬁed grey boundary is
everywhere transverse to the leaves of the foliation. On the other hand, if we attempt
to do the same thing in the situation of (b), choosing the grey boundary to be close to
the left (resp. right) clasp arc, a point of tangency with leaves of the foliation will be
introduced, so it is necessary to include the singular leaf which is on the left (resp. right)
in the modiﬁed connected region, as illustrated in (g) (resp. (h)). We leave it to the reader
to check that (e) and (h) are modiﬁcations of (c), and that (f) and (g) are modiﬁcations
of (d). In (e)–(h), which are based directly upon the sketches in Figure 45, all have their
rightmost singular leaf in G−,δ. But there is a second possibility: we are given the
foliation near X+, and we do not know much about it outside the normal neighborhoods.
In fact there are 4 other possible patterns for the right and left boundaries, also restricted
by the fact that X+ must be transverse to ﬁbers of H. They are illustrated in sketches
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
485
(e′),(f′),(g′),(h′) of Figure 47, and were obtained from (e),(f),(g),(h) by interchanging
the roles of grey and black.
Let’s examine the possibilities for the regions. Figure 43 shows the foliated annulus and
the four possible foliated disc regions in S, up to the number of pairs of components
of G−,δ and G+,−δ. In each, we give examples of how the clasp arcs might be
placed. To construct S from the various non-trivially foliated regions we ﬁrst join disc
regions which are consecutive as one travels along a component of X+ with bands of
s–arcs which run between X+ and X−. We may also need some number of standard
annuli which have long clasp arcs. (See Figure 43 again.) Finally we may need some
number of annuli which are foliated entirely by s–arcs. This completes the proof of
Lemma 5.3.1.
Let S be an annular subset of PA which contains X+ (or a component of X+ in the
case when X is a link) as one of its boundary components. We consider the foliation
of S which is induced by the foliation on PA. A (possibly empty) family of s–arcs
S = {s1, . . . , sl : si ⊂S} is a complete collection of s–arcs in S if (i) no two s–arcs in
the collection split off a sub-band of S that is foliated entirely by s–arcs, and (ii) for
any other s–arc s ⊂PA there exists an si ∈S such that s ∪si splits off a sub-band
of S that is foliated entirely by s–arcs. It is immediate that cutting S open along a
complete collection S of s–arcs decomposes S into a disjoint union of thin regions and
bands of s–arcs. This construction will be used in what follows.
The grey boundary of the thin annuli will in general be in the interior of PA, although
in special cases it will coincide with X−. Observe that the difference in braid index
b(X+) −b(X−) across the union of the annuli which make up S is the total number of
positive vertices in S minus the total number of negative vertices in S. From Figure 43
we see that this difference is always either 0, 1 or −1 in a single non-trivially foliated
region. Thus the motion of X+ across S to X−increases braid index if and only if
there are more regions of type −1 than of type +1 in S. The regions of type 0 do
not affect the count. We call our regions types 1d, −1d, 0d,1 and 0d,2, the subscript
indicating that the region is a disc. (The two cases of type 0d are distinguished by the
placement of their clasp arcs.) There is also the special case of the standard annulus.
The standard annulus ﬁrst appeared in Corollary 5.1.2 as an embedded annulus. We are
now allowing for the occurrence of clasp arcs.
The previous construction of a thin annular subset S in PA has X+ as one of its
boundary components. But, we can also use the same construction to produce a thin
annular subset which has X−as one of its boundary components. Let S+ (resp. S−) be
the thin annular subset of PA having X+ (resp. X−) as one of its boundary components.
Notice that S−, like S+, will have type 0d, 1d, −1d regions that are connected by
Geometry & Topology 10 (2006)
486
Joan S Birman and William W Menasco
s–bands. However, the dotted grey boundary will be replaced by a solid grey boundary
since it will now be X−; and the solid black boundary will be replace by a dotted black
boundary since it may or may not be X+.
Referring to the regions in Figure 43 we consider the cyclic ordering of the singularities
in H. We say a type 0d,1 or 1d (resp. 0d,2 or −1d) region is a fan if all of its
singularities of parity −δ (resp. δ) occur in sequence in the ﬁbration, followed by all of
its singularities of parity δ (resp. −δ).
We now have a proposition that allows us to use b(X+) and b(X−) to limit the occurrences
of these regions in S+ and S−. It will play a key role, later, when we prove the ﬁniteness
of the set of templates. (Look ahead to part (6) of Lemma 6.3.2 in Section 6.)
Let ρ: PA →CA be the natural immersion.
Proposition 5.3.1 The annular regions S+, S−⊂PA contribute to b(X+) and b(X−)
in the following ways.
(1) The number of type 1d regions in S+ is bounded by b(X+).
(1′) The number of type −1d regions in S−is bounded by b(X−).
(2) If R1 ⊂S+ is a type 0d,1 region and R2 ⊂S+ is a type 0d,2 region with
ρ(R1) ∩ρ(R2)̸ = ∅, then the pair (R1, R2) contributes at least +1 to b(X+).
(2′) If R1 ⊂S−is a type 0d,1 region and R2 ⊂S−is a type 0d,2 region with
ρ(R1) ∩ρ(R2)̸ = ∅, then the pair (R1, R2) contributes at least +1 to b(X−).
(3) Suppose R1, R2 ⊂S+ are regions of type 0d.1 and 0d,2 and that R3 ⊂S+ is a
region of any type that is a fan. Assume that
(a)
ρ(R1) ∩ρ(R3)̸ = ∅,
(b)
ρ(R2) ∩ρ(R3)̸ = ∅,
(c)
R1 and R2 are adjacent to a common s–band Rs.
Then the triple (R1, R2, Rs) contributes at least +1 to b(X+).
(3′) Suppose R1, R2 ⊂S−are regions of type 0d.1 and 0d,2 and that R3 ⊂S−is a
region of any type that is a fan. Assume that
(a)
ρ(R1) ∩ρ(R3)̸ = ∅,
(b)
ρ(R2) ∩ρ(R3)̸ = ∅,
(c)
R1 and R2 are adjacent to a common s–band Rs.
Then the triple (R1, R2, Rs) contributes at least +1 to b(X−).
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
487
Proof of (1) Consider a type 1d region. Its boundary is a union of two s–arcs, labeled
s and s′, and subarcs x+, x−of X+, X−. Let Hθ, Hθ′ be the ﬁbers which contain s, s′.
Then x+ (resp. x−) begins on Hθ, travels around the braid axis some number of times,
staying transverse to ﬁbers, and ends at Hθ′ . Since there are more positive than negative
vertices in a type 1d region, it follows that x+ makes at least one more circuit about
the braid axis than x−. In particular, x+ makes at least one full circuit about A and so
contributes at least 1 to b(X+).
Proof of (2) Since ρ(R1) and ρ(R2) intersect along a common clasp arc, we can cut
open their preimages in the thin annulus subset S of PA along the two components of
the clasp arc. Paste them together in the unique new way to obtain two new regions
which resemble type 1d and −1d regions in S. Observe that, while the new regions look
like they are type ±1d, their images in CA will have the property: the Xϵ boundary,
ϵ = ±, say xϵ will be a union of two arcs, xϵ,1 ∪xϵ,2, where the ﬁnal endpoint of xϵ,1
and the initial endpoint of xϵ,2 are on the same ﬁber, but are at different points of that
ﬁber. We call this a ‘surgery’. After the surgery, we may use the same argument that we
used to prove (1), to show that the angular support of x+,1 ∪x+,2 is 2π greater than the
angular support of x−,1 ∪x−,2. Therefore x+,1 ∪x+,2 contributes at least 1 to b(X+).
Proof of (3) We have the following list of possibilities:
Case (i)
R1 and R2 have different types, say R1 is type 0d,1 and R2 is type 0d,2.
(ia) As we traverse X+ on R3 we encounter an a+–arc that is adjacent to a clasp
arc that R3 shares with R1 before we encounter an a+–arc that is adjacent to a
clasp arc that R3 shares with R2.
We surger our three regions R1, R2 and R3, in PA, along the pre-images of the
clasp arcs in ρ(R1) ∩ρ(R3) and ρ(R2) ∩ρ(R3). Since the angular support for
Rs is either contained within the angular support of X+ ∩R3, or is outside the
angular support of X+ ∩R3, the angular length of X+ ∩(R1 ∪Rs ∪R2) must
be greater than 2π. (Conceptually, R3 creates an ‘adequate amount of spacing’
between R1 and R2 so that the triple (R1, R2, Rs) contributes +1 to b(X+).)
(ib) As we traverse X+ on R3 we encounter an a+–arc that is adjacent to a clasp
arc that R3 shares with R2 before we encounter an a+–arc that is adjacent to a
clasp arc that R3 shares with R1.
We need to consider the positioning of the s–band, Rs, that runs from R1 to R2.
If the angular length of Rs is greater than 2π then we are done. So assume that
the angular length of Rs is less than 2π. Next, we can assume that the angular
length of X+ ∩R3 is also less than 2π.
Now, a convenient way of accounting for braid index is to line up the foliations of
R1, R2 and R3 (which are still thought of as being in PA) so that corresponding
Geometry & Topology 10 (2006)
488
Joan S Birman and William W Menasco
clasp arcs line up. (For examples the reader should jump ahead to Figures 48 and
50). Since our argument is concerned with the measurement of angular length
we need only focus on where we start and end this measurement. It is convenient
to use the endpoint of a clasp arc in R1 (or R2) as our starting point and the
endpoint a clasp arc in R2 (or, reversing the interplay, R1) as our ending point.
Thus, as a simplifying measure in drawing such a illustration we can focus in on
the portion of the foliation of R1 and R2 where these clasp arcs are placed, for
each such portion of the foliation has just two vertices, two singularities and a
single clasp arc. Consider the position of Rs in this superimposed picture. If Rs
is not next to R3 then we can again do a cut-and-paste to produce a topological
annulus that contributes +1 to the braid index of b(X+). If Rs is next to the
foliation of R3 then it is easy to see that X+ ∩(R1 ∪Rs ∪R2) contributes +1
to b(X+). In the superimposed image of R1 ∪Rs ∪R2 in R3 it can be seen that
X+ ∩(R1 ∪Rs ∪R2) bounds a type 1d region. Again, the assumption that R3
is a fan is not needed. (In the right sketch of Figure 48(ii), the short s–band that
runs from dot g to dot c′ is an example of an s–band that would be superimposed
in the foliation of the right sketch in Figure 48(ii).
Case (ii)
R1 and R2 are both type 0d,1 (or both type 0d,2). Suppose regions R1, R2
are of type 0d,1 and R3 is a region that is a fan. We now employ this procedure of
superimposing the foliations of R1 and R2 onto the foliation of R3. We again consider
the positioning of Rs. As before we assume that the angular support of Rs and X+ ∩R3
is less than 2π. When we superimpose R1 ∪Rs ∪R2 onto R3 we will see two copies
of a type 0d,1 region side-by-side. (Please refer to Figure 43 for a understanding of the
labels s and s′.) We have two sub-possibilities:
(iia)
Rs runs from the s′ label of the left region (which will be R1 in our side-by-side
image) to the s label of the right region, which is R2.
Notice that the cyclic ordering of the singularities in R3 imposes an order on the
singularities of R1 and R2 where they intersect R3. Thus, since R3 is a fan the
−δ singularity in R1 must occur after the δ singularity in R2. (Recall we are
making the simplifying assumption that R1 and R2 only have two singularities.)
So the angular support of Rs must overlap with the angular support of ∂R1
forcing X+ ∩(R1 ∪Rs) to have angular length greater than 2π. Thus, the triple
(R1, R2, Rs) contributes +1 to b(X+).
(iib)
Rs runs from the s label of the left region, which is R1, to the s′ label of the
right region, which is R2.
We cut-and-paste R1, R2, R3 to produce a type 0d,1 region having a portion of
X+ in its boundary but sheared in two places. If we adjoin Rs to this new 0d,1
region we see that the resulting X+ boundary contributes +1 to b(X+).
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
489
The proofs of (1′), (2′) and (3′) are almost identical to the proofs of (1),(2),(3), and we
leave them to the reader.
