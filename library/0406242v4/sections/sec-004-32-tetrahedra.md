---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-004-32-tetrahedra
section_title: "Tetrahedra"
section_number: 3.2
pages: 5-6
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Tetrahedra
As before, let ϕ be an element of SL2(Z) with two distinct eigenvalues in R∗
+. In the
proof of Proposition 2.1, we introduced the triangles t0, t1, . . . crossed by the axis D
of ϕ. In view of the above, this yields a nonbacktracking path of diagonal exchanges
between some triangulation (associated to t0) and its pushforward by ϕ (associated to
tm).
More precisely, when the oriented line D crosses an edge e of the Farey tessellation,
e comes with a transverse orientation.
So we can deﬁne the top (resp. bottom)
triangulation τ+(e) (resp. τ−(e)) of the punctured torus T as being the one associated
with the Farey triangle crossed just after (resp. before) the edge e. A diagonal exchange
separates the triangulations τ−(e) and τ+(e). An ideal tetrahedron is by deﬁnition a
space diffeomorphic to an ideal hyperbolic tetrahedron (topologically it is a compact
tetrahedron with its vertices removed). We can immerse such an ideal tetrahedron ∆(e)
in T × R: the boundary of the immersed ∆(e) is made up of two pleated surfaces (top
and bottom) homotopic to T and triangulated according to τ+(e) and τ−(e) respectively
Geometry & Topology 10 (2006)
1244
Franc¸ois Gu´eritaud and David Futer
Figure 1: Four copies of ∆(e) in the cover (R2∖Z2) × R of T × R
(Figure 1). The immersion is an embedding on the interior of ∆(e), but two pairs of
opposite edges undergo identiﬁcations.
Next, if D crosses the Farey edges ei, ei+1, . . . , we can glue the top of the tetrahedron
∆i := ∆(ei) onto the bottom of ∆i+1 in T × R, because τ+(ei) = τ−(ei+1). We
thus get a bi-inﬁnite stack of tetrahedra (∆i)i∈Z. For any nonnegative N the space
UN := SN
i=−N ∆i is a strong deformation retraction of T × R. For N large enough,
UN is homeomorphic to T × [0, 1]: the only way this can fail is if all the ∆i for
−N ≤i ≤N have a common edge; but any edge of any tetrahedron ∆j is shared
by only ﬁnitely many other (consecutive) ∆i’s, because for any Farey vertex v, only
ﬁnitely many of the Farey edges ei bound triangles with v as a vertex (and these ei are
consecutive). Therefore, the space U = S
i∈Z ∆i is homeomorphic to T × R. If m is
the period of the word Ω, there is an orientation-preserving homeomorphism Φ of U,
acting like [ϕ] on the T –factor, that sends ∆i to ∆i+m for all i. The quotient U/Φ is a
manifold (homeomorphic to) Vϕ, naturally triangulated into m ideal tetrahedra.
Figure 2 also shows a way to interpret the standard transvection matrices R and L
directly as adjunctions of new tetrahedra (by performing diagonal exchanges on the top
faces). Similarly, to topologically triangulate a general pseudo-Anosov surface bundle,
we can always go by diagonal exchanges from some triangulation (of the surface) to its
pushforward by the monodromy map, an idea usually credited to Casson.
