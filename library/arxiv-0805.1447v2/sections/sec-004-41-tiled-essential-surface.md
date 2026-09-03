---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-004-41-tiled-essential-surface
section_title: "Tiled essential surface"
section_number: 4.1
pages: 10-12
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
Assume F is tiled. Since F is tiled, every singular point is bb-singularity,
and F can be decomposed into bb-tiles. A decomposition into bb-tiles
determines cellular-decomposition of F , and we call this tiling. The
notion of vertex and valance we deﬁned in section 3 coincides to usua l
deﬁnition of vertex and valance in this cellular decomposition.
First we estimate a valance of each vertex, using Euler characteris tic
argument which is standard in braid foliation theory.
Lemma 1 (Euler characteristic formula, Tiled case) . Let β be a braid
and F be a tiled essential genus g closed surface in the complement of
closed braid ˆβ , and V (i) be a number of vertex whose valance is i. then,
3∑
v=1
(4 − v)V (v) + 8g − 8 =
∞∑
v=4
(v − 4)V (v)
holds.
Proof. Let E, R be a number of 1-cell and 2-cell of tiling. Since F has an
Euler characteristic −2g+2, ( ∑ ∞
i=1 Vi)−E +R = −2g+2. On the other
hand, each 1-cell is the boundary of exactly two 2-cells and each 1- cell
has two vertices as their boundary ,so 2 R = E and ( ∑ ∞
i=1 iVi) = 2 E.
By combining these equation, we establish the claim.
□
Since each term of equation in lemma 1 is positive, lemma 1 implies
V (i) are bounded except V (4). Next we see that Dehornor ﬂoor can
be estimated from above by a valance of vertex.
Lemma 2. Let F be a tiled essential genus g closed surface in the
complement of closed braid L = ˆβ . If F contains a valance v vertex,
then [β ]D < v
2 + 1.
Proof. Let p be a valance v vertex and {Hθ1, H θ2, · · · , H θv| θi < θ i+1}
be a sequence of singular ﬁbers such that each Hθi contains singular
leaves which pass the vertex p. Let bθ be a b-arc in the ﬁber Hθ which
passes v. By taking isotopy near each singular ﬁber Hθi, we can always
assume that for suﬃciently small ε > 0, braiding of strands does not
occur in the interval [ θi − ε, θ i + ε] and each ﬁber Hθi±ε is pierced by L
exactly the same points {p1, p 2, · · · , p n}. Notice that this modiﬁcation
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 11
can be done without changing H0 ∩ ˆβ so this modiﬁcation does not
change braid β as a element of braid groups. After this modiﬁcation,
we can always consider sub-braiding in each interval [ θi − ε, θ i + ε],
[θi + ε, θ i+1 − ε]. Since ε is chosen to suﬃciently small, we can assume
there exist no other singular points in each interval [ θi − ε, θ i + ε].
Now we see a sequence of bθ as a move of b-arc in D2. Then we
can also assume by taking isotopy of surface and braids, in the inter val
[θi + ε, θ i+1 − ε], bθ do not move when we see bθ as a move of the arcs.
First we investigate a sub-braiding β1 in [ θ1 + ε, θ 3 − ε]. By taking
appropriate conjugacy of β1, we can assume F ∩Hθ1+ε consists of several
number of vertical arcs as depicted in left of ﬁgure 5 and bb-singula rity
in θ2 is modeled as shown in the right of ﬁgure 5. We denote this braid
by β ′
1
Then, by seeing braids as a move of puncture point of disc, we can
write this modiﬁed braiding β ′
1 in [ θ1 + ε, θ 3 − ε] as shown in ﬁgure
6, which contains only one σ1, σ −1
1 . The original braiding β1 in [ θ1 +
ε, θ 3 − ε] is conjugate to the braid β ′
1 so proposition 3 shows [ β1]D = 0.
/C8/CB/CU/D6/CP/CV /D6/CT/D4/D0/CP
/CT/D1/CT/D2 /D8/D7
/A1 /A1 /A1/A1 /A1 /A1/A1 /A1 /A1/A1 /A1 /A1
/A1 /A1 /A1
Figure 5. Model of intersection and bb-singularity
Iterating this argument, we conclude that sub-braid βi in the interval
[θ2i−1 + ε, θ 2i+1 − ε] for i = 1 , · · · , v
2 has zero Dehornoy ﬂoor. Since
original braid β is conjugate to the braid β1β2 · · · βv/ 2, by proposition
2, [ β ]D < v
2 . □
Combining above two lemmas, now it is easy to estimate Dehornor
ﬂoor via information of tiling.
Proof of Theorem 1(1). Assume F is tiled. Let V (i) be the number of
valance i vertices. If some of V (i) is non-zero for i ≤ 3, then lemma 2
means [β ]D < 2 < g + 1, so conclusion holds. Therefore we can assume
12 TETSUYA ITO
/C8/CB/CU/D6/CP/CV /D6/CT/D4/D0/CP
/CT/D1/CT/D2 /D8/D7
/AI
/BD
/B7 Ꜽ
/AI
/BE
/AI
/BF
/A0 Ꜽ
Figure 6. Braiding in [ θ1 + ε, θ 3 − ε]: bb-singularity case
V (i) = 0 for i ≤ 3, and Euler characteristic formula in lemma 1 become
8g − 8 =
∞∑
v=4
(v − 4)V (v)
Since g is not zero, there exist at least two b-arcs in each regular
ﬁber, so at least four vertices in the tiling of F . Therefore the minimal
valance of vertices is smaller than max{2g + 2, 4}, that is, 2 g + 2. Then
lemma 2 establishes [ β ]D < g + 2. □
