---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT"
section_id: sec-005-14-deformation-variety
section_title: "Deformation variety"
section_number: 1.4
pages: 6-8
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
doc_brief: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
DecX(Γ, PGL(2, C))
by deﬁning the deformation variety with the gluing equations. We use in
this paper an analog og this space for the group PGL(3 , C). From now on,
we will always assume thatn = 3. This space is deﬁned by further assuming
thatM is ideally triangulated: M is homeomorphic to a gluing of tetrahedra
with vertices removed as in [22, 2] So let T = (T1,T 2,...,T ν) be an ideal
triangulation of M.
We now recall coordinates on these spaces as deﬁned in [1] (see Figure 1).
For each of these (oriented) tetrahedra, one consider a set of 16 coordinates:
one on each half-edge and one in the center of this face. If the vertices of the
tetrahedron T are (ijkl), one has twelve coordinates on half edges, denoted
byzij(T ), zik(T )... and four on faces, denoted by zijk(T ).
As described in [1], these coordinates are subject to two diﬀerent kinds
of consistency relations:
• Internal relations: for a tetrahedron T = (ijkl) we have around each
vertex zij(T )zik(T )zil(T ) =−1 and zik(T ) = 1
1−zij(T ); and for each
face zijk(T ) =−zil(T )zkl(T )zjl(T ).
• Gluing relations: ﬁrst, given two adjacent tetrahedra Tµ, Tµ′ of T
with a common face (ijk) then
(1) zijk(Tµ)zikj(Tµ′) = 1.
second given a sequence T1,...,T µ of tetrahedra sharing a common
edge ij and such that ij is an inner edge of the sub-complex com-
posed by T1∪···∪ Tµ then
(2) zij(T1)··· zij(Tµ) =zji(T1)··· zji(Tµ) = 1.
7
i
j k
l
zij
zil
zik
zijk
zilj zikl
Figure 1. Coordinates for a tetrahedron of ﬂags
GivenM and a triangulationT withn tetrahedra, we consider the space
of solutions of these equations and denote it by
Defor(M,T )⊂ C16n.
We call it the deformation variety of a triangulation.
Up to combinatoric choices, the holonomy map associates to each point
in Defor(M,T ) a decorated representation into PGL(3 , C) as in [1, section
5]:
Defor(M,T )→ DecHom(π1(M), PGL(3, C)).
Moreover this map is algebraic 3 and a diﬀerent initial choice gives a conju-
gated decorated representation.
So this gives two well deﬁned maps, landing in DecMon or Dec X, both
called holonomy maps and denoted by Hol. Note that the second one is
algebraic:
Hol : Defor( M,T )→ DecMon(π1(M), PGL(3, C)),
and
Hol : Defor( M,T )→ DecX(π1(M), PGL(3, C)),
We extend the peripheral holonomy map deﬁned in the previous section in
a natural way:
Holperiph : Defor(M,T )→ DecX(π1(T ), PGL(3, C))≃ (C∗)4
Let us comment a bit on the properties of both the holonomy maps Hol:
the ﬁrst map is injective but not surjective, as some representation are not
detected by a given triangulation. Moreover, if you forget the decoration, the
maps are not any more injective : there is a (generically) ﬁnite choice for a
3indeed, by construction, the expression of the matrix entries are algebraic.
8 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
decoration of a given representation. All this can be seen already in the case
of representations into PGL(2, C). In particular the identity representation
can be obtained by gluing two tetrahedra to obtain the sphereS3 minus four
points and the solutions to the hyperbolic equations has a curve such that
the associated representations are trivial [20]. Also, in the tables obtained
in [2] the 1-dimensional components give conjugated representations with
