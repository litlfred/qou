---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-013-11-completion-of-proof-of-theorem
section_title: "Completion of proof of Theorem ??"
section_number: 11
pages: 41-47
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
In this section we show that we can always resolve the singularities of |K|
to replace it by a triangulated 3–manifold and then discuss surgery on this
3–manifold to complete the proof of Theorem 4.6.
The underlying space of K is a 3–manifold except at 0–simplices, where it
may look locally like the cone on a closed surface of genus ≥1. Suppose this
occurs at some 0–simplex v. Choose a non-separating simple closed simplicial
curve C in the link Lv. This curve is determined by an open disk D in the
star of v. We slice |K| open along D and splice in a complex as in Figure 6,
gluing the top and the bottom of that complex to the two copies of D resulting
from slicing |K|. This introduces a new 0–simplex v′ in K. We give v′ a
G–label distinct from that of each adjacent 0–simplex. We order 0–simplices
by inserting v′ anywhere (eg, as a new maximal element). We must check that
we can put ﬂattenings on the inserted 3–simplices so that the conditions for a
strong ﬂattening of our complex still hold.
Figure 6: Double cone on a disc
We ﬁrst show that it suﬃces to satisfy the log-parameter ﬂattening conditions.
Indeed, by Corollary 5.4, if we satisfy the logarithmic ﬂattening conditions, the
parity conditions hold around edges. Parity along normal paths then gives a
homomorphism from H1(|K −K(0)|) to Z/2. If we denote the new complex
by K′ and the curve in K′ given by the two vertical 1–simplices by C, then
H1(|K −K(0)|) = H1(|K′ −K(0)| −C) which surjects to H1(|K′ −(K′)(0)|) by
the inclusion, so the parity condition will hold for all normal paths.
We satisfy the log-parameter strong ﬂattening condition as follows. The added
3–simplices come in pairs with identical G–labelings, adjacent to each other
Geometry & Topology, Volume 8 (2004)
454
Walter D Neumann
above and below the central disk in the picture. We will give the two simplices
of a pair identical ﬂattenings so they cancel in the sum P
i ǫi[xi, pi, qi] ∈bB(C)
(they appear with opposite signs in this sum). Flatten all the added simplices
in the top layer in order to satisfy the ﬂattening conditions at the top edges
in the picture (there are n degrees of freedom in doing this, where n is the
number of 1–simplices around the curve C).
We then need only verify the
ﬂattening condition around the central vertical 1–simplex. Since the sum of
the three log-parameters of a ﬂattened simplex is zero, the appropriately signed
sum of log parameters around the central edge is the negative of the signed
sum of the 2n log-parameters of these simplices at the top edges in the picture.
This, in turn, is equal to the log-parameter along a normal path in the star of
v determined by a path in the link Lv that runs parallel to C on one side. It
is thus zero by the strong ﬂattening condition for such normal paths.
(An alternate argument is to look at the developing image centered at v as in
section 5. The ﬂattenings before we change K give us rotation levels on the
edges of the image in C. After changing K we have a new point in C at the
image of v′ and n segments incident on it, corresponding to the 2–simplices of
the central horizontal disk in the picture. Assign any rotation levels to these
n segments. As in section 5, this determines ﬂattenings of the 3–simplices so
that the ﬂattening conditions are satisﬁed.)
We call the above procedure “blowing up” at the 0–simplex v. Note that it
reduces the genus of the link of v. By repeated blowing up we can thus make
|K| into a 3–manifold. The following lemma improves on this.
Lemma 11.1 If K is just ﬂattened (rather than strongly ﬂattened) then we
can blow up to make |K| into a 3–manifold without changing the represented
element in bBC. In particular, Theorem 4.6 holds for ﬂattenings if it holds for
strong ﬂattenings.
Proof To apply the above argument to to blow up and simplify the link of
a vertex we need a separating curve C in the link so that the log-parameter
along a parallel normal curve in the link Lv is zero. Suppose the log-parameter
ﬂattening conditions are satisﬁed around edges, but not necessarily along nor-
mal curves. Log-parameters along normal curves then give a homomorphism
H1(Lv; Z) →Zπi ⊂C. It is well known that for any closed oriented surface S
and non-trivial homomorphism H1(S; Z) →Z there exist elements in the kernel
represented by non-separating simple closed curves (in fact, the mapping class
group acts transitively on the set of surjective homomorphisms H1(S; Z) →Z).
Thus, there exists a curve to use for blowing up, so the lemma follows.
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
455
At this point we may assume our element in H3(G; Z) is represented by a tri-
angulated 3–manifold with ﬂat G–bundle over it, or equivalently, a 3–manifold
|K| with a homotopy class of mappings |K| →BG.
Since H3(BG; Z) =
Ω3(BG) (oriented bordism), and bordism is generated by homotopy (ie, maps
of |K| × I ) and handle addition, it suﬃces to show that when we modify K by
surgery resulting from a handle-addition to |K| × I the represented element in
bB(C) is not changed.
It suﬃces to consider adding 1–handles and 2–handles, since any bordism of
connected 3–manifolds is the composition of bordisms that add 1, 2, and 3
handles in that order, and the latter are inverses of bordisms that add 1–
handles.
We ﬁrst consider adding a 1–handle. Combinatorially, homotoping |K| in BG
means changing the G–valued 1–cocycle by the coboundary action. We make
such a change so that the handle addition can be realized by gluing a 4–simplex
∆4 to K by gluing two of the 3–faces of ∆4 to disjoint 3–simplices ∆3
1 and
∆3
2 in K. The common 2–simplex of the two 3–simplices in ∂∆4 determines
2–faces of ∆3
1 and ∆3
2 that will be glued together in this construction. Our
initial change of the G–valued 1–cocycle arranges for the cocycle to match on
these two simplices.
The resulting surgery of K is the result of ﬁrst removing the interiors of ∆3
1
and ∆3
2, then gluing the resulting boundary components along the 2–simplices
mentioned above to give a manifold with a single 2–sphere boundary triangu-
lated as the suspension of a triangle, and ﬁnally gluing in a 3–ball triangulated
as three 3–simplices meeting along a common 1–simplex. Call the resulting
triangulated manifold K′.
We must make the construction compatible with orderings and provide suitable
ﬂattenings. By Lemma 10.6 we may order the vertices of K as v1, v2, . . . so
that the vertices of ∆3
1 are v1, v3, v5, v7 and of ∆3
2 are v2, v4, v6, v8 and the
2–simplices that are identiﬁed are given by the ﬁrst three vertices of each in the
given order. Then the vertices of K′ are v1 = v2, v3 = v4, v5 = v6, v7, v8, . . . and
the common 3–simplices of K and K′ have not changed their vertex orderings.
Each of the two 3–simplices ∆3
1 and ∆3
2 had a ﬂattening before the surgery, and
we use lemma 3.5 to deﬁne the ﬂattening on the three new 3–simplices. The
log-parameter part of the ﬂattening condition is then satisﬁed in K′, but the
parity condition may not be. The surgery has added a generator to H1(K, Z)
represented by any normal path that passes once through the 2–simplex that
we glued. We must check the parity condition along one such path. If it fails,
then before performing the surgery we change ﬂattenings of K by the cycle
Geometry & Topology, Volume 8 (2004)
456
Walter D Neumann
relation of Lemma 6.1 about the 1–simplex v1v3. After doing so the parity
part of the ﬂattening condition will be satisﬁed for K′.
Finally, we must consider adding a 2–handle along a simplicial curve in K. We
can realize this by doing the reverse of a blow-up (a “blow-down”) to collapse
the curve to a single vertex v with link a torus, and then blowing up again
using a longitude of the curve we collapsed. We need to show, therefore, that if
K contains a curve that maps to the trivial element in G under the homomor-
phism determined by the G–valued 1–cocycle, then we can (after adjusting the
triangulation) ﬁnd a ﬂattening that lets us perform a blow-down to collapse the
curve, followed by a blow-up using a longitude of the curve.
By retriangulating we may assume the curve C in question is length 2 and
the 3–simplices that have a 1–simplex in common with it are conﬁgured as in
Figure 6 (with, for concreteness, 6 simplices around each edge of C, as in the
ﬁgure). In particular, the bottom and top vertices in the ﬁgure are the same
0–simplex v in K, and, since the 1–cocyle along the curve gives the trivial
element of G, if we G–label the simplices of the ﬁgure all with the same label
for v′ then each pair of vertically adjacent 3–simplices has the same labeling.
The rest of the star of v will be the cone on an annulus. In particular, the
1–simplices radiating from v on the top surface of the ﬁgure are distinct from
the 1–simplices radiating from v on the bottom surface.
We must verify that we can modify the ﬂattenings so that vertically adjacent
3–simplices have the same ﬂattening, in which case we can perform the desired
blow-down.
Denote the 1–simplices radiating from v in the bottom surface of the ﬁgure
e1, . . . , e6 in order, and the 1–simplices above these in the central disk e′
1, . . . , e′
6
(with e′
i above ei). Denote by ∆i the 3–simplex in the bottom layer with edges
ei and ei+1 (indices mod 6). By applying suitable multiples of the cycle relation
of Lemma 6.1 around 1–simplices e1 and e2 we can adjust the ﬂattening of ∆1
arbitrarily, so we can make it match the 3–simplex above it. The ﬂattening
condition at 1–simplex e′
2 now implies that the log-parameter of ∆2 at edge
e′
2 matches the simplex above it, and by applying the cycle relation around
e3 we can ﬁx up the ﬂattening of ∆2 at edge e′
3. Continuing this way, we ﬁx
∆3, . . . , ∆5, at which point the ﬂattening conditions about e′
5 and e′
6 imply
that ∆6 also has its desired ﬂattening.
We can now do the blow-down by removing the interior of the complex shown
in the ﬁgure from K and then gluing the top and bottom surfaces. The result is
a complex K′ in which the link of 0–simplex v is a torus, and if we can blow up
using a complementary curve in this torus then our handle addition is complete.
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
457
However, to blow up we need the log-parameter along the appropriate normal
curve to be zero, which need not be the case. We describe how to remedy this.
Suppose we are in the situation just before we do the blow-down, so the ﬂat-
tening have been matched on pairs of 3–simplices in the ﬁgure. If we apply
the cycle relation about the lower vertical 1–simplex joining v to v′ we destroy
this matching. The procedure described above to make ﬂattenings match again
then applies the cycle relation once about each of the 1–simplices e1, . . . , e6.
We claim that the end result is to change the log-parameter along the normal
curve we are interested in by 2πi.
Indeed, recall that the full star neighborhood of the curve C consists of the com-
plex of Figure 6 glued to the cone on an annulus. In Figure 7 we show a possible
triangulation of the annulus (we may assume it is triangulated this way, since
we may choose the triangulation). The ﬁgure also shows how log-parameters
are changed by the above procedure. The normal curve that interests us is the
vertical curve, and the log-parameter along it has been changed by 2πi.
+
+
+
+
+
+
+
+
+
+
−
−
−
−
−
−
−
−
−
−
0
0
0
0
+
0
+
0
Figure 7: Left and right sides are identiﬁed to form an annulus. Signs indicate change
of ﬂattening by ±πi and 0 signiﬁes that ﬂattening has been changed by both πi and
−πi so total change is zero. The log-parameters aﬀected by applying the cycle relation
about a single ei are bold.
Since the log-parameter along the normal curve is a multiple of 2πi (Corollary
5.4), we can apply a multiple of the above procedure to make sure that desired
log-parameter along the curve is zero before we perform the blow-down.
This would complete the proof of Theorem 4.6 except that we have carried out
the proof only for ordered 3–cycles whose vertex-orderings come from a global
ordering of the 0–simplices of K. We now show that this stronger condition
is unnecessary. We will also show, as promised earlier, that K need only be
a quasi-simplicial complex (closed simplices do not necessarily embed in |K|).
An example of such a quasi-simplicial ordered 3–cycle is given by gluing the
two 3–simplices in Figure 8 by matching each face of the left 3–simplex with
the correspondingly decorated face of the right 3–simplex (the decorations in
question are the single and double arrows on the edges that bound the face).
The arrows on the edges order the vertices of each 3–simplex as shown, and, by
construction, these orderings match on common faces. The resulting complex
Geometry & Topology, Volume 8 (2004)
458
Walter D Neumann
1
3
2
4
1
2
3
4
Figure 8: A quasi-simplicial ordered 3–cycle
has one 0–simplex, two 1–simplices, four 2–simplices, and two 3–simplices.
(This 3–cycle is simply connected, so it cannot give a non-trivial element of
H3(G; Z) in Theorem 4.6, but we will return to it when discussing invariants
of 3–manifolds, since |K| −K(0) is Thurston’s ideal triangulation of the ﬁgure
eight knot complement.)
Proposition 11.2 Any quasi-simplicial ordered 3–cycle K is related by Pach-
ner moves that respect vertex-orderings of 3–simplices to a simplicial 3–cycle
K′ whose vertex-orderings are induced by a global ordering of the 0–simplices
of K′.
Proof We will start with an arbitrary ordering of the 0–simplices of K. At
ﬁrst this ordering will not induce the given vertex-orderings of simplices. We
will perform various Pachner moves on K. Each time we perform a 1 →4 move
we will add the new 0–simplex as a new maximal element both in our ordering
of 0–simplices and also in the vertex-orderings of the new 3–simplices created
by the move. At each stage in the process, the ordering of the two vertices of
a 1–simplex will be induced by the global ordering of the 0–simplices except
maybe if both vertices are “old” 0–simplices (ie, they occurred in K). We will
therefore be done once no two old 0–simplices are joined by a 1–simplex.
We will assume no 3–simplex of K meets itself across a 2–face (do a 1 →4
Pachner move on any such simplex if it occurs). Suppose K has n 3–simplices.
We ﬁrst do 1 →4 Pachner moves on each of the 3–simplices of K, creating
n new 0–simplices. Next, for each old 2–simplex (ie, a 2–simplex that was
already in K) we do a 2 →3 Pachner move on the two 3–simplices that meet
across it. Each 3–simplex of the resulting complex is in the star of a unique
“old” 1–simplex. So if we operate in the star of an old 1–simplex it will not
aﬀect the star of any other old simplex.
If there are three or more three 3–simplices in the star of an old 1–simplex,
we reduce the number to three by repeatedly doing 2 →3 moves on pairs of
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
459
adjacent simplices in its star, and then ﬁnally do a 3 →2 move on the three
3–simplices in its star to remove the old 1–simplex. If an old 1–simplex has
just two 3–simplices in its star we do a 1 →4 move on one of them and then
do a 3 →2 move to remove the old 1–simplex.
In this way we alter the complex by Pachner moves until all the old 1–simplices
have been removed. Then no two old 0–simplices are still joined by a 1–simplex,
so the proof is complete. Since Pachner moves do not aﬀect the represented
element in bB(C), this also completes the proof of Theorem 4.6.
The parity condition in the deﬁnition of ﬂattening is probably essential to The-
orem 4.6, but it’s failure can at most change the resulting element of bB(C) by
2–torsion:
Lemma 11.3 If we represent an element α ∈H3(G; Z) as in Theorem 4.6
but without requiring the condition on parity then the resulting element diﬀers
from λ(α) at worst by the element of order 2 in bB(C).
Proof Suppose the log-parameter condition is satisﬁed but the parity condi-
tion is not satisﬁed for the ﬂattening of K and let µ be the resulting element
in bB(C). Parity along paths determines an element of H1(|K|−K(0); Z/2) and
hence a 2–fold cover of K (possibly branched at some 0–simplices). The lift of
the ﬂattening to this cover will satisfy the parity condition and hence represent
λ(2α) = 2λ(α). But it clearly also represents 2µ, so 2(µ −λ(α)) = 0.
12
