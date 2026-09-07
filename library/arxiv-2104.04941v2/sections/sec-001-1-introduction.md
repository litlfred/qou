---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
1.1. Classical Teichmüller space 3
1.2. Cluster ensemble structures 4
1.3. Higher Teichmüller spaces 5
1.4. Results 6
1.5. Historical context 7
2. Ingredients 8
2.1. Root spaces and Weyl groups 8
2.2. Unipotent subgroups 9
2.3. Coxeter elements 9
2.4. Generalized minors 9
2.5. Factorization coordinates 11
2.6. Quivers 11
2.7. Cluster ensembles 12
3. Key identities 13
3.1. Actions of σG 13
3.2. Grid exchange relations 14
4. Coordinates on generically-decorated representations 15
4.1. Conﬁgurations and gluings 16
4.2. Triangular quivers and Fock–Goncharov coordinate str uctures 17
4.3. From coordinates to representations 21
4.4. Regarding 3-manifolds 23
5. Main Result: Fock–Goncharov coordinate structures for n on-An 23
5.1. Overview 23
5.2. Building the rectangle Q0 24
5.3. Construction of µrot 25
5.4. The A• edge 26
5.5. Construction of µﬂip 27
5.6. The map M 29
5.7. The signiﬁcance of the “twisting” mutations 31
6. Construction for An 32
E-mail address : sgilles@sgilles.net.
Date: 2021-03-24.
1
7. Proof of Theorem 4.19 for simple G 33
7.1. Overview 33
7.2. Ordering mutations 34
7.3. Rotation mutations 36
7.4. Flip mutations 40
8. Proof of Theorem 4.19 for semisimple G 43
9. Examples 44
9.1. A5 44
9.2. B3 45
9.3. D5 46
9.4. G2 47
9.5. E6 48
9.6. E7 50
9.7. E8 51
9.8. D2 =A1 ×A1 51
9.9. A3 ×C2 51
References 53
Acknowledgements
I owe thanks to far too many people to list them all by name. My p rofessors have shared their time and
expertise with me, my oﬃce-mates have put up with me for multi ple semesters, and my employers have given
me ﬂexibility to complete my research. I am grateful to them a ll.
My advisor, Professor Zickert, has provided me with expert g uidance and mentoring over the years. He
has helped me to achieve the goal for which I began my study, an d words cannot express my appreciation.
Finally, I would like to thank S. Kane, who taught me the meani ng of work, and whom I am unable to
repay.
Soli Deo Gloria.
1. Introduction
The program of Fock–Goncharov, starting with [FG06b], aims to describe representation spaces of hyper-
bolic surfaces into Lie groups by moduli spaces deﬁned by pol ynomial equations. These moduli spaces carry
a positive structure (see Deﬁnition 4.23), and in the case of the Lie group PSL2(R), the associated positive
spaces can be identiﬁed with Teichmüller space and decorate d Teichmüller space. For more complicated Lie
groups, these positive spaces give (decorated) higher Teic hmüller spaces.
Our result regards an additional structure, a cluster ensem ble structure (see Section 2.7), which allows
manipulating these moduli spaces eﬃciently via quivers.
(a) Cutting Σ into a fundamental domain.
· · ·
· · ·· · ·
· · ·
· · ·
· · · · · ·
· · ·
(b) Embedding a fundamental domain for Σ
into the disk model for hyperbolic space.
Figure 1. Putting a hyperbolic structure on Σ .
2
1.1. Classical T eichmüller space. We start by describing the Fock–Goncharov program for the ca se of
Lie groups of type A1. Let Σ be a surface that admits ideal triangulation, for example th e once-punctured
torus Σ = Σ 1,1. The Fock–Goncharov moduli spaces will describe (decorate d) Teichmüller space, so ﬁx a
hyperbolic structure on Σ . This can be described by an embedding of Σ ’s fundamental domain in H2, as in
Figure 1.
We now describe the two moduli spaces with seven key points.
1. The structure is determined by ideal points.
This follows from our ideal triangulation: all vertices are on∂H2, and all edges between them are unique
geodesics. See Figure 2 a.
(a) Two diﬀerent hyperbolic
structures on Σ .
g3B+
g2B+
g1B+ g0B+
d
(b) Deﬁning a representation
by B+-cosets.
g3N+
g2N+
g1N+ g0N+
λ 2,3
(c) Deﬁning a representation
by N+-cosets.
Figure 2. Representations of Σ by cosets.
2. We can identify ideal points with cosets of isometries in Isom+(H2) that ﬁx them.
The speciﬁc type of isometry determines which moduli space w e create.
• We can consider B+, a maximal borel subgroup, which ﬁxes a point on ∂H2. Thus diﬀerent cosets
gB+ ﬁx, and can be identiﬁed with, diﬀerent points on ∂H2. See Figure 2 b.
• Replacing points with horocycles, we can consider N+, a maximal unipotent subgroup, which ﬁxes
a horocycle in H2. See Figure 2 c.
3. Choosing an ordered triangulation attaches a non-degener ate ordered triple of cosets to
each triangle.
The non-degeneracy condition requires that the cosets be di stinct, so that the triangle has three well-
deﬁned edges. Describing how the coordinates of Fock–Gonch arov’s moduli spaces change under alternate
choices for the triangulation and the ordering is one of our p rimary concerns.
4. Coordinates can be assigned to each triple (or pair of triple s) of cosets.
• If we consider B+-cosets, then the coordinates we attach to each edge resembl e Thurston’s shear
coordinates (as described in e.g. [Bon96]) along that ident iﬁed edge, as the distance d in Figure 2 b.
Some of these coordinates need two triples to deﬁne. We will n ot focus on these in this introduction.
• If we consider N+-cosets, then the portion of each geodesic between horocycl es has ﬁnite length.
These are equivalent to Penner’s λ-lengths in his parametrization of decorated Teichmüller s pace of
[Pen87]. We associate to each triangle’s edge the λ-length of its truncated geodesic as a coordinate.
See Figure 2 c.
In our example, we label the edges a,b, and e as in Figure 3 a (identiﬁed edges necessarily have the same
λ-length). Using the (0 → 1, 1 → 2, 2 → 0)-ordering on a triangle’s edges, the coordinates we obtain a re
(a,b,e ) on the left and (e,a,b ) on the right.
5. We must describe how the coordinates change under (oriented ) reordering and retriangu-
lation.
In this A1 case, reordering has a trivial eﬀect on the coordinates. If w e rename g0, g1, g2, g3, but do not
change their values, we merely rearrange the coordinates fo llowing the new cyclic ordering on the triangle’s
edges. The coordinates deﬁned by Figure 3 b are (b,e,a ) on the left and (a,b,e ) on the right.
3
g3N+
g2N+
g1N+ g0N+
a
b
a
b
e
(a) Coordinate assignments
for one ordered triangulation.
g2N+
g1N+
g0N+ g3N+
a
b
a
b
e
(b) Figure 3 a under reorder-
ing.
g3N+
g2N+
g1N+ g0N+
a
b
a
b
f
(c) Figure 3 a under retrian-
gulation.
Figure 3. Coordinates by N+-cosets under reordering and retriangulation.
The retriangulation has a more interesting eﬀect, as shown i n Figure 3 c. The coordinates we obtain are
(b,a,f ) for the top and (a,f,b ) for the bottom, but we need to describe the relationship of th e new λ-length
f to the λ-lengths a, b, e. This is given by the classic Ptolemy’s Theorem regarding le ngths and diagonals
of circumscribed quadrilaterals. In Euclidean space this i s given by Figure 4 a, and in hyperbolic space by
Figure 4 b. For our example, taking identiﬁcations into account,
ef =a2 +b2.
a
b
c
d
e
f
(a) Ptolemy’s Theorem for lengths in Eu-
clidean space.
a
b
a
b
e
f
(b) Ptolemy’s Theorem for λ -lengths in hyper-
bolic space.
Figure 4. Ptolemy’s theorem: ac +bd =ef
6. Hyperbolic structures are those for which all coordinates a re positive.
The coordinates a,b,e,f with the relation ef =a2 +b2 describe an algebraic variety, but not every point
corresponds to a hyperbolic structure. Those which do are ex actly the points with positive coordinates, and
thus positive geodesic lengths. This positivity need only b e checked for one collection of coordinates: if a,b,
and e are all positive, then f will be as well.
7. The representation ρ :π1(Σ) →G can be reconstructed.
Via the coordinates we have mentioned, the holonomy ρ(γ) corresponding to this hyperbolic structure for
γ ∈π1(Σ) can be computed. See Section 4.3 for greater detail.
The moduli space we have described using N+-cosets is ASL2(R),Σ , and points with positive coordinates
correspond to points in Penner’s decorated Teichmüller spa ce for Σ . The moduli space derived from consid-
ering B+-cosets is XPGL2(R),Σ , and positive points correspond to points in Teichmüller sp ace for Σ .
