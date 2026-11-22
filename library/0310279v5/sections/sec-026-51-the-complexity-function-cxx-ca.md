---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-026-51-the-complexity-function-cxx-ca
section_title: "The complexity function c(X+,X-,CA)"
section_number: 5.1
pages: 59-67
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
By Proposition 4.5.1 we may assume that each clasp arc pair is contained in a normal
neighborhood pair, and can be pushed into the union of leaves. Assume from now on
that has been done. Deﬁne the complexity c(X+, X−, CA) to be the lexicographically
ordered pair (c1, c2), where c1 is the number of singular points on the clasp arcs and c2
is the number of singular points that are outside normal neighborhoods. Note that if the
clasp arcs are transverse to the ﬁbers of H, then c1 can be interpreted as the number of
singular leaves crossed by γ+ and γ−.
The reader may wonder why we do not include a count of vertices in the foliation? The
reason is simple: the vertex count is determined by the singularity count, using the
Euler characteristic of the annulus. See the argument at the beginning of the proof of
Lemma 6.3.1.
The reader may also wonder why our complexity function ignores all the singularities
that are in normal neighborhoods but not on the clasp arcs. The reason is again simple:
when we constructed normal neighborhoods we created lots of inessential b–arcs. If
we omit them, we will be forced to give up normal neighborhoods, and we don’t want
to do that now.
Finally, the reader may wonder why we are not including braid index in our complexity
function. That is a more subtle matter. At this stage in the work it sufﬁces to say that
we will introduce it later (see the augmented complexity function of Section 6.)
In the manuscript [9] the authors proved that when X is the µ–component unlink,
exchange moves and destabilization sufﬁce to reduce any closed braid representative
X+ to the identity braid in the µ–strand braid group. In this section we see how far we
can go in the simpliﬁcation of our clasp annulus CA with the help of exchange moves
Geometry & Topology 10 (2006)
472
Joan S Birman and William W Menasco
and destabilization. The moves that we use here will create the two subsequences (1)
and (2) of the MTWS. The reason that we had to separate the sequences (1) and (2)
in the statement of the MTWS from the sequence (3) is that it may happen that the
given braid X−does not have minimum complexity with respect to exchange moves,
for example it may be wound up in the manner illustrated in Figure 5. If so, then if we
simply tried to modify the given X+ to X−, it might not be possible to do it without
increasing complexity at some point.
We shall regard changes in foliation and braid isotopy to be ‘trivial moves’. On the other
hand, in general exchange moves modify the braid isotopy class and destabilizations
change the braid index too. Our goal will be to minimize the complexity, using all four
moves: braid isotopy, changes in foliation, exchange moves and destabilizations.
One expects the singular leaves to contain key information about a foliation. In the
case of braid foliations more is true, because the singular leaves divide nicely into
subsets which are characterized by the signs of their vertices and singularities. Let Gϵ,δ,
where ϵ and δ are ±, be the set of all singular leaves which pass through only vertices
of sign ϵ and singularities of sign δ. We consider the four subgraphs of the graph
of the singular leaves G+,+, G−,−, G+,−, G−,+. By deﬁnitions Gϵ,δ ∩G−ϵ,−δ = ∅.
See Figure 42, which illustrates how the 4 graphs intersect a bb–tile. Similar graphs
-
+
+
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
+
+
-
-
G++
G−−
G+−
G−+
Figure 42: The graph Gϵ,δ includes all singular leaves through vertices of sign ϵ and singularities
of sign δ. The thick edges in this example illustrate the passage of G+,+, G−,−, G+,−, G−,+
through a bb–tile.
appeared in Bennequin [2], in connection with his studies of the characteristic foliation
of surfaces bounded by knots.
The intersection of a clasp arc γϵ with a subdisc ∆of PA is good if (∆∩γϵ) ⊂(∆∩Gϵ,δ)
for some (ϵ, δ) ∈{(+, +), (+, −), (−, +), (−, −)} and if no component of ∆∩γϵ
includes the puncture endpoint of γϵ. A subdisc ∆of PA is good if every component
of intersection of ∆with a clasp arc γϵ is good. A subdisc that is disjoint from the
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
473
clasp arcs is, of course, good. A disc that contains a puncture endpoint of a clasp arc is
not good.
A vertex is said to be near Xϵ , where ϵ = ±, if it is the endpoint of a leaf of type aϵ in
the foliation of PA. A vertex v is said to be an interior vertex it is not near either X+
or X−. In both cases we deﬁne link(v) to be the closure of the union of all b–arcs and
aϵ–arcs which meet v.
To begin our work, we study ab and bb–exchange moves and changes in foliation in the
presence of clasp arcs, under the hypothesis that the moves are supported in good discs:
The (ab)⋆exchange move Let v be a vertex of valence 2 in the foliation of PA which
is near Xϵ and is the endpoint of a b–arc. Assume that ∆= link(v) is a good disc
which has non-empty intersection with a clasp arc γϵ. Consult Figure 23(a), which
illustrates the case when v is a positive vertex. The disc ∆is the closed disc bounded
by the singular leaves wqp and wst in Figure 23(a) and by the subarc pt of X+. If
ϵ = −all vertex signs are reversed and the roles of X+ and X−are interchanged, but
the underlying phenomena are unchanged. We are interested in whether we can push
X+ across ∆in the presence of the clasp arc γ?
Notice that all 4 graphs G+,+, G+,−, G−,+ and G−,−intersect ∆in Figure 23(a). By
our deﬁnition of a good disc, γ ∩∆is a subset of some Gϵ,δ, however the case ϵ = +
is impossible. The reason is: G+,± ends at v in the interior of ∆(because the two
singularities in ∆have opposite signs), also by hypothesis ∆is a good disc, so that
γ cannot have its puncture endpoint in ∆. Therefore (γϵ ∩∆) ⊂G−,+ or G−,−.
Both cases can occur, and the two cases are essentially the same. In both cases ∆is
embedded, because γϵ lies in a normal neighborhood and so its partner γ−ϵ cannot
intersect ∆. In fact normal neighborhoods tell us more: γϵ is the only clasp arc that
can intersect ∆. So γ begins at, say, p ∈X+ and passes through q to w, always in ∂∆.
Just as in the embedded case, we can push X+ across a neighborhood of ∆, removing
two vertices and two singularities from the foliation. This is the ‘light bulb’ move of
Figure 23(b). It shortens γϵ and so also shortens its partner γ−ϵ, reducing the entry
c1 in c(X+, X−, CA). The second sheet of PA is unchanged by the move, except for
the fact that its clasp arc is shortened by pulling in its puncture endpoint. The link X+
remains embedded throughout the move. The argument is identical if X+ is replaced by
X−. This is the move that we call the (ab)⋆exchange move. It is exactly the same as
the ab–exchange move, but in the presence of clasp arcs and with the assumption of
good discs.
The (bb)⋆exchange move Let v be an interior vertex of valence 2 in the foliation of
PA. Assume that ∆= link(v) is a good disc which has non-empty intersection with a
clasp arc γ. Consult Figure 25, which illustrates the case when v is a negative vertex.
Geometry & Topology 10 (2006)
474
Joan S Birman and William W Menasco
The disc ∆is the closed disc bounded by the singular leaves w1sw2 and w1qw2. All
vertex signs could be reversed, it will not matter, so we assume they are as illustrated.
We are interested in whether we can do the bb–exchange move and collapse of the
pocket, as illustrated in the passage from the left to right sketches in Figure 25, in the
presence of the clasp arc γ, when ∆is a good disc?
As in the case of the (ab)⋆move, the intersection of our clasp arc with ∆is assumed to
be a subset of the intersection of one of the 4 graphs with ∆. Since the puncture point of
γ cannot be in ∆the only possibilities are the graphs G+,+ or G+,−, because the other
two possibilities lead to a puncture point in the interior of ∆. Assume without loss of
generality that γ ⊂G+,+, for example γ might pass through the points pw1sw2p′ in the
left sketch in Figure 25. Using the hypothesis that γ is in a normal neighborhood, we
can (by Proposition 4.5.1) push γ to a new position which we call pw′
1s′w′
2p′ where it is
transverse to the leaves of the foliation. But then the bb–exchange move goes through
as before, as described in full detail in sketches 2.15–2.19 and the accompanying text of
Birman–Finkelstein [4]. Since that argument is long and technical, and since a complete
reference is available, we do not repeat it here. After the move the ‘pocket may be
collapsed’, as illustrated in the passage from the left to the middle sketch in Figure 24
of this paper, and also in the passage from the left to the right sketch in Figure 25. The
clasp arc can then be pushed back into a union of leaves, ie to the position pw2p′ in the
right sketch. The complexity c(X+, X−, CA) has been reduced because the singularity
s is no longer on γ. This is the move that we call the (bb)⋆exchange move. It is
exactly the same as the bb–exchange move, but in the presence of clasp arcs and with
the assumption of good discs.
The change of foliation of Lemma 3.2.1 in the presence of clasp arcs
As in the
case of the ab and bb–exchange moves, we will refer to the manuscript by Birman and
Finkelstein [4] for all details, since the required changes in foliation were justiﬁed very
carefully there, in the proof of Theorem 2.1 of that paper, under the hypothesis that the
surface in question was embedded. But the immersed case is really no different from
the embedded case because the changes in foliation that we need here can always be
thought of as being induced by changes in the choice of disc ﬁbers for the ﬁbration
H of 3–space minus the braid axis, and not by any change in the position of CA in
3–space. See Figure 20, which illustrates the case when we are interested in changing
the foliation on two bb–tiles which meet in a common b–arc. The sketches show the
changes when there are no clasp arcs. The fact that the clasp arcs have been positioned
in normal neighborhoods shows us that we can change the foliation in one of the sheets
without changing the other sheet. Assume that the union of our two bb–tiles is a good
disc. There are three cases:
(i) Both s1 and s2 are contained in a single normal neighborhood as consecutive
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
475
singularities, on a clasp arc. After the change of foliation, the path of the clasp
arc contains one fewer singularity, so c(X+, X−, CA) is reduced. In particular, if
ϵ = + and we have a symmetric clasp arc then the resulting change of foliation
is the one that is labeled (ii) in Figure 20. In this case the clasp arc contains the
two right-most positive vertices and the right-most singular point. If ϵ = −, then
the resulting change of foliation is the one that is labeled (i) in Figure 20, and the
clasp arc contains the two left-most negative vertices and the left-most singular
point.
(ii) One of the two singularities, say s1, is contained in a normal neighborhood of
a clasp arc, but not on the clasp arc. After the change in foliation, the path of
the clasp arc is unchanged. For example, if ϵ = + and the clasp arc contains s1
(resp. s2) then we have a change of foliation that takes us to (i) (resp. (ii)).
(iii) The two singularities are contained in disjoint normal neighborhoods of different
clasp arcs. The path of the two clasp arcs is unchanged by the change in foliation.
For example, if ϵ = + and the bottom singularity was contained in the clasp arc
for the beginning tilings in the sequences in Figure 20 then the resulting change
of foliation is (ii) in all three cases.
Armed with this knowledge, we are now able to adapt [4, Theorem 3.1] to our clasp
annulus CA and its foliated preimage PA. We will use the symbol Nϵ for a normal
neighborhood of the clasp arc γϵ and the symbol N for the union of all normal
neighborhoods of all clasp arcs.
Proposition 5.1.1 Each of the following holds for all four graphs G+,+, G−,−, G−,+
and G+,−:
(1)
Gϵ,δ ∩G−ϵ,−δ = ∅.
(2) Every singular point and every vertex in the foliation of PA is in G+,+ or G−,−
(and also in G+,−or G−,+).
(3)
Gϵ,δ has no interior isolated vertex v.
(4)
Gϵ,δ \ (Gϵ,δ ∩N) has no interior endpoint vertex v.
Assume that all clasp arcs are positioned in normal neighborhoods, and that initially
they have been pushed into unions of leaves of the foliation. Then after some number of
exchange moves (combined with changes in foliation and isotopies in the complement
of the axis) the following holds for all four graphs at once:
(5)
Gϵ,δ contains no closed loop l which bounds a good disk ∆⊂PA.
After some number of exchange moves and destabilizations, the following also holds
for all four graphs at once:
Geometry & Topology 10 (2006)
476
Joan S Birman and William W Menasco
(6) There is no closed loop l which is the union of an edgepath E1 ⊂Gϵ,+ and an
edgepath E2 ⊂Gϵ,−which bounds a good disc ∆⊂PA \ N .
(7) Let E1, E2, E3 be connected arcs, with E1 ⊂Gϵ,ϵ, E2 ⊂Gϵ,−ϵ, E3 ⊂Xϵ. Then
there is no closed loop l = E1 ⊔E2 ⊔E3 or E2 ⊔E3 or E1 ⊔E3 which bounds a
good disc ∆on PA.
Proof The proof is almost identical with the proof of [4, Theorem 3.1]. Outside normal
neighborhoods of the clasp arcs it is identical. Inside normal neighborhoods the key
concepts which makes it possible to carry over arguments used in [4] are good discs. In
the presence of clasp arcs we simply use the exchange moves (ab)⋆and (bb)⋆instead
of ab and bb and the complexity function c(X+.X−, CA). An application of (ab)⋆can
shorten the length of a clasp arc γϵ, reducing the number of singular leaves it intersects.
It will necessarily shorten the length of γ−ϵ and decrease the number of tiles of PA
that are in N−ϵ. Thus, there may be some inessential b–arcs that are now away from
normal neighborhoods, and they can be eliminated.
Also, an application of (bb)⋆can shorten the length of a clasp arc γϵ, reducing the
number of singular leaves it intersects. But, it does not immediately reduce the number
of singular leaves γ−ϵ intersects. Moreover, neither γϵ nor γ−ϵ may be in normal
neighborhoods anymore. To re-establish the symmetry between the the lengths of the
two clasp arcs in PA we take a tab neighborhood around γϵ (since a tab neighborhood
will have the shortest clasp length) and re-apply the normal neighborhood construction
of Proposition 4.5.1.
Our ﬁrst corollary produces the modiﬁed braids X′
+ and X′
−in the statement of the
MTWS. In the course of changing X± to X′
±, it also produces the sequences (1) and (2)
of the MTWS, which modify X± →X′
±:
Corollary 5.1.1 Assume that all changes are made in the complement of normal
neighborhoods of the clasp arcs. Then with the help of:
• complexity-reducing exchange moves on X+ and X−,
• complexity-reducing destabilizations of X+,
• changes in foliation (which modify CA but do not change X+ or X−),
the triplet (X+, X−, CA) may be changed to a new triplet (X′
+, X′
−, CA′) which has
minimum complexity, and for which the foliation of PA has the following properties:
(1) There are no aϵs or aϵaϵ singularities in PA for ϵ = + or −.
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
477
(2) If α is a path in Gϵ,δ which begins and ends on Xϵ, and ∆is the disc on PA
which is split off by α and a subarc of Xϵ, then int(∆) contains a puncture
end-point of a γ−ϵ clasp arc.
(3) If α ⊂Gϵ,δ is a loop which bounds a disc ∆in PA, then int(∆) contains at
least two puncture end-points of clasp arcs, one from some γi
ϵ and the other from
γi
−ϵ.
(4) If v ∈Gϵ,δ is an endpoint vertex, then either link(v) contains a puncture endpoint
of a clasp arc or v lies in a normal neighborhood of a clasp arc.
Proof In the case of an embedded surface, details on how to pass from the analogue of
Proposition 5.1.1 to that of the Corollary are given in the proof of [4, Lemma 3.8]. We
have modiﬁed the statement of [4, Lemma 3.8], by saying that if a disc ∆exists with
the stated undesirable properties, then ∆is not a good disk. In the case of assertion (3)
of the Corollary we need the puncture endpoints of both γi
+ and γi
−because if both are
not in ∆then ∆will be embedded, but no such embedded disc exists.
Remark 5.1.1 Armed with Corollary 5.1.1, the reader is advised to go back and look
at Figure 6 again. It was intuitively clear, when we ﬁrst presented this sketch, that the
unwinding process which is illustrated in the passage from left to right ought to be
‘complexity-reducing’. Now that we have ﬁnally deﬁned an appropriate complexity
function we can understand exactly what that means.
We need the modiﬁcations of Corollary 5.1.1 for the following reason: If it should
happen that the given braid X−is wound up some number of times as on the left, and if
we were to modify X+ but leave X−unaltered, then we might be able to use exchange
moves and destabilizations to modify X+ to a minimum braid index representative,
using only complexity-decreasing moves, but if we did not modify X−too then we
would have to increase complexity at the end. That is the reason that we need the
initial complexity-reducing modiﬁcations of both X+ and X−. That is the content of
Corollary 5.1.1.
An annulus component of CA is standard if every component E ⊂Gϵ,δ on the annulus
satisﬁes the following conditions:
(1)
E is homeomorphic to either S1 or [0, 1], ie either a circle or a line.
(2) If E is a circle then it is a core circle of the annulus component.
(3) If E is a line with ∂E = p ∪p′ then p ∈Xϵ and p′ is near X−ϵ.
Geometry & Topology 10 (2006)
478
Joan S Birman and William W Menasco
An annulus component of CA is trivially foliated if it is foliated entirely by s–arcs.
Examples of a standard annulus, and of a trivially foliated annulus, are given in Figure 43.
Our second Corollary relates to modiﬁcations which may be needed after all the clasp
arcs have been shortened, that is c1 = 0.
Corollary 5.1.2 Let (X−, X+, CA) be of minimal complexity with c1 = 0. Then
each component of PA is either an annulus which is foliated entirely with s–arcs or a
standard annulus.
Proof The statement follows directly from Corollary 5.1.1, when we add the assumption
that c1 = 0.
-
+
+-
-
+
+
+
-
+
+
+
+
-
-
-
-
+
+
-
+
-
-
+
-
-
-
+
+
-
-
-
+
-
+
+
standard annulus
trivially foliated annulus
type 1d
type 0d,1
type −1d
type 0d,2
δ
δ
δ
−δ
−δ
−δ
−δ
s
−δ
δ
−δ
δ
−δ
δ
−δ
s′
s
−δ
δ
−δ
δ
−δ
δ
s′
s
δ
−δ
δ
−δ
δ
−δ
δ
s′
s
δ
−δ
δ
−δ
δ
−δ
s′
Figure 43: Examples of a standard annulus, a trivially foliated annulus, and regions in a thin
annulus. Thin annuli will be deﬁned in Section 5.3.
Remark 5.1.2 The problem of pushing X+ across such a standard annulus will be
treated in Section 5.7.
Remark 5.1.3 We know exactly how the foliation of PA looks inside a normal
neighborhood of a clasp arc. We now ask what can happen outside the union of normal
neighborhoods, when the puncture points are in the interior of PA, as in the left
and right sketches in Figure 37. An example is illustrated in Figure 44. The shaded
regions are unions of overlapping normal neighborhoods of clasp arcs. The clasp arcs
in question are negative. We show only one of them, to avoid clutter and enable us
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
479
+
+
_
_
+
+
+
+
+
+
+
+
U
V
Y
Z
J
K
W
W′
W′′
Figure 44: The foliation of PA, near the puncture point of a clasp arc γ−but outside its normal
neighborhood. It is assumed here that the puncture point of γ−is in the interior of PA.
to focus on the features which are of interest now. It is to be compared with the right
sketch in Figure 37. The boundaries of the region we are studying are indicated with
dotted black and grey arcs transverse to the foliation because in general they are in the
interior of PA (although in special cases there is no reason why they could not be X+
and X−. This sketch will be used in Section 6 in the proof of the ﬁniteness of T (m).♦
