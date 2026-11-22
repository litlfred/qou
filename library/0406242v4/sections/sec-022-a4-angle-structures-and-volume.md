---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-022-a4-angle-structures-and-volume
section_title: "A.4 Angle structures and volume"
section_number: null
pages: 36-37
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Angle structures and volume
Following Section 5 of the main article, we will parameterize the dihedral angles of
the tetrahedra by pleating angles on the pleated 4–punctured spheres. Each sphere Si
described above has a natural transverse orientation that points (equivalently) toward
the inside of the link projection, toward increasing indices, and upward in Figure 18.
Just as in Section 5, for any edge e ⊂Si, we can deﬁne the pleating angle α to be the
(signed) external angle at e, with signs chosen so that α is positive whenever the angle
above e is less than π.
On the pleated sphere Si+1 living between ∆i and ∆i+1, this deﬁnition will give
pleating angles
−2wi,
2wi+1
and
2wi −2wi+1,
exactly as in (2). The clasp surface S1, which borders ∆1 on one side and is folded on
the other side, will have pleating angles −π, 2w1, and π −2w1, where the pleating
angle of −π corresponds to the hairpin turn in Figure 19. Thus, if we deﬁne w0 = π/2
(even though there is no tetrahedron layer ∆0), the pleating angles on S1 will be given
by the same expressions as above. Similarly, setting wc = π/2 allows us to label the
pleating angles on Sc by the same expressions as in (2).
Lemma A.2 For i = 0, . . . , c, choose a parameter wi, such that w0 = wc = π/2 and
w1, . . . , wc−1 satisfy the range, concavity, and hinge conditions (3). For each such
choice of parameters, set the dihedral angles of the tetrahedra as in Figure 5. Then
(1) for each ∆i, the angles xi, yi, zi are positive and add up to π,
(2) the dihedral angles around each edge add up to 2π, and
(3) for each Si, the pleating angles add up to 0.
Geometry & Topology 10 (2006)
Canonical triangulations
1275
Proof The range, concavity, and hinge conditions imply that all the tetrahedron angles
xi, yi, zi are positive, and the claim that their sum is π is immediate from Figure 5. For
each pleated surface Si, the pleating angles sum to 0 by construction. Therefore, it
remains to check the angle sum around each edge e of S3∖K.
If e is not the core of S1 or Sc, the combinatorial picture of Figure 18 is the same as
the one for torus bundles. Thus, as in Section 5, each layer ∆i contributes precisely
the difference between the pleating angles of the neighboring surfaces, and the sum
around e simpliﬁes to 2π. If e is the core of a clasp, say the core of S1, the left panel
of Figure 19 shows that four sectors contribute dihedral angles at e: two sectors that
have angle z1, plus two fans of angles above pleated surface S1, each having dihedral
angle 2w1. Thus, because z1 + 2w1 = π, the total angle sum at e is 2π.
By Lemma A.2, our triangulation will have an angle structure whenever we set
w0 = wc = π/2 and interpolate between these parameters in a way that satisﬁes the
range, concavity, and hinge conditions. One can always do this graphically, by ﬁrst
ﬁxing wi for the hinge indices and then connecting the hinges by pieces of parabolas,
as in Figure 6 (this is where we use the hypothesis that Ωcontains at least one hinge).
Lemma A.3 Let P be the open afﬁne polyhedron of angle structures for the triangu-
lation of S3∖K, parameterized by sequences ( π
2 , w1, . . . , wc−1, π
2 ), as in Lemma A.2.
Then a point of P is a critical point of the volume functional V if and only if the
corresponding tetrahedron shapes give a complete hyperbolic structure on S3∖K.
Just like Lemma 6.2, this is an instance of a much more general theorem of Rivin, Chan,
and Hodgson [9, 22]. It is also possible to prove Lemma A.3 directly, using the same
line of argument as in Lemma 6.2, although in the setting of two-bridge links this would
require considering a number of special cases.
