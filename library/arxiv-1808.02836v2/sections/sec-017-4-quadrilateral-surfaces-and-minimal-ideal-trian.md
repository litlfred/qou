---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-017-4-quadrilateral-surfaces-and-minimal-ideal-trian
section_title: "Quadrilateral surfaces and minimal ideal triangulations"
section_number: 4
pages: 19-28
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low degree edges"
---
In this section we prove the following result, ﬁrst stated in the introduction. The essence of the proof is a
counting argument taking into account even edges, compression discs for the canonical normal representatives,
and types of tetrahedra. This is modelled on the blueprint for closed 3–manifolds [20, 21, 22, 28].
19
Theorem 1 Let T be an ideal triangulation of a cusped hyperbolic 3–manifold M and let H ≤ H2(M, Z2)
be a rank 2 subgroup. Then
|T|≥ ∑
0⁄=c∈H
|| c||.
Moreover, in the case of equality the triangulation is minimal, each canonical normal representative of a non-
zero element in H≤ H2(M, Z2) is taut and meets each tetrahedron in a quadrilateral disc, and the number of
tetrahedra in the triangulation is even.
Note that the conclusion that each canonical normal representative meets each tetrahedron in a quadrilateral
disc is equivalent to saying that all tetrahedra are of type ∆qqq.
Proof It sufﬁces to work with a minimal ideal triangulation. For if we can show any such a triangulation
satisﬁes the desired inequality, then clearly an arbitrary ideal one does also. Moreover, if any ideal triangulation
admits equality, then it clearly must be minimal.
Let T′ be a minimal ideal triangulation of a cusped hyperbolic 3–manifoldM. Fix a subgroup H < H2(M, Z2)
of rank 2 , and let Si, i = 1,2,3, be the canonical normal representatives of the non-zero classes 0 ⁄= ϕi∈ H.
Let T be the minimal triangulation that has the smallest number of tetrahedra of type ∆/ 0amongst all minimal
triangulations of M that can be obtained from T′ by a sequence of 4-4-moves.
Following the notation used in Section 3, the union of the normal surfacesSi, i = 1,2,3, intersects the tetrahedra
of T in nqtt tetrahedra of type ∆qtt, nqq tetrahedra of type ∆qq, and so on.
Let di be the maximal number of pairwise disjoint compression discs for Si, whose union does not separate
any component of Si. We have||ci||≤− χ(Si) due to Lemma 13. Moreover, in the presence of compression
discs, we obtain the stronger bound
3
∑
i=1
|| ci||≤−
3
∑
i=1
(χ(Si) +2di)
since compressions do not change the homology class and do not introduce components that are spheres or
projective planes. To simplify the expression, and with a view towards the second part of the theorem, we write
3
∑
i=1
|| ci|| =−D−∑ χ(Si),
where D≥ 0. Here, we take care of the possibility that the canonical surfaces are incompressible but not norm
minimising, and we note that each independent compression disc contributes 2 to D.
For the sake of contradiction, assume
|T| <
3
∑
i=1
|| ci||.
Lemma 14 now implies the strict inequality
ntt + nqtt + 2D +
∞
∑
d=5
(d− 4)ed < e3. (4.1)
Hence, proving the ﬁrst part of Theorem 1 is equivalent to showing that this is impossible. That is, we need to
prove that the left hand side of inequality (4.1) must be at least as large as the right hand side.
The idea of the proof is to counter-balance each contribution to the right hand side with a contribution to the
left hand side of (4.1) of equal or larger size. A contribution to the right hand side only arises from a degree
three edge, and we have already shown that each such edge is contained in a layered ∂ –punctured solid torus
subcomplex. Any such complex contains at most one edge of degree three. The organising principles for the
20
counting argument are as follows. We identify sets of degree three edges that can be associated with anH –even
edge f such that d( f )− 4 is as least as large as the size of the associated set of degree three edges (see Claim
2 and the paragraph directly after the proof of Claim 2). In doing so, we may double count some of the degree
three edges, but we make sure not to double count any of edges f . For the remaining degree three edges,
there are only a small number of special cases, in which we need to also take into account the remaining terms
ntt +nqtt +2D. Here we need to make sure that such contributions to the left hand side are only counted at most
once. Moreover, in these special cases the contribution to the left hand side of (4.1) is strictly greater than the
contribution to the right hand side.
The following terminology helps organise the counting argument. A deﬁcit in (4.1) is when the contribution
to the left is bigger than to the right, a balance in (4.1) is when they are equal, and otherwise we have a gain
in (4.1). Thus, for proving the ﬁrst part of Theorem 1 it is sufﬁcient to disregard all deﬁcits and balances and
show that it is impossible to construct a triangulation exhibiting a gain. For the second part of Theorem 1 we
also need to keep track of balances.
Recall that the core tetrahedron of any layered ∂ –punctured solid torus LST is a standard one-tetrahedron
layered ∂ –punctured solid torus LST ⋆(1,2,3). A canonical normal representative of a class of H2(M, Z2)
necessarily intersects LST ⋆(1,2,3) in one particular quadrilateral type, or not at all. This can be seen by
enumerating all 0/1-colourings of edges in LST ⋆(1,2,3) such that every face of LST⋆(1,2,3) has zero or two
edges of colour 1. Accordingly, the intersection of LST⋆(1,2,3) with all three canonical normal representatives
of non-trivial classes of H must result in a tetrahedron of type ∆qq or ∆/ 0.
It follows that either all tetrahedra in LST are of type ∆qq or of type ∆/ 0(this follows directly from looking at
the pattern of H –odd edges in the boundary). Accordingly we say that LST is of type ∆qq or ∆/ 0. A layered
∂ –punctured solid torus LST of type ∆qq has one H –even boundary edge and the other two boundary edges
are H –odd.
Claim 0: All edges of degree 3 in T are H –even.
Proof of Claim 0: Due to Lemma 11, every edge e∈ T of degree three can be associated to a maximal layered
∂ –punctured solid torus LST e⊂ T containing e in its interior. More precisely, e occurs twice in the core
tetrahedron of LST e and once in the tetrahedron adjacent to the core. If LST e is of type ∆/ 0, then naturally e
must be H –even. Hence, let LST e be of type ∆qq. Since e occurs twice in the core tetrahedron and the other
two edges in the core tetrahedron occur in it one and three times respectively, they only way the core tetrahedron
of LSTe can be of type ∆qq is for e to be H –even.
A layered ∂ –punctured solid torus LST has exactly one boundary edge of degree 1 with respect to LST . We
call the other two boundary edges non-unital.
Claim 1: A maximal layered ∂ –punctured solid torus LST of type ∆/ 0containing an H –even edge of degree
three either has an interiorH –even edge of degree≥ 6, or non-unital boundary edges g and f with dLST(g) = 3
and dLST( f )≥ 5.
Proof of Claim 1: In a layered solid torus of type ∆/ 0every edge is necessarily H –even. We can thus ignore
the edge-coulourings.
Every layered ∂ –punctured solid torus LST in a minimal triangulation T and containing a degree three edge
is obtained from a layered ∂ –punctured solid torus of type LST⋆(1,3,4) by iteratively layering onto one of the
non-unital boundary edges. In LST⋆(1,3,4), the non-unital boundary edges g and f have degrees dLST(g) = 3
and dLST( f ) = 5. If we layer on f we create an interior edge of degree six and we are done. If we layer ong we
create an interior edge of degree four, the formerly unital boundary edge is now of degree three, and the degree
of g – still being in the boundary – is increased by two. Layering on the unital edge contradicts minimality,
since it creates an edge of degree two. Iterating this procedure proves the claim.
21
Claim 2: Let LST⊂ T be a maximal layered ∂ –punctured solid torus that contains an interior edge e∈ T of
degree three. Then LST is incident with an H –even edge f such that if m is the number of degree three edges
of all maximal layered ∂ –punctured solid tori incident with f , then d( f )− 4≥ m (i.e. contributing a deﬁcit or
balance in (4.1)), unless the following three conditions are satisﬁed for LST:
(1) all interior H –even edges distinct from e are of degree four,
(2) the solid torus is of type ∆qq, and
(3) the unique H –even boundary edge f is of degree one with respect to LST .
We call a maximal layered ∂ –punctured solid torus that contains an interior edgee of degree three and satisﬁes
the conditions (1)–(3) internally unbalanced.
Proof of Claim 2: No interior edge of LST distinct from e can be of degree less than four (see Lemma 11). If
LST contains an interior H –even edge of degree > 4, then we choose f to be this edge. It follows that m = 1,
and thus d( f )− 4≥ m holds. Hence assume that all interior H –even edges distinct from e are of degree four.
Suppose that LST is of type ∆/ 0. All edges of LST are H –even and, by the above, all its interior edges apart
from e are of degree four. But then, by Claim 1, there exists a boundary edgef∈ ∂ LST satisfying dLST( f )≥ 5.
Now m− 1 additional maximal layered solid tori containing degree three edges meet f in one of their H –even
boundary edges. By Lemma 12, f is of degree at least 4 + 2m. Thus d( f )− 4≥ 2m > m and we have a deﬁcit
in (4.1).
The last case is that LST is of type ∆qq. Since LST is of type ∆qq it has a unique H -even boundary edge
f∈ ∂ LST. If dLST( f ) > 1, then dLST( f )≥ 3. Again m− 1 additional maximal layered solid tori containing
degree three edges are incident with f . By Lemma 12, f is of degree at least 2+2m. Thus d( f )−4≥ 2m−2.
So if m≥ 2, then d( f )− 4≥ m. If m = 1, then we claim that the degree of f is at least ﬁve. Suppose it is not.
Then the neighbourhood of f is modelled on a layered ∂ –punctured solid torus having one more tetrahedron
than LST but extra identiﬁcations between the boundary edges. This is not possible due to maximality and
Lemma 10. Hence no identiﬁcations are possible amongst the edges and so d( f )≥ 5.
The set of internally unbalanced maximal layered∂ –punctured solid tori can now be canonically partitioned, by
grouping together those which meet along their uniqueH –even boundary edge. Fix one such set ofm internally
unbalanced maximal layered ∂ –punctured solid tori around a common H –even edge f . Its contribution to the
right hand side of (4.1) is m. But f must be of degree at least 2m by Lemma 12, and its contribution to the left
hand side of (4.1) is≥ 2m−4. Hence, there is a deﬁcit if m > 4. We therefore consider the cases wherem≤ 4.
If m = 4 and d( f ) > 8, we also obtain a deﬁcit.
Special cases: Since the degree d = deg( f ) of f is bounded below by four, we obtain at most a balance if:
(m,d)∈{ (4,8), (3,7), (2,6), (1,5)},
and we obtain at most a gain if:
(m,d)∈{ (3,6), (2,5), (2,4), (1,4)}.
We call the edges in the above collections the balancing edges and the gaining edges, respectively.
The maximal potential gain is 2 in the case (2,4) and it is 1 in all other cases. Our strategy now is to visit
each edge f that gives a potential gain, show that it either achieves a deﬁcit, or (even stronger) that it achieves
a deﬁcit for itself and all H –even edges in its star.
Before taking a closer look at these cases, we ﬁrst prove an auxiliary statement. For this and for the remainder
of this proof, we denote the tetrahedra around f by ∆1, . . . ,∆d (labelled in cyclic order such that ∆i shares a
triangle with ∆i+1; some tetrahedron may appear in this sequence multiple times). Moreover, without loss of
22
generality and following Lemma 12, the internally unbalanced maximal layered ∂ –punctured solid torus LSTi
incident to f can be assumed to contain ∆2i−1, 1≤ i≤ m.
Claim 3: In all four cases (m,d)∈{ (3,6), (2,5), (2,4), (1,4)}, the edge f is surrounded by d pairwise distinct
tetrahedra.
Proof of Claim 3: Tetrahedra contained in distinct internally unbalanced maximal layered ∂ –punctured solid
tori must be pairwise distinct. Hence the tetrahedra ∆2i−1, 1≤ i≤ m, are pairwise distinct since ∆2i−1 is
contained in LSTi .
A tetrahedron of type ∆qtt cannot occur twice around f because it has only one H –even edge and, of course,
there can be no tetrahedron of type ∆qqq. Moreover, only ∆3 in case (1,4) can be of type ∆/ 0, and hence a
tetrahedron of type ∆/ 0cannot occur more than once around f .
If f occurs more than once in a tetrahedron ∆ of type ∆tt, then we must be in (2,5) or (1,4) since f is
contained in a face only havingH –even edges. In case (2,5) we have ∆ = ∆4 = ∆5; in case (1,4) we either have
∆ = ∆2 = ∆3, or ∆ = ∆3 = ∆4, or ∆ = ∆2 = ∆4. Assume we have one of the three cases where ∆ = ∆i = ∆i+1.
Then two faces of ∆ are identiﬁed. However, there is only one way to identify two faces of a tetrahedron of type
∆tt in an orientation preserving manner, and this creates an edge of degree one, which is not possible. Hence
we are in case (1,4) and ∆ = ∆2 = ∆4. Then ∆3 is necessarily of type ∆/ 0. But ∆/ 0cannot share two distinct
faces with ∆2 = ∆4 because a tetrahedron of type ∆tt only has one triangle of H –even edges.
The remaining tetrahedron type ∆qq can occur in all cases and in all places around f . To start suppose ∆2 is of
type ∆qq; one of the H –even edges of ∆2 is f and we denote the other f′. If ∆2 appears more than once around
f , then f = f′. In particular the two faces of ∆2 containing f′ meet ∆1 in at least two edges and hence cannot
be identiﬁed with a tetrahedron ∆2i−1, 2≤ i≤ m. This shows that in the cases (3,6) and (2,4) all tetrahedra
must be pairwise distinct by the symmetry of the situation.
In the case (2,5) this implies that ∆2 cannot equal ∆4. However, ∆2 also meets a face of ∆3 and by the same
reasoning cannot equal ∆5. The only remaining possibility in this case is that ∆4 equals ∆5. Here again, ∆5
meets ∆1 in a face, and hence if ∆4 equals ∆5, then ∆1 and ∆3 share two edges, which is not possible.
It remains to consider the case (1,4). First suppose that ∆2 and ∆3 are the same tetrahedron. There are two
possibilities that are combinatorially equivalent. Taking all the face pairings into account, we conclude that
∆2 is a 1–tetrahedron LST ⋆(1,2,3). But this meets ∆1, and hence LST 1, in three edges, a contradiction. See
Figure 14 for an illustration of this case.
Figure 14: Identifying ∆2 and ∆3 in case (1,4) yields a one-tetrahedron layered solid torus meeting LST 1
in three edges.
Hence suppose without loss of generality that ∆2 and ∆4 are the same tetrahedron. Analysing the two different
gluings that arise, we see that ∆2 is layered on one of the two H -odd boundary edges of ∆1. But this either
contradicts maximality of LST1 or it contradicts Lemma 10, see Figure 15.
23
Figure 15: Identifying ∆2 and ∆4 in case (1,4) yields a layering on the boundary of LST1 .
This completes the proof of the claim.
The case m = 2 and d = 4: Since f is H –even of degree four, we have to ﬁnd a contribution to the left hand
side of (4.1) of 2 to obtain a balance and > 2 to obtain a deﬁcit.
By Claim 3 and by the preliminary observations above, we can assume that all four tetrahedra surrounding f
are distinct and tetrahedra ∆1 and ∆3 are of both of type ∆qq. If the quadrilaterals in ∆1 and ∆3 are of distinct
colours, ∆2 and ∆4 must both be of type ∆qtt. Hence, they contribute 2 to the left hand side of (4.1). Moreover,
since these two tetrahedra then do not have anyH –even edges other than f , they cannot contribute to any other
set of maximal layered solid tori united along an H –even edge, and their contribution to (4.1) is global. In
particular, there is at most a balance and not a gain. Now one of the surfaces,Si, links the edge f in an annulus.
We can perform a compression of this annulus, using a disc transverse to f . This is indeed a compression
disc since the resulting surface is still connected, due to its intersection with the H -odd boundary edges of the
layered ∂ –punctured solid tori. Whence in total, we have a deﬁcit of 4 . We also note that this compression
disc is conﬁned to a neighbourhood of f and that the tetrahedra ∆2 and ∆4 have a unique H –even edge. Thus,
the quadrilateral discs of Si affected by this compression allow no other compressions of this kind and we may
associate the total deﬁcit with f .
We can thus assume that ∆1 and ∆3 are coloured the same. This implies that ∆2 and ∆4 must both be of type
∆qq with the same colours as well. In particular, the octahedron that is the boundary of the star of f has eight
H -odd edges, all of degree two inside the star of f , and a 4–cycle of H –even edges, all of degree 1 inside
the star of f . In this case we can perform compressions of two of the surfaces as above. Whence in total we
have a contribution of 8 to the left hand side and a contribution of 2 to the right hand side. We now allocate a
contribution of 3 to f so that in total we have a deﬁcit of 1 associated with f . We then associate a contribution
of 2 .5 to each of the other two H –even edges of ∆2 and ∆4. Hence each of these (if it is in our collection
of gaining or balancing edges) now has a deﬁcit associated with it and is not visited again. In particular, any
further compression discs we ﬁnd in the star of an H –even edge is disjoint from the ones we just found.
This completes the case of gaining edges of type (2,4) showing that they all contribute a deﬁcit. We may thus
assume that the maximal potential gain of an edge we have not yet considered is 1.
The case m = 3 and d = 6: Since f is H –even of degree six, it contributes 2 to the left hand side of (4.1).
Hence, we have to ﬁnd an additional contribution of 1 to obtain a balance and > 1 to obtain a deﬁcit.
Since LST 1, LST2 and LST 3 are internally unbalanced, ∆1, ∆3 and ∆5 are all of type ∆qq. If not all of them
are coloured the same, at least two of ∆2, ∆4 and ∆6 must be of type ∆qtt, contributing 2 to the left hand side
of (4.1) and we are done (again, note that the two tetrahedra of type ∆qtt do not have any other H –even edges,
and their contribution to the star of f is global).
24
Hence all tetrahedra ∆i, 1≤ i≤ 6, are of type ∆qq, all with the same colours. This implies that one can perform
a compression of two of the surfaces Si, i∈{ 1,2,3}, by cutting along the two tubes around the H –even edge
f , and pasting two discs, each intersecting f once (see Figure 16 for an illustration of this process). The
compressed surfaces are still embedded.
Moreover, note that three of the quadrilaterals in the tubes linking edge f are contained in layered solid tori
LST j , 1≤ j≤ 3. Hence, each such quadrilateral has its vertices identiﬁed in diagonally opposed pairs. In
particular, the compressed surfaces still have the same number of connected components, and their compo-
nents still have non-positive Euler characteristic and Lemma 13 applies. Altogether, the possibility of such
compressions yields a contribution of 8 to the term 2 D≥ 4 ∑3
i=1 di of the left hand side of (4.1).
Figure 16: Compression along an H –even edge surrounded by tetrahedra of type ∆qq. The picture only
shows one of the two parallel surfaces.
We distribute this contribution onto f and the three remaining H –even edges of ∆2, ∆4 and ∆6 equally. Thus,
all of the four edges receive a sufﬁcient contribution to give a deﬁcit in (4.1), and are not visited again (except
that they may receive additional deﬁcit from other edges). In particular, any other compression discs we ﬁnd
do not intersect the tetrahedra in the star of f .
This completes the case of gaining edges of type (3,6) showing that they all contribute a deﬁcit.
The case m = 2 and d = 5: Since f is H –even of degree ﬁve, it contributes 1 to the left hand side of (4.1).
Hence, we have to ﬁnd an additional contribution of 1 to achieve a balance and > 1 to achieve a deﬁcit.
Again, ∆1 and ∆3 can be assumed to be of type ∆qq. If ∆1 and ∆3 are of distinct colours, ∆2 must be of type
∆qtt. If there is at least one other tetrahedron of type ∆qtt incident with f , then there is a contribution to the
left hand side of 4.1 of 2 and we have a deﬁcit. Otherwise there are two distinct tetrahedra of type ∆tt also
incident with f . We obtain a contribution of 2 to the left hand side of (4.1) from these tetrahedra which needs
to be shared with the two other H –even edges, g and h of the triangle shared by ∆4 and ∆5. We can distribute
a contribution of 2
3 from these tetrahedra to the (possibly not pairwise distinct edges) f , g and h. This yields a
total contribution of 5
3 > 1 to f and hence a deﬁcit.
Hence, assume that ∆1 and ∆3 are equally coloured and thus ∆2 must be of type ∆qq with matching colours.
If any of ∆4 or ∆5 is of type ∆qtt, the other one must be as well, we obtain a contribution of 2 , and we have a
deﬁcit.
If one of ∆4 and ∆5 is of type ∆qq the other one must be as well. As before, this implies that one can perform a
compression of two of the surfaces Si, i∈{ 1,2,3}, by cutting along the two tubes around the H –even edge f .
25
Again, there is an additional contribution to the left hand side of 8 , distributed equally over the four H –even
edges of ∆2, ∆4 and ∆5 (see Figure 16). In particular, each of these edges has an associated deﬁcit.
Hence, we can assume that both ∆4 and ∆5 are of type ∆tt, both with the same colouring. We obtain a
contribution of 2 to the left hand side of (4.1) which needs to be shared with the two other H –even edges,
g and h of the triangle shared by ∆4 and ∆5. However, for this contribution to be insufﬁcient globally, both
g and h must be surrounded by some internally unbalanced maximal layered solid tori, with the tetrahedra
surrounding g and h and distinct from ∆4 and ∆5 all being of type ∆qq and of matching colours. This implies
that one can perform two compressions of two of the surfaces Si, i∈{ 1,2,3}, by cutting along the three times
two incomplete tubes around the edges f , g and h. This process replaces the two parallel triangles inside ∆4
and ∆5 by pairs of parallel normal triangles of all three other types. Again, quadrilaterals in the tubes linking
edges which are contained in a layered solid torus have their vertices identiﬁed in diagonally opposed pairs.
Hence this operation does not produce any new connected components. See Figure 17 for an illustration of this
process in the case of one surface (rather than two parallel ones).
Figure 17: Double compression along a triangle of H –even edges. Only one of the two parallel copies of
surfaces is drawn.
This double compression of two surfaces contributes a total of 16 to the left hand side of (4.1). We distribute
two to each of f , g and h, as well as to the at most three other H –even edges in the neighbourhoods of f , g
and h. The extra contribution of at least 4 is a surplus and not needed. We therefore again have a deﬁcit.
This completes the case of gaining edges of type (2,5) showing that they all contribute a deﬁcit.
The case m = 1 and d = 4: In this case, f does not contribute to the left hand side of (4.1) and we have to ﬁnd
a total contribution of 1 for a balance and > 1 for a deﬁcit.
Again, ∆1 can be assumed to be of type ∆qq. If any of ∆2, ∆3 and ∆4 is of type ∆qtt then we again have two
cases. Either at least two of these are of type ∆qtt and we obtain a contribution of at least 2 to the left hand
side of (4.1) and we are done, or one of them is of type ∆qtt and two are of type ∆tt. In this case we distribute
the contribution of 2 to the tetrahedra of type ∆tt evenly over their three H –even edges and obtain a total
contribution > 1 for f . If all ∆i, 1≤ i≤ 4 are of type ∆qq, there exist compressions for two of the surfaces
Si, i∈{ 1,2,3}, with a total contribution of 8 , which can be distributed equally over the four H –even edges
contained in ∆2, ∆3 and ∆4. This again gives a deﬁcit for all H –even edges involved.
26
There are two cases remaining (up to symmetry). In the ﬁrst case we have (without loss of generality) ∆2 of
type ∆qq and ∆3 and ∆4 of type ∆tt. Here, we fall back onto the double compression case along a triangle of
H –even edges, as done in the case m = 2, d = 5 (see Figure 17). This again gives a deﬁcit for all H –even
edges involved.
In the second case we have ∆2 and ∆4 of type ∆tt and ∆3 of type ∆/ 0. In this case, we obtain another minimal
triangulation of M by performing a 4-4-move on f . This results in two tetrahedra of type ∆tt and two of type
∆qq. But this contradicts our hypothesis that T locally has the smallest number of tetrahedra of type ∆/ 0. In
particular, this case does not happen.
This completes the case of gaining edges, showing that they all contribute a deﬁcit.
To sum up, it is not possible to achieve a gain, and hence we have proved the ﬁrst part of the theorem, estab-
lishing the basic lower bound on the number of tetrahedra.
To prove the second part, we make some additional observations regarding the balancing edges.
If the balancing edge f received a contribution > 0 as a member of the star of a gaining edge, then it has an
associated deﬁcit. Hence assume that f has not received such a contribution. If f is incident with a tetrahedron
of type ∆qtt then there is a deﬁcit. If f is incident with a tetrahedron of type ∆tt, then this tetrahedron has not
been counted yet since otherwise f would have received a contribution. We can therefore allocate 1/3 to each
edge incident with this tetrahedron and hence f has a deﬁcit.
In particular, this shows that associated to the subcomplex that is the union of all internally unbalanced tori
and all tetrahedra of type ∆qtt or ∆tt we have an overall deﬁcit.
These observations regarding the balancing edges sufﬁce to analyse the case of equality. Hence suppose|T| =
∑
0⁄=c∈H
|| c|| and so
ntt + nqtt + 2D +
∞
∑
d=5
(d− 4)ed = e3.
The above analysis shows that this equality is only possible if there is no deﬁcit since otherwise the right hand
side is smaller than the left hand side. In particular, the subcomplex that is the union of all internally unbalanced
tori and all tetrahedra of type ∆qtt or ∆tt must be empty. Whence ntt = nqtt = 0. From the possible face pairings
between tetrahedra of the different types, this implies that either all tetrahedra in T are of type ∆/ 0(but then H
has rank 0); or all tetrahedra are of type ∆qq (but then H has rank 1); or all are of type ∆qqq. Hence we have
the last case and each canonical surface is a quadrilateral surface. Since all tetrahedra are of type ∆qqq, there
are no H –even edges. Whence e3 = 0, which implies D = 0 and the three surfaces therefore are taut.
It remains to show that inevery minimal triangulations of M the canonical normal representatives of non-trivial
classes in H are taut and all tetrahedra are of type ∆qqq. Recall that T was obtained from an arbitrary minimal
triangulation T′ by 4-4 moves.
We ﬁrst note that every edge e of T is contained in at most d(e)− 1 distinct tetrahedra. Otherwise the unique
canonical representative S disjoint from e can be altered by cutting out the tube around e and pasting in two
discs orthogonal to e. Since S is taut, this operation cannot be a compression of S and thus it must produce
two connected components – one of which must be a normal 2-sphere. This contradicts the fact that T is 0-
efﬁcient due to Theorem 4. But if no edge e of T is contained in d(e) distinct tetrahedra, it is in particular true
that T does not admit 4-4-moves. Hence T′ = T . In particular, the minimality assumption on the number of
tetrahedra of type ∆/ 0is true for all minimal triangulations of M.
27
We now show that if all tetrahedra are of type ∆qqq, then the total number of tetrahedra in T is even. For this
we use the fact that M is orientable and we assume that all tetrahedra are coherently oriented. In a tetrahedron
of type ∆qqq, every boundary triangle has one 1-even, one 2-even and one 3-even edge and the orientation on
the triangle induced by the orientation of the tetrahedron determines a cyclic order of the labels 1, 2, and 3. This
is the same cyclic order for all boundary triangles of the same oriented tetrahedron. Hence there are two types
of oriented tetrahedra of type ∆qqq. Tetrahedra meeting in a triangle must induce opposite cyclic orders on this
triangle, see Figure 18. Hence, they are of different orientation types. It follows that the number of tetrahedra
is even.
Figure 18: The two orientation types of a tetrahedron of type ∆qqq .
