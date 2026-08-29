---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-026-state-sums-with-defect-discs
section_title: "State sums with defect discs"
section_number: null
pages: 44-48
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
To prove the triangulation independence of the state sum, we first show that the state sums of 3-ballsM that
shell to fine neighbourhoods of defect discsD are given as cyclic evaluations of certain polygon diagrams.
These polygon diagrams are obtained by projecting the dual graphs of the boundary triangulations on∂M to
the defect disc. AsM is PL homeomorphic to[0, 1]×D via an orientation preserving PL homeomorphism
ϕ : M→ [0, 1]×D by Lemma 5.8, this projection is given by Definition 5.9. Lemma 5.10 ensures that
different choices ofϕ yield graphs onD that are related by isotopies.
Proposition 5.11. LetM be a 3-manifold with defect data that shells to a fine neighbourhood of a defect disc
D by shellings with tetrahedra that do not intersectD. Then for all labelingsl∂M, b∂M as in Definition 4.7
Z′(M,l∂M,b∂M ) = ev(P ),
where ev(P ) is the cyclic evaluation of the polygon diagramP obtained by
• projecting the dual graph of the boundary triangulation on∂M to D,
• labeling the edges and vertices of the resulting diagram with the data assigned byl∂M and b∂M.
Proof. 1. We first suppose thatM is a fine neighbourhood of the defect discD and prove the claim by
induction over the number of tetrahedra in the triangulation. For a single tetrahedron, this holds by definition
of the generalised 6j symbol, see Figure 3, and of the rescaled state sum.
Any fine neighbourhoodM of D with n + 1 tetrahedra is obtained by gluing a single tetrahedront to a
fine neighbourhoodM′ of D with n tetrahedra. This follows, because the triangulation ofM defines a cell
complex structure onD and every cell decomposition of a disc is shellable, see for instance Sanderson [Sa57,
Lemma 1]. Shellings of the defect disc correspond to 3d shellings of its fine neighbourhoodM.
44
The tetrahedront can be glued toM′ either along one or two faces. Gluing along three faces is not possible,
as t intersectsD either in three edges incident at a common vertex as in Figure 2 (a) or in all except two
opposite edges as in Figure 2 (b). The first case would yield a contradiction to the assumption that the defect
surfaces inM and M′ are both discs. In the second case there would be an internal edge inM common to
two glued faces that does not intersectD, contradicting thatM is a fine neighbourhood ofD.
By Corollary 4.10, formula (83) and the induction hypothesis, the rescaled state sum forM is
Z′(M,l∂M,b∂M ) =
∑
l
∑
bg
∏
e∈Eg
diml(e)ev(P′) 6j(t,l,b ), (88)
where
• ev(P′) denotes the cyclic evaluation of the corresponding polygon diagram forM′,
• Eg is the set of internal edges inM that correspond to boundary edges oft and M′,
• the sumΣl runs over all labelings of edges inEg with simple objects in the chosen sets of representatives,
• the sum Σbg runs over bases of the morphism spaces for glued faces oft and M′.
We compute the sum in (88) depending on the number of glued faces oft:
(i) Ift is glued toM′ along a single facef, thenEg =∅. Identity(66) implies that the sum in(88) is given by
Z′(M,l∂M,b∂M ) =
∑
bf
ev(P′) 6j(t,l,b )
(66)
= ev( P ).
(ii) Ift is glued toM′ along two facesf,f′ that share an edgee, thenEg ={e} ande intersectsD. Otherwise,
t would have to intersectD in four edges, as in Figure 2 (b). As the intersections of the defect disc int with
f and f′ are both glued to the boundary of the defect disc inM′, the defect surfaceD could not be a disc.
We apply identity(66) to gluet on M′ along f. This yields a polygon diagramP′′ with the morphisms for
f′ assigned to adjacent sides ofP′′ that are separated by a vertex labeledl(e). Identity(67) implies that the
state sum in (88) is given by
Z′(M,l∂M,b∂M ) =
∑
l(e)
∑
bf,bf′
diml(e) ev(P′) 6j(t,l,b )
(66)
=
∑
l(e)
∑
bf′
diml(e)ev(P′′)
(67)
= ev( P ).
This proves the claim for the case whereM is a fine neighbourhood of the defect disc.
2. Suppose now thatM is obtained from a fine neighbourhood of the defect disc by inverse shellings with
tetrahedra that do not intersectD. We prove the claim by induction over the numbern of tetrahedra in the
triangulation that do not intersectD. Ifn = 0 the claim holds by 1.
If M containsn + 1 tetrahedra that do not intersectD, thenM is obtained by gluing a tetrahedront that
does not intersectD to a defect 3-manifoldM′ with n tetrahedra that do not intersectD and also satisfies
the assumptions. Ift is contained in a region labeled by a spherical fusion categoryC, then by Corollary 4.10
and the induction hypothesis, the rescaled state sum forM is given by
Z′(M,l∂M,b∂M ) =
∑
l
∑
bg
∏
e∈Eg diml(e)
dimCvg
ev(P′) 6j(t,l,b ), (89)
where the notation is as in(88) and vg∈{ 0, 1} is the number of internal vertices inM that correspond to
boundary vertices oft and M′. We compute the sum in (89) depending on the number of glued faces oft:
(i) Ift is glued toM′ along a single facef, thenEg =∅ and vg = 0. Identity(69) then implies that the state
sum in (89) is given by
Z′(M,l∂M,b∂M ) =
∑
bf
ev(P′) 6j(t,l,b )
(69)
= ev( P ).
(ii) Ift is glued toM′ along two facesf,f′ that share an edgee, thenEg ={e} and vg = 0. We use identity
(69) to insert the 6j symbol fort into the diagramP′. This yields a polygon diagramP′′ with the morphisms
for f′ assigned to vertices in the interior that are connected by an edge labeledl(e). Applying the second
identity in (60) then yields
Z′(M,l∂M,b∂M ) =
∑
l(e)
∑
bf,bf′
diml(e) ev(P′) 6j(t,l,b )
(69)
=
∑
l(e)
∑
bf′
diml(e)ev(P′′)
(60)
= ev( P ).
45
(iii) Ift is glued toM′ along three facesf,f′,f′′, then they share three edgese =f∩f′, e′ =f∩f′′ and
e′′ =f′∩f′′, and there is exactly one vertexv in t that becomes internal after the gluing. Thus we have
Eg ={e,e′,e′′} and vg = 1. We first gluet to M′ along f with identity(69). This eliminates the summation
over bf in (89) and yields a polygonP′′ with the morphisms forf′ assigned to adjacent vertices in the
interior that are connected by an edge labeledl(e). Applying the second identity in(60) then eliminates the
summation overl(e) and bf′ and the factordiml(e) in (89), as in (ii). This yields a polygon diagramP′′′
that differs fromP only in a disc in its interior, where one has
P′′′
i
l(e′) l(e′′)
i
γ
γ
P
i
(90)
withγ∈ Hom(f′′)andi∈IC labelingtheremainingedgeof f′′. Multiplying ev(P′′′)by diml(e′) diml(e′′) dimC−1
and summing overl(e′),l (e′′)∈IC and overγ∈ Hom(f′′) then yields
Z′(M,l∂M,b∂M ) = dimC−1 ∑
γ,l(e′),l(e′′)
diml(e′) diml(e′′)ev(P′′′)
(65)
= ev( P ).
Note that the evaluation of the diagram obtained by projecting the dual of the boundary triangulation onM to
the defect surfaceD does not depend on the choice of the underlying PL homeomorphismϕ :M→ [0, 1]×D.
By Lemma 5.10 different choices ofϕ yield isotopic projection maps. Diagrams for spherical fusion categories
that are related by PL isotopies have the same evaluation. This is well-known and can be viewed as a
special case of [JS91, Th. 1.12], [BMS12, Th. 2.12] for 2-category diagrams and [BMS12, Th. 3.9] for planar
2-category diagrams, see also the paragraphs after Example 2.1 and Definition 2.2. Together with identities
(39) to (43) this ensures that the evaluation of the resulting diagram is independent ofϕ.
As the evaluation of the polygon diagram in Proposition 5.11 depends only on the triangulation and labeling
of ∂M and on the defect data, we obtain
Corollary 5.12. Let M,M′ be triangulated 3-manifolds with defect data that satisfy the assumptions of
Proposition 5.11 and whose boundary triangulations coincide. Then for all labelingsl∂M of the boundary one
hasZ(M,l∂M ) =Z(M′,l∂M ).
In particular, this implies that the state sum of any generic transversal triangulated 3-manifold with defect
data is invariant under generic transversal bistellar moves. This follows with Corollary 4.10, as the tetrahedra
in such moves define triangulations of a 3-ball that satisfy the assumptions of Proposition 5.11 and agree on
its boundary.
Corollary 5.13. Let M be a generic and transversal triangulated 3-manifold with defect data andl∂M
a labeling of its boundary. Then the state sumZ(M,l∂M ) from Definition 4.7 is invariant under generic
transversal bistellar moves in the interior ofM.
All generic transversal bistellar moves for tetrahedra with defect surfaces are shown in Figure 8. The moves for
tetrahedra that also involve defect lines and defect vertices are analogous, but with the additional conditions
that defect vertices must not lie on faces and defect edges must not intersect edges of the tetrahedra.
The bistellar invariance of state sums for 3-manifolds with defect surfaces has a similar interpretation to the
one for Turaev-Viro-Barrett-Westbury state sums outlined at the end of Section 5.1. The moves in Figure 8
(c) to (f) encode the pentagon relation(6) for the structure isomorphismsci,j,m : (i⊗j)▷m→i▷ (j▷m)
for aC-module category and equivalent relations obtained from it by taking inverses. The moves in
Figure 8 (g) to (i) encode the pentagon relation(10) and the invertibility of the structure isomorphisms
bc,m,d : (c▷m)◁d→c▷ (m◁d) in a (C,D)-bimodule category. The corresponding moves for surfaces with
line and point defects combine these pentagon relations with the pentagon relations(13), (15) forC-module
andD-right module functors and the hexagon relation (17) for(C,D)-bimodule functors.
46
(c)
(e)
(g)
(h) (i)
(f)
(d)
(a)
 (b)
Figure 8: bistellar moves for tetrahedra without and with defect discs:
(a),(b): encoding the associator of a spherical fusion categoryC,
(c)-(f): encoding the natural isomorphismc for aC-module categoryM,
(g)-(i): encoding the natural isomorphismb for a (C,D)-bimodule categoryM.
47
As for a spherical fusion category, the bistellar invariance for manifolds with defects can be formulated as
generalised Biedenharn-Elliott and orthogonality relations for 6j symbols, which generalise the diagrammatic
identities (86) and (87). However, it becomes cumbersome to list all of these relations.
