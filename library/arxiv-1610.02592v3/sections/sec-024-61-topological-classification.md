---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-024-61-topological-classification
section_title: "Topological classification"
section_number: 6.1
pages: 163-165
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Figure 6.2. The 0-handle andk 1-handles form a subsurfaceS′⊂ S
with connected boundary, to which the 2-handle is attached (left). A 0-
handle and two linked 1-handles (centre). If we attach a 2-handle to the
centre ﬁgure we get a handle decomposition of the torus (right).
Theorem 6.1.6 (Classiﬁcation of surfaces).Every closed, connected, ori-
entable surface is diﬀeomorphic toSg for someg> 0.
Proof. Being a closed manifold, every closed orientable surfaceS has a
handle decomposition. By Proposition 1.7.13 it has one with one 0-handle, a
certain numberk of 1-handles, and one 2-handle. We getχ(S) = 2−k. We
prove by induction onk thatk = 2g is even andS is diﬀeomorphic toSg.
Ifk = 0 thenS is obtained by gluing two discs (the 0- and 2-handle) and
is hence a sphere by Corollary 6.1.3.
Suppose k >0. The 0-handle is a disc and the 1-handles are rectangles
attached to its boundary as in Figure 6.2-(left). Note that sinceS is orientable
every rectangle is attached without a twist, otherwise it would create a Möbius
strip. The 0- and 1-handles altogether form a compact surfaceS′⊂S with
only one boundary component, to which the 2-handle is attached.
Since ∂S′ is connected, every rectangle is linked to some other rectangle
as in Figure 6.2-(centre). A pair of linked rectangles form a sub-subsurface
S′′⊂S′⊂S as in Figure 6.2-(centre) with connected boundary. If we cutS
along the curve∂S′′ and then cap oﬀ with two discs we perform the inverse
of a connected sum.
ThereforeS =S1#S2, whereS1 isS′′ with a disc attached,i.e. a torus as
Figure 6.2-(right) shows. The surfaceS2 decomposes into a 0-handle,k− 2
1-handles, and one 2-handle. We conclude by induction onk. □
6.1.3. Homology. The homology ofSg is easily calculated.
Proposition 6.1.7. We have
H0(Sg, Z) = Z, H 1(Sg, Z) = Z2g, H 2(Sg, Z) = Z.
Proof. SinceSg is closed, connected, and orientable, we haveH0(Sg) =
H2(Sg) = Z. Since χ(Sg) = 2 − 2g, the groupH1(Sg) has rank 2g. By
Poincaré dualityH1(Sg) =H1(Sg) = Hom(π1(Sg), Z) has no torsion. □
156 6. SURFACES
Figure 6.3. These 6 oriented curves represent a symplectic basis for
H1(S3, Z) = Z6.
Figure 6.4. The ﬁnite type surfaceSg,b,p.
Recall from Section 1.6.3 that by ﬁxing an orientation forSg we get a sym-
plectic intersection formω onH1(Sg, Z). A basis forH1(Sg, Z) is symplectic
ifω =
( 0 Ig
−Ig 0
)
with respect to this basis: an example is in Figure 6.3.
The algebraic intersectionof two closed curves is the intersection form of
their classes inH1(Sg, Z); if the curves are transverse, this is just the algebraic
sum of their intersections, where each intersection counts as±1 according to
the local orientations.
6.1.4. Surfaces of ﬁnite type.We extend our investigation to a larger
interesting class of surfaces.
Deﬁnition 6.1.8. Letg,b,p > 0 be three natural numbers. Thesurface of
ﬁnite typeSg,b,p is the surface obtained fromSg by removing the interior of
b disjoint discs andp points.
See Figure 6.4. We say thatSg,b,p has genusg, hasb boundary compo-
nents, andp punctures. Its Euler characteristic is
χ(Sg,b,p ) = 2− 2g−b−p.
We also use the notationSg,b to indicateSg,b,0.
Proposition6.1.9. Everycompactconnectedorientablesurfacewithbound-
ary is diﬀeomorphic toSg,b for someg,b > 0.
