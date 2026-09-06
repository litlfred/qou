---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-051-123-flat-three-manifolds
section_title: "Flat three-manifolds"
section_number: 12.3
pages: 388-391
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We now turn to ﬂat three-manifolds. In dimension two, every orientation-
preserving isometry of R2 is a translation, and this easily implies that every
ﬂat orientable closed surface is a torus. In dimension three we also have
rototranslations, which produce more orientable manifolds.
12.3. FLAT THREE-MANIFOLDS 381
We now classify all the closed ﬂat orientable three-manifolds up to diﬀeo-
morphism and prove the following.
Theorem 12.3.1.A closed orientable 3-manifoldM admits a ﬂat metric if
and only if it is a Seifert manifold withe =χ = 0.
There are six such manifolds, listed in Table 10.3.
12.3.1. Classiﬁcation.Every closed ﬂat 3-manifold is isometric toR3/Γ
for some crystallographic groupΓ< Isom(R3) acting freely, see Section 4.4.4.
Exercise 12.3.2. Every element inΓ is either a translation or a rototrans-
lation (deﬁned in Example 4.4.7).
We prove one half of Theorem 12.3.1.
Proposition 12.3.3. Every closed orientable ﬂat 3-manifold is a Seifert
manifold withe =χ = 0.
Proof. We haveM = R3/Γ. Recall the exact sequence
0−→H−→Γ−→r (Γ)−→0
whereH◁ Γ is the translation subgroup andr (Γ)<SO (3) is ﬁnite by Proposi-
tion 4.4.9. We now prove thatΓ preserves a foliation ofR3 into parallel lines
that projects to a Seifert structure onM.
If r (Γ) is trivial, thenΓ = H consists of translations and preserves many
foliations into parallel lines that project to a Seifert structure on the quotient
3-torusM. Ifr (Γ) is non-trivial, it is isomorphic toCn,D2m,T12,O24, orI60.
Ifr (Γ) =Cn orD2m, it has a common ﬁxed vector linel⊂ R3 and Γ preserves
the foliation of lines parallel tol.
Ifr (Γ) =T12,O 24, orI60 we obtain a contradiction as follows. In all cases
we haveT12⊂r (Γ). The groupT12 consists of the identity, theπ-rotations
along the three coordinate axis, and the± 2π
3 -rotations along the axis spanned
by (1, 1, 1), (1,−1,−1), (−1, 1,−1), and (1,−1,−1).
Pick a rototranslationh∈ Γ with axis l parallel to (1, 1, 1), and up to
conjugating Γ by a translation we may suppose thatl contains the origin
0∈ R3. We haveh(0) = (d,d,d ) for somed⁄= 0. Since h3 is a translation
we get (3d, 3d, 3d)∈H.
The groupΓand henceT12 acts onH via conjugation. ThereforeH isT12-
symmetric and (3d,−3d,−3d)∈H using theπ-rotation along the ﬁrst axis.
Hencet = (6d, 0, 0) = (3d, 3d, 3d) + (3d,−3d,−3d)∈H. The composition
t◦h2 has a ﬁxed point, because it sends0 to (2d, 2d, 2d)− (6d, 0, 0) =
(−4d, 2d, 2d) which is orthogonal tol: a contradiction.
In all casesM has a Seifert structure. By Bieberbach’s Theorem (stated
as Corollary 4.4.11) the manifoldM is ﬁnitely covered by the 3-torus, and
henceχ =e = 0 by Proposition 10.3.26. □
382 12. THE EIGHT GEOMETRIES
L
L
P
P
P
P
PP
P
P P
P
F
F
Figure 12.2. The six closed orientable ﬂat 3-manifolds, up to diﬀeo-
morphism. Each is constructed by pairing isometrically the faces of a
polyhedron in R3 according to the labels. When a face has no label, it
is simply paired to its opposite by a translation. The polyhedra shown
here are three cubes, two prisms with regular hexagonal basis, and one
parallelepiped made of two cubes.
We now prove the other half.
Proposition 12.3.4. Every closed Seifert manifold M with e = χ = 0
admits a ﬂat metric.
Proof. There are six such Seifert manifolds up to diﬀeomorphism, listed
in Table 10.3. We build a ﬂat metric for each in Figure 12.2.
Theﬁgureshowssixﬂatmanifolds, constructedbyidentifyingisometrically
the faces of a polyhedron inR3. The reader is invited to check that each
construction gives indeed a ﬂat manifold, by verifying that the ﬂat metric
extends to the edges and to the vertices.
In all cases the foliation by parallel horizontal lines (orthogonal to theP
faces) descends to a Seifert ﬁbration on the ﬂat manifold. By looking at these
lines one checks that the base surface of the ﬁbration is respectively
T, (S2, 2, 2, 2, 2), (S2, 2, 4, 4), (S2, 2, 3, 6), (S2, 3, 3, 3), (RP2, 2, 2).
These orbifolds are obtained respectively from the ﬁgures by considering: the
square torus, its quotient via aπ-rotation, via aπ
4-rotation, the quotient of a
hexagon torus by aπ
3-rotation, by a 2π
3 -rotation, and the quotient of a Klein
bottle via aπ-rotation.
These ﬂat Seifert manifolds havee = 0 by Proposition 12.3.3, and hence
they are precisely those listed in Table 10.3. □
