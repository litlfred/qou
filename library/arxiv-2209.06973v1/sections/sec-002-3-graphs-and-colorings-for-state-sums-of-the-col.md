---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-002-3-graphs-and-colorings-for-state-sums-of-the-col
section_title: "Graphs and colorings for state-sums of the colored Jones polynomial"
section_number: 3
pages: 5-17
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
ored Jones polynomial
We will ﬁrst consider part arc-graphs and arc-graphs following [7], which are
deﬁned from Morse projections K. We will also introduce a third type of
graph representation (and the corresponding colorings), which we call chord
graphs, closely related to the chord diagrams in Vassiliev theory.
In the following sections we will restrict to closed braid diagrams.
A Morse projection K is a smooth regular embedding of an oriented
link in R2× [0, 1], which projects to a smooth immersion in the plane R2,
and such that the composition with the projection onto the y-axis deﬁnes a
Morse function on the components of K. Note that each regular projection
can be approximated with a Morse projection by planar isotopy. Sometimes
we will identifyK just with the embedded circles.
The image of the immersion deﬁned by K in R2 is the part arc-graph
PK and is a four-valent planar directed graph, with signs± assigned to each
vertex. We will color part arc-graphs by n-bounded ﬂows according to Def-
inition 2.3 such that at all crossings the colors are increasing (respectively
decreasing) along the overcrossing arc in the direction of the link orienta-
tion. Because of the ﬂow condition, correspondingly the colors are decreasing
(respectively increasing) along the undercrossing arc. This deﬁnes subsets
Fn
±(PK) ofFn(PK). The corresponding states are called (+)-colorings (re-
spectively (−)-colorings).
Next we enhance the notion of arc graph as deﬁned in [7] by adding
additional decoration. Again we assume that the Morse projection K of a
link is given as above.
5
Figure 1
Deﬁnition 3.1. Let GK = G+K be the bichromatic labeled fat digraph
with (fat) vertices corresponding to overcrossing-arcs of K. The edges of
the graph are decorated by colors blue and red. The directed blue edge
eb
v from a vertex v to the vertex w corresponds to the transition at the
undercrossing at which we switch from the overcrossing arc ending at vertex
v to the next overcrossing arc ending atw. The red arc er
v corresponds to the
jump up transition at the end of arc v, as in the picture to the overcrossing
arc (or circle) w′. The vertices corresponding to overcrossing arcs of GK
are decorated by the signs of the vertices of K at which the corresponding
overcrossing arc ends. Note that the vertices corresponding to overcrossing
circles are not decorated by a sign. The boundary of each fat vertex is also
decorated by an orientation. For a vertex corresponding to an arc this is
from the incoming blue edge in the direction of the outgoing red edge.
There will be additional decorations±, called rotation numbers along the
boundaries of fat vertices, which indicate when part arcs of PK run through
a right oriented maximum respectively minimum. (We explain below in more
detail how the part arcs on the boundaries of fat vertices are identiﬁed with
the edges of PK.) If a part arc runs through a sequence of right oriented
extrema the contributions from maxima and minima will cancel, so that
each part arc will carry at most one ±.
6
The order of incoming red and blue arcs at a fat vertex is according to
the corresponding order of overcrossings in K. We call this enhanced graph
the arc graph for the given projection K. In the setting of [7] no preferred
ordering between the outgoing edges is given. But, our correspondence
between states will suggest that the outgoing red edge precedes the outgoing
blue edge. There is a graph deﬁned from undercrossing arcs in the same way,
denoted G−K.
Remark. (a) There is exactly one red edgeer
v and one blue edgeeb
v out of each
vertex v of GK corresponding to an overcrossing arc. For an overcrossing
circle there are no outgoing edges and there is no incoming blue edge. De-
pending on possible overcrossings, there will be an even number of incoming
red edges. A special case of an overcrossing arc is the projection of a ﬁgure
eight. In this case there are one blue edge and one red edge incident with
this vertex, which are both outgoing and ingoing. There can be additional
incoming red edges corresponding to the ﬁgure eight component overcross-
ing other components ofK. We will usually not consider projections of this
form because we could isotope into a split projection.
(b) We divide the boundary of each fat vertex corresponding to an over-
crossing arc into an active half-circle , starting at the incoming blue edge
and ending at the outgoing red edge. The complementary half-circle is the
passive half-circle, and is colored yellow in Figure 1. The boundary of the
fat vertex corresponding to an overcrossing circle will be considered active.
Note that the part-arcs of the active part of the boundaries of fat vertices
of GK exactly correspond to the part-arcs of PK.
(c) Suppose that a Morse projectionK of a link is equipped with a preferred
part arc of the corresponding part arc graph PK as in Figure 2, i. e. the
only part of the projection outside of the box is the right maxima arc.
7
Figure 2
In this case we can open the projection naturally to include a long com-
ponent, and consider this long component projection K (the dashed half
arcs replace the semi-circle). Usually we will omit the dash in notation and
denote byK also the Morse projection of a long component projection. The
corresponding part arc-graph is deﬁned from the new projection just as in
the closed case but the special arc is now cut into the two oriented half
arcs. Note that a long component Morse projection closes uniquely to a
projection by closing long component with a right oriented maximum. The
two processes are inverse to each other. Suppose that the long component
is not an overcrossing arc and the crossing adjacent to the bottom half arc
is an undercrossing at the end of the half arc as in Figure 2. We will usually
not introduce a diﬀerent notation for long component projections. In this
case we associate to the long component projection the reduced arc-graph,
see the discussion in section 7 below.
(d) A Morse projectionK is alternating if and only if each fat vertex of GK
has exactly one incoming red edge, or no incoming red edge for a circle arc
without crossings.
(e) Note that PK is a planar graph while GK is an abstract graph. Not
8
every bichromatic enhanced graph as deﬁned above is the arc graph of a
Morse projection. This is due to the missing horizontal compatibility of
red edges in the graph. Below we deﬁne chord graphs, which will include
this information. It seems interesting to extend arc graphs to the setting of
virtual projections by adding undirected red edges corresponding to virtual
crossings.
Deﬁnition 3.2. A coloring of GK is a coloring of all blue and red edges.
Moreover, for each fat vertex corresponding to an overcrossing circle there
will be a color assigned to a part-arc of the boundary, if there are incoming
red edges, or to the whole boundary circle otherwise. The coloring will be
n-bounded at each vertex corresponding to an overcrossing arc, and it will
satisfy that the sum of all incoming red edge colors is 0. Note that if we
run through a component of K we run through the active edges of GK (we
will jump across blue edges whenever we switch from one overcrossing arc
to the next one), thereby traversing a connected component of GK. While
traversing the active boundaries of the corresponding fat vertices following
the orientations we cross red incoming edges. We require that the sum of the
colors of all incoming red edges minus the sum of the colors of all outgoing
red edges adds to zero for each component. We require additionally that
the n-ﬂow condition is met at each vertex corresponding to an arc. See
the deﬁnition of potential below to understand these conditions. The set
of all those colorings of GK is denoted Fn(GK). This is a subset of the
set of functions f : E→ n, except if G contains vertices corresponding to
overcrossing circles. In this case f is deﬁned on the union of the set of all
red and blue edges and a part arc in the boundary of the fat vertex or the
whole boundary of the fat vertex as discussed above.
LetPK the part arc-graph of a Morse projection K of a link K with
µ components. Let V be the set of vertices corresponding to crossings of
distinct components of PK, and V =⊔1≤j≤k≤𝓁Vjk with Vjk corresponding
to the set of crossings of the j-th and k-th component, Vjk = Vkj. In the
following we will assume that the components of K are ordered and a part
arc is chosen on each component, which is not an overcrossing circle. We
call this a basing. The chosen part arc will usually be the ﬁrst part arc on
an overcrossing arc but exceptions are possible. Note that when considering
braid projections there is a natural way to choose the basing. For long
component projections the long component will always be chosen as the ﬁrst
component and the part arc can be chosen by one of the two long half-arcs.
We call a projection with ordering and basing of components based.
9
Deﬁnition 3.3. A potential on a based projection K is a pair of functions
(r,β ) with r : V → N0 and β :{2,...,µ }→ N0. Here V is the vertex set
of the part arc-graph. We call βi the base values of the potential, and the
function r deﬁnes the jump values . For µ > 1 the following relations are
required for 1≤i≤µ:
∑
i⁄=j,c∈Vi,j
λi(c)r(c) = 0
We call these relations cycle relations . Here λi(c) = ±1 depending on
whether while walking along the i-th component the crossing c is an over-
crossing respectively an undercrossing. We will sometimes work with Z-
potentials deﬁned as above but with β,r possibly taking values in Z.
Remark. (a) It is important to note that the cycle relations are not indepen-
dent, e. g. the relation for i = 1 is the negative of the sum of the relations
for 2 ≤ j≤ µ− 1. This follows because each r(c) appears in exactly two
relations but with diﬀerent signs. So if we sum relations for 1 ≤i≤µ then
the result is 0.
(b) For a long component projection we will assume that the ﬁrst component
is long component. Moreover, the part arc on the ﬁrst component chosen
(c) A braid induces framing, orientation, ordering and basing (choice of
base-point) of the components of the link. The base-point on a component
is determined by the part-arc at the bottom of the link on the ﬁrst arc on
the component from the left.
Each potential determines an edge-coloring of PK in Z as follows: Use
the function β to deﬁne the coloring of part-arcs at basings for all compo-
nents except the ﬁrst one. For the left-bottom part-arc on the ﬁrst com-
ponent deﬁne the color to be 0. Then, along each component, at crossing
c change the edge-coloring according to the diagram below. This means
adding the valuer(c) along an overcrossing and subtracting along an under-
crossing (ﬂow condition). We think of the potential as giving the derivative
and base values for the coloring of PK. A contributing potential is a po-
tential for which all resulting edge-colorings take values in N0. We use this
language to indicate that this means that the state will be contributing to
the state-sum of the n-colored Jones polynomial for a large value of n. The
potential isn-contributing (usually we just say only contributing ifn is clear
from the context) if all resulting edge colors are in n. This implies that r,β
have to take values in n. It follows from the formulas for state-sum contri-
butions discussed in sections 5 and 6 that n-contributing states are exactly
10
those which will be contributing to the state-sum of the n-th colored Jones
polynomial. Of course, restricting the values of r,β to n does not neces-
sarily deﬁne n-bounded ﬂows. But any negative edge coloring will result in
non-contributing states. This will follow from the deﬁnitions of quantum
binomials and Pochhammer symbols in section 5. See Deﬁnition 2.3 above.
We will discuss the inequalities deﬁning contributing states in section 7.
The cycle conditions guarantee that returning to the basepoints along
each component means returning to the starting color β(j) =: βj,β 0 := 0
along each component. Note that starting from the base-points each self-
crossing is traversed twice and the color changes cancel.
Deﬁnition 3.4. Each Morse projection K, which is equipped with an or-
dering of the components and a choice of base point on each component,
deﬁnes a chord graph as follows: The chord graph CK ofK is given by µ
ordered, based and oriented circles. Each crossing is represented by an ori-
ented chord. If the orientation of the circle followed by the orientation of an
incoming chord at a point on a circle is the positive orientation of the plane
then proceeding along the circle in the direction of its orientation at this
point is an overcrossing of the correspond arc on the circle, correspondingly
at outgoing chords the arcs along circles correspond to undercrossing arcs
ofK. The sign of the crossing is added as ± decorating the chords by pairs
(r,ε ). Sometimes we do not need this additional decoration. If we want to
emphasize the crossing signs we also talk about signed chord graphs.
A coloring of a chord graph is given by adding the data from a potential
to the chords, and basepoints on the circles ordered 2 ,...,µ .
The chords subdivide the circles into arcs corresponding to the edges of
K. A potential on K induces a coloring of the chord graph. We will usually
work with Z-chord graph colorings, so allow functions r,β to take values in
Z. Note that changing the orientation of a chord and the sign of the color
of the chord will not change the corresponding part-arc coloring on K. By
deﬁnition, a chord graph is the graph of an abstract collection of µ circles
and chords, which is not necessarily induced from the chord graph on a part
arc-graphK. But we assume that all chord graph colorings satisfy the cycle
conditions. Note that for each chord graph induced from a projection K the
number of chords between diﬀerent circles is even, while we do not require
this for abstract chord graphs.
IfK is deﬁned from a closed braid projection then we will furthermore
assume that chords respect the horizontal positions induced from a braid in
the following way: For this imagine that we label the strings of the braid
1, 2,..., s. Then we can assign numbers between 1 and s to each part-arc
11
represented by a segment between chords on a circle of the chord graph.
Here we assume that the part-arcs run vertically upwards along the braid
except at a crossing represented by a braid generator σi corresponding to
the permutation ( i,i + 1) and the incoming left bottom part-arc will get
an additional horizontal position label i. Note that crossing an incoming
chord (means that the orientation of the chord is positive) with positive
sign means that the horizontal position increases. The same will be true
for an outgoing chord carrying a negative sign. The point here is that in
order to be induced from a braid the horizontal positions have to match as
in the following picture. Note that the two vertical arcs represent arcs on
component circles but can also be arcs on the same circle. This is just the
representation of the braid generator σε
k. Compare with the discussion of
special Morse projections as discussed following Theorem 6.2.
Figure 3
Note that switching sign and orientation of the chord and replacing r by
−r simultaneously, we get both the same jumps in colors and horizontal
positions on the two circle segments. Using negative chord colors r will be
essential for some of our arguments.
Example. Below is the braid (long) projection of σ1σ−1
2 σ1, which is a 2-
component link. The cycle relation is r2 = r3. For contributing states we
further have to restrict to r1 ≤ r3 ≤ β2. The chord graph gives a very
transparent way of recording the coloring of all part-arcs. Note that we use
the overcrossing arc ordering of the vertices and corresponding values for
r(i) =ri. In this case we placed the base color on the part arc following the
ﬁrst undercrossing from the bottom on the second component. Where the
base values are placed is not important for part arc graph or chord graph.
But since we color blue edges of the arc graph we usually place base values
on the speciﬁc part arcs leaving the crossing on the undercrossing.
12
Figure 4
Figure 5 below shows the corresponding arc graph as deﬁned in section 2.
Note that ∗ are labeling the part-arcs, which run downwards in the braid
closure. Note that the the f(eb
3) =β2−r3 is not a base value.
Figure 5
13
From the colored arc-graph the corresponding Garoufalidis-Loebl state-sum
contribution will be determined without reference to the part arc-graph, see
section 6.
Remark. For each Morse projectionK,PK determinesCK, from which GK
can be deduced as follows. Just cut the fat vertices from disks bounding the
circles of the chord graph by introducing cut arcs (see Figure 6) following
each outgoing chord. The blue edges then are easily added like in the picture.
Note that the cut arcs added correspond to the passive half arcs in the
boundaries of fat vertices. Also colorings of CK induce the colorings on
GK.
Figure 6
4 The ﬂow lemma
Lemma 4.1 (Flow lemma, this is in [7] for n = 1 and knots). LetK be the
Morse projection of a link. Then there is a natural bijection φ± from the
set of Z-ﬂows on G±K to the set of Z-ﬂows of PK. For (+) it assigns the
color of a blue edge of GK to the color of the part arc of PK following the
transition, and assigns the red edge colors to the changes in the colors of the
two incoming part arcs at the crossing corresponding to the transition. This
map restricts for each n≥ 1 and± to bijections of ﬂows:
φ± :Fn(G±K)→F n
±(PK)
14
Proof. We will only consider the (+)-case and letµ be the number of compo-
nents of the link in the morse projection. A given general potential as above
deﬁnes a (+)-coloring onPK in Z as explained following Deﬁnition 3.3. But
it also deﬁnes a corresponding coloring f of the arc graph GK. In fact, de-
ﬁnef(er
v) =r(v) for all vertices v, with vertices identiﬁed with overcrossing
arcs. Deﬁne f(eb
v) = βj for the vertex v corresponding to the overcrossing
arc containing the speciﬁc part arc chosen for the basing of the projection
in Deﬁnition 3.3 for all v of GK corresponding to overcrossing arcs. There
can be vertices of GK corresponding to overcrossing circles. Assign the cor-
responding base value βi if this vertex represents the i-th component. Note
that the part arcs of PK uniquely correspond to part arcs in the boundaries
of the fat vertices. So (+)-coloring of GK deﬁned following Deﬁnition 3.3
also deﬁnes a coloring of all part-arcs, which are following a vertex v at
which an overcrossing arc v ends. So this deﬁnes f(eb
v) for all vertices v of
GK. Note that conversely the coloring of GK extends to all part arcs in
the boundaries of fat vertices by using red arcs adjacent to the vertex. In
fact, using the orientation of the boundary of each fat vertex, add the value
f(er
w) for each edge er
w ending at vertex v. Figure 7 below shows how the
colors are mapped locally. The left hand side shows the overcrossing arc u
and the colorings of PK deﬁning the corresponding colorings of the edges at
the vertex u of GK. If we are given i,j,k,𝓁 then the colorings of GK are as
given in the Figure. Conversely if we have given the edge colorings of the
blue and red edges at the vertex u ofGK with the f(er
u) =r then the color
i is determined by considering the segment of the overcrossing arc w from
its beginning until the crossing w. The coloring at the beginning is given by
f(eb
w′) where w′ is the overcrossing arc preceding w. Then i is deﬁned by
adding the jumps at all overcrossings before reaching the vertex w. Then
𝓁 =i +r andj,k are deﬁned as j0 +r1 +... +rρ andk =j−r. Since r≤j
it follows k≥ 0. It also follows immediately that the ﬂow conditions corre-
spond to each other, and moreover a ﬂow in Fn
+(PK) deﬁned in this way,
corresponds to a ﬂow inFn(GK). For contributing states we assume that all
colorings are nonnegative. We havei,j,k,𝓁 ≤n for the coloring of the edges
at vertex u of PK (corresponding to the overcrossing arc vertex of GK)).
Because we have a (+)-coloring of PK it follows i +j =k +𝓁 and 𝓁≥i. It
follows𝓁−i≥ 0. The numbers r1,...,r ρ≥ 0 are the jumps along the over-
crossing arcu. It follows that j =j0+r1+... +rρ =𝓁−i+k. This is the ﬂow
condition also at the vertexu ofGK. Moreover j≤n⇐⇒(𝓁−i)+k≤n. If
we begin with an n-ﬂow onGK we havej≤n, which impliesk =j−r≤n.
Also 𝓁 = i0 +r′
1 +... +r′
ρ′ +r≤ n because this is a sum of colorings of
incoming edges at the vertex w, and i = 𝓁−r ≤ n. So the n-bounded
15
(+)-ﬂows on PK exactly correspond to the n-ﬂows on GK.
Figure 7
Remark. (a) The boundedness restrictions determine the contributing states
in each model.
(b) It was pointed out in the proof of [7] in the knot case that colorings of
the arc graph are determined by the colors of the red edges through the ﬂow
condition. Similarly Garoufalidis and Le point out that in the knot case the
jumps at the crossings determine the part arc colorings of a long knot. It is
in fact only this basic observation, which we generalize in the above lemma.
(e) Our formula generalization for [7] diﬀers from the formula by the re-
placement of t with t−1, corresponding to the various conventions for the
skein relation of the Jones polynomial.
(f) The ﬂow condition is not special to the colored Jones polynomial. The
R-matrix for the standard representation of sl(N) given in [24], 4.2.1 gives
non-trivial contributions onlyi =j≤k =𝓁, withi,j denoting the incoming
16
colors and k,𝓁 the outgoing colors at a crossing. Note that this condition
transfers to
f(eb
v) =
∑
e<erv
f(e)
for the vertex colorings of GK, additionally to the ﬂow condition.
