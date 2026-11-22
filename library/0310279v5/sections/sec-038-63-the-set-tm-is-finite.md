---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-038-63-the-set-tm-is-finite
section_title: "The set T(m) is finite"
section_number: 6.3
pages: 109-123
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
The set T (m) is ﬁnite
We return to the main thread of the argument. There is still one very big unanswered
question: how do we know that T (m) is ﬁnite? Proving that it is, in fact, ﬁnite, is the
main result in this ﬁnal subsection. See Proposition 6.3.1. The proof of the MTWS will
follow immediately.
We begin with an investigation of restrictions on the tiling of CA which follow from
the fact that it is a topological annulus. Let W be a vertex in the foliation of PA.
Geometry & Topology 10 (2006)
522
Joan S Birman and William W Menasco
The valence v of W is the number of singular leaves which have an endpoint on
W. Traveling around W in either direction one will encounter a cyclically ordered
sequence (t1, t2, . . . , tv) of non-singular leaf types, where each ti is either a± or b. If
this sequence includes α edges of type a± and v −α edges of type b, then we say that
W has type (α, v −α). Let V(α, v −α) be the number of vertices of valence v and
type (α, v −α) in the foliation of PA. Let E(s) be the number of s–arcs which are
boundary edges of a band of s–arcs in the foliation of PA. For example, in the foliated
annulus of Figure 43 we have E(s) = 4.
Lemma 6.3.1 The vertices in the foliation of CA satisfy the following restriction:
(6–4)
V(1, 1) + 2V(1, 0) + 2V(0, 2) + V(0, 3) =
2E(s) + V(2, 1) + 2V(3, 0) +
∞
X
v=4
v
X
α=0
(v + α −4)V(α, v −α),
with every term on both the LHS and the RHS non-negative. Notice that every vertex
type appears and is counted, with the following 3 exceptions: vertices of type (1, 2),
(2, 0) and (0, 4) do not appear in this equation because in all three cases the coefﬁcient
(v + α −4) = 0.
Proof On each annular component of PA the foliation determines a cellular decom-
position which goes over to a cellular decomposition of S2 on shrinking the 2 boundary
components to points. Letting V, E and F be the number of vertices, edges and tiles,
the fact that χ(S2) = 2 shows that on each component of the foliated surface CA we
have V + 2 −E + F = 2. Each tile has four edges and each edge is an edge of exactly 2
tiles, so that E = 2F. Combining this with the previous equation we learn that 2V = E.
Let E(a), E(b), and E(s) be the number of a–, b–, and s–edges, where we count both
a+ and a−edges as being type a. Then
(6–5)
2V = E(a) + E(b) + E(s).
Since
V
=
∞
X
v=1
v
X
α=0
V(α, v −α)
(6–6)
E(a)
=
∞
X
v=1
v
X
α=0
αV(α, v −α)
(6–7)
2E(b)
=
∞
X
v=1
v
X
α=0
(v −α)V(α, v −α)
(6–8)
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
523
we may combine equations (6–5) through (6–8) to obtain
(6–9)
∞
X
v=1
v
X
α=0
(4 −v −α)V(α, v −α) = 2E(s).
Rearranging terms, we have proved the lemma.
Our next goal is to learn which of the terms in Equation (6–4) are bounded, and which
terms can grow without bound, when we ﬁx the braid indices b(X+) and b(X−). For a
triple (X+, X−, CA) of minimal complexity with (b(X+), b(X−)) = (m, n), let N ⊂PA
be the union of all normal neighborhoods of the clasp arcs and let N ′ be its complement
in PA. As before, let V(α, β) be the number of vertices of valence v and type (α, β)
in the foliation of PA. Let V′(α, β) denote the number of vertices which are in N ′
and contribute to V(α, β).
Our primary method for accounting for the braid index of the braid X+ ⊔X−is by
counting the number of b–arcs in non-singular disc ﬁbers of H. This number is
independent of the choice of the ﬁber. Let b be a b–arc in CA ∩Hθ. Then b has 2
endpoints on A and divides Hθ into 2 subdiscs, ∆1 and ∆2. In Section 4.5 we created
normal neighborhoods of the clasp arcs, at the expense of introducing lots of b–arcs
into the foliation of CA. Those b–arcs are ones that can always be removed, if we wish
to do so, by reversing the isotopy. We need to make sure that they do not mess up our
counting process. For that reason, we now sharpen the concept of an essential b–arc.
(Up to this point, a b–arc was deﬁned to be essential if it was not inessential. )
• A b–arc b is strongly essential if the interiors of ∆1 and ∆2 each contain either
an a±– arc or an s–arc. Note that in the creation of normal neighborhoods we
never introduced new strongly essential b–arcs.
• A b–arc b is weakly essential if the interiors of ∆1 and ∆2 do not contain a±
or s arcs. The reason these are only ‘weakly essential’ is because, if their vertex
endpoints are not adjacent on A, then one of discs ∆or ∆′ contains a family
of b–arcs and the innermost member of that family will be inessential. Thus
a weakly essential b–arc can always be changed to an inessential b–arc by an
appropriate sequence of isotopies.
• A b–arc b is inessential if v and w are adjacent on A. This implies that neither
∆1 nor ∆2 contains an aϵ–arcs, an s–arc or a b–arc.
The construction of normal neighborhoods introduces numerous weakly essential b–arcs
in N . There may also be weakly essential b–arcs in N ′, e.g. b may be in N ′ but ∆
and/or ∆′ may contain b–arcs that are in N . For this reason, we reﬁne our count. We
already deﬁned V(α, β). Recall that V′(α, β) is the number of vertices which are in
Geometry & Topology 10 (2006)
524
Joan S Birman and William W Menasco
N ′ and contribute to V(α, β). Let Ve(α, βe) denote the number of vertices which are
adjacent to α a–arcs and βe strongly essential b–arcs. We will obtain the bounds that
we need from V(α, β), V′(α, β) and Ve(α, βe)
Lemma 6.3.2 The following hold for the individual terms in Equation (6–4), when the
braid indices m and n are ﬁxed and (X+, X−, CA) has minimal complexity through the
application of exchange moves (applied to X+ and X−) and destabilizations (applied to
X+):
(1)
V(1, 0) is zero.
(2)
V(α, v −α) is zero for α ≥2.
(3) If the complexity is minimal, then V′(0, 2) = V′(0, 3) = 0.
(4)
Ve(1, 2) and Ve(0, 4) are bounded.
(5)
E(s) is bounded.
(6)
V(1, 1) is bounded.
(7)
P∞
β=3 Ve(1, βe) is bounded.
(8)
P∞
β=5 Ve(0, βe) is bounded.
Remark 6.3.1 We do not obtain bounds for V(0, 2), V(0, 3), V(0, 4), V(1, 2), V′(1, 2)
and V′(0, 4), and indeed they cannot be bounded. With this observation, we have
accounted for every possible term V(α, β) and V′(α, β) for α, β ≥0.
♦
Proof We consider the various inequalities in order:
Proof of (1) and (2) These two statements follow from Corollary 5.1.1. Speciﬁcally,
statement 1. of Corollary 5.1.1 forces V(1, 0) to be zero. If there is a vertex vϵ that
is adjacent to the boundary of PA that contributes to the count of V(α, v −α) for
α ≤2 then there are two aϵ–arcs, a1
ϵ, a2
ϵ , adjacent to vϵ that are not isotopic to each
other in the foliation. The subdisc, ∆(vϵ), that a1
ϵ ∪a2
ϵ splits off in PA can only
contain γϵ clasp arcs. The absence of γ−ϵ makes ∆(vϵ) embedded when considered in
CA. This implies that all components of Gϵ,δ ∩∆(vϵ) ⊂∆(Vϵ) are simply connected,
ie by statement 3. of Corollary 5.1.1 there are no loops in the graphs Gϵ,δ ∩∆(vϵ).
This further implies that there exists a path α in either G−ϵ,+ or G−ϵ,−satisfying the
assumptions in statement 2. of Corollary 5.1.1. Since our subdisc does not contain a
γ−ϵ clasp arc, we get a contradiction of statement 2. We conclude that V(α, v −α) is
zero.
Proof of (3) By Proposition 5.1.1, if a vertex W has type (0,2) or (0,3), and if its link
is a good disc, then that vertex can be removed by changes of foliation followed by
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
525
exchange moves, reducing complexity. However, we are assuming minimum complexity.
Therefore no such W exists, unless link(W) is not good, ie it intersects N .
Proof of (4) Suppose that W is a vertex that contributes to the count of V(1, 2). It
is near X+ or X−, so assume that it is adjacent to a strongly essential b–arc. An
example was given in Figure 58(a). In this situation we showed in Figure 58(b) that the
corresponding embedding is a root. Each new block in the root contributes at least 1
to the braid index. This forces the braid index of X+ ⊔X−to grow, contradicting our
assumption that it is ﬁxed at m + n. A similar argument applies to V(0, 4).
Proof of (5) Suppose that E(s) is unbounded. Then there will be an unbounded number
of singularities of type aϵs and/or sb. Notice that there is a direct correspondence
between the number of aϵs–singularities and the number of vertices contributing to
V(1, 0) and V(α, v −α) for α ≥2. But by statements (1) and (2) we know that V(1, 0)
and V(α, v −α), α ≥2 are bounded. Thus, the only way that E(s) can grow is if there
is a growth in the number of singularities of type sb.
Previously in Section 5.3.1 we deﬁned the notion of a complete collection of s–arcs
for thin annuli. We have a similar notion for CA and PA. A (possibly empty) family
of s–arcs S = {s1, . . . , sl : si ⊂CA} is a complete collection of s–arcs in CA if: (i)
no two s–arcs in the collection split off a sub-band of CA that is foliated entirely by
s–arcs; and, (ii) for any other s–arc s ⊂CA there exists an si ∈S such that s ∪si splits
off a sub-band of CA that is foliated entirely by s–arcs. It is immediate that cutting CA
open along a complete collection S of s–arcs decomposes CA into a disjoint union of
components that contain in one-to-one correspondence the components of CAtiled and
bands of s–arc.
Now ﬁxing CA, let S to be a complete collection of s–arcs in the foliation. Assume
that E(s) can be arbitrarily large. We know that the number of components of E(s)
which have angular length ≥2π is bounded, because each time that a band of s–arcs
travels completely around A it contributes 1 to b(X+) and 1 to b(X−). This means that
all of the growth in the cardinality |CA \ S| (which is the same as |CAtiled|) comes from
components C with the angular length of X+ ∩C and X−∩C being strictly less than 2π.
In particular, for such a component the set of ﬁbers Hθ for which Hθ ∩(X+ ∩C)̸ = ∅
coincides with the set of ﬁbers for which Hθ ∩(X−∩C)̸ = ∅, since X+ ∩C and X−∩C
have their endpoints on the same two bs–singularities. We are thus seeing a growth in
the components of CAtiled that are characterized by the condition:
• There exists an Hθ ∈H with Hθ ∩(Xϵ ∩C) = ∅, ϵ = + and −.
We conclude that the following holds: Let {C1, . . . , CJ} ⊂CA \ S be the set of
components for which there exists an Hθ ∈H such that Hθ ∩(X± ∩Cj) = ∅for all
Geometry & Topology 10 (2006)
526
Joan S Birman and William W Menasco
1 ≤j ≤J. (Note that there may be a different Hθ for each Cj.) If E(s) grows then the
index J must also grow.
Now suppose we have a subcollection of such components {Ci1, . . . , CiL} ⊂{C1, . . . , CJ}
such that for every Hθ ∈H we have that Hθ ∩[S
1≤j≤L Cij] contains a strongly essential
b–arc. Then this subcollection contributes to the braid index of X+ ⊔X−. Since our
braid index is ﬁxed such subcollections cannot grow in number. Thus, as the index
J grows we can only have growth in a subset {C′
i1, . . . , C′
iL′} ⊂{C1, . . . , CJ} with the
property that there exists a ﬁxed disc ﬁber H′
θ with H′
θ ∩[S
1≤j≤L′ C′
ij] being a union of
weakly inessential b–arcs. Pushing these weakly essential b–arcs off of H′
θ we see that
the isotopy across the components {C′
i1, . . . , C′
iL′} can be achieved in the complement
of A. Thus, our original triplet (X+, X−, CA) has unnecessary motion and was not of
minimal complexity. But, we are assuming that we started with minimal complexity.
Thus, E(s) cannot grow.
Proof of (6)
We refer back to Proposition 5.3.1 to establish the boundedness of
V(1, 1). If we consider the construction of S+ and S−we know from (1) and (2) of
Proposition 5.3.1 that there can be at most m type 1d regions in S+ and n type −1d
regions in S−. Each type 1d (resp. −1d) region in S+ (resp. S−) accounts for two
vertices that contribute to the count of V(1, 1). So if V(1, 1) is able to increase it must
be through either the occurrence of type 0d,1 and 0d,2 regions in S+ and S−, or through
the occurrence of a subregion like those in Figure 57. (The distinguishing feature
between the two cases is whether the clasp arc intersecting the region is long or not.)
An increase in the latter will not increase b(X+) + b(X−) since it will be associated
with a G–exchange move. So we need only consider growth in S+ and S−.
If V(1, 1) is allowed to grow arbitrarily large then there will be one annular component
of PA that will contribute an arbitrarily large number of vertices to the count of V(1, 1).
Thus, we will have a single component of PA which will contribute an arbitrarily large
number of type 0d,1 or 0d,2 regions to the construction of either S+ or S−. Since this
growth occurs on a single component of PA, any two type 0d regions on that PA
component will be adjacent to a common s–band, (an assumption which is needed to
apply (3) and (3′) of Proposition 5.3.1).
Focusing on S+, we know from (2) of Proposition 5.3.1 that we cannot have growth in
the number of pairs of type 0d,1 regions and type 0d,2 regions that intersect each other.
From (5) of Proposition 5.3.1 we know that we cannot have a single region (see R3 in
Proposition 5.3.1) which is intersected by a growing number of type 0d regions. (By
Remark 5.3.1 any R3 region in S+ or S−will be a fan, which is an assumption needed
for the application of (3) and (3′) of Proposition 5.3.1.)
Thus, we can only have an increase in V(1, 1) if it comes from a pair of intersecting
regions. Dealing with the growth of V(1, 1) in S+, we list the possibilities: (i) a
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
527
type 0d,1 could intersect another type 0d,1; (ii) a type 0d,1 could intersect a type 0d,2;
(iii) a type 0d,1 (or 0d,2) could intersect a type 1d; or (iv) a type 0d,1 (or 0d,2) could
intersect a type −1d. If we have possibility (i), for one of the (1, 1) vertices the link(v)
will be a good disc and we could have eliminated it by (7) of Proposition 5.1.1. This
violates our minimal complexity assumption, so possibility (i) does not occur. If we
have possibilities (ii) or (iii) then by (2) and (2′) of Proposition 5.3.1 there will be a
contribution of +1 to b(X+). So these occurrences are bounded.
Finally, we consider the growth of V(1, 1) in S+ through an unbounded number of
occurrences of possibility (iv). Suppose there is growth in pairs of regions (R0, R−1d)
such that: R0 ⊂S+ is a type 0d,2 region; R−1d ⊂S+ is a type −1d region; and
ρ(R0) ∩ρ(R−1)̸ = ∅. We refer the reader back to Figures 46 and 43, and adapt them to
our purpose at hand. In Figure 43 we see an illustration of a type −1d region. Given
such a region we can perform the inverse of the operation illustrated in the top sketch of
Figure 46 to introduce an inessential b–arc that is positioned as the ‘left most’ b–arc
in R−1d . (Referring to the type −1d region in Figure 43, as we traverse the black
boundary in the direction of its orientation, with this introduction of an inessential
b–arc, the ﬁrst ﬁrst singularity of parity δ will no longer be associated with a clasp
intersection.) Now, if we stabilize X+ along this ﬁrst singularity we will eat into R−1d
and the remaining portion of R−1d will be a type 0d,1 region which we call R′
−1d . The
new stabilized X+ we call X′
+, and we will have b(X′
+) = b(X+) + 1. But, since R0
is type 0d,2 and ρ(R0) ∩ρ(R′
−1d)̸ = ∅, by (3) of Proposition 5.3.1 we know that this
intersection contributes +1 to b(X′
+). Since X′
+ came from X+ by a single stabilization
we know 2 ≤b(X′
+) = b(X+) + 1. Thus, if we had x such (R0, R−1d) pairs, for each
pair we could have performed a similar stabilization on X+ to produce a braid X′
+; and
we would know that 2x ≤b(X′
+) = b(X+) + x. This implies x ≤b(X+). So we have
bounded V(1, 1).
Proof of (7) and (8) We study Equation (6–4) and ask which terms can grow without
bound on both sides? By statements (1) and (6) of this lemma we know that the
terms V(1, 0) and V(1, 1) on the LHS cannot grow without bound for ﬁxed m and n.
By statement (3) of this Lemma we know that if V(0, 2) and/or V(0, 3) on the LHS
grow without bound, then the growth must occur inside the union N of all normal
neighborhoods of clasp arcs. By equation (7) we know that a growth in V(1, 1) will
force a growth in P∞
β=3 V(1, β) or E(s).
Passing to the RHS of Equation (6–4), we know from statement (5) that E(s) cannot
grow without bound, for ﬁxed m, n. By statement (2) we know that V(2, 1) and V(3, 0)
are bounded. But then, the only terms which might not be bounded, on the RHS of
Equation (6–4), are those in the double sum. However, of the terms in the double sum
we know from statement (2) that V(α, v −α) is bounded if α ≥2.
Geometry & Topology 10 (2006)
528
Joan S Birman and William W Menasco
Suppose that β is bounded but that V(1, β) increases without bound. This means that
there is some ﬁxed value of β for which there are arbitrarily many vertices of type (1, β).
An example was illustrated earlier, in Figure 44. In this illustration vertices U, V, Y, Z
are vertices ‘at the bottom’ of a region that is composed of normal neighborhoods (see
the right sketch of Figure 37), and the vertices W, W′′ can be thought of as ‘coning’
these vertices and their associated singular leaves. (The vertex W′′ should be thought
of in a similar manner.) Then W and W′′ contribute to the count of V(0, β) or V(1, β)
and we are able to see the interplay between these terms and V(0, 2) and V(0, 3) in
equation (7). The vertices U, V, Y, Z are in N , but are adjacent to a vertex outside of
N . They have valence 2.
Such a coning idea can be iterated. Referring back to Figure 62, if we imagine
an additional vertex W′′′ lying below the black dotted arc we could conceivably
cone W, W′, W′′ and all of the associated singular leaves to such a W′′′. Since the
number of vertices in the shaded region (vertices like U, V, Y, Z) can possibly grow,
the number of vertices coning the bottom (or top) of a region composed of normal
neighborhoods can also grow. And, the number of vertices coning the W–ﬂavored
vertices can then also grow, etc. So we see that there is no inherent reason why
P∞
β=5 V(0, β) or P∞
β=3 V(1, β) should be bounded. However, we need only establish
that P∞
β=5 Ve(0, βe) or P∞
β=3 Ve(1, βe) are bounded.
By construction the vertices that contribute to Ve(0, βe) and Ve(1, βe) count are outside
normal neighborhoods. We suppose that a growth in them is balanced in Equation (6–4)
by a growth in V(0, 2) and V(0, 3) that are associated with the normal neighborhoods
of γ+ arcs.
We need to go back to our original construction of CA and extract an embedded
annulus from CA that contains the vertices that contribute to the P∞
β=5 Ve(0, βe) or
P∞
β=3 Ve(1, βe). We do this by taking a tab neighborhood for each γ−⊂PA (see
the left sketch of Figure 38) and removing it from PA and its image from CA. (This
is equivalent to stabilizing X−along all of the singular leaves that are in the tab
neighborhoods of the preimages γ−of the clasp arcs.) Through an abuse of notation
(and in keeping with Section 2) we call this embedded annulus A+.
Recall the notation X−, X0, X+, A−, A+ from the basic construction in Section 2.
Choose an annular neighborhood A0 of X0 in A+ ∪A−which does not intersect the
clasp arcs. Then A0 is embedded and has X0 as its core circle. Since A+ and A−
are both embedded, we may extend them to embedded annuli A′
+ = A+ ∪A0 and
A′
−= A−∪A0 which have a common framing, also both are embedded and both
have X0 as a core circle. From the construction in Section 2 we know that the algebraic
linking number Lk(X−, X0) = 0. It then follows that the linking number Lk(X+, X0) is
also 0, and so A′
+ can be extended to a minimal genus Seifert surface F+ (different
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
529
from the one which we used in Section 2) having X+ as its boundary. Observe that
all of the vertices that contribute to P∞
β=5 V(0, β) or P∞
β=3 V(1, β) are in A+, and so
also are in F+.
Now consider the count P∞
β=5 Ve(0, βe) on A+ ⊂F+, and suppose we have a type
(0, 2) vertex, v ∈A+. The possibilities are: that both of the b–arcs that are adjacent to
v are strongly essential; or one is strongly essential and the other is weakly essential; or
both are weakly essential. (Our notion of weakly essential and strongly essential are
now with respect to the surface F+.) We observe that if we have the last case, when we
eliminate either of the weakly essential b–arcs using an exchange move and the surgery
in Figure 25, the sum P∞
β=5 Ve(0, βe) will remain constant. (Referring to the labeling
in Figure 25, any strongly essential b–arcs that were adjacent to the vertex w1 will
be adjacent to the vertex w2 after the surgery. Thus, the essential valence of w2 will
increase by exactly the essential valence of w1.)
Next, we observe that the count P∞
β=5 Ve(0, βe) is invariant under our change in
foliation illustrated in Figure 20. This is proved by examining the changes in the
Hθ–sequence under the change in foliation (which reverses the order of the associated
singularities).
So we allow in A+ the conversion of type (0, 3) vertices to type (0, 2) vertices, and the
elimination of type (0, 2) vertices if both of the adjacent b–arcs are weakly essential.
Such alterations to A+ keep P∞
β=5 Ve(0, βe) constant. If the number of type (0, 2)
vertices which we cannot eliminate in this manner is arbitrarily large then, since for
each such vertex there is a strongly essential (with respect to F+) b–arc, the braid
index of X+ will be unbounded. (Basically, A+ is forcing the existence of a block and
strand tree of arbitrarily high index as described in Section 5.5.) Since we cannot have
an arbitrarily large number of such type (0, 2) vertices adjacent to strongly essential
b–arcs, and they balance out P∞
β=5 Ve(0, βe), this sum must be bounded.
A similar argument applies to P∞
β=3 Ve(1, βe). Also, we can interchange the role X+
with X−, using A−instead of A+. (A subtle point is that we will have to change the
orientation of A−to match that of X−.) This completes the proof of Lemma 6.3.2.
Remark 6.3.2 It is interesting to note the similarities between (6–4) and [10, Equa-
tion (7)]. Given any Seifert surface, F with Euler characteristic χ(F), assume that F is
tiled by aa–, ab– and bb–tiles. Using the notation introduced earlier for V(α, β) , we
have
(6–10)
V(1, 1) + 2V(0, 2) + V(0, 3) =
4χ(F) + V(2, 1) + 2V(3, 0) +
∞
X
v=4
v
X
α=0
(v + α −4)V(α, v −α).
Geometry & Topology 10 (2006)
530
Joan S Birman and William W Menasco
In our proof of statements (7) and (8) of Lemma 6.3.2 we used the fact that A+ can
be extended to a Seifert surface F+ bounded by X+. In Equation (6–4) we noticed
that when dealing with a bounded braid index, growth in the values V(0, 2), V(0, 3) is
balanced by growth in the values V(α, v −α) for α = 0, 1 and 4 ≤v. So in Equation
(6–10), if there is any additional growth in the values V((α, v −α) for 0 ≤α and
4 ≤v it must be balanced out by (positive) growth in the value −χ(F+). (If there are
any vertices in F+ \ A+ that contribute to the count of V(0, 2) or V(0, 3) then by our
argument in [10] they would have been eliminated through changes in foliation and
exchange moves.) In other words, one can think of A+ as being the largest subannuli in
F+ such that when Equation (6–10) is specialized to the surface F+ \A+, growth in the
sum V(2, 1) + 2V(3, 0) + P∞
v=4
Pv
α=0(v + α −4)V(α, v −α) is balanced precisely by
growth in the genus of F+. As the number of tiles of F+ grow the only way A+ ⊂F+
can intersect these additional tiles is by s–bands going through aa– or ab–tiles parallel
to the X+ boundary. The braiding of s–bands of A+ that comes from them running
through aa– or ab–tiles of F+ can be seen as accounting for some of the braiding that
occurs in the ﬁxed blocks of a block-strand diagram.
♦
Proposition 6.3.1 Choose any positive integer m. Then for each ﬁxed positive integer
n ≤m the set of templates in T (m, n) is ﬁnite. Moreover, while the ﬁnitely many
templates in T (m, n) depend on the braid indices m and n of ∂A, they do not depend
in any other way on the choice of A.
Proof The idea behind the assertion that T (m) is ﬁnite is that the parts of the foliated
clasp annulus CA which can grow without bound when we ﬁx the braid index of the
boundary are all inside the blocks. In this regard observe that a block of braid index
k < m can contain an unbounded number of distinct k–braids, and of course in any one
example the k–braid assignment to the block contributes to the foliation of CA. The
hard part of the proof is to show that in all cases where aspects of the foliation of CA
grow without bound, the growth in a template T = (D+, D−) can be understood as
occurring inside the blocks of D+ (which are also the blocks of D−).
We begin by deﬁning a subset of CA which contains precisely the information that we
need to construct a template in T (m). In this regard we remark that one of the beautiful
features of block-strand diagrams is that most of the detailed information about the links
that they support is concealed in the blocks, however we do not need to know details
of what is in the blocks to construct the templates. Therefore we really need a rather
limited amount of information from the foliation of CA to construct the templates in
T (m).
A b–arc in CA is said to be near Xϵ, ϵ = ±, if it has a vertex endpoint that meets an
aϵ–arc. The subset BS of CA which is of interest to us now is the union of all s–arcs
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
531
and a± arcs in CA, together with all b–arcs which are near X+ or X−, enlarged to a
closed neighborhood in CA which is chosen so that its boundary (which include both
X+ and X−) is a union of simple closed curves which are transverse to the foliation
of CA. We call it the boundary support of PA, because it is the subset of PA which
determines the embeddings of D+ and D−in 3–space, by Proposition 3.1.1 and the
construction in Section 5.4. In the example in Figure 56 the boundary support includes
everything except the b–arcs which join vertices 5 and 11, and also vertices 2 and 14.
In generic examples BS will be a very small subset of PA.
By deﬁnition BS includes the thin annuli, S+ (resp S−) which are associated to X+
(resp. X−), and all b–arcs in CA that are near X+ ⊔X−. A clasp arc pair (γ+, γ−)
in PA induces a clasp arc pair (γ+, γ−) in BS. It follows from the deﬁnition of BS
that clasp arcs in CA are in BS if and only if they are doubly long. For, if it happens
that γi
ϵ is long but γi
−ϵ is not, then BS will be embedded near Xϵ, even though CA
is not embedded near γi, and we are studying the part of PA which determines the
embedding of the template in 3–space. Notice further that an s–arc is in CA if and only
if it is in BS. From now on we will drop the parity subscripts for a–arcs when we talk
about the induced foliation on BS.
As before, N ⊂PA be the union of all normal neighborhoods of the clasp arcs and
let N ′ be its complement in PA. Initially, we let Ndl be the union of all normal
neighborhoods of all doubly long clasp arcs in PA. These are the clasp arcs with the
property that we can push X+ across it all the way to X−by a sequence of microﬂypes
that amalgamate to a ﬂype. (Other clasp arcs are not doubly long initially, but may
become doubly long after G–exchange moves.) We enlarge Ndl by adjoining to it any
ab–tile that has only weakly essential b–arcs intersecting the boundary of our initial
Ndl. We allow continual enlargement of Ndl in this fashion until any ab–tile that
intersects Ndl and has only weakly essential b–arcs is also in Ndl. Next, let N ′
dl be
the complement of Ndl in N . Let S be the union of all bands of s–arcs. It will be
convenient to divide the foliation of BS into parts:
•
BS1 = S, the union of all bands of s–arcs.
•
BS2 = BS ∩Ndl.
•
BS3 = BS ∩N ′
dl.
•
BS4 = BS ∩N , the intersection of BS with the union of all normal neighbor-
hoods of all clasp arcs.
•
BS5 = BS \ (BS1 ∪BS4), ie the part of BS that is non-trivially tiled and
outside all of the normal neighborhoods.
If A is a subset of PA, let |A| denote the number of connected components in A.
Claim
|BSi| is bounded for i = 1, 2, 3, 4, 5.
Geometry & Topology 10 (2006)
532
Joan S Birman and William W Menasco
Proof of claim
|BS1| = |S| is bounded, because every band of s–arcs has 2 s–edges,
but by (5) of Lemma 6.3.2 we know that the number of s–edges in the foliation of CA
is bounded. Suppose next that |BS2| = |BS ∩Ndl| is unbounded. Since the clasp arcs
in Ndl are doubly long, there must be some connected component of PA split along the
bounded set S which has the property that as one travels along X± in this component
one passes from Ndl to N ′
dl an unbounded number of times. However, studying the
regions in Figure 43 we see that this would violate (4), (5) and (6) of Lemma 6.3.2, so
this cannot happen. The identical argument shows that |BS3| = |BS ∩N ′
dl| is also
bounded. (Remark: this does not say that there is a bound on the number of clasp arcs,
in fact no such bound exists.) Since BS4 = BS2 + BS3 it follows that |BS4| is also
bounded. Since BS5 is the part of BS that is non-trivially tiled and outside the union
of all normal neighborhoods, it follows that as we travel along a component of X± we
will intersect components of BS1, BS5 and BS4. We never pass from a component of
BS5 to another component of BS5 without passing through a component of BS1 or
BS4. Since |BS1| and |BS4| are both bounded, it follows that |BS5| must be bounded
too. This proves the claim.
Our next task is examine the contributions of the components of BSi to D+ and D−.
For this we need to investigate in detail (in a more general setting) the construction in
Section 5.4. Recall that to construct a template (D+, D−) we needed to understand four
aspects of its structure: the moving blocks, the moving strands, the ﬁxed blocks and the
ﬁxed strands. We analyze each separately.
Moving blocks An amalgamating block B will be moved to an amalgamating block
B if and only if B and B are related amalgamating blocks as deﬁned in Section 5.6.
This assumes that they are associated to clasp arcs which are doubly long in PA. Thus
the moving blocks will be associated to Ndl. Note that there may be some choices
involved when we select the amalgamating blocks. We make those choices in such a
way that the set of all moving blocks has minimal cardinality.
The strands of X+ which are incorporated into an amalgamating block lie in the black
boundary of Ndl, ie in the subset BS2 of BS. We have already proved that BS2 is
bounded. We know that if a subarc of X+ ∩Ndl is related to a corresponding subarc of
X−∩Ndl, then their angular lengths coincide. So let {N1, . . . , Nr} = Ndl be a listing
of all of the components. For each component Ni we deﬁne its angular support ∠Ni to
be the interval [θ0
i , θ1
i ] ⊂[0, 2π) for which θ ∈[θ0
i , θ1
i ] iff Hθ ∩[(X+ ∪X−) ∩Ni]̸ = ∅.
Notice that if B and B are related amalgamating blocks then the angular support of
every Ni component that intersects B (or B) must overlap, ie if each component of the
subcollection {Nj1, . . . , NjR} ⊂{N1, . . . , Nr} intersects B then ∠Nj1 ∩· · · ∩∠NjR̸ = ∅.
Since Ndl is a ﬁnite set there are a ﬁnite number of angular support intervals, and for
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
533
those intervals there are only a ﬁnite number of possible intersection subsets. Thus,
there are only a ﬁnite number of possible moving blocks in any template of T (m, n).
Moving Strands
Every subarc of X+ which is away from the bands of s–arcs is
potentially a moving strand, however some of these potential moving strands have been
amalgamated into moving blocks. We separate the surviving moving strands into two
types:
(a) Moving strands that are the subarcs of X+ which are in ∂Ndl but were not
amalgamated into moving blocks. The ﬁniteness of this set of strands follows
from the argument we used to prove that the number of moving blocks is ﬁnite.
(b) Moving strands that are the subarcs of X+ which intersect BS5. Since |BS5|
is bounded, we can restrict ourselves to the strands which intersect a single
component of BS5.
By Proposition 3.1.1, the embedding of these strands is determined by the ordering and
signs of the vertices and singularities which belong to a tile in BS5 which intersects
X+. If we can show that the number of such vertices is bounded, it will follow that the
number of singularities is also bounded. Since the number of distinct ways to assign
orders and signs to a ﬁnite set of vertices and singularities is ﬁnite, it will then follow
that the number of possible arrangements of the moving strands in set (b) is bounded.
The vertices in question contribute to the count of V(1, β), and unfortunately could be
unbounded. For example, since we can have arbitrarily many clasp arcs, the number of
vertices contributing to the count of V(1, 2) can be arbitrarily high. But, these vertices
are adjacent to weakly essential b–arcs which do not add information to the positioning
of our type (a) or (b) strands. Thus, the only vertices that we need to be concerned with
are the ones that contribute to the count of Ve(1, βe). By statement (7) of Lemma 6.3.2,
we know that they are bounded. Thus, there are only a ﬁnite number of possibilities for
the positioning of moving strands in any template in T (m, n).
Fixed blocks The argument here is more subtle than the one for the moving blocks,
because the ﬁxed blocks are associated to bands of s–arcs, and so there is no tiling
to work with. Nevertheless, we can relate the phenomenon of block amalgamation
to the tiling, in the following way. Recall (see the construction in Section 5.4) how
the ﬁxed blocks are formed. Let CA be the clasp annulus and let CAtiled be the part
that is not foliated by s–arcs. Let {θ1, . . . , θr} be a listing of all of the singularities
in BS ∩CAtiled. For each θ in one of the intervals [θi, θi+1] we know there are no
singularities. For each such θ we also know that Hθ contains a–arcs and b–arcs and
s–arcs. So (Hθ \ [Hθ ∩CAtiled]) is a collection of discs, each containing only s–arcs
(with some discs possibly containing no s–arcs). Each component of the union over all
Geometry & Topology 10 (2006)
534
Joan S Birman and William W Menasco
θ ∈[θi, θi+1] of the set {(Hθ \ Hθ ∩CAtiled)} has a D2 × [θi, θi+1] structure. Let C
be one such component. If C contains bands of s–arcs. amalgamate them into a single
block B(C). If C contained no bands or just a single band then B(C) is either vacuous
or a single ﬁxed strand.
Now it may happen that there is another connected component C′ with its associated
block B(C′), such that we have the amalgamation condition
(6–11)
{s−arcs} ∩C′ ∩Hθi+1 ⊂{s−arcs} ∩C ∩Hθi+1.
If this happens, amalgamate B(C′) and B(C) and delete the singularity at θi+1, so
that we have a single block B(C ∪C′). (If B(C′) was vacuous or a single strand then
B(C ∪C′) is essentially still B(C).) Continue this amalgamation process as long as
possible. Among all amalgamated blocks discovered in this way, choose one such that
the set of ﬁxed blocks has minimum cardinality. In this way we will have eliminated
some number of singularities, ie the ones which separated the new-amalgamated blocks.
Let θ1, . . . , θp be the angles which remain. We need to show that this listing is bounded,
when b(X+) and b(X−) are ﬁxed.
To do this we consider the effect a singularity has in the Hθ–sequence when weakly
essential b–arcs are used. We refer to Figure 18, where the possibilities for the b–edges
of bb– and ab–tiles are illustrated. Each could be either strongly or weakly essential.
Figure 62: The possibilities for b–edges of bb– and ab–tiles. A black undotted b–edge means
strongly essential A black dotted b–edge means weakly essential.
First, note that occurrences of aa–singularities will effect the block amalgamation
condition stated previously, ie (6–11) above. So the occurrence of aa–singularities will
register in our listing of remaining angles θ1, . . . , θp. But, by statements (1), (2) and
(3) of Lemma 6.3.2 we will have a bounded number of such singularities.
Second, notice that among the possibilities for bb–tiles, (1) and (2) will not effect our
amalgamation condition, because weakly essential b–arcs split off regions that contain
no s–arcs. This is also true for (1) and (2) in our possibilities for ab tiles.
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
535
Thus, the only possibilities that effect the amalgamation condition are (4), (5) and (6)
for bb–tiles, and (3) for ab–tiles.
Now by statements (1), (2), (4), (6), (7) and (8) of Lemma 6.3.2 there are a bounded
number of strongly essential b–arcs in a ﬁxed ﬁber of H. So there are a bounded
number of singularities that can effect our amalgamation condition. Thus, the growth in
our remaining angles θ1, . . . , θp is bounded. (It is interesting to notice that since the
tiles in the normal neighborhoods have all of their sides labeled wi they do not effect
the amalgamation condition.)
We have in fact established more than just that there are a ﬁnite number of ﬁxed blocks.
We have established that there are only a ﬁnite number of possible positions for ﬁxed
blocks. This is because there are only a ﬁnite number of positions for vertices that
contribute to the count of Ve(α, βe) and, thus, a ﬁnite number of singularities that
correspond to possibilities (3)–(5) for bb tiles and possibilities (2) and (3) for ab tiles.
Therefore any combinatorial information having to do with cyclic ordering of vertices
on A and cyclic ordering of singularities in H is also ﬁnite.
Fixed strands
If the number of moving blocks, moving strands and ﬁxed blocks
is ﬁnite then the number of ﬁxed strands must be ﬁnite. Using the observation we
employed to establish the ﬁniteness of positions of ﬁxed blocks, we can establish
ﬁniteness of the positions of ﬁxed strands.
Thus everything is bounded, and so the number of block-strand diagram pairs is bounded.
The proof of Proposition 6.3.1 is complete. But then, so is the proof of Theorem 2.
