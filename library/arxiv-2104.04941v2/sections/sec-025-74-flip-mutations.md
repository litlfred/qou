---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-025-74-flip-mutations
section_title: "Flip mutations"
section_number: 7.4
pages: 40-44
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
to that of µrot. First, we put the coordinates of Q0– 2 into a rectangular pattern, then apply mutations
that respect [FZ99, Theorem 1.17], showing that the resulti ng coordinates are of Q1– 3. The most signiﬁcant
diﬃculty is to construct the element of G holding the appropriate generalized minors, which we obtai n by a
result of Zickert.
Lemma 7.6. Item 5 of Deﬁnition 4.16 holds.
Proof. This proof almost entirely focuses on ~µFlipcore. The preﬁx, ~µP, is a sequence of rotations as depicted
in Figure 22. The suﬃx, ~µO3~µO4~µO5, is a reordering that switches the left and right sides.
40
Letα = (g0N+,g 1N+,g 2N+,g 3N+) ∈ Conf ∗
4(G/N+), and recall Deﬁnition 4.6. For notation, let
α012 = (g0sGN+,g 1N+,g 2N+) α023 = (g0N+,g 2N+,g 3N+)
α123 = (g1N+,g 2N+,g 3N+) α013 = (g0N+,g 1sGN+,g 3N+),
with other αijk deﬁned by rotation, and let uijk be the element of N− in the canonical form of αijk . As
usual, let hij = [w0−1g−1
i gj]0.
We must show that µﬂip takes Q0– 2 to Q1– 3. By an argument entirely analogous to that of Lemma 7.5,
we assume that all edge coordinates of α123 and α013 are trivial. That is, every hij is trivial except h20 and
h02. We also appeal to Remark 2.35, and only consider A-coordinates.
By Deﬁnition 4.14, coordinates for Q0– 2 come from α012 and α023. After applying ~µP, these are rotated
to α120 and α230. Treating α230 as the rotation of α302, the coordinates are given by
∆ wkωik ,ωik
(u120) and ∆ wkωik ,ωik
(u230).
We must show that ~µFlipcore takes these to
∆ wkωik ,ωik
(u123) and ∆ wkωik ,ωik
(u013).
Now consider g = Φ −1(u123)u130h−1
31h30. We also have g =u120h20w0(h12)Φ −1(u023) by [Zic19, Proposi-
tion 5.14], and this will be identity which relates the two si des of the ﬂip. All the coordinates we need are,
up to edge coordinates, minors of g.
∆ wkωik ,ωik
(u120) = χωik
([
w−1
k [g]−
]
0
)
=χωik
([
w−1
k g[g]−1
0
(
[g]−1
0 [g]−1
+ [g]0
)]
0
)
=χωik
([
w−1
k g
]
0
)
/χωik
([g]0)
= ∆ wkωik ,ωik
(g) 1
χωik
(h20w0(h12))
= ∆ wkωik ,ωik
(g) 1
χωik
(h20)χωik
(w0(h12))
∆ wkωik ,ωik
(u302) = ∆ wkωik ,ωik
((ΦΨΦΨ)( u023))
∆ ωik ,ωik
(w0(h02)h23)
∆ wkωik ,wkωik
(w0(h02)h23)
= ∆ wkωik ,ωik
([[w0u023]+w0]−)
∆ wkωik ,wkωik
(w0(h02)h23)
∆ w0ωik ,w0ωik
(w0(h02)h23)
= ∆ wkωik ,ωik
([w0u023]−1
− )
∆ ωik ,ωik
([w0u023]0)∆ wkωik ,wkωik
(w0(h02)h23)
∆ wkωik ,wkωik
([w0u023]0)∆ w0ωik ,w0ωik
(w0(h02)h23)
= ∆ ωi∗
k
,w∗
kωi∗
k
([g]+)
∆ ωik ,ωik
([w0u023]0)∆ wkωik ,wkωik
(w0(h02)h23)
∆ wkωik ,wkωik
([w0u023]0)∆ w0ωik ,w0ωik
(w0(h02)h23)
= ∆ ωi∗
k
,w∗
kωi∗
k
(g)
∆ ωik ,ωik
([w0u023]0)∆ wkωik ,wkωik
(w0(h02)h23)
∆ ωi∗
k
,ωi∗
k
([g]0)∆ wkωik ,wkωik
([w0u023]0)∆ w0ωik ,w0ωik
(w0(h02)h23)
= ∆ ωi∗
k
,w∗
kωi∗
k
(g)
χωik
(
w0(h20h−1
30 )h12
)
∆ wkωik ,wkωik
(h03)
= ∆ ωi∗
k
,w∗
kωi∗
k
(g)
χωik
(
w0(h−1
30 )h12
)
χωik
(h02)∆ wkωik ,wkωik
(h03)
41
D1
D2
D3
E1
E2
E3
F1
F2
F3
G1
G2
G3
∆ ω1,ω1 (g)
∆ ω2,ω2 (g)
∆ ω3,ω3 (g)
∆ ωi9 ,w9ωi9 (g)
∆ ωi8 ,w8ωi8 (g)
∆ ωi7 ,w7ωi7 (g)
∆ ωi6 ,w6ωi6 (g)
∆ ωi5 ,w5ωi5 (g)
∆ ωi4 ,w4ωi4 (g)
∆ w9ωi9 ,ωi9 (g)
∆ w8ωi8 ,ωi8 (g)
∆ w7ωi7 ,ωi7 (g)
∆ w6ωi6 ,ωi6 (g)
∆ w5ωi5 ,ωi5 (g)
∆ w4ωi4 ,ωi4 (g)
Figure 34. Coordinates from α120 and α302.
∆ wkωik ,ωik
(u123) = ∆ wkωik ,ωik
([gw0]−)
=χωik
([
w−1
k gw0[gw0]−1
+ [gw0]−1
0
]
0
)
= ∆ wkωik ,w0ωik
(g) 1
∆ ωik ,w0ωik
(g)
= ∆ wkωik ,w0ωik
(g) 1
χωik
([w0[w0−1u123]−]0w0(h−1
31h30))
= ∆ wkωik ,w0ωik
(g) 1
χωik
([w0−1u123]−1
0 w0(h−1
31h30))
= ∆ wkωik ,w0ωik
(g) 1
χωik
(w0(h12h30)h23)
∆ w0ωik ,wkωik
(u130) = ∆ w0ωik ,wkωik
(Φ −1(u123)u130h−1
31h30) 1
∆ wkωik ,wkωik
(h−1
31h30)
= ∆ w0ωik ,wkωik
(g) 1
∆ wkωik ,wkωik
(h−1
31h30)
Amalgamating α120 and α302 and labeling coordinates by minors of g (up to edge coordinates) gives
Figure 34. This includes the central edge because [g]0 =h20w0(h12). This is not Q0– 2, but the diﬀerence is
only a matter of rotations and twistings.
Note that the factors ofχωik
(h20) andχωik
(h02) in the assignments for ∆ wkωik ,ωik
(u120) and ∆ wkωik ,ωik
(u302)
are exactly cancelled out by the ∆ ωi(h2) factor of m from Deﬁnition 5.18. Therefore we are justiﬁed in ig-
noring edge coordinates for the remainder of the proof since we assume the others to be trivial.
After applying
(
µR
rotTw
)
the result is ~µP(Q0– 2), with the coordinates of α120 and α230, as in Figure 35.
In this ﬁgure, since each ∆ wj ωik ,wkωik
(g) is equivalent to some ∆ cnωik ,cmωik
(g), we label vertices by the pair
(n,m ). Further, taking into account that ch =w2
0 which lifts to an element of H, we may consider n andm
modulo h.
As with µrot, each mutation in ~µFlipcore takes ∆ caωik ,cbωik
(g) to ∆ ca−1ωik ,cb−1ωik
(g) by [FZ99, Theo-
rem 1.17] and Lemma 3.8. That results in Figure 36.
Converting (n,m ) back to ∆ cnωik ,cmωik
(g), we obtain Figure 37. By the calculations above, these are
coordinates of u123 on the right and u013 (as rotated u130) on the left.
The ﬁnal combination of ~µO3~µO4~µO5 serve to swap the left and right halves by Lemma 7.2. This comp letes
the proof. □
42
D1
D2
D3
E1
E2
E3 F1
F2
F3
G1
G2
G3
(8, 6)
(8, 6)
(8, 6)
(7, 6)
(7, 6)
(7, 6)
(6, 6)
(6, 6)
(6, 6)
(5, 6)
(5, 6)
(5, 6)
(4, 6)
(4, 6)
(4, 6)
Figure 35. Coordinates from α120 and α230, labeled by (n,m ).
E1
E2
E3
F1
F2
F3
G1
G2
G3
D1
D2
D3
(3, 1)
(3, 1)
(3, 1)
(3, 2)
(3, 2)
(3, 2)
(3, 3)
(3, 3)
(3, 3)
(3, 4)
(3, 4)
(3, 4)
(3, 5)
(3, 5)
(3, 5)
Figure 36. Coordinates after applying ~µFlipcore, labeled by (n,m ).
E1
E2
E3
F1
F2
F3
G1
G2
G3
D1
D2
D3
∆ w0ω1,w0ω1 (g)
∆ w0ω2,w0ω2 (g)
∆ w0ω3,w0ω3 (g)
∆ w0ωi9 ,w0w9ωi9 (g)
∆ w0ωi8 ,w0w8ωi8 (g)
∆ w0ωi7 ,w0w7ωi7 (g)
∆ w0ωi6 ,w0w6ωi6 (g)
∆ w0ωi5 ,w0w5ωi5 (g)
∆ w0ωi4 ,w0w4ωi4 (g)
∆ w0ωi9 ,w9ωi9 (g)
∆ w0ωi8 ,w8ωi8 (g)
∆ w0ωi7 ,w7ωi7 (g)
∆ w0ωi6 ,w6ωi6 (g)
∆ w0ωi5 ,w5ωi5 (g)
∆ w0ωi4 ,w4ωi4 (g)
Figure 37. Coordinates after applying ~µFlipcore.
8. Proof of Theorem 4.19 for semisimple G
We now expand from “simple” to “semisimple”. Since the algor ithm of Section 5 really only needed the
information of G’s Dynkin diagram, and Dynkin diagrams behave very nicely wi th respect to products, the
construction easily generalizes.
43
Lemma 8.1. LetG, a semisimple Lie group over C, be G =G1 ⊕G2 ⊕ · · · ⊕Gn, with each Gi a simple Lie
group over C admitting quivers Qi with Fock–Goncharov coordinate structures (µrot)i, (µﬂip )i, and Mi.
Then for G, there is a quiver Q which also carries a Fock–Goncharov coordinate structure.
Proof. We must construct Q,µrot,µﬂip , M, then show that all requirements of Deﬁnition 4.16 are satis ﬁed.
This follows entirely from the fact that the Dynkin diagram o f the direct product of groups is the disjoint
union of Dynkin diagrams of the factors.
ForQ, take the disjoint union of each Qi, with each d∆ (Q) being the disjoint union of all d∆ (Qi). This
is triangular since each component is.
The mutations µrot and µﬂip are concatenations of all (µrot)i and (µﬂip )i respectively. The ordering of
these components are irrelevant, because quiver mutations at disconnected vertices commute and Q is exactly
a disjoint union. Any concatenation will operate component wise on the pieces of the disjoint union. This
satisﬁes Item 1.
By the aforementioned fact of Dynkin diagrams, Item 2 is also satisﬁed.
The map M is deﬁned as a product of each Mi in the following manner. Let αi and αj be any two
elements of the roots system for G associated to diﬀerent factors. Then the nodes correspondi ng to those
roots are disconnected in the Dynkin diagram for G, so the Aij = 0 in the Cartan matrix.
By e.g. [Kna96, Proposition 2.95], the bracket of any {ei,f i,h i } and {ej,f j,h j } vanishes, so any
{xi,y i,χ ∗
i } and {xj,y j,χ ∗
j } commute. Letting α = (g0N+,g 1N+,g 2N+,g 3N+), by suﬃcient genericity
we may factorize any gi as a product of xk,y k,χ ∗
k elements, and may therefore rearrange these factors so
that
gi = (gi)1(gi)2 · · · (gi)n, (gi)j ∈Gj.
Then the maps rot and Ψ ij trivially factor through the decomposition of α into
n∏
i=1
[
αi = ((g0)i, (g1)iN+, (g2)iN+, (g3)iN+)
]
.
That is, it is obvious that ∏
i rot(αi) = rot(∏
iαi). This, together with the construction of Q, shows that
Items 3 to 5 are satisﬁed since they are satisﬁed for each Gi. □
