---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-020-a2-the-ideal-triangulation
section_title: "A.2 The ideal triangulation"
section_number: null
pages: 31-34
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
The ideal triangulation
The word Ωdescribes a monodromy triangulation of the product region S×I, in exactly
the same fashion as for 4–punctured sphere bundles. In fact, because this product
region is the complement of a braid in the part of S3 bounded by the two pillowcases,
we can locate the edges of the triangulation concretely in the projection diagram.
Let c = Pn
i=1 ai be the length of Ω. Each letter Ωi (1 ≤i ≤c), and thus each crossing
in the alternating braid, corresponds to a 4–punctured sphere Si ⊂S3∖K, with the four
strands of K seen in Figure 14 passing through the four punctures. The braid induces
an ideal triangulation on each Si, whose edges come from arcs in the diagram that look
vertical and horizontal immediately before and/or after the corresponding crossing. See
Figure 15.
Geometry & Topology 10 (2006)
1270
Franc¸ois Gu´eritaud and David Futer
Figure 15: Two views of the same 4–punctured sphere Si living near a crossing in the link
diagram (arcs with the same dashing pattern have the same slope)
Just as with punctured torus bundles, we can locate the progressively changing tri-
angulations in the Farey tesselation F. Each triangulation of a 4–punctured sphere
Si, containing six edges of three different slopes, corresponds to a Farey triangle ti.
Triangles ti and ti+1 share an edge ei, whose endpoints are the shared slopes of Si and
Si+1. If Ωi = R, the path from ei−1 to ei takes a right turn across ti; if Ωi = L, the
path takes a left turn. This rule also deﬁnes an initial edge e0, because Ω1 = R, so a
right turn should take e0 to e1. Similarly, the action of Ωc deﬁnes a terminal edge ec.
For each ei, 1 ≤i ≤c −1, the 4–punctured spheres Si and Si+1 are joined together
along four edges, two for each endpoint of ei. In between them lies a layer ∆i = ∆(ei)
of two tetrahedra, whose bottom surface Si has the triangulation of ti and whose top
surface Si+1 has the triangulation of ti+1. (See Figure 16 for an example.) Stacking
these tetrahedron layers together produces a layered triangulation of the product region
between S1 and Sc.
Figure 16: The tetrahedron layer ∆1 = ∆(e1), made of two tetrahedra contained between
4–punctured spheres S1 and S2 (sides with identical arrows are identiﬁed)
If we wanted to construct a bundle of 4–punctured spheres over the circle, we would
glue the top of this product region to the bottom. To recover the complement of the
link K(Ω), we follow a slightly different procedure. On the 4–punctured sphere S1,
corresponding to the ﬁrst crossing inside the outer pillowcase, let the peripheral edges
be the edges whose slope is the vertex of t1 opposite the initial edge e0.
We will fold S1 along the two peripheral edges, identifying its ideal triangles in pairs.
Geometry & Topology 10 (2006)
Canonical triangulations
1271
Figure 17 shows that this creates exactly the desired effect of connecting the strands
of K in pairs, with a twist. This full twist corresponds to the ﬁrst two crossings in the
link projection: the ﬁrst crossing in the braid, as well as the “extra” crossing outside
the outer pillowcase. The four nonperipheral edges on S1 are identiﬁed to a single
edge, isotopic to a short arc near the crossing. The two ideal triangles that remain after
folding are clasped together around this edge, which we call the core of the clasp.
⇒
⇓
isotopy
⇐
Figure 17: Folding the pleated surface S1 produces the ﬁrst two crossings in the link.
Let α be the mirror image of the peripheral slope across e0 in the Farey graph.
Topologically, folding S1 as above amounts to attaching a thickened disk of boundary
slope α to the outer pillowcase [23, Lemma II.2.5].
In a similar fashion, we deﬁne the peripheral edges on Sc to be the edges whose slope
is the vertex of tc opposite ec. We fold Sc along these two peripheral edges, identifying
its faces to a clasp of two ideal triangles. Topologically, attaching 2–handles to S1 and
Sc results in a space homeomorphic to the link complement. Combinatorially, folding
S1 and Sc deﬁnes a gluing pattern for all the faces of the tetrahedra, giving us an ideal
triangulation of S3∖K. See [23, Section II.2] for more details of this triangulation.
Geometry & Topology 10 (2006)
1272 Francois Guéritaud and David Futer
