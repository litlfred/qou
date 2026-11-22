---
doc_id: 0310280v4
doc_title: "Stabilization in the braid groups II: Transversal simplicity of knots"
section_id: sec-004-23-braid-foliations-on-transversal-clasp-annuli
section_title: "Braid foliations on transversal clasp annuli"
section_number: 2.3
pages: 13-20
source_pdf: 0310280v4.pdf
source_sha256: 1e146ee4ebc157f2
toc_source: outline
doc_brief: "Stabilization in the braid groups II: Transversal simplicity of knots — 10 sections: Front matter; Introduction and description of re; The MTWS and transversal isotopies"
---
Braid foliations on transversal clasp annuli
The principle tool in the proof of the MTWS is the study of the braid foliation of CA,
the singular foliation which is determined by the intersections of CA with the disc
ﬁbers Hθ of H. Braid foliations have been reviewed in several places. We refer readers
who are unfamiliar with them to the review in Sections 3 and 4 of [6], and if necessary
thence to [3] for additional details. However, there are aspects of these foliations which
will be needed here and may not be so familiar, so we recall them next. After that, we
will prove Proposition 2, which describes the braid foliation on the transversal clasp
annulus of the preceding section.
X−
X−
X+
X+
+
+
+
+
−
−
−
−
type a−
type a+
type b
type s
Figure 6: The left sketch illustrates the types of non-singular leaves in the foliation of CA. The
right sketch illustrates a foliated neighborhood of a type bb–singularity.
As in [6] and [3]: Given a braid structure (H, A) and a clasp annulus CA, we arrange
that A transversally intersects CA in ﬁnite many points. The points of CA ∩A are
the vertices of the braid foliation. Since CA has an orientation that is consistent with
the orientation of X+, and since A also has an orientation, each vertex of the braid
foliation will have an associated parity. We can also assume that all but ﬁnitely many
disc ﬁbers of Hθ ∈H will intersect CA transversally. Of the ﬁnitely many disc ﬁbers
that do not intersect CA transversally, each contains a single point of non-transversality
that corresponds to a saddle point. Since CA is oriented, and since the orientations on
A and the ﬁbers of H are consistent, there is also a natural parity assignment to each
singularity in the braid foliation of CA. (See the left sketch in Figure 6, and see [6] and
in particular [3] for all details).
Geometry & Topology 10 (2006)
1438
Joan S Birman and William W Menasco
After an isotopy of CA with respect to the braid structure (H, A) we may assume that
the non-singular leaves of the braid foliation on CA are either s–arcs, a–arcs or b–arcs.
The a–arcs subdivide into two groups: a+–arcs which have one endpoint on a positive
vertex and one endpoint on X+; and a−–arcs which have one endpoint on a negative
vertex and one endpoint on X−. In the foliation the set of possible types of singularities
can be listed in correspondence to the types of leaves that are in a regular neighborhood
of the singularities. Such a regular neighborhood is called a tile. For example, the right
sketch in Figure 6 illustrates a foliated bb–tile.
In Figure 7 we show the listing of possible singularity and tile types.
a+a+
a+b
a+s
a−a+
a−a−
a−b
a−s
sb
bb
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
Figure 7: Possible tile types in the foliation of CA. The black (resp. gray) arcs represent subarcs
of X+ (resp. X−).
The foliation determines a cellular decomposition of PA which goes over to a cellular
decomposition of S2 on shrinking the 2 boundary components to points. Letting V, E
and F be the number of vertices, edges and faces, the fact that χ(S2) = 2 shows that on
each component of the foliated surface PA we have V + 2 −E + F = 2. Each tile has
four edges and each edge is an edge of exactly 2 tiles, so that E = 2F. Combining this
with the previous equation we learn that V = F. Let vϵ (resp. sϵ) be the number of
vertices (resp. singularities) of sign ϵ in PA. Since there is exactly one singularity of
either sign in each tile, it follows that
(3)
(v+ + v−) = (s+ + s−).
We return to the situation where X+ and X−are transversal knots TX+, TX−, also TA
is a transversal clasp annulus, so that the isotopy across TA is a transversal isotopy.
Geometry & Topology 10 (2006)
Stabilization in the braid groups II
1439
We claim that the signed vertices and singularities also detect the difference between the
Bennequin invariants β(TX+) and β(TX−). For, recall that the isotopy was constructed
from the transversal Markov tower of (2). The moves that relate adjacent braids in that
tower are braid isotopy and positive stabilizations and destabilizations. While braid
isotopy may change the braid foliation, it does not change the numbers v+, v−, s+, s−,
so the only issue is what happens during stabilizations and destabilizations. Let’s
consider a positive destabilization. We have a single trivial loop around the z axis,
with a positive crossing. We have dθ > 0 along the entire length of the loop since we
are working with a closed braid. For a positive crossing we have dz ≥0 throughout
the loop as well. Therefore the inequality dz/dθ > −ρ2 is true for all non-zero real
values of ρ. Crossing the z–axis to destabilize the braid results in at least one singular
point, where dθ = 0, but if we continue to keep dz ≥0 then in the limit, as −ρ2 →0
from the negative real numbers, dz/dθ goes to ∞through the positives. Therefore
dz/dθ̸ = −ρ2 at any stage in the isotopy. Therefore the isotopy is transversal. After
the isotopy the number of positive vertices will have decreased by 1 and the number
of positive singularities also will have decreased by 1 so that the difference between
them is zero. Now recall that the Bennequin invariant β(TX) of a transversal knot is
the difference between its braid index and its algebraic crossing number. Thus the
Bennequin invariant is preserved during a positive destabilization. The situation is the
same for a positive stabilization. In particular, if we study the sequence of moves that
take us from TX+ to TX−in (2) we see that:
(4)
β(X+) −β(X−) = (s+ −s−) −(v+ −v−) = 0.
Using Equations (3) and (4), it follows that if TA is swept out during a transversal
isotopy, then:
(5)
v+ = s+ and v−= s−.
We now wish to apply our knowledge about transversal isotopies to a speciﬁc situation.
Let X ∈X be a braid in braid structure (H, A) such that X ∈Bmin(X). Let T∆⊂R3
be an embedded disc, with boundary ∂(T∆) the union of two intervals a1 ∪a2, where:
(1)
a1 ⊂X.
(2)
(X \ a1) ∪a2 = X′ ∈B(X). In particular, X ∩int(T∆) = ∅and X′ is isotopic to
X by the motion of a2 to a1 across T∆.
(3) The positioning of T∆in (H, A) is such that the braid foliation of T∆is either
by parallel arcs transverse to the boundary, or is the union of tiles from Figure 7
with the exception that we allow the foliation of T∆to have two cusp points near
the points a1 ∩a2.
Geometry & Topology 10 (2006)
1440
Joan S Birman and William W Menasco
(4) Orienting T∆so as to be consistent with the orientation of a2, the tiling of T∆
is such that (v+ −v−) −(s+ −s−) = 0. Thus, the graph X ∪a2 is in braid
position and its edges have natural orientations.
We call such a disc T∆a transversal disc between X and X′.
Before we can state our next lemma, we need one more concept about braid foliations. It
is to be expected that the union of the singular leaves will contain most of the information
about the braid foliation, but in our situation there is additional information. The parity
information associated with the vertices and singularities of a braid foliation allows us
to deﬁne four graphs G+,+, G+,−, G−,+ and G−,−. Let Gϵ,δ, where ϵ and δ are ±, be
the graph that contains the
G+,+
G−,−
G+,−
G−,+
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
Figure 8: The graph Gϵ,δ includes all singular leaves through vertices of sign ϵ and singularities
of sign δ. The thick edges illustrate the passage of G+,+, G−,−, G+,−, G−,+ through a bb–tile.
vertices of sign ϵ and connects them together using edges that are contained in singular
leaves of sign δ. By deﬁnition Gϵ,δ ∩G−ϵ,−δ = ∅. See Figure 8, which illustrates how
the 4 graphs intersect a bb–tile. The reader should not have any difﬁculty in seeing how
the 4 graphs pass through the tiles in Figure 7. Observe that for all the other tiles there
will be vertex endpoints of the graphs on the boundary, because the singular leaves have
endpoints on the boundary.
Lemma 3 Let T∆be a transversal disc between the braids X and X′. Then, when X
and X′ are viewed as transversal knots in the standard contact structure, the isotopy
across T∆is a transversal isotopy. In particular, if C ⊂G+,+ (resp. G−,−) is a
component of the graph in T∆then C is a tree having a single endpoint on a1 (resp.
a2).
Proof From [7] we know that a positive stabilization or destabilization corresponds
to a transversal isotopy. From Section 3.4 of [6] we know if δ ⊂T∆is a regular
Geometry & Topology 10 (2006)
Stabilization in the braid groups II
1441
neighborhood of a single edge of G−,−which has an endpoint on a2 then the isotopy
of a2 across δ corresponds to a positive stabilization of a2. Similarly, if v ⊂G+,+ is
an endpoint of a component and, also, a valence one vertex in the foliation of T∆then
from Section 3.3 of [6] we know we can eliminate v by a positive destabilization. Thus,
if every component of G−,−is a tree having a single endpoint on a2 we can eliminate
the graph G−,−through a sequence of positive stabilizations of a2. All that will remain
is the graph G+,+. If the components of G+,+ are trees each having an endpoint on
a1 then through a sequence of positive destabilizations (starting at vertex endpoints)
we can eliminate the components of G+,+. What will remain of T∆will be trivially
foliated and an isotopy across a trivially foliated transverse tab corresponds to a braid
isotopy in the complement of A. But, such braid isotopies are transversal isotopies.
Thus, to establish the main assertion of the lemma we need to establish the assertions
that the components of our graphs G±,± are trees having endpoints on the appropriate
ai arc of T∆.
The initial fact that each component of G±,± must be a tree follows from Theorem
3.1 of [3]. We also learn from Theorem 3.1 of [3] that if C ⊂G+,+ has more than
one endpoint on a1 then after a sequence of braid isotopies (which are in the form of
change of ﬁbration) and exchange moves, we can destabilize a1. But this would imply
that X was not of minimal braid index. So any component of G+,+ can have at most
one endpoint on a1. Now notice that for those components of G+,+ having a single
endpoint on a1 the number of positive vertices equals the number of singularities. And,
for those that don’t have an endpoint on a1 the number of positive vertices is always
one more than the number of singularities. But, since v+ = s+ we have to have all
components of G+,+ having an endpoint on a1. Finally, if C ⊂G−,−is a component
that has more than one endpoint on a2 then there is a path in C that splits off a subdisc of
T∆that contains a component of C′ ⊂G+,+. But, then C′ could not have an endpoint
on a1, which contradicts what we just proved.
We need a few more deﬁnitions before we can state our main application of Lemma 3, ie,
Proposition 2 below. We say that a clasp arc γ ⊂TA is short for X+ (resp. X−) if there
exists a triangular disc ∆+ ⊂PA (resp. ∆−⊂PA) such that a1 ∪a2 ∪a3 = ∂∆+
(resp. = ∂∆−) where a1 in contained in an a+–arc (resp. a−–arc); a2 = γ+ (resp.
= γ−); a3 ⊂e−1(X+) (resp. e−1(X−)); and, ∆+ (resp. ∆−) is trivially foliated.
We say that a clasp arc γ−(resp. γ+) is parallel to a component C of G+,+ (resp.
G−,−). if there exists an edgepath E ⊂C and a rectangular disc R ⊂PA such that;
(1)
∂R = a1 ∪a2 ∪a3 ∪a4, where a1 = γ−(resp. a1 = γ+), a2 is a subarc
contained in a leaf of the foliation, a3 ⊂X−(resp. a3 ⊂X+) and a4 = E .
Geometry & Topology 10 (2006)
1442
Joan S Birman and William W Menasco
(2)
int(R) does not contain any vertices or singularities of the foliation.
(A foliated neighborhood of the edgepath E which contains γ−(or γ+) and only the
vertices and singularities in E will play the part that tab neighborhoods of clasp arcs
played in [6].)
Proposition 2 Let T X be a transversal oriented knot type and (TX+, TX−) be a
pair of transversal closed braids which represent T X . Assume that the braid index
b(TX+) = b(TX−) = m, where m is minimal for all closed braid representatives of
the topological knot type X . Then the transversal clasp annulus TA associated with
(TX+, TX−) supports a braid foliation, which satisﬁes the following conditions:
(a) The leaves of the the braid foliation are type s–, a+–, a−– or b–arcs and the
singularities correspond to those listed in Figure 7.
(b) The components of G+,+ (resp. G−,−) are trees, having a single endpoint on
TX−(resp. TX+).
(c) For each clasp arc γi ⊂TA at least one of its associated pre-images γi
+ or
γi
−⊂PA is either short or is parallel to an edgepath in the pre-image of G+,+
or G−,−.
Proof Our proof will use Lemma 3. Let TA be a transversal clasp annulus associated
with the pair (TX+, TX−). Inside the pre-image PA we have the pre-image of the clasp
arcs {γ1
+, γ1
−, · · · , γk
+, γk
−} and their extension arcs {g1
+, g1
−, · · · , gk
+, gk
−}. Recall that
we have the graph
G = TX+ ∪TX−∪(∪1≤i≤kγi) ∪(∪1≤i≤ke(gi
+)) ∪(∪1≤i≤ke(gi
−)),
and that it is both in braid position and transverse to the standard contact structure. By
a small isotopy near the vertices of this graph we can assume that it is differentiable.
Thus, in PA each edgepath gi
± ∪γi
± will split off a subdisc of PA that has two cusps.
TX+
TX−
TXos
γm
+
gm
+
γi
+
gi
+
γi
−
gi
−
s1
s2
s3
s4
s5
Figure 9: The graph G, as it appears in the annulus PA.
Geometry & Topology 10 (2006)
Stabilization in the braid groups II
1443
We now use the fact that the edgepaths {(g1
+ ∪γ1
+), (g1
−∪γ1
−), · · · , (gk
+ ∪γk
+), (gk
−∪
γk
−)} ⊂PA are staggered. Let Λ = {s1, · · · , sl} ⊂PA be a set of leaves in the
pre-image of the characteristic foliation of TA such that:
(i) Each component of PA \ Λ is a subdisc that contains at most one gi
± ∪γi
±
edgepath. (We allow for the possibility that a component contains no such
edgepath.)
(ii) By a small isotopy, the components of Λ ⊂PA can be made transverse to the
characteristic foliation so that the graph TX+ ∪TX−∪e(Λ) is: differentiable
and transverse in the standard contact structure; and, there is a smooth loop
TXos ⊂TX+ ∪TX−∪e(Λ) that oscillates away from the clasps; ie, there
exists arcs {x1
+, · · · , xl
+} ⊂TX+ and {x1
−, · · · , xl
−} ⊂TX−such that, when
the leaves of e(Λ) are positioned transversal in TA the smooth loop TXos =
x1
+ ∪s1 ∪x1
−∪s2 ∪x2
+ ∪s3 ∪x3
−∪· · · ∪sl does not intersect any clasp arcs.
Notice that TXos ⊂TA is transversally isotopic to TX+, to TX0 and to TX−.
We now consider the expanded graph
Γ = TX+ ∪TX−∪TXos ∪(∪1≤i≤kγi) ∪(∪1≤i≤ke(gi
+)) ∪(∪1≤i≤ke(gi
−)) ⊂TA
The graph Γ is a transversal graph in the standard contact structure. Except for the
portion of it that corresponds to e(Λ), it is also a braided graph. We now make it entirely
braided by applying ﬁrst the Bennequin trick to e(Λ) then extending this transversal
isotopy of Γ to all of (R3, ξ) by Eliashberg’s Lemma (Lemma 2). The resulting TA
will still be a transversal clasp annulus with TXos now being in braid position.
We claim that the braid foliation on TA must be a tiling. If it is not then there will exist
a leaf in the braid foliation of c ⊂TA that is a circle. But, notice that, due to the fact
the Γ is in braid position, its edges can be consistently oriented. Thus, c ∩Γ = ∅due
to orientation considerations. We then have c ⊂TA \ Γ and c will therefore bound an
embedded disc ∆c ⊂TA. Since c ⊂Hθ for some Hθ ∈H we see that it also bounds
a ∆θ ⊂Hθ which, without loss of generality, we can assume is inner most in Hθ. After
smoothing the corners around c we will have a smooth 2–sphere ∆c ∪c ∆θ whose
characteristic foliation will be radial in ∆θ(⊂∆c ∪c ∆θ ∼= S2) with one elliptic point.
So the characteristic foliation on ∆c must also have an elliptic point. But, ∆c ⊂TA
and the characteristic foliation on TA is trivial. We conclude that the circle leaf c
could not have existed in the braid foliation of TA. Thus TA is tiled.
Next we establish that each clasp arc γi is associated to the preimage of either a short
clasp arc or a parallel clasp arc in PA. So let Ei
−= γi
−∪gi
−⊂PA be a clasp arc
and its extension. Notice that e(Ei
−) ⊂TA splits off an embedded disc, T∆i
−⊂TA,
Geometry & Topology 10 (2006)
1444
Joan S Birman and William W Menasco
that has an induced trivial characteristic foliation. So there is a transversal isotopy of
e(Ei
−) across T∆i
−into TX−. Our initial goal is to establish that T∆i
−is a transversal
disc. But, this is clear because when we consider the braid foliation of TA restricted to
T∆i
−we see that it has an induced tiling and that one of its boundary arcs is on a braid
of minimal index. Moreover, since T∆i
−illustrates a transversal isotopy, for the tiling
of T∆i
−we have the equation (v+ −v−) −(s+ −s−) = 0.
If the induced braid foliation on T∆i
−is trivial, then γi
−is short. So assume the
braid foliation on T∆i
−is non-trivial. Then we apply Lemma 3 and conclude that
every component of Gϵ,ϵ, ϵ = ±, is a tree, also each component of G−,−will have
one endpoint on e(Ei
−), and each component of G+,+ will have one endpoint on
TX−. We can assume that the endpoints of G−,−on e(Ei
−) are away from the point
e(γi
−∩gi
−) ⊂TX+ which cannot be moved. Now, by stabilizing positively e(Ei
−) along
the components of G−,−in T∆i
−we can force the elimination of G−,−in the resulting
transversal disc, which by abuse of notation we still call T∆i
−. We now eliminate the
endpoint vertices of any component of G+,+ in T∆+,+ via positive destabilization,
ie, we eliminate valence one vertices of G+,+ in T∆i
−. (See Sections 3.3 and 4.3 of
[6].) This can be done so long as the neighborhood of the valence one vertex does not
contain the point e(γi
−∩gi
−). After the elimination of all possible valence one vertices
we will have the resulting T∆i
−containing only a linear component of G+,+ and γi
−
will, thus, be parallel to an edgepath in G+,+.
Finally, we notice that TXos ⊂TA decomposes TA into a union of transversal discs.
The reasoning is similar to that of why T∆i
−was a transversal disc. Namely, any
disc component T∆⊂TA \ TXos is an embedded disc having a trivial characteristic
foliation coming from the characteristic foliation of TA. Thus, an isotopy of TXos
across T∆is a transversal isotopy. This implies that for the braid foliation on TA
restricted to T∆we again have the equation (v+ −v−) −(s+ −s−) = 0. Applying
Lemma 3 to T∆we see that, since one boundary arc of ∂T∆is on a braid of minimal
index, the components of Gϵ,ϵ are trees having endpoints on the appropriate subarcs of
the boundary of T∆. This implies that the components of Gϵ,ϵ ⊂TA are trees having
single endpoints on TX−ϵ. Our proof is complete.
