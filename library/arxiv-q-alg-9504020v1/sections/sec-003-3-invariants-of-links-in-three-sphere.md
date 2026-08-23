---
doc_id: arxiv-q-alg-9504020v1
doc_title: "A link invariant from quantum dilogarithm"
section_id: sec-003-3-invariants-of-links-in-three-sphere
section_title: "Invariants of Links in Three-Sphere"
section_number: 3
pages: 4-5
source_pdf: 9504020v1.pdf
source_sha256: 0baef40fa9934c91
doc_brief: "A link invariant from quantum dilogarithm — The link invariant, arising from the cyclic quantum dilogarithm via the particular R-matrix construction, is proved to coincide with the invariant of"
---
Let linkL inS3 is given by a two-strand tangle. Consider some non-singular (i.e.
with only simple intersection points) planar projection of this tangle. Denote by
V,E,F the sets of vertices, edges, and faces, respectively, in the planar graph.
We will write v ∈f , for some vertex v and face f ifv lies in the boundary of f .
There are two distinguished elements e1 and e2 inE, corresponding to the two
strands of the tangle, and one distinguished element f0 in F , corresponding to
the outer region in the plane. Deﬁne the following two maps:
j:E →ZN, a :V ×F →ZN, (3.1)
where we identiﬁed ZN with the set {0,...,N − 1}. Impose the restrictions on
j:
j(e1) = j(e2) = 0, (3.2)
and on a:
a(v,f 0) = 0; v ⁄∈f ⇒a(v,f ) = 0, v ∈V ;f ∈F, (3.3)
∑
f ∈F
a(v,f ) =
∑
v∈V
a(v,f ) = 1, f ⁄=f0. (3.4)
Using these maps, associate with each vertex the Boltzmann w eight according
to Sect. 2. This gives us one more map:
rj,a :V →C. (3.5)
Consider now the “partition” function:
⟨L⟩ =
∑
j
∏
v∈V
rj,a (v)
∏
e∈E
ω j(e). (3.6)
3
Theorem 1 (1) The quantity ⟨L⟩N is an ambient isotopy invariant of the link
L in three-sphere; (2) for odd N the following equality holds:
⟨L⟩N =Q(S3,L ), (3.7)
whereQ(M,L ) is the invariant of triangulated link L in three-manifold M de-
ﬁned in [14].
The ﬁrst part of the theorem is a consequence of the identitie s, satisﬁed by
the R-symbols (see Sect. 2). There is a freedom in choosing the sec ond map in
(3.1). In fact, diﬀerent choices lead to one and the same parti tion function (3.6)
up to N -th roots of unity. Note that the face indices are nothing els e but the
angle dependent data, corresponding to “enhanced” vertex m odels [4, 13, 19].
This becomes evident after Fourier transformation over the edge indices. The
face index - angle correspondence is described by the formul a:
φ =π − 2πa, (3.8)
where φ is the angle between the adjoining straight edges in the diag ram, cor-
responding to R-symbol (see Sect. 2), and a is the face index associated with
the sector bounded by these edges.
The proof of the second part of the theorem is given in the next section.
Note that the two strand tangle representation of links has b een used in [16]
to construct the state sum for Alexander-Conway polynomial [1, 7], because the
latter is zero for disjoint union of links. This is also true f or the invariant (3.6):
⟨L1 ⊔L2⟩ = 0. (3.9)
In the language of quantum group theory, property (3.9) reﬂe cts the vanishing
quantum dimension. In the three-dimensional deﬁnition giv en in [14] ( see also
the next section) no tangle description is needed.
