---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT"
section_id: sec-010-6-surfaces-with-boundary
section_title: "Surfaces with boundary"
section_number: 6
pages: 22-24
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
In this section we extend the deﬁnition of TV TQFT to surfaces with b oundary
(and 3-manifolds with corners). Recall that according to general ideas of extended
ﬁeld theory (see [Lur]), an extended 3d TQFT should assign to a close d 1-manifold
a 2-vector space, or an abelian category, and to a 2-cobordism be tween two 1-
manifolds, a functor between corresponding categories (which in t he special case of
cobordism between two empty 1-manifolds gives a functor Vec → Vec, i.e. a vector
space). In this section we show that the extension of the TV TQFT t o 1-manifolds
assigns to a circle S1 the categoryZ(C)—the Drinfeld center of the original spherical
category C. This result was proved by Turaev in the special case when the origin al
category C is ribbon (see [Tur1994]); the general case has remained a conject ure.
For technical reasons, it is more convenient to replace surfaces w ith boundaries
by surfaces with embedded disks. These two notions give equivalent theories: given
a surface with boundary, we can glue a disk to every boundary circle and get a
surface with embedded disks; conversely, given a surface with emb edded disks,
one can remove the disks to get a surface with boundary. Moreove r, in order to
accommodate real-life examples, we need to consider framing. This le ads to the
following deﬁnition.
We denote
D2 = [0, 1] × [0, 1]
and will call it the standard disk (it is, of course, a square, but this is what a disk
looks like in PL setting). We will also the marked point P0 on the boundary of D2
P0 = (0, 1) ∈∂D 2
Deﬁnition 6.1. A framed embedded disk D in a PL surface N is the image of a
PL map
ϕ : D2 →N
which is a homeomorphism with the image, together with the point P =ϕ (P0) ⊂
∂D .
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 23
An extended surface is a PL surface N together with a ﬁnite collection of disjoint
framed embedded disks (see Figure 22). We will denote the set of em bedded disks
byD(N ).
A coloring of an extended surface is a choice of an object Yα ∈ ObjZ(C) for
every embedded disk Dα .
Figure 22. Extended surface
Next, we can deﬁne cobordisms between such surfaces. As usual, such a cobor-
dism will be a 3-manifold with boundary together with some “tubes” ins ide which
connect the embedded disks on the boundary of M . The following gives a precise
deﬁnition in the PL category.
Deﬁnition 6.2. Let M be a PL 3-manifold with boundary.
An open embedded tubeT ⊂M is the image of a PL map
ϕ : [0, 1] ×D2 →M
which is satisﬁes the conditions below, together with the oriented ar cγ =ϕ ([0, 1] ×
{P0}) (which we will call the longitude).
The map ϕ should satisfy:
(1) ϕ is a homeomorphism onto its image
(2) T ∩∂M =ϕ ({0} ×D2) ∪ϕ ({1} ×D2)
We will call the disks B0 =ϕ ({0} ×D2) and B1 =ϕ ({1} ×D2) the bottom and
top disks of the tube.
A closed embedded tube T ⊂M is the image of a PL map
ϕ : S1 ×D2 →M
which is satisﬁes the conditions below, together with the oriented ar cγ =ϕ ([0, 1] ×
{P0}) (the longitude) and the disk B =ϕ ({0} ×D2) ⊂T .
The map ϕ should satisfy:
(1) ϕ is a homeomorphism onto its image
(2) T ∩∂M = ∅
The longitude γ determines the framing of the tube; the disk B is convenient for
technical reasons; later we will get rid of it.
Deﬁnition 6.3. An extended 3-manifold M is an oriented PL 3-manifold with
boundary together with a ﬁnite collection of disjoint framed tubes Ti ⊂ M . We
denote the set of tubes of M byT (M ).
A coloring of an extended 3-manifold M is a choice of an object Yα ∈ ObjZ(C)
for every tube Tα .
Note that if M is an extended 3-manifold, then its boundary ∂M has a natural
structure of an extended surface: the embedded disks are the b ottom and top disks
24 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
Figure 23. Extended 3-manifold
of the open tubes, and the marked points on the boundary of embe dded disks are
the endpoints of the longitude arcs γα , where α runs over the set of all open tubes
in M . Moreover, a coloring of M deﬁnes a coloring of ∂M : if an open tube Tα is
colored with Yα ∈ ObjZ(C), we color the embedded disk ϕ α ({1} × D2) with Yα
and the embedded disk ϕ α ({0} ×D2) with Y ∗
α .
Our main goal will be extending the TV invariants to such extended su rfaces
and cobordisms. Namely, we will
(1) Deﬁne, for every colored extended surface N , the spaceZT V (N, {Yα }) which
• functorially depends on colors Yα
• is functorial under homeomorphisms of extended surfaces
• has natural isomorphisms ZT V (N, {Y ∗
α }) = ZT V (N, {Yα })∗
• satisﬁes the gluing axiom for surfaces
(2) Deﬁne, for every colored extended 3-manifold M , a vector ZT V (M ) ∈
ZT V (∂M ) (or, equivalently, for any colored extended 3-cobordism M be-
tween colored extended surfacesN1,N 2, a linear mapZT V (M ) :ZT V (N1) →
ZT V (N2)) so that this satisﬁes the gluing axiom for extended 3-manifolds.
In the subsequent papers we will show that this extended theory a ctually coin-
cides with the Reshetikhin–Turaev theory for the modular categor yZ(C):
ZRT,Z (C) =ZT V, C.
The construction of the theory proceeds similar to the construct ion of TV invari-
ants. Namely, we will ﬁrst deﬁne ZT V (N ),ZT V (M ) for manifolds with a polytope
decomposition and then show that the so deﬁned objects are indep endent of the
choice of a polytope decomposition and thus deﬁne an invariant of ex tended mani-
folds.
