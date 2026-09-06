---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-038-93-incompressible-surfaces
section_title: "Incompressible surfaces"
section_number: 9.3
pages: 295-302
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
D D'
S S' S S'
D'
Figure 9.15. The discsD and D′ form a sphere which bounds a ball
sinceM is irreducible. We can use this ball to isotopeS′ away fromS.
we only remove a ball: hence we can replaceD0 withD1⊔D2. After ﬁnitely
many steps we getS∩S′ = ∅ and thereforeS∪S′ is a reducing set producing
the sameMi’s ofS andS′, up to balls. □
9.2.13. Projective planes. The previous discussions show how to deal
withspheresanddiscs, andwenowturntotheonlyremainingcompactsurface
withχ> 0: the projective plane. There is not much to say about it.
Proposition 9.2.34.The only compact irreducible orientable 3-manifoldM
containing RP2 is RP3.
Proof. The orientableM contains the orientable tubular neighbourhood
N = RP2×∼ I of RP2. The boundary∂N is the orientable coverS2 or RP2.
SinceM is irreducible, the sphere∂N bounds a ballB. ThereforeM is uniquely
determined as the manifold obtained by capping oﬀ the boundary sphere ofN.
The manifold RP3 is irreducible (because its coverS3 is) and contains
RP2, hence we must haveM = RP3. □
This proposition does not hold for non-orientable three-manifolds, which
might contain RP2 with a product neighbourhoodRP2×I. These cases are
diﬃcult to deal with, so one typically excludes thema prioriby requiring the
manifoldtobe RP2-irreducible, whichmeansthatitdoesnotcontaintwo-sided
projective planes.
9.3. Incompressible surfaces
Wehaveprovedthateverycompactoriented3-manifolddecomposesalong
essential spheres and discs, into some canonical pieces that do not contain
essential spheres or discs anymore.
We would like to pursue this strategy with the next simplest surfaces,
namely tori and annuli. To this purpose we deﬁne the important notion of
incompressible surface in a three-manifold, which applies to all surfaces of
non-positive Euler characteristic.
288 9. TOPOLOGY OF THREE-MANIFOLDS
D
S
D
S
∂M
S
D D'
D
S
D'
Figure 9.16. A surface S is incompressible (∂-incompressible) if the
existence of a discD as in the top-left (bottom-left) picture implies the
existenceofanotherdisc D′⊂S asinthetop-right(bottom-right)picture.
If in additionM is irreducible (∂-irreducible) the two discsD andD′ form a
sphere (disc) which bounds a ball (is∂-parallel), and hence by substituting
D′ withD we get two isotopic surfaces.
9.3.1. Incompressible surfaces. Throughout all this sectionM denotes
a compact orientable 3-manifold with (possibly empty) boundary. LetS⊂M
be a properly embedded orientable surface. Acompressing discforS is a disc
D⊂ M with ∂D = D∩S, such that∂D does not bound a disc inS. With
this hypothesis, the surgery in Figure 9.8 is called acompression: it transform
S into a new surfaceS′⊂M which is simpler thanS.
Proposition 9.3.1. The surfaceS′ may have one or two componentsS′
i,
andχ(S′
i )>χ (S) for each component.
Proof. We haveχ(S′) =χ(S) + 2. IfS′ has one component we are done,
so supposeS′ = S′
1⊔S′
2. Since ∂D did not bound a disc inS, noS′
i is a
sphere, henceχ(S′
i )⩽ 1 that impliesχ(S′
i )>χ (S) fori = 1, 2. □
A properly embedded connected orientable compact surfaceS⊂M with
χ(S)⩽ 0 is compressible if it has a compressing disc, andincompressible
otherwise. See Figure 9.16-(top).
Corollary 9.3.2.LetS⊂M be any properly embedded orientable surface.
After compressing it a ﬁnite number of times it transforms into a disjoint union
of spheres, discs, and incompressible surfaces.
Proof. We compressS as much as we can; after ﬁnitely many steps we
must stop because of Proposition 9.3.1. □
Remark9.3.3. Bydeﬁnition, anorientable3-manifoldis ∂-irreducibleifand
only if its boundary consists of incompressible components. (Strictly speak-
ing, a boundary component is not properly embedded and hence cannot be
incompressible: we implicitly push it inside the 3-manifold.)
9.3. INCOMPRESSIBLE SURFACES 289
D
B
T
D
B
T
Figure 9.17. A torus in an irreducible 3-manifold is either incompress-
ible, or it bounds a solid torus (left), or is contained in a ball (right).
A simple incompressibility criterion is the following.
Proposition 9.3.4. Let S⊂M be an orientable, connected, properly em-
bedded surface with χ(S) ⩽ 0. If the map π1(S) → π1(M) induced by
inclusion is injective, thenS is incompressible.
Proof. Suppose that a discD compresses S. Its boundary∂D is a non-
trivial element inπ1(S) because it does not bound a disc inS by Proposition
6.3.5, but is clearly trivial inπ1(M): a contradiction. □
The converse is also true, but its proof is much harder! We will complete
it at the end of this chapter. For the moment we content ourselves with the
following.
Proposition 9.3.5. If S⊂M is incompressible, every component of∂S is
non-trivial in∂M.
Proof. If a component of∂S is trivial in∂M, it bounds a discD⊂ ∂M
there. By taking an innermost one we getD∩S = ∂D, and by pushingD
insideM we ﬁnd a compressing disc forS. □
9.3.2. Tori. The ﬁrst closed surface to look at is the torus.
Proposition 9.3.6.LetT⊂M be a torus in an irreducible 3-manifold. One
of the following holds:
(1) T is incompressible,
(2) T bounds a solid torus,
(3) T is contained in a ball.
Proof. IfT is not incompressible, it compresses along a discD. The result
of the compression is necessarily a sphereS⊂M which bounds a ballB since
M is irreducible. If B is disjoint from T, then T bounds a solid torus as
in Fig.9.17-(left). If B contains T, then case (3) holds as shown in Figure
9.17-(right). □
290 9. TOPOLOGY OF THREE-MANIFOLDS
Figure 9.18. An annulusA in an irreducible and∂-irreducible 3-manifold
is either incompressible and∂-incompressible, or is parallel to an annulus in
∂M (left), or bounds a tube (centre), or is contained in a ball intersecting
∂M in a disc (right).
If M = S3 the case (3) can be excluded: ifT is contained in a ballB,
then it bounds a solid torus “on the outside” using the complementary ball
S3\B. We will also exclude the case (1) when we show thatS3 contains no
incompressible surfaces.
9.3.3. ∂-incompressible surfaces. There is of course also a∂-version of
incompressibility. LetS⊂M be a properly embedded orientable surface in a
3-manifoldM. A∂-compressing discforS is a discD with∂D =α∪β, where
α lies inS and β in ∂M as in Figure 9.9-(left); we also require that there is
no sub-discD′⊂S with∂D′ =α∪β′ andβ′⊂∂S. The move in Figure 9.9
is a∂-compression and transformsS into a surfaceS′⊂M simpler thanS:
Proposition 9.3.7. The surfaceS′ may have one or two componentsS′
i,
andχ(S′
i )>χ (S) for each component.
Proof. We haveχ(S′) =χ(S) + 1. IfS′ has one component we are done,
so supposeS′ =S′
1⊔S′
2. Sinceα did not bound a disc inS, noS′
i is a disc,
henceχ(S′
i )⩽ 0 that impliesχ(S′
i )>χ (S) fori = 1, 2. □
A properly embedded connected orientable compactS⊂M withχ(S)⩽ 0
is ∂-compressible if it has a∂-compressing disc, and∂-incompressible other-
wise. See Figure 9.16.
Corollary 9.3.8.LetS⊂M be any properly embedded orientable surface.
After ∂-compressing it a ﬁnite number of times it transforms into a disjoint
union of spheres, discs, and∂-incompressible surfaces.
9.3.4. Annuli. The ﬁrst non-closed surface to look at is the annulus. Let
a tube be the tubular neighbourhood of a properly embedded arc.
Proposition 9.3.9. Let A ⊂ M be a properly embedded annulus in an
irreducible and∂-irreducible 3-manifold. One of the following holds:
(1) A is incompressible and∂-incompressible,
9.3. INCOMPRESSIBLE SURFACES 291
(2) A bounds a tube,
(3) A is parallel to an annulus in∂M,
(4) A is contained in a ballB intersecting∂M in a disc.
Proof. IfA compresses along a discD, it transforms into two discs that
are parallel to two discsD1,D 2⊂∂M sinceM is∂-irreducible. IfD1∩D2 = ∅
thenAbounds a tube as in Figure 9.18-(right); ifD1⊂D2 thenAis contained
in a ballB intersecting∂M inD2.
IfA∂ -compresses along a discD, it transforms into a disc which is again
∂-parallel and henceA is as in Figure 9.18-(left) or bounds a tube. □
As a corollary, we get a simple criterion for detecting incompressible and
∂-incompressible annuli:
Corollary 9.3.10. Let A⊂M be a properly embedded annulus in an irre-
ducible and∂-irreducible 3-manifold. If the components of∂A are non-trivial
and non-parallel in∂M, the annulusA is incompressible and∂-incompressible.
9.3.5. Handlebodies. We study some examples. We investigate the in-
compressible and ∂-incompressible surfaces in the three-sphere and in the
handlebodies. Recall that a (∂)-incompressible surface is always compact,
orientable, connected, properly embedded, and with non-positive Euler char-
acteristic by hypothesis.
Proposition 9.3.11. There are no incompressible surfaces inR3.
Proof. LetS be a surface inR3. By applying as is the proof of Alexander
Theorem 9.2.10 we ﬁnd thatS transforms into spheres after surgerying along
discs. ThereforeS compresses somewhere. □
Ahighgenusclosedsurfacemaybeembeddedin R3 inarathercomplicated
way (which may be hard to imagine) and the proposition says that no matter
how intricate the surface is, there is always a compressing disc somewhere
that one can use to simplify the picture. After ﬁnitely many compressions the
complicated surface is atomised into some trivial spheres.
Corollary 9.3.12.There are no incompressible surfaces inS3.
Corollary 9.3.13.There are no incompressible surfaces in the ballB.
Proof. Use Proposition 9.3.5. □
Corollary 9.3.14.Every torus inS3 bounds a solid torus and every properly
embedded annulus inB bounds a tube.
Proof. Apply Propositions 9.3.6 and 9.3.9. Since the manifold isS3 orB,
the cases (3) or (4) easily imply (2). □
292 9. TOPOLOGY OF THREE-MANIFOLDS
The solid torus inS3 and the tube inB may of course be knotted! We now
turn to handlebodies. Recall that a handlebody of genusg≥ 1 is irreducible
by Corollary 9.2.20, but it is clearly not∂-irreducible.
Proposition 9.3.15 (Handlebodies).The genus-g handlebodyHg contains
no incompressible and∂-incompressible surfaces.
Proof. Suppose thatS⊂Hg is incompressible and∂-incompressible. Pick
disjoint essential discsD1,...,D g that cutHg into a ballB. PutS in trans-
verse position with respect to⊔iDi, so that the intersection ofS with⊔iDi
consists of circles and properly embedded arcs. SinceHg is irreducible and
S is incompressible and∂-incompressible, all these intersections can be re-
moved by an isotopy ofS, as explained below. Then Corollary 9.3.13 gives a
contradiction.
The intersections removal goes as follows. Letα be one arc or circle in
S∩Dj. SinceS is incompressible and∂-incompressible, there is a discD′⊂S
bounded byα (if α is a circle) or byα∪β with β⊂ ∂S (if α is an arc) as
in Figure 9.16. After substitutingα with an innermost intersection ofD′ with
⊔iDi we may suppose thatD′ is entirely contained inB and hence we may
eliminateα with an isotopy as explained in Figure 9.16. □
We can be more speciﬁc on the solid torusH1.
Proposition 9.3.16. Every incompressible surface in a solid torus is a∂-
parallel annulus.
Proof. Every incompressible surfaceS⊂H1 is ∂-compressible by Propo-
sition 9.3.15. If we∂-compress it, we get either a disc or an incompressible
surface again. ThereforeS is constructed iteratively from some discs by a se-
quence of moves opposite to the∂-compression, that produce incompressible
surfaces at each step. One easily sees that the only incompressible surface
that this move can produce at the ﬁrst step is a∂-parallel annulus (from a
single disc), and then one gets stuck. □
Warning 9.3.17. The handlebodyH2 contains many complicated properly
embedded incompressible surfaces! However, these are all ∂-compressible.
The main diﬀerence betweenH1 andH2 is thatπ1(H2) = Z∗ Z is a free group
of rank two and contains many free groups of arbitrarily high rank, so there
is a lot of space forπ1-injective incompressible surfaces inH2 with boundary
(whose fundamental group is free).
9.3.6. Line bundles. We now turn to product line bundles. Recall that
Sg is the closed orientable surface of genusg.
Proposition 9.3.18 (Line bundles).Fix g> 1. The product M = Sg×
[−1, 1]isirreducibleand ∂-irreducible. Theincompressibleand ∂-incompressible
surfaces inM are precisely the following (up to isotopy):
9.3. INCOMPRESSIBLE SURFACES 293
D
e
S
e
S
Figure 9.19. A move that decreases the intersection number ofS with
the vertical edges (left). The surfaceS intersects every prism into hori-
zontal triangles (centre) or vertical rectangles (right).
• the horizontal surfaceSg× 0,
• a vertical annulusγ× [−1, 1] for each non-trivial simple closed curve
γ⊂Sg.
Proof. We know thatM is irreducible by Proposition 9.2.21. The horizon-
tal surface and the vertical annuli are both incompressible and∂-incompressible
by Propositions 9.3.4 and 9.3.10. Propositions 9.3.4 also shows thatM is∂-
irreducible.
We now prove that every incompressible and∂-incompressibleS is either
vertical or horizontal, up to isotopy. We use a version of normal surface theory,
with prisms instead of tetrahedra.
A triangulation ∆ of Sg determines a decomposition ofSg× [−1, 1] into
prisms. Every vertex v of ∆ gives rise to a vertical edgee = v× [−1, 1].
We suppose thatS is transverse to the prisms and has minimum intersection
number with the vertical edges. The intersection ofS with a vertical rectan-
gular face consists of arcs and circles. The simpliﬁcation argument described
below shows that after an isotopy we get only horizontal or vertical arcs (that
is, arcs joining opposite sides of the rectangle). By further isotopies we can
also supppose thatS intersects every horizontal triangle of the prism into arcs
joining distinct sides. ThereforeS intersects necessarily every prism into ei-
ther horizontal triangles or vertical rectangles as in Figure 9.19-(centre) and
(right). These pieces glue up to give a horizontal or vertical surface.
Here is the simpliﬁcation argument. There cannot be arcs with endpoints
in two consecutive edges, because they could be removed by an isotopy as in
Figure 9.19-(left) contradicting minimality. Analogously there are no arcs with
bothendpointsinthesameverticaledge. Circlesandarcswithendpointsinthe
same horizontal edge are removed as in the proof of Proposition 9.3.15.□
294 9. TOPOLOGY OF THREE-MANIFOLDS
